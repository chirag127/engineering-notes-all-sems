### Locks for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A lock is a mechanism that allows only one of the innumerable nodes or processes to access and modify a resource or data that is being shared commonly to prevent execution of same task twice and also maintain data integrity.
- Locks are designed to enforce a mutual exclusion concurrency control policy, which means that only one transaction can hold a lock on a data item at a time.
- Locks can be classified into different types based on the following criteria:
  - The granularity of the data item being locked, such as record-level, page-level, or table-level locks.
  - The mode of the lock, such as shared (read) or exclusive (write) locks.
  - The duration of the lock, such as long (until the transaction commits or aborts) or short (until the operation finishes) locks.
  - The protocol of acquiring and releasing locks, such as two-phase locking (2PL), timestamp ordering, or optimistic concurrency control.
- In distributed systems, locks can be implemented using different strategies, such as:
  - Wait-and-see strategy, which involves pausing the operation until the lock is available or a timeout occurs.
  - Retry strategy, which involves aborting the operation and retrying it later with a backoff mechanism.
  - Fail-fast strategy, which involves aborting the operation and returning an error immediately.
- Distributed locks can be based on different types of systems, such as:
  - Distributed systems based on asynchronous replication, such as MySQL, Tair, and Redis, which use a leader-follower model and rely on the leader node to grant locks.
  - Paxos-based distributed consensus systems, such as ZooKeeper, etcd, and Consul, which use a quorum-based model and rely on a majority of nodes to agree on locks.
  - Distributed systems based on atomic operations, such as Redis, which use a single-key model and rely on the atomicity of operations such as SETNX and EXPIRE to acquire and release locks.