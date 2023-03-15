 Here is the content in markdown format for ## Unit 4 - Hyperledger Fabric (A):

## Unit 4 - Hyperledger Fabric (A)

Hyperledger Fabric is a blockchain framework implementation and one of the Hyperledger projects hosted by The Linux Foundation.

### Key points to learn:

1. Hyperledger Fabric has a modular architecture with distinct components and well-defined interfaces enabling plug-and-play components. The major components are:

- Ledger: The blockchain ledger stores the transactions sequenced into blocks and maintains the current state of the network.
- Transaction flow: The transaction flow includes endorsement, ordering, validation, and commit phases to reach consensus on the order and validity of transactions.
- Channels: Channels allow for data isolation and confidentiality through segmentation of the ledger and transaction flows.
- Membership services: Membership services are responsible for authenticating client identity and managing the access control of clients.
- Chaincode: Chaincode are the transaction processors that modify the ledger state, encapsulated in containers.

2. Fabric has a modular system chaincode with an endorsement policy for access control and an isolation model based on channels. This enables both confidentiality of transactions and efficient sharing of a blockchain network between organizations with differing trust relationships.

3. Fabric uses a variant of the Practical Byzantine Fault Tolerance (PBFT) algorithm to achieve high performance with strong consistency and fault tolerance. The ordering service orders transactions into blocks and then distributes the blocks to peers to commit the transactions to their ledgers.

4. Some key concepts in Hyperledger Fabric are:

- Ledger: The permanent, tamper-resistant, shared record of all the transactions in a network. The ledger is append-only, so once a transaction is recorded to the ledger, it cannot be removed or modified.
- World state: The current state of the ledger. It is calculated by executing the chaincode transactions sequentially and capture the outputs.
- Transaction: A proposal to update the ledger and the corresponding world state. It is either validated and committed to the ledger, or invalidated.
- Channel: A private 'subnet' of communication between two or more specific peers. Channels are defined by a configuration block, and they isolate transactions, blocks, and ledger state.
- Chaincode: The term for smart contracts in Hyperledger Fabric. Chaincode is executable code that implements a prescribed interface.
- Endorsement policy: A policy that determines which peers must endorse a transaction proposal for it to be considered valid. The policy is written in a general-purpose policy language.

[Detailed explanations, diagrams, examples, mnemonics, advantages, disadvantages, applications, etc. can be included here if helpful for learning.]