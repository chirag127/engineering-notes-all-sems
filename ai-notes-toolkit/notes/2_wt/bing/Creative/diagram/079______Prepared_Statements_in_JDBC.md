#### Prepared Statements in JDBC
A prepared statement is a special type of statement that allows you to execute parameterized queries against the database. A parameterized query is a query that contains placeholders (represented by ? symbols) for the values that will be supplied at runtime. A prepared statement is precompiled by the database and can be executed multiple times with different values for the parameters.

A prepared statement has the following advantages over a regular statement:

- It improves performance by reducing the parsing and compiling overhead for the database.
- It prevents SQL injection attacks by escaping the values of the parameters automatically.
- It makes the code more readable and maintainable by separating the SQL syntax from the data values.

To use a prepared statement, you need to follow these steps:

1. Create a PreparedStatement object by calling the prepareStatement() method of the Connection object with the SQL query as an argument. For example:

```java
PreparedStatement ps = conn.prepareStatement("INSERT INTO EMPLOYEE VALUES (?, ?, ?)");
```

2. Set the values for the parameters by calling the appropriate setter methods of the PreparedStatement object. The first argument of these methods is the index of the parameter (starting from 1), and the second argument is the value to be set. For example:

```java
ps.setInt(1, 101); // set the first parameter to 101
ps.setString(2, "John"); // set the second parameter to "John"
ps.setDouble(3, 5000.0); // set the third parameter to 5000.0
```

3. Execute the prepared statement by calling the execute(), executeQuery(), or executeUpdate() methods of the PreparedStatement object. For example:

```java
int rows = ps.executeUpdate(); // execute the insert statement and get the number of affected rows
```

4. Close the prepared statement by calling the close() method of the PreparedStatement object. For example:

```java
ps.close(); // close the prepared statement
```

The following diagram illustrates the flow of using a prepared statement:

```
+-----------------+        +-----------------+        +-----------------+
| Java Application|        | JDBC Driver     |        | Database        |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
| 1. Create       |------->| 1. Prepare      |------->| 1. Compile      |
| PreparedStatement|        | PreparedStatement|        | SQL query       |
|                 |        |                 |        |                 |
| 2. Set          |------->| 2. Set          |------->| 2. Bind         |
| parameters      |        | parameters      |        | parameters      |
|                 |        |                 |        |                 |
| 3. Execute      |------->| 3. Execute      |------->| 3. Execute      |
| PreparedStatement|        | PreparedStatement|        | SQL query       |
|                 |        |                 |        |                 |
| 4. Close        |------->| 4. Close        |------->| 4. Close        |
| PreparedStatement|        | PreparedStatement|        | SQL query       |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
```