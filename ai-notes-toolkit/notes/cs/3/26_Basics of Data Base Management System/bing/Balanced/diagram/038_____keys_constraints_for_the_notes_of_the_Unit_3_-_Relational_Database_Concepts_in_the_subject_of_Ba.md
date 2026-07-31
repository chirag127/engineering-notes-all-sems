### Key Constraints in Relational Database

Key constraints are rules that are applied to the columns or attributes that are used as primary keys or foreign keys in a relational database. They ensure the uniqueness, integrity and consistency of the data in the tables.

Some of the key constraints in relational database are:

- **Primary key constraint**: This constraint requires every entry in the column or set of columns that are designated as the primary key to be unique and not NULL. The primary key is used to identify each row in the table and to establish relationships with other tables. A table can have only one primary key constraint, which can consist of up to 16 columns and a total key length of 900 bytes .
- **Foreign key constraint**: This constraint requires every entry in the column or set of columns that are designated as the foreign key to match an existing value in the primary key column or set of columns of another table. The foreign key is used to reference or link data from one table to another. A table can have multiple foreign key constraints, which can reference the same or different tables .
- **Unique constraint**: This constraint requires every entry in the column or set of columns to be unique, but allows NULL values. The unique constraint is used to ensure that there are no duplicate values in the table. A table can have multiple unique constraints, which can consist of one or more columns.
- **Check constraint**: This constraint requires every entry in the column or set of columns to satisfy a specified condition or expression. The check constraint is used to limit the range or format of the data in the table. A table can have multiple check constraints, which can apply to one or more columns.
- **Not NULL constraint**: This constraint requires every entry in the column or set of columns to have a non-NULL value. The not NULL constraint is used to ensure that there are no missing values in the table. A table can have multiple not NULL constraints, which can apply to one or more columns.

These are some of the key constraints in relational database that you should know for the Unit 3 - Relational Database Concepts in the subject of Basics of Data Base Management System. I hope this helps you in your studies. If you have any questions, please ask me.