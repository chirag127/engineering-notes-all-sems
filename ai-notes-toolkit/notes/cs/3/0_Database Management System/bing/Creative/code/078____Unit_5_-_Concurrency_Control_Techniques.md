## Unit 5 - Concurrency Control Techniques

Concurrency control techniques are methods of managing the simultaneous execution of transactions in a shared database. They aim to preserve the database consistency, enforce the isolation of different transactions, and resolve the conflicts that occur due to the read-write operations of transactions .

The need for concurrency control arises because multiple transactions may access and modify the same data items concurrently, which may lead to inconsistency, incorrectness, or loss of data integrity. Therefore, concurrency control techniques ensure that the transactions are concurrent, accurate, and give correct results without violating data integrity. They also ensure serializability, which means that the concurrent execution of transactions produces the same result as some serial execution of the same transactions.

Some of the common concurrency control techniques are :

- **Two-phase locking protocol**: This technique uses locks to secure the permission to read or write a data item. A transaction has two phases: a locking (growing) phase, where it acquires locks on desired data items one at a time, and an unlocking (shrinking) phase, where it releases locks on its locked data items one at a time. A transaction cannot acquire any new locks after it releases any lock. This protocol ensures serializability, but may cause deadlock, starvation, or cascading rollback .
- **Timestamp ordering protocol**: This technique assigns a unique timestamp to each transaction, which reflects its start time. A transaction can read or write a data item only if its timestamp is compatible with the read and write timestamps of the data item, which record the latest transactions that have read or written the data item. This protocol ensures serializability and avoids deadlock, but may cause abortion, starvation, or cascading rollback.
- **Multi-version concurrency control**: This technique maintains multiple versions of each data item, each with a different timestamp. A transaction can read the latest version of a data item that is older than its timestamp, and can write a new version of a data item with its timestamp. This protocol ensures serializability and avoids abortion, deadlock, and cascading rollback, but may cause storage overhead and complexity.
- **Validation concurrency control**: This technique divides a transaction into three phases: a read phase, where it reads data items but does not write any, a validation phase, where it checks for conflicts with other transactions, and a write phase, where it writes the data items if the validation is successful. This protocol ensures serializability and avoids deadlock and cascading rollback, but may cause abortion, starvation, or delay.

: https://quescol.com/dbms/concurrency-control-techniques
: https://www.geeksforgeeks.org/concurrency-control-techniques/
: https://quescol.com/dbms/need-for-concurrency-control
: https://en.wikipedia.org/wiki/Concurrency_control
: https://www.cs.purdue.edu/homes/bb/cs448_Spring2014/lecture-files/pdf/ch18-Concurrency%20Control%20Techniques.pdf