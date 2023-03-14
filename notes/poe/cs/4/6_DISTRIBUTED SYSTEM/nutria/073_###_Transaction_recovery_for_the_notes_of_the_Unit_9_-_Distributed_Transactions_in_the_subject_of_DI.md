
### Transaction Recovery for the Notes of Unit 9 - Distributed Transactions in the Subject of Distributed Systems 

Transaction recovery is a process used by distributed systems to ensure that all transactions are completed correctly. This is done by using a combination of techniques such as logging, checkpointing, and two-phase commit. 

1. **Logging**: This technique involves recording all the transactions that are executed in the system. This allows the system to recover from failures by replaying the logged transactions. 

2. **Checkpointing**: This technique involves periodically saving the state of the system. This allows the system to recover from failures by restoring the system to the state that was saved in the checkpoint. 

3. **Two-Phase Commit**: This technique involves committing all transactions in two phases. The first phase involves all the participants agreeing to commit the transaction. The second phase involves all the participants committing the transaction. This ensures that all the participants agree on the outcome of the transaction. 

Transaction recovery is an important part of distributed systems. It ensures that all transactions are completed correctly and that the system is resilient to failures. It is important to understand the different techniques used for transaction recovery in order to ensure that the system is reliable.