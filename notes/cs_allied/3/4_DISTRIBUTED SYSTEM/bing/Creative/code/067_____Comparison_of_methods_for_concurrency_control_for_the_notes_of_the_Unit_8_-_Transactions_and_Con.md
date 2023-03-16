### Comparison of methods for concurrency control

Concurrency control is the process of managing the simultaneous execution of transactions in a distributed system, such that the consistency and correctness of the data are preserved. Concurrency control methods can be classified into two main categories: pessimistic and optimistic.

- Pessimistic methods assume that conflicts are likely to occur and prevent them by using locking or timestamping mechanisms. Pessimistic methods guarantee serializability, which means that the outcome of concurrent transactions is equivalent to some serial execution of them. However, pessimistic methods may incur high overhead, blocking, and deadlock problems.

- Optimistic methods assume that conflicts are rare and allow transactions to execute without any coordination until the commit time. Then, they check for conflicts and abort or restart transactions if necessary. Optimistic methods avoid blocking and deadlock, but may incur high abort and restart costs.

Some of the common concurrency control methods are:

- Two-phase locking (2PL): A pessimistic method that requires transactions to acquire locks on data items before reading or writing them, and release them after they are done. 2PL ensures serializability, but may cause blocking and deadlock. There are different variants of 2PL, such as strict 2PL, rigorous 2PL, and conservative 2PL, that differ in the timing and order of lock acquisition and release.

- Timestamp ordering (TO): A pessimistic method that assigns a unique timestamp to each transaction and orders them according to their timestamps. Transactions are allowed to read or write data items only if their timestamps are compatible with the timestamps of previous transactions that accessed the same data items. TO ensures serializability, but may cause aborts and restarts.

- Multi-version concurrency control (MVCC): A method that maintains multiple versions of each data item, each with a timestamp indicating when it was created or modified. Transactions can read the latest committed version of a data item that is compatible with their timestamp, and write a new version with their own timestamp. MVCC avoids blocking and ensures serializability, but may incur high storage and garbage collection costs.

- Validation concurrency control (VCC): An optimistic method that divides the execution of a transaction into three phases: read, validation, and write. In the read phase, transactions read data items without any locking or timestamping. In the validation phase, transactions check for conflicts with other concurrent transactions using a validation test. In the write phase, transactions write their updates to the database if they pass the validation test. VCC avoids blocking and ensures serializability, but may cause aborts and restarts.