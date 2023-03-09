 Here is the content in markdown format for the topic ### recovery from transaction failures for the notes of the Unit 7 - Transaction Processing Concepts in the subject of Basics of Data Base Management System:

### Recovery from Transaction Failures

- Transaction failures can occur due to system crashes, errors, etc. The database may be left in an inconsistent state after such failures.
- Recovery techniques are used to undo the effects of incomplete transactions and restore the database to a consistent state. The following are the main recovery techniques:

1. Logging: All transaction updates to the database are first logged (recorded) in a log file before being applied to the actual database. In case of a failure, the log is used to undo the incomplete transactions. The database is restored to the state before the start of the incomplete transaction by undoing the changes recorded in the log. This ensures atomicity of transactions.

2. Checkpointing: The state of the database is periodically saved in a checkpoint. In case of a failure, recovery needs to be done only from the latest checkpoint rather than from the start. This makes the recovery process much faster. The checkpoint data can be used to identify incomplete transactions and undo their effects to restore consistency.

3. Shadow paging: The original data values are temporarily stored in a shadow page when a transaction updates a data item. If the transaction completes successfully, the shadow page updates are merged into the actual database. Otherwise, the values in the shadow page are discarded and the original values in the database are retained. This ensures that only committed transactions affect the database.

- The logging and checkpointing techniques can be used together to improve performance during normal execution and recovery. Recovery management is an important function of a database system to maintain data consistency and reliability.

- Diagrams and examples can be included to illustrate the recovery techniques. The advantages and disadvantages of the techniques and their applications can also be discussed. The content can be expanded with more details and points as needed.