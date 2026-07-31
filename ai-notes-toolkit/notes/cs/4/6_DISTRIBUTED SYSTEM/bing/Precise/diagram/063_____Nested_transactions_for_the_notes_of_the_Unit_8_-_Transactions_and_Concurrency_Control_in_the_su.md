### Unit 8 - Transactions and Concurrency Control in DISTRIBUTED SYSTEMS
#### Nested Transactions

- A nested transaction is a transaction that is executed within the context of another transaction, called the parent transaction.
- Nested transactions provide a way to structure complex transactions into smaller, more manageable units.
- Each nested transaction has its own independent workspace, which is used to store changes made during the transaction.
- If a nested transaction commits, its changes are saved to the workspace of its parent transaction.
- If a nested transaction aborts, its changes are discarded and do not affect the parent transaction.
- The parent transaction can choose to commit or abort the changes made by its nested transactions.
- Nested transactions can be used to implement advanced concurrency control techniques, such as optimistic concurrency control and multiversion concurrency control.
- Nested transactions can also be used to implement advanced recovery techniques, such as nested top actions and partial rollbacks.
