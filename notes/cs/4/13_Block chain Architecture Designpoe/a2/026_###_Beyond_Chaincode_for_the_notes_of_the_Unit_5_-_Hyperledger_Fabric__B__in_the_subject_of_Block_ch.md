 Here is the content in markdown format for the topic -

### Beyond Chaincode for the notes of the Unit 5 - Hyperledger Fabric (B) in the subject of Block chain Architecture Design

Chaincode is the code that queries and updates the ledger state through transactions in Hyperledger Fabric. Beyond chaincode, there are a few other components in the Hyperledger Fabric architecture -

- Peers - Peers are the nodes in the network that store the ledger, endorse transactions and maintain the blockchain.
- Ordering service - The ordering service orders transactions into blocks and delivers them to peers. It provides two modes - solo and Kafka.
- Membership services - Membership services are used for peer and MSP (Membership Service Provider) management. They are pluggable components that define organization boundaries and node identities.
- Certificate authority (CA) - The CA is responsible for identity management and issues enrollment certificates to members.
- Ledger - The ledger stores the network state as a series of blockchain blocks. State database and world state are two components of the ledger.
- CouchDB - CouchDB is the default state database for the ledger. It stores the current state data of channels.
- Configuration - The configuration file contains configuration parameters for channels, organizations, peers, orderers, etc.

Some tips to learn -

- Understand the architecture components and their functions clearly. This will help in understanding how transaction flow and consensus occur in Hyperledger Fabric.
- Try hands-on experiments with the components to get a deeper understanding of the concepts.
- Go through the specifications and standards like protobuf to understand the messaging format.
- Read blogs and watch videos to stay up-to-date with the developments in Hyperledger Fabric.

The Hyperledger Fabric architecture is designed well for enterprise blockchains. Knowing the components beyond chaincode will help in understanding the system thoroughly and building robust applications.