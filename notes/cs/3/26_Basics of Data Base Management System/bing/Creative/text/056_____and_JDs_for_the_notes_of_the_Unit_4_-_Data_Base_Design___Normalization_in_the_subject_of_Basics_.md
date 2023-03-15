Hello, I am Sydney, your AI assistant. I can help you with your topic of Unit 4 - Data Base Design & Normalization in the subject of Basics of Data Base Management System. Here are some notes that you can use for your study material:

# Unit 4 - Data Base Design & Normalization

## Database Design
- Database design is the process of creating a logical and physical structure for the data in a database system.
- Database design involves identifying the entities, attributes, relationships, and constraints that represent the real-world problem domain and the user requirements.
- Database design also involves choosing the appropriate data types, keys, indexes, and storage options for the data.
- Database design aims to achieve the following objectives:
  - Ensure data integrity, consistency, and accuracy
  - Avoid data redundancy and anomalies
  - Optimize data access and performance
  - Facilitate data security and privacy
  - Support data maintenance and evolution

## Normalization
- Normalization is an important process in database design that helps in improving the efficiency, consistency, and accuracy of the database.
- Normalization makes it easier to manage and maintain the data and ensures that the database is adaptable to changing business needs.
- Normalization is based on the concept of normal forms, which are rules or criteria that define the degree of organization of the data in a table.
- Normal forms are numbered from 1 to 5, with higher normal forms being more normalized and having fewer anomalies and redundancies.
- The most common normal forms are:
  - First Normal Form (1NF): A table is in 1NF if it has no repeating groups or arrays of data, and every attribute is atomic, meaning it cannot be further subdivided.
  - Second Normal Form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key, meaning it cannot be derived from any other attribute or subset of attributes in the table.
  - Third Normal Form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key, meaning it cannot be derived from any other non-key attribute in the table.
  - Boyce-Codd Normal Form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key, meaning there are no partial or transitive dependencies on any non-key attribute.
  - Fourth Normal Form (4NF): A table is in 4NF if it is in BCNF and has no multi-valued dependencies, meaning there are no attributes that depend on more than one independent attribute in the table.
  - Fifth Normal Form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies, meaning it cannot be decomposed into two or more tables without losing information.

## Normalization Process
- The normalization process involves the following steps:
  - Determine the purpose and scope of the database
  - Identify the entities and attributes that represent the problem domain and the user requirements
  - Define the functional dependencies and the candidate keys for each entity
  - Check if the entities are in 1NF and eliminate any repeating groups or arrays of data
  - Check if the entities are in 2NF and eliminate any partial dependencies on the primary key
  - Check if the entities are in 3NF and eliminate any transitive dependencies on the primary key
  - Check if the entities are in BCNF and eliminate any non-key dependencies on the candidate keys
  - Check if the entities are in 4NF and eliminate any multi-valued dependencies
  - Check if the entities are in 5NF and eliminate any join dependencies
  - Review and refine the database design and ensure that it meets the user requirements and the business rules
  - Implement the database design using the appropriate data types, keys, indexes, and storage options

## References
-  Introduction of Database Normalization - GeeksforGeeks
-  Db2 11 - Introduction - Normalization in database design - IBM
-  A Step-By-Step Guide to Normalization in DBMS With Examples - Database Star
-  Database design basics - Microsoft Support