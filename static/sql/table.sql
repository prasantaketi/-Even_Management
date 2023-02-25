CREATE DATABASE IF NOT EXISTS event_management;
use event_management;
create table users (user_id  varchar(30) not null, full_name varchar(30) not null, email varchar(50), 
password varchar(40) not null, phone_no varchar(10) not null, address varchar(70),
primary key(user_id), unique(email),unique(phone_no));

create table events (event_id  int auto_increment, event_name varchar(30) not null, event_desc varchar(1000), 
price int not null,primary key(event_id), unique(event_name));
ALTER TABLE events AUTO_INCREMENT=100;

create table bookings (booking_id int auto_increment, user_id varchar(30) not null, event_id int, 
booking_date date not null, location varchar(30) not null, total_price int default 0, amount_paid int default 0,
primary key(booking_id), foreign key (user_id) references users(user_id), foreign key (event_id) references
events(event_id));

ALTER TABLE bookings AUTO_INCREMENT=700;

insert into users values ('pushpa','PushpaLatha','pushpalatha@gmail.com','pushpa',9876543211,'banglore');

insert into events (event_name,event_desc,price) values('Birthday', 'cake cutting, ballons, chocolates', 15000);
insert into events (event_name,event_desc,price) values('wedding', 'cake cutting, ballons, chocolates', 15000);
insert into events (event_name,event_desc,price) values('party', 'cake cutting, ballons, chocolates', 15000);
insert into events (event_name,event_desc,price) values('recepiton', 'cake cutting, ballons, chocolates', 15000);

insert into bookings (user_id, event_id, booking_date, location, total_price) values('prasanth_a', 
100, '2023-07-01','banglore','15000');
insert into bookings (user_id, event_id, booking_date, location, total_price) values('prasanth_a', 
100, '2023-07-01','banglore','16000');
insert into bookings (user_id, event_id, booking_date, location, total_price) values('pushpa', 
100, '2023-07-01','banglore','15000');

INSERT INTO BOOKINGS (USER_ID, EVENT_ID, BOOKING_DATE, LOCATION, TOTAL_PRICE) VALUES ('pushpa',100, '2023-07-01','banglore',(SELECT PRICE FROM EVENTS WHERE EVENT_ID=100));
