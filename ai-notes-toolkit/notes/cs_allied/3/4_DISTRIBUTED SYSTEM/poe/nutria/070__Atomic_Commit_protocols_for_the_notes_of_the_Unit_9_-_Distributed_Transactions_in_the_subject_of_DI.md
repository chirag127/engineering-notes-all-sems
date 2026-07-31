
### Atomic Commit protocols for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

* Atomic commit protocols are used to ensure that a distributed transaction is either completed in its entirety or not at all.
* The two-phase commit protocol is the most widely used atomic commit protocol. It consists of two phases: the prepare phase and the commit phase. 
* In the prepare phase, the transaction coordinator sends a prepare request to all the participants in the transaction. The participants then vote on whether they are willing to accept the transaction. 
* If all the participants vote yes, then the transaction coordinator sends a commit request in the commit phase. Once all the participants have received the commit request, the transaction is committed. 
* If any of the participants vote no, then the transaction coordinator sends an abort request and the transaction is aborted. 
* The three-phase commit protocol is an extension of the two-phase commit protocol. It adds an extra phase, the pre-commit phase, in which the participants can communicate with each other before voting. 
* The main advantage of the three-phase commit protocol is that it allows for better coordination among the participants and can reduce the chance of conflicts between transactions. 
* The distributed transaction protocol is a variation of the two-phase commit protocol. It allows for multiple transactions to be coordinated in a single distributed transaction. 
* This protocol is used when multiple operations need to be done in a single transaction and the participants need to coordinate with each other in order to ensure the correctness of the transaction. 
* The optimistic concurrency control protocol is an alternative to the two-phase commit protocol. It allows for transactions to be executed in parallel without the need for coordination. 
* The main advantage of this protocol is that it reduces the overhead of the two-phase commit protocol and allows for faster transaction execution. 
* The consensus-based commit protocol is another alternative to the two-phase commit protocol. It allows for transactions to be committed without the need for a centralized coordinator. 
* This protocol is used when there are multiple participants in the transaction and they need to agree on the outcome of the transaction. 
* The Paxos protocol is an example of a consensus-based commit protocol. It allows for transactions to be committed without the need for a centralized coordinator.