# Unit 3 - Database Design and Normalization

## Database Design
- Database design is the process of creating a logical and physical structure for storing and manipulating data in a relational database management system (RDBMS).
- Database design involves identifying the entities, attributes, relationships, and constraints that represent the real-world problem domain and mapping them to tables and columns in a relational schema.
- Database design aims to achieve the following objectives:
  - Minimize data redundancy and inconsistency by avoiding duplication and conflicts of data across tables.
  - Maximize data integrity and quality by ensuring that the data stored in the database conforms to the rules and expectations of the problem domain.
  - Optimize data access and performance by choosing appropriate data types, indexes, and query methods for the data and the application requirements.
  - Enhance data security and privacy by implementing access control and encryption mechanisms for the data and the database objects.
  - Facilitate data maintenance and evolution by providing clear and consistent documentation and naming conventions for the database schema and its components.

## Normalization
- Normalization is a database design technique, which is used to design a relational database table up to higher normal form. The process is progressive, and a higher level of database normalization cannot be achieved unless the previous levels have been satisfied.
- Normalization also simplifies the database design so that it achieves the optimal structure composed of atomic elements (i.e. elements that cannot be broken down into smaller parts).
- Normalization helps to achieve the objectives of database design by reducing data redundancy and inconsistency, improving data integrity and quality, and optimizing data access and performance.
- Normalization involves applying a set of rules or criteria to a table to check if it satisfies a certain normal form. The most common normal forms are:
  - First Normal Form (1NF): A table is in 1NF if it contains only atomic values and has no repeating groups of attributes.
  - Second Normal Form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key.
  - Third Normal Form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key.
  - Boyce-Codd Normal Form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key.
  - Fourth Normal Form (4NF): A table is in 4NF if it is in BCNF and has no multi-valued dependencies.
  - Fifth Normal Form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies.

## Example
- Consider the following table that stores information about students, courses, and instructors:

| Student ID | Student Name | Course ID | Course Name | Instructor ID | Instructor Name |
|------------|--------------|-----------|-------------|---------------|-----------------|
| S001       | Alice        | C001      | Math        | I001          | Bob             |
| S001       | Alice        | C002      | English     | I002          | Carol           |
| S002       | David        | C001      | Math        | I001          | Bob             |
| S002       | David        | C003      | Science     | I003          | Dan             |
| S003       | Eve          | C002      | English     | I002          | Carol           |
| S003       | Eve          | C003      | Science     | I003          | Dan             |

- This table is not in 1NF because it has repeating groups of attributes (Course ID, Course Name, Instructor ID, Instructor Name) for each student. To convert it to 1NF, we need to create a separate table for each repeating group and link them with a foreign key. For example:

| Student ID | Student Name |
|------------|--------------|
| S001       | Alice        |
| S002       | David        |
| S003       | Eve          |

| Course ID | Course Name |
|-----------|-------------|
| C001      | Math        |
| C002      | English     |
| C003      | Science     |

| Instructor ID | Instructor Name |
|---------------|-----------------|
| I001          | Bob             |
| I002          | Carol           |
| I003          | Dan             |

| Student ID | Course ID | Instructor ID |
|------------|-----------|---------------|
| S001       | C001      | I001