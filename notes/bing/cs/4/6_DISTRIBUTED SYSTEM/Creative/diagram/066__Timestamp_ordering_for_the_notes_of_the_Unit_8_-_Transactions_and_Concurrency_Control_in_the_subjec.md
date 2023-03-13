Timestamp ordering is a method of concurrency control in distributed systems that assigns a unique timestamp to each transaction and ensures that conflicting operations are executed in the order of their timestamps. A transaction is allowed to read or write an object only if its timestamp is greater than or equal to the timestamp of the last operation on that object. Otherwise, the transaction is aborted and restarted with a new timestamp.

The following diagram illustrates the basic architecture of a timestamp ordering system:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Transaction    |     |  Transaction    |     |  Transaction    |
|  Manager 1      |     |  Manager 2      |     |  Manager 3      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Timestamp      |     |  Timestamp      |     |  Timestamp      |
|  Ordering       |     |  Ordering       |     |  Ordering       |
|  Module 1       |     |  Module 2       |     |  Module 3       |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       +---------------------+---------------------+
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Data           |     |  Data           |     |  Data           |
|  Object 1       |     |  Object 2       |     |  Object 3       |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

Each transaction manager is responsible for generating timestamps for the transactions it initiates, using a logical clock or a physical clock. Each timestamp ordering module is responsible for enforcing the timestamp ordering protocol for the transactions it receives, using a read timestamp (RTS) and a write timestamp (WTS) for each data object. Each data object is stored in a shared database and has a value and a version number. The version number is incremented whenever the object is updated by a transaction.