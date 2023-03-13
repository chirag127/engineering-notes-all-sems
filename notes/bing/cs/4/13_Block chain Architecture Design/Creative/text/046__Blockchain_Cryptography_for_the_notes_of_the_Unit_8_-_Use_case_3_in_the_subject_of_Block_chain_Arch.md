### Blockchain Cryptography

- Blockchain cryptography is a method of securing data and transactions on a distributed ledger using cryptographic techniques.
- Cryptography is the science of encoding and decoding information using mathematical principles and algorithms.
- Cryptography in blockchain has two main functions: to ensure the integrity and authenticity of data, and to enable the privacy and confidentiality of transactions.
- Blockchain cryptography uses two main concepts: hashing and public-key cryptography.

#### Hashing

- Hashing is a process of transforming any input data into a fixed-length output, called a hash or a digest, using a mathematical function, called a hash function.
- Hashing has the following properties:
  - It is deterministic, meaning that the same input always produces the same output.
  - It is one-way, meaning that it is easy to compute the output from the input, but hard to find the input from the output.
  - It is collision-resistant, meaning that it is hard to find two different inputs that produce the same output.
- Hashing is used in blockchain to:
  - Link blocks together, by including the hash of the previous block in the current block.
  - Verify the validity of blocks, by checking if the hash of the block matches the expected value.
  - Store transaction data efficiently, by using a data structure called a Merkle tree, where the root hash represents the entire set of transactions.
  - Generate unique identifiers for transactions, blocks, and addresses, by hashing the relevant data.

#### Public-key cryptography

- Public-key cryptography is a system of encryption and decryption that uses two different keys: a public key and a private key.
- The public key can be shared with anyone, while the private key must be kept secret by the owner.
- The public key and the private key are mathematically related, but it is hard to derive the private key from the public key.
- Public-key cryptography has the following properties:
  - It is asymmetric, meaning that the encryption and decryption processes use different keys.
  - It enables digital signatures, which are a way of proving the ownership and authenticity of a message, by using the private key to sign the message and the public key to verify the signature.
  - It enables encryption and decryption, which are a way of protecting the confidentiality of a message, by using the public key to encrypt the message and the private key to decrypt the message.
- Public-key cryptography is used in blockchain to:
  - Generate addresses, which are derived from the public key and used to identify the sender and the receiver of a transaction.
  - Sign transactions, which are a way of authorizing the transfer of value from one address to another, by using the private key to sign the transaction and the public key to verify the signature.
  - Encrypt and decrypt transactions, which are a way of ensuring the privacy and confidentiality of the transaction data, by using the public key to encrypt the transaction and the private key to decrypt the transaction.