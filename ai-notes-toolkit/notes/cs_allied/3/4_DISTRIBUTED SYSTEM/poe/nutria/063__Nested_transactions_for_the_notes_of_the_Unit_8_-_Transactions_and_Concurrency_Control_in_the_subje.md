
### Nested Transactions

Nested transactions are database transactions that are nested within other transactions. They are used to ensure data integrity when multiple operations are performed in a single transaction. 

Nested transactions are typically used in distributed systems, where multiple operations must be performed in order to complete a single task. Nested transactions provide a way to ensure that all operations are completed successfully, or none of them are.

The following are the key concepts related to nested transactions:

1. Atomicity: All operations within a nested transaction must be completed successfully in order for the entire transaction to succeed. If any operation fails, then all operations within the transaction must be rolled back.

2. Isolation: Nested transactions must be isolated from each other in order to ensure that the data integrity of each transaction is maintained.

3. Durability: All operations within a nested transaction must be durable, meaning that the data must be persisted in a reliable storage system in order for the transaction to be completed successfully.

4. Consistency: All operations within a nested transaction must be consistent, meaning that the data must be valid and consistent with the rules of the database.