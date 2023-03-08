 Here is the content in markdown format for the given topic:

### Manipulating data for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

1. Inserting data into tables:
- INSERT statement is used to insert new rows into a table.
- The INSERT statement has the following structure:

INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);

- If you are inserting values for all the columns of the table, you do not need to specify the column names in the INSERT statement.
- However, for the sake of clarity and to avoid errors, it is a good practice to specify the column names.

2. Updating data in tables:
- The UPDATE statement is used to update existing records in a table.
- The UPDATE statement has the following structure:

UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;

- You should always specify a WHERE clause with the UPDATE statement to avoid updating all the rows of the table.
- The WHERE clause specifies which record(s) should be updated. If you omit the WHERE clause, all records in the table will be updated.

3. Deleting data from tables:
- The DELETE statement is used to delete rows from a table.
- The DELETE statement has the following structure:

DELETE FROM table_name WHERE condition;

- You should always specify a WHERE clause with the DELETE statement to avoid deleting all the rows of the table.
- The WHERE clause specifies which record(s) should be deleted. If you omit the WHERE clause, all records in the table will be deleted.

[Detailed explanations can be added here with examples and diagrams]