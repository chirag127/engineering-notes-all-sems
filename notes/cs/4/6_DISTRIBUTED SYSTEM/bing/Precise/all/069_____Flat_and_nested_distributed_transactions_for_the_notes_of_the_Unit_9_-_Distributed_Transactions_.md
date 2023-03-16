# Unit 9 - Distributed Transactions

### Flat and Nested Distributed Transactions

- A distributed transaction is a transaction that spans multiple systems or resources.
- Flat distributed transactions involve multiple resources, but only a single transaction coordinator.
- Nested distributed transactions involve multiple resources and multiple transaction coordinators, with each coordinator managing a subset of the resources.
- In a flat distributed transaction, the transaction coordinator is responsible for ensuring that all resources involved in the transaction either commit or abort the transaction.
- In a nested distributed transaction, the top-level transaction coordinator is responsible for ensuring that all sub-coordinators either commit or abort their respective transactions.
- Nested distributed transactions allow for more fine-grained control over the transaction process, as sub-transactions can be committed or aborted independently of the overall transaction.
- However, nested distributed transactions can also be more complex to manage, as the coordination of multiple transaction coordinators must be carefully managed to ensure the overall consistency of the transaction.