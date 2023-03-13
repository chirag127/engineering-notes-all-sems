The following is a detailed ASCII diagram for Blockchain Cryptography for the notes of the Unit 8 - Use case 3 in the subject of Block chain Architecture Design.

### Blockchain Cryptography

A blockchain is a distributed ledger with growing lists of records (blocks) that are securely linked together via cryptographic hashes. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data (generally represented as a Merkle tree, where data nodes are represented by leaves). The timestamp proves that the transaction data existed when the block was published in order to get into the blockchain. The hash secures the block against tampering.

The blockchain network consists of nodes that communicate with each other using peer-to-peer transmission. Each node maintains a copy of the ledger and validates new blocks using a consensus protocol. The consensus protocol ensures that all nodes agree on the state of the ledger and prevents malicious nodes from creating forks or double-spending.

Cryptography is a method of securing data from unauthorized access. In the blockchain, cryptography is used to secure transactions taking place between two nodes in a blockchain network. There are two main types of cryptography used in blockchain: asymmetric cryptography and symmetric cryptography.

Asymmetric cryptography, also known as public-key cryptography, uses a pair of keys: a public key and a private key. The public key can be shared with anyone, while the private key is kept secret by the owner. The public key can be used to encrypt data, while the private key can be used to decrypt data. The public key can also be used to verify the signature of the owner, while the private key can be used to sign data.

Symmetric cryptography, also known as secret-key cryptography, uses a single key to encrypt and decrypt data. The key must be shared between the sender and the receiver of the data, and must be kept secret from anyone else. Symmetric cryptography is faster than asymmetric cryptography, but less secure, as the key can be compromised or intercepted.

In blockchain, asymmetric cryptography is used to generate digital signatures, which are used to prove the ownership and authenticity of transactions. A digital signature is created by hashing the transaction data and signing it with the private key of the sender. The digital signature can be verified by anyone using the public key of the sender. The digital signature ensures that the transaction data has not been altered and that the sender is the legitimate owner of the funds.

Symmetric cryptography is used to encrypt the data stored in the blocks, which are then hashed and linked together. The encryption key is derived from the hash of the previous block, creating a chain of encryption keys. The encryption key ensures that the data in the block can only be decrypted by the nodes that have the previous block. The encryption key also prevents anyone from modifying the data in the block, as it would invalidate the hash and break the chain.

The following diagram illustrates the basic architecture of a blockchain cryptography system using ASCII art:

```
+-----------------+    +-----------------+    +-----------------+
| Block 1         |    | Block 2         |    | Block 3         |
|-----------------|    |-----------------|    |-----------------|
| Hash: H1        |    | Hash: H2        |    | Hash: H3        |
| Prev Hash: 0    |    | Prev Hash: H1   |    | Prev Hash: H2   |
| Timestamp: T1   |    | Timestamp: T2   |    | Timestamp: T3   |
| Data: D1        |    | Data: D2        |    | Data: D3        |
| Signature: S1   |    | Signature: S2   |    | Signature: S3   |
+-----------------+    +-----------------+    +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       V                      V                      V
+-----------------+    +-----------------+    +----------------