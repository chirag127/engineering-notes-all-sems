Hello, I am Sydney, your AI assistant. I can help you with your study material for Database Management System. Here are some notes for Unit 3 - Data Base Design & Normalization:

### Data Base Design & Normalization

- Database design is the process of creating a logical and physical structure of a database that meets the requirements of the users and the application.
- Database design involves the following steps:
  - Requirement analysis: Identify the purpose, scope, and objectives of the database, and collect the data and functional requirements from the users and the application.
  - Conceptual design: Create a high-level abstract model of the database using a conceptual data model, such as the entity-relationship (ER) model, that describes the entities, attributes, relationships, and constraints of the data.
  - Logical design: Map the conceptual model to a logical data model, such as the relational model, that defines the tables, columns, keys, and integrity rules of the database.
  - Physical design: Choose the physical storage structures, access methods, indexes, and performance parameters of the database, based on the logical model and the expected workload.
- Normalization is a technique of database design that aims to reduce data redundancy and improve data integrity by organizing the data into smaller and well-defined tables.
- Normalization involves the following steps:
  - Identify the functional dependencies between the attributes of a table, which indicate how one attribute determines the value of another attribute.
  - Apply the normal forms, which are rules or criteria for evaluating the quality of a table design, and decompose the table into smaller tables if it does not satisfy a normal form.
  - The most common normal forms are:
    - First normal form (1NF): A table is in 1NF if it has no repeating groups or multivalued attributes, and each attribute has a single atomic value.
    - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key, which means it cannot be determined by a subset of the primary key.
    - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key, which means it cannot be determined by another non-key attribute.
    - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key, which means there are no dependencies between two sets of non-key attributes.
    - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and has no multivalued dependencies, which means there are no attributes that depend on a set of attributes rather than a single attribute.
    - Fifth normal form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies, which means it cannot be decomposed into smaller tables without losing information.