### Atomic Commit protocols for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

Distributed transactions involve multiple processes or systems coordinating with each other to execute a transaction. Atomic commit protocols ensure that either all of the participating processes commit or none of them do. Here are some important points to keep in mind when dealing with atomic commit protocols:

- Atomicity: Atomic commit protocols ensure that a transaction either completes successfully on all participating processes or is rolled back on all of them. This guarantees that the system is always in a consistent state.

- Two-phase commit (2PC): 2PC is a widely-used atomic commit protocol. In the first phase, the coordinator sends a prepare message to all the participating processes. If all the processes respond with a yes, the coordinator sends a commit message in the second phase. If even one process responds with a no, the coordinator sends an abort message to all processes, and the transaction is rolled back.

- Three-phase commit (3PC): 3PC is an improvement over 2PC. In this protocol, a third phase is added before the commit phase. The coordinator sends a pre-commit message in the third phase to check if all processes are ready to commit. If all processes respond with a yes, the coordinator sends a commit message in the next phase. If any process responds with a no, the coordinator sends an abort message to all processes.

- Drawbacks of 2PC: While 2PC is widely used, it has some drawbacks. It can lead to blocking if a participant fails and does not respond to the prepare message. In addition, it can cause a cascading rollback if a participant fails after sending a yes response to the prepare message.

- Drawbacks of 3PC: 3PC addresses some of the issues with 2PC, but it is not perfect. It can still lead to blocking if a participant fails after sending a pre-commit message. In addition, it can lead to a loss of atomicity if the coordinator fails after sending the pre-commit message.

- Other protocols: There are other atomic commit protocols, such as the Paxos protocol and the Raft protocol. These protocols are more complex than 2PC and 3PC but provide better fault tolerance and scalability.

In summary, atomic commit protocols are essential for ensuring the consistency of distributed transactions. While 2PC is widely used, it has some drawbacks that 3PC and other protocols attempt to address. It is important to understand the strengths and weaknesses of each protocol in order to choose the right one for a given system.