## Unit 5 - Hyperledger Fabric (B)

- Hyperledger Fabric is a permissioned, modular, and extensible blockchain platform that supports smart contracts and various consensus mechanisms.
- Hyperledger Fabric has a layered architecture that separates the transaction processing from the transaction ordering and validation.
- Hyperledger Fabric has four main components: peers, orderers, channels, and chaincodes.
- Peers are the nodes that execute and validate transactions, store the ledger and the state, and communicate with other peers and clients.
- Orderers are the nodes that order transactions into blocks and broadcast them to the peers in a channel.
- Channels are the private communication channels that allow a subset of peers to share a ledger and execute transactions without exposing them to the rest of the network.
- Chaincodes are the smart contracts that define the business logic and the rules for modifying the state of the ledger.
- Hyperledger Fabric supports two types of chaincodes: system chaincodes and user chaincodes.
- System chaincodes are pre-installed and provide core functions such as configuration, lifecycle management, and endorsement policies.
- User chaincodes are custom chaincodes that implement the specific logic of a business application.
- Hyperledger Fabric uses a pluggable endorsement policy to specify the conditions for validating a transaction. An endorsement policy defines which peers need to endorse a transaction and how many endorsements are required.
- Hyperledger Fabric also uses a pluggable consensus mechanism to ensure the consistency and finality of the ledger. A consensus mechanism defines how the orderers reach an agreement on the order of transactions and how the peers validate the blocks.
- Hyperledger Fabric supports several consensus mechanisms, such as Solo, Kafka, and Raft.
- Solo is a simple consensus mechanism that uses a single orderer node. It is suitable for development and testing purposes, but not for production environments.
- Kafka is a consensus mechanism that uses a cluster of orderers that communicate with a Kafka service. It provides high throughput and scalability, but not fault tolerance or Byzantine fault tolerance.
- Raft is a consensus mechanism that uses a cluster of orderers that follow the Raft protocol. It provides fault tolerance, Byzantine fault tolerance, and dynamic reconfiguration of the orderer cluster.