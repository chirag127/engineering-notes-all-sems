# Defining Constraints for the Notes of the Unit 5 - Structured Query Language (SQL) in the Subject of Basics of Data Base Management System

- Constraints are rules or restrictions that are applied to the data in a table to ensure its validity and integrity.
- Constraints can be defined at the column level or the table level, depending on the scope of the rule.
- Constraints can be specified when creating a table using the CREATE TABLE statement, or after the table is created using the ALTER TABLE statement.
- Some of the common types of constraints are:

  - NOT NULL: This constraint ensures that a column cannot have a null value, which means it must have a value in every row.
  - UNIQUE: This constraint ensures that a column or a combination of columns has a unique value in every row, which means no two rows can have the same value.
  - PRIMARY KEY: This constraint identifies the column or the combination of columns that uniquely identifies each row in the table. A primary key is a special type of unique constraint that also implies a not null constraint.
  - FOREIGN KEY: This constraint establishes a relationship between a column or a combination of columns in one table and a primary key or a unique key in another table. A foreign key ensures that the value in the referencing column or columns must exist in the referenced column or columns.
  - CHECK: This constraint allows defining a condition that must be satisfied by the value in a column or a combination of columns. A check constraint can be used to enforce domain integrity, such as limiting the range of values or the format of values.
  - DEFAULT: This constraint specifies a default value for a column that is used when no value is provided for that column in an insert or update operation. A default constraint can be used to assign a constant value, a system function, or a user-defined function.