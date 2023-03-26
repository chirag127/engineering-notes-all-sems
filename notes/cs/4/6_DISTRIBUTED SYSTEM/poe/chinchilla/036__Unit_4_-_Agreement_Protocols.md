## Unit 4 - Agreement Protocols

Agreement protocols are essential in distributed systems to ensure that all nodes agree on a particular value or decision. In this unit, we will discuss various agreement protocols and their properties.

### 1. Consensus Problem

The consensus problem refers to the task of reaching an agreement among a group of nodes in a distributed system. The nodes must agree on a single value even when some of them may fail or be faulty.

### 2. Two-Phase Commit Protocol

The two-phase commit protocol is a widely used agreement protocol that ensures all nodes agree on a particular transaction. It involves two phases:

1. The prepare phase - in this phase, the coordinator asks all nodes to prepare for the transaction.
2. The commit phase - in this phase, the coordinator sends a commit message to all nodes, and they execute the transaction.

This protocol has the property of atomicity, which means that either all nodes commit or none of them do.

### 3. Paxos Protocol

The Paxos protocol is another agreement protocol that allows nodes to agree on a single value even in the presence of faulty nodes. It involves three phases:

1. The prepare phase - in this phase, a node sends a prepare message to all nodes.
2. The promise phase - in this phase, all nodes respond with a promise message, which includes the highest proposal they have seen.
3. The accept phase - in this phase, the node with the highest proposal sends an accept message to all nodes, which then commit to the value.

This protocol has the property of safety, which means that all nodes agree on the same value, and liveness, which means that the protocol eventually terminates.

### 4. Raft Protocol

The Raft protocol is a consensus algorithm that allows a group of nodes to agree on a single value. It involves electing a leader who is responsible for coordinating the agreement process. The protocol has the following phases:

1. Leader election - in this phase, nodes elect a leader.
2. Log replication - in this phase, the leader sends log entries to all nodes, which then replicate them.
3. Commitment - in this phase, nodes commit to the log entries they have replicated.

This protocol has the property of safety and liveness.

### Conclusion

Agreement protocols are essential in distributed systems to ensure that all nodes agree on a particular value or decision. The two-phase commit protocol, Paxos protocol, and Raft protocol are widely used agreement protocols that have different properties. Understanding these protocols is crucial for building reliable and fault-tolerant distributed systems.