### Comparison of methods for concurrency control

Concurrency control is the process of managing the concurrent access and modification of shared data in a distributed system, such that the ACID properties of transactions are preserved. Concurrency control methods can be classified into two main categories: pessimistic and optimistic.

- Pessimistic methods prevent conflicts from occurring by acquiring locks on data items before accessing them. Transactions that request locks on data items that are already locked by other transactions have to wait until the locks are released. This ensures serializability, but may cause deadlock, blocking, and reduced concurrency. Examples of pessimistic methods are two-phase locking (2PL), timestamp ordering (TO), and distributed locking (DL).

- Optimistic methods allow conflicts to occur, but detect and resolve them before committing transactions. Transactions do not acquire locks on data items, but instead keep track of their read and write sets. Before committing, transactions validate their read and write sets against other concurrent transactions, and abort and restart if any conflict is detected. This avoids deadlock, blocking, and increases concurrency, but may cause more aborts and restarts. Examples of optimistic methods are validation (or certification), multiversion concurrency control (MVCC), and snapshot isolation (SI).

The following table summarizes some of the advantages and disadvantages of the different concurrency control methods:

| Method | Advantages | Disadvantages |
|--------|------------|---------------|
| 2PL | Simple, ensures serializability and strictness | May cause deadlock, blocking, reduced concurrency, and high locking overhead |
| TO | Avoids deadlock, ensures serializability and strictness | May cause blocking, reduced concurrency, and high timestamp management overhead |
| DL | Allows distributed transactions to acquire locks on multiple data servers | May cause deadlock, blocking, reduced concurrency, and high communication overhead |
| Validation | Avoids deadlock, blocking, and increases concurrency | May cause more aborts and restarts, and high validation overhead |
| MVCC | Avoids deadlock, blocking, and increases concurrency | May cause more storage and garbage collection overhead, and non-serializable anomalies |
| SI | Avoids deadlock, blocking, and increases concurrency | May cause non-serializable anomalies, such as write skew and read skew |