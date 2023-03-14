### Beyond Chaincode for the notes of the Unit 5 - Hyperledger Fabric (B) in the subject of Block chain Architecture Design

Hyperledger Fabric is an open-source blockchain platform that enables the creation and management of decentralized applications. In the previous unit, we learned about Chaincode, which is the smart contract in Hyperledger Fabric. In this unit, we will go beyond Chaincode and explore other important concepts in Hyperledger Fabric.

#### 1. Channels
- A channel is a private communication mechanism between two or more participants in a Hyperledger Fabric network.
- Each channel has its own ledger, which contains a copy of the chaincode and the transaction history for that channel.
- Channels are useful when different groups within an organization need to interact with each other privately without involving the entire network.

#### 2. Orderer Service
- The orderer service is responsible for ordering transactions and creating blocks in the Hyperledger Fabric network.
- It ensures that all nodes in the network have a consistent view of the ledger.
- There can be multiple orderer nodes in a network to provide fault tolerance.

#### 3. Membership Service Provider (MSP)
- MSP manages the identities of participants in the Hyperledger Fabric network.
- It provides authentication and authorization for network access.
- Each participant has its own MSP, which is responsible for managing its identity.

#### 4. Fabric Node Types
- Peer Nodes: Peer nodes maintain a copy of the ledger and execute chaincode transactions.
- Endorsing Peer Nodes: Endorsing peer nodes execute chaincode and return a digital signature that is added to the transaction before it is sent to the orderer service.
- Client Nodes: Client nodes interact with the network by submitting transactions and querying the ledger.
- Certificate Authority Nodes (CA): CA nodes issue and manage digital certificates for network participants.

#### 5. Hyperledger Fabric SDK
- The Hyperledger Fabric SDK is a set of libraries that allows developers to interact with the Hyperledger Fabric network.
- It provides APIs for submitting transactions, querying the ledger, and managing identities.
- SDKs are available in several programming languages, including Java, Go, and Node.js.

#### 6. Mnemonic
- To remember the different node types in Hyperledger Fabric, you can use the mnemonic "PECC" which stands for Peer, Endorsing Peer, Client, and Certificate Authority.

#### 7. Learning Trick
- To understand the concept of channels, imagine a chat group on WhatsApp or any other messaging platform. Each chat group is like a channel in Hyperledger Fabric, where only the members of that group can communicate with each other privately.
- To remember the role of the orderer service, think of it as a referee in a sports match who ensures that all the players follow the rules and have a fair game.
- To understand the concept of MSP, imagine a bouncer at a club who checks the IDs of the participants before allowing them to enter.
- To remember the different SDKs available for Hyperledger Fabric, think of SDKs as tools in a toolkit that developers can use to build applications on the platform.