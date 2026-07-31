# Unit 1 - Introduction to Blockchain

### Hash

- A hash is a fixed-size string of characters that uniquely identifies data.
- Hash functions are mathematical algorithms that take input data of any size and transform it into a fixed-size output, commonly referred to as a hash value or simply a hash.
- The same input data will always produce the same hash value, but even a small change in the input data will produce a completely different hash value.
- Hash functions are commonly used in cryptography, data indexing, and data integrity verification.
- In the context of blockchain, hash functions are used to secure and verify the integrity of data stored in blocks.
- Each block in a blockchain contains a hash of the previous block, creating a chain of blocks that is tamper-evident.
- Any attempt to alter the data in a block will result in a different hash value, breaking the chain and making the tampering evident.
- Commonly used hash functions in blockchain include SHA-256 and Keccak-256.
