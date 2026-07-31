### Transaction Processing

Transaction processing is a type of computer processing that takes place in the presence of a transaction. A transaction is a logical unit of work that must be either completed in its entirety or aborted. Transaction processing systems are designed to ensure that transactions are processed reliably and that the system remains in a consistent state even in the event of failures.

Some key features of transaction processing systems include:

1. **Atomicity**: This means that a transaction is treated as a single, indivisible unit of work. Either all of the changes made during the transaction are committed, or none of them are.

2. **Consistency**: This means that the system must remain in a consistent state before and after the transaction. Any data that is modified during the transaction must be valid according to the rules of the system.

3. **Isolation**: This means that each transaction must be executed in isolation from other transactions. The changes made by one transaction must not be visible to other transactions until the first transaction is committed.

4. **Durability**: This means that once a transaction is committed, its changes must be permanent. The system must ensure that the changes are not lost, even in the event of a failure.

In the context of Enterprise Java Beans (EJB), transaction processing is handled by the EJB container. The container manages the transactions on behalf of the beans, ensuring that the above properties are maintained. EJBs can be configured to use container-managed transactions, where the container automatically starts and commits transactions, or bean-managed transactions, where the bean is responsible for managing its own transactions.