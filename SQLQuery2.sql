
USE master;  --Use Master Database
GO  

IF DB_ID (N'AcademicControlSystem') IS NOT NULL  
DROP DATABASE AcademicControlSystem;  
GO  

CREATE DATABASE AcademicControlSystem;
GO

use AcademicControlSystem;
go


-- Create Course table 
CREATE TABLE Course(
	CID int PRIMARY KEY ,
	Cname varchar(10) ,
);
go

-- Create Instructor table 
CREATE TABLE Instructor(
	ID int PRIMARY KEY ,
	[Password] varchar(10) ,

);
go
-- Create Admin table 
CREATE TABLE [Admin](
	ID int PRIMARY KEY ,
	[Password] varchar(10) ,

);
go
-- Create Student table 
CREATE TABLE Student(
	ID int PRIMARY KEY ,
	[Password] varchar(10) ,
	grade float 
);
go


-- Create Student_Class table  
CREATE TABLE Student_Class(
	StudentID int ,
	CourseID int,
	PRIMARY KEY (StudentID,CourseID)

);

go























