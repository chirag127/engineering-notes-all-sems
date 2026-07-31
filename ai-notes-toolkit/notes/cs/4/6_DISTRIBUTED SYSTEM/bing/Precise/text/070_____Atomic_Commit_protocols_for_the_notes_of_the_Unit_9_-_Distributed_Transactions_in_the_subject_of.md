### Atomic Commit protocols

- Atomic Commit Protocol guarantees the atomicity property of a transaction in which all transactions are completed or not in the system .
- Distributed transaction refers to the transaction in which multiple servers are involved .
- In a distributed system, the atomic commit protocol ensures that a transaction is either committed or rolled back in its entirety, even if the system fails or some of the nodes fail or crash .
- This is important for maintaining the consistency and integrity of the data in the system .
- To achieve an atomic commit of distributed transactions, two-phase commit protocol (2PC) is employed, a type of atomic commitment protocol .
- Distributed transaction involves atomic commit, atomic visibility, and global consistency .
- 2PC is the only practical solution for atomic commit .