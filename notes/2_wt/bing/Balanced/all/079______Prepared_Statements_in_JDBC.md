#### Prepared Statements in JDBC

- A prepared statement is a precompiled SQL statement that can be executed multiple times with different parameters.
- A prepared statement is created by calling the `prepareStatement` method of the `Connection` interface, passing the SQL query as a parameter.
- A prepared statement can have one or more placeholders (`?`) that represent the parameters to be supplied at runtime.
- A prepared statement can improve the performance and security of the application, as it reduces the parsing and compilation overhead, and prevents SQL injection attacks.
- A prepared statement can be executed by calling the `execute`, `executeQuery`, or `executeUpdate` methods of the `PreparedStatement` interface, passing the values for the parameters as arguments.
- A prepared statement can also be used to perform batch updates, by adding multiple sets of parameters using the `addBatch` method, and executing them using the `executeBatch` method.

Example:

```java
//Create a prepared statement to insert a record into the student table
PreparedStatement ps = conn.prepareStatement("insert into student values(?,?,?)");

//Set the values for the parameters
ps.setInt(1, 101); //first parameter is the roll number
ps.setString(2, "Alice"); //second parameter is the name
ps.setFloat(3, 95.5f); //third parameter is the marks

//Execute the prepared statement
int rows = ps.executeUpdate();

//Check the number of rows affected
if(rows > 0){
  System.out.println("Record inserted successfully");
}else{
  System.out.println("Record insertion failed");
}

//Close the prepared statement
ps.close();
```

Mnemonic:

- A prepared statement is like a **template** that can be filled with different values and executed repeatedly.
- A prepared statement has **placeholders** (`?`) that represent the parameters to be supplied at runtime.
- A prepared statement can improve the **performance** and **security** of the application, as it reduces the parsing and compilation overhead, and prevents SQL injection attacks.
- A prepared statement can be used to perform **batch updates**, by adding multiple sets of parameters and executing them together.