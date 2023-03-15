### Integrity Constraints for the Notes of the Unit 3 - Relational Database Concepts in the Subject of Basics of Data Base Management System

- Integrity constraints are the set of rules that can be used to maintain the data integrity during an insert, delete and update operations into a table.
- Data integrity refers to the overall validity, integrity, and consistency of the data present in the database table.
- There are four main types of integrity constraints in relational database:
  - Domain constraints: These are the rules that define the valid values for a column or attribute. For example, a column that stores the age of a person must have a positive integer value.
  - Key constraints: These are the rules that ensure the uniqueness of a row or record in a table. For example, a primary key is a column or a combination of columns that can uniquely identify a row in a table.
  - Entity integrity constraints: These are the rules that ensure that every table has a primary key and that the primary key or any part of it does not contain null values. For example, a table that stores the details of employees must have a primary key such as employee_id and it cannot be null.
  - Referential integrity constraints: These are the rules that ensure that the foreign key values in a table are consistent with the primary key values in the related table. For example, a table that stores the details of departments must have a foreign key such as manager_id that references the employee_id in the employee table.
- Integrity constraints are enforced by the database management system (DBMS) to ensure the quality and accuracy of the data in the database.
- Integrity constraints can be specified at the time of table creation or table modification using the SQL commands such as CREATE TABLE, ALTER TABLE, or ADD CONSTRAINT.