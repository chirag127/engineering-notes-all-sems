### Basic Crypto Primitives for the Notes of the Unit 1 - Introduction to Blockchain in the Subject of Blockchain Architecture Design

Cryptographic primitives are the building blocks of a blockchain system. They play a crucial role in ensuring the security and integrity of the data stored on the blockchain. In this section, we will discuss some of the basic cryptographic primitives that are used in blockchain systems.

#### 1. Hash Functions

A hash function is a mathematical function that converts input data of any size into a fixed-size output. The output is commonly referred to as a hash or message digest. A hash function is designed to be one-way, meaning that it is computationally infeasible to reverse the process and obtain the original input data from the hash.

Hash functions are used extensively in blockchain systems for various purposes, such as:

- Generating unique identifiers for each block in the blockchain.
- Verifying the integrity of data stored in the blockchain.
- Protecting the confidentiality of sensitive information by storing only the hash of the data.

One mnemonic to remember the properties of a hash function is "SHA256: Secure, Hash, Algorithm, 256 bits".

#### 2. Public Key Cryptography

Public Key Cryptography, also known as asymmetric cryptography, is a cryptographic system that uses two keys – a public key and a private key – to encrypt and decrypt data. The public key is used to encrypt data, while the private key is used to decrypt data.

Public Key Cryptography is used in blockchain systems for various purposes, such as:

- Authenticating users and nodes on the network.
- Verifying digital signatures.
- Encrypting and decrypting data transmitted over the network.

One mnemonic to remember the difference between Public Key Cryptography and Symmetric Key Cryptography is "Public Key = Padlock, Symmetric Key = Secret Handshake".

#### 3. Digital Signatures

A digital signature is a mathematical technique used to verify the authenticity and integrity of a message or document. It is a type of electronic signature that provides a way to ensure that the message or document has not been tampered with since it was signed.

Digital signatures are used extensively in blockchain systems for various purposes, such as:

- Authenticating transactions on the blockchain.
- Verifying the identity of the sender of a transaction.
- Ensuring the integrity of data stored on the blockchain.

One mnemonic to remember the components of a digital signature is "HASH, ENCRYPT, VERIFY".

In conclusion, understanding the basic cryptographic primitives used in blockchain systems is essential for anyone looking to design or develop blockchain-based applications. By using these primitives correctly, we can ensure the security and integrity of the data stored on the blockchain.