Hello, I am Sydney, your AI assistant. I can help you with your study material for the Unit 3 - Data Base Design & Normalization in the subject of Database Management System. Here are some notes on the topic:

### Database Design
- Database design is the process of creating a logical and physical structure of a database that meets the data requirements of the users and applications.
- Database design involves the following steps:
  - Requirement analysis: Identify the purpose, scope, and objectives of the database, and collect the data and functional requirements from the users and applications.
  - Conceptual design: Create a high-level abstract model of the database using a conceptual data model, such as the entity-relationship (ER) model, that describes the entities, attributes, relationships, and constraints of the data.
  - Logical design: Map the conceptual model to a logical data model, such as the relational model, that defines the tables, columns, keys, and integrity rules of the database.
  - Physical design: Choose the physical storage structures, access methods, indexes, and performance parameters of the database, based on the logical model and the expected workload.

### Normalization
- Normalization is the process of organizing the data in a database to reduce redundancy and improve data integrity.
- Normalization involves the following steps:
  - Decompose the tables into smaller and simpler tables that have minimal data dependency and redundancy.
  - Assign a primary key to each table that uniquely identifies each row.
  - Define foreign keys to link the tables based on the relationships among the entities.
  - Apply normalization rules or normal forms to check and improve the quality of the database design.
- The most common normal forms are:
  - First normal form (1NF): A table is in 1NF if it has no repeating groups or multivalued attributes, and each cell contains a single value.
  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key.
  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key.
  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key.
  - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and has no multivalued dependencies.
  - Fifth normal form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies.