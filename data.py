from flask import *
import os
import datetime
from flask_mysqldb import MySQL 

app = Flask(__name__)
app.secret_key=os.urandom(34)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pushpa@123'
app.config['MYSQL_DB'] = 'event_management'
mysql = MySQL(app)

#welcome screeen
@app.route('/')
def master():
	return render_template('master.html')


@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/usernameCheck',methods=['GET','POST'])
def usernameCheck():
	if request.method=='POST':
		userId = request.form['userId']
		cur = mysql.connection.cursor()
		cur.execute('SELECT USER_ID FROM USERS WHERE USER_ID=%s',[userId])
		user=cur.fetchone()
		message=False
		if user is not None:
			message=False
		else:
			message=True
		return jsonify({"message":message})


@app.route('/registerUser',methods=['GET','POST'])
def registerUser():
	if request.method=='POST':
		fullname = request.form['fullname']
		phone = request.form['phone']
		userId = request.form['userId']
		password = request.form['password']
		email = request.form['email']
		address = request.form['address']
		connection = mysql.connection
		cur=connection.cursor()
		cur.execute('INSERT into USERS VALUES (%s,%s,%s,%s,%s,%s)',[userId,fullname,email,password,phone,address])
		connection.commit()
		return render_template('login.html')

@app.route('/feedback',methods=['GET','POST'])
def feedback():
	if request.method=='POST':
		comment = request.form['comment']
		connection = mysql.connection
		cur=connection.cursor()
		status = cur.execute('INSERT INTO FEEDBACK (USER_ID,COMMENTS) VALUES (%s,%s)',[session.get('username'),comment])
		response =""
		if(status>0):
			response += "Comment Posted"
		else:
			response += "Error occured"
		connection.commit()
		return jsonify({"response":response})
			
@app.route('/login')
def login():
	if 'username' in session:
		return redirect(url_for('home'))
	else:
		return render_template('login.html')
@app.route('/logout')
def logout():
	session.pop('username',None)
	session.clear()
	return redirect(url_for('login'))

@app.route('/home')
def home():
	if 'username' in session:
		cur = mysql.connection.cursor()
		cur.execute('SELECT booking.booking_id ,event.event_name,booking.booking_date, booking.location, booking.total_price, CASE WHEN pay.amount>0 or pay.amount!=null THEN pay.amount ELSE 0 END AS amount FROM  bookings booking  join events event on booking.event_id=event.event_id left join payments pay on pay.booking_id=booking.booking_id where user_id=%s',[session.get('username')])
		bookingData=cur.fetchall()
		return render_template('home.html',bookingData=bookingData)
	else:
		return redirect(url_for('login'))

@app.route('/logincheck',methods=['GET','POST'])
def index():
	if 'username' in session:
		return redirect(url_for('home'))
	else:
		if request.method=='POST':
			username=request.form['userid']
			password=request.form['password']
			cur = mysql.connection.cursor()
			cur.execute('SELECT user_id FROM users where user_id=%s and password=%s',[username,password])
			data=cur.fetchone()
			if data is not None:
				try:
					if(len(data)>0):
						session['username']=username
						app.permanent_session_lifetime=datetime.timedelta(minutes=20)
						session.modified=True
						session['message']="Welcome "+username
						return redirect(url_for('home'))
					else:
						return render_template('login.html',error="Error Occurred")
				except Exception:
					return render_template('login.html',error="Error Occured")
			else:
				return render_template('login.html',error="Invalid User Details")
				
@app.route('/events',methods=['GET','POST'])
def events():
	if 'username' in session:
		cur = mysql.connection.cursor()
		cur.execute('SELECT * FROM EVENTS',)
		eventsData=cur.fetchall()	
		return render_template('events.html',eventsData=eventsData)
	else:
		return redirect(url_for('login'))

@app.route('/bookEvent',methods=['GET','POST'])
def bookEvent():
	if 'username' in session:

		if request.method=='POST':
			userId=session.get('username')
			eventId=request.form['eventId']
			location=request.form['eventLocation']
			eventDate=request.form['bookingDate']
			if location !="" and eventDate !="":
				connection = mysql.connection
				cur=connection.cursor()
				bookingDate=datetime.datetime.strptime(eventDate,"%Y-%m-%d")
				todayDate=datetime.datetime.today()
				if((todayDate+datetime.timedelta(days=7))<=bookingDate and bookingDate<=todayDate+datetime.timedelta(days=30)):
					result = cur.execute('INSERT into BOOKINGS (USER_ID, EVENT_ID, BOOKING_DATE, LOCATION, TOTAL_PRICE) VALUES (%s,%s,%s,%s,(SELECT PRICE FROM EVENTS WHERE EVENT_ID=%s))',[userId,eventId,bookingDate,location,eventId])
					connection.commit()
					if(result>0):
						session['message'] = "Event Booking Success..."
						return redirect(url_for('home'))
		session['message'] = "Event Booking Failed. Please Try Again..."
		return redirect(url_for('events'))
	else:
		return redirect(url_for('login'))

@app.route('/payment')
def payment():
	cur = mysql.connection.cursor()
	cur.execute('SELECT BOOKING_ID FROM BOOKINGS WHERE USER_ID=%s',[session.get('username')])
	bookings=cur.fetchall()	
	return render_template('payment.html',bookings=bookings)	

@app.route('/doPayment',methods=['GET','POST'])
def doPayment():
	if 'username' in session:
		if request.method=='POST':
			amount = int(request.form['amount'])
			bookingId = request.form["bookedId"]
			todayDate=datetime.datetime.today()
			if amount !="" and bookingId!="":
				connection = mysql.connection
				cur=connection.cursor()
				cur.execute('SELECT CASE WHEN pay.amount>0 or pay.amount!=null  THEN pay.amount ELSE 0 END AS amount,BOOKING.TOTAL_PRICE FROM  BOOKINGS BOOKING LEFT JOIN PAYMENTS PAY ON PAY.BOOKING_ID= BOOKING.BOOKING_ID WHERE  BOOKING.BOOKING_ID=%s',[bookingId])
				paymentfetch =cur.fetchone()
				if paymentfetch is not None:
					amountPaid=int(paymentfetch[0])
					totalAmount=int(paymentfetch[1])
					if amount+amountPaid <=totalAmount:
						if amountPaid==0:
							status = cur.execute('INSERT INTO PAYMENTS (BOOKING_ID, AMOUNT, PAYMENT_DATE) VALUES (%s,%s,%s)',[bookingId,amount,todayDate])
							connection.commit()
						else:
							status=cur.execute('UPDATE PAYMENTS SET AMOUNT=%s WHERE BOOKING_ID=%s',[amount+amountPaid,bookingId])
							connection.commit()
							if(status>0):
								session['message'] = "Payment Success..."
								return redirect(url_for('home'))
							else:
								session['message'] = "Payment Unsuccess..."
					else:
						session['message'] = "You need to pay only "+str(totalAmount+amountPaid)
				else:
					session['message'] = "Error occured. Sorry..."
			else:
				session['message'] = "Fields are Empty"
				
		return redirect(url_for('payment'))
	else:
		return redirect(url_for('login'))	

if __name__ == '__main__':
	app.run(debug=True)