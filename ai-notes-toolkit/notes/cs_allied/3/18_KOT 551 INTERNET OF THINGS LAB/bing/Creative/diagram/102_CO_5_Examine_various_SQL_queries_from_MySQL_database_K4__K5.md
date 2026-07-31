# CO 5 Examine various SQL queries from MySQL database K4, K5

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases.
- MySQL is a relational database management system (RDBMS) that supports different back ends, several different client programs and libraries, administrative tools, and a wide range of application-programming interfaces (APIs) .
- MySQL is the world’s most popular open source database, and it powers many of the most accessed applications, such as Facebook, Twitter, Netflix, Uber, Airbnb, Shopify, and Booking.com .
- MySQL Database Service is a fully managed database service to deploy cloud-native applications. HeatWave, an integrated, high-performance analytics engine, accelerates MySQL performance by 400x .
- SQL queries are statements that are used to perform various operations on data, such as selecting, inserting, updating, deleting, creating, altering, and dropping tables, views, indexes, and other database objects.
- SQL queries can be executed from MySQL client programs, such as mysql, mysqladmin, mysqldump, or MySQL Workbench, or from application code that uses MySQL APIs, such as PHP, Java, Python, or C#.
- SQL queries follow a basic syntax that consists of keywords, clauses, expressions, operators, and functions. The syntax can vary depending on the type and purpose of the query.
- SQL queries can be classified into two main categories: data definition language (DDL) and data manipulation language (DML).
  - DDL queries are used to define the structure and schema of the database, such as creating, altering, and dropping tables, views, indexes, and other database objects.
  - DML queries are used to manipulate the data in the database, such as selecting, inserting, updating, and deleting records from tables and views.
- Some examples of SQL queries from MySQL database are:

  - Creating a table named customers with four columns: id, name, email, and phone.

    ```sql
    CREATE TABLE customers (
      id INT PRIMARY KEY,
      name VARCHAR(50) NOT NULL,
      email VARCHAR(50) UNIQUE,
      phone VARCHAR(15)
    );
    ```

  - Inserting three records into the customers table.

    ```sql
    INSERT INTO customers (id, name, email, phone) VALUES
    (1, 'Alice', 'alice@example.com', '1234567890'),
    (2, 'Bob', 'bob@example.com', '2345678901'),
    (3, 'Charlie', 'charlie@example.com', '3456789012');
    ```

  - Selecting all records from the customers table.

    ```sql
    SELECT * FROM customers;
    ```

  - Updating the phone number of the customer with id 2.

    ```sql
    UPDATE customers SET phone = '4567890123' WHERE id = 2;
    ```

  - Deleting the record of the customer with id 3.

    ```sql
    DELETE FROM customers WHERE id = 3;
    ```

  - Creating a view named customer_info that shows the name and email of the customers.

    ```sql
    CREATE VIEW customer_info AS
    SELECT name, email FROM customers;
    ```

  - Selecting all records from the customer_info view.

    ```sql
    SELECT * FROM customer_info;
    ```

  - Dropping the customer_info view.

    ```sql
    DROP VIEW customer_info;
    ```

  - Creating an index named email_idx on the email column of the customers table.

    ```sql
    CREATE INDEX email_idx ON customers (email);
    ```

  - Dropping the email_idx index.

    ```sql
    DROP INDEX email_idx ON customers;
    ```

- For more information and examples of SQL queries from MySQL database, please refer to the official MySQL documentation .