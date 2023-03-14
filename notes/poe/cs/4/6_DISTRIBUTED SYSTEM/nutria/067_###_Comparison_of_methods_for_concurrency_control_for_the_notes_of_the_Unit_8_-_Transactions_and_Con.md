
### Comparison of Methods for Concurrency Control for the Notes of the Unit 8 - Transactions and Concurrency Control in the Subject of DISTRIBUTED SYSTEM

- **Time Stamp Ordering (TSO)**: This method is based on the idea of assigning a timestamp to each transaction. Whenever a transaction is executed, a timestamp is assigned to it. This timestamp is then used to order the transactions in the order in which they were executed. The transactions are then executed in the same order. This method is simple to implement but it does not guarantee serializability. 

- **Lock-Based Protocols**: This method is based on the idea of locking the resources that are accessed by the transactions. When a transaction wants to access a resource, it must acquire a lock on the resource. This lock will prevent any other transaction from accessing the same resource. This method is more complex to implement but it guarantees serializability.

- **Optimistic Concurrency Control (OCC)**: This method is based on the idea of allowing transactions to execute without locking the resources. The transactions are then checked for conflicts after they have been executed. If a conflict is detected, the conflicting transactions are rolled back and re-executed. This method is more efficient than lock-based protocols but it does not guarantee serializability.

- **Mnemonics and Learning Tricks**: To remember the different methods of concurrency control, you can use the acronym TSLO (Time Stamp Ordering, Lock-Based Protocols, Optimistic Concurrency Control).