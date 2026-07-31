## Unit 8 - Concurrency Control Techniques

Concurrency control techniques are methods of managing the simultaneous execution of transactions in a shared database. They aim to preserve the database consistency, enforce the isolation of different transactions, and resolve the conflicts that occur due to the read-write operations of transactions .

The need for concurrency control arises because multiple transactions may access and modify the same data items concurrently, which may lead to inconsistency, lost updates, uncommitted dependencies, or incorrect summary.

Some of the common concurrency control techniques are:

- **Two-phase locking protocol**: This technique uses locks to secure the permission to read or write a data item. A transaction goes through two phases: a locking phase, where it acquires locks on the data items it needs, and an unlocking phase, where it releases the locks. The locking phase precedes the unlocking phase, and no new locks can be acquired after releasing any lock. This protocol ensures serializability, which means that the concurrent execution of transactions is equivalent to some serial execution of the same transactions .
- **Timestamp ordering protocol**: This technique assigns a unique timestamp to each transaction, which reflects its start time. The timestamp is used to order the transactions and determine their precedence. A transaction can read or write a data item only if its timestamp is greater than the timestamp of the last transaction that wrote the data item. Otherwise, the transaction is aborted and restarted with a new timestamp. This protocol avoids the deadlock problem, which occurs when two or more transactions are waiting for each other to release locks.
- **Multi-version concurrency control**: This technique maintains multiple versions of each data item, each with a different timestamp. A transaction can read the version of a data item that was the latest before its start time, and can write a new version of a data item with its own timestamp. This protocol allows more concurrency than the timestamp ordering protocol, as transactions can read older versions of data items without conflicting with other transactions that write newer versions.
- **Validation concurrency control**: This technique divides a transaction into three phases: a read phase, where it reads the data items from the database, a validation phase, where it checks for conflicts with other transactions, and a write phase, where it writes the modified data items to the database. A transaction can validate successfully only if it does not overlap with any other transaction that has written any data item that it has read or written. Otherwise, the transaction is aborted and restarted. This protocol avoids locking and timestamping, and reduces the chances of abortion .

: https://quescol.com/dbms/concurrency-control-techniques
: https://www.geeksforgeeks.org/concurrency-control-techniques/
: https://quescol.com/dbms/need-for-concurrency-control
: https://en.wikipedia.org/wiki/Concurrency_control
: https://www.cs.purdue.edu/homes/bb/cs448_Spring2014/lecture-files/pdf/ch18-Concurrency%20Control%20Techniques.pdf