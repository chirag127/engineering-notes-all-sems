 Here is the content in markdown format for the topic -
### Consensus for the notes of the Unit 1 - Introduction to Blockchain in the subject of Block chain Architecture Design

- Consensus is a agreement on a single data value among distributed nodes in a network. In blockchain, consensus is required to agree upon the order of transactions and to prevent double spending.
- Types of Consensus:
    - Proof of Work: Nodes prove that they have done some work to solve a complex computational problem. The node that solves the problem first gets to add the next block in the chain. Eg: Bitcoin uses Proof of Work.
    - Proof of Stake: Nodes prove that they have a stake in the network by owning and locking up some currency. The node with the largest stake gets to add the next block. Eg: Ethereum is moving to Proof of Stake.
    - Delegated Proof of Stake: Nodes elect a fixed set of delegates to validate transactions and earn rewards. Eg: EOS uses Delegated Proof of Stake.
    - Practical Byzantine Fault Tolerance: A complex system of consensus that can tolerate malicious nodes. Eg: Hyperledger uses Practical Byzantine Fault Tolerance.
- Properties of a good Consensus mechanism:
    - Agreement: All honest nodes must agree upon the same value.
    - Validity: If all nodes are honest, the consensus value must be the correct value.
    - Integrity: No node can manipulate the consensus process to make the nodes agree on an incorrect value.
    - Termination: The consensus process must eventually terminate with all nodes agreeing on a value.
- Advantages: Ensures integrity of the blockchain, Prevents double spending, Reaches agreement in a decentralized network.
- Disadvantages: Proof of Work is energy intensive, Vulnerable to 51% attacks if one entity controls majority of nodes or currency.

[Detailed diagrams and examples can be added if required]