### Blockchain Cryptography for the notes of the Unit 8 - Use case 3 in the subject of Block chain Architecture Design

Cryptography is an important aspect of blockchain technology as it ensures that the data stored on the blockchain is secure and tamper-proof. In this unit, we will discuss the different types of cryptography used in blockchain and their applications.

#### Types of Cryptography Used in Blockchain

1. **Hashing**: Hashing is a one-way function that takes an input and produces a fixed-size output. It is commonly used in blockchain to create a unique identifier, also known as a hash, for each block in the chain. The hash of a block is calculated based on the data in the block and the hash of the previous block. This makes it impossible to modify previous blocks without changing the entire chain.

2. **Public Key Cryptography**: Public key cryptography, also known as asymmetric cryptography, uses two keys, a public key and a private key, to encrypt and decrypt data. The public key is used to encrypt the data, while the private key is used to decrypt it. This type of cryptography is used in blockchain to create a digital signature for transactions. The sender uses their private key to sign the transaction, which can be verified using their public key.

3. **Symmetric Cryptography**: Symmetric cryptography uses the same key to both encrypt and decrypt data. This type of cryptography is used in blockchain to encrypt the data stored in each block. The key used for encryption is derived from the hash of the previous block, making it impossible to modify previous blocks without changing the entire chain.

#### Mnemonics and Learning Tricks

1. To remember the difference between public key and symmetric cryptography, think of a mailbox. The public key is like the mailbox, anyone can put something in it, but only the owner can take something out. Symmetric cryptography is like a safe, only the owner has the key to open it.

2. To remember how hashing works in blockchain, think of a jigsaw puzzle. The hash of a block is like a piece of the puzzle, it fits perfectly with the hash of the previous block to create a complete picture.

Overall, understanding blockchain cryptography is essential for designing secure and reliable blockchain architecture. By using a combination of hashing, public key cryptography, and symmetric cryptography, we can create a tamper-proof and decentralized system that can be used for a variety of applications.