CREATE DATABASE flash_db;
USE flash_db;

CREATE TABLE student(
    id int(10) NOT NULL auto_increment PRIMARY KEY,
    fname VARCHAR(100) NOT NULL,
    lname VARCHAR(100) NOT NULL,
    phone VARCHAR(100) NOT NULL
);
