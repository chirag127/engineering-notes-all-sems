Consensus protocols for permissioned blockchains are algorithms that ensure that all the nodes in a network agree on the validity and order of transactions. Permissioned blockchains are networks where only authorized nodes can participate and access the data. Permissioned blockchains may use different consensus protocols depending on the level of trust, scalability, and performance required. Some of the common consensus protocols for permissioned blockchains are:

- **Practical Byzantine Fault Tolerance (PBFT)**: This protocol is based on the Byzantine Generals' Problem, which is a scenario where a group of generals have to coordinate an attack or retreat, but some of them may be traitors who send false messages. PBFT assumes that there is a fixed number of nodes in the network, and each node has a unique identity. The protocol works by electing a leader node that proposes a block of transactions, and then the other nodes vote on whether to accept or reject the block. The block is accepted if more than two-thirds of the nodes agree. PBFT can tolerate up to one-third of faulty nodes, but it requires a lot of communication and computation, which limits its scalability and performance.

- **Raft**: This protocol is a simplified version of PBFT, where the leader node is chosen randomly and periodically. The leader node is responsible for appending new blocks to the ledger and replicating them to the other nodes. The other nodes act as followers, who accept the leader's blocks and send acknowledgments. If the leader node fails or becomes unresponsive, the followers can elect a new leader. Raft can tolerate up to one-half of faulty nodes, but it assumes that the network is reliable and synchronous, which may not be realistic in some scenarios.

- **Proof of Authority (PoA)**: This protocol is based on the idea of reputation, where the nodes that validate transactions are selected based on their identity and credibility. The validators are usually known and trusted entities, such as organizations or individuals, who stake their reputation on the network. The validators take turns to create and sign new blocks, and the other nodes accept the blocks as long as they are signed by a majority of validators. PoA can achieve high scalability and performance, but it sacrifices some degree of decentralization and security, as the validators may collude or be compromised.

- **Proof of Elapsed Time (PoET)**: This protocol is based on the idea of randomness, where the nodes that create new blocks are chosen based on a lottery system. The nodes use a trusted execution environment (TEE), such as Intel SGX, to generate a random wait time and prove that they have waited for that time. The node with the shortest wait time wins the lottery and gets to create the next block. The other nodes verify the proof and accept the block. PoET can achieve high scalability and performance, but it relies on the security and availability of the TEE, which may not be guaranteed in some cases.

The following diagram illustrates the basic architecture of a permissioned blockchain using a consensus protocol:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|    Node 1      |     |    Node 2      |     |    Node 3      |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Consensus     |     |  Consensus     |     |  Consensus     |
|  Protocol      |     |  Protocol      |     |  Protocol      |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Ledger        |     |  Ledger        |     |  Ledger        |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       +---------------------+---------------------+
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |