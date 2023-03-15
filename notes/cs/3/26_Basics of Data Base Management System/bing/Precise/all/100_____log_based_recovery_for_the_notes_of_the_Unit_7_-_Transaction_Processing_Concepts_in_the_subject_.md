### Log-Based Recovery

Log-based recovery is a technique used in database management systems (DBMS) to recover a database to a consistent state in the event of a failure or crash. It involves the use of transaction logs, which are records of all the transactions performed on the database.

- Log-based recovery provides the facility to maintain or recover data if any failure may occur in the system.
- Log means sequence of records or data, each transaction DBMS creates a log in some stable storage device so that we can easily recover data if any failure may occur.
- In immediate Mode of log-based recovery, database modification is performed while Transaction is in Active State. It means as soon as Transaction is performed or executes its WRITE Operation, then immediately these changes are saved in Database also.
- The log is a sequence of records. Log of each transaction is maintained in some stable storage so that if any failure occurs, then it can be recovered from there.
