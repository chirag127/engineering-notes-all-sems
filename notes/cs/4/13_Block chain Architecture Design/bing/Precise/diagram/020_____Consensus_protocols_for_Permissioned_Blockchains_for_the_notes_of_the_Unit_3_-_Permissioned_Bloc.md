### Consensus protocols for Permissioned Blockchains

Consensus protocols are a crucial component of blockchain technology, as they ensure that all nodes in the network agree on the state of the shared ledger. In permissioned blockchains, where the participants are known and trusted, consensus can be achieved through a variety of mechanisms. Some of the most commonly used consensus protocols for permissioned blockchains include:

1. **Practical Byzantine Fault Tolerance (PBFT):** This protocol is designed to tolerate Byzantine faults, where nodes may behave maliciously or fail arbitrarily. In PBFT, a designated leader node proposes a new block, and the other nodes in the network must agree on the validity of the block before it is added to the chain.

2. **Raft:** Raft is a leader-based consensus protocol that is designed to be easy to understand and implement. In Raft, a leader node is elected, and this node is responsible for proposing new blocks and coordinating the agreement of the other nodes in the network.

3. **Proof of Authority (PoA):** In PoA, a set of pre-approved nodes, known as validators, are responsible for validating transactions and creating new blocks. This protocol is often used in private or consortium blockchains, where the validators are known and trusted entities.

4. **Federated Byzantine Agreement (FBA):** FBA is a generalization of PBFT that allows for more flexible trust models. In FBA, each node can choose which other nodes it trusts, and consensus is achieved through a process of voting and agreement among these trusted nodes.

These are just a few examples of the many consensus protocols that can be used in permissioned blockchains. The choice of protocol will depend on the specific requirements of the network, such as the level of trust among participants, the desired level of decentralization, and the need for fault tolerance.