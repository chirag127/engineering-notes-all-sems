### Decomposing the consensus process for the notes of the Unit 4 - Hyperledger Fabric (A) in the subject of Block chain Architecture Design

- Consensus is a mechanism that ensures all copies of a distributed ledger are the same and that the transactions are valid and ordered .
- Hyperledger Fabric achieves consensus by relying on a backend service (known as the ordering service) that intermediates the messages between senders and receivers.
- The ordering service is responsible for delivering a consistent stream of transactions to all the peers in the network.
- The ordering service can use different algorithms to achieve consensus, such as Solo, Kafka, or Raft.
- Solo is a single node ordering service that is suitable for development and testing purposes.
- Kafka is a crash fault tolerant (CFT) ordering service that uses Apache Kafka and Zookeeper to handle high throughput and scalability.
- Raft is a leader-based ordering service that uses the Raft protocol to elect a leader and handle failures.
- The consensus process in Hyperledger Fabric can be decomposed into three phases: endorsement, ordering, and validation .
- Endorsement is the process of executing a transaction proposal and obtaining signatures from a subset of peers (known as endorsers) that agree on the result .
- Endorsement policies define the set of endorsers and the number of signatures required for a transaction to be valid .
- Ordering is the process of batching transactions into blocks and delivering them to all the peers in the network in a consistent order .
- Ordering policies define the algorithm and the parameters used by the ordering service to achieve consensus .
- Validation is the process of checking the endorsement and ordering policies and the read-write sets of transactions to ensure that they are consistent and have not been tampered with .
- Validation policies define the rules for accepting or rejecting transactions based on their validity .
- Transactions that pass the validation phase are committed to the ledger and updated in the state database .
- Transactions that fail the validation phase are marked as invalid and recorded in the ledger, but not updated in the state database .

A possible mnemonic to remember the three phases of consensus in Hyperledger Fabric is **EOV** (Endorsement, Ordering, Validation).

A possible ascii diagram to illustrate the consensus process in Hyperledger Fabric is:

```
    Client
      |
      | 1. Send transaction proposal
      v
    Endorsers
      |
      | 2. Execute transaction and return endorsement
      v
    Client
      |
      | 3. Send endorsed transaction to ordering service
      v
    Ordering service
      |
      | 4. Order transactions and create blocks
      v
    Peers
      |
      | 5. Validate transactions and commit to ledger
      v
    Ledger
```