## Unit 5 - Hyperledger Fabric (B)

This unit covers the following topics related to Hyperledger Fabric:

- Chaincode
- Channels
- Private data
- Endorsement policies
- Consensus mechanisms
- Ordering service

### Chaincode

- Chaincode is the term used for smart contracts in Hyperledger Fabric.
- Chaincode is a program that implements the business logic and rules of a specific application.
- Chaincode runs on the peers and interacts with the ledger through transactions.
- Chaincode can be written in various languages, such as Go, Node.js, or Java.
- Chaincode can be installed and instantiated on one or more channels by the administrators of the organizations that participate in the channel.
- Chaincode can be invoked by the clients through proposals, which are sent to the endorsing peers for endorsement.
- Chaincode can also query the ledger state or invoke other chaincodes on the same or different channels.

### Channels

- Channels are the mechanism for creating private subnets of communication between two or more organizations in Hyperledger Fabric.
- Channels allow for data isolation and confidentiality among the participating organizations.
- Channels are created by a channel configuration transaction, which defines the policies, access control lists, and members of the channel.
- Channels are identified by a unique name and a channel ID.
- Channels can have one or more chaincodes installed and instantiated on them.
- Channels can also have one or more ordering service nodes assigned to them, which are responsible for ordering and delivering the transactions to the peers.
- Channels can be joined or left by the organizations at any time, as long as they have the permission from the channel administrator.

### Private data

- Private data is a feature of Hyperledger Fabric that allows for the sharing of confidential data among a subset of organizations on a channel, without exposing it to the rest of the network.
- Private data is stored in a separate database called a private data store (PDS), which is local to each peer.
- Private data is accessed through a special type of chaincode called a private data collection (PDC), which defines the name, scope, and endorsement policy of the private data.
- Private data is transmitted among the authorized peers through a gossip protocol, which ensures the data consistency and availability.
- Private data is hashed and stored on the ledger as a proof of existence, which can be used for verification and audit purposes.

### Endorsement policies

- Endorsement policies are the rules that specify which peers must endorse a transaction before it can be submitted to the ordering service and committed to the ledger.
- Endorsement policies are defined at the chaincode level or the private data collection level, and can be customized for different scenarios and requirements.
- Endorsement policies can be expressed in a simple language that uses the logical operators AND, OR, and NOT, and the attributes of the peers, such as their organization, role, or identity.
- Endorsement policies can also be expressed in a more complex language that uses the signature policy syntax (SPS), which allows for more flexibility and granularity.
- Endorsement policies are evaluated by the client and the committing peers to ensure that the transaction has received the required endorsements.

### Consensus mechanisms

- Consensus mechanisms are the processes that ensure the agreement and finality of the transactions among the peers in Hyperledger Fabric.
- Consensus mechanisms consist of three phases: endorsement, ordering, and validation.
- Endorsement is the phase where the client sends a proposal to the endorsing peers, and receives their endorsements in the form of signed responses.
- Ordering is the phase where the ordering service nodes receive the endorsed transactions from the clients, and sort them into blocks according to a predefined algorithm and policy.
- Validation is the phase where the committing peers receive the blocks from the ordering service, and validate the transactions against the endorsement policies and the current ledger state.
- Consensus mechanisms can be configured and customized for different levels of trust, performance, and scalability.

### Ordering service

- Ordering service is the component of Hyperledger Fabric that provides the ordering and delivery of the transactions to the peers.
- Ordering service consists of one or more ordering service nodes (OSNs), which can be run by one or more organizations.
- Ordering service nodes can use different algorithms and protocols to order the transactions, such as Solo, Kafka, or Raft.
- Ordering service nodes can also use different policies to determine the access and participation of the organizations in the ordering service, such as implicit or explicit policies.
- Ordering service nodes can be added or removed from the ordering service at any time, as long as they have the permission from the ordering service administrator.