 Here is the content in markdown format for the given topic:

### Hyperledger fabric components for the notes of the Unit 4 - Hyperledger Fabric (A) in the subject of Block chain Architecture Design

The major components of Hyperledger Fabric are:

1. Ledger - The ledger stores the blockchain data. It maintains the chain of transactions in a blockchain network. The ledger is replicated across peers in the network.
2. Smart Contracts - Smart contracts define the business logic of the blockchain network. They are written in Go or Node.js. Smart contracts can query or update the ledger state.
3. Peers - Peers are the nodes in the blockchain network that maintain the ledger and execute smart contracts. The peers perform two major functions:

- Maintain a copy of the ledger and validate transactions.
- Execute smart contracts by processing transactions that trigger the smart contract logic.

4. Ordering Service - The ordering service ensures that transactions are delivered in the same order across all peers in the network. It receives transactions from clients, orders them, and delivers them to peers. This ensures consistency across the ledger replicas.
5. Membership Service Provider (MSP) - The MSP manages identities of users and organizations involved in the blockchain network. It issues enrollment certificates and verifies signatures from users. These help establish trust between the different participants in a permissioned blockchain network.
6. Certificate Authority (CA) - The CA issues certificates for components like peers and ordering nodes. These certificates are used to establish secure TLS connections between components. The CA helps establish identity and security in the blockchain network.

Some key advantages of Hyperledger Fabric are:

- Modular architecture with plug-and-play components
- Smart contract expressiveness with general purpose programming languages
- Identity management and access control suitable for private blockchains
- Scalability and performance suitable for enterprise use cases

Some key disadvantages are:

- Steep learning curve due to flexibility and complexity
- Lack of formal verification methods for smart contracts
- Limited number of developers and resources in the Hyperledger community compared to public blockchains like Ethereum