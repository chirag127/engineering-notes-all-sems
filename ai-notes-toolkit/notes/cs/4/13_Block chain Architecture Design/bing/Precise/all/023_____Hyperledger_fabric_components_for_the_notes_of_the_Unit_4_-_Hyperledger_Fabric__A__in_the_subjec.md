# Unit 4 - Hyperledger Fabric (A)

### Hyperledger Fabric Components

Hyperledger Fabric is a blockchain framework that runs smart contracts called chaincode. It is designed to be modular and extensible, allowing for the integration of various components. Some of the key components of Hyperledger Fabric include:

1. **Peer Nodes**: These are the nodes that maintain the ledger and run chaincode. They are responsible for validating transactions and updating the ledger.

2. **Ordering Service**: This is a component that orders transactions into blocks and delivers them to the peer nodes. It ensures that all peers receive the same transactions in the same order.

3. **Membership Service Provider (MSP)**: This component manages identity and access control. It is responsible for issuing and validating digital certificates, which are used to authenticate the identity of participants in the network.

4. **Chaincode**: This is the smart contract that runs on the peer nodes. It defines the business logic and rules for the transactions that are executed on the network.

5. **Channels**: These are private communication channels between specific members of the network. They allow for the creation of private ledgers that are only accessible to the members of the channel.

6. **Ledger**: This is the record of all transactions that have taken place on the network. It is maintained by the peer nodes and is updated with each new block of transactions.

These are some of the key components of Hyperledger Fabric. Each component plays a crucial role in the functioning of the network and allows for the creation of secure and efficient blockchain solutions.