# Joins for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- Joins are operations in relational databases that allow queries across multiple tables by matching rows that satisfy a join condition .
- Joins are based on the relational algebra operation of the same name, which is a combination of Cartesian product and selection .
- Joins are useful for retrieving data from related tables and combining them in a single result table  .
- The prerequisite for using joins is that the tables have foreign key relationships, which link them by a common attribute  .
- There are different types of joins, each with a different syntax and result  . Some of the most common ones are:

  - Theta join: A join that uses a comparison operator other than equality to match rows from different tables. The join condition is denoted by the symbol θ.
  - Equijoin: A join that uses only the equality operator to match rows from different tables. It is a special case of theta join .
  - Natural join: A join that matches rows from different tables based on the common attributes with the same name and data type. It does not use any comparison operator or explicit join condition .
  - Outer join: A join that includes rows from one or both tables that do not have matching rows in the other table. There are three types of outer joins: left, right, and full   .
    - Left outer join: A join that includes all rows from the left table and only the matching rows from the right table   .
    - Right outer join: A join that includes all rows from the right table and only the matching rows from the left table   .
    - Full outer join: A join that includes all rows from both tables, regardless of whether they have matching rows in the other table   .

- The syntax for joins varies depending on the database system and the type of join. However, a general form of a join query is:

  ```sql
  SELECT column_list
  FROM table1 JOIN_TYPE table2
  ON join_condition;
  ```

  where `JOIN_TYPE` is one of the join types mentioned above, and `join_condition` is the expression that specifies how to match rows from both tables .

- Here is an example of a join query that uses the natural join type to combine data from two tables: `employees` and `departments`:

  ```sql
  SELECT employees.first_name, employees.last_name, departments.name
  FROM employees NATURAL JOIN departments;
  ```

  This query will return the first name, last name, and department name of each employee, assuming that both tables have a common attribute called `department_id`.

- Here is another example of a join query that uses the left outer join type to combine data from two tables: `customers` and `orders`:

  ```sql
  SELECT customers.customer_id, customers.name, orders.order_id, orders.total
  FROM customers LEFT OUTER JOIN orders
  ON customers.customer_id = orders.customer_id;
  ```

  This query will return the customer ID, name, order ID, and total of each customer and their orders, as well as the customers who have not placed any orders.