### Decomposing the consensus process for the notes of the Unit 4 - Hyperledger Fabric (A) in the subject of Block chain Architecture Design

- Consensus in Hyperledger Fabric is a process where the nodes in the network provide a guaranteed ordering of the transactions and validate those blocks of transactions that need to be committed to the ledger.
- Consensus in Hyperledger Fabric must ensure the following properties in the network:
  - Agreement: All honest nodes must agree on the same set of transactions and their order.
  - Validity: Only valid transactions that satisfy the endorsement policy and other rules must be committed to the ledger.
  - Integrity: No node can tamper with or forge transactions or blocks.
  - Finality: Once a transaction is committed to the ledger, it cannot be reversed or modified.
- Consensus in Hyperledger Fabric is broken out into three phases: Endorsement, Ordering, and Validation .
  - Endorsement: This phase is driven by policy (m out of n signatures) upon which participants endorse a transaction. An endorsing peer executes a chaincode (smart contract) and signs the input and output of the transaction. The client collects the endorsements and submits the transaction proposal to the ordering service.
  - Ordering: This phase will get the endorsed transaction proposals and agrees on the order to be committed to the ledger. The ordering service is a cluster of nodes that use a consensus algorithm (such as Solo or Kafka) to reach agreement on the order of transactions. The ordering service creates blocks of transactions and delivers them to the committing peers.
  - Validation: This phase will validate the transactions in a block and decide whether to commit or reject them. A committing peer checks the endorsement policy, the read-write set, and the versioning of the ledger state. If the transaction is valid, it is committed to the ledger and the state is updated. If the transaction is invalid, it is marked as such and not applied to the ledger.