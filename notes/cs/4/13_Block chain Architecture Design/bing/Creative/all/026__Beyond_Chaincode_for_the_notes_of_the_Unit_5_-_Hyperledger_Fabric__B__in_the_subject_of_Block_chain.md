### Beyond Chaincode for the notes of the Unit 5 - Hyperledger Fabric (B) in the subject of Block chain Architecture Design

- Chaincode is a program, written in Go, Node.js, or Java that implements a prescribed interface.
- Chaincode runs in a secured Docker container isolated from the endorsing peer process.
- Chaincode initializes and manages ledger state through transactions submitted by applications.
- Chaincode typically handles business logic agreed to by members of the network, so it may be considered as a “smart contract”.
- Chaincode can only access the state created by itself and can’t be accessed directly by another chaincode.
- Chaincode can invoke another chaincode to access its state, given the appropriate permission.
- Chaincode deployment requires that organizations agree to the parameters that define a chaincode, such as name, version, and the chaincode endorsement policy.
- Chaincode deployment involves four steps: package the chaincode, install the chaincode on your peers, approve a chaincode definition for your organization, and commit the chaincode definition to the channel.
- Chaincode can be upgraded by installing a new chaincode package and approving and committing a new chaincode definition with a higher version number.
- Chaincode can be migrated to the new Fabric lifecycle by enabling the channel capabilities to V2_0 and following the new deployment steps.

#### Mnemonics and learning tricks

- To remember the four steps of chaincode deployment, use the acronym **PICA**: **P**ackage, **I**nstall, **C**ommit, **A**pprove.
- To remember the difference between chaincode and smart contracts, use the phrase **Chaincode is smart, but smart contracts are not chaincode**. Chaincode is a broader term that encompasses smart contracts, but not all smart contracts are chaincode. Chaincode is specific to Hyperledger Fabric, while smart contracts can be used in other platforms.
- To remember the three languages that chaincode can be written in, use the word **GoNJ**: **Go**, **N**ode.js, **J**ava.