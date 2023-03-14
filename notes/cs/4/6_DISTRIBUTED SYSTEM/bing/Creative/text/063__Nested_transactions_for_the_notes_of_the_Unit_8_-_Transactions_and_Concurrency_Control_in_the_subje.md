### Nested transactions

- A nested transaction is a transaction that is composed of subtransactions, each of which may be distributed across multiple servers.
- A nested transaction has a hierarchical structure, where the top-level transaction is the parent of all subtransactions, and each subtransaction may have its own children.
- A nested transaction is atomic, meaning that either all of its subtransactions commit or all of them abort.
- A nested transaction is also isolated, meaning that it does not interfere with other concurrent transactions.
- A nested transaction can provide more flexibility and concurrency than a flat transaction, which has a single begin and end point.
- A nested transaction can also support partial rollback and recovery, where a subtransaction can abort without affecting its siblings or parent.
- A nested transaction can be implemented using various protocols, such as the two-phase commit protocol, the nested two-phase commit protocol, or the sagas protocol.