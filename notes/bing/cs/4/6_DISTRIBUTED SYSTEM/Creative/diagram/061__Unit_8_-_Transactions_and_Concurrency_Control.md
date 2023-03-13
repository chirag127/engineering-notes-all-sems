## Unit 8 - Transactions and Concurrency Control

A transaction is a logical unit of work that consists of a sequence of operations on a database. A transaction must satisfy the ACID properties: atomicity, consistency, isolation, and durability. Atomicity means that either all the operations of a transaction are executed or none of them are. Consistency means that a transaction preserves the integrity constraints of the database. Isolation means that a transaction does not interfere with other concurrent transactions. Durability means that the effects of a committed transaction are permanent and survive any system failures.

Concurrency control is the process of managing the simultaneous execution of transactions in a shared database. Concurrency control ensures that correct results for concurrent operations are generated while getting those results as quickly as possible. Concurrency control is needed to prevent problems such as lost updates, uncommitted data, inconsistent reads, and phantom reads.

There are different techniques for implementing concurrency control, such as locking, timestamping, validation, and multiversioning. Locking is a mechanism where a transaction acquires a lock on a data item before accessing it. A lock can be either shared or exclusive, depending on whether the transaction intends to read or write the data item. A transaction must release the lock after completing its operation on the data item. Locking ensures serializability, which means that the concurrent execution of transactions is equivalent to some serial execution of the same transactions.

Timestamping is a mechanism where a transaction is assigned a unique timestamp that represents its start time. A timestamp can be used to order the transactions and determine their precedence. A transaction can access a data item only if its timestamp is compatible with the read and write timestamps of the data item. Timestamping ensures conflict serializability, which means that the concurrent execution of transactions is equivalent to some serial execution of the same transactions that preserves the order of conflicting operations.

Validation is a mechanism where a transaction is executed in three phases: read, validate, and write. In the read phase, the transaction reads the data items from the database but does not make any changes. In the validate phase, the transaction checks whether it can commit without violating serializability. In the write phase, the transaction writes the updated data items to the database. Validation ensures view serializability, which means that the concurrent execution of transactions is equivalent to some serial execution of the same transactions that produces the same final state of the database.

Multiversioning is a mechanism where a transaction can access multiple versions of a data item that are created by other transactions. A transaction can read the most recent committed version of a data item that is compatible with its timestamp. A transaction can write a new version of a data item without overwriting the existing versions. Multiversioning ensures snapshot isolation, which means that a transaction sees a consistent snapshot of the database at the time of its start and does not experience any phantom reads.

The following diagram illustrates the basic architecture of a concurrency control system:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Transaction    |     |  Concurrency    |     |  Data           |
|  Manager        |     |  Control        |     |  Manager        |
|                 |     |  Manager        |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Begin          |     |  Lock           |     |  Read           |
|  Commit         |     |  Unlock         |     |  Write          |
|  Abort          |     |  Timestamp      |     |                 |
|                 |     |  Validate       |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|