# CO 5: Examine Various SQL Queries from MySQL Database K4, K5

In this section, we will examine various SQL queries that can be used in the MySQL database. These queries are essential for performing various operations on the database, such as retrieving data, modifying data, and creating tables.

## Retrieving Data

1. **SELECT statement**: The SELECT statement is used to retrieve data from one or more tables. It has a basic syntax:

   ```sql
   SELECT column1, column2, ...
   FROM table_name;
   ```

   This query will retrieve all columns from the specified table. However, if we want to retrieve only specific columns, we can list them in the SELECT statement.

2. **WHERE clause**: The WHERE clause is used to filter the data retrieved by the SELECT statement based on certain conditions. It has a basic syntax:

   ```sql
   SELECT column1, column2, ...
   FROM table_name
   WHERE condition;
   ```

   The condition can be any logical expression that evaluates to true or false. For example, we can retrieve only the records where the age is greater than 18:

   ```sql
   SELECT name, age
   FROM users
   WHERE age > 18;
   ```

3. **ORDER BY clause**: The ORDER BY clause is used to sort the retrieved data in ascending or descending order. It has a basic syntax:

   ```sql
   SELECT column1, column2, ...
   FROM table_name
   ORDER BY column1 ASC/DESC;
   ```

   The ASC keyword is used for ascending order, and the DESC keyword is used for descending order. For example, we can retrieve the records from the users table sorted by age in descending order:

   ```sql
   SELECT name, age
   FROM users
   ORDER BY age DESC;
   ```

## Modifying Data

1. **INSERT statement**: The INSERT statement is used to insert new records into a table. It has a basic syntax:

   ```sql
   INSERT INTO table_name (column1, column2, ...)
   VALUES (value1, value2, ...);
   ```

   The values should be in the same order as the columns specified in the INSERT INTO statement. For example, we can insert a new record into the users table:

   ```sql
   INSERT INTO users (name, age)
   VALUES ('John Doe', 25);
   ```

2. **UPDATE statement**: The UPDATE statement is used to update existing records in a table. It has a basic syntax:

   ```sql
   UPDATE table_name
   SET column1 = value1, column2 = value2, ...
   WHERE condition;
   ```

   The condition specifies which records should be updated. For example, we can update the age of the user with the name 'John Doe':

   ```sql
   UPDATE users
   SET age = 26
   WHERE name = 'John Doe';
   ```

3. **DELETE statement**: The DELETE statement is used to delete existing records from a table. It has a basic syntax:

   ```sql
   DELETE FROM table_name
   WHERE condition;
   ```

   The condition specifies which records should be deleted. For example, we can delete the user with the name 'John Doe':

   ```sql
   DELETE FROM users
   WHERE name = 'John Doe';
   ```

## Creating Tables

1. **CREATE TABLE statement**: The CREATE TABLE statement is used to create a new table in the database. It has a basic syntax:

   ```sql
   CREATE TABLE table_name (
     column1 datatype,
     column2 datatype,
     ...
   );
   ```

   The datatype specifies the type of data that can be stored in the column. For example, we can create a new table for storing employee information:

   ```sql
   CREATE TABLE employees (
     id INT PRIMARY KEY,
     name VARCHAR(50),
     age INT,
     salary DECIMAL(10,2)
   );
   ```

2. **ALTER TABLE statement**: The ALTER TABLE statement is used to modify an existing table. It has a basic syntax:

   ```sql
   ALTER TABLE table_name
   ADD column_name datatype;
   ```

   The ADD keyword is used to add a new column to the table. For example, we can add a new column for the department:

   ```sql
   ALTER TABLE employees
   ADD department VARCHAR(50);
   ```

3. **DROP TABLE statement**: The DROP TABLE statement is used to delete an existing table from the database. It has a basic syntax:

   ```sql
   DROP TABLE table_name;
   ```

   For example, we can delete the employees table:

   ```sql
   DROP TABLE employees;
   ```

In conclusion, SQL queries are essential for performing various operations on the MySQL database, such as retrieving data, modifying data, and creating tables. By mastering these queries, you can efficiently manage your database and extract valuable insights from