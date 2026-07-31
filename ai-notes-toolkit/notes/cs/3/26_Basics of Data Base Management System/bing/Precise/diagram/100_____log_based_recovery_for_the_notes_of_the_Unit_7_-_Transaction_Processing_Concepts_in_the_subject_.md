### Log Based Recovery in DBMS

Log-based recovery in DBMS provides the ability to maintain or recover data in case of system failure. DBMS keeps a record of every transaction on some stable storage device to provide easy access to data when the system fails. A log file will be created for every operation performed on the database at that point .

- **Introduction to Log-Based Recovery in DBMS**: A start log is produced when the transaction begins. For example, `<Tn, Start>`. A new log is written to the file when the City is changed from Chennai to NCR `<Tn, City, 'Chennai', 'NCR' >`. Once the transaction has been completed, another log will be written to indicate the completion .

- **Definition of DBMS Log-Based Recovery**: Log-based recovery provides the facility to maintain or recover data if any failure may occur in the system. Log means sequence of records or data, each transaction DBMS creates a log in some stable storage device so that we easily recover data if any failure may occur .

- **What is log-based recovery in DBMS?**: As the name suggests, log is a sequence of records that is maintained in a stable storage devices to note down all the changes made by transactions in a sequential manner. This log is used to recover the transaction in case of failure .

- **Log-based recovery technique**: Log-based recovery is a technique used in database management systems (DBMS) to recover a database to a consistent state in the event of a failure or crash. It involves the use of transaction logs, which are records of all the transactions performed on the database .

- **Log-Based Recovery**: The log is a sequence of records. Log of each transaction is maintained in some stable storage so that if any failure occurs, the data can be recovered. If any operation is performed on the database, then it will be recorded in the log. But the process of storing the logs should be done before the actual operation is performed on the database .
