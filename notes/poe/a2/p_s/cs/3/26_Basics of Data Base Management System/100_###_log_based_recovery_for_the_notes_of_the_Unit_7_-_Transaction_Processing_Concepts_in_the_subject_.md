 Here is the content in markdown format for the topic ### log based recovery for the notes of the Unit 7 - Transaction Processing Concepts in the subject of Basics of Data Base Management System:

### Log Based Recovery

- Log based recovery is a technique used to recover the database to a consistent state in case of a system crash.
- The database system maintains a log of all changes made to the database. This log is called a transaction log or redo log.
- The log contains a sequence of log records, each describing a change made to the database. The log records are arranged in chronological order.
- In case of a system crash, the database can be recovered by scanning the log records in the transaction log starting from the last checkpoint, and applying modifications described in the log records to the database. This process of applying log records to reconstruct the state of the database is called rollback.
- The key advantage of log based recovery is that it is simple and efficient. The main disadvantage is that the log may grow very long and hence managing the log becomes an important issue.
- The following ascii diagram shows the basic steps involved in log based recovery -

[A diagram showing the steps -
1. Normal execution - Transactions modify database and log records are added to log
2. System crash
3. Rollback - Log records from last checkpoint are processed to recover database]

- Some key points to note -
-- Only changes are logged, not the actual data. This keeps the log size manageable.
-- The log must be on stable storage as it is critical for recovery.
-- Checkpoints are added to the log periodically to limit the number of log records that need to be processed during recovery. The checkpoint marks a consistent state of the database.
-- After recovering, the database is stable but may be slightly out of date. Subsequent transactions can bring the database completely up to date.