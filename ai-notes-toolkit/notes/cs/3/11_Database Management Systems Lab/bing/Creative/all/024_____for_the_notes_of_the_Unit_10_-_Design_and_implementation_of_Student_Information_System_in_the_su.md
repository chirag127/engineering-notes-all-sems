# Unit 10 - Design and implementation of Student Information System in the subject of Database Management Systems Lab

## Introduction

A Student Information System (SIS) is a software application that manages the data related to students, such as their personal details, academic records, attendance, fees, courses, grades, etc. A SIS can help in improving the efficiency and effectiveness of the educational process, as well as providing better services to students and stakeholders.

## Objectives

The objectives of this unit are to:

- Understand the basic concepts and principles of database design and development
- Learn how to use ER diagrams to model the data requirements of a SIS
- Learn how to use SQL to create and manipulate tables, queries, views, and stored procedures for a SIS
- Learn how to use Microsoft Access as a tool for implementing and testing a SIS

## Database Design

Database design is the process of defining the structure, organization, and relationships of the data that will be stored in a database. Database design involves the following steps:

- Identify the entities and attributes that are relevant to the problem domain
- Identify the relationships and constraints among the entities and attributes
- Draw an ER diagram to represent the conceptual model of the data
- Normalize the data to reduce redundancy and anomalies
- Translate the ER diagram into a relational schema
- Choose appropriate data types and constraints for the attributes
- Implement the relational schema in a DBMS

## ER Diagram for SIS

An ER diagram is a graphical representation of the entities, attributes, and relationships in a database. An ER diagram for a SIS can be drawn as follows:

![ER diagram for SIS](https://itsourcecode.com/wp-content/uploads/2021/09/ER-Diagram-for-Student-Management-System-Database-Design.png)

The ER diagram shows the following entities and their attributes:

- Student: This entity represents a student who is enrolled in the institution. The attributes are StudentID, FirstName, LastName, Gender, DateOfBirth, Address, Phone, Email, and CourseID.
- Course: This entity represents a course that is offered by the institution. The attributes are CourseID, CourseName, Duration, and Fee.
- Enrollment: This entity represents the enrollment of a student in a course. The attributes are EnrollmentID, StudentID, CourseID, DateEnrolled, and Status.
- Attendance: This entity represents the attendance of a student in a course. The attributes are AttendanceID, EnrollmentID, Date, and Present.
- Grade: This entity represents the grade of a student in a course. The attributes are GradeID, EnrollmentID, ExamType, Score, and Grade.

The ER diagram also shows the following relationships and constraints:

- A student can enroll in one or more courses, and a course can have one or more students enrolled. This is a many-to-many relationship, which is resolved by creating the Enrollment entity.
- A student can have one or more enrollments, and an enrollment belongs to one student. This is a one-to-many relationship, which is represented by a foreign key StudentID in the Enrollment entity.
- A course can have one or more enrollments, and an enrollment belongs to one course. This is a one-to-many relationship, which is represented by a foreign key CourseID in the Enrollment entity.
- An enrollment can have one or more attendances, and an attendance belongs to one enrollment. This is a one-to-many relationship, which is represented by a foreign key EnrollmentID in the Attendance entity.
- An enrollment can have one or more grades, and a grade belongs to one enrollment. This is a one-to-many relationship, which is represented by a foreign key EnrollmentID in the Grade entity.
- The primary keys of the entities are StudentID, CourseID, EnrollmentID, AttendanceID, and GradeID, which are underlined in the ER diagram. The primary keys are unique and not null identifiers of the entities.
- The foreign keys of the entities are StudentID, CourseID, and EnrollmentID, which are italicized in the ER diagram. The foreign keys are references to the primary keys of other entities, and they enforce the referential integrity of the relationships.

## SQL for SIS

SQL is a standard language for creating and manipulating databases. SQL can be used to perform the following tasks for a SIS:

- Create tables to store the data of the entities
- Insert data into the tables
- Query data from the tables
- Update data in the tables
- Delete data from the tables
- Create views to simplify the access to the data
- Create stored procedures to automate the execution of SQL statements