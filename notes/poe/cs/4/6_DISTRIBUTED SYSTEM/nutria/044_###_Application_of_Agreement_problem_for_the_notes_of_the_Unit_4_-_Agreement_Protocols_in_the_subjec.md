
### Application of Agreement problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

Agreement protocols are a type of distributed system protocol that is used to ensure that all nodes in a distributed system agree on a single value. Agreement protocols are used to ensure consistency of data across multiple nodes, and to ensure that all nodes have the same information.

The most common type of agreement protocol is the two-phase commit protocol. This protocol works by first having each node in the system send a message to the coordinator node. The coordinator node then sends a message to all the nodes asking them to agree on a single value. If all the nodes agree, then the coordinator node sends a message to all the nodes confirming the agreement.

Another type of agreement protocol is the three-phase commit protocol. This protocol works by having three phases: the prepare phase, the commit phase, and the finish phase. In the prepare phase, each node sends a message to the coordinator node asking it to prepare for the agreement. In the commit phase, the coordinator node sends a message to all the nodes asking them to agree on a single value. In the finish phase, the coordinator node sends a message to all the nodes confirming the agreement.

Mnemonics and Learning Tricks:
* Two-phase commit: “2PC”
* Three-phase commit: “3PC”
* Prepare phase: “Prepare”
* Commit phase: “Commit”
* Finish phase: “Finish”