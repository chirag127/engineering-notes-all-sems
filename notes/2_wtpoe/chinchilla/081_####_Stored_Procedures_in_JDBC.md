#### Stored Procedures in JDBC

Stored procedures are pre-compiled SQL statements that are stored in a database and can be executed by calling them from an application. JDBC (Java Database Connectivity) is a Java API that provides a standard way of accessing relational databases. JDBC can be used to execute stored procedures in a database.

Stored procedures in JDBC can be used to perform complex database operations that require multiple SQL statements. They can also be used to improve the performance of database operations by reducing the amount of data that needs to be transferred between the database and the application.

##### Syntax for executing stored procedures in JDBC

The syntax for executing a stored procedure in JDBC is as follows:

```
CallableStatement stmt = connection.prepareCall("{call stored_procedure_name(?, ?, ...)}");
stmt.setXXX(parameter_index, parameter_value);
stmt.execute();
```

- `CallableStatement` is a JDBC interface that represents a stored procedure call. 
- `connection.prepareCall()` method is used to prepare a `CallableStatement` object that represents a call to a stored procedure.
- `{call stored_procedure_name(?, ?, ...)}` is the SQL statement that represents the stored procedure call. The `{call ...}` syntax is used to indicate that this is a stored procedure call.
- `stmt.setXXX(parameter_index, parameter_value)` is used to set the input parameters to the stored procedure. `XXX` represents the data type of the parameter. The `parameter_index` is the position of the parameter in the stored procedure call (starting from 1), and `parameter_value` is the value of the parameter.
- `stmt.execute()` is used to execute the stored procedure.

##### Advantages of using stored procedures in JDBC

- Improved performance: Stored procedures can be pre-compiled and optimized, which can improve the performance of database operations.
- Reusability: Stored procedures can be reused by different applications, which can save development time and reduce code duplication.
- Security: Stored procedures can be used to enforce security constraints in the database, as they can be executed with different permissions than the application that calls them.
- Encapsulation: Stored procedures can encapsulate complex database operations, which can simplify the application code and improve maintainability.

##### Disadvantages of using stored procedures in JDBC

- Database vendor lock-in: Stored procedures are specific to a particular database vendor and may not be portable to other databases.
- Complexity: Stored procedures can be complex to develop and maintain, especially for complex database operations.
- Limited functionality: Stored procedures may not support all the features of SQL, which can limit their functionality.

##### Examples of stored procedures in JDBC

Here is an example of a stored procedure that calculates the average salary of employees in a department:

```
CREATE PROCEDURE avg_salary(IN dept_id INT, OUT avg_sal DECIMAL(10,2))
BEGIN
  SELECT AVG(salary) INTO avg_sal FROM employees WHERE department_id = dept_id;
END
```

Here is how the stored procedure can be called from a Java application using JDBC:

```
CallableStatement stmt = connection.prepareCall("{call avg_salary(?, ?)}");
stmt.setInt(1, 10); // set the department ID input parameter
stmt.registerOutParameter(2, Types.DECIMAL); // register the output parameter
stmt.execute();
BigDecimal avgSal = stmt.getBigDecimal(2); // get the output parameter value
```

##### Mnemonic for executing stored procedures in JDBC

One mnemonic for executing stored procedures in JDBC is the acronym `CSE`:

- `C` stands for `CallableStatement`, the JDBC interface used to represent a stored procedure call.
- `S` stands for `setXXX()`, the method used to set input parameters to the stored procedure.
- `E` stands for `execute()`, the method used to execute the stored procedure.