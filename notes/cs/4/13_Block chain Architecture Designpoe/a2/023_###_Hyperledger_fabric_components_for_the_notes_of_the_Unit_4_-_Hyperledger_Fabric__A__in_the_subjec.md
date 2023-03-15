 Here is the content in markdown format for the given topic:

### Hyperledger fabric components for the notes of the Unit 4 - Hyperledger Fabric (A) in the subject of Block chain Architecture Design

The main components of Hyperledger Fabric are:

- Ledger: The ledger is the permanent and definitive record of all the transactions in the blockchain network. The ledger is maintained by every peer in the network, and the transactions are recorded in blocks that are cryptographically linked together.
- Smart contract: Smart contracts are chaincode in Fabric. They are programs that define the rules and logic around a transaction and control the updates to the ledger. They are written in Go, Node.js, or Java.
- Peers: Peers are the nodes in the network that maintain the ledger, execute smart contracts, and participate in consensus and validation of transactions.
- Ordering service: The ordering service orders transactions into blocks and then delivers them to the peers. This component provides a consistent view of the blockchain and ensures the integrity of the shared ledger.
- Membership services provider: The MSP is responsible for managing identities in the blockchain network. It issues enrollment certificates and verifies client certificates used to authenticate client identity.
- Certificate authority: The CA is responsible for issuing certificates for components in the network. It provides a layer of security by signing certificates to verify member identity.

Some mnemonics to remember the components:

Ledger stores,
Smart contracts execute,
Peers share and validate,
Ordering service sequences,
MSP checks identities,
CA secures certificates.

The advantages of Hyperledger Fabric are:

- Modularity: Fabric has a modular architecture that allows components to be plug-and-play.
- Privacy: Fabric offers confidentiality of transactions and data privacy. Channels can be created to segregate transactions and associated data.
- Performance: Fabric is designed to achieve high throughput of transactions and can handle large networks with many channels and peers.
- Pluggability: Fabric is designed to be pluggable, allowing different implementations of core components. This enables optimization and customization.

The applications of Hyperledger Fabric include:

- Supply chain tracking: Tracking the provenance of goods through a supply chain.
- Healthcare: Securely sharing and tracking health records.
- Finance: Facilitating instant payments and other financial transactions.
- Voting: Secure, verifiable, and private voting systems.

Does this help? Let me know if you would like me to elaborate on any of the points or modify the content.