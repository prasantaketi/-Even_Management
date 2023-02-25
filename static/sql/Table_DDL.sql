DROP DATABASE EVENT_MANAGEMENT;
CREATE DATABASE IF NOT EXISTS event_management;
use event_management;

create table users (user_id  varchar(30) not null, full_name varchar(30) not null, email varchar(50), 
password varchar(40) not null, phone_no varchar(10) not null, address varchar(70),
primary key(user_id), unique(email),unique(phone_no));

create table events (event_id  int auto_increment, event_name varchar(30) not null, event_desc varchar(10000), 
price int not null,primary key(event_id), unique(event_name));
ALTER TABLE events AUTO_INCREMENT=100;

create table bookings (booking_id int auto_increment, user_id varchar(30) not null, event_id int, 
booking_date date not null, location varchar(30) not null, total_price int default 0, amount_paid int default 0,
key(booking_id), foreign key (user_id) references users(user_id), foreign key (event_id) references
events(event_id));
ALTER TABLE bookings AUTO_INCREMENT=700;

create table feedback (comment_id int auto_increment,user_id  varchar(30) not null, comments varchar(200) not null, primary key(comment_id), foreign key (user_id) references users(user_id));
ALTER TABLE feedback AUTO_INCREMENT=1000;

create table payments (payment_id int auto_increment,booking_id int not null,amount int not null,payment_date date not null ,primary key(payment_id)
, foreign key (booking_id) references bookings(booking_id));
ALTER TABLE payments AUTO_INCREMENT=5000;

INSERT INTO USERS VALUES ('pushpa','PushpaLatha','pushpalatha@gmail.com','pushpa',9876543211,'Banglore');
INSERT INTO USERS VALUES ('shalini','Shalini M','shalinim@gmail.com','shalini',9876543233,'Banglore');

INSERT INTO EVENTS (event_name,event_desc,price) VALUES('Birthday', 'Cake(3kg), Decoration(Based on themes), Invitations, Entertainment Programs, Snaps, Music, Party games, Catering', 20000);
INSERT INTO EVENTS (event_name,event_desc,price) VALUES('Wedding', 'Haldi, Sangeeth, Mehendi, Makeup, Decorations, Dance, Catering(Breakfast, Lunch, Dinner), Complete Event Video & Photgraphs', 300000);
INSERT INTO EVENTS (event_name,event_desc,price) VALUES('Party', 'Decorations, Music, Welcome Drinks, Snacks, Party, Catering, Photo Booth, Entertainment Programs', 200000);
INSERT INTO EVENTS (event_name,event_desc,price) VALUES('Recepiton', 'Stage Decoration, Makeup, Music and Dance, Catering', 250000);
INSERT INTO EVENTS (event_name,event_desc,price) VALUES('Inaugration', 'Decoration, Welcoming Guests, Drinks, Snacks Catering, Photographs', 150000);
INSERT INTO EVENTS (event_name,event_desc,price) VALUES('Anniversary', 'Cake(3kg), Decoration, Invitations, Catering, Entertaiment Programs', 200000);
