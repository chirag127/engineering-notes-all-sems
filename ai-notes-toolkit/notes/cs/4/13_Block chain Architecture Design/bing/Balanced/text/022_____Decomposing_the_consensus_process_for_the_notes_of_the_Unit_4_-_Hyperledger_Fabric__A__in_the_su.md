### Decomposing the consensus process for the notes of the Unit 4 - Hyperledger Fabric (A) in the subject of Block chain Architecture Design

- Consensus is a process where the nodes in the network provide a guaranteed ordering of the transactions and validate those blocks of transactions that need to be committed to the ledger.
- Consensus must ensure the following in the network:
  - Agreement on the order and results of transactions
  - Fault tolerance and finality
  - Network performance and scalability
  - Network security and privacy
- Consensus in Hyperledger Fabric is broken out into three phases: Endorsement, Ordering, and Validation .
- Endorsement is driven by policy (m out of n signatures) upon which participants endorse a transaction.
- Ordering phase will get the endorsed transaction and agrees to the order to be committed to the ledger.
- Validation phase will check the endorsement policy and read-write sets for conflicts before committing the transaction to the ledger.
- Hyperledger Fabric follows a modular approach wherein different consensus techniques can be plugged in as per the requirement.
- Currently, Hyperledger Fabric uses Solo and Kafka to reach consensus, which requires a node to validate a batch of transactions and add them as a new block to the blockchain.
- Solo is a single node ordering service that is used for development and testing purposes.
- Kafka is a distributed messaging system that provides a crash fault tolerant and scalable ordering service for production environments.
- Hyperledger Fabric is intended as a foundation for developing applications or solutions with a modular architecture.
- Hyperledger Fabric allows components, such as consensus and membership services, to be plug-and-play.
- Its modular and versatile design satisfies a broad range of industry use cases.