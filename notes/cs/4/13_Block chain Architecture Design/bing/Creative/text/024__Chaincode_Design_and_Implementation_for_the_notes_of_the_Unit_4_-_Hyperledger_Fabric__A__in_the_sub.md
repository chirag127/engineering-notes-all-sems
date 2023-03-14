### Chaincode Design and Implementation

- Chaincode is a program that implements a prescribed interface and runs in a secured Docker container isolated from the endorsing peer process.
- Chaincode initializes and manages ledger state through transactions submitted by applications.
- Chaincode can be written in Go, Node.js, or Java .
- Chaincode can be invoked to update or query the ledger in a proposal transaction.
- Chaincode can also invoke another chaincode, either in the same channel or in different channels, to access its state.
- Chaincode typically handles business logic agreed to by members of the network, so it is similar to a "smart contract".
- Chaincode can be developed using the Fabric Contract API, which provides a high level API for application developers.
- Chaincode can be deployed to a running network using the Fabric chaincode lifecycle, which involves installing, approving, committing, and initializing the chaincode.
- Chaincode can be tested using the Fabric test network, which provides a sample network configuration and chaincode application.