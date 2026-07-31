# Unit 4 - Database Design and Normalization

## Database Design

- Database design is the process of creating a logical and physical structure for storing and manipulating data in a relational database management system (RDBMS).
- Database design involves identifying the entities, attributes, relationships, and constraints that represent the real-world problem domain and mapping them to tables and columns in a database schema.
- Database design follows a top-down or bottom-up approach, depending on whether the design starts from a conceptual model (such as an entity-relationship diagram) or from an existing database (such as a reverse-engineered schema).
- Database design aims to achieve the following objectives:
  - Minimize data redundancy and inconsistency by avoiding duplication and conflicts of data across tables.
  - Maximize data integrity and quality by enforcing rules and validations on the data values and relationships.
  - Optimize data access and performance by choosing appropriate data types, indexes, views, and queries.
  - Ensure data security and privacy by implementing access control and encryption mechanisms.
  - Facilitate data maintenance and evolution by allowing changes and updates to the database schema and data without affecting the existing functionality and applications.

## Normalization

- Normalization is a database design technique, which is used to design a relational database table up to higher normal form. The process is progressive, and a higher level of database normalization cannot be achieved unless the previous levels have been satisfied. 
- Normalization helps to eliminate data anomalies, such as insertion, deletion, and update anomalies, that may arise due to data redundancy and inconsistency in a database table.
- Normalization also simplifies the database design by reducing the number of columns and tables and ensuring that each table contains only related data. 
- Normalization is based on the concept of functional dependency, which is a relationship between two sets of attributes in a table, such that the values of one set (called the determinant) uniquely determine the values of the other set (called the dependent).
- Normalization involves applying a series of normal forms, which are rules or criteria that define the level of normalization of a table. The most common normal forms are:
  - First normal form (1NF): A table is in 1NF if it contains only atomic values (i.e. values that cannot be broken down into smaller parts) and has no repeating groups of attributes. 
  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key (i.e. there are no partial dependencies). 
  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key (i.e. there are no transitive dependencies). 
  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key (i.e. there are no non-trivial dependencies that violate the key constraint). 
  - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and has no multi-valued dependencies (i.e. dependencies between two or more sets of attributes that are independent of each other). 
  - Fifth normal form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies (i.e. dependencies that can be expressed by joining two or more tables that are not subsets of the original table). 

## Example of Normalization

- Consider the following table that stores information about students, courses, and instructors:

| Student ID | Student Name | Course ID | Course Name | Instructor ID | Instructor Name |
|------------|--------------|-----------|-------------|---------------|-----------------|
| S001       | Alice        | C001      | Math        | I001          | Bob             |
| S001       | Alice        | C002      | English     | I002          | Carol           |
| S002       | David        | C001      | Math        | I001          | Bob             |
| S002       | David        | C003      | Science     | I003          | Dan             |
| S003       | Eve          | C002      | English     | I002          | Carol           |
| S003       | Eve          | C003      | Science     | I003          | Dan             |

- This table