# Integrity Constraints for the Notes of the Unit 3 - Relational Database Concepts

- Integrity constraints are the set of rules that can be used to maintain the data integrity during an insert, delete and update operations into a table.
- Data integrity refers to the overall validity, integrity, and consistency of the data present in the database table.
- There are four main types of integrity constraints in relational database:
  - Domain constraints
  - Key constraints
  - Entity integrity constraints
  - Referential integrity constraints
- Domain constraints specify the valid values for a column or an attribute. They can be defined by data type, range, format, or a set of permissible values .
- Key constraints specify that a column or a combination of columns can uniquely identify a row in a table. They can be primary key or candidate key .
- Entity integrity constraints ensure that every table has a primary key and that the primary key has no null values.
- Referential integrity constraints ensure that the foreign key values in one table match the primary key values in another table. They also define the actions to be taken when the primary key or the foreign key is modified or deleted .
- Integrity constraints can be enforced by the database management system (DBMS) or by the application program. The DBMS can check the constraints before performing any operation on the tables and reject any operation that violates the constraints .
- Integrity constraints can help to prevent data anomalies, such as insertion, deletion, and update anomalies, that can compromise the quality and consistency of the data .