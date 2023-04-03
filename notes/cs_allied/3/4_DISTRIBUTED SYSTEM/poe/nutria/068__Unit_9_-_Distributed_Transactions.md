
## Unit 9 - Distributed Transactions

* A distributed transaction is a database transaction in which two or more networked computer systems are involved.
* The most common type of distributed transaction is the two-phase commit protocol, which ensures that all systems involved in the transaction either commit or roll back their changes.
* The two-phase commit protocol involves a coordinator and one or more participants. The coordinator is responsible for initiating the transaction and ensuring that all participants are in agreement with the changes.
* The first phase of the two-phase commit protocol is the prepare phase, in which the coordinator sends a message to all participants informing them of the transaction. Each participant then has the opportunity to either commit or abort the transaction.
* The second phase of the two-phase commit protocol is the commit phase, in which the coordinator sends a message to all participants informing them that the transaction has been committed. All participants must then commit their changes.
* Distributed transactions can be used to ensure data consistency across multiple systems. They can also be used to ensure that data is not corrupted during a transaction.
* Distributed transactions can be complex and difficult to implement, and they can have a significant impact on system performance. Therefore, it is important to understand the trade-offs involved in using distributed transactions.