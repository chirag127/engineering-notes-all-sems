## Unit 5 - Creating Cursor

A cursor is a database object that is used to manipulate data in a row-by-row manner. It enables you to traverse the result set retrieved by a SELECT statement one row at a time. In this unit, we will learn how to create a cursor in SQL.

### Creating a Cursor

To create a cursor in SQL, you need to follow these steps:

1. Declare a cursor: The first step is to declare a cursor. You need to specify the SELECT statement that will retrieve the result set that you want to manipulate. For example:

   ```
   DECLARE cursor_name CURSOR FOR SELECT column1, column2 FROM table_name;
   ```
   
2. Open the cursor: Once you have declared the cursor, you need to open it. This will execute the SELECT statement and retrieve the result set. For example:

   ```
   OPEN cursor_name;
   ```
   
3. Fetch the data: You can now fetch the data from the cursor one row at a time. You can use the FETCH NEXT statement to retrieve the next row in the result set. For example:

   ```
   FETCH NEXT FROM cursor_name INTO variable1, variable2;
   ```
   
4. Process the data: You can now process the data that you have fetched from the cursor. You can use the variables that you defined in the FETCH NEXT statement to manipulate the data. For example:

   ```
   PRINT variable1 + ' ' + variable2;
   ```
   
5. Close the cursor: Once you have finished processing the data, you need to close the cursor. This will free up any resources that were used by the cursor. For example:

   ```
   CLOSE cursor_name;
   ```
   
6. Deallocate the cursor: Finally, you need to deallocate the cursor. This will remove the cursor from memory. For example:

   ```
   DEALLOCATE cursor_name;
   ```

### Advantages of Cursors

- Cursors enable you to manipulate data in a row-by-row manner
- Cursors can be used to retrieve large result sets that cannot be retrieved in a single query
- Cursors can be used to manipulate data from multiple tables
- Cursors can be used to update or delete rows in a result set

### Disadvantages of Cursors

- Cursors can be slow and use a lot of system resources
- Cursors can cause lock contention and reduce concurrency
- Cursors can make code difficult to read and maintain

### Example

Here is an example of how to create a cursor in SQL:

```
DECLARE employee_cursor CURSOR FOR SELECT id, name FROM employees;
OPEN employee_cursor;
FETCH NEXT FROM employee_cursor INTO @id, @name;
WHILE @@FETCH_STATUS = 0
BEGIN
    PRINT 'Employee ID: ' + CAST(@id AS VARCHAR(10)) + ', Name: ' + @name;
    FETCH NEXT FROM employee_cursor INTO @id, @name;
END
CLOSE employee_cursor;
DEALLOCATE employee_cursor;
```

This example retrieves the ID and name of each employee from the employees table and prints them to the console.

### Applications

Cursors are commonly used in the following scenarios:

- Processing data in a row-by-row manner
- Retrieving large result sets that cannot be retrieved in a single query
- Manipulating data from multiple tables
- Updating or deleting rows in a result set

Overall, cursors can be a powerful tool for manipulating data in SQL. However, they should be used with caution as they can be slow and resource-intensive.