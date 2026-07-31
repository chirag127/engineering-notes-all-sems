### Connecting to a Database Using Java Program/Servlet/JSP

In the subject of Web Technology Lab, Unit 5 focuses on designing server site applications using JDBC, ODBC, and section tracking API. In this unit, you will learn how to connect to a database using a Java program/servlet/JSP and extract data from tables to display it.

To connect to a database and extract data from tables, follow these steps:

1. Import the required packages: The first step is to import the necessary packages for connecting to a database. You can use the following packages:

   ```java
   import java.sql.Connection;
   import java.sql.DriverManager;
   import java.sql.ResultSet;
   import java.sql.Statement;
   ```

2. Load the JDBC driver: To connect to a database, you need to load the JDBC driver for the database you are using. For example, if you are using MySQL, you can use the following code:

   ```java
   Class.forName("com.mysql.jdbc.Driver");
   ```

3. Establish a connection: Once you have loaded the JDBC driver, you can establish a connection to the database using the following code:

   ```java
   String url = "jdbc:mysql://localhost:3306/mydatabase";
   String username = "root";
   String password = "password";

   Connection con = DriverManager.getConnection(url, username, password);
   ```

   In this code, `url` specifies the database URL, `username` and `password` are the database credentials.

4. Create a statement: Once the connection is established, create a statement object using the `createStatement()` method of the `Connection` interface:

   ```java
   Statement stmt = con.createStatement();
   ```

5. Execute the query: Use the `executeQuery()` method of the `Statement` interface to execute a SQL query:

   ```java
   String sql = "SELECT * FROM mytable";
   ResultSet rs = stmt.executeQuery(sql);
   ```

   In this code, `sql` is the SQL query to be executed, and `rs` is the `ResultSet` object that holds the result of the query.

6. Display the result: Finally, iterate through the `ResultSet` object to display the result:

   ```java
   while (rs.next()) {
       int id = rs.getInt("id");
       String name = rs.getString("name");
       int age = rs.getInt("age");

       System.out.println("ID: " + id + ", Name: " + name + ", Age: " + age);
   }
   ```

   In this code, `getInt()`, `getString()`, and `getInt()` methods are used to retrieve data from the `ResultSet` object.

7. Close the connection: After the data is extracted, close the connection using the `close()` method of the `Connection` interface:

   ```java
   con.close();
   ```

By following these steps, you can connect to a database using a Java program/servlet/JSP and extract data from tables to display it.