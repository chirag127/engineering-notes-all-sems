### Decomposing the consensus process for the notes of the Unit 4 - Hyperledger Fabric (A) in the subject of Block chain Architecture Design

1. Consensus in the context of blockchain technology refers to the process of achieving agreement among the network participants on the order and content of transactions.
2. In Hyperledger Fabric, the consensus process is decomposed into three phases: Endorsement, Ordering, and Validation.
3. During the Endorsement phase, transactions are proposed by clients and then endorsed by a specified number of peers according to the endorsement policy.
4. In the Ordering phase, the endorsed transactions are collected into blocks and the order of the blocks is established by the ordering service.
5. During the Validation phase, the blocks are delivered to the peers, which validate the transactions according to the endorsement policy and the current state of the ledger.
6. This decomposition of the consensus process allows for greater flexibility and scalability in the design of the blockchain network.
7. It also enables the use of different consensus algorithms for the different phases, allowing for the use of more efficient and performant algorithms for each phase.
8. This approach to consensus is one of the key features of Hyperledger Fabric that sets it apart from other blockchain platforms.
