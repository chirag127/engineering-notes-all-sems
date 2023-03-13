## Unit 1 - Introduction to Blockchain

A blockchain is a distributed ledger that records transactions in a sequence of blocks. Each block contains a cryptographic hash of the previous block, a timestamp, and a list of transactions. Transactions are verified by the network nodes through a consensus mechanism, such as proof-of-work or proof-of-stake. Once a block is added to the chain, it cannot be altered or deleted, ensuring the integrity and immutability of the ledger.

The following diagram illustrates the basic architecture of a blockchain system:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|     Node 1      |     |     Node 2      |     |     Node 3      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Blockchain     |     |  Blockchain     |     |  Blockchain     |
|    Ledger       |     |    Ledger       |     |    Ledger       |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Consensus      |     |  Consensus      |     |  Consensus      |
|  Mechanism      |     |  Mechanism      |     |  Mechanism      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Cryptography   |     |  Cryptography   |     |  Cryptography   |
|  and Digital    |     |  and Digital    |     |  and Digital    |
|  Signatures     |     |  Signatures     |     |  Signatures     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Transactions   |     |  Transactions   |     |  Transactions   |
|  and Data       |     |  and Data       |     |  and Data       |
|  Sources        |     |  Sources        |     |  Sources        |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

Each node in the network has a copy of the blockchain ledger, which is synchronized through the consensus mechanism. The transactions and data sources are the inputs to the system, which are validated and recorded in the ledger. The cryptography and digital signatures are used to ensure the security and authenticity of the transactions. The blockchain architecture enables trusted transactions among the participants without the need for a central authority.