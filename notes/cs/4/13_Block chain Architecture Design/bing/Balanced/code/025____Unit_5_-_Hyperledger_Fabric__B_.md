## Unit 5 - Hyperledger Fabric (B)

Hyperledger Fabric is an open source blockchain framework and a de facto standard for enterprise blockchain platforms. It is intended as a foundation for developing applications or solutions with a modular architecture that uses plug-and-play components. Some of the features and benefits of Hyperledger Fabric are:

- It supports **permissioned networks**, where participants are known and authorized by a membership service provider (MSP).
- It allows for **privacy and confidentiality** of transactions and data, using channels, private data collections, and encryption mechanisms.
- It enables **scalability and performance**, by allowing parallel execution and validation of transactions, and by using a pluggable consensus mechanism that can be tailored to different network requirements.
- It offers **flexibility and extensibility**, by allowing developers to choose the programming languages, data formats, and smart contract models that suit their needs, and by providing a rich set of APIs and SDKs for integration and interoperability.
- It supports **governance and compliance**, by providing a policy-based framework for managing the network configuration, access control, and endorsement policies.

Hyperledger Fabric is composed of several core components, such as:

- **Peer nodes**, which host the ledger and smart contracts, and execute and validate transactions.
- **Ordering nodes**, which form the ordering service that batches and orders transactions into blocks, and broadcasts them to the peer nodes.
- **Certificate authority**, which issues and manages the digital certificates and identities of the network participants.
- **Channel**, which is a private communication channel between a subset of network members, where transactions and data are isolated and confidential.
- **Chaincode**, which is the term for smart contracts in Hyperledger Fabric, and which defines the business logic and rules for the network.
- **Ledger**, which is a distributed and immutable record of all the transactions and state changes that have occurred on the network.
- **World state**, which is a database that stores the current state of the ledger, and which can be queried by the chaincode or the applications.

Hyperledger Fabric 2.0 is the latest version of the framework, which was released in January 2020. It introduces several new features and improvements, such as:

- **Decentralized governance for smart contracts**, which allows multiple organizations to agree on the parameters and lifecycle of a chaincode, without requiring a central authority or intermediary.
- **External chaincode launcher**, which enables the use of external builders and launchers to run the chaincode, and which supports a wider range of programming languages and frameworks.
- **Private data enhancements**, which improve the performance, security, and usability of private data collections, and which allow for implicit collections and organization-specific endorsement policies.
- **New chaincode lifecycle**, which simplifies the process of installing, approving, and committing a chaincode, and which provides more control and visibility over the chaincode dependencies and upgradeability.
- **Alpine-based docker images**, which reduce the size and vulnerability of the docker images used by Hyperledger Fabric, and which enhance the portability and compatibility of the framework.

Hyperledger Fabric is a powerful and versatile blockchain framework that can be used to create enterprise-grade applications and solutions for various industries and use cases, such as finance, banking, healthcare, supply chain, manufacturing, and technology. It is one of the most widely used and supported projects under the Hyperledger umbrella, and it has a vibrant and active community of developers and contributors.