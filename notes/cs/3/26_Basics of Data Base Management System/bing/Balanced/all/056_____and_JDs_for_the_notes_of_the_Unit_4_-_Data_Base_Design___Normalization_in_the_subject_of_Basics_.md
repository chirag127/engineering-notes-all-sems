# Unit 4 - Database Design and Normalization

## Database Design
- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database system.
- Database design involves identifying the data requirements, defining the entities and attributes, determining the relationships and constraints, and choosing the appropriate data model and storage format.
- Database design aims to achieve the following objectives:
  - Accurately represent the real-world domain and its rules.
  - Ensure data integrity, consistency, and quality.
  - Support efficient and secure data access and manipulation.
  - Facilitate data maintenance and evolution.
  - Minimize data redundancy and anomalies.

## Database Normalization
- Database normalization is a database schema design technique, by which an existing schema is modified to minimize redundancy and dependency of data.
- Normalization splits a large table into smaller tables and defines relationships between them to increase the clarity in organizing data.
- Normalization helps in improving the overall design of the database, making it easier to maintain, query, and update.
- Normalization also makes the database more flexible and adaptable to changing business needs.
- Normalization is based on a set of rules or forms, each of which is a refinement of the previous one. The most common forms are:
  - First Normal Form (1NF): A table is in 1NF if it contains only atomic values and no repeating groups of attributes.
  - Second Normal Form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key.
  - Third Normal Form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key.
  - Boyce-Codd Normal Form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key.
  - Fourth Normal Form (4NF): A table is in 4NF if it is in BCNF and has no multi-valued dependencies.
  - Fifth Normal Form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies.

## Database Design and Normalization Example
- Suppose we have a table called Student_Course that stores the information of students and the courses they enroll in:

| Student_ID | Student_Name | Course_ID | Course_Name | Instructor_ID | Instructor_Name |
|------------|--------------|-----------|-------------|---------------|-----------------|
| 101        | Alice        | CS101     | Programming | 1001          | Bob             |
| 101        | Alice        | CS102     | Database    | 1002          | Carol           |
| 102        | David        | CS101     | Programming | 1001          | Bob             |
| 103        | Eve          | CS102     | Database    | 1002          | Carol           |

- This table is not in 1NF, because it has repeating groups of attributes (Course_ID, Course_Name, Instructor_ID, Instructor_Name) for each student.
- To convert it to 1NF, we can create a new table called Enrollment that stores the relationship between students and courses, and remove the repeating attributes from the Student_Course table:

| Student_ID | Student_Name |
|------------|--------------|
| 101        | Alice        |
| 102        | David        |
| 103        | Eve          |

| Course_ID | Course_Name | Instructor_ID | Instructor_Name |
|-----------|-------------|---------------|-----------------|
| CS101     | Programming | 1001          | Bob             |
| CS102     | Database    | 1002          | Carol           |

| Student_ID | Course_ID |
|------------|-----------|
| 101        | CS101     |
| 101        | CS102     |
| 102        | CS101     |
| 103        | CS102     |

- The Student_Course table is now in 1NF, but not in 2NF, because the non-key attributes (Student_Name, Course_Name, Instructor_Name) are not fully dependent on the primary key (Student_ID, Course_ID), but only on part of it.
- To convert it to 2NF, we can create separate tables for Student, Course, and Instructor, and use foreign keys to reference them in the Enrollment table:

| Student_ID | Student_Name |
|------------|--------------|
| 101        | Alice        |
| 102        |