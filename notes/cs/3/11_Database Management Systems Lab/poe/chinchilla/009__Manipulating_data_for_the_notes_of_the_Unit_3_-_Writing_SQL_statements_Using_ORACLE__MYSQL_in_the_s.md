### Manipulating data for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

In the previous units, we learned about the basics of SQL and how to create and manipulate tables in a database. In this unit, we will focus on manipulating data in those tables. Here are some important points to keep in mind:

- **INSERT statement**: The INSERT statement is used to insert new data into a table. The basic syntax for the INSERT statement is:

  ```
  INSERT INTO table_name (column1, column2, column3, ...)
  VALUES (value1, value2, value3, ...);
  ```

  It is important to ensure that the data being inserted matches the data type of the columns in the table.

- **UPDATE statement**: The UPDATE statement is used to modify existing data in a table. The basic syntax for the UPDATE statement is:

  ```
  UPDATE table_name
  SET column1 = value1, column2 = value2, ...
  WHERE some_column = some_value;
  ```

  The WHERE clause is used to specify which rows to update. If the WHERE clause is not specified, all rows in the table will be updated.

- **DELETE statement**: The DELETE statement is used to delete data from a table. The basic syntax for the DELETE statement is:

  ```
  DELETE FROM table_name
  WHERE some_column = some_value;
  ```

  The WHERE clause is used to specify which rows to delete. If the WHERE clause is not specified, all rows in the table will be deleted.

- **SELECT statement**: The SELECT statement is used to retrieve data from a table. The basic syntax for the SELECT statement is:

  ```
  SELECT column1, column2, ...
  FROM table_name
  WHERE some_column = some_value;
  ```

  The WHERE clause is used to filter the results based on a condition. If the WHERE clause is not specified, all rows in the table will be returned.

- **ORDER BY clause**: The ORDER BY clause is used to sort the results in ascending or descending order based on one or more columns. The basic syntax for the ORDER BY clause is:

  ```
  SELECT column1, column2, ...
  FROM table_name
  ORDER BY column1 ASC/DESC;
  ```

- **GROUP BY clause**: The GROUP BY clause is used to group the results based on one or more columns. The basic syntax for the GROUP BY clause is:

  ```
  SELECT column1, COUNT(*)
  FROM table_name
  GROUP BY column1;
  ```

  This example will group the results by column1 and count the number of occurrences of each value in column1.

- **JOIN statement**: The JOIN statement is used to combine rows from two or more tables based on a related column between them. The basic syntax for the JOIN statement is:

  ```
  SELECT table1.column1, table2.column2, ...
  FROM table1
  JOIN table2
  ON table1.related_column = table2.related_column;
  ```

  This example will join table1 and table2 based on the related_column column in both tables.

These are the basic SQL statements that are used to manipulate data in a database. It is important to understand how each statement works and how to use them effectively in order to work with databases efficiently.