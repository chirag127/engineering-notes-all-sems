The following diagram illustrates the basic architecture of a blockchain cryptography system:

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|    Node 1      |      |    Node 2      |      |    Node 3      |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Transactions  |      |  Transactions  |      |  Transactions  |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|    Hashing     |      |    Hashing     |      |    Hashing     |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Consensus     |      |  Consensus     |      |  Consensus     |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Blockchain    |      |  Blockchain    |      |  Blockchain    |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
```

The diagram shows three nodes in a blockchain network, each with four layers: transactions, hashing, consensus, and blockchain.

- Transactions are the data that the nodes want to exchange and record on the blockchain. They can be anything from financial transfers, contracts, votes, or any other information that needs to be verified and immutable.
- Hashing is the process of applying a mathematical function to the transactions to generate a unique and fixed-length string of characters, called a hash. Hashing ensures the integrity and security of the transactions, as any change in the input data would result in a different hash output. Hashing also helps to link the transactions into blocks, as each block contains the hash of the previous block, forming a chain of blocks.
- Consensus is the mechanism that the nodes use to agree on the validity and order of the transactions and blocks. Consensus ensures the decentralization and synchronization of the blockchain, as no single node can control or manipulate the data. Different blockchain networks may use different consensus algorithms, such as proof-of-work, proof-of-stake, or Byzantine fault tolerance.
- Blockchain is the distributed ledger that stores the validated and ordered transactions and blocks. Blockchain ensures the traceability and immutability of the data, as each node has a copy of the ledger and can verify the history and state of the transactions and blocks. Blockchain also provides transparency and accountability, as anyone can access and audit the ledger.