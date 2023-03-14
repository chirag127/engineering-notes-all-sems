### Decomposing the consensus process for the notes of the Unit 4 - Hyperledger Fabric (A) in the subject of Block chain Architecture Design

- Consensus is the process that ensures all copies of a distributed ledger are the same and provides a guaranteed ordering of transactions and validation of blocks.
- Consensus in Hyperledger Fabric is achieved by relying on a backend service (known as the ordering service) that intermediates the messages between senders and receivers.
- Consensus in Hyperledger Fabric is pluggable, which means that it can be replaced with a different algorithm as needed.
- The most commonly used consensus algorithms in Hyperledger Fabric are:
  - Solo: A single ordering node that orders transactions and delivers blocks to peers. It is meant for development and testing purposes only.
  - Kafka: A crash fault-tolerant (CFT) ordering service that uses Apache Kafka and Zookeeper to order transactions and deliver blocks to peers. It is suitable for production environments with high throughput and scalability requirements.
  - Raft: A leader-based CFT ordering service that uses the Raft protocol to order transactions and deliver blocks to peers. It is an alternative to Kafka that offers more flexibility and control over the ordering service configuration.
- Consensus in Hyperledger Fabric can be decomposed into three phases:
  - Endorsement: The client application submits a transaction proposal to a set of endorsing peers that execute the chaincode (smart contract) and endorse the transaction by signing the result.
  - Ordering: The endorsed transactions are sent to the ordering service, which orders them into blocks and delivers them to the committing peers.
  - Validation: The committing peers validate the transactions according to the endorsement policy and the versioning of the ledger state, and append the blocks to the ledger.
- A mnemonic to remember the three phases of consensus in Hyperledger Fabric is **EOV** (Endorsement, Ordering, Validation).
- A diagram to illustrate the consensus process in Hyperledger Fabric is:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Endorsing      |       |  Ordering       |       |  Committing     |
|  Peers          |       |  Service        |       |  Peers          |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
      |  |  |                    |  |  |                    |  |  |
      |  |  |                    |  |  |                    |  |  |
      |  |  +--------------------+  |  +--------------------+  |  |
      |  |                          |                          |  |
      |  +--------------------------+--------------------------+  |
      |                                                           |
      +-----------------------------------------------------------+
                             |  |  |
                             |  |  |
                             |  |  |
+-----------------+          |  |  |          +-----------------+
|                 |          |  |  |          |                 |
|  Client         |----------+  |  +----------|  Ledger         |
|  Application    |             |             |                 |
|                 |             +-------------|                 |
+-----------------+                           +-----------------+
```

- Key points to remember about the consensus process in Hyperledger Fabric are:
  - Consensus is pluggable and can be configured according to the network requirements.
  - Consensus is decomposed into three phases: endorsement, ordering, and validation.
  - Consensus relies on the ordering service to order transactions and deliver blocks to peers.
  - Consensus depends on the chaincode and the endorsement policy to verify the correctness of transactions.