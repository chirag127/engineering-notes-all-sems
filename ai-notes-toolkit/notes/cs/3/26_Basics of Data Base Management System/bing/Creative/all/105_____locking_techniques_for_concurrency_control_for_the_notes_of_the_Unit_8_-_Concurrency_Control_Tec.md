# Locking Techniques for Concurrency Control

Concurrency control is the process of managing simultaneous access to shared data in a database system. Concurrency control ensures that transactions are executed in a consistent and correct manner, and that the integrity of the database is maintained. Concurrency control also prevents conflicts and anomalies that may arise due to concurrent access, such as lost updates, dirty reads, unrepeatable reads, and phantom reads.

One of the most common concurrency control techniques is locking. Locking is a mechanism that grants or denies permission to access a data item based on the type and mode of the lock. Locking can be implemented at different levels of granularity, such as database, table, page, or record. Locking can also be classified into different types, such as binary, shared, exclusive, or intention locks.

The main idea behind locking is to enforce serializability, which is the property that the concurrent execution of transactions is equivalent to some serial execution of the same transactions. Serializability ensures that the outcome of concurrent transactions is the same as if they were executed one after the other, without any interference.

To achieve serializability, a locking protocol must follow some rules or principles. One of the most widely used locking protocols is the two-phase locking (2PL) protocol, which divides the execution of a transaction into two phases: the growing phase and the shrinking phase. In the growing phase, a transaction can acquire locks on data items, but cannot release any lock. In the shrinking phase, a transaction can release locks on data items, but cannot acquire any new lock. The point where the transaction switches from the growing phase to the shrinking phase is called the lock point.

The 2PL protocol ensures serializability, but it may cause some problems, such as deadlocks, starvation, or cascading aborts. Deadlocks occur when two or more transactions are waiting for each other to release locks on data items that they need. Starvation occurs when a transaction is repeatedly denied access to a data item due to the presence of other conflicting locks. Cascading aborts occur when a transaction aborts and causes other transactions that have read its uncommitted data to abort as well.

To overcome these problems, some variations or extensions of the 2PL protocol have been proposed, such as:

- Strict 2PL: A transaction must hold all its locks until it commits or aborts. This prevents cascading aborts, but may increase the lock holding time and reduce concurrency.
- Rigorous 2PL: A transaction must hold all its exclusive locks until it commits or aborts, and all its shared locks until it reads the corresponding data items. This is a stronger version of strict 2PL that also prevents dirty reads, but may further reduce concurrency.
- Conservative 2PL: A transaction must request all its locks before it starts its execution. This prevents deadlocks, but may cause unnecessary blocking and waste of resources.
- Timestamp-based 2PL: A transaction is assigned a unique timestamp when it starts, and uses this timestamp to order its lock requests. This avoids deadlocks and starvation, but may cause more aborts due to conflicts.
- Multi-version 2PL: A transaction can access multiple versions of a data item, each with a different timestamp. This increases concurrency and reduces conflicts, but requires more storage space and complexity.

These are some of the main locking techniques for concurrency control. There are other techniques as well, such as validation, optimistic, or snapshot isolation, that do not rely on locking, but use other methods to ensure serializability and consistency. Each technique has its own advantages and disadvantages, and the choice of the best technique depends on the characteristics and requirements of the database system and the application.