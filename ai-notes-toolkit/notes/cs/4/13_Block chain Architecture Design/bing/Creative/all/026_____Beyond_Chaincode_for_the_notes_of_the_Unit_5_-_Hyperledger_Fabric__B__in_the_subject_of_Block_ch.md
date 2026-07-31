# Beyond Chaincode

- Chaincode is a fabric-specific script written to perform operations within the framework.
- Chaincode enables a user with no knowledge of blockchain technology to build and deploy smart contracts and transactions.
- Chaincode runs in a secured Docker container isolated from the endorsing peer process .
- Chaincode initializes and manages ledger state through transactions submitted by applications .
- Chaincode can be written in Go, node.js, or Java.
- Chaincode can be installed and instantiated through an SDK or CLI onto a network of Hyperledger Fabric peer nodes, enabling interaction with that network’s shared ledger.
- Chaincode can be plug-and-play, allowing components, such as consensus and membership services, to be customized.
- Chaincode has a lifecycle that requires organizations to agree on the parameters that define a chaincode, such as name, version, and the chaincode endorsement policy.
- Chaincode can be upgraded, redefined, or deleted by following the chaincode lifecycle steps.
- Chaincode can be executed using Intel SGX for Hyperledger Fabric, which provides confidentiality and privacy for the application state and the users.