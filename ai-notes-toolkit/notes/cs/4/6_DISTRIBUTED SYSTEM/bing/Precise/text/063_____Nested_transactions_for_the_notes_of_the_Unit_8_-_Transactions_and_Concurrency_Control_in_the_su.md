### Nested Transactions
- A nested transaction is a transaction that is executed within the context of another transaction, called the parent transaction.
- The parent transaction can have multiple nested transactions, and each nested transaction can have its own nested transactions, forming a hierarchy of transactions.
- The changes made by a nested transaction are not visible to other transactions until the parent transaction commits.
- If a nested transaction aborts, its changes are rolled back, but the parent transaction can continue executing.
- If the parent transaction aborts, all changes made by its nested transactions are rolled back.
- Nested transactions provide a way to structure complex transactions and to handle partial failures.
- They are commonly used in distributed systems, where a transaction may involve multiple servers, and each server may execute its part of the transaction as a nested transaction.
- Nested transactions can be implemented using savepoints, which allow a transaction to roll back to a specific point in its execution.
- The two-phase commit protocol can be used to coordinate the commit or abort of nested transactions across multiple servers.