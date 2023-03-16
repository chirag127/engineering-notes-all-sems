# Nested Transactions

Nested transactions are a type of transaction that allows for sub-transactions to be created within a larger, parent transaction. This is useful in distributed systems where multiple operations may need to be performed as part of a single, larger transaction.

Here are some key points to remember about nested transactions:

1. A nested transaction is a transaction that is executed within the context of another transaction, known as the parent transaction.

2. The parent transaction can have multiple nested transactions, and each nested transaction can have its own nested transactions, forming a hierarchy of transactions.

3. If a nested transaction commits, its changes are not immediately made permanent. Instead, they are saved as part of the parent transaction.

4. If the parent transaction commits, all changes made by its nested transactions are made permanent. If the parent transaction aborts, all changes made by its nested transactions are discarded.

5. Nested transactions provide a way to structure complex transactions into smaller, more manageable units.

6. Nested transactions can improve the performance and reliability of distributed systems by allowing for more fine-grained control over transaction execution.

7. Nested transactions are commonly used in distributed databases, where multiple operations may need to be performed as part of a single, larger transaction.
