### Atomic Commit protocols for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

In distributed systems, transactions often involve multiple resources and processes that are distributed across different nodes. Atomic commit protocols are used to ensure the atomicity property of distributed transactions, which means that either all the operations in a transaction are executed successfully or none of them are executed at all.

There are several atomic commit protocols that are commonly used in distributed systems. Some of these protocols are:

1. Two-Phase Commit (2PC)
   - This protocol is widely used in distributed systems and involves a coordinator and multiple participants.
   - The protocol works in two phases: the prepare phase and the commit phase.
   - During the prepare phase, the coordinator sends a prepare message to all the participants, asking them to prepare for the transaction. If all participants are ready, they send a "yes" vote to the coordinator, otherwise, they send a "no" vote.
   - If all participants send a "yes" vote, the coordinator sends a commit message to all participants, asking them to commit the transaction. Otherwise, the coordinator sends an abort message to all participants, asking them to abort the transaction.
   - The main advantage of this protocol is that it ensures atomicity of transactions, even in the presence of failures.

2. Three-Phase Commit (3PC)
   - This protocol is an extension of the 2PC protocol and involves three phases: the prepare phase, the ready phase, and the commit phase.
   - During the prepare phase, the coordinator sends a prepare message to all the participants, asking them to prepare for the transaction. If all participants are ready, they send a "ready" message to the coordinator, otherwise, they send a "abort" message.
   - During the ready phase, the coordinator sends a commit request to all the participants, asking them if they are ready to commit the transaction.
   - If all participants are ready, they send a "ready" message to the coordinator, otherwise, they send a "abort" message.
   - During the commit phase, the coordinator sends a commit message to all the participants, asking them to commit the transaction. If any participant fails to commit, the coordinator sends an abort message to all participants.
   - The main advantage of this protocol is that it reduces the blocking time during the prepare phase of the 2PC protocol.

Mnemonic: "2PC and 3PC, prepare, ready, and commit phase; ensuring atomicity in distributed transactions is their main aim!" 

In conclusion, atomic commit protocols are essential in ensuring the atomicity property of distributed transactions. The choice of protocol depends on the specific requirements of the application and the nature of the distributed system. Mnemonics can be used as a learning trick to remember the different phases of the protocols.