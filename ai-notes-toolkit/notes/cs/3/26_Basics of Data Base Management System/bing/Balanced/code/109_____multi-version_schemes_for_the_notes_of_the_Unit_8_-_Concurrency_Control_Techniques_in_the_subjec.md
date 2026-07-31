# Multi-version Schemes for Concurrency Control

- Multi-version schemes are a type of concurrency control method that allow concurrent access to the database without locking the data.
- Multi-version schemes create and maintain different versions of data items for each write operation performed by a transaction.
- Multi-version schemes allow read operations to access the most recent committed version of a data item, without waiting for the write operations to finish.
- Multi-version schemes improve the performance and concurrency of database applications in a multiuser environment, by reducing the conflicts and delays between read and write operations.
- Multi-version schemes can be implemented in different ways, such as timestamp ordering, multiversion two-phase locking, or snapshot isolation.

## Timestamp Ordering

- Timestamp ordering is a multi-version scheme that assigns a unique timestamp to each transaction and each version of a data item.
- Timestamp ordering ensures that the transactions and the versions of data items are executed in a serializable order, based on their timestamps.
- Timestamp ordering uses two rules to enforce serializability:
  - Write Rule: A transaction T can write a new version of a data item X only if the timestamp of T is greater than the timestamp of the latest committed version of X.
  - Read Rule: A transaction T can read a version of a data item X only if the timestamp of T is greater than or equal to the timestamp of that version of X, and less than the timestamp of any uncommitted version of X.
- Timestamp ordering prevents write-write conflicts and write-read conflicts, but allows read-write conflicts.

## Multiversion Two-Phase Locking

- Multiversion two-phase locking is a multi-version scheme that combines the two-phase locking protocol with the creation of multiple versions of data items.
- Multiversion two-phase locking allows read operations to access the latest committed version of a data item, without acquiring any lock on it.
- Multiversion two-phase locking requires write operations to acquire exclusive locks on the data items they want to update, and to create new versions of them.
- Multiversion two-phase locking ensures that the transactions and the versions of data items are executed in a serializable order, based on the lock points of the transactions.
- Multiversion two-phase locking prevents write-write conflicts and read-write conflicts, but allows write-read conflicts.

## Snapshot Isolation

- Snapshot isolation is a multi-version scheme that provides each transaction with a consistent snapshot of the database at the start of the transaction.
- Snapshot isolation allows read operations to access the data items as they were in the snapshot, without acquiring any lock on them.
- Snapshot isolation requires write operations to check for conflicts with other concurrent transactions before committing, and to abort if any conflict is detected.
- Snapshot isolation ensures that the transactions and the versions of data items are executed in a serializable order, based on the commit order of the transactions.
- Snapshot isolation prevents write-write conflicts and write-read conflicts, but allows read-write conflicts.