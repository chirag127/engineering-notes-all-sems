 Here is the formal content in Markdown format without any emojis or external links:

### Manipulating data for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab.

1. Inserting Data:
- INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);

2. Updating Data:
- UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;

3. Deleting Data:
- DELETE FROM table_name WHERE condition;

4. SELECT statement:
- SELECT column1, column2, ...
FROM table_name;

- SELECT * FROM table_name; // To select all columns

- Select with DISTINCT: Removes duplicate rows
SELECT DISTINCT column1, column2, ...
FROM table_name;

- Select with WHERE: Extracts only rows that fulfill a specified condition
SELECT column1, column2, ...
FROM table_name
WHERE condition;

5. Sorting Results:
- ORDER BY column1, column2, ... ASC|DESC;
// ASC - Ascending (lowest to highest), DESC - Descending (highest to lowest)

6. Limiting Results:
- LIMIT number; // Limits the number of rows in the result