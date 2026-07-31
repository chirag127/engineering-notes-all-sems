 Here is the content in Markdown format without any emojis or external links and in a formal tone:

### DML for the notes of the Unit 1 - Introduction in the subject of Basics of Data Base Management System

1. Data Manipulation Language (DML) is used to manipulate data within the database. The common DML commands are:
- INSERT: Adds a new row (record) to a table
- UPDATE: Updates existing rows (records) in a table
- DELETE: Deletes rows (records) from a table

2. The INSERT statement adds a new row to a table. The new row is specified by values for one or more column names. If values are not specified for all columns, the remaining columns will contain NULL values.

Syntax:
INSERT INTO table_name (column_1, column_2, ...)
VALUES (value_1, value_2, ...);

3. The UPDATE statement is used to modify the existing records in a table. It can be used to modify one or more fields of one or more records.

Syntax:
UPDATE table_name
SET column_1 = value_1, column_2 = value_2, ...
WHERE condition;

4. The DELETE statement is used to remove existing records from a table.

Syntax:
DELETE FROM table_name
WHERE condition;

5. The results of DML commands are not persistent until you commit the transaction using the COMMIT statement or implicitly commit the transaction. An explicit COMMIT statement ensures that all DML commands are persisted in the database and that the changes are permanent.