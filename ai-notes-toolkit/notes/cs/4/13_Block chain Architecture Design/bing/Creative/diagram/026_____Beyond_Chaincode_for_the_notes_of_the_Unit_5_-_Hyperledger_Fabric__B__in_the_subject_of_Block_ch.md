### Beyond Chaincode

- Chaincode is a fabric-specific script that implements the application logic of a smart contract on Hyperledger Fabric  .
- Chaincode runs in a secured Docker container isolated from the endorsing peer process and interacts with the ledger state through transactions submitted by applications .
- Chaincode can be written in Go, node.js, or Java and has a prescribed interface that defines the functions of init, invoke, and query.
- Chaincode lifecycle is the process of agreeing on the parameters that define a chaincode, such as name, version, and endorsement policy, among the channel members.
- Chaincode lifecycle consists of four steps: packaging, installing, approving, and committing the chaincode on the channel.
- Chaincode can be upgraded or removed from the channel by following a similar process as the initial deployment.
- Hyperledger Fabric Private Chaincode (FPC) is an extension of Hyperledger Fabric that enables the execution of chaincode using Intel SGX, a hardware-based trusted execution environment.
- FPC aims to provide confidentiality and privacy for the chaincode logic and state, as well as the transactions and queries, by encrypting and attesting the data and code.
- FPC supports the same chaincode interface and lifecycle as Hyperledger Fabric, but requires some additional components, such as an enclave registry and an enclave endorsement validation component.