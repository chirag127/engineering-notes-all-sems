## Unit 9 - Distributed Transactions

A distributed transaction is a database transaction that involves two or more network hosts. A transaction manager is responsible for creating and managing a global transaction that encompasses all operations against the transactional resources on different hosts.

The following diagram illustrates the basic architecture of a distributed transaction using the two-phase commit protocol:

```
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|   Application   |        | Transaction     |        | Transactional   |
|                 |        | Manager         |        | Resource        |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Begin          |        |                 |        |                 |
|  Transaction    |        |                 |        |                 |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Execute        |        |                 |        |                 |
|  SQL            |        |                 |        |                 |
|  Statements     |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Commit         |        |                 |        |                 |
|  Transaction    |        |                 |        |                 |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|                 |------->|  Begin          |------->|  Begin          |
|                 |        |  Distributed    |        |  Local          |
|                 |        |  Transaction    |        |  Transaction    |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|                 |        |  Prepare        |------->|  Prepare        |
|                 |        |  Resource       |        |  Resource       |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|                 |        |                 |<-------|  Vote           |
|                 |        |                 |        |  (Yes/No)       |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|                 |        |  Commit/Rollback|------->|  Commit/Rollback|
|                 |        |  Resource       |        |  Resource       |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|                 |        |                 |<-------|  Acknowledge    |
|                 |        |                 |        |                 |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|                 |<-------|  End            |<-------|  End            |
|                 |        |  Distributed    |        |  Local          |
|                 |        |  Transaction    |        |  Transaction    |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
```