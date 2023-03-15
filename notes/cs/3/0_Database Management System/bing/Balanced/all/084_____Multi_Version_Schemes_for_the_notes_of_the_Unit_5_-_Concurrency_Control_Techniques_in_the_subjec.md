# Multi Version Schemes for Concurrency Control

- Multi version schemes are a type of concurrency control method that allow multiple versions of data objects to coexist in the database.
- The main idea is to grant an appropriate version of a data object to each read request, while write requests operate on a copy of the data object, not the original one.
- This way, read operations do not block write operations, and vice versa, and the database can support a high level of concurrency.
- The advantages of multi version schemes are:
  - They reduce the number of conflicts and aborts among transactions.
  - They improve the performance and throughput of the database system.
  - They preserve the consistency and integrity of the database.
- The disadvantages of multi version schemes are:
  - They require more storage space and overhead to maintain multiple versions of data objects.
  - They may introduce complexity and overhead in the version management and garbage collection.
  - They may cause anomalies such as phantom reads and non-repeatable reads if the isolation level is not high enough.

- There are different ways to implement multi version schemes, such as:
  - Timestamp ordering: Each version of a data object is assigned a timestamp based on the transaction that created or modified it. Read requests are granted the latest version of the data object that is older than or equal to their timestamp. Write requests are allowed only if their timestamp is greater than the timestamp of the latest version of the data object.
  - Validation: Each transaction is divided into three phases: read, validation, and write. In the read phase, the transaction reads the versions of the data objects that are consistent with its start time. In the validation phase, the transaction checks if its read set is still valid, i.e., no other transaction has modified the data objects that it read. If the validation succeeds, the transaction proceeds to the write phase, where it writes new versions of the data objects that it modified. Otherwise, the transaction is aborted and restarted.
  - Snapshot isolation: Each transaction sees a snapshot of the database as of its start time, i.e., the versions of the data objects that were committed before the transaction began. Read requests are granted the versions of the data objects from the snapshot. Write requests are allowed only if the data objects that they modify have not been modified by any other concurrent transaction. Otherwise, the transaction is aborted and restarted.