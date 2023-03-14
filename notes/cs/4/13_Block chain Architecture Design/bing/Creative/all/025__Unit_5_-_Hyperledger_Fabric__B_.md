## Unit 5 - Hyperledger Fabric (B)

Hyperledger Fabric is an open source project from the Linux Foundation that provides a modular blockchain framework for developing enterprise-grade applications and solutions. It is one of the most widely used and mature blockchain platforms in the industry. It offers a unique approach to consensus that enables performance at scale while preserving privacy. It also supports smart contracts written in various programming languages and executed in Docker containers.

Some of the key features and concepts of Hyperledger Fabric are:

- **Channels**: Channels are private subnets of communication between two or more network members, allowing for data isolation and confidentiality. A channel is defined by a set of peers, a channel configuration, and a shared ledger. Channels are useful for scenarios where not all participants need to see or access the same information.

- **Organizations**: Organizations are logical entities that represent network members, such as companies, institutions, or individuals. Each organization has a unique identity and a set of cryptographic credentials issued by a trusted certificate authority. Organizations can join or leave channels, endorse transactions, and host peers and orderers.

- **Peers**: Peers are the nodes that maintain the state and ledger of a channel. They can have different roles and capabilities, such as endorsing, committing, or querying transactions. Peers can belong to one or more channels and can communicate with other peers on the same channel.

- **Orderers**: Orderers are the nodes that ensure the consistency and finality of transactions across the network. They receive transactions from peers, sort them into blocks, and deliver them to the peers of a channel. Orderers can use different consensus mechanisms, such as Solo, Kafka, or Raft.

- **Chaincode**: Chaincode is the term for smart contracts in Hyperledger Fabric. It is the business logic that defines the rules and operations for interacting with the ledger. Chaincode can be written in various programming languages, such as Go, Node.js, or Java. Chaincode runs in a separate process from the peer, in a Docker container, and can be invoked by applications through the peer.

- **Ledger**: Ledger is the term for the shared, immutable record of transactions in Hyperledger Fabric. It consists of two components: the world state and the transaction log. The world state is a database that captures the current values of the assets and parameters on the network. The transaction log is a sequential record of all the transactions that have occurred on the network. The ledger is cryptographically hashed and linked using Merkle trees.

- **MSP**: MSP stands for Membership Service Provider, which is a component that defines the rules and policies for the identity, authentication, and authorization of network members. MSPs allow for the abstraction and interoperability of different identity protocols, such as X.509 certificates or Identity Mixer. MSPs can be local (for peers and orderers) or channel-wide (for organizations and channels).

- **Endorsement policy**: Endorsement policy is a set of rules that specify which peers must endorse (execute and sign) a transaction before it can be submitted to the orderer and committed to the ledger. Endorsement policies can be defined at the chaincode level, the channel level, or the individual transaction level. Endorsement policies are useful for implementing different trust and verification models, such as requiring a majority or a subset of peers to endorse a transaction.

- **Private data**: Private data is a feature that allows for the sharing of confidential or sensitive information among a subset of network members, without exposing it to the rest of the channel. Private data is stored in a private database (called a sideDB) on the peers of the authorized members, and is hashed and referenced in the public ledger. Private data can be accessed and modified by chaincode, and can be subject to endorsement policies.

- **CouchDB**: CouchDB is an optional state database that can be used to store the world state of a channel. CouchDB is a document-oriented database that allows for rich and complex queries of the ledger data, such as range queries, pagination, or composite keys. CouchDB is useful for applications that need to perform analytics or reporting on the ledger data.