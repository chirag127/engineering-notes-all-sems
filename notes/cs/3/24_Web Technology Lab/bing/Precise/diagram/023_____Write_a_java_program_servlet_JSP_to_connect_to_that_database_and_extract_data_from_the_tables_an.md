### Java Program to Connect to Database and Extract Data from Tables

To connect to a database and extract data from tables using Java, you can use the JDBC (Java Database Connectivity) API. JDBC provides a standard interface for accessing relational databases from Java programs.

Here are the steps to connect to a database and extract data from tables using JDBC:

1. **Load the JDBC driver**: The first step is to load the JDBC driver for the database you want to connect to. This is done using the `Class.forName()` method. For example, to load the MySQL JDBC driver, you would use the following code:

```java
Class.forName("com.mysql.jdbc.Driver");
```

2. **Establish a connection**: Once the driver is loaded, you can establish a connection to the database using the `DriverManager.getConnection()` method. This method takes the database URL, username, and password as arguments. For example, to connect to a MySQL database running on the local machine, you would use the following code:

```java
String url = "jdbc:mysql://localhost:3306/database_name";
String username = "username";
String password = "password";
Connection conn = DriverManager.getConnection(url, username, password);
```

3. **Create a statement**: Once you have a connection to the database, you can create a `Statement` object to execute SQL queries. This is done using the `Connection.createStatement()` method. For example:

```java
Statement stmt = conn.createStatement();
```

4. **Execute a query**: To execute a query, you can use the `Statement.executeQuery()` method. This method takes an SQL query as an argument and returns a `ResultSet` object containing the results of the query. For example, to execute a query that selects all rows from a table named `employees`, you would use the following code:

```java
String query = "SELECT * FROM employees";
ResultSet rs = stmt.executeQuery(query);
```

5. **Process the results**: Once you have a `ResultSet` object, you can use its methods to iterate over the rows of the result set and extract the data from the columns. For example, to print the values of the `first_name` and `last_name` columns for each row in the result set, you would use the following code:

```java
while (rs.next()) {
    String firstName = rs.getString("first_name");
    String lastName = rs.getString("last_name");
    System.out.println(firstName + " " + lastName);
}
```

6. **Close the resources**: Once you are done processing the results, you should close the resources you have used, including the `ResultSet`, `Statement`, and `Connection` objects. This is done using the `close()` method of each object. For example:

```java
rs.close();
stmt.close();
conn.close();
```

This is a basic example of how to connect to a database and extract data from tables using JDBC. You can use this as a starting point and modify it to suit your needs.