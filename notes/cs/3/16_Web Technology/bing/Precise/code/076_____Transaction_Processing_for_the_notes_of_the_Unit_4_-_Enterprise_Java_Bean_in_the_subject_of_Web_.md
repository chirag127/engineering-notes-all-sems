### Transaction Processing

Transaction processing is a type of computer processing that takes place in the presence of a transaction. A transaction is a logical unit of work that must be either completed in its entirety or aborted. Transaction processing systems are designed to ensure that transactions are processed reliably and that the system remains in a consistent state even in the event of failures.

Some key features of transaction processing systems include:

1. **Atomicity:** This means that a transaction is treated as a single, indivisible unit of work. Either all the changes made during the transaction are committed, or none of them are.

2. **Consistency:** This means that the system must remain in a consistent state before and after the transaction. Any data written during the transaction must satisfy all the constraints defined by the system.

3. **Isolation:** This means that the changes made during a transaction must be isolated from other transactions until the transaction is committed. This ensures that other transactions do not see intermediate states of the data.

4. **Durability:** This means that once a transaction is committed, the changes made during the transaction must be permanent. The system must ensure that the changes are not lost due to any failures.

In the context of Enterprise Java Beans (EJB), transaction processing is handled by the EJB container. The container manages the transactions on behalf of the beans and ensures that the above properties are satisfied. EJBs can use either container-managed transactions or bean-managed transactions. In container-managed transactions, the container automatically starts and ends transactions, while in bean-managed transactions, the bean is responsible for managing the transactions.