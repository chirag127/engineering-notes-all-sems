The following diagram illustrates the basic architecture of a optimistic concurrency control system for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM.

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Transaction 1  |    |  Transaction 2  |    |  Transaction 3  |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       v                      v                      v
+---------------------------------------------------------+
|                                                         |
|                    Validation Module                    |
|                                                         |
+---------------------------------------------------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       v                      v                      v
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Database 1     |    |  Database 2     |    |  Database 3     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

The optimistic concurrency control method assumes that multiple transactions can frequently complete without interfering with each other. Therefore, it does not lock the records when they are fetched from the database for an update, but only when the actual update is performed. This helps increase the database performance and reduce the locking overhead.

The optimistic concurrency control system works by ensuring that the record being updated or deleted has the same values as it did when the updating or deleting process started. For example, when a transaction reads a record from the database, it also reads a version number or a timestamp associated with that record. When the transaction tries to update or delete the record, it compares the current version number or timestamp with the one it read earlier. If they match, it means that no other transaction has modified the record in the meantime, and the update or delete can proceed. If they do not match, it means that another transaction has updated or deleted the record concurrently, and the current transaction has to abort and restart.

The validation module is responsible for checking the version numbers or timestamps of the records before updating or deleting them. It can also resolve any conflicts that may arise due to concurrent operations on the same record. The validation module can be centralized or distributed, depending on the architecture of the distributed system. In a centralized system, there is one validation module that communicates with all the transactions and databases. In a distributed system, there are multiple validation modules that coordinate with each other and with the transactions and databases.