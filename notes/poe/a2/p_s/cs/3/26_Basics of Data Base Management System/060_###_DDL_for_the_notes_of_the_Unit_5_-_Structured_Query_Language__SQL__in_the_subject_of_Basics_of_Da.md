 Here is the content in Markdown format for the topic -

### DDL for the notes of the Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System

1. DDL or Data Definition Language is used to define the database structure. It includes commands like:

- CREATE - to create a new database, table, index, etc.
- ALTER - alters an existing database object
- DROP - deletes an existing database object

2. CREATE DATABASE - is used to create a new database. The syntax is -

```
CREATE DATABASE database_name;
```

3. CREATE TABLE - is used to create a new table. The syntax is -

```
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    ...
);
```

Example -

```
CREATE TABLE employees (
    id INT,
    name VARCHAR(30),
    salary INT
);
```

4. ALTER TABLE - is used to modify an existing table. It can be used to add, delete or modify columns. The syntax is -

```
ALTER TABLE table_name
   ADD column_name datatype;

ALTER TABLE table_name
   DROP COLUMN column_name;

ALTER TABLE table_name
   MODIFY COLUMN column_name datatype;
```

5. DROP TABLE - is used to delete an existing table. The syntax is -

```
DROP TABLE table_name;
```

[Detailed explanations, examples and diagrams can be added here for better understanding]

The advantages of using DDL are -

1. It allows us to create and modify database objects efficiently.
2. It provides data integrity by applying constraints.
3. It makes the database well-organized and managed.

The disadvantages are -

1. If a mistake is made while using DDL, it can delete the whole database or table leading to loss of data.
2. DDL commands are irreversible. Once a table is deleted using DROP TABLE, it cannot be undone.

[Applications and codes can also be included here if required]