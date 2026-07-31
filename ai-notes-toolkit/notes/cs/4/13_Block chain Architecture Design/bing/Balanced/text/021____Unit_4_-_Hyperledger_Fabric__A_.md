## Unit 4 - Hyperledger Fabric (A)

- Hyperledger Fabric is an open source project from the Linux Foundation that provides a modular blockchain framework and a de facto standard for enterprise blockchain platforms  .
- Hyperledger Fabric is intended as a foundation for developing applications or solutions with a modular architecture that allows components, such as consensus and membership services, to be plug-and-play .
- Hyperledger Fabric is designed to support various industry use cases, such as finance, banking, healthcare, IoT, supply chain, manufacturing and technology .
- Hyperledger Fabric delivers a uniquely elastic and extensible architecture, distinguishing it from alternative blockchain solutions .
- Hyperledger Fabric supports smart contracts written in general-purpose programming languages, such as Java, Go and Node.js .
- Hyperledger Fabric enables a network of participants to agree on a shared ledger of transactions, while preserving privacy, confidentiality and scalability  .
- Hyperledger Fabric is composed of several core components, such as:
  - Peer nodes: responsible for endorsing and validating transactions, maintaining the ledger state and running chaincode (smart contracts) .
  - Orderer nodes: responsible for ordering transactions into blocks and broadcasting them to peer nodes .
  - Certificate authority: responsible for issuing and managing digital certificates for identity and access control .
  - Channel: a private communication channel that allows a subset of network participants to share a ledger and execute transactions .
  - Chaincode: the business logic that defines the rules and operations for a specific asset or function on the ledger .
- Hyperledger Fabric 2.0 is the latest version of the framework, released in January 2020, that introduces several new features and improvements, such as:
  - Decentralized chaincode lifecycle: allows network participants to agree on the parameters and policies for deploying and upgrading chaincode, without requiring a central authority.
  - State-based endorsement: allows chaincode to specify different endorsement policies for different states or keys on the ledger, enabling more flexibility and efficiency.
  - Private data collections: allows network participants to store and share sensitive data in a private and secure way, without revealing it to the entire network.
  - Raft-based ordering service: allows network participants to use a crash fault tolerant consensus algorithm that is easier to set up and maintain than the previous Kafka-based one.
  - External chaincode launcher: allows network participants to use external builders and launchers to run chaincode, enabling more control and customization.