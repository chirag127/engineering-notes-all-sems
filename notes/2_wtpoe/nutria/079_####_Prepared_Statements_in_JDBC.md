

### Prepared Statements in JDBC

A **Prepared Statement** is a special type of statement in Java Database Connectivity (JDBC) that is used to execute pre-compiled SQL statements. This type of statement is useful for preventing SQL injection attacks, as it allows the programmer to separate the data from the SQL code.

* Advantages
  * Prevents SQL injection attacks
  * Improves performance by pre-compiling the statement
  * Allows for parameterized queries

* Disadvantages
  * Requires more coding
  * Can be difficult to debug

* Mnemonics and Learning Tricks
  * P - Prepare
  * S - Statements
  * J - Java
  * D - Database
  * B - Connectivity

* Examples
  * `PreparedStatement pstmt = conn.prepareStatement("SELECT * FROM users WHERE user_id = ?");`
  * `pstmt.setInt(1, userID);`
  * `ResultSet rs = pstmt.executeQuery();`

* Applications
  * Used for secure database operations
  * Used for executing large batches of SQL statements
  * Used for executing stored procedures