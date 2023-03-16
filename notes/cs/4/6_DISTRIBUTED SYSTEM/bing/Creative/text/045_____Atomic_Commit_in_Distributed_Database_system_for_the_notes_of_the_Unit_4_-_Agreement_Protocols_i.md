### Atomic Commit in Distributed Database System

- A distributed database system consists of multiple database sites that are connected by a communication network.
- A distributed transaction is a transaction that accesses data from multiple sites and updates them atomically.
- Atomicity means that either all the updates are committed or none of them are, leaving the database in a consistent state.
- Atomic commit is the process of ensuring that all the sites involved in a distributed transaction agree on the final outcome of the transaction, whether it is commit or abort.
- Atomic commit is essential for maintaining the ACID properties of transactions in a distributed database system, especially in the presence of failures or network partitions.
- Atomic commit protocols are the algorithms that coordinate the decision making among the sites and handle the possible failures or conflicts.
- Atomic commit protocols can be classified into two categories: blocking and non-blocking.
- Blocking protocols are those that require some sites to wait for the response of other sites before committing or aborting their local updates. These protocols may block indefinitely if some sites fail or become unreachable.
- Non-blocking protocols are those that do not require any site to wait for the response of other sites. These protocols can guarantee the termination of the atomic commit process even if some sites fail or become unreachable.
- Examples of blocking protocols are the two-phase commit protocol (2PC) and the three-phase commit protocol (3PC).
- Examples of non-blocking protocols are the Paxos commit protocol and the FLAC protocol.