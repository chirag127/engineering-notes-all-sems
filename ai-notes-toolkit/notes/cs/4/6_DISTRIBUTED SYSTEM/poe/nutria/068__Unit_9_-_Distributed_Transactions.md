
## Unit 9 - Distributed Transactions

* Distributed transactions are transactions that span multiple systems, such as multiple databases, message queues, and web services.
* A distributed transaction is a single operation that is composed of multiple sub-operations, each of which is executed on a different system.
* Distributed transactions are more complex than traditional transactions, since they require coordination between multiple systems.
* The two-phase commit protocol is the most commonly used protocol for coordinating distributed transactions.
* The two-phase commit protocol consists of two phases: the prepare phase and the commit phase.
* In the prepare phase, the transaction coordinator sends a prepare message to all the participating systems.
* The participating systems then decide whether or not to commit the transaction.
* If all the systems agree to commit the transaction, the transaction coordinator sends a commit message to all the participating systems.
* If any of the systems decide not to commit the transaction, the transaction coordinator sends an abort message to all the participating systems.
* Distributed transactions can be used to ensure that data is consistent across multiple systems.