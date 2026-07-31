### Multi Version Schemes for the notes of the Unit 5 - Concurrency Control Techniques in the subject of Database Management System

Multi Version Schemes (MVS) are used in Database Management Systems (DBMS) to provide concurrency control techniques that allow multiple users to access the same data simultaneously. Below are some key points to understand about Multi Version Schemes:

- MVS uses multiple versions of the same data item to allow concurrent access to the data. Each version is time-stamped with the transaction ID that created it.
- MVS allows read-only transactions to access the most recent version of the data, while read-write transactions can create new versions of the data.
- MVS provides snapshot isolation, which means each transaction sees a consistent view of the database as if it were the only transaction accessing the data.
- MVS uses a garbage collection mechanism to remove old versions of the data that are no longer needed.
- MVS can be implemented using two-phase locking or optimistic concurrency control techniques.
- In two-phase locking, a transaction acquires locks on data items it accesses during its execution. Locks are released only after the transaction has completed.
- In optimistic concurrency control, a transaction assumes that it can complete without conflicts and validates its changes before committing them. If a conflict is detected, the transaction is rolled back and restarted.
- MVS can be used in databases that have high read and low write workloads, and in databases that require high availability and fault tolerance.

Overall, Multi Version Schemes provide an effective way to manage concurrency in databases that have multiple users accessing the same data. By using multiple versions of the data, MVS allows read-only and read-write transactions to access the data concurrently, while ensuring consistency and correctness of the data.