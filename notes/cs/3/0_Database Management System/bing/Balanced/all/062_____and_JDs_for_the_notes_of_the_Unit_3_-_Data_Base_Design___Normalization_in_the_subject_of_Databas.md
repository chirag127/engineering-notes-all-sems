# Unit 3 - Database Design and Normalization

## Database Design
- Database design is the process of creating a logical and physical structure for storing and manipulating data in a relational database management system (RDBMS).
- Database design involves identifying the entities, attributes, and relationships that represent the information and business rules of a domain.
- Database design also involves choosing the appropriate data types, constraints, indexes, and views for each attribute and table.
- Database design aims to achieve the following objectives:
  - Reduce data redundancy and inconsistency by avoiding unnecessary duplication and ensuring data integrity.
  - Improve data quality and accuracy by enforcing validation rules and business logic.
  - Enhance data security and privacy by implementing access control and encryption mechanisms.
  - Optimize data performance and scalability by minimizing disk space and memory usage, and maximizing query speed and concurrency.
  - Facilitate data maintenance and evolution by allowing easy modification and extension of the database schema and data.

## Normalization
- Normalization is a database design technique, which is used to design a relational database table up to higher normal form.
- The process is progressive, and a higher level of database normalization cannot be achieved unless the previous levels have been satisfied.
- Normalization helps to eliminate data anomalies, such as insertion, deletion, and update anomalies, that may arise due to poor database design.
- Normalization also simplifies the database design so that it achieves the optimal structure composed of atomic elements (i.e. elements that cannot be broken down into smaller parts).
- There are several normal forms, such as first normal form (1NF), second normal form (2NF), third normal form (3NF), Boyce-Codd normal form (BCNF), fourth normal form (4NF), and fifth normal form (5NF), that define the criteria for a well-designed database table.
- The most common normal forms are 1NF, 2NF, and 3NF, which are explained below:

### First Normal Form (1NF)
- A table is in 1NF if it satisfies the following conditions:
  - Each table has a unique name and a primary key that uniquely identifies each row.
  - Each attribute has a single value and a unique name.
  - Each attribute has a domain that specifies the range of values and the data type of the attribute.
  - There are no repeating groups or arrays of values in any attribute.
  - The order of the rows and columns does not matter.

### Second Normal Form (2NF)
- A table is in 2NF if it satisfies the following conditions:
  - The table is in 1NF.
  - All the non-key attributes are fully functionally dependent on the primary key, meaning that they are determined by the primary key and not by any other attribute or subset of attributes.
  - There are no partial dependencies, meaning that no non-key attribute depends on only a part of the primary key.

### Third Normal Form (3NF)
- A table is in 3NF if it satisfies the following conditions:
  - The table is in 2NF.
  - All the non-key attributes are non-transitively dependent on the primary key, meaning that they are determined by the primary key and not by any other non-key attribute or combination of non-key attributes.
  - There are no transitive dependencies, meaning that no non-key attribute depends on another non-key attribute that depends on the primary key.

## Example of Normalization
- Consider the following table that stores the information of students, courses, and instructors:

| Student ID | Student Name | Course ID | Course Name | Instructor ID | Instructor Name |
|------------|--------------|-----------|-------------|---------------|-----------------|
| S001       | Alice        | C001      | Math        | I001          | Bob             |
| S001       | Alice        | C002      | English     | I002          | Carol           |
| S002       | David        | C001      | Math        | I001          | Bob             |
| S002       | David        | C003      | Science     | I003          | Eve             |
| S003       | Frank        | C002      | English     | I002          | Carol           |
| S003       | Frank        | C003      | Science     | I003          | Eve             |

- This table is not in 1NF, because it has repeating groups of values in the Course ID, Course Name, Instructor ID, and Instructor Name attributes. To convert it to 1NF, we need to split the table into two tables: one for the student