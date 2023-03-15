## Unit 3 - Data Base Design & Normalization

- Database design is the process of creating a logical and physical structure for storing and manipulating data in a database system.
- Normalization is a technique of database design that aims to reduce data redundancy and improve data integrity by organizing data into tables with well-defined relationships and constraints.
- The main steps of database design are:
  - Requirement analysis: Identify the purpose, scope, and users of the database system.
  - Conceptual design: Create an abstract model of the data using a high-level notation such as entity-relationship (ER) diagrams or unified modeling language (UML) diagrams.
  - Logical design: Translate the conceptual model into a logical schema using a specific data model such as relational, hierarchical, or network.
  - Physical design: Choose the physical storage structures, access methods, and performance tuning parameters for the database system.
- The main benefits of normalization are:
  - Eliminate data anomalies: Data anomalies are inconsistencies or errors that occur when data is inserted, updated, or deleted in a database. Normalization prevents data anomalies by ensuring that each piece of data is stored in only one place and that the dependencies among data are properly enforced by the database system.
  - Minimize data redundancy: Data redundancy is the duplication of data in a database. Normalization minimizes data redundancy by eliminating unnecessary or derived attributes and by splitting large tables into smaller ones with fewer columns.
  - Enhance data integrity: Data integrity is the accuracy and consistency of data in a database. Normalization enhances data integrity by defining primary keys, foreign keys, and other constraints that ensure the validity and uniqueness of data.
- The main levels of normalization are:
  - First normal form (1NF): A table is in 1NF if it has no repeating groups or arrays of data. Each row represents a single record and each column represents a single attribute. All values are atomic, meaning they cannot be further decomposed into smaller parts.
  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute is fully functionally dependent on the primary key. Functional dependency means that the value of one attribute determines the value of another attribute. Full functional dependency means that the dependency cannot be reduced to a subset of the primary key.
  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key. Transitive dependency means that the value of one attribute depends on the value of another attribute that is not part of the primary key. Non-transitive dependency means that the dependency is direct and not indirect.
  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant is a candidate key. A determinant is an attribute or a set of attributes that determines the value of another attribute. A candidate key is a minimal set of attributes that uniquely identifies a record in a table.
  - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and has no multi-valued dependencies. A multi-valued dependency means that the value of one attribute depends on the value of another attribute, and both attributes are part of the primary key.
  - Fifth normal form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies. A join dependency means that a table can be decomposed into two or more tables and then reconstructed by joining them on their common attributes without losing any information.