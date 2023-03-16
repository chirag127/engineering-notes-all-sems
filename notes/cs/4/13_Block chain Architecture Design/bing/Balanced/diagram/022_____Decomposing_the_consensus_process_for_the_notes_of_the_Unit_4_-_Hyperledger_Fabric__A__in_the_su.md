### Decomposing the consensus process for the notes of the Unit 4 - Hyperledger Fabric (A) in the subject of Block chain Architecture Design

- Consensus is a process where the nodes in the network provide a guaranteed ordering of the transactions and validate those blocks of transactions that need to be committed to the ledger.
- Consensus must ensure the following in the network:
  - Agreement: All the nodes must agree on the same order of transactions and the same state of the ledger.
  - Validity: Only valid transactions must be added to the ledger, and invalid transactions must be rejected.
  - Integrity: No node should be able to tamper with the transactions or the ledger.
  - Finality: Once a transaction is committed to the ledger, it cannot be reversed or changed.
- Consensus in Hyperledger Fabric is broken out into three phases: Endorsement, Ordering, and Validation  .
  - Endorsement: This phase is driven by a policy (m out of n signatures) upon which participants endorse a transaction. The endorsing peers execute the transaction and produce a signed proposal that contains the transaction output and a read/write set. The client collects the endorsements and submits them to the ordering service.
  - Ordering: This phase is responsible for collecting the endorsed transactions and agreeing on the order to be committed to the ledger. The ordering service can use different consensus algorithms, such as Solo (for development) or Kafka (for production). The ordering service creates blocks of transactions and delivers them to the committing peers.
  - Validation: This phase is where the committing peers validate the transactions and ensure that they satisfy the endorsement policy and do not have any conflicts. The committing peers also update their ledger state and mark the transactions as valid or invalid. Only valid transactions are added to the ledger, and invalid transactions are marked as such.