### Chaincode Design and Implementation for the notes of the Unit 4 - Hyperledger Fabric (A) in the subject of Block chain Architecture Design

- Chaincode is a program that implements a prescribed interface and runs in a secured Docker container isolated from the endorsing peer process.
- Chaincode initializes and manages ledger state through transactions submitted by applications.
- Chaincode can be written in Go, node.js, or Java.
- Chaincode can be considered as a "smart contract" that handles business logic agreed to by members of the network.
- Chaincode can access its own state and invoke other chaincodes to access their states, given the appropriate permissions.
- There are two types of chaincodes in Hyperledger Fabric: system chaincodes and application chaincodes.
- System chaincodes are predefined chaincodes that provide essential functions such as configuration, lifecycle management, and endorsement policies.
- System chaincodes are usually written in a programming language based on Javascript (e.g., Nodejs) and run in a container as an isolated process.
- Application chaincodes are custom chaincodes that implement the specific logic and rules for a given use case or scenario.
- Application chaincodes can be written using one of the available SDKs for systems programming languages such as C++, Go, Rust, and Python.
- Application chaincodes can be deployed on one or more channels, depending on the visibility and privacy requirements.
- To design and implement a chaincode, the following steps are required :
  - Define the data model and the state variables for the chaincode.
  - Define the functions and the parameters for the chaincode.
  - Implement the functions using the chosen programming language and the SDK.
  - Test the chaincode locally using a mock stub or a development network.
  - Package the chaincode and its dependencies into a tar file.
  - Install the chaincode on the endorsing peers using the peer CLI or the SDK.
  - Approve the chaincode definition for the channel using the peer CLI or the SDK.
  - Commit the chaincode definition to the channel using the peer CLI or the SDK.
  - Invoke the chaincode functions using the peer CLI, the SDK, or the REST API.

- A possible mnemonic to remember the steps for chaincode design and implementation is: **D**efine, **I**mplement, **T**est, **P**ackage, **I**nstall, **A**pprove, **C**ommit, **I**nvoke, or **DITPIACI**.