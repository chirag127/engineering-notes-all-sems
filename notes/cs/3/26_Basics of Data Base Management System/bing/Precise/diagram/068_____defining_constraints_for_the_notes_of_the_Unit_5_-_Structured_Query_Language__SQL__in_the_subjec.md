# Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System

## Defining Constraints

Constraints are used to specify the rules for the data in a table. They are used to limit the type of data that can go into a table. This ensures the accuracy and reliability of the data in the table. There are several types of constraints that can be used in SQL:

1. **NOT NULL** - This constraint ensures that a column cannot have a NULL value.
2. **UNIQUE** - This constraint ensures that all values in a column are unique.
3. **PRIMARY KEY** - This constraint uniquely identifies each record in a table. It must contain unique values and cannot contain NULL values.
4. **FOREIGN KEY** - This constraint is used to link two tables together. It is a field (or collection of fields) in one table that refers to the PRIMARY KEY in another table.
5. **CHECK** - This constraint ensures that all values in a column satisfy a specific condition.
6. **DEFAULT** - This constraint provides a default value for a column when no value is specified.

These constraints can be defined at the column level or the table level. They can be added during the creation of the table or after the table has been created using the ALTER TABLE command.