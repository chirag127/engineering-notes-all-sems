### Atomic Commit protocols for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

Atomic Commit protocols are used in distributed transactions to ensure that all participants in the transaction either commit or abort the transaction together. The goal of these protocols is to maintain the atomicity property of transactions in a distributed system. 

Here are some important points to remember about Atomic Commit protocols:

- Atomic Commit protocols are used to ensure that all participants in a transaction either commit or abort together. This ensures that the transaction is atomic in nature and maintains data consistency.
- Two-phase commit protocol (2PC) is one of the most widely used Atomic Commit protocols. It is a blocking protocol that ensures that all participants either commit or abort the transaction before returning control to the application.
- In the first phase of 2PC, the transaction coordinator sends a prepare message to all participants. The participants respond with a vote indicating whether they can commit or not. 
- If all participants vote to commit, the coordinator sends a commit message to all participants. If any participant votes to abort, the coordinator sends an abort message to all participants. 
- 2PC is a blocking protocol, which means that it can lead to performance issues in a distributed system with a large number of participants. 
- Three-phase commit protocol (3PC) is an extension of 2PC that aims to reduce the blocking time by adding an extra phase to the protocol. 
- In the first phase of 3PC, the transaction coordinator sends a prepare message to all participants. The participants respond with a vote indicating whether they can commit or not, but do not commit yet. 
- In the second phase, the coordinator sends a pre-commit message to all participants. The participants respond with an acknowledgement. 
- In the third phase, the coordinator sends a commit message to all participants. If any participant fails to respond, the coordinator sends an abort message to all participants. 
- 3PC reduces the blocking time compared to 2PC, but it is more complex and requires more communication between participants. 

In conclusion, Atomic Commit protocols are important in maintaining the atomicity property of transactions in a distributed system. Two-phase commit protocol (2PC) and Three-phase commit protocol (3PC) are two widely used protocols. While 2PC is a blocking protocol and can lead to performance issues, 3PC reduces the blocking time but is more complex.