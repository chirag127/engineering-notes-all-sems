### Nested transactions

- A nested transaction is a transaction that is composed of subtransactions, each of which may have its own begin and end points.
- A nested transaction can be used to implement partial rollback, modular programming, and concurrency control in distributed systems.
- A nested transaction has a tree structure, where the root is the top-level transaction and the leaves are the subtransactions.
- A nested transaction can be either flat or nested distributed, depending on whether it accesses objects handled by different servers or not.
- A nested transaction can be either open or closed, depending on whether it allows communication with other transactions or not.
- A nested transaction can have different commit protocols, such as two-phase commit, nested two-phase commit, or multilevel commit, depending on how the subtransactions coordinate their decisions.
- A nested transaction can have different serializability criteria, such as conflict serializability, strict serializability, or snapshot serializability, depending on how the subtransactions order their operations.
- A nested transaction can have different recovery mechanisms, such as undo, redo, or compensation, depending on how the subtransactions handle failures.
- A nested transaction can have different deadlock detection and resolution strategies, such as timeout, wound-wait, or wait-die, depending on how the subtransactions handle conflicts.