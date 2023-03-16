#### Manipulating in JDBC:

Java Database Connectivity (JDBC) is a standard API for connecting Java applications to databases. It enables Java programs to interact with databases using SQL statements. JDBC provides various methods to manipulate data in a database. In this section, we will discuss how to manipulate data in a database using JDBC.

Here are some important points to keep in mind when manipulating data in JDBC:

1. To manipulate data in a database using JDBC, we need to establish a connection to the database first. We can establish a connection using the DriverManager class.

2. After establishing a connection, we can create a Statement object to execute SQL statements. The Statement object is used to send SQL statements to the database and retrieve results.

3. We can execute SQL statements using the execute() method of the Statement object. The execute() method returns a boolean value, which indicates whether the SQL statement was executed successfully or not.

4. JDBC provides three types of statements: Statement, PreparedStatement, and CallableStatement. The Statement object is used to execute simple SQL statements, while PreparedStatement is used to execute parameterized SQL statements. CallableStatement is used to execute stored procedures in the database.

5. We can use the executeUpdate() method of the Statement object to execute SQL statements that modify data in the database, such as INSERT, UPDATE, and DELETE statements. The executeUpdate() method returns an integer value, which indicates the number of rows affected by the SQL statement.

6. We can use the executeQuery() method of the Statement object to execute SQL statements that retrieve data from the database, such as SELECT statements. The executeQuery() method returns a ResultSet object, which contains the data retrieved from the database.

7. We can use the ResultSet object to retrieve data from the database. The ResultSet object provides various methods to retrieve data, such as getInt(), getString(), getBoolean(), etc.

8. We can use the PreparedStatement object to execute parameterized SQL statements. Parameterized SQL statements are used to pass parameters to the SQL statement at runtime.

9. We can use the setXXX() methods of the PreparedStatement object to set values for the parameters in the SQL statement. The setXXX() methods are used to set values for different types of parameters, such as integers, strings, dates, etc.

10. We can use the executeUpdate() method of the PreparedStatement object to execute parameterized SQL statements that modify data in the database. The executeUpdate() method returns an integer value, which indicates the number of rows affected by the SQL statement.

11. We can use the executeQuery() method of the PreparedStatement object to execute parameterized SQL statements that retrieve data from the database. The executeQuery() method returns a ResultSet object, which contains the data retrieved from the database.

12. We can use the CallableStatement object to execute stored procedures in the database. Stored procedures are precompiled SQL statements that can be executed multiple times with different parameters.

13. We can use the registerOutParameter() method of the CallableStatement object to register output parameters for the stored procedure. Output parameters are used to return values from the stored procedure to the Java program.

14. We can use the execute() method of the CallableStatement object to execute the stored procedure. The execute() method returns a boolean value, which indicates whether the stored procedure was executed successfully or not.

In conclusion, manipulating data in JDBC involves establishing a connection to the database, creating a Statement object to execute SQL statements, and using various methods to manipulate data in the database. It is important to understand the different types of statements provided by JDBC and how to use them to manipulate data in the database.