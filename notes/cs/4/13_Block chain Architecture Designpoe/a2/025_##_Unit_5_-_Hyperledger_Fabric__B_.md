 Here is the content in markdown format for ## Unit 5 - Hyperledger Fabric (B):

## Unit 5 - Hyperledger Fabric (B)

### Peers
- Peers are the nodes in the Fabric network that maintain the ledger and execute chaincode (smart contracts).
- Endorsing peers: Execute transactions and endorse proposals.
- Committing peers: Validate and commit transactions to the ledger.
- Ordering peers: Special peers that order transactions into blocks.

### Ledger
- The ledger is a permanent and tamper-resistant store for all blockchain data (transactions, blocks, etc.).
- Two types:
    - World state: Current state of the ledger (asset holdings, etc.).
    - Blockchain: Ordered blocks of transactions that comprise the entire history of the ledger.
- The ledger is distributed and maintained by committing peers.

### Channels
- Channels are private subnets of communication within a Fabric network.
- Allow for confidential transactions and segmented data access control.
- Peers opt into channels and can belong to multiple channels.
- Data in channels is isolated (only members of a channel can access the data).

**Mnemonic**: Think of channels like different rooms in a company - only certain employees have access to certain rooms.

### Chaincode (Smart Contracts)
- Chaincode are programs that define and execute transactions on the ledger.
- Written in Go, Node.js, Java, or Python.
- Control asset transfer, record state changes, etc.
- Installed on endorsing peers and invoked via transactions.
- Can have multiple versions installed for upgrade/rollback.

**Advantages**: Flexibility, Upgradability, Language Options
**Disadvantages**: Complexity, Vulnerability to bugs

[Detailed diagrams, examples, applications, etc. can be added here if helpful for learning and exams.]