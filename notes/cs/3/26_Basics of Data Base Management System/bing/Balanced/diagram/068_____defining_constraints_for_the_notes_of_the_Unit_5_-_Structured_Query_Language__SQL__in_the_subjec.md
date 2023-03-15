### Defining Constraints for the Notes of the Unit 5 - Structured Query Language (SQL) in the Subject of Basics of Data Base Management System

- Constraints are rules that the SQL Server Database Engine enforces for you to ensure the accuracy and reliability of the data in a table  .
- Constraints can be applied at the column level or the table level .
- Column level constraints are defined as part of the column definition, while table level constraints are defined after all the columns are defined.
- Some of the frequently used SQL constraints are  :
  - NOT NULL: Ensures that a column cannot have a NULL value  .
  - DEFAULT: Provides a default value for a column when none is specified .
  - UNIQUE: Ensures that all values in a column are different   .
  - PRIMARY KEY: Uniquely identifies each row/record in a table  .
  - FOREIGN KEY: References a primary key in another table to establish a relationship between the tables  .
  - CHECK: Validates that the values in a column meet a specified condition   .
- Constraints can be created, modified, or dropped using the CREATE TABLE, ALTER TABLE, or DROP TABLE statements.
- Constraints can be named or unnamed. If unnamed, the SQL Server Database Engine assigns a system-generated name.
- Constraints can be enabled or disabled. If disabled, the constraint is not enforced by the SQL Server Database Engine.
- Constraints can be trusted or untrusted. If trusted, the SQL Server Database Engine guarantees that no existing rows violate the constraint.