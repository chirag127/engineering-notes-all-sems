### Beyond Chaincode for the notes of the Unit 5 - Hyperledger Fabric (B) in the subject of Block chain Architecture Design

In Hyperledger Fabric, chaincode is used to define the business logic of the network. However, there are other components that are important for the proper functioning of the network. In this section, we will discuss the components beyond chaincode that are necessary for a successful Hyperledger Fabric network.

#### 1. Fabric SDKs
Hyperledger Fabric provides several SDKs (Software Development Kits) that allow developers to interact with the network. These SDKs provide a set of APIs that can be used to query and update the ledger, invoke chaincode, and manage network resources. The SDKs are available in several programming languages including Go, Java, and Node.js. 

#### 2. Membership Services Provider (MSP)
The Membership Services Provider (MSP) is responsible for managing the identities of network participants. It issues certificates to network participants and verifies the authenticity of incoming requests. The MSP also defines the roles and permissions of network participants, ensuring that only authorized users can access the network resources.

#### 3. Ordering Service
The Ordering Service is responsible for ordering transactions and creating new blocks on the network. The Ordering Service receives transaction proposals from the clients, orders them according to a predefined consensus algorithm, and generates a new block that is added to the blockchain. Hyperledger Fabric supports several ordering service implementations, including Kafka and Solo.

#### 4. Peer Nodes
Peer Nodes maintain a copy of the ledger and validate transactions sent to the network. Peer Nodes are responsible for endorsing transactions, which involves verifying that the transaction meets the requirements of the chaincode. Peer Nodes also validate transactions sent to them by other nodes on the network. 

#### 5. Channels
Channels are used to partition the network into smaller sub-networks. Each channel has its own ledger and chaincode instances, and only the participants with access to the channel can interact with it. Channels can be used to create private sub-networks within the larger network, allowing for greater privacy and scalability.

#### 6. Fabric CA
The Fabric Certificate Authority (CA) is responsible for issuing and managing X.509 certificates for network participants. The Fabric CA can be used to create and revoke certificates, and can be integrated with external identity providers.

#### 7. Hyperledger Explorer
Hyperledger Explorer is a web-based tool that allows users to view and interact with the network. It provides real-time monitoring of the network, and allows users to view the transaction history, block history, and network topology.

#### 8. Chaincode Best Practices
There are several best practices that should be followed when writing chaincode for Hyperledger Fabric. These include writing efficient code, using appropriate data structures, and properly handling errors. It is also important to properly test and document the chaincode, and to follow established security protocols.

Overall, these components beyond chaincode are essential for the proper functioning of a Hyperledger Fabric network. Understanding these components is critical for developers and network administrators who want to create and maintain successful blockchain networks.