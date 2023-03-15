# Locking Techniques for Concurrency Control

Concurrency control is the process of managing simultaneous access to shared data in a database system. Concurrency control ensures that transactions are executed in a consistent and correct manner, and that the integrity of the database is maintained.

One of the most common concurrency control techniques is locking. Locking is the mechanism of granting or denying access to a data item based on the type of lock applied by a transaction. Locking can prevent conflicts such as lost updates, dirty reads, unrepeatable reads, and phantom reads.

There are different types of locks and locking protocols that can be used for concurrency control. Some of the main ones are:

- **Binary locks**: These are the simplest locks that have only two states: locked or unlocked. A transaction can either lock a data item for exclusive access, or leave it unlocked for shared access. Binary locks can prevent lost updates, but not dirty reads, unrepeatable reads, or phantom reads.

- **Shared and exclusive locks**: These are more sophisticated locks that have three states: unlocked, shared, or exclusive. A transaction can lock a data item in shared mode, which allows other transactions to read the same data item, but not to write it. Alternatively, a transaction can lock a data item in exclusive mode, which prevents other transactions from reading or writing the same data item. Shared and exclusive locks can prevent lost updates and dirty reads, but not unrepeatable reads or phantom reads.

- **Intention locks**: These are locks that indicate the intention of a transaction to lock a data item or a group of data items in a certain mode. For example, a transaction can lock a table in intention-shared mode, which means that it intends to lock some of the rows in the table in shared mode. Intention locks are used to implement hierarchical locking, which allows transactions to lock data items at different levels of granularity, such as tables, pages, or rows. Intention locks can prevent deadlocks and improve concurrency.

- **Certify locks**: These are locks that are used in multi-version concurrency control techniques, which maintain multiple versions of a data item to allow concurrent reads and writes. A transaction can read a committed version of a data item without locking it, but it has to lock a data item in certify mode before committing its write. A certify lock checks if the write is valid and does not conflict with other transactions. Certify locks can improve concurrency and performance, but they require more storage space and overhead.

## Two-Phase Locking Protocol

The two-phase locking protocol is a locking protocol that ensures serializability of transactions, which means that the concurrent execution of transactions is equivalent to some serial execution. The two-phase locking protocol divides the execution of a transaction into two phases:

- **Locking (Growing) phase**: In this phase, a transaction can acquire locks on data items, but cannot release any lock. The transaction can lock data items in any order and mode, as long as it does not violate the compatibility rules of the locks. The locking phase ends when the transaction acquires its last lock.

- **Unlocking (Shrinking) phase**: In this phase, a transaction can release locks on data items, but cannot acquire any new lock. The transaction can unlock data items in any order and mode, as long as it does not violate the consistency rules of the locks. The unlocking phase ends when the transaction releases its last lock.

The two-phase locking protocol guarantees serializability, but it does not prevent deadlocks, which occur when two or more transactions are waiting for each other to release locks. To avoid or resolve deadlocks, the protocol can use techniques such as timeouts, deadlock detection, or deadlock prevention.

## Time Stamp Ordering Protocol

The time stamp ordering protocol is a concurrency control technique that does not use locking, but instead assigns a unique time stamp to each transaction and each data item. The time stamp of a transaction represents its logical start time, and the time stamp of a data item represents the last time it was read or written by a transaction. The time stamp ordering protocol uses the time stamps to order the transactions and the data items, and to determine if a transaction can read or write a data item.

The time stamp ordering protocol has two main rules:

- **Read rule**: A transaction T can read a data item X only if the time stamp of T is greater than or equal to the write time stamp of X, which means that T started after the last transaction that wrote X. Otherwise, T is aborted and restarted with a new time stamp.

- **Write rule**: A transaction T can write a data item X only if the time stamp of T is greater than both the