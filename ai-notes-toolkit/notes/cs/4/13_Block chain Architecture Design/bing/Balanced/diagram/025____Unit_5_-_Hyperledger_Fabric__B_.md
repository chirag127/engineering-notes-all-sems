## Unit 5 - Hyperledger Fabric (B)

- In this unit, we will learn about the following topics related to Hyperledger Fabric:

  - The architecture and components of a Hyperledger Fabric network
  - The process of creating and joining a Hyperledger Fabric channel
  - The role and functions of chaincode in Hyperledger Fabric
  - The lifecycle and endorsement policies of chaincode in Hyperledger Fabric
  - The types and features of Hyperledger Fabric transactions
  - The structure and content of Hyperledger Fabric blocks
  - The mechanisms and tools for querying and updating the ledger state in Hyperledger Fabric

- Hyperledger Fabric is a permissioned, modular, and extensible blockchain platform that supports smart contracts, or chaincode, written in various programming languages.

- Hyperledger Fabric network consists of the following components:

  - Peers: Nodes that host and execute chaincode, store ledger data, and validate transactions. Peers can have different roles, such as endorsing peers, committing peers, or ordering service nodes.
  - Orderers: Nodes that order and batch transactions into blocks and deliver them to the peers. Orderers can use different consensus algorithms, such as Solo, Kafka, or Raft.
  - Clients: Applications or SDKs that interact with the network by invoking chaincode, submitting transactions, or querying the ledger state. Clients can use different programming languages, such as Node.js, Java, or Go.
  - Certificate Authorities: Services that issue and manage digital certificates for the network participants. Certificate authorities can use different protocols, such as Fabric CA or MSP.
  - Channels: Logical partitions of the network that allow for data and transaction isolation and privacy. Channels are created by a subset of network members and joined by peers that want to participate in the channel.
  - Chaincode: Smart contracts that define the business logic and rules for the network. Chaincode can be written in different programming languages, such as Go, Node.js, or Java. Chaincode can be installed, instantiated, upgraded, or invoked by the network members.
  - Ledger: A distributed and immutable record of all the transactions and states in the network. The ledger consists of two parts: the world state and the transaction log. The world state is a key-value database that stores the current state of the assets and contracts in the network. The transaction log is a hash-linked list of blocks that contains the history of all the transactions and changes in the network.
  - Transactions: Requests or proposals that invoke chaincode functions and update the ledger state. Transactions are submitted by clients, endorsed by peers, ordered by orderers, and committed by peers. Transactions can have different types, such as invoke, query, or config.
  - Blocks: Containers that store a batch of ordered and validated transactions. Blocks are linked by hashes to form a blockchain. Blocks have a header, a data section, and a metadata section. Blocks can be queried or inspected by the network members.