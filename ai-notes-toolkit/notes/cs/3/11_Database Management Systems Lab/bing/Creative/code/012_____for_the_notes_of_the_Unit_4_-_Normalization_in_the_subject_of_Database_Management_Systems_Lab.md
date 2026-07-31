# Unit 4 - Normalization in Database Management Systems Lab

Normalization is a technique to reduce data redundancy and improve data integrity in a database. It involves dividing a large table into smaller tables based on certain rules, and linking them using foreign keys. The main benefits of normalization are:

- It avoids anomalies, such as insertion, deletion, and update anomalies, that can cause inconsistency and duplication of data.
- It reduces the storage space required by eliminating redundant data.
- It enhances the performance of queries by simplifying the structure of tables and indexes.
- It facilitates the enforcement of referential integrity and data validation rules.

There are different levels of normalization, called normal forms, that a database can achieve. Each normal form has a set of criteria or conditions that must be satisfied by the table. The most common normal forms are:

- First Normal Form (1NF): A table is in 1NF if it has no repeating groups or multivalued attributes, and each attribute is atomic, meaning it cannot be further subdivided.
- Second Normal Form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key, meaning it cannot be determined by a subset of the primary key.
- Third Normal Form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key, meaning it cannot be determined by another non-key attribute.
- Boyce-Codd Normal Form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key, meaning there are no partial or transitive dependencies on non-key attributes.

There are also higher normal forms, such as Fourth Normal Form (4NF) and Fifth Normal Form (5NF), that deal with multivalued dependencies and join dependencies, respectively. However, they are less commonly used in practice.

To normalize a database, we follow a step-by-step process of applying the normal forms to each table and checking if they satisfy the conditions. If not, we decompose the table into smaller tables and repeat the process until we reach the desired level of normalization. We also need to ensure that the normalized tables preserve the original information and relationships of the unnormalized table.

Here is an example of normalization using a table called Student_Course:

| Student_ID | Student_Name | Course_ID | Course_Name | Instructor_Name |
|------------|--------------|-----------|-------------|-----------------|
| 101        | Alice        | C1        | DBMS        | John            |
| 102        | Bob          | C2        | Java        | Mary            |
| 103        | Charlie      | C1        | DBMS        | John            |
| 103        | Charlie      | C3        | Python      | Lisa            |
| 104        | David        | C2        | Java        | Mary            |
| 104        | David        | C4        | C++         | Mike            |

This table is not in 1NF, because it has a repeating group of Course_ID, Course_Name, and Instructor_Name for each student. To convert it to 1NF, we need to remove the repeating group and create a separate record for each combination of Student_ID and Course_ID. The resulting table is:

| Student_ID | Student_Name | Course_ID | Course_Name | Instructor_Name |
|------------|--------------|-----------|-------------|-----------------|
| 101        | Alice        | C1        | DBMS        | John            |
| 102        | Bob          | C2        | Java        | Mary            |
| 103        | Charlie      | C1        | DBMS        | John            |
| 103        | Charlie      | C3        | Python      | Lisa            |
| 104        | David        | C2        | Java        | Mary            |
| 104        | David        | C4        | C++         | Mike            |

This table is in 1NF, but not in 2NF, because it has some non-key attributes that are not fully functionally dependent on the primary key. The primary key of this table is a composite key of Student_ID and Course_ID, but the attributes Student_Name, Course_Name, and Instructor_Name are only dependent on Student_ID or Course_ID, not both. To convert it to 2NF, we need to split the table into two tables, one for Student and one for Course, and link them using a foreign key. The resulting tables are:

| Student_ID |