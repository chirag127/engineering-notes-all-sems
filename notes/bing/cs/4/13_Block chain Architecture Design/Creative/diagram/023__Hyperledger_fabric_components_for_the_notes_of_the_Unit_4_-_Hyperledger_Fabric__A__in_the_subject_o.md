The following is a detailed ASCII diagram for Hyperledger Fabric components for the notes of the Unit 4 - Hyperledger Fabric (A) in the subject of Block chain Architecture Design.

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Client 1     |     |    Client 2     |     |    Client 3     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+---------------------------------------------------------------+
|                                                               |
|                        Channel 1                              |
|                                                               |
+---------------------------------------------------------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Peer 1       |     |    Peer 2       |     |    Peer 3       |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+---------------------------------------------------------------+
|                                                               |
|                        Channel 2                              |
|                                                               |
+---------------------------------------------------------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Peer 4       |     |    Peer 5       |     |    Peer 6       |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+---------------------------------------------------------------+
|                                                               |
|                        Ordering Service                       |
|                                                               |
+---------------------------------------------------------------+
```

The diagram illustrates the basic architecture of a Hyperledger Fabric network, which consists of the following components:

- **Assets**: Anything that has value and has state and ownership. Assets are represented as key-value pairs in the ledger.
- **Shared ledger**: The ledger records the state and ownership of assets. The ledger consists of two components: the world state and the transaction log. The world state is a database that describes the current state of the ledger, and the transaction log is a record of all the transactions that have occurred in the network.
- **Smart contract**: Hyperledger Fabric smart contracts are called chaincode. They are programs that define the business logic and rules for modifying the state of assets. Chaincode is executed by peers and endorsed by a subset of peers according to the endorsement policy.
- **Peer nodes**: Peers are the fundamental elements of the network because they host ledgers and smart contracts. Peers can have different roles, such as endorser, committer, anchor, or leader. Peers can also belong to different organizations and channels.
- **Channel**: A channel is a private communication mechanism that allows a subset of network participants to share a ledger and execute transactions. A channel is defined by a configuration block that specifies the policies, members, and chaincode that are allowed on the channel.
- **Organization**: An organization is a logical grouping of network participants that have a common authority and interest. Organizations can have different levels of trust and permissions in the network. Organizations are represented by a Membership Services Provider (MSP).
- **Membership Services Provider (MSP)**: An MSP is a component that defines the identity, roles, and permissions of network participants. An MSP can use different mechanisms to issue and validate certificates, such as a Certificate Authority