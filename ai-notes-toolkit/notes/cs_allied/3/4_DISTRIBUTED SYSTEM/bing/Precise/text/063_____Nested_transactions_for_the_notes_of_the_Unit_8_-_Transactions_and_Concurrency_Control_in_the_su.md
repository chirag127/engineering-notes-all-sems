### Nested Transactions

Nested transactions are a type of transaction that allows for sub-transactions within a larger transaction. This is useful in distributed systems where multiple operations may need to be performed as part of a single transaction.

Some key points to remember about nested transactions are:

1. Nested transactions allow for more fine-grained control over the operations within a transaction.
2. Each sub-transaction can be committed or aborted independently of the others.
3. If a sub-transaction is aborted, it can be retried without affecting the other sub-transactions.
4. If the parent transaction is aborted, all sub-transactions are also aborted.
5. Nested transactions can help improve the performance of distributed systems by reducing the need for global coordination.

In summary, nested transactions provide a useful mechanism for managing complex transactions in distributed systems. They allow for more fine-grained control over the operations within a transaction and can help improve performance by reducing the need for global coordination.