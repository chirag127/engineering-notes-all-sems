 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Creating and managing tables for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab.

1. Creating a table:

- Define the table name.
- Define the column names and their data types.
- Define the primary key.
- Define foreign keys if any.
- Define constraints like NOT NULL, UNIQUE, etc if any.

Syntax:
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    ...,
    constraint1,
    constraint2,
    ...
    primary key(coloumn1, ...)
);

2. Altering a table:

- Adding a new column.
- Modifying the data type of a column.
- Setting default value to a column.
- Adding constraints.
- Renaming a table.

Syntax:
ALTER TABLE table_name
[ADD|MODIFY|DROP] column_definition
[ADD|DROP constraint]
[RENAME TO new_table_name];

3. Dropping a table:

- Table and all its data gets deleted.
- Can't be rolled back.
- Dependent objects like views, stored procedures, etc also get dropped.

Syntax:
DROP TABLE table_name;

4. Truncating a table:

- Clears all the rows from a table but the table structure remains the same.
- Can be rolled back.
- Much faster than deleting all rows of a table.

Syntax:
TRUNCATE TABLE table_name;