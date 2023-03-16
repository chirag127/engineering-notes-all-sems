### Nested transactions

- A nested transaction is a transaction that is composed of subtransactions, each of which may have its own commit or abort point.
- A nested transaction can be used to implement partial rollback, modular programming, and concurrency control in distributed systems.
- A nested transaction has a hierarchical structure, where the top-level transaction is the parent of all subtransactions, and each subtransaction may have its own children.
- A nested transaction can be classified into two types: closed nested transactions and open nested transactions.
  - A closed nested transaction is a transaction that is fully contained within its parent transaction, and its commit or abort depends on the outcome of the parent transaction.
  - An open nested transaction is a transaction that can commit or abort independently of its parent transaction, and may have visible effects on other transactions or the database state.
- A nested transaction can be implemented using different models, such as the following:
  - The flat model, where all subtransactions are treated as a single transaction, and the commit or abort of the top-level transaction determines the fate of all subtransactions.
  - The strict model, where subtransactions can commit or abort only when their parent transaction commits or aborts, and the effects of subtransactions are not visible to other transactions until the top-level transaction commits.
  - The relaxed model, where subtransactions can commit or abort independently of their parent transaction, and the effects of subtransactions are visible to other transactions as soon as they commit.
  - The sagas model, where subtransactions can commit or abort independently of their parent transaction, and the effects of subtransactions are compensated by inverse operations in case of abort.
- A nested transaction can provide the following benefits in distributed systems:
  - It can reduce the communication overhead and the blocking time of distributed transactions, by allowing subtransactions to commit or abort locally without waiting for the global decision of the top-level transaction.
  - It can increase the concurrency and the availability of distributed transactions, by allowing subtransactions to access different data items or servers without conflicting with each other or with other transactions.
  - It can enhance the modularity and the reusability of distributed transactions, by allowing subtransactions to be defined as independent units of work that can be nested within different transactions or executed in parallel.
  - It can support the partial rollback and the recovery of distributed transactions, by allowing subtransactions to undo their effects in case of failure or abort, without affecting the rest of the transaction or the database state.