 create database SISDB;

use SISDB;

create table Student(
studentId int Identity(1,1) primary key,
firstName varchar(30) not null,
lastName varchar(30) not null,
dateOfBirth date not null,
email varchar(100) not null,
phoneNumber BIGINT);


create Table Course(
courseId int Identity(1,1) primary key,
courseName varchar(50),
courseCode varchar(10),
teacherId int,foreign key(teacherId) references Teacher(teacherId));

create Table Enrollment(
enrollmentId int Identity(1,1) primary key,
studentId int,courseId int,enrollmentDate date,
foreign key(studentId) references Student(studentId),
foreign key(courseId) references Course(courseId));

create Table Teacher(
teacherId int Identity(1,1) primary key,
firstName varchar(30),
lastName varchar(30),
email varchar(50));
drop table Teacher;
drop table Course;
drop table Enrollment;

create table Payment(
paymentId int Identity(1,1) primary key,
studentId int,
amount decimal,
paymentDate Datetime,
foreign key(studentId) references Student(studentId));


insert into Student(firstName,lastName,dateOfBirth,email,phoneNumber) values

('Emily', 'Chen', '1999-02-15', 'emilyc@gmail.com', 1234567890),
('Ryan', 'Thompson', '2001-10-22', 'ryan.t@gmail.com', 9876543210),
('Priya','Singh','2000-08-12','psn@gmail.com',4567894321),
( 'Michael', 'Lee', '1998-05-10', 'mike.lee@yahoo.com', 7418529630),
('Sophia', 'Patel', '2002-01-05', 'sophia.patel@hotmail.com', 3692581470),
('David', 'Kim', '1997-09-20', 'david.kim@outlook.com', 8529637410),
('Olivia', 'Brown', '2000-04-15', 'olivia.brown@gmail.com', 1357924680),
('Ethan', 'Hall', '1999-11-25', 'ethan.hall@yahoo.com', 2468013579),
('Ava', 'Martin', '2001-06-01', 'ava.martin@hotmail.com', 9638527410),
('Liam', 'Davis', '1998-03-10', 'liam.davis@outlook.com', 5792468103);

select * from Student;

insert into Teacher(firstName,lastName,email) values
('Ram','Patel','ram@edu.in'),
('Curie','Joe','joe@school.in'),
('Sita','Singh','s@gmail.com'),
('Rama','Martin','rama@edu.org'),
('Raghu','Reddy','rr@email.com'),
('Vishwa','Sen','sen@school.edu'),
('Pavani','Rose','prose@school.org'),
('Anitha','Rathode','anitha@gmail.com'),
('Teju','Lee','lee@edu.in'),
('Nani','Saheb','nani@org.in');

select * from Teacher;

insert into Course(courseName,courseCode,teacherId) values
('English','E23',2),
('Maths','M2',5),
('Science','S1',6),
('C','C32',1),
('Python','P85',7),
('C++','C44',8),
('Java','J6',10),
('SQL','DB4',9),
('C#','C92',3),
('Skills','S1',4);

select * from Course;

insert into Enrollment(studentId,courseId,enrollmentDate) values
(1, 1, '2022-08-15'),
(2, 2, '2022-08-20'),
(3, 3, '2022-08-25'),
(4, 4, '2022-09-01'),
(5, 4, '2022-09-05'),
(6, 6, '2022-09-10'),
(7, 1, '2022-09-12'),
(8, 8, '2022-09-18'),
(9, 3, '2022-09-22'),
(10, 10, '2022-09-28');


insert into Payment(studentId,amount,paymentDate) values
(1, 1000.00, '2022-08-15'),
(2, 500.00, '2022-08-20'),
(3, 800.00, '2022-08-25'),
(4, 1200.00, '2022-09-01'),
(5, 900.00, '2022-09-05'),
(6, 600.00, '2022-09-10'),
(7, 1500.00, '2022-09-12'),
(8, 700.00, '2022-09-18'),
(9, 1100.00, '2022-09-22'),
(10, 1300.00, '2022-09-28');

select * from Enrollment;




select * from Payment;