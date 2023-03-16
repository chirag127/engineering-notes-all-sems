### Concurrency control in distributed transactions

- Concurrency control is the process of managing the concurrent execution of transactions in a distributed database system, such that the ACID properties are preserved .
- Concurrency control is necessary to avoid conflicts and inconsistencies that may arise due to the interleaved execution of transactions that access and modify shared data .
- Concurrency control can be achieved by using various techniques, such as locking, timestamping, optimistic methods, or serialization .
- Locking-based concurrency control protocols use the concept of locking data items before accessing or modifying them, to prevent other transactions from interfering with them .
- Timestamp-based concurrency control algorithms use a transaction’s timestamp to order the execution of conflicting operations, such that older transactions have priority over newer ones .
- Optimistic concurrency control methods assume that conflicts are rare and allow transactions to execute without any synchronization, but validate them before committing to ensure serializability .
- Serialization is the property that ensures that the concurrent execution of transactions is equivalent to some serial execution of the same transactions, where no two transactions are interleaved .
- Distributed concurrency control protocols have to deal with additional challenges, such as network delays, communication failures, partial failures, and distributed deadlock detection and resolution .
- Distributed concurrency control protocols can be classified into two categories: centralized and decentralized .
- Centralized concurrency control protocols rely on a single coordinator node to manage the concurrency control of all transactions in the system, which may introduce a single point of failure and a performance bottleneck .
- Decentralized concurrency control protocols distribute the responsibility of concurrency control among multiple nodes, which may increase the scalability and fault-tolerance of the system, but also increase the complexity and overhead of coordination .
- Examples of centralized concurrency control protocols are two-phase locking (2PL), two-phase commit (2PC), and three-phase commit (3PC) .
- Examples of decentralized concurrency control protocols are distributed 2PL, distributed 2PC, distributed optimistic concurrency control, and distributed timestamp ordering  .