## Unit 4 - Hyperledger Fabric (A)

Hyperledger Fabric is a platform for distributed ledger solutions, underpinned by a modular architecture delivering high degrees of confidentiality, resiliency, flexibility and scalability. It is intended as a foundation for developing applications or solutions with a modular architecture. Hyperledger Fabric allows components, such as consensus and membership services, to be plug-and-play.

The following diagram illustrates the basic architecture of a Hyperledger Fabric network:

```
+-----------------------------------------------------------------+
|                                                                 |
|  +----------------+  +----------------+  +----------------+      |
|  |                |  |                |  |                |      |
|  |    Client      |  |    Client      |  |    Client      |      |
|  |                |  |                |  |                |      |
|  +----------------+  +----------------+  +----------------+      |
|                                                                 |
|  +----------------+  +----------------+  +----------------+      |
|  |                |  |                |  |                |      |
|  |    Peer        |  |    Peer        |  |    Peer        |      |
|  |                |  |                |  |                |      |
|  +----------------+  +----------------+  +----------------+      |
|                                                                 |
|  +----------------+  +----------------+  +----------------+      |
|  |                |  |                |  |                |      |
|  |    Orderer     |  |    Orderer     |  |    Orderer     |      |
|  |                |  |                |  |                |      |
|  +----------------+  +----------------+  +----------------+      |
|                                                                 |
+-----------------------------------------------------------------+
```

The main components of a Hyperledger Fabric network are:

- **Clients**: Clients are applications that act on behalf of a user to submit transactions to the network. They communicate with peers to endorse transactions and with orderers to broadcast transactions to the network.
- **Peers**: Peers are nodes that maintain the state and ledger of a channel. They execute chaincode, the logic that defines the transactions. Peers also endorse transactions and validate them before committing them to the ledger.
- **Orderers**: Orderers are nodes that order transactions into blocks and deliver them to peers. They implement a pluggable consensus mechanism that ensures consistency and finality of the ledger.
- **Channels**: Channels are logical partitions of the network that allow data isolation and confidentiality. A channel is defined by a set of peers that share the same ledger and chaincode. Transactions within a channel are only visible to the members of that channel.
- **Chaincode**: Chaincode is the term for the smart contracts that run on a Hyperledger Fabric network. Chaincode defines the business logic and rules for the transactions. Chaincode can be written in various languages, such as Go, Node.js, or Java.
- **Ledger**: Ledger is the term for the append-only record of all the transactions that have occurred in a channel. It consists of two parts: the world state, which is the current value of the state variables, and the blockchain, which is the immutable history of all the transactions.