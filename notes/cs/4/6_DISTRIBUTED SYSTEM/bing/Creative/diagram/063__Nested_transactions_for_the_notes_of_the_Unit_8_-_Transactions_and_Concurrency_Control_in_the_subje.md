A nested transaction is a transaction that consists of sub-transactions that can be executed independently and can be committed or aborted separately. A nested transaction can be used to improve the concurrency and fault tolerance of a distributed system. A nested transaction has a tree structure, where the root is the top-level transaction and the leaves are the sub-transactions. A sub-transaction can be either atomic or nested itself. A nested transaction can be committed only if all its sub-transactions are committed, and it can be aborted if any of its sub-transactions are aborted. A nested transaction can also be partially committed, which means that some of its sub-transactions are committed and some are aborted. A partial commit can be useful for preserving some of the work done by the sub-transactions, but it may violate the atomicity property of the top-level transaction.

The following diagram illustrates the basic structure of a nested transaction using ASCII characters:

```
    +-----------------+
    | Top-level       |
    | transaction T   |
    +-----------------+
    /        |        \
   /         |         \
  /          |          \
 /           |           \
+---+      +---+       +---+
| S |      | S |       | S |
| 1 |      | 2 |       | 3 |
+---+      +---+       +---+
  |          |           |
  |          |           |
+---+      +---+       +---+
| A |      | A |       | A |
| 1 |      | 2 |       | 3 |
+---+      +---+       +---+
  |          |           |
  |          |           |
+---+      +---+       +---+
| N |      | N |       | N |
| 1 |      | 2 |       | 3 |
+---+      +---+       +---+
 / \        / \         / \
/   \      /   \       /   \
A   A     A    A      A    A
1.1 1.2   2.1  2.2    3.1  3.2
```

In this diagram, T is the top-level transaction, S1, S2, and S3 are sub-transactions that are atomic, A1, A2, and A3 are sub-transactions that are nested, and N1, N2, and N3 are sub-transactions that are nested and atomic. A1.1, A1.2, A2.1, A2.2, A3.1, and A3.2 are the leaf sub-transactions that perform the actual operations on the data. Each sub-transaction has a parent transaction that initiated it, and a set of child transactions that it initiated. A sub-transaction can communicate with its parent and its children, but not with its siblings or other sub-transactions in the tree. A sub-transaction can also access the data that is shared by its ancestors, but not by its descendants or other sub-transactions in the tree. A sub-transaction can commit or abort independently of its parent or its children, but it must notify them of its decision. A sub-transaction can also delegate its decision to its parent or its children, if it does not have enough information or authority to make the decision by itself. A sub-transaction can also request a vote from its parent or its children, if it wants to reach a consensus on the decision.

The advantages of using nested transactions are:

- They can increase the concurrency of the system, by allowing sub-transactions to execute in parallel and to access different data sets.
- They can improve the fault tolerance of the system, by allowing sub-transactions to recover from failures and to retry or compensate for failed operations.
- They can reduce the locking overhead of the system, by allowing sub-transactions to use finer-grained locks and to release them earlier.
- They can simplify the programming of the system, by allowing sub-transactions to encapsulate complex operations and to hide the details of the distributed coordination.

The disadvantages of using nested transactions are:

- They can increase the complexity of the system, by requiring more communication and synchronization among sub-transactions and by introducing partial commits and compensating actions.
- They can reduce the consistency of the system, by allowing partial commits and by violating the atomicity property of the top-level transaction.
- They can increase the overhead of the system, by requiring more logging and checkpointing of sub-transactions and by creating more intermediate states and versions of the