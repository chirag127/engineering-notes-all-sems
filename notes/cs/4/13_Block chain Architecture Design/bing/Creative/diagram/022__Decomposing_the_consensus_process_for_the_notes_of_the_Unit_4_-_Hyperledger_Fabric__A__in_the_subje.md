The consensus process in Hyperledger Fabric is the mechanism that ensures all copies of the distributed ledger are the same and that the transactions are valid according to the endorsement policies and the chaincode logic. The consensus process can be decomposed into three phases: endorsement, ordering, and validation.

The following diagram illustrates the basic architecture of a Hyperledger Fabric network and the steps involved in the consensus process:

```
+-----------------+  +-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |  |                 |
|    Client       |  |    Peer E0      |  |    Peer E1      |  |    Peer E2      |
|                 |  |                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+  +-----------------+
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |------------------->|                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |------------------->|                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |------------------->|
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |<-------------------|                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |<-------------------|                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |<-------------------|                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |-------------------------------------------------------------------->|
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |<--------------------------------------------------------------------|
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       v                    v                    v                    v
+-----------------+  +-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |  |                 |
|    Ordering     |  |    Peer P0      |  |    Peer P1      |  |    Peer P2      |
|    Service      |  |                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+  +-----------------+
```

The steps are as follows:

1. The client application submits a transaction proposal to the endorsers (