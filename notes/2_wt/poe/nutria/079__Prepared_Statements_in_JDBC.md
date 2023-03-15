
#### Prepared Statements in JDBC

* Prepared Statements are pre-compiled SQL statements which are used to execute the same or similar SQL statements multiple times. 
* Prepared Statements can be used to execute dynamic SQL statements more efficiently.
* Prepared Statements are created using the Connection object's prepareStatement() method. 
* Prepared Statements are used to avoid SQL injection attacks.
* Prepared Statements are faster than Statement objects as the Prepared Statements are pre-compiled and stored in a PreparedStatement object.
* Prepared Statements can accept parameters which can be set using the setXXX() methods.
* Prepared Statements can be used for batch updates. 
* Prepared Statements support the use of stored procedures.