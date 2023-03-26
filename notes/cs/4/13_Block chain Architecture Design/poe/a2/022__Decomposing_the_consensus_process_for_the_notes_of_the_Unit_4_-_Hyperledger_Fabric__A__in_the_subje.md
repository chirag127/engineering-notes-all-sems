 Here is the formal content written in Markdown format without any emojis or external links on the given topic:

### Decomposing the consensus process for the notes of the Unit 4 - Hyperledger Fabric (A) in the subject of Block chain Architecture Design.

1. Peers: Peers are the network participants in Hyperledger Fabric. They maintain the ledger and execute chaincode (smart contracts). Peers reach consensus on the order of transactions and the state of the ledger.

2. Ledger: The ledger is a append-only transaction log maintained by all peers in the network. New transactions are recorded in blocks which are appended to the ledger in a linear, chronological order. The ledger maintains the complete and consistent history of all transactions ever executed by the network.

3. Chaincode: Chaincode (a.k.a smart contracts) are software modules that define and execute transaction logic on the ledger. Chaincode runs in a separate process and is isolated from the peer process. Communication between the chaincode and the peer happens via transactions on the ledger.

4. Ordering service: The ordering service orders transactions into blocks and then delivers the blocks to peers for commit and validation. This is a centralized service in Fabric v1.0, however multiple ordering nodes can be configured for high availability and fault tolerance.

5. Membership services: The membership services component handles the network's security by managing identities (members, admins, etc.) and their permissions. It stores identities and credentials and verifies signatures and certificates used to sign transactions and other requests to the blockchain network.

The notes cover the key components involved in the consensus process in Hyperledger Fabric (peers, ledger, chaincode, ordering service, and membership services) and their roles and interactions in maintaining a consistent, shared ledger. The notes are written in a formal tone with points and without any emojis or external links as per the given instructions.