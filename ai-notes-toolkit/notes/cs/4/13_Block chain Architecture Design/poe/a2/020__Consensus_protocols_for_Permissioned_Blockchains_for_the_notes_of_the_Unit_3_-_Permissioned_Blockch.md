 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Consensus protocols for Permissioned Blockchains

1. Practical Byzantine Fault Tolerance (PBFT)
- PBFT is a popular consensus algorithm for permissioned blockchains.
- It is an asynchronous consensus algorithm that can tolerate Byzantine faults.
- It requires 3f+1 nodes to reach consensus where f is the maximum number of faulty nodes.
- The consensus is achieved in multiple phases - pre-prepare, prepare, commit.
- The leader node initiates the consensus by sending a pre-prepare message with the proposal. The other nodes validate and broadcast prepare messages. Once a quorum of prepare messages is received, the nodes broadcast commit messages.
- Once a quorum of commit messages is received, the block is finalized.

2. Proof of Authority (PoA)
- In PoA, consensus is achieved based on the identity of the nodes, not their computational resources.
- The validators are known, trusted entities like banks or financial institutions.
- The consensus algorithm is simpler than PoW or PoS as the validators are known and trusted. The blocks are proposed and voted upon by the validators.
- The main drawback is that the decentralization is limited as the validators are selected entities. The system is prone to centralization.

3. Delegated Proof of Stake (DPoS)
- In DPoS, the nodes elect representative nodes (witnesses) to validate transactions and produce blocks.
- The representatives are elected based on the stake (number of tokens) held by the electing nodes.
- The elected witnesses take turns to produce blocks in a fast and efficient manner.
- The high throughput and fast finality comes at the cost of lesser decentralization as the consensus power is given to a few elected witnesses.