### Beyond Chaincode

- Chaincode is a fabric-specific script that implements the application logic of a smart contract on Hyperledger Fabric  .
- Chaincode runs in a secured Docker container isolated from the endorsing peer process .
- Chaincode initializes and manages ledger state through transactions submitted by applications .
- Chaincode can be written in Go, node.js, Java, or EVM bytecode .
- Chaincode has a lifecycle that requires organizations to agree on its parameters, such as name, version, and endorsement policy.
- Chaincode can be installed and instantiated through an SDK or CLI onto a network of Hyperledger Fabric peer nodes, enabling interaction with that network’s shared ledger .
- Chaincode can be upgraded, redefined, or removed from the network by following the chaincode lifecycle process.
- Chaincode can be invoked by applications or other chaincodes through the peer nodes.
- Chaincode can access the ledger state, the transaction context, and the channel configuration.
- Chaincode can emit events that can be consumed by applications or other chaincodes.