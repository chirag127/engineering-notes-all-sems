#### Transaction Processing in JDBC

- Transaction processing is a way of ensuring the consistency and reliability of the data in a database by grouping a set of related operations into a single unit of work.
- A transaction is a set of one or more SQL statements that are executed as a unit, so either all of the statements are executed, or none of the statements is executed.
- Transactions have four properties: atomicity, consistency, isolation, and durability (ACID).
  - Atomicity means that either all the statements in a transaction are executed successfully, or none of them are executed at all. If any statement fails, the whole transaction is rolled back to the previous state.
  - Consistency means that a transaction brings the database from one valid state to another valid state, without violating any integrity constraints or business rules.
  - Isolation means that a transaction is not affected by the concurrent execution of other transactions. Each transaction sees a consistent view of the data, as if it were the only transaction running.
  - Durability means that the effects of a committed transaction are permanent and will not be lost in case of a system failure or power outage.
- JDBC supports both local and distributed transactions. Local transactions are performed on a single database connection, while distributed transactions are performed on multiple database connections that may span different databases or servers.
- By default, JDBC connections are in auto-commit mode, which means that each individual SQL statement is treated as a transaction and is automatically committed right after it is executed. To disable auto-commit mode and group multiple statements into a transaction, use the `setAutoCommit(false)` method on the connection object.
- To commit a transaction, use the `commit()` method on the connection object. To roll back a transaction, use the `rollback()` method on the connection object. Rolling back a transaction discards all the changes made by the statements in the transaction and restores the database to its previous state.
- JDBC also supports transaction savepoints, which are intermediate points within a transaction that can be used to roll back a part of the transaction, without affecting the rest of the transaction. To create a savepoint, use the `setSavepoint()` method on the connection object. To roll back to a savepoint, use the `rollback(Savepoint)` method on the connection object. To release a savepoint, use the `releaseSavepoint(Savepoint)` method on the connection object.
- JDBC also supports transaction isolation levels, which are the degree of isolation that a transaction has from the concurrent transactions. The higher the isolation level, the more protected the transaction is from the interference of other transactions, but the lower the concurrency and performance. JDBC defines four isolation levels: `TRANSACTION_READ_UNCOMMITTED`, `TRANSACTION_READ_COMMITTED`, `TRANSACTION_REPEATABLE_READ`, and `TRANSACTION_SERIALIZABLE`. To set the isolation level for a connection, use the `setTransactionIsolation(int)` method on the connection object. To get the current isolation level for a connection, use the `getTransactionIsolation()` method on the connection object.
- JDBC also supports result set holdability, which is the ability of a result set to remain open and accessible after a transaction is committed or rolled back. JDBC defines two holdability modes: `HOLD_CURSORS_OVER_COMMIT` and `CLOSE_CURSORS_AT_COMMIT`. To set the holdability mode for a connection, use the `setHoldability(int)` method on the connection object. To get the current holdability mode for a connection, use the `getHoldability()` method on the connection object.

Here is an example of transaction processing in JDBC, where a coffee sales table is updated with the sales for a week and the total sales to date. The transaction consists of two update statements, one for the sales column and one for the total column. The transaction is committed only if both statements are executed successfully, otherwise it is rolled back. The transaction also uses a savepoint to mark the point before the second update statement, in case it needs to be rolled back partially.

```java
public void updateCoffeeSales(HashMap<String, Integer> salesForWeek) throws SQLException {
  String updateString = "update COFFEES set SALES = ? where COF_NAME = ?";
  String updateStatement = "update COFFEES set TOTAL = TOTAL + ? where COF_NAME = ?";

  try (PreparedStatement updateSales = con.prepareStatement(updateString);
       PreparedStatement updateTotal = con.prepareStatement(updateStatement)) {

    con.setAutoCommit(false); // disable auto-commit mode
    Savepoint savepoint = con.setSavepoint(); // create a savepoint

    for (Map.Entry<String, Integer> e :