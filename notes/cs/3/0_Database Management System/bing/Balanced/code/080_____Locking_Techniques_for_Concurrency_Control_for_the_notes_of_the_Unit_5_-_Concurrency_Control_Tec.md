### Locking Techniques for Concurrency Control

Locking techniques are methods of ensuring serializability and consistency of transactions in a database system. Locking techniques prevent multiple transactions from accessing or modifying the same data item simultaneously, which may cause concurrency problems such as lost update, dirty read, unrepeatable read, or phantom read.

A lock is a variable associated with a data item that describes the status of the item with respect to possible operations that can be applied to it. Generally, there are two types of locks:

- Shared lock (S-lock): allows a transaction to read a data item, but not to write or modify it. Multiple transactions can hold shared locks on the same data item concurrently, as long as no other transaction holds an exclusive lock on it.
- Exclusive lock (X-lock): allows a transaction to read, write, or modify a data item. Only one transaction can hold an exclusive lock on a data item at a time, and no other transaction can hold any lock on it.

A transaction can acquire or release locks on data items according to some locking protocol, which defines the rules and constraints for locking and unlocking. A locking protocol should ensure the following properties:

- Serializability: the execution of concurrent transactions should be equivalent to some serial execution of the same transactions.
- Deadlock-freedom: the locking protocol should prevent or avoid deadlock, which is a situation where two or more transactions are waiting for each other to release locks on data items they need.
- Liveliness: the locking protocol should ensure that every transaction can eventually proceed and complete its execution.

Some common locking protocols are:

- Two-phase locking (2PL): a transaction must acquire all the locks it needs before it releases any lock. The transaction's execution is divided into two phases: a growing phase, where it can only acquire locks, and a shrinking phase, where it can only release locks. 2PL ensures serializability, but may cause deadlock or starvation.
- Strict two-phase locking (Strict 2PL): a transaction must hold all its exclusive locks until it commits or aborts. This ensures that no other transaction can read or write the data items updated by an uncommitted transaction, which avoids the problems of dirty read and cascading rollback. Strict 2PL is a special case of 2PL.
- Rigorous two-phase locking (Rigorous 2PL): a transaction must hold all its locks, both shared and exclusive, until it commits or aborts. This ensures that no other transaction can read the data items accessed by an uncommitted transaction, which avoids the problems of unrepeatable read and phantom read. Rigorous 2PL is a special case of Strict 2PL.
- Timestamp ordering: a transaction is assigned a unique timestamp when it starts, and the timestamp determines the order of conflicting operations. A transaction can read or write a data item only if its timestamp is greater than the timestamp of the last transaction that wrote the data item, and less than the timestamp of the last transaction that read the data item. Otherwise, the transaction is aborted and restarted with a new timestamp. Timestamp ordering ensures serializability and deadlock-freedom, but may cause high abort rate or starvation.