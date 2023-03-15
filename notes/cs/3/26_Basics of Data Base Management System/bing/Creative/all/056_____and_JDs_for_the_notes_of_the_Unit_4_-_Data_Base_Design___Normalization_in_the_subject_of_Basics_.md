# Unit 4 - Database Design and Normalization

## Database Design
- Database design is the process of creating a logical and physical structure for storing and manipulating data in a relational database system.
- Database design involves identifying the entities, attributes, relationships, and constraints that represent the real-world problem domain and mapping them to tables and columns in a relational schema.
- Database design also involves choosing appropriate data types, indexes, keys, and integrity rules to ensure data quality, consistency, and performance.

## Normalization
- Normalization is a database design technique, which is used to design a relational database table up to higher normal form.
- The process is progressive, and a higher level of database normalization cannot be achieved unless the previous levels have been satisfied.
- Normalization aims to reduce data redundancy, eliminate data anomalies, and improve data integrity by organizing the data into tables and columns that are related and independent.
- Normalization also simplifies the database design and makes it easier to query, update, and maintain the data.

## Normal Forms
- Normal forms are the levels of normalization that a database table can achieve based on certain rules and criteria.
- The most common normal forms are the first normal form (1NF), the second normal form (2NF), the third normal form (3NF), and the Boyce-Codd normal form (BCNF).
- Each normal form has a set of requirements that a table must satisfy to be in that normal form. For example, to be in 1NF, a table must have no repeating groups, no multivalued attributes, and a primary key. To be in 2NF, a table must be in 1NF and have no partial dependencies. To be in 3NF, a table must be in 2NF and have no transitive dependencies. To be in BCNF, a table must be in 3NF and have no non-trivial functional dependencies that are not determined by a candidate key  .
- Higher normal forms, such as the fourth normal form (4NF) and the fifth normal form (5NF), exist but are less commonly used in practice. They deal with more complex types of dependencies and relationships, such as multivalued dependencies and join dependencies.

## Normalization Example
- To illustrate the normalization process, let us consider a simple example of a database that stores information about students, courses, and grades. The database has one table called Student_Course_Grade, which has the following columns and sample data:

| Student_ID | Student_Name | Course_ID | Course_Name | Grade |
|------------|--------------|-----------|-------------|-------|
| 101        | Alice        | C101      | Math        | A     |
| 101        | Alice        | C102      | English     | B     |
| 102        | Bob          | C101      | Math        | C     |
| 102        | Bob          | C103      | Science     | A     |
| 103        | Charlie      | C102      | English     | A     |
| 103        | Charlie      | C103      | Science     | B     |

- This table is not in 1NF, because it has repeating groups of Course_ID, Course_Name, and Grade for each student. To convert it to 1NF, we need to remove the repeating groups and create a separate row for each combination of Student_ID and Course_ID. The resulting table is:

| Student_ID | Student_Name | Course_ID | Course_Name | Grade |
|------------|--------------|-----------|-------------|-------|
| 101        | Alice        | C101      | Math        | A     |
| 101        | Alice        | C102      | English     | B     |
| 102        | Bob          | C101      | Math        | C     |
| 102        | Bob          | C103      | Science     | A     |
| 103        | Charlie      | C102      | English     | A     |
| 103        | Charlie      | C103      | Science     | B     |

- This table is now in 1NF, but not in 2NF, because it has partial dependencies. For example, the Student_Name column depends only on the Student_ID column, and the Course_Name column depends only on the Course_ID column. These columns are not fully dependent on the primary key, which is the combination of Student_ID and Course_ID. To convert it to 2NF, we need to remove the partial dependencies and create separate tables for