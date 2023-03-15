# Unit 3 - Database Design and Normalization

## Database Design
- Database design is the process of creating a logical and physical structure for storing and manipulating data in a relational database management system (RDBMS).
- Database design involves identifying the entities, attributes, relationships, and constraints that represent the real-world problem domain and mapping them to tables and columns in a relational schema.
- Database design follows a top-down or bottom-up approach, depending on whether the design starts from a conceptual model (such as an entity-relationship diagram) or from existing data sources (such as spreadsheets or flat files).
- Database design aims to achieve the following objectives:
  - Minimize data redundancy and inconsistency by avoiding duplication and conflicts of data across tables.
  - Maximize data integrity and quality by enforcing rules and constraints that ensure the validity and accuracy of data.
  - Optimize data performance and efficiency by choosing appropriate data types, indexes, and storage structures that facilitate fast and easy data access and manipulation.
  - Enhance data security and privacy by implementing access control mechanisms that restrict unauthorized or inappropriate data access and modification.
  - Facilitate data maintenance and evolution by allowing changes and updates to the database schema and data without affecting the existing functionality and applications.

## Database Normalization
- Database normalization is a database design technique, which is used to design a relational database table up to higher normal form. The process is progressive, and a higher level of database normalization cannot be achieved unless the previous levels have been satisfied.
- Database normalization is based on the principle of decomposition, which involves breaking down a complex table into smaller and simpler tables that eliminate data redundancy and dependency anomalies.
- Database normalization is guided by a set of rules or criteria, called normal forms, that define the properties and characteristics of a well-designed table. The most common normal forms are:
  - First normal form (1NF): A table is in 1NF if it contains only atomic values (i.e., values that cannot be further divided) and has no repeating groups (i.e., columns that store multiple values of the same type for a single record).
  - Second normal form (2NF): A table is in 2NF if it is in 1NF and every non-key attribute (i.e., an attribute that is not part of the primary key or a candidate key) is fully functionally dependent on the primary key (i.e., the value of a non-key attribute is determined by the value of the primary key and nothing else).
  - Third normal form (3NF): A table is in 3NF if it is in 2NF and every non-key attribute is non-transitively dependent on the primary key (i.e., the value of a non-key attribute is determined by the value of the primary key and not by the value of another non-key attribute that depends on the primary key).
  - Boyce-Codd normal form (BCNF): A table is in BCNF if it is in 3NF and every determinant (i.e., an attribute or a set of attributes that determines the value of another attribute) is a candidate key (i.e., a minimal set of attributes that uniquely identifies a record).
  - Fourth normal form (4NF): A table is in 4NF if it is in BCNF and has no multi-valued dependencies (i.e., dependencies between two or more non-key attributes that are independent of the primary key).
  - Fifth normal form (5NF): A table is in 5NF if it is in 4NF and has no join dependencies (i.e., dependencies that require joining two or more tables to reconstruct the original table).
- Database normalization has the following benefits:
  - It reduces data redundancy and inconsistency by eliminating duplicate and conflicting data across tables.
  - It improves data integrity and quality by enforcing rules and constraints that ensure the validity and accuracy of data.
  - It simplifies data manipulation and querying by reducing the complexity and ambiguity of data relationships and operations.
  - It facilitates data maintenance and evolution by allowing changes and updates to the database schema and data without affecting the existing functionality and applications.
- Database normalization also has some drawbacks, such as:
  - It may increase the number of tables and joins, which can affect the performance and efficiency of data access and manipulation.
  - It may lose some information or meaning that is implicit in the original table, which can affect the usability and understanding of data.
  - It may not be suitable for some types of data or applications that require denormalized or unstructured data, such as data warehousing, data mining, or big data analytics.