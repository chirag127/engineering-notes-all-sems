Unit 5 - Hyperledger Fabric (B)
===============================

The following diagram illustrates the basic architecture of a Hyperledger Fabric network:

```
+------------------------------------------------------------------------+
|                                                                        |
|  +-----------------+  +-----------------+  +-----------------+         |
|  |                 |  |                 |  |                 |         |
|  |  Organization A |  |  Organization B |  |  Organization C |         |
|  |                 |  |                 |  |                 |         |
|  +-----------------+  +-----------------+  +-----------------+         |
|                                                                        |
|  +-----------------+  +-----------------+  +-----------------+         |
|  |                 |  |                 |  |                 |         |
|  |  Peer Node 1    |  |  Peer Node 2    |  |  Peer Node 3    |         |
|  |                 |  |                 |  |                 |         |
|  +-----------------+  +-----------------+  +-----------------+         |
|                                                                        |
|  +-----------------+  +-----------------+  +-----------------+         |
|  |                 |  |                 |  |                 |         |
|  |  Ledger         |  |  Ledger         |  |  Ledger         |         |
|  |                 |  |                 |  |                 |         |
|  +-----------------+  +-----------------+  +-----------------+         |
|                                                                        |
|  +-----------------+  +-----------------+  +-----------------+         |
|  |                 |  |                 |  |                 |         |
|  |  Chaincode      |  |  Chaincode      |  |  Chaincode      |         |
|  |                 |  |                 |  |                 |         |
|  +-----------------+  +-----------------+  +-----------------+         |
|                                                                        |
+------------------------------------------------------------------------+
|                                                                        |
|  +-----------------+  +-----------------+  +-----------------+         |
|  |                 |  |                 |  |                 |         |
|  |  Orderer Node 1 |  |  Orderer Node 2 |  |  Orderer Node 3 |         |
|  |                 |  |                 |  |                 |         |
|  +-----------------+  +-----------------+  +-----------------+         |
|                                                                        |
|  +-----------------+  +-----------------+  +-----------------+         |
|  |                 |  |                 |  |                 |         |
|  |  Ordering       |  |  Ordering       |  |  Ordering       |         |
|  |  Service        |  |  Service        |  |  Service        |         |
|  |                 |  |                 |  |                 |         |
|  +-----------------+  +-----------------+  +-----------------+         |
|                                                                        |
+------------------------------------------------------------------------+
|                                                                        |
|  +-----------------+                                                  |
|  |                 |                                                  |
|  |  Client         |                                                  |
|  |                 |                                                  |
|  +-----------------+                                                  |
|                                                                        |
|  +-----------------+                                                  |
|  |                 |                                                  |
|  |  Application    |                                                  |
|  |                 |                                                  |
|  +-----------------+                                                  |
|                                                                        |
+------------------------------------------------------------------------+
```

A Hyperledger Fabric network consists of the following components:

- Organizations: These are the entities that own and manage the peer nodes and participate in the network. Each organization has a unique identity and a membership service provider (MSP) that manages the certificates and cryptographic keys of its members.
- Peer nodes: These are the nodes that store the ledger and execute the chaincode. Each peer node belongs to one organization and has a copy of the ledger and the chaincode installed on it. Peer nodes can act as endorsers, committers, or both, depending on the endorsement policy of the chaincode.
- Ledger: This is the distributed database that records the transactions and the state of the network. The ledger consists of two parts: the world state and the blockchain. The world state is a key-value store that represents the current state of the assets and contracts on the network. The blockchain is a sequence of blocks that contain the history of all transactions that have been validated and committed on the network.
- Chaincode: This is the smart contract that defines the business logic and rules for the network. The chaincode is written in a programming language such as Go, Node.js, or Java, and is deployed on the peer nodes. The chaincode can