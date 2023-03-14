 Here is the content in markdown format for ## Unit 5 - Hyperledger Fabric (B):

## Unit 5 - Hyperledger Fabric (B)

### Ledger
- The ledger is a collection of blocks added to the blockchain in a linear, chronological order.
- Each block contains a timestamp and a link to the previous block in the chain.
- The ledger is distributed and maintained by the peers in the network.
- The ledger provides an immutable, permanent, and tamper-resistant record of all the transactions.

### World state
- The world state represents the latest values for all keys (assets) in the blockchain network.
- It is like a global distributed database that contains the latest state of all the ledger entries/records.
- The world state is updated accordingly whenever a transaction is committed to the ledger.
- The world state allows efficient searching/retrieval of records/values based on keys.
- The world state is also distributed and maintained by the peers in the network in sync.

### Chaincode (Smart Contracts)
- Chaincode (also called smart contracts) are programs that are executed by the peers to query or update the world state based on the transactions.
- They are written in general purpose programming languages like Go and installed on the peers.
- The chaincode defines and enforces the rules/logic around the assets/data in the blockchain network.
- The execution of chaincode leads to modification of the world state and creation of new ledger entries.
- The chaincode must be installed and instantiated on every peer that endorses or commits transactions.

[Detailed diagrams, examples, advantages, disadvantages, and applications can be included here if found helpful.]