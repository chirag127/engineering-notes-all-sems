## Unit 4 - Data Base Design & Normalization

In this unit, we will learn about database design and normalization. Database design is the process of creating a database schema, which defines the structure of the database. Normalization is the process of organizing the data in a database to reduce redundancy and improve data integrity.

### 1. Database Design

1.1. Entity-Relationship (ER) Diagrams
- ER diagrams are a graphical representation of the database schema.
- They are used to model the entities, attributes, and relationships in the database.
- Entities are the objects or concepts that we want to store in the database.
- Attributes are the characteristics or properties of the entities.
- Relationships describe how the entities are related to each other.

1.2. Relational Database Management Systems (RDBMS)
- RDBMS is a software system used to manage relational databases.
- It provides tools for creating, updating, and querying the database.
- The most common RDBMS are MySQL, Oracle, and Microsoft SQL Server.

1.3. Database Normalization
- Normalization is the process of organizing the data in a database to reduce redundancy and improve data integrity.
- There are several normal forms that a database can be in, ranging from first normal form (1NF) to fifth normal form (5NF).
- The higher the normal form, the less redundancy there is in the database.

### 2. Normalization

2.1. First Normal Form (1NF)
- Each table has a primary key.
- Each column in the table is atomic (i.e., cannot be further subdivided).

2.2. Second Normal Form (2NF)
- The table is in 1NF.
- Each non-key column is dependent on the entire primary key.

2.3. Third Normal Form (3NF)
- The table is in 2NF.
- There are no transitive dependencies (i.e., a non-key column is dependent on another non-key column).

2.4. Fourth Normal Form (4NF)
- The table is in 3NF.
- There are no multi-valued dependencies (i.e., a non-key column is dependent on a set of values in another non-key column).

2.5. Fifth Normal Form (5NF)
- The table is in 4NF.
- There are no join dependencies (i.e., a non-key column is dependent on another non-key column in a different table).

In conclusion, database design and normalization are essential concepts in creating an efficient and effective database. Understanding these concepts will help ensure the data stored in the database is accurate and easily retrievable.