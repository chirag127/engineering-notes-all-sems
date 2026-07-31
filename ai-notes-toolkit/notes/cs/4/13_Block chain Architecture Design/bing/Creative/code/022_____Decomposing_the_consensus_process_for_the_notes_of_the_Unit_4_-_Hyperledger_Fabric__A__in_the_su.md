### Decomposing the consensus process for the notes of the Unit 4 - Hyperledger Fabric (A) in the subject of Block chain Architecture Design

- Consensus in Hyperledger Fabric is a process where the nodes in the network provide a guaranteed ordering of the transactions and validate those blocks of transactions that need to be committed to the ledger.
- Consensus in Hyperledger Fabric must ensure the following properties in the network:
  - Agreement: All honest nodes must agree on the same set of transactions and their order.
  - Validity: Only valid transactions that satisfy the endorsement policy and other rules must be committed to the ledger.
  - Integrity: No node can tamper with or forge a transaction or a block.
  - Finality: Once a transaction is committed to the ledger, it cannot be reversed or changed.
- Consensus in Hyperledger Fabric is broken out into three phases: Endorsement, Ordering, and Validation .
  - Endorsement: This phase is driven by the endorsement policy, which specifies how many and which participants must endorse a transaction. An endorsing peer executes a transaction proposal and signs the result, which is called an endorsement. The client collects the endorsements and submits them to the ordering service.
  - Ordering: This phase is performed by the ordering service, which is a set of nodes that agree on the order of transactions and create blocks. The ordering service can use different consensus algorithms, such as Solo, Kafka, or Raft, depending on the network configuration and requirements. The ordering service delivers the blocks to all the peers in the network.
  - Validation: This phase is performed by the committing peers, which validate the transactions and the endorsements in each block. The committing peers check that the transactions satisfy the endorsement policy, the versioning policy, and the read-write set policy. The committing peers also mark any invalid transactions as such and do not update the ledger state with them. The committing peers append the validated block to the ledger.