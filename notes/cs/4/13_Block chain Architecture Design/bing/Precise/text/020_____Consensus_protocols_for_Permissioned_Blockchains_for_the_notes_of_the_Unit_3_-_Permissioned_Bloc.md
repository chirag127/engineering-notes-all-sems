### Consensus protocols for Permissioned Blockchains

1. **Practical Byzantine Fault Tolerance (PBFT)**: This protocol is designed to handle malicious attacks and system failures in a distributed network. It requires all nodes to communicate with each other to reach a consensus, making it more suitable for smaller networks.

2. **Raft**: This protocol is designed for easy understandability and implementation. It uses a leader-follower model, where the leader is responsible for managing the log replication process and the followers simply replicate the leader's log.

3. **Simplified Byzantine Fault Tolerance (SBFT)**: This protocol is a simplified version of PBFT, designed for improved performance and scalability. It uses a rotating leader model, where the leader is changed periodically to prevent any single node from dominating the decision-making process.

4. **Federated Byzantine Agreement (FBA)**: This protocol allows for more flexible trust models, where nodes can choose which other nodes to trust. It uses a quorum-based approach, where a subset of nodes must agree on a decision for it to be considered valid.

These are some of the consensus protocols used in permissioned blockchains. Each protocol has its own strengths and weaknesses, and the choice of protocol depends on the specific requirements of the blockchain network.