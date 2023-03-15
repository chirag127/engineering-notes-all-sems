# Data Model Schema and Instances

- A data model is a collection of concepts and rules for describing the structure, meaning, and constraints of the data stored in a database.
- A schema is the formal description of the structure and organization of the data in a database. It defines the tables, columns, keys, relationships, and constraints of the data.
- An instance is the set of data stored in a database at a particular moment of time. It represents the current state and values of the data.
- A schema is static and does not change frequently, whereas an instance is dynamic and changes constantly as the data is inserted, updated, or deleted.
- A schema can be represented by a diagram or a text, whereas an instance can be represented by a table or a record.
- A schema can be of three types: logical, physical, and view. A logical schema describes the data in terms of its entities, attributes, and relationships. A physical schema describes how the data is stored and accessed in the database system. A view schema describes a subset or a projection of the data for a specific purpose or user.
- An example of a schema and an instance for a student database is shown below:

Logical schema:

Student (StudentID, Name, Major, GPA)
Course (CourseID, Title, Credits)
Enroll (StudentID, CourseID, Grade)

Physical schema:

Student: stored in a file named student.dat, with fixed-length records of 50 bytes each, and StudentID as the primary key.
Course: stored in a file named course.dat, with variable-length records of up to 100 bytes each, and CourseID as the primary key.
Enroll: stored in a file named enroll.dat, with fixed-length records of 20 bytes each, and (StudentID, CourseID) as the primary key.

View schema:

StudentView: a view of the Student table that shows only the Name and GPA of the students.
CourseView: a view of the Course table that shows only the Title and Credits of the courses.

Instance:

Student:

| StudentID | Name | Major | GPA |
|-----------|------|-------|-----|
| 1001 | Alice | CS | 3.8 |
| 1002 | Bob | Math | 3.5 |
| 1003 | Charlie | CS | 3.2 |

Course:

| CourseID | Title | Credits |
|----------|-------|---------|
| CS101 | Introduction to Programming | 4 |
| CS102 | Data Structures and Algorithms | 4 |
| MATH101 | Calculus I | 3 |

Enroll:

| StudentID | CourseID | Grade |
|-----------|----------|-------|
| 1001 | CS101 | A |
| 1001 | CS102 | B |
| 1002 | MATH101 | A |
| 1003 | CS101 | C |
| 1003 | CS102 | B |

StudentView:

| Name | GPA |
|------|-----|
| Alice | 3.8 |
| Bob | 3.5 |
| Charlie | 3.2 |

CourseView:

| Title | Credits |
|-------|---------|
| Introduction to Programming | 4 |
| Data Structures and Algorithms | 4 |
| Calculus I | 3 |