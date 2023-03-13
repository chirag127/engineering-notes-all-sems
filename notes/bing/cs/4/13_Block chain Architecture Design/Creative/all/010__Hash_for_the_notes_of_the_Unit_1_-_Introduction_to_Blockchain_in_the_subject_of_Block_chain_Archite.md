### Hash for the notes of the Unit 1 - Introduction to Blockchain in the subject of Block chain Architecture Design

- A hash is a function that converts any input data into a fixed-length string of bytes, called a hash value or a digest.
- A hash function has the following properties:
  - Deterministic: The same input data will always produce the same hash value.
  - Fast: The hash function can be computed quickly and efficiently.
  - Preimage resistant: It is hard to find the input data given only the hash value.
  - Collision resistant: It is hard to find two different inputs that produce the same hash value.
  - Avalanche effect: A small change in the input data will produce a large change in the hash value.
- Hash functions are used in blockchain for various purposes, such as:
  - Merkle tree: A data structure that uses hash functions to verify the integrity and consistency of a large set of data. The hash value of the root node of the tree is called the Merkle root and it represents the entire data set.
  - Proof of work consensus: An algorithm that defines a valid block as the one whose block header has a hash value that meets a certain difficulty criterion. The process of finding such a hash value is called mining and it requires a lot of computational power.
  - Digital signature: A cryptographic scheme that uses a private key to sign a message or a document and a public key to verify the signature. The signature is a hash value of the message or the document that is encrypted with the private key.
  - Address: A unique identifier of a blockchain account that is derived from the public key using a hash function. The address is used to send and receive transactions on the blockchain.
- Some of the common hash functions used in blockchain are:
  - SHA-256: A hash function that produces a 256-bit hash value. It is used in Bitcoin, Ethereum, and many other blockchains.
  - RIPEMD-160: A hash function that produces a 160-bit hash value. It is used in Bitcoin to create addresses from public keys.
  - Keccak-256: A hash function that produces a 256-bit hash value. It is used in Ethereum to create addresses from public keys and to implement smart contracts.
  - BLAKE2: A hash function that produces a variable-length hash value. It is used in Zcash, a privacy-focused blockchain, to implement zero-knowledge proofs.
- A possible mnemonic to remember the hash functions and their uses is:

  - SHA-256: **S**ecure **H**ash **A**lgorithm for **256**-bit blockchains
  - RIPEMD-160: **R**educed **I**nput **P**assword **E**ncryption **M**essage **D**igest for **160**-bit addresses
  - Keccak-256: **K**ey **E**ncryption **C**ode **C**reation for **256**-bit Ethereum
  - BLAKE2: **B**etter **L**ightweight **A**lternative **K**ey **E**ncryption for **2**-way privacy