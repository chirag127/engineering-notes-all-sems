 Here is the content in markdown format for ## Unit 4 - Hyperledger Fabric (A):

## Unit 4 - Hyperledger Fabric (A)

Hyperledger Fabric is a blockchain framework implementation and one of the Hyperledger projects hosted by The Linux Foundation.

### Key points to learn:

1. Hyperledger Fabric has a modular architecture with distinct components that can be plugged and played. The major components are:
- Ledger: The ledger is a permanent and tamper-resistant record of all transactions.
- Consensus: The consensus component handles the process of reaching agreement on the validity and order of transactions.
- Membership services: The membership services component manages the network participants and their roles.
- Chaincode: Chaincode defines and executes the transactions that modify the ledger state.
- APIs and CLIs: The APIs and CLIs enable applications and developers to interact with the Hyperledger Fabric blockchain.

2. Hyperledger Fabric uses a permissioned blockchain network, where the identities of all entities are known and cryptographically verified. This enables confidential transactions, where only authorized participants can view the details of a transaction.
3. The ordering service provides ordering and consistency guarantees for block creation across the peer nodes. It manages the sequence of ordering requests from multiple channels and deliver blocks to peers for validation and commitment.
4. Channels are central concepts in Hyperledger Fabric that enable confidential transactions. A channel is a private ???subnet??? of communication between a subset of consortium members. Only peers that are members of a specific channel can transact and access the channel's shared ledger.
5. Smart contracts in Hyperledger Fabric are called chaincode and are written in Go, Node.js, or Java. Chaincode executes transaction proposals on peer nodes, query ledger data, and endorse transactions. Chaincode is separated from the consensus mechanics to enable decoupling application logic from the core system.

[Further details, diagrams, examples, advantages, disadvantages, and applications can be added here if required.]