 Here is the content in markdown format for the given topic:

### Design goals for the notes of the Unit 3 - Permissioned Blockchains in the subject of Block chain Architecture Design

The design goals for the notes on Permissioned Blockchains are:

1. Explain what Permissioned Blockchains are:
- Permissioned Blockchains are private blockchains where the identity of the nodes is known and verified. Only authorized nodes are allowed to join the network.
- They are centralized in nature as the consensus is achieved by a subset of nodes rather than all the nodes in the network.
- Examples: Hyperledger Fabric, R3 Corda, Quorum, etc.

2. Highlight the advantages of Permissioned Blockchains:
- Greater scalability as the number of nodes is limited.
- Faster transaction speeds due to smaller network size and alternative consensus mechanisms.
- Enhanced privacy as the identities are known and the data is restricted to certain nodes.
- Regulatory compliance is easier as the participating nodes can be determined.

3. Discuss the disadvantages of Permissioned Blockchains:
- They are less decentralized as the consensus is achieved by a subset of trusted nodes.
- Single point of failure as the network depends on the participating nodes. If the nodes go down, the entire network halts.
- Prone to collusions and power concentration as the nodes are known and authoritative.

4. Explain the components and working of a sample Permissioned Blockchain platform like Hyperledger Fabric:
- Membership services: Handles the addition and removal of members (nodes) from the network.
- Consensus: Reaches agreement on the state of the ledger via Kafka and couchDB.
- Transactions: Proposes and executes chaincode (smart contracts) for transactions.
- Ledger: Maintains the immutable, permanent, and verifiable record of all the transactions.
- APIs and CLIs: Provide interfaces to interact with the blockchain network.

[Include diagrams and examples to illustrate the concepts]

The notes can include Mnemonics and learning tricks wherever applicable to enhance understanding and memorability. Only include them if they are easy to remember. The content has to be written in a formal tone as if writing study material for exams.