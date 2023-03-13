## Unit 5 - Hyperledger Fabric (B)

Hyperledger Fabric is a permissioned blockchain framework that runs on a modular architecture. It allows components, such as consensus and membership services, to be plug-and-play. It also leverages container technology to host smart contracts (chaincode) that contain the application logic.

The following diagram illustrates the basic architecture of a Hyperledger Fabric network:

```
+------------------------------------------------------------------------+
|                                                                        |
|  +-----------------+  +-----------------+  +-----------------+         |
|  |                 |  |                 |  |                 |         |
|  |  Orderer Node   |  |  Orderer Node   |  |  Orderer Node   |         |
|  |                 |  |                 |  |                 |         |
|  +-----------------+  +-----------------+  +-----------------+         |
|                                                                        |
|  +------------------------------------------------------------------+  |
|  |                                                                  |  |
|  |  Ordering Service: Provides consensus and broadcasts blocks to   |  |
|  |  the peers. It can use different algorithms, such as Solo, Kafka |  |
|  |  or Raft.                                                       |  |
|  |                                                                  |  |
|  +------------------------------------------------------------------+  |
|                                                                        |
+------------------------------------------------------------------------+
|                                                                        |
|  +-----------------+  +-----------------+  +-----------------+         |
|  |                 |  |                 |  |                 |         |
|  |  Peer Node      |  |  Peer Node      |  |  Peer Node      |         |
|  |                 |  |                 |  |                 |         |
|  +-----------------+  +-----------------+  +-----------------+         |
|                                                                        |
|  +------------------------------------------------------------------+  |
|  |                                                                  |  |
|  |  Peer Nodes: Maintain the ledger and state, and execute the      |  |
|  |  chaincode. They can have different roles, such as endorser,     |  |
|  |  committer or anchor. They belong to different organizations     |  |
|  |  that form a channel.                                            |  |
|  |                                                                  |  |
|  +------------------------------------------------------------------+  |
|                                                                        |
+------------------------------------------------------------------------+
|                                                                        |
|  +-----------------+  +-----------------+  +-----------------+         |
|  |                 |  |                 |  |                 |         |
|  |  Client App     |  |  Client App     |  |  Client App     |         |
|  |                 |  |                 |  |                 |         |
|  +-----------------+  +-----------------+  +-----------------+         |
|                                                                        |
|  +------------------------------------------------------------------+  |
|  |                                                                  |  |
|  |  Client Applications: Interact with the peer nodes to submit     |  |
|  |  transactions or query the ledger. They use SDKs to communicate  |  |
|  |  with the network.                                              |  |
|  |                                                                  |  |
|  +------------------------------------------------------------------+  |
|                                                                        |
+------------------------------------------------------------------------+
```