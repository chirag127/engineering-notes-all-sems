# Unit 5 - Design server site applications using JDDC,ODBC and section tracking API

## Introduction

- JDDC stands for Java Database Connectivity, which is an API that allows Java applications to interact with various types of databases.
- ODBC stands for Open Database Connectivity, which is an API that allows applications written in different languages and platforms to access databases using a common interface.
- Section tracking API is an API that allows web applications to maintain state information across multiple requests from the same client.

## Creating a table with name, password, email-id, and phone number fields

- To create a table with the required fields, we need to use the SQL statement `CREATE TABLE` with the appropriate data types and constraints for each field.
- For example, we can use the following SQL statement to create a table named `users` with the four fields:

```sql
CREATE TABLE users (
  name VARCHAR(50) NOT NULL,
  password VARCHAR(20) NOT NULL,
  email_id VARCHAR(50) UNIQUE NOT NULL,
  phone_number VARCHAR(15) UNIQUE NOT NULL
);
```

- The data type `VARCHAR(n)` means a variable-length character string with a maximum length of `n` characters.
- The constraint `NOT NULL` means that the field cannot be empty or missing.
- The constraint `UNIQUE` means that the field cannot have duplicate values in the table.

## Using JDDC, ODBC, and section tracking API to design server site applications

- To use JDDC, ODBC, and section tracking API to design server site applications, we need to follow these steps:

  - Load the appropriate driver for the database we want to connect to. For example, if we want to use MySQL database, we can load the driver using the following Java code:

  ```java
  Class.forName("com.mysql.jdbc.Driver");
  ```

  - Establish a connection to the database using the driver. For example, we can use the following Java code to connect to a MySQL database named `webtech` with the username `root` and the password `password`:

  ```java
  Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/webtech", "root", "password");
  ```

  - Create a statement object to execute SQL queries. For example, we can use the following Java code to create a statement object:

  ```java
  Statement stmt = con.createStatement();
  ```

  - Execute the SQL queries using the statement object and process the results. For example, we can use the following Java code to insert a new user into the `users` table and retrieve all the users from the table:

  ```java
  // Insert a new user
  String sql = "INSERT INTO users VALUES ('Alice', '1234', 'alice@gmail.com', '111-222-3333')";
  int rows = stmt.executeUpdate(sql); // returns the number of rows affected by the query
  System.out.println("Inserted " + rows + " row(s)");

  // Retrieve all the users
  sql = "SELECT * FROM users";
  ResultSet rs = stmt.executeQuery(sql); // returns a result set object that contains the query results
  while (rs.next()) { // loop through the result set
    // get the values of each field using the column name or index
    String name = rs.getString("name");
    String password = rs.getString(2);
    String email_id = rs.getString("email_id");
    String phone_number = rs.getString(4);
    // print the values
    System.out.println(name + " " + password + " " + email_id + " " + phone_number);
  }
  ```

  - Close the connection, statement, and result set objects when done. For example, we can use the following Java code to close the objects:

  ```java
  rs.close();
  stmt.close();
  con.close();
  ```

- To use ODBC, we need to use a JDBC-ODBC bridge driver that converts the JDBC API calls to ODBC API calls and vice versa. For example, we can use the following Java code to load the bridge driver:

```java
Class.forName("sun.jdbc.odbc.JdbcOdbcDriver");
```

- Then, we can use the same JDBC API methods as before, but with a different connection URL that specifies the ODBC data source name (DSN) that we have configured for the database. For example, we can use the following Java code to connect to a MySQL database using ODBC:

```java
Connection con = DriverManager.getConnection("jdbc:odbc:

```
