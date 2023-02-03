## Unit 4 - Hyperledger Fabric (A)

Hyperledger Fabric is a permissioned blockchain platform developed under the Hyperledger project by the Linux Foundation. It is used to build enterprise-grade blockchain applications and networks.

Unit 4 focuses on the architecture and components of Hyperledger Fabric. It covers topics such as:
- Network architecture
- Participants (Peers, Orderers, Clients)
- Chaincode (Smart Contracts)
- Ledger
- Consensus mechanism
- Security and privacy features

Hyperledger Fabric has a modular architecture, allowing for plug-and-play components and customization. It uses a permissioned network, meaning only authorized participants can join and access the network. The participants in a Hyperledger Fabric network are Peers, Orderers, and Clients. Peers maintain a copy of the ledger and execute transactions, Orderers order transactions into blocks, and Clients initiate transactions.

Chaincode, also known as smart contracts, define the business logic for the network. They are written in Go and stored on the network for execution. The ledger in Hyperledger Fabric is a distributed ledger that maintains a complete record of all transactions and states.

Hyperledger Fabric uses a consensus mechanism to ensure the integrity of the ledger and secure the network. It supports several consensus algorithms, including Practical Byzantine Fault Tolerance (PBFT) and Kafka-based consensus.

Hyperledger Fabric has built-in security and privacy features, such as access control, privacy of transactions, and confidentiality of chaincode. These features can be customized to meet the specific needs of the network.

In summary, Unit 4 of Hyperledger Fabric covers the architecture and components of the platform, including network architecture, participants, chaincode, ledger, consensus mechanism, and security and privacy features.
