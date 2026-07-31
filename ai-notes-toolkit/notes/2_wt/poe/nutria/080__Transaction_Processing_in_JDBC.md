
#### Transaction Processing in JDBC

1. JDBC (Java Database Connectivity) is an application programming interface (API) that allows Java applications to access and manipulate data stored in a database. 
2. JDBC provides two levels of transaction processing: local transaction and global transaction. 
3. Local transaction is used to process a single database transaction and global transaction is used to process multiple database transactions.
4. When using local transaction, the transaction is processed in the same database connection and the changes are committed or rolled back depending on the result of the transaction. 
5. When using global transaction, the transaction is processed in multiple database connections and the changes are committed or rolled back depending on the result of the transaction. 
6. JDBC provides methods to start, commit, and rollback a transaction. 
7. The commit() method is used to commit a transaction and the rollback() method is used to rollback a transaction. 
8. The setAutoCommit() method is used to set the auto-commit mode for a connection. 
9. The getAutoCommit() method is used to get the auto-commit mode for a connection. 
10. The setTransactionIsolation() method is used to set the transaction isolation level for a connection. 
11. The getTransactionIsolation() method is used to get the transaction isolation level for a connection.