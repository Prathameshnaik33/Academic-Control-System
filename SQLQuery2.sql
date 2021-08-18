
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

CREATE TABLE Course_Profile(
	Profile_ID INT PRIMARY KEY,
	Course_ID int FOREIGN KEY REFERENCES Course(CID),
	Student_ID int ,
	Instructor_ID INT, 
	constraint fk_Instructor foreign key (Instructor_ID )
               references Instructor(ID),
    constraint fk_Student foreign key (Student_ID )
               references Student(ID)
	);
go


-- Create Student_Class table  
CREATE TABLE Student_Class(
	StudentID int ,
	CourseID int,
	PRIMARY KEY (StudentID,CourseID)

);

go























