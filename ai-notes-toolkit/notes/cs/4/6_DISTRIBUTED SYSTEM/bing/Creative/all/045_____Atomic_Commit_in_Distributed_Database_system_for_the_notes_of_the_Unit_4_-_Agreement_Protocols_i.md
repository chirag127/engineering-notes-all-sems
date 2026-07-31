# Atomic Commit in Distributed Database System

- An atomic commit is an operation that applies a set of distinct changes as a single operation.
- If the changes are applied, then the atomic commit is said to have succeeded. If the changes are not applied, then the atomic commit is said to have failed or aborted.
- In distributed database systems, the primary need for atomic commit protocols is to maintain the atomicity of distributed transactions .
- Atomicity is the property that ensures that either all the data changes made by a transaction are committed or none of them are.
- Atomic commit protocols coordinate the distinct operations of a transaction across different database sites and decide whether to commit or abort the transaction  .
- Atomic commit protocols can be classified into two categories: blocking and non-blocking .
- Blocking protocols are those that may block the progress of some transactions if some of the sites participating in the transaction fail .
- Non-blocking protocols are those that guarantee the progress of some transactions even if some of the sites participating in the transaction fail .
- Examples of blocking protocols are two-phase commit (2PC) and three-phase commit (3PC)  .
- Examples of non-blocking protocols are Paxos commit, consensus commit, and FLAC  .
- Blocking protocols are simpler and more efficient than non-blocking protocols in the absence of failures, but they may cause unnecessary aborts or delays in the presence of failures .
- Non-blocking protocols are more resilient and fault-tolerant than blocking protocols, but they may incur more communication and computation overheads .
- Atomic commit protocols can also be integrated with other protocols, such as concurrency control, replication, and recovery, to optimize the performance and reliability of distributed database systems.