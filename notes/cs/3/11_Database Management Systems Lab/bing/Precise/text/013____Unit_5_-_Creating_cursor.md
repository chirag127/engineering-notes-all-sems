## Unit 5 - Creating cursor

A cursor is a control structure that enables traversal over the records in a database. Cursors allow you to iterate over a set of rows returned by a query and process each row individually. Here are the steps to create a cursor:

1. **Declare the cursor:** The first step in creating a cursor is to declare it. This is done using the `DECLARE CURSOR` statement. The syntax for declaring a cursor is as follows:
```
DECLARE cursor_name CURSOR FOR
SELECT_statement;
```
2. **Open the cursor:** Once the cursor is declared, it needs to be opened using the `OPEN` statement. This statement executes the `SELECT` statement associated with the cursor and populates the result set.
```
OPEN cursor_name;
```
3. **Fetch rows from the cursor:** After the cursor is opened, you can fetch rows from it using the `FETCH` statement. This statement retrieves the current row from the cursor and advances the cursor to the next row.
```
FETCH NEXT FROM cursor_name
INTO @variable1, @variable2, ...;
```
4. **Close the cursor:** Once you have finished processing the rows in the cursor, you need to close it using the `CLOSE` statement. This statement releases the resources associated with the cursor.
```
CLOSE cursor_name;
```
5. **Deallocate the cursor:** The final step in working with a cursor is to deallocate it using the `DEALLOCATE` statement. This statement removes the cursor definition and releases the resources associated with it.
```
DEALLOCATE cursor_name;
```
It is important to note that cursors can have a significant impact on performance and should be used judiciously. In many cases, it is possible to achieve the same result using a combination of other SQL statements. However, in some situations, cursors can be a useful tool for working with data in a database.