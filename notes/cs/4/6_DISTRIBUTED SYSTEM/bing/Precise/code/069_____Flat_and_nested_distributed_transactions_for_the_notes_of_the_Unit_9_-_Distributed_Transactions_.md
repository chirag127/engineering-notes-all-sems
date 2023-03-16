### Flat and Nested Distributed Transactions

Distributed transactions are transactions that involve multiple systems or resources, often across different locations or networks. These transactions are used to ensure data consistency and integrity in distributed systems.

There are two main types of distributed transactions: flat and nested.

1. **Flat Distributed Transactions**: A flat distributed transaction is a single transaction that involves multiple resources or systems. All the operations in the transaction are treated as a single unit of work, and either all of them are committed or all of them are rolled back. This type of transaction is also known as a two-phase commit (2PC) transaction.

2. **Nested Distributed Transactions**: A nested distributed transaction is a transaction that contains other transactions, called subtransactions. Each subtransaction can involve multiple resources or systems, and can be committed or rolled back independently of the other subtransactions. This type of transaction is also known as a multi-level transaction.

In summary, flat distributed transactions treat all operations as a single unit of work, while nested distributed transactions allow for more fine-grained control over the individual subtransactions. Both types of transactions are used to ensure data consistency and integrity in distributed systems.