### Aggregate Functions

- Aggregate functions are special functions in SQL that perform calculations on a set of values and return a single value.
- Aggregate functions can be used to summarize numerical data, such as finding the average, minimum, maximum, sum, or count of a column.
- Aggregate functions can also be used to combine values from different rows into a single value, such as concatenating strings or calculating checksums.
- Aggregate functions can be used with the `GROUP BY` clause to group the rows by a certain column or expression and apply the aggregate function to each group.
- Aggregate functions can also be used with the `HAVING` clause to filter the groups based on a certain condition.
- Some of the common aggregate functions in SQL are:

  - `AVG(column_name)` returns the average value of a numeric column.
  - `COUNT(column_name)` returns the number of non-null values in a column.
  - `COUNT(*)` returns the number of rows in a table or group.
  - `MAX(column_name)` returns the maximum value in a column.
  - `MIN(column_name)` returns the minimum value in a column.
  - `SUM(column_name)` returns the sum of the values in a numeric column.
  - `STRING_AGG(column_name, separator)` returns a string that concatenates the values in a column with a specified separator.
  - `CHECKSUM_AGG(column_name)` returns a checksum value that can be used to verify the integrity of the data in a column.

- Here are some examples of using aggregate functions in SQL:

  - To find the average salary of all employees:

    ```sql
    SELECT AVG(salary) FROM employees;
    ```

  - To find the number of employees in each department:

    ```sql
    SELECT department, COUNT(*) FROM employees GROUP BY department;
    ```

  - To find the highest salary in each department:

    ```sql
    SELECT department, MAX(salary) FROM employees GROUP BY department;
    ```

  - To find the total sales amount for each product:

    ```sql
    SELECT product, SUM(amount) FROM sales GROUP BY product;
    ```

  - To find the names of the products that have more than 10 sales:

    ```sql
    SELECT product FROM sales GROUP BY product HAVING COUNT(*) > 10;
    ```

  - To find the list of customers and their orders separated by commas:

    ```sql
    SELECT customer, STRING_AGG(order_id, ',') FROM orders GROUP BY customer;
    ```

  - To find the checksum value of the order_id column:

    ```sql
    SELECT CHECKSUM_AGG(order_id) FROM orders;
    ```