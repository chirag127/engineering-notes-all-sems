# Unit 8 - Transactions and Concurrency Control in Distributed Systems

### Timestamp Ordering

Timestamp ordering is a concurrency control protocol used in distributed systems to ensure serializability of transactions. It assigns a unique timestamp to each transaction, which represents the order in which the transactions are to be executed.

- Each transaction is assigned a unique timestamp when it enters the system.
- The timestamp of a transaction determines its priority in conflict resolution.
- If two transactions conflict, the one with the earlier timestamp is allowed to proceed, while the other must wait or be rolled back.
- Timestamps can be assigned using either the system time or a logical counter.
- Timestamp ordering ensures conflict serializability, but not necessarily recoverability or cascadelessness.
- One of the main advantages of timestamp ordering is that it is a decentralized protocol, which makes it suitable for distributed systems.
- However, timestamp ordering can suffer from the "Thomas write rule" problem, where a transaction may be allowed to write an older value, resulting in an inconsistent database state.
