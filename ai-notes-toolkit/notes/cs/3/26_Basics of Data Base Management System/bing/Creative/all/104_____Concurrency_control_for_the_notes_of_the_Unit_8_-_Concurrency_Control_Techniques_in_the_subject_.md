# Concurrency Control

Concurrency control is a database management systems (DBMS) concept that is used to address the problems that occur with a multi-user system. Concurrency control, when applied to a DBMS, is meant to coordinate simultaneous transactions while preserving data integrity of the respective databases.

Some of the objectives of concurrency control are:

- To ensure the consistency and correctness of the database state after the execution of concurrent transactions.
- To prevent data loss or corruption due to concurrent access or modification of the same data item by different transactions.
- To improve the performance and throughput of the DBMS by allowing a high degree of concurrency among transactions.
- To avoid deadlock or starvation situations where transactions are waiting indefinitely for resources held by other transactions.

Some of the techniques of concurrency control are:

- Locking: This technique involves granting exclusive or shared access to a data item or a set of data items to a transaction based on the type of operation (read or write) it performs. A transaction must acquire a lock before accessing a data item and release it after completing the operation. Locking can ensure serializability, which is a correctness criterion for concurrent transactions, but it can also cause deadlock or blocking problems .
- Timestamping: This technique involves assigning a unique timestamp to each transaction based on its start time or priority. A transaction can access a data item only if its timestamp is compatible with the read and write timestamps of the data item, which are updated after each operation. Timestamping can ensure serializability without causing deadlock, but it can cause aborts or restarts of transactions due to timestamp conflicts .
- Optimistic: This technique involves allowing transactions to execute without any concurrency control until they are ready to commit. Then, a validation phase checks if the transactions have violated any serializability constraints based on their read and write sets. If no violation is detected, the transactions are committed; otherwise, they are aborted and restarted. Optimistic concurrency control can improve performance and avoid deadlock in low-conflict scenarios, but it can cause high overhead and aborts in high-conflict scenarios .