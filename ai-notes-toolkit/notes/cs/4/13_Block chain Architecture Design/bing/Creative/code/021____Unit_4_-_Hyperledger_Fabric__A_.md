# Unit 4 - Hyperledger Fabric (A)

Hyperledger Fabric is an open source project from the Linux Foundation that provides a modular blockchain framework and a de facto standard for enterprise blockchain platforms  . It is intended as a foundation for developing applications or solutions with a plug-and-play architecture that allows components, such as consensus and membership services, to be interchangeable . It is designed to satisfy a broad range of industry use cases, such as finance, banking, healthcare, IoT, supply chain, manufacturing and technology .

Some of the key features of Hyperledger Fabric are:

- **Permissioned network**: Hyperledger Fabric requires all participants to have an identity that is issued and managed by a trusted authority. This ensures that the network is secure, transparent and accountable  .
- **Channels**: Hyperledger Fabric allows the creation of private subnets of communication between two or more network members, enabling the isolation and confidentiality of transactions and data  .
- **Smart contracts**: Hyperledger Fabric supports the execution of business logic in the form of smart contracts, which are also known as chaincode. Chaincode can be written in various programming languages, such as Go, Java, Node.js and TypeScript  .
- **Endorsement policy**: Hyperledger Fabric defines the endorsement policy as the set of rules that specify which network members must endorse a transaction before it can be committed to the ledger. The endorsement policy can be customized for different chaincodes and channels, depending on the business requirements  .
- **Ordering service**: Hyperledger Fabric uses an ordering service to ensure the consistency and finality of transactions across the network. The ordering service can be implemented using different consensus algorithms, such as Raft, Kafka or Solo  .
- **CouchDB**: Hyperledger Fabric supports the use of CouchDB as a state database that stores the current values of the ledger assets. CouchDB enables rich queries and complex data models for chaincode applications .

Hyperledger Fabric has released its latest version, 2.0, in January 2020, which introduces several improvements and new features, such as:

- **Decentralized governance for smart contracts**: Hyperledger Fabric 2.0 allows the network members to agree on the parameters and lifecycle of the chaincode, such as the version, the endorsement policy and the upgrade process. This eliminates the need for a central authority to manage the chaincode and enhances the autonomy and flexibility of the network.
- **External chaincode launcher**: Hyperledger Fabric 2.0 enables the use of an external chaincode launcher that can run the chaincode in a separate container or process from the peer. This improves the security and performance of the chaincode execution and allows the use of any programming language that supports the gRPC protocol.
- **Private data enhancements**: Hyperledger Fabric 2.0 introduces new features for private data management, such as implicit collections, private data reconciliation and purge, and hashed indexes. These features enable the network members to share and synchronize private data more efficiently and securely.
- **New chaincode application patterns**: Hyperledger Fabric 2.0 supports new chaincode application patterns, such as state-based endorsement, chaincode-to-chaincode invocation and token management. These patterns enable the network members to implement more complex and diverse business scenarios using the chaincode.

Hyperledger Fabric is a powerful and versatile blockchain framework that can be used to create enterprise-grade applications and solutions that are secure, scalable and customizable. It is one of the most widely used and adopted blockchain platforms in the industry and has a vibrant and active community of developers and contributors .