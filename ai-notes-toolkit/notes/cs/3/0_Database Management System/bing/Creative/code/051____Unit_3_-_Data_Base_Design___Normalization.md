Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for Unit 3 - Data Base Design & Normalization:

## Unit 3 - Data Base Design & Normalization

- Data base design is the process of creating a logical and physical structure of a data base that meets the requirements of the users and the application.
- Normalization is a technique of data base design that aims to reduce data redundancy and improve data integrity by organizing the data into smaller and well-defined tables.
- The main steps of data base design are:
  - Requirement analysis: Identify the purpose, scope, and objectives of the data base, and collect the data and functional requirements from the users and the application.
  - Conceptual design: Create an abstract model of the data base using a high-level data model, such as the entity-relationship (ER) model, that shows the entities, attributes, and relationships of the data.
  - Logical design: Map the conceptual model to a logical data model, such as the relational model, that defines the tables, columns, keys, and constraints of the data base.
  - Physical design: Choose the physical storage structures, indexes, access methods, and performance parameters of the data base, based on the logical data model and the expected workload.
- The main benefits of normalization are:
  - Eliminate data anomalies: Data anomalies are inconsistencies or errors that occur when data is inserted, updated, or deleted in a data base. Normalization avoids data anomalies by ensuring that each piece of data is stored in only one place and that the dependencies among the data are properly enforced by the keys and constraints.
  - Minimize data redundancy: Data redundancy is the duplication of data in a data base, which wastes storage space and increases the risk of data inconsistency. Normalization minimizes data redundancy by decomposing the tables into smaller and simpler tables that have fewer columns and store only the relevant data.
  - Enhance data integrity: Data integrity is the accuracy, consistency, and validity of the data in a data base. Normalization enhances data integrity by defining the rules and constraints that govern the data, such as the primary keys, foreign keys, and check constraints, and by ensuring that the data conforms to these rules and constraints.
- The main levels of normalization are:
  - First normal form (1NF): A table is in 1NF if it has no repeating groups, that is, each column contains only atomic values and each row is unique.
  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key column is fully dependent on the primary key, that is, there are no partial dependencies.
  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key column is non-transitively dependent on the primary key, that is, there are no transitive dependencies.
  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key, that is, there are no non-trivial functional dependencies that violate the key constraint.
  - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and has no multi-valued dependencies, that is, there are no dependencies among two or more non-key columns that are independent of the primary key.
  - Fifth normal form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies, that is, it cannot be decomposed into smaller tables without losing information.