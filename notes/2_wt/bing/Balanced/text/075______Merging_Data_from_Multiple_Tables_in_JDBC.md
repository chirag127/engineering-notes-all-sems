#### Merging Data from Multiple Tables in JDBC

- JDBC stands for Java Database Connectivity, which is an API for connecting and executing queries on databases using Java.
- JDBC allows us to perform various operations on databases, such as creating, updating, deleting, and querying data.
- One of the common tasks in JDBC is to merge data from multiple tables, which means to combine the results of two or more queries into a single result set.
- There are different ways to merge data from multiple tables in JDBC, depending on the type and structure of the data, and the desired output format.
- Some of the common methods are:

  - Using JOIN clauses: A JOIN clause is a SQL keyword that allows us to combine data from two or more tables based on a common column or condition. There are different types of JOIN clauses, such as INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN, which specify how to match the rows from the tables. For example, an INNER JOIN returns only the rows that have matching values in both tables, while a LEFT JOIN returns all the rows from the left table and the matching rows from the right table. To use a JOIN clause in JDBC, we need to write a SQL query that contains the JOIN keyword and the tables and columns to join, and then execute it using a Statement or PreparedStatement object. For example:

    ```java
    // Create a SQL query that joins the customers and orders tables on the customer_id column
    String sql = "SELECT c.name, c.email, o.order_id, o.order_date FROM customers c INNER JOIN orders o ON c.customer_id = o.customer_id";

    // Create a Statement object to execute the query
    Statement stmt = conn.createStatement();

    // Execute the query and get the result set
    ResultSet rs = stmt.executeQuery(sql);

    // Loop through the result set and print the data
    while (rs.next()) {
      System.out.println(rs.getString("name") + ", " + rs.getString("email") + ", " + rs.getInt("order_id") + ", " + rs.getDate("order_date"));
    }

    // Close the result set, statement, and connection
    rs.close();
    stmt.close();
    conn.close();
    ```

  - Using UNION, INTERSECT, or EXCEPT operators: These are SQL operators that allow us to combine the results of two or more queries into a single result set, based on the set theory concepts of union, intersection, and difference. A UNION operator returns all the rows from both queries, eliminating any duplicates. An INTERSECT operator returns only the rows that are common to both queries. An EXCEPT operator returns only the rows that are in the first query but not in the second query. To use these operators in JDBC, we need to write a SQL query that contains the operator and the queries to combine, and then execute it using a Statement or PreparedStatement object. For example:

    ```java
    // Create a SQL query that returns the names of the customers who have placed orders and the names of the products they have ordered, using a UNION operator
    String sql = "SELECT c.name FROM customers c INNER JOIN orders o ON c.customer_id = o.customer_id UNION SELECT p.name FROM products p INNER JOIN order_details od ON p.product_id = od.product_id";

    // Create a Statement object to execute the query
    Statement stmt = conn.createStatement();

    // Execute the query and get the result set
    ResultSet rs = stmt.executeQuery(sql);

    // Loop through the result set and print the data
    while (rs.next()) {
      System.out.println(rs.getString("name"));
    }

    // Close the result set, statement, and connection
    rs.close();
    stmt.close();
    conn.close();
    ```

  - Using nested queries: A nested query is a SQL query that contains another SQL query as a subquery. A subquery is a query that is executed within another query and returns a single value, a row, or a table. A nested query can be used to merge data from multiple tables by using the subquery as a filter, a source, or a target for the main query. To use a nested query in JDBC, we need to write a SQL query that contains the subquery within parentheses, and then execute it using a Statement or PreparedStatement object. For example:

    ```java
    // Create a SQL query that returns the names and emails of the customers who have ordered the product with the name 'Laptop', using a nested query
    String sql = "SELECT c.name, c.email FROM customers c WHERE c.customer_id IN (SELECT o.customer_id FROM orders o INNER JOIN order_details od ON o.order_id = od.order_id INNER JOIN products p ON od.product_id = p.product_id WHERE p.name =

```
