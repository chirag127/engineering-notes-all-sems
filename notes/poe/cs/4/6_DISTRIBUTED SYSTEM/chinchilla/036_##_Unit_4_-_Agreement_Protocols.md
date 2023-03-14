## Unit 4 - Agreement Protocols

Agreement protocols refer to the processes and procedures used to reach a consensus or agreement between multiple participants in a distributed system. These protocols are crucial in ensuring the correct functioning of distributed systems, where multiple nodes need to work together to reach a common goal. In this unit, we will discuss the various types of agreement protocols and their applications.

### Types of Agreement Protocols
1. **Two-phase Commit Protocol (2PC)** - This protocol is used to ensure that all participants in a distributed transaction either commit or abort the transaction together. The protocol involves two phases - the prepare phase and the commit phase. During the prepare phase, all participants are asked to prepare for the transaction. If all participants are ready, then the commit phase is initiated, and all participants commit to the transaction. If any participant is not ready, the transaction is aborted.

2. **Three-phase Commit Protocol (3PC)** - This protocol is an extension of the 2PC protocol and is used to ensure that distributed transactions are committed or aborted even in the presence of failures. The protocol involves three phases - the can-commit phase, the pre-commit phase, and the commit phase. During the can-commit phase, all participants are asked if they can commit to the transaction. If all participants can commit, then the pre-commit phase is initiated, where participants prepare for the transaction. If all participants are ready, then the commit phase is initiated, and all participants commit to the transaction. If any participant fails during any of the phases, the transaction is aborted.

3. **Paxos Protocol** - This protocol is used to ensure that a distributed system reaches a consensus on a value even in the presence of failures. The protocol involves multiple rounds of voting, where each participant proposes a value and tries to get a majority of votes. The protocol is designed to ensure that at least one participant always has the correct value, even if some participants fail.

4. **Raft Protocol** - This protocol is a consensus algorithm used to ensure that a distributed system reaches a consensus on a value. The protocol involves electing a leader who is responsible for managing the consensus process. The leader replicates its state to all other nodes in the system, and all decisions are made by the leader. If the leader fails, a new leader is elected.

### Applications of Agreement Protocols
Agreement protocols are used in various distributed systems, such as:
- Distributed databases
- Multiplayer online games
- Blockchain networks
- Cloud computing systems
- Distributed file systems

### Advantages of Agreement Protocols
- Ensures that all participants in a distributed system reach a consensus or agreement.
- Improves the fault tolerance of the system.
- Increases the reliability of the system.

### Disadvantages of Agreement Protocols
- Can be complex to implement and maintain.
- Can lead to increased latency due to the need for coordination between participants.
- Can be vulnerable to attacks, such as Byzantine faults.

Mnemonics and Learning Tricks:
- To remember the phases of the Two-phase Commit Protocol, you can use the acronym PREPARE-COMMIT.
- To remember the phases of the Three-phase Commit Protocol, you can use the acronym CAN-PRE-COMMIT.