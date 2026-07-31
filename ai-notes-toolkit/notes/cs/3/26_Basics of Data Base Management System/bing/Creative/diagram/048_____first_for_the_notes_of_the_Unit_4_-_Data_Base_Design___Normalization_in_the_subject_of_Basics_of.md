### Unit 4 - Database Design and Normalization

- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database system.
- Database normalization is a technique of database design that aims to reduce data redundancy and dependency by splitting a large table into smaller tables and defining relationships between them.
- The benefits of database normalization are:
  - Improved database performance and efficiency
  - Reduced data storage and maintenance costs
  - Enhanced data integrity and consistency
  - Simplified query and update operations
  - Increased database flexibility and scalability
- The drawbacks of database normalization are:
  - Increased complexity and overhead of database design and implementation
  - Possible loss of data access speed and convenience
  - Potential need for more joins and indexes
- The levels of database normalization are:
  - First Normal Form (1NF): A table is in 1NF if it has no repeating groups or multivalued attributes, and each attribute is atomic (cannot be further subdivided).
  - Second Normal Form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key (i.e., the non-key attribute depends on the whole key and not on a part of it).
  - Third Normal Form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key (i.e., the non-key attribute depends only on the key and not on another non-key attribute).
  - Boyce-Codd Normal Form (BCNF): A table is in BCNF if it is in 3NF and every determinant (an attribute or a set of attributes that determines another attribute) is a candidate key (a minimal set of attributes that uniquely identifies a tuple).
  - Fourth Normal Form (4NF): A table is in 4NF if it is in BCNF and has no multivalued dependencies (a dependency where one attribute or a set of attributes determines a set of values for another attribute).
  - Fifth Normal Form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies (a dependency where a table can be decomposed into two or more tables and then reconstructed by joining them without losing any information).
- The process of database normalization involves the following steps:
  - Identify the functional dependencies (relationships) between the attributes of a table
  - Determine the candidate keys (possible primary keys) of the table
  - Check if the table satisfies the normal form requirements
  - If not, decompose the table into smaller tables that satisfy the normal form requirements
  - Repeat the steps for each table until all tables are normalized
- An example of database normalization is shown below:

| StudentID | Name | Course | Instructor | Room |
|-----------|------|--------|------------|------|
| S001      | Amy  | CS101  | Smith      | R101 |
| S002      | Bob  | CS101  | Smith      | R101 |
| S003      | Cam  | CS102  | Jones      | R102 |
| S004      | Dan  | CS102  | Jones      | R102 |
| S005      | Eve  | CS103  | Lee        | R103 |

- The table above is not in 1NF because it has a repeating group (Course, Instructor, Room) for each student. To convert it to 1NF, we need to remove the repeating group and create a separate table for it.

| StudentID | Name |
|-----------|------|
| S001      | Amy  |
| S002      | Bob  |
| S003      | Cam  |
| S004      | Dan  |
| S005      | Eve  |

| Course | Instructor | Room |
|--------|------------|------|
| CS101  | Smith      | R101 |
| CS102  | Jones      | R102 |
| CS103  | Lee        | R103 |

- The table for students is in 1NF and 2NF, but not in 3NF because the name attribute is not functionally dependent on the student ID (i.e., two students can have the same name). To convert it to 3NF, we need to split the name attribute into first name and last name.

| StudentID | FirstName | LastName |
|-----------|-----------|----------|
| S001      | Amy       | Adams    |
| S002      | Bob       | Brown    |
| S003