# Multi Version Schemes for Concurrency Control

- Multi version schemes are a type of concurrency control method that allow multiple versions of data objects to exist in the database at the same time.
- The main idea of multi version schemes is to grant an appropriate version of a data object to each read request, while write requests operate on a copy of the data object, not the original one.
- This way, read requests do not have to wait for write requests to finish, and write requests do not have to lock the data object from other transactions.
- The advantages of multi version schemes are that they increase the concurrency and performance of the database system, and reduce the chances of deadlock and starvation.
- The disadvantages of multi version schemes are that they require more storage space and overhead to maintain multiple versions of data objects, and they may cause inconsistency and anomalies if the versions are not managed properly.
- There are different types of multi version schemes, such as timestamp ordering, multiversion two-phase locking, and snapshot isolation.
- Timestamp ordering is a multi version scheme that assigns a unique timestamp to each transaction, and uses the timestamp to determine the order of execution and the version of the data object to be accessed.
- Multiversion two-phase locking is a multi version scheme that combines two-phase locking with versioning, and allows transactions to read the latest committed version of a data object, while locking the data object for writing.
- Snapshot isolation is a multi version scheme that provides each transaction with a snapshot of the database state at the start of the transaction, and allows transactions to read and write without locking, as long as there are no write-write conflicts.