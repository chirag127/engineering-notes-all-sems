# Decomposing the consensus process for the notes of the Unit 4 - Hyperledger Fabric (A) in the subject of Block chain Architecture Design

- Consensus is a process where the nodes in the network provide a guaranteed ordering of the transactions and validate those blocks of transactions that need to be committed to the ledger.
- Consensus must ensure the following in the network:
  - Agreement: All the nodes must agree on the same order and content of the transactions.
  - Validity: Only valid transactions are included in the ledger, and invalid transactions are rejected.
  - Integrity: No node can tamper with or forge transactions or blocks.
  - Finality: Once a transaction is committed to the ledger, it cannot be reversed or changed.
- Consensus in Hyperledger Fabric is broken out into three phases: Endorsement, Ordering, and Validation  .
  - Endorsement: This phase is driven by a policy (m out of n signatures) upon which participants endorse a transaction. The policy defines which nodes must sign the transaction for it to be valid. The endorsing nodes execute the transaction and produce a read-write set, which contains the current and proposed values of the ledger state. The endorsing nodes also sign the read-write set and send it back to the client.
  - Ordering: This phase is where the endorsed transactions are collected by an ordering service, which is a set of nodes that agree on the order of the transactions. The ordering service uses a consensus algorithm (such as Solo or Kafka) to ensure that all the nodes receive the same order of transactions. The ordering service then batches the transactions into blocks and delivers them to the committing nodes.
  - Validation: This phase is where the committing nodes validate the transactions and the blocks before appending them to the ledger. The committing nodes check that the transactions have been endorsed by the required nodes, and that the read-write sets do not conflict with each other or with the current state of the ledger. The committing nodes also mark the transactions as valid or invalid, and update the ledger accordingly.