# Unit 10 - Design and implementation of Student Information System in the subject of Database Management Systems Lab

## Introduction

A Student Information System (SIS) is a software that is designed to manage all data related to students right from the day they join in until they graduate. It can store and process information such as student personal details, academic records, attendance, fees, courses, grades, etc. A SIS can also provide various functions such as enrollment, registration, scheduling, reporting, communication, etc.

## Database Design

A database is a collection of data that is organized and structured in a way that allows easy access, retrieval, modification, and analysis. A database design is the process of defining the logical and physical structure of the database, as well as the relationships and constraints among the data elements. A database design can be represented using different models, such as Entity-Relationship (ER) diagrams, Relational models, etc.

An ER diagram is a graphical representation of the entities, attributes, and relationships in a database. An entity is a real-world object or concept that can be identified uniquely, such as a student, a course, a department, etc. An attribute is a property or characteristic of an entity, such as name, age, address, etc. A relationship is an association or link between two or more entities, such as a student enrolls in a course, a course belongs to a department, etc.

A relational model is a representation of the database using tables, columns, and rows. A table is a collection of data about a specific entity or relationship, such as a student table, a course table, a enrollment table, etc. A column is a data element that describes an attribute of the entity or relationship, such as student_id, course_id, grade, etc. A row is a record that contains the values for each column, such as (101, John, CS, 3.5), (102, Mary, EE, 4.0), etc.

## Example of SIS Database Design

Based on the web search results, an example of a SIS database design using ER diagram and relational model is shown below. Note that this is not the only possible design, and different SIS may have different requirements and specifications.

### ER Diagram

![ER Diagram for SIS](https://itsourcecode.com/wp-content/uploads/2021/09/ER-Diagram-for-Student-Management-System-Database-Design.png)

The ER diagram above shows the following entities and attributes:

- Student: student_id, name, address, phone, email, gender, dob, department_id
- Department: department_id, name, head, phone, email
- Course: course_id, name, description, credits, department_id
- Enrollment: student_id, course_id, semester, year, grade
- Fee: student_id, semester, year, amount, status

The ER diagram also shows the following relationships and cardinalities:

- A student belongs to one department, and a department has many students. This is a one-to-many relationship, denoted by 1 and N on the ER diagram.
- A course belongs to one department, and a department offers many courses. This is also a one-to-many relationship, denoted by 1 and N on the ER diagram.
- A student enrolls in many courses, and a course has many students enrolled. This is a many-to-many relationship, denoted by N and M on the ER diagram. This relationship also has attributes such as semester, year, and grade, which are specific to each enrollment instance.
- A student pays fee for each semester and year, and a fee record is associated with one student, semester, and year. This is a one-to-one relationship, denoted by 1 and 1 on the ER diagram.

### Relational Model

Based on the ER diagram, the relational model for the SIS database can be represented using the following tables and columns:

- Student (student_id, name, address, phone, email, gender, dob, department_id)
- Department (department_id, name, head, phone, email)
- Course (course_id, name, description, credits, department_id)
- Enrollment (student_id, course_id, semester, year, grade)
- Fee (student_id, semester, year, amount, status)

The primary keys of each table are underlined, and the foreign keys are italicized. A primary key is a column or a combination of columns that uniquely identifies each row in a table. A foreign key is a column or a combination of columns that references the primary key of another