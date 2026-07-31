 Here is the content in markdown format without emojis or external links:

## Unit 3 - Writing SQL statements Using ORACLE /MYSQL

1. SELECT statement
- Retrieve data from a table: SELECT column1, column2 FROM table_name;
- Use DISTINCT to get only distinct (different) values: SELECT DISTINCT column1 FROM table_name;
- Use * to select all columns: SELECT * FROM table_name;

2. WHERE clause
- Filter records: SELECT column1, column2 FROM table_name WHERE condition;
- Common conditions:
-- Equality: column1 = 'value'
-- Inequality: column1 <> 'value'
-- Greater than: column1 > 'value'
-- Less than: column1 < 'value'

3. AND, OR and NOT operators
- Combine multiple conditions:
-- AND: SELECT * FROM table_name WHERE condition1 AND condition2
-- Returns records that meet both conditions
-- OR: SELECT * FROM table_name WHERE condition1 OR condition2
-- Returns records that meet either condition
-- NOT: SELECT * FROM table_name WHERE NOT condition
-- Returns records that do not meet the condition

4. UPDATE statement
- Update existing data in a table
- SET clause specifies the column and new value to update
- WHERE clause specifies which record(s) to update
- Example: UPDATE table_name SET column1 = 'new value' WHERE condition;

5. DELETE statement
- Delete records from a table
- Use WHERE clause to specify which records to delete
- Example: DELETE FROM table_name WHERE condition;

[The content continues in the same formal tone with points on ORDER BY, BETWEEN, IN, NULL etc.]