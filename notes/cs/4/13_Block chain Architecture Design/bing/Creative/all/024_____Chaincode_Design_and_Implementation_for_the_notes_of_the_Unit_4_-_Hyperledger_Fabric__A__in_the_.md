# Chaincode Design and Implementation for the notes of the Unit 4 - Hyperledger Fabric (A) in the subject of Block chain Architecture Design

- Chaincode is a program, written in Go, node.js , or Java that implements a prescribed interface.
- Chaincode runs in a secured Docker container isolated from the endorsing peer process.
- Chaincode initializes and manages ledger state through transactions submitted by applications.
- Chaincode can also query the ledger, invoke other chaincodes, or communicate with external data sources.
- Chaincode is also known as smart contracts, as they define the rules for interacting with the data stored on a blockchain.
- Chaincode can be developed, installed, instantiated, and upgraded using the Hyperledger Fabric API.
- Chaincode can be deployed on a channel, which is a private subnet of communication between two or more network members.
- Chaincode can be accessed by applications through the Fabric SDKs, which provide a high-level interface to invoke and query chaincode transactions.
- Chaincode can be written using the fabric-contract-api, which provides a contract interface and a high-level API for application developers.
- Chaincode can be tested using the fabric-chaincode-shim, which provides a mock stub and a testing framework for chaincode.