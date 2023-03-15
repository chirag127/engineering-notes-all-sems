# Log Based Recovery

Log based recovery is a technique used in database management systems (DBMS) to recover a database to a consistent state in the event of a failure or crash. It involves the use of transaction logs, which are records of all the transactions performed on the database.

## Advantages of Log Based Recovery

- It provides the ability to maintain or recover data in case of system failure.
- It ensures the atomicity and durability properties of transactions.
- It allows the database to be restored to a consistent state without losing any committed changes.

## Types of Log Based Recovery

There are two main types of log based recovery: undo logging and redo logging.

### Undo Logging

Undo logging is a type of log based recovery that uses the log records to undo the changes made by transactions that did not commit before the failure. It is also known as backward recovery or rollback.

The steps involved in undo logging are:

- Scan the log file backwards from the end to the most recent checkpoint.
- For each log record <Tn, X, V1, V2>, where Tn is the transaction id, X is the data item, V1 is the old value and V2 is the new value, do the following:
  - If the log record is <Tn, commit>, then mark Tn as committed.
  - If the log record is <Tn, start>, then check if Tn is marked as committed. If not, then add Tn to the undo list.
  - If the log record is <Tn, X, V1, V2>, then check if Tn is in the undo list. If yes, then restore the old value of X by writing V1 to the database.
- Write an end record to the log file and flush it to the stable storage.

### Redo Logging

Redo logging is a type of log based recovery that uses the log records to redo the changes made by transactions that committed before the failure. It is also known as forward recovery or rollforward.

The steps involved in redo logging are:

- Scan the log file forward from the most recent checkpoint to the end.
- For each log record <Tn, X, V1, V2>, where Tn is the transaction id, X is the data item, V1 is the old value and V2 is the new value, do the following:
  - If the log record is <Tn, start>, then mark Tn as active.
  - If the log record is <Tn, commit>, then mark Tn as committed and add Tn to the redo list.
  - If the log record is <Tn, X, V1, V2>, then check if Tn is in the redo list. If yes, then restore the new value of X by writing V2 to the database.
- Write an end record to the log file and flush it to the stable storage.

## Example of Log Based Recovery

Consider the following transactions and log records:

| Transaction | Operation |
| ----------- | --------- |
| T1          | Read(A)   |
| T1          | A = A + 100 |
| T1          | Write(A)  |
| T2          | Read(B)   |
| T2          | B = B - 50 |
| T2          | Write(B)  |
| T1          | Commit    |
| T2          | Read(C)   |
| T2          | C = C + 50 |
| T2          | Write(C)  |

| Log Record | Meaning |
| ---------- | ------- |
| <T1, start> | Transaction T1 starts |
| <T1, A, 500, 600> | Transaction T1 updates A from 500 to 600 |
| <T2, start> | Transaction T2 starts |
| <T2, B, 400, 350> | Transaction T2 updates B from 400 to 350 |
| <T1, commit> | Transaction T1 commits |
| <T2, C, 300, 350> | Transaction T2 updates C from 300 to 350 |

Assume that the system crashes after writing the last log record and before writing the commit record for T2. The database state before the crash is:

| Data Item | Value |
| ---------