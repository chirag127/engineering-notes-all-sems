# Unit 4 - Database Design and Normalization

## Database Design
- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database system.
- Database design involves identifying the data requirements, defining the entities and attributes, determining the relationships and constraints, and choosing the appropriate data model and storage format.
- Database design aims to achieve the following objectives:
  - Accuracy: The database should accurately represent the real-world domain and the business rules of the application.
  - Efficiency: The database should allow fast and easy access, insertion, update, and deletion of data, while minimizing the storage space and processing overhead.
  - Security: The database should protect the data from unauthorized access, modification, or deletion, and ensure the integrity and consistency of the data.
  - Flexibility: The database should be able to accommodate changing data requirements and business needs, without requiring major modifications or redesigns.

## Database Normalization
- Database normalization is a database schema design technique, by which an existing schema is modified to minimize redundancy and dependency of data.
- Normalization splits a large table into smaller tables and defines relationships between them to increase the clarity and organization of data.
- Normalization also helps to avoid data anomalies, such as insertion, update, and deletion anomalies, that may arise due to redundant or dependent data.
- Normalization is based on a set of rules or normal forms, that define the criteria for a well-structured database schema. The most common normal forms are:
  - First Normal Form (1NF): A table is in 1NF if it has no repeating groups or multivalued attributes, and each attribute is atomic (cannot be further subdivided).
  - Second Normal Form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key (i.e., the non-key attribute depends on the whole key and not on a part of it).
  - Third Normal Form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key (i.e., the non-key attribute depends only on the key and not on another non-key attribute).
  - Boyce-Codd Normal Form (BCNF): A table is in BCNF if it is in 3NF and every determinant (a set of attributes that determines another attribute) is a candidate key (a minimal set of attributes that uniquely identifies a tuple).
  - Fourth Normal Form (4NF): A table is in 4NF if it is in BCNF and has no multivalued dependencies (a dependency where one attribute determines a set of values for another attribute).
  - Fifth Normal Form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies (a dependency where a table can be decomposed into two or more tables and then reconstructed by joining them without losing any information).

## Example of Database Normalization
- Consider the following table that stores the information about the courses offered by a college, the instructors who teach them, and the students who enroll in them.

| Course_ID | Course_Name | Instructor_ID | Instructor_Name | Student_ID | Student_Name |
|-----------|-------------|---------------|-----------------|------------|--------------|
| CSE101    | Programming | I001          | Alice           | S001       | Bob          |
| CSE101    | Programming | I001          | Alice           | S002       | Carol        |
| CSE101    | Programming | I001          | Alice           | S003       | Dave         |
| CSE102    | Database    | I002          | Eve             | S002       | Carol        |
| CSE102    | Database    | I002          | Eve             | S004       | Frank        |
| CSE103    | Web Design  | I003          | Grace           | S001       | Bob          |
| CSE103    | Web Design  | I003          | Grace           | S003       | Dave         |
| CSE103    | Web Design  | I003          | Grace           | S005       | Helen        |

- This table is not in 1NF, because it has repeating groups of attributes (Course_Name, Instructor_ID, Instructor_Name, Student_ID, Student_Name) for each Course_ID. To convert it to 1NF, we need to remove the repeating groups and create a separate table for each group, with a foreign key referencing the Course_ID. For example:

| Course_ID | Course