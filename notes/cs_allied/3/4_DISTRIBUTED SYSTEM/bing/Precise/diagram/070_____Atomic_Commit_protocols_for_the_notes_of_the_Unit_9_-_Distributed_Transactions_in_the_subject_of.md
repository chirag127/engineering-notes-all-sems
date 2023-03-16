### Atomic Commit protocols

Atomic Commit protocols are used to guarantee the atomicity property of a transaction in a distributed system. This means that all transactions are either completed or not in the system. Distributed transactions refer to transactions in which multiple servers are involved.

In a distributed system, the atomic commit protocol ensures that a transaction is either committed or rolled back in its entirety, even if the system fails or some of the nodes fail or crash. This is important for maintaining the consistency and integrity of the data in the system.

One of the most commonly used atomic commit protocols is the two-phase commit protocol (2PC). It is a type of atomic commitment protocol that is used to achieve an atomic commit of distributed transactions. Distributed transactions involve atomic commit, atomic visibility, and global consistency. 2PC is the only practical solution for atomic commit.

There are also other atomic commit protocols, such as the parallel commit protocol, which aims to reduce the latency of transactions down to only a single round-trip of distributed consensus. To accomplish this goal, the two-phase commit protocol is replaced and the way transactions arrive at a committed state is reworked.