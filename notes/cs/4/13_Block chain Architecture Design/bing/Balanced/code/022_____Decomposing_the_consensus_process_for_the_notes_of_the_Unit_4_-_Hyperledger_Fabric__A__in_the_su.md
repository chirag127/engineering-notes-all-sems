### Decomposing the consensus process for the notes of the Unit 4 - Hyperledger Fabric (A) in the subject of Block chain Architecture Design

- Consensus in Hyperledger Fabric is a process where the nodes in the network provide a guaranteed ordering of the transactions and validate those blocks of transactions that need to be committed to the ledger .
- Consensus must ensure the following in the network:
  - Agreement on the order and results of transactions
  - Fault tolerance and resilience to attacks
  - Finality and correctness of the ledger state
- Consensus in Hyperledger Fabric is broken out into three phases: Endorsement, Ordering, and Validation .
  - Endorsement is driven by policy (m out of n signatures) upon which participants endorse a transaction. Endorsers are peers that simulate and validate the transactions and produce a signed response.
  - Ordering phase will get the endorsed transactions and agree on the order to be committed to the ledger. Orderers are nodes that batch the transactions into blocks and deliver them to the peers.
  - Validation phase will check the endorsement policy and the read-write sets of the transactions and mark them as valid or invalid. Validators are peers that apply the transactions to the ledger and maintain the state.
- Hyperledger Fabric follows a modular approach wherein different consensus techniques can be plugged in as per the requirement. Currently, Hyperledger Fabric uses Solo and Kafka to reach consensus, which requires a node to validate a batch of transactions and add them as a new block to the blockchain.
  - Solo is a single orderer node that is used for development and testing purposes. It does not provide any fault tolerance or scalability.
  - Kafka is a distributed messaging system that uses a cluster of orderer nodes and a set of Kafka brokers to provide fault tolerance, scalability, and crash recovery. It uses a leader-follower model to elect a leader node that orders the transactions and broadcasts them to the followers.