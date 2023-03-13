The following is a detailed ascii diagram for Design goals for the notes of the Unit 3 - Permissioned Blockchains in the subject of Block chain Architecture Design.

### Design goals for the notes of the Unit 3 - Permissioned Blockchains in the subject of Block chain Architecture Design

```
+-----------------------------------------------------------------------------+
|                                                                             |
|  Permissioned Blockchains                                                   |
|                                                                             |
|  A permissioned blockchain is a blockchain network that requires access     |
|  to be part of. In these blockchain types, a control layer runs on top of   |
|  the blockchain that governs the actions performed by the allowed           |
|  participants.                                                              |
|                                                                             |
|  The design goals of permissioned blockchains are:                          |
|                                                                             |
|  - To provide a secure and distributed ledger maintained by a number of     |
|    trusted validation nodes.                                                |
|                                                                             |
|  - To benefit from the advantages of blockchains without surrendering the   |
|    authority of the centralized system.                                     |
|                                                                             |
|  - To build the right access hierarchy using hierarchical governance and    |
|    smart contracts.                                                         |
|                                                                             |
|  - To enable various use cases from different application domains, such as  |
|    supply chain, healthcare, finance, etc.                                  |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
+-----------------------------------------------------------------------------+
|                                                                             |
|  Permissioned Blockchain Architecture                                       |
|                                                                             |
|  A permissioned blockchain architecture consists of the following           |
|  components:                                                                |
|                                                                             |
|  - Blockchain layer: This is the core layer that stores the transactions    |
|    and the state of the system in a tamper-proof and immutable way. It      |
|    also implements the consensus mechanism that ensures the agreement       |
|    among the validation nodes.                                              |
|                                                                             |
|  - Access control layer: This is the layer that defines the roles and       |
|    permissions of the participants in the network. It also enforces the     |
|    access policies and the authentication and authorization mechanisms.     |
|                                                                             |
|  - Smart contract layer: This is the layer that enables the execution of    |
|    business logic and rules on the blockchain. It also provides the         |
|    interface for the application layer to interact with the blockchain.     |
|                                                                             |
|  - Application layer: This is the layer that provides the user interface    |
|    and the functionality for the end-users and the stakeholders. It also    |
|    integrates with other systems and services using APIs and middleware.    |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
+-----------------------------------------------------------------------------+
|                                                                             |
|  Permissioned Blockchain Diagram                                            |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|                                                                             |
|  +-----------------+                                                        |
|  |                 |                                                        |
|  |  Application    |                                                        |
|  |  Layer          |                                                        |
|  |                 |                                                        |
|  +-----------------+                                                        |
|         |                                                                    |
|         |                                                                    |
|         |                                                                    |
|         |                                                                    |
|         |                                                                    |
|         |                                                                    |
|         |                                                                    |
|         |                                                                    |
|         |                                                                    |
|         |                                                                    |
|         |                                                                    |
|  +-----------------+                                                        |
|  |                 |                                                        |
|  |  Smart Contract |                                                        |
|  |  Layer          |                                                        |
|  |                 |                                                        |
|  +-----------------+                                                        |
|         |                                                                    |
|         |                                                                    |
|         |                                                                    |
|         |                                                                    |
|         |                                                                    |
|         |                                                                    |
|         |                                                                    |
|         |                                                                    |
|         |                                                                    |
|  +-----------------+                                                        |
|  |                 |                                                        |
|  |  Access Control |                                                        |
|  |  Layer          |                                                        |
|  |                 |                                                        |
|  +-----------------+                                                        |
|         |                                                                    |
|         |                                                                    |
|         |                                                                    |
|         |                                                                    |
|         |                                                                    |
|         |                                                                    |
|         |                                                                    |
|  +-----------------+                                                        |
|  |                 |                                                        |