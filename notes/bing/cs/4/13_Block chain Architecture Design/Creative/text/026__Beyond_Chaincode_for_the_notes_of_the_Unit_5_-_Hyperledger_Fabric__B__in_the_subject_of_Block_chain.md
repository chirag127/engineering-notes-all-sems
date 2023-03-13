### Beyond Chaincode

- Chaincode is the term used for smart contracts in Hyperledger Fabric. It is a program that runs on the peers and interacts with the ledger.
- Chaincode can be written in various languages, such as Go, Node.js, or Java. It can implement any logic or functionality that the application requires.
- Chaincode can be invoked by clients through transactions, or by other chaincodes through chaincode-to-chaincode calls.
- Chaincode can access the ledger state through the stub interface, which provides methods for getting and setting key-value pairs, querying the ledger, and creating composite keys.
- Chaincode can also use the stub interface to emit events, which can be subscribed by external applications or other chaincodes.
- Chaincode can be installed and instantiated on the peers using the peer CLI or the SDK. It can also be upgraded to a new version when needed.
- Chaincode can be packaged and deployed using the chaincode lifecycle, which is a new feature introduced in Fabric v2.0. It allows more control and flexibility over the chaincode endorsement policy, the chaincode definition, and the chaincode approval process.
- Chaincode can be categorized into two types: user chaincode and system chaincode. User chaincode is the chaincode that implements the business logic of the application. System chaincode is the chaincode that provides system-level functions, such as the configuration of the channel or the endorsement policy. System chaincode is not visible to the users and cannot be invoked by them.