### Atomic Commit in Distributed Database System

- A distributed database system consists of multiple database sites that are connected by a communication network.
- A distributed transaction is a transaction that accesses data from multiple sites and updates them atomically.
- Atomicity means that either all the updates are committed or none of them are committed, leaving the database in a consistent state.
- Atomic commit is the process of coordinating the decision to commit or abort a distributed transaction among all the participating sites.
- Atomic commit is essential to ensure the ACID properties of distributed transactions, especially the atomicity and durability properties.
- Atomic commit is challenging because of the possibility of site failures, network failures, and communication delays in a distributed system.
- Atomic commit protocols are algorithms that enable the participating sites to reach a consensus on the outcome of a distributed transaction, despite the presence of failures and uncertainties.
- Atomic commit protocols can be classified into two categories: blocking and non-blocking protocols.
- Blocking protocols are protocols that require the participation of all the sites to reach a decision. If some sites fail, the protocol blocks until they recover or are replaced.
- Non-blocking protocols are protocols that can reach a decision without waiting for the failed sites to recover. They use techniques such as timeouts, majority voting, and backup coordinators to cope with failures.
- Examples of blocking protocols are the two-phase commit protocol (2PC) and the three-phase commit protocol (3PC).
- Examples of non-blocking protocols are the Paxos commit protocol, the FLAC protocol, and the Skeen protocol.
- Atomic commit protocols have trade-offs between performance, availability, and fault-tolerance. Blocking protocols are simpler and faster, but less available and fault-tolerant. Non-blocking protocols are more available and fault-tolerant, but more complex and slower.
- Atomic commit protocols are an important component of distributed database systems, as they ensure the consistency and reliability of distributed transactions.