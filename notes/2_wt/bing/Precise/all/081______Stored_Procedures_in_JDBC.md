#### Stored Procedures in JDBC

Stored procedures are pre-compiled SQL statements that are stored in a database. They can be called from a Java program using JDBC (Java Database Connectivity) API. Here are some key points to remember when working with stored procedures in JDBC:

1. To call a stored procedure, you need to use the `CallableStatement` interface, which extends the `PreparedStatement` interface. You can create a `CallableStatement` object using the `prepareCall()` method of the `Connection` interface.

2. The syntax for calling a stored procedure is `{call procedure_name(?, ?, ...)}` where `?` represents a parameter. You can set the values of the parameters using the `setXXX()` methods of the `CallableStatement` interface, where `XXX` is the data type of the parameter.

3. If the stored procedure returns a result set, you can retrieve it using the `executeQuery()` method of the `CallableStatement` interface. If the stored procedure does not return a result set, you can use the `executeUpdate()` method to execute it.

4. You can also register output parameters for a stored procedure using the `registerOutParameter()` method of the `CallableStatement` interface. After executing the stored procedure, you can retrieve the values of the output parameters using the `getXXX()` methods of the `CallableStatement` interface.

5. Stored procedures can improve the performance of your database operations by reducing the network traffic between the application and the database server. They can also help to encapsulate complex database operations and make them easier to manage.

Here is an example of how to call a stored procedure using JDBC:

```java
Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb", "user", "password");
CallableStatement cstmt = conn.prepareCall("{call my_procedure(?, ?)}");
cstmt.setInt(1, 123);
cstmt.registerOutParameter(2, Types.VARCHAR);
cstmt.executeUpdate();
String outputValue = cstmt.getString(2);
cstmt.close();
conn.close();
```

In this example, we are calling a stored procedure named `my_procedure` with two parameters. The first parameter is an input parameter of type `INT` and the second parameter is an output parameter of type `VARCHAR`. We set the value of the first parameter using the `setInt()` method and register the second parameter as an output parameter using the `registerOutParameter()` method. After executing the stored procedure using the `executeUpdate()` method, we retrieve the value of the output parameter using the `getString()` method.

Mnemonic: **C**allable**S**tatement **C**alls **S**tored **P**rocedures.