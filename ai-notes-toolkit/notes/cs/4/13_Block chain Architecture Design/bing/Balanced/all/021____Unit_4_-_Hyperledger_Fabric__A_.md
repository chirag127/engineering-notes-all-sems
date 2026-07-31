# Unit 4 - Hyperledger Fabric (A)

Hyperledger Fabric is a modular blockchain framework that acts as a foundation for developing blockchain-based products, solutions, and applications using plug-and-play components that are aimed for use within private enterprises.

Some of the features and benefits of Hyperledger Fabric are:

- It is open source and hosted by the Linux Foundation .
- It supports smart contracts written in various programming languages, such as Go, Java, and Node.js .
- It allows for flexible and customizable consensus mechanisms, such as Raft, Kafka, and Solo .
- It enables fine-grained access control and data privacy through channels, private data collections, and encryption .
- It supports interoperability and integration with other blockchain platforms and legacy systems .
- It is scalable and high-performing, with low latency and high throughput .

Hyperledger Fabric is composed of several components, such as:

- Peers: The nodes that execute and validate transactions, store the ledger, and run smart contracts .
- Orderers: The nodes that order and batch transactions into blocks, and broadcast them to the peers .
- Clients: The applications that interact with the peers and orderers, and invoke or query smart contracts .
- Certificate Authorities: The entities that issue and manage digital certificates for identity and membership services .
- Channels: The logical partitions of the network that allow for data isolation and confidentiality among different organizations .
- Chaincode: The term used for smart contracts in Hyperledger Fabric, which contain the business logic and rules for the transactions .

Hyperledger Fabric has released several versions since its inception, with the latest being version 2.3.2 as of March 2021. Some of the improvements and enhancements in version 2.x include:

- Decentralized governance for smart contracts, which allows multiple organizations to agree on the parameters and lifecycle of the chaincode.
- State-based endorsement policies, which enable more granular control over the endorsement requirements for different keys or values in the ledger.
- Private data enhancements, such as implicit collections, hashed indexes, and purge support, which improve the security and efficiency of private data management.
- Raft-based ordering service, which provides a crash fault tolerant and leader-based consensus mechanism that is easier to set up and maintain.
- External chaincode launcher, which allows for the use of external builders and launchers for chaincode execution, and supports the use of Docker or Kubernetes as the chaincode runtime.

Hyperledger Fabric is a powerful and versatile blockchain framework that can be used for various industry use cases, such as finance, banking, healthcare, IoT, supply chain, manufacturing, and technology  . It is one of the most widely adopted and mature enterprise blockchain platforms in the market  .