### Multi Version Schemes for Concurrency Control

- Multi version schemes are a type of concurrency control method that allow multiple versions of the same data object to exist in the database at the same time.
- The main idea of multi version schemes is to grant an appropriate version of the data object to each read request, while write requests operate on a copy of the data object, not the original one.
- This way, read requests do not have to wait for write requests to finish, and write requests do not have to lock the data object, thus increasing the concurrency and performance of the database system.
- There are different ways to implement multi version schemes, such as timestamp ordering, validation, and snapshot isolation.
- Some advantages of multi version schemes are:
  - They reduce the number of conflicts and aborts among transactions.
  - They allow long-running read-only transactions to access consistent snapshots of the database without blocking or being blocked by other transactions.
  - They support high availability and fault tolerance by allowing transactions to access backup versions of the data objects in case of failures.
- Some disadvantages of multi version schemes are:
  - They increase the storage and maintenance overhead of the database system, as multiple versions of the data objects have to be stored and managed.
  - They may introduce anomalies and inconsistencies among transactions, such as write skew and phantom reads, if the isolation level is not set properly.
  - They may not preserve the serializability and recoverability properties of transactions, depending on the implementation and the conflict resolution policy.