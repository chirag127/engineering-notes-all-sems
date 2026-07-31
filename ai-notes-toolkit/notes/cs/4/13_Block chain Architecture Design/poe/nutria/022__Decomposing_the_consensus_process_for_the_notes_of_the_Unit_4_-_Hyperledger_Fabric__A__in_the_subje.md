
### Decomposing the Consensus Process for the Notes of the Unit 4 - Hyperledger Fabric (A) in the Subject of Blockchain Architecture Design

1. Consensus is a process used to reach agreement among distributed parties. In the context of blockchain, it refers to the process of reaching agreement on the state of a ledger among all the nodes in the network.

2. Hyperledger Fabric (A) is a blockchain platform designed to enable distributed applications to run securely on the blockchain. It is an open source project initiated by the Hyperledger Project, a collaboration of organizations and individuals from various industries.

3. The consensus process in Hyperledger Fabric (A) is based on a Byzantine Fault Tolerance (BFT) algorithm. This algorithm is used to ensure that all nodes in the network reach agreement on the state of the ledger.

4. The consensus process in Hyperledger Fabric (A) is divided into four stages: Pre-prepare, Prepare, Commit and Validation.

5. In the Pre-prepare stage, the leader node broadcasts a message to all the other nodes in the network. This message contains a block of transactions that the leader node wants to add to the ledger.

6. In the Prepare stage, each node in the network verifies the block of transactions and sends a message to the leader node indicating whether it agrees or disagrees with the block.

7. In the Commit stage, the leader node collects the responses from all the other nodes and computes a consensus value. If the consensus value is positive, the block of transactions is added to the ledger.

8. In the Validation stage, each node in the network validates the block of transactions and updates its local copy of the ledger. Once all the nodes in the network have validated the block of transactions, the consensus process is complete.