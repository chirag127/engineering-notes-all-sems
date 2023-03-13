#### Manipulating in JDBC

Manipulating data in a database is an essential part of any application that interacts with a database. JDBC (Java Database Connectivity) is a powerful API that enables Java programs to interact with databases. In this section, we will discuss how to manipulate data using JDBC.

Manipulating data in a database involves inserting, updating, and deleting records. Here are the steps involved in manipulating data using JDBC:

1. Establish a connection to the database: To manipulate data in a database, you need to establish a connection to the database. You can use the DriverManager class to establish a connection to the database.

2. Create a statement: Once you have established a connection to the database, you need to create a statement object. You can use the createStatement() method of the Connection class to create a statement object.

3. Execute the SQL statement: Once you have created a statement object, you need to execute the SQL statement. You can use the executeUpdate() method of the Statement class to execute the SQL statement. The executeUpdate() method returns the number of rows affected by the SQL statement.

4. Close the statement and connection: Once you have executed the SQL statement, you need to close the statement object and the connection object. You can use the close() method of the Statement and Connection classes to close the statement and connection objects.

Here are some examples of how to manipulate data using JDBC:

- Inserting data into a database:

```
String sql = "INSERT INTO employee (id, name, age) VALUES (1, 'John Doe', 35)";
Statement statement = connection.createStatement();
int rowsAffected = statement.executeUpdate(sql);
statement.close();
connection.close();
```

- Updating data in a database:

```
String sql = "UPDATE employee SET age = 36 WHERE id = 1";
Statement statement = connection.createStatement();
int rowsAffected = statement.executeUpdate(sql);
statement.close();
connection.close();
```

- Deleting data from a database:

```
String sql = "DELETE FROM employee WHERE id = 1";
Statement statement = connection.createStatement();
int rowsAffected = statement.executeUpdate(sql);
statement.close();
connection.close();
```

Advantages of manipulating data using JDBC:

- JDBC provides a simple and easy-to-use API for interacting with databases.
- JDBC allows you to write database-independent code.
- JDBC provides support for transactions.

Disadvantages of manipulating data using JDBC:

- JDBC can be verbose and tedious to use.
- JDBC does not provide object-relational mapping (ORM) capabilities.

In conclusion, manipulating data using JDBC is a fundamental skill for any Java developer who wants to interact with databases. By following the steps outlined in this section, you can easily insert, update, and delete data from a database using JDBC.