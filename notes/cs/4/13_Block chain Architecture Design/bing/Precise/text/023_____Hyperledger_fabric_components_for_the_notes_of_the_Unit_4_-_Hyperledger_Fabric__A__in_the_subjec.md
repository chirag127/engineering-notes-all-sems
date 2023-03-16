### Unit 4 - Hyperledger Fabric (A) - Hyperledger Fabric Components

Hyperledger Fabric is a permissioned blockchain platform designed for use in enterprise contexts. It is one of the Hyperledger projects hosted by the Linux Foundation. Some of the key components of Hyperledger Fabric include:

1. **Peer Nodes**: These are the nodes that maintain the ledger and validate transactions. They can be divided into two types: endorsing peers and committing peers. Endorsing peers simulate and endorse transactions, while committing peers validate and commit transactions to the ledger.

2. **Ordering Service**: This is responsible for ordering transactions and creating blocks. It is a cluster of ordering nodes that use a consensus mechanism to agree on the order of transactions.

3. **Membership Service Provider (MSP)**: This is responsible for managing identities and access control. It issues and validates digital certificates, which are used to authenticate the identity of participants in the network.

4. **Chaincode**: This is the smart contract layer of Hyperledger Fabric. Chaincode is written in a general-purpose programming language such as Go or Node.js and is used to define the business logic of the blockchain.

5. **Channels**: These are private communication paths between specific members of the network. Channels allow for the creation of private ledgers that are only accessible to the members of the channel.

6. **Ledger**: This is the record of all transactions and state changes that have occurred on the blockchain. The ledger is maintained by the peer nodes and is composed of two parts: the world state and the blockchain.

These are some of the key components of Hyperledger Fabric. Each component plays a crucial role in the functioning of the blockchain network.