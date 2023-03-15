### Primary Key

- A primary key is a special column or combination of columns in a relational database table that uniquely identifies each row in the table    .
- A primary key is used as a unique identifier to quickly access and manipulate data within the table .
- A table can have only one primary key, which can be either a single column or a composite key (a set of columns)   .
- A primary key must satisfy the following properties  :
  - **Uniqueness**: No two rows in the table can have the same primary key value.
  - **Non-nullability**: The primary key column(s) cannot contain null values, as null values cannot be used to identify rows.
  - **Stability**: The primary key value should not change frequently, as it may affect the integrity and performance of the database.
  - **Simplicity**: The primary key should be as simple and concise as possible, to avoid unnecessary complexity and overhead.
- A primary key can be either natural or surrogate :
  - A natural key is a column or set of columns that have a logical relationship to the data in the table, such as a student ID or a phone number.
  - A surrogate key is a column or set of columns that have no inherent meaning to the data in the table, such as a randomly generated number or a sequential number.
- A primary key can be defined using the PRIMARY KEY constraint in the CREATE TABLE or ALTER TABLE statements.
- A primary key can be referenced by other tables to establish relationships between them, using foreign keys.