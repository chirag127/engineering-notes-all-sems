# Atomic Commit in Distributed Database System

- Atomic commit is an operation that applies a set of distinct changes as a single operation.
- Atomic commit ensures the atomicity property of transactions, which means either all or none of the changes are made.
- Atomic commit is of prime importance in distributed database systems, where transactions may span multiple sites and failures may occur .
- Atomic commit protocols are algorithms that coordinate the sites involved in a transaction and decide whether to commit or abort the transaction.
- Atomic commit protocols can be classified into two categories: blocking and non-blocking .
  - Blocking protocols may block the progress of some transactions if a site fails during the commit process .
  - Non-blocking protocols guarantee the progress of all transactions regardless of failures, but they may require more messages or additional assumptions .
- Some examples of blocking protocols are two-phase commit (2PC), three-phase commit (3PC), and presumed commit .
- Some examples of non-blocking protocols are presumed abort, non-blocking 2PC, and failure-aware commit (FLAC)  .
- Atomic commit protocols can be integrated with other components of distributed database systems, such as concurrency control, replication, and recovery.
- Atomic commit protocols can be optimized for different scenarios, such as read-only transactions, single-site transactions, or network partitions.