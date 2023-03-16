### Consensus protocols for Permissioned Blockchains

Consensus protocols are a crucial component of blockchain technology, as they ensure that all nodes in the network agree on the state of the shared ledger. In permissioned blockchains, where the participants are known and trusted, consensus can be achieved through a variety of mechanisms. Here are some of the most commonly used consensus protocols for permissioned blockchains:

1. **Practical Byzantine Fault Tolerance (PBFT):** This protocol is designed to tolerate Byzantine faults, where nodes may behave maliciously or fail arbitrarily. It requires a supermajority of nodes to agree on the state of the ledger, and can tolerate up to one-third of nodes being faulty.

2. **Raft:** This protocol is designed for leader-based consensus, where a leader node is elected to propose new blocks to the network. The other nodes then vote on whether to accept the proposed block. Raft is designed to be easy to understand and implement, and provides strong consistency guarantees.

3. **Proof of Authority (PoA):** This protocol is based on the idea of trusted validators, who are responsible for validating transactions and creating new blocks. Validators are chosen based on their reputation and reliability, and the protocol is designed to be fast and efficient.

4. **Federated Byzantine Agreement (FBA):** This protocol is similar to PBFT, but allows for more flexible trust models. Nodes can choose which other nodes to trust, and the network can tolerate a higher proportion of faulty nodes.

These are just a few examples of the many consensus protocols that can be used in permissioned blockchains. The choice of protocol will depend on the specific requirements of the network, such as the level of trust between participants, the desired level of security, and the need for scalability.