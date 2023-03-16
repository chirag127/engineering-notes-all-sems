# Consensus protocols for Permissioned Blockchains

Consensus protocols are a crucial component of blockchain technology, as they ensure that all participants in the network agree on the state of the shared ledger. In permissioned blockchains, where the participants are known and trusted, consensus can be achieved through a variety of mechanisms. Here are some common consensus protocols used in permissioned blockchains:

1. **Practical Byzantine Fault Tolerance (PBFT):** This protocol is designed to tolerate Byzantine faults, where nodes may behave maliciously or fail arbitrarily. In PBFT, a designated leader node proposes a new block, and the other nodes in the network validate and vote on the proposal. If a supermajority of nodes agree, the block is added to the chain.

2. **Raft:** Raft is a leader-based consensus protocol that is designed to be easy to understand and implement. In Raft, a leader node is elected, and it is responsible for managing the log replication process and ensuring that the logs on all nodes are consistent.

3. **Proof of Authority (PoA):** In PoA, a set of pre-approved validator nodes are responsible for validating transactions and creating new blocks. This protocol is often used in private blockchain networks, where the validators are known and trusted entities.

4. **Federated Byzantine Agreement (FBA):** FBA is a generalization of PBFT that allows for more flexible trust models. In FBA, each node chooses a set of other nodes that it trusts, and consensus is achieved when a sufficient number of nodes in each trust set agree on the same value.

These are just a few examples of the many consensus protocols that can be used in permissioned blockchains. The choice of protocol will depend on the specific requirements of the network, such as the level of trust between participants, the desired level of decentralization, and the need for fault tolerance.