# Unit 1 - Introduction to Blockchain

## Hash

- A hash is a function that converts any data form into a unique text string of a fixed length .
- A hash is also called a digest, a fingerprint, or a checksum of the data.
- A hash has the following properties :
  - It is deterministic, meaning that the same data will always produce the same hash value.
  - It is one-way, meaning that it is easy to compute the hash from the data, but hard to recover the data from the hash.
  - It is collision-resistant, meaning that it is very unlikely that two different data inputs will produce the same hash value.
- Hashes are used in several parts of a blockchain system :
  - Each block header contains the previous block's hash, which ensures that nothing has been tampered with as new blocks are added.
  - Cryptocurrency blockchains use hashes to secure information and make the ledger immutable.
  - Miners create new blocks by providing two hashes to the network: a hash of all transactions in the block, and a hash that proves that they have spent a considerable amount of energy creating the block.
- The most common hash algorithm used in blockchain is SHA-256 or Secure Hashing Algorithm 256 bits. It produces a 64-character hexadecimal string as the hash value. For example, the hash of "Hello, world!" is "64ec88ca00b268e5ba1a35678a1b5316d212f4f366b2477232534a8aeca37f3c".