### Comparison of methods for concurrency control

Concurrency control is the process of managing the concurrent access and modification of shared data in a distributed system, such that the consistency and correctness of the data and the system are preserved. Concurrency control methods can be classified into two main categories: pessimistic and optimistic.

- Pessimistic methods prevent conflicts from occurring by using locks, timestamps, or other mechanisms to coordinate the access and modification of data by concurrent transactions. Pessimistic methods ensure serializability, which means that the outcome of concurrent transactions is equivalent to some serial execution of them. However, pessimistic methods may incur high overhead, blocking, deadlock, and reduced concurrency.

- Optimistic methods allow conflicts to occur and then detect and resolve them by using validation, versioning, or other mechanisms to verify the correctness of concurrent transactions. Optimistic methods do not ensure serializability, but rather weaker consistency criteria, such as snapshot isolation or causal consistency. However, optimistic methods may reduce overhead, blocking, deadlock, and increase concurrency.

Some examples of concurrency control methods are:

- Two-phase locking (2PL): A pessimistic method that uses locks to grant exclusive or shared access to data items by transactions. A transaction must acquire all the locks it needs before releasing any lock, and it must release all the locks after committing or aborting. 2PL ensures serializability and strictness, but it may cause blocking and deadlock.

- Timestamp ordering (TO): A pessimistic method that uses timestamps to order the execution of transactions. A transaction is assigned a unique timestamp when it starts, and it must access and modify data items in timestamp order. TO ensures serializability and strictness, but it may cause aborts and restarts.

- Multi-version concurrency control (MVCC): An optimistic method that uses versions to maintain multiple copies of data items, each with a timestamp. A transaction reads the latest committed version of a data item that is older than its timestamp, and it writes a new version of a data item with its timestamp. MVCC ensures snapshot isolation, which means that a transaction sees a consistent snapshot of the database at its start time, and it does not overwrite the changes of other concurrent transactions. However, MVCC may cause write skew, which is a form of inconsistency that occurs when two transactions update different data items based on a common predicate.

- Validation concurrency control (VCC): An optimistic method that uses validation to check the correctness of transactions before committing them. A transaction executes without any coordination with other transactions, and then it validates its read and write sets against the database state. VCC ensures serializability, but it may cause aborts and restarts.