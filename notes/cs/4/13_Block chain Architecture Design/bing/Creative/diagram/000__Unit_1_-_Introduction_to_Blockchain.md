## Unit 1 - Introduction to Blockchain

A blockchain is a distributed ledger that records transactions in a secure and verifiable way. It consists of a network of nodes that communicate and validate transactions using a consensus mechanism. Each node maintains a copy of the ledger, which is composed of blocks that contain transactions. Each block is linked to the previous block by a cryptographic hash, creating a chain of blocks that is immutable and tamper-proof.

The following diagram illustrates the basic architecture of a blockchain:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|     Node 1      |     |     Node 2      |     |     Node 3      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  +----------+   |     |  +----------+   |     |  +----------+   |
|  |          |   |     |  |          |   |     |  |          |   |
|  |  Block n |   |     |  |  Block n |   |     |  |  Block n |   |
|  |          |   |     |  |          |   |     |  |          |   |
|  +----------+   |     |  +----------+   |     |  +----------+   |
|  |          |   |     |  |          |   |     |  |          |   |
|  |  Block n-1 |  |     |  |  Block n-1 |  |     |  |  Block n-1 |  |
|  |          |   |     |  |          |   |     |  |          |   |
|  +----------+   |     |  +----------+   |     |  +----------+   |
|  |          |   |     |  |          |   |     |  |          |   |
|  |  Block n-2 |  |     |  |  Block n-2 |  |     |  |  Block n-2 |  |
|  |          |   |     |  |          |   |     |  |          |   |
|  +----------+   |     |  +----------+   |     |  +----------+   |
|  |          |   |     |  |          |   |     |  |          |   |
|  |  Block n-3 |  |     |  |  Block n-3 |  |     |  |  Block n-3 |  |
|  |          |   |     |  |          |   |     |  |          |   |
|  +----------+   |     |  +----------+   |     |  +----------+   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

Each block contains a header and a body. The header contains metadata such as the block number, the timestamp, the hash of the previous block, and the hash of the transactions in the body. The body contains a list of transactions that are validated by the nodes using a digital signature scheme. Each transaction has a sender, a receiver, an amount, and a fee.

When a node wants to add a new transaction to the ledger, it broadcasts it to the network. The other nodes verify the validity of the transaction and add it to their pool of pending transactions. Then, a node is selected to create a new block using a consensus mechanism, such as proof-of-work or proof-of-stake. The selected node collects some of the pending transactions and hashes them together to form a Merkle tree. The root of the Merkle tree is included in the block header, along with the hash of the previous block. The node then solves a cryptographic puzzle to find a nonce that makes the block header hash below a certain difficulty target. The node then broadcasts the new block to the network. The other nodes verify the validity of the block and append it to their ledger, if it is the longest chain. The node that created the block is rewarded with some newly minted coins and the fees of the transactions in the block.

This process ensures that the ledger is consistent and secure across the network, and that no one can alter or delete any transactions once they are recorded in a block. The blockchain architecture also enables peer-to