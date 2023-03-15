#### Manipulating in JDBC

- JDBC stands for Java Database Connectivity, which is an API that allows Java programs to interact with various types of databases.
- To manipulate data in a database using JDBC, the following steps are typically required:
  - Load the appropriate JDBC driver class using the Class.forName() method.
  - Establish a connection to the database using the DriverManager.getConnection() method, which returns a Connection object.
  - Create a Statement object from the Connection object using the createStatement() method, which allows executing SQL queries and commands.
  - Execute the SQL statement using the executeUpdate() method of the Statement object, which returns an int value indicating the number of rows affected by the operation. Alternatively, use the executeQuery() method for queries that return a ResultSet object, which contains the data retrieved from the database.
  - Close the Statement and Connection objects using the close() method to release the resources.
- Some examples of SQL statements that can be used to manipulate data in a database are:
  - INSERT: to insert a new row into a table.
  - UPDATE: to modify the values of existing rows in a table.
  - DELETE: to remove rows from a table.
  - CREATE: to create a new table or other database object.
  - DROP: to delete a table or other database object.
  - ALTER: to change the structure or properties of a table or other database object.