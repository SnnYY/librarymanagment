CREATE TABLE auth(
	id varchar(30) primary key,
	password varchar(30),
	status varchar(10) DEFAULT 'student'
);

DROP TABLE auth

INSERT INTO auth (id,password,status) VALUES ('admin','admin','admin')
INSERT INTO auth (id,password) VALUES ('180444034','barris')
INSERT INTO auth VALUES (id,password) VALUES ('180444035','yilmaz')

SELECT * FROM auth

SELECT * FROM auth WHERE id = '180444034'

select * from books_issued WHERE student_number = '180444034'

CREATE TABLE books(
	bid varchar(30) primary key,
	title varchar(30),
	author varchar(30),
	status varchar(10) DEFAULT 'Open',
);

INSERT INTO books (bid,title,author)  VALUES ('213322','Tehlikeli Oyunlar','Oðuz Atay'),('213232','HARRY POTTER','JKR'),('232323','Tutunamayanlar','Oðuz Atay')
SELECT * FROM books
DROP TABLE books

CREATE TABLE books_issued(
	bid varchar(30) primary key,
	student_number varchar(30),
	taken_date date,
	return_date date
);

INSERT INTO books_issued (bid,student_number,taken_date,return_date) VALUES ('213232','180444035','2021-12-26','2021-12-25')
INSERT INTO books_issued (bid,student_number,taken_date,return_date) VALUES ('213233','180444034','2021-12-26','2021-12-30')

SELECT * FROM books_issued;

DROP TABLE books_issued

SELECT * FROM books_issued WHERE return_date < GETDATE() ORDER BY return_date DESC 



SELECT status FROM books WHERE bid = 212252