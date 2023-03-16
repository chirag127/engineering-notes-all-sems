### Recovery in Distributed Database Systems

- Recovery in distributed database systems is the process of restoring the database to a consistent state after a failure or an error .
- Recovery in distributed database systems is more complicated than in centralized database systems because failures can occur at multiple sites or communication links.
- Recovery in distributed database systems aims to maintain the atomicity and durability of distributed transactions, which are transactions that span multiple sites.
- Recovery in distributed database systems can be classified into two types: local recovery and global recovery .
- Local recovery is the recovery of a single site from a failure or an error. Local recovery techniques include transaction undo, transaction redo, shadow paging, and checkpointing .
- Global recovery is the recovery of the entire distributed database system from a failure or an error that affects multiple sites or communication links. Global recovery techniques include two-phase commit, three-phase commit, presumed abort, presumed commit, and non-blocking commit .
- Global recovery techniques rely on the exchange of messages and votes among the participating sites to reach a consensus on the outcome of a distributed transaction.
- Global recovery techniques also use logs, timestamps, and locks to record and coordinate the actions of distributed transactions .
- Global recovery techniques have different trade-offs in terms of performance, reliability, availability, and complexity.