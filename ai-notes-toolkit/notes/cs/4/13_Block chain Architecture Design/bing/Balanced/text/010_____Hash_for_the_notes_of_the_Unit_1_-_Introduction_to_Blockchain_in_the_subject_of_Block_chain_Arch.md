### Hash for the notes of the Unit 1 - Introduction to Blockchain in the subject of Block chain Architecture Design

- A hash is a function that converts any data form into a unique text string of a fixed length .
- A hash is also called a digest, a fingerprint, or a checksum of the data.
- A hash has the following properties  :
  - It is deterministic, meaning that the same input data will always produce the same hash value.
  - It is one-way, meaning that it is easy to compute the hash from the input data, but hard to find the input data from the hash.
  - It is collision-resistant, meaning that it is very unlikely that two different input data will produce the same hash value.
- Hashes are used in several parts of a blockchain system :
  - Each block header contains the previous block's hash, which ensures that nothing has been tampered with as new blocks are added.
  - Cryptocurrency blockchains use hashes to secure information and make the ledger immutable.
  - Miners create new blocks by finding a hash that meets a certain difficulty criterion, which is called proof-of-work.
  - Transactions are hashed and grouped into a data structure called a Merkle tree, which allows for efficient verification of the transactions.
- The most common hash algorithm used in blockchain is SHA-256 or Secure Hashing Algorithm 256 bits.
  - SHA-256 takes any input data and produces a 256-bit (32-byte) hash value, which is usually represented as a 64-digit hexadecimal number.
  - SHA-256 is considered to be a secure and reliable hash algorithm, as no collisions or vulnerabilities have been found so far.
  - SHA-256 is also used in other cryptographic applications, such as digital signatures, encryption, and authentication.