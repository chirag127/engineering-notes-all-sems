### Nested Transactions

Nested transactions are a type of transaction that allows for multiple levels of transactions within a single transaction. This means that a transaction can contain other transactions, which can themselves contain further transactions, and so on. This allows for greater flexibility and control over the execution of transactions.

Some key points to note about nested transactions are:

- Nested transactions can be used to provide more fine-grained control over the execution of transactions, allowing for greater flexibility in managing complex operations.
- Each nested transaction has its own savepoint, which allows for partial rollbacks of the transaction if necessary.
- If a nested transaction is rolled back, all changes made within that transaction and any nested transactions within it are undone.
- If a nested transaction is committed, all changes made within that transaction and any nested transactions within it are made permanent.
- Nested transactions can be used to improve the performance of certain operations by reducing the amount of locking and contention required.

Nested transactions are commonly used in distributed systems to manage complex operations that span multiple nodes or databases. They provide a powerful tool for managing concurrency and ensuring the consistency of data in these systems.