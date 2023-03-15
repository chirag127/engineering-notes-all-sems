# Unit 4 - Database Design and Normalization

## Database Design
- Database design is the process of creating a logical and physical structure for storing and manipulating data in a relational database management system (RDBMS).
- Database design involves identifying the entities, attributes, relationships, and constraints that represent the real-world problem domain and mapping them to tables and columns in a relational schema.
- Database design follows a top-down or bottom-up approach, depending on whether the design starts from the conceptual level (abstract representation of data) or the physical level (storage and access methods).
- Database design aims to achieve the following objectives:
  - Minimize data redundancy and inconsistency by avoiding duplication and conflicts of data across tables.
  - Maximize data integrity and security by enforcing rules and policies on data values, access, and modification.
  - Optimize data performance and scalability by choosing appropriate data types, indexes, and partitioning strategies.
  - Facilitate data usability and maintainability by providing clear and consistent naming conventions, documentation, and metadata.

## Normalization
- Normalization is a database design technique, which is used to design a relational database table up to higher normal form. The process is progressive, and a higher level of database normalization cannot be achieved unless the previous levels have been satisfied.
- Normalization helps to reduce data redundancy and inconsistency, improve data integrity, and simplify the database design by eliminating anomalies and dependencies that may cause insertion, deletion, or update anomalies.
- Normalization involves applying a set of rules or criteria, called normal forms, to each table in the database. The most common normal forms are:
  - First normal form (1NF): A table is in 1NF if it contains only atomic values (i.e. values that cannot be further decomposed) and has no repeating groups (i.e. columns that store multiple values of the same type).
  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute (i.e. attribute that is not part of the primary key or a candidate key) is fully functionally dependent on the primary key (i.e. the value of the non-key attribute is determined by the value of the primary key).
  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key (i.e. the value of the non-key attribute is not determined by the value of another non-key attribute that is dependent on the primary key).
  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant (i.e. attribute or set of attributes that determines the value of another attribute) is a candidate key (i.e. a minimal set of attributes that uniquely identifies a row in the table).
  - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and has no multi-valued dependencies (i.e. dependencies where the value of one attribute depends on the value of another attribute and vice versa).
  - Fifth normal form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies (i.e. dependencies where the table can be decomposed into two or more tables and then reconstructed by joining them without losing any information).

## Example of Database Design and Normalization
- Suppose we want to design a database for a university that stores information about students, courses, and enrollments. A possible database design and normalization process is as follows:

### Step 1: Identify the entities and attributes
- The main entities in the problem domain are students, courses, and enrollments. Each entity has a set of attributes that describe its properties and characteristics. For example, a student has a student ID, name, address, phone number, email, and major. A course has a course ID, title, description, credits, and instructor. An enrollment has a student ID, course ID, semester, year, and grade.

### Step 2: Define the relationships and constraints
- The entities are related to each other by various types of relationships, such as one-to-one, one-to-many, or many-to-many. Each relationship may have some constraints, such as cardinality, participation, or referential integrity. For example, a student can enroll in many courses, and a course can have many students enrolled in it. This is a many-to-many relationship, which has a cardinality of M:N. The participation of both entities is