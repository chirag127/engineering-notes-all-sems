# Decomposing the consensus process for the notes of the Unit 4 - Hyperledger Fabric (A) in the subject of Block chain Architecture Design

- Consensus is a process where the nodes in the network provide a guaranteed ordering of the transactions and validate those blocks of transactions that need to be committed to the ledger.
- Consensus must ensure the following in the network:
  - Agreement: All the nodes must agree on the same order and content of the transactions.
  - Validity: Only valid transactions must be included in the ledger, and invalid transactions must be rejected.
  - Integrity: No node should be able to tamper with the transactions or the ledger.
  - Finality: Once a transaction is committed to the ledger, it cannot be reversed or modified.
- Consensus in Hyperledger Fabric is broken out into three phases: Endorsement, Ordering, and Validation .
  - Endorsement: This phase is driven by a policy (m out of n signatures) upon which participants endorse a transaction. The endorsing peers execute the transaction and sign the result, which is called a proposal response. The client collects the proposal responses from different peers and sends them to the ordering service as a transaction .
  - Ordering: This phase is responsible for establishing a total order of transactions and batching them into blocks. The ordering service receives the transactions from the clients and agrees on the order to be committed to the ledger. The ordering service can use different algorithms, such as Solo (for development) or Kafka (for production), to reach consensus among the ordering nodes .
  - Validation: This phase is performed by the committing peers, which receive the ordered blocks from the ordering service and validate them according to the endorsement policy and other system chaincodes. The committing peers check that the transactions have been endorsed by the required number of peers, that there are no read-write conflicts, and that the version of the state is consistent. The valid transactions are then committed to the ledger, and the invalid transactions are marked as such .