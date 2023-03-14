## Unit 2 - Consensus

Consensus is a fundamental concept in distributed systems, where a group of nodes needs to agree on a common decision or state. It is essential to ensure that all nodes in a distributed system are consistent and operate on the same data.

### Paxos Algorithm

Paxos is a consensus algorithm that ensures fault-tolerance in a distributed system. It allows a group of nodes to agree on a single value, even if some nodes fail or send incorrect information. 

Steps in Paxos Algorithm -

1. Proposal Phase - A proposer suggests a value and sends a prepare request to a majority of acceptors.
2. Promise Phase - Acceptors respond to the prepare request with a promise not to accept any proposal with a lower proposal number.
3. Accept Phase - If the proposer receives promises from a majority of acceptors, it sends an accept request to them with the proposed value.
4. Learn Phase - If the acceptors accept the proposal, they send an acceptance message to all nodes in the system, and the proposed value becomes the consensus value.

### Raft Algorithm

Raft is another consensus algorithm that is designed to be more understandable and easier to implement than Paxos. It divides the nodes in a distributed system into three roles -

1. Leader - responsible for managing the consistency of the system and accepting client requests.
2. Follower - passively replicates the leader's log and responds to client requests.
3. Candidate - tries to become the leader by requesting votes from other nodes.

Steps in Raft Algorithm -

1. Leader Election - A candidate requests votes from a majority of nodes in the system to become the leader.
2. Log Replication - The leader appends new entries to its log and sends them to the followers for replication.
3. Commitment - Once a majority of nodes have replicated the log entry, it is committed, and the leader notifies the followers.
4. Safety - Raft ensures that once a log entry is committed, it is never overwritten or lost.

### Mnemonics and Learning Tricks

To remember the steps in Paxos Algorithm, you can use the following mnemonic - 
PAPA LEAP - Prepare, Accept, Promise, Accept, Learn.

To remember the roles in Raft Algorithm, you can use the following mnemonic - 
LFC - Leader, Follower, Candidate.

In conclusion, consensus is a crucial concept in distributed systems, and Paxos and Raft algorithms are two popular ways to achieve it. By understanding these algorithms' steps and roles, one can design robust and fault-tolerant distributed systems.