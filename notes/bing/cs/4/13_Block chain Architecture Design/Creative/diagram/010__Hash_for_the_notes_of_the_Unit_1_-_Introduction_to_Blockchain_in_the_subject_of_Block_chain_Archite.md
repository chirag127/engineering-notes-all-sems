A hash function is a mathematical function that takes an arbitrary input and produces a fixed-length output, called a hash or a digest. Hash functions are used in blockchain to ensure the integrity, security and efficiency of the data. A hash function has the following properties:

- Deterministic: The same input always produces the same output.
- Fast: The hash function can be computed quickly for any input.
- Pre-image resistant: It is hard to find an input that produces a given output.
- Collision resistant: It is hard to find two different inputs that produce the same output.
- Avalanche effect: A small change in the input produces a large change in the output.

A hash function can be represented as a diagram like this:

```
+----------------+       +-------------+       +----------------+
| Arbitrary input| ----> | Hash function| ----> | Fixed-length output|
+----------------+       +-------------+       +----------------+
```

In blockchain, hash functions are used for various purposes, such as:

- Merkle tree: A data structure that uses hash functions to organize and verify the transactions in a block. The root hash of the Merkle tree is stored in the block header and serves as a summary of all the transactions in the block.
- Proof of work: A consensus algorithm that requires the miners to find a nonce that produces a hash value that satisfies a certain difficulty target. The hash value is based on the block header, which includes the previous block hash, the Merkle root hash, the timestamp and the nonce.
- Digital signature: A cryptographic scheme that uses a private key to sign a message and a public key to verify the signature. The signature is based on the hash of the message, which ensures that the message has not been tampered with.

A diagram of the basic architecture of a blockchain using hash functions can be drawn as follows:

```
+----------------+       +-------------+       +----------------+
| Block 1        |       | Block 2     |       | Block 3        |
+----------------+       +-------------+       +----------------+
| Previous hash  |       | Previous hash|      | Previous hash  |
| Nonce          |       | Nonce       |       | Nonce          |
| Timestamp      |       | Timestamp   |       | Timestamp      |
| Merkle root    |       | Merkle root |       | Merkle root    |
+----------------+       +-------------+       +----------------+
| Transactions   |       | Transactions|       | Transactions   |
|                |       |             |       |                |
|                |       |             |       |                |
|                |       |             |       |                |
+----------------+       +-------------+       +----------------+
| Hash           |       | Hash        |       | Hash           |
+----------------+       +-------------+       +----------------+
       |                      |                      |
       |                      |                      |
       +----------------------+----------------------+
                              |
                              V
                    +-----------------+
                    | Hash function   |
                    +-----------------+
                              |
                              V
                    +-----------------+
                    | Difficulty target|
                    +-----------------+
                              |
                              V
                    +-----------------+
                    | Proof of work   |
                    +-----------------+
```

I hope this diagram helps you understand the hash function and its role in blockchain. If you have any questions, please let me know.