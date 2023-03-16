### Chaincode Design and Implementation for the notes of the Unit 4 - Hyperledger Fabric (A) in the subject of Block chain Architecture Design

- Chaincode is a program, written in Go, node.js , or Java that implements a prescribed interface.
- Chaincode runs in a secured Docker container isolated from the endorsing peer process.
- Chaincode initializes and manages ledger state through transactions submitted by applications.
- Chaincode can also query the ledger state, invoke other chaincodes, or communicate with external data sources.
- Chaincode is also known as smart contracts, as they define the rules for interacting with the data stored on a blockchain.
- Chaincode can be deployed on a channel, which is a private subnet of communication between two or more network members.
- Chaincode can be installed, instantiated, upgraded, and invoked by the network members using the Hyperledger Fabric API.
- Chaincode can be written using the fabric-contract-api, which provides a high level API for application developers to implement smart contracts.
- Chaincode can also use the fabric-shim-api, which provides a lower level API for accessing the ledger, the transaction context, and the chaincode stub.
- Chaincode can be packaged, signed, and approved by the network members before being committed to the channel ledger.
- Chaincode can be versioned and have different endorsement policies for different functions.
- Chaincode can be tested using various tools, such as the chaincode-dev-mode, the fabric-samples, and the fabric-test.