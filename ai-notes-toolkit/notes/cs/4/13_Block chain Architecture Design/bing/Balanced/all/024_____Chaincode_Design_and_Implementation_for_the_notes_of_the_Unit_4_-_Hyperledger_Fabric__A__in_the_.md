# Chaincode Design and Implementation for the notes of the Unit 4 - Hyperledger Fabric (A) in the subject of Block chain Architecture Design

- Chaincode is a program that implements a prescribed interface and runs in a secured Docker container isolated from the endorsing peer process.
- Chaincode is also known as smart contracts, and it defines the rules for interacting with the data stored on a blockchain, such as reading and writing data to the ledger, verifying the identity of users, and enforcing access controls.
- Chaincode can be written in Go, node.js, or Java, and it can use the fabric-contract-api, a high level API for application developers to implement smart contracts.
- Chaincode can be deployed on a Hyperledger Fabric network through a chaincode lifecycle, which consists of the following steps:
  - Packaging: The chaincode source code and metadata are packaged into a tar file that can be installed on peers.
  - Installing: The chaincode package is installed on the peers that will endorse the chaincode transactions.
  - Approving: The organizations that are part of the channel approve the chaincode definition, which specifies the name, version, endorsement policy, and other parameters of the chaincode.
  - Committing: The chaincode definition is committed to the channel, which makes it available for invocation by applications.
  - Invoking: The chaincode is invoked by applications through the endorsing peers, which execute the chaincode logic and produce a proposal. The proposal is then sent to the ordering service, which creates a block and delivers it to the committing peers. The committing peers validate the transactions and update the ledger state accordingly.
- Chaincode can be updated or upgraded by following a similar chaincode lifecycle, with some differences depending on the type of change:
  - Updating: The chaincode definition can be updated with minor changes, such as changing the endorsement policy or the collection configuration. This requires a new approval and commit process, but does not require a new chaincode package or version.
  - Upgrading: The chaincode source code can be upgraded with major changes, such as adding new functions or fixing bugs. This requires a new chaincode package and version, as well as a new approval and commit process. The old and new versions of the chaincode can coexist on the channel until the new version is ready to be invoked.