## Unit 4 - Hyperledger Fabric (A)

Hyperledger Fabric is a permissioned, modular, and extensible blockchain platform that supports smart contracts and various consensus mechanisms. It is one of the projects under the Hyperledger umbrella, which is hosted by the Linux Foundation.

Some of the main features and concepts of Hyperledger Fabric are:

- **Channels**: Channels are private subnets of communication between two or more network members, allowing for data isolation and confidentiality. Channels are defined by a configuration block that specifies the policies, access control lists, and members of the channel. Each channel has its own ledger and smart contracts (called chaincode) that are only accessible to the channel members.

- **Chaincode**: Chaincode is the term for smart contracts in Hyperledger Fabric. Chaincode is a program that runs on the peer nodes and interacts with the ledger. Chaincode can be written in various languages, such as Go, Node.js, or Java. Chaincode can be installed and instantiated on different channels, depending on the business logic and the network topology.

- **Endorsement policy**: Endorsement policy is a set of rules that specify which peer nodes must endorse (i.e., sign) a transaction before it can be submitted to the ordering service and committed to the ledger. Endorsement policies can be defined at the chaincode level, the channel level, or the individual transaction level. Endorsement policies enforce the principle of distributed trust and prevent double-spending or malicious transactions.

- **Ordering service**: Ordering service is a component that ensures the consistency and finality of the transactions across the network. Ordering service receives endorsed transactions from the peer nodes and batches them into blocks. Ordering service then delivers the blocks to all the peer nodes in a channel, following a specific consensus algorithm. Ordering service can be configured to use different consensus mechanisms, such as Solo, Kafka, or Raft.

- **Ledger**: Ledger is a distributed database that records the state and history of the transactions in a channel. Ledger consists of two parts: the world state and the blockchain. The world state is a snapshot of the current values of the assets and parameters in the ledger, stored as key-value pairs in a state database (such as LevelDB or CouchDB). The blockchain is a sequential log of the transactions that have occurred in the ledger, stored as blocks linked by hashes. The ledger is immutable and append-only, meaning that the transactions cannot be modified or deleted once they are committed.

- **Membership service provider (MSP)**: MSP is a component that defines the rules and policies for the identity management and access control in a Hyperledger Fabric network. MSP specifies how the certificates are issued, revoked, and verified, and how the roles and permissions are assigned to the network members. MSP allows for the use of different identity providers, such as CA (certificate authority), LDAP (lightweight directory access protocol), or OAuth.

- **Peer**: Peer is a node that hosts the ledger and the chaincode, and participates in the transaction processing and validation. There are two types of peers in Hyperledger Fabric: endorsing peers and committing peers. Endorsing peers are responsible for executing and endorsing transactions, according to the endorsement policy. Committing peers are responsible for validating and committing transactions to the ledger, according to the ordering service. A peer can be both an endorsing peer and a committing peer, depending on the network configuration.

Some of the possible mnemonics and learning tricks for Unit 4 - Hyperledger Fabric (A) are:

- To remember the main features and concepts of Hyperledger Fabric, use the acronym **CCELOLP** (pronounced as "see-lope"), which stands for **C**hannels, **C**haincode, **E**ndorsement policy, **L**edger, **O**rdering service, **L**edger, and **P**eer.

- To remember the types of peers in Hyperledger Fabric, use the phrase **"Endorse and commit"**, which reminds you that there are **endorsing peers** and **committing peers**.

- To remember the parts of the ledger in Hyperledger Fabric, use the phrase **"World and block"**, which reminds you that there are **world state** and **blockchain**.