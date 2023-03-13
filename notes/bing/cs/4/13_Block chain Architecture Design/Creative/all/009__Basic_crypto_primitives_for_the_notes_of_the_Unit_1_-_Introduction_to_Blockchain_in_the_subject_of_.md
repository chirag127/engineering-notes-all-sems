### Basic crypto primitives for the notes of the Unit 1 - Introduction to Blockchain in the subject of Block chain Architecture Design

Cryptographic primitives are the basic building blocks for the development of security protocols. They are the low-level algorithms that are used to build cryptographic systems. Cryptographic primitives are essential for blockchain because they provide security, privacy, and integrity for the transactions and data stored in the distributed ledger. Some of the common cryptographic primitives used in blockchain are:

- **Hash functions**: A hash function is a mathematical function that maps data of arbitrary size to a fixed-size output, called a hash or a digest. A hash function has the following properties :
  - It is easy to compute the hash for any given input, but hard to find an input that produces a given hash (one-way property).
  - It is hard to find two different inputs that produce the same hash (collision resistance property).
  - A small change in the input results in a large change in the hash (avalanche effect property).
- Hash functions are used in blockchain for various purposes, such as:
  - Generating unique identifiers for transactions and blocks.
  - Creating digital fingerprints for data and documents.
  - Building Merkle trees for efficient verification and storage of data.
  - Implementing proof-of-work consensus algorithms for validating transactions and securing the network.
  - Some of the hash functions used in blockchain are SHA-256, SHA-512, and Ethash.

- **Digital signatures**: A digital signature is a cryptographic technique that allows a sender to sign a message with a private key, and a receiver to verify the signature with a public key. A digital signature has the following properties :
  - It is easy for the sender to generate a signature for any given message, but hard for anyone else to forge a signature without knowing the private key (unforgeability property).
  - It is easy for the receiver to verify the signature with the public key, but hard for anyone else to verify the signature without knowing the public key (non-repudiation property).
  - It is hard for the sender to generate a signature for a different message that matches the signature for the original message (message integrity property).
- Digital signatures are used in blockchain for various purposes, such as:
  - Authenticating the identity and ownership of the sender of a transaction.
  - Ensuring the integrity and non-repudiation of the transaction data.
  - Enabling multisignature transactions that require multiple parties to sign a transaction.
  - Some of the digital signature schemes used in blockchain are Elliptic Curve Digital Signature Algorithm (ECDSA), Schnorr signatures, and BLS signatures .

- **Encryption**: Encryption is a cryptographic technique that allows a sender to encrypt a message with a key, and a receiver to decrypt the message with the same or a different key. Encryption has the following properties :
  - It is easy for the sender to encrypt a message with a key, but hard for anyone else to decrypt the message without knowing the key (confidentiality property).
  - It is easy for the receiver to decrypt the message with the key, but hard for anyone else to encrypt a message that matches the encrypted message without knowing the key (authenticity property).
  - It is hard for anyone to modify the encrypted message without being detected (integrity property).
- Encryption is used in blockchain for various purposes, such as:
  - Protecting the privacy and confidentiality of the transaction data and the user identity.
  - Enabling secure communication and data exchange between nodes and peers in the network.
  - Implementing zero-knowledge proofs and other advanced cryptographic protocols for enhancing the security and scalability of the blockchain.
  - Some of the encryption schemes used in blockchain are symmetric-key encryption, asymmetric-key encryption, and homomorphic encryption .

: Basics of Cryptographic Primitives for Blockchain Development, https://link.springer.com/chapter/10.1007/978-981-19-1488-1_4
: What is Cryptographic Primitive in Blockchain? - GeeksforGeeks, https://www.geeksforgeeks.org/what-is-cryptographic-primitive-in-blockchain/
: Cryptographic primitives in blockchains - ScienceDirect, https://www.sciencedirect.com/science/article/pii/S108480451830362X