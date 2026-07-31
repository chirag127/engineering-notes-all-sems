### DML for the notes of the Unit 1 - Introduction in the subject of Basics of Data Base Management System

Data Manipulation Language (DML) is a subset of SQL (Structured Query Language) used to manipulate data in a database. Here are some important points to understand about DML:

- DML is used to insert, update, and delete data from a database.

- The INSERT statement is used to add new rows to a table. The syntax for the INSERT statement is as follows:

  ```
  INSERT INTO table_name (column1, column2, column3, ...)
  VALUES (value1, value2, value3, ...);
  ```

- The UPDATE statement is used to modify existing data in a table. The syntax for the UPDATE statement is as follows:

  ```
  UPDATE table_name
  SET column1 = value1, column2 = value2, ...
  WHERE condition;
  ```

- The DELETE statement is used to remove rows from a table. The syntax for the DELETE statement is as follows:

  ```
  DELETE FROM table_name
  WHERE condition;
  ```

- DML statements are executed one at a time, and they can affect one or more rows in a table.

- DML statements can be combined with other SQL statements, such as SELECT and JOIN, to perform complex queries and data manipulations.

- It is important to use caution when using DML statements, as they can permanently modify the data in a database. It is always recommended to backup data before making any changes to a database.

Understanding DML is essential for anyone working with databases. It allows for efficient data manipulation and retrieval, and can be used to perform complex data analysis.