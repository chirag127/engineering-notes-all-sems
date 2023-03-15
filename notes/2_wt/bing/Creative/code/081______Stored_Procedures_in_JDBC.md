#### Stored Procedures in JDBC

A stored procedure is a precompiled SQL statement that can be executed by the database server. Stored procedures can improve the performance and security of database applications by reducing the network traffic and enforcing access control. To call a stored procedure from a JDBC program, you need to follow these steps:

- Create a CallableStatement object using the Connection.prepareCall() method. The SQL statement passed to this method should use the syntax {call procedure_name(?, ?, ...)} where ? represents a parameter placeholder.
- Set the input parameters (if any) using the appropriate setter methods of the CallableStatement object. For example, setInt(), setString(), etc. The index of the first parameter is 1, and it increases by one for each parameter.
- Register the output parameters (if any) using the registerOutParameter() method of the CallableStatement object. You need to specify the index and the SQL type of the output parameter. For example, registerOutParameter(2, Types.INTEGER) means that the second parameter is an integer output parameter.
- Execute the stored procedure using the execute() or executeUpdate() method of the CallableStatement object. The execute() method returns a boolean value indicating whether the stored procedure returns a ResultSet object or not. The executeUpdate() method returns an int value indicating the number of rows affected by the stored procedure.
- Retrieve the output parameters (if any) using the appropriate getter methods of the CallableStatement object. For example, getInt(), getString(), etc. You need to specify the index of the output parameter. For example, getInt(2) means that the second parameter is an integer output parameter.
- Close the CallableStatement object using the close() method.

Here is an example of calling a stored procedure named addNumbers that takes two integer input parameters and returns their sum as an output parameter:

```java
// Step 1: Create a CallableStatement object
CallableStatement cs = conn.prepareCall("{call addNumbers(?, ?)}");

// Step 2: Set the input parameters
cs.setInt(1, 10); // set the first parameter to 10
cs.setInt(2, 20); // set the second parameter to 20

// Step 3: Register the output parameter
cs.registerOutParameter(3, Types.INTEGER); // register the third parameter as an integer output parameter

// Step 4: Execute the stored procedure
cs.executeUpdate();

// Step 5: Retrieve the output parameter
int result = cs.getInt(3); // get the value of the third parameter
System.out.println("The sum is " + result);

// Step 6: Close the CallableStatement object
cs.close();
```