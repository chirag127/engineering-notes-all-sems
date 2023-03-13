## Unit 4 - Hyperledger Fabric (A)

- Hyperledger Fabric is an open source project from the Linux Foundation that provides a modular blockchain framework and a de facto standard for enterprise blockchain platforms  .
- Hyperledger Fabric is intended as a foundation for developing applications or solutions with a modular architecture that allows components, such as consensus and membership services, to be plug-and-play .
- Hyperledger Fabric is designed to support various industry use cases, such as finance, banking, healthcare, IoT, supply chain, manufacturing and technology .
- Hyperledger Fabric has the following key features and advantages  :
  - **Permissioned**: Hyperledger Fabric requires participants to have identities and roles that are managed by a membership service provider (MSP). This ensures accountability and governance in the network.
  - **Private**: Hyperledger Fabric allows participants to create private channels that isolate transactions and data from other participants. This enables confidentiality and scalability in the network.
  - **Modular**: Hyperledger Fabric allows participants to choose and customize various components, such as consensus algorithms, ordering services, smart contracts (called chaincode), and ledger storage. This enables flexibility and interoperability in the network.
  - **Performance**: Hyperledger Fabric uses a novel execute-order-validate architecture that separates the transaction processing into three phases. This reduces network overhead and improves throughput and latency in the network.
  - **Secure**: Hyperledger Fabric uses cryptographic mechanisms, such as digital signatures, encryption, and hashing, to ensure the integrity and authenticity of transactions and data in the network.
- Hyperledger Fabric has the following key components and concepts  :
  - **Peer**: A peer is a node that maintains a copy of the ledger and executes chaincode. Peers can be divided into two types: endorsing peers and committing peers. Endorsing peers validate and endorse transactions, while committing peers verify and commit transactions to the ledger.
  - **Orderer**: An orderer is a node that orders transactions into blocks and delivers them to the peers. Orderers can use different consensus algorithms, such as Solo, Kafka, or Raft, to ensure consistency and finality in the network.
  - **Channel**: A channel is a private communication mechanism that allows a subset of participants to conduct transactions and share data. Channels are created by a channel configuration that defines the policies, members, and permissions of the channel.
  - **Chaincode**: Chaincode is a smart contract that defines the business logic and rules for transactions and data on the ledger. Chaincode is written in a programming language, such as Go, Java, or Node.js, and deployed on the peers.
  - **Ledger**: A ledger is a data structure that records the history and current state of transactions and data on the network. A ledger consists of two parts: a world state and a blockchain. The world state is a database that stores the current values of the data, while the blockchain is a linked list of blocks that stores the history of the transactions.
  - **MSP**: A MSP is a component that manages the identities and roles of the participants in the network. A MSP defines the root of trust, the certificate authorities, the identity validators, and the identity revocation mechanisms for the network.
  - **Client**: A client is an application that interacts with the network by submitting transactions and querying data. A client can use a software development kit (SDK) or a command-line interface (CLI) to communicate with the peers and orderers.

- A possible mnemonic to remember the key components and concepts of Hyperledger Fabric is: **POCCoLMS** (pronounced as "pock-olms"), which stands for **P**eer, **O**rderer, **C**hannel, **C**haincode, **L**edger, **M**SP, and **S**DK/CLI.