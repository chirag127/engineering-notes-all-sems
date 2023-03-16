### Basic crypto primitives for the notes of the Unit 1 - Introduction to Blockchain in the subject of Block chain Architecture Design

Cryptographic primitives are the basic building blocks for the development of security protocols. They are an integral part of the blockchain because they provide security, privacy, and integrity for the transactions and data stored in the distributed ledger. Some of the common cryptographic primitives used in blockchain are:

- **Hash functions**: A hash function is a mathematical function that maps data of arbitrary size to a fixed-size output, called a hash or a digest. A hash function has the following properties :
  - It is easy to compute the hash for any given input, but hard to find an input that produces a given hash (one-way property).
  - It is hard to find two different inputs that produce the same hash (collision resistance property).
  - A small change in the input results in a large change in the output (avalanche effect property).
- Hash functions are used in blockchain for various purposes, such as:
  - Generating unique identifiers for transactions and blocks.
  - Creating digital fingerprints for data and documents.
  - Implementing proof-of-work consensus algorithms, such as SHA-256, SHA-512, and Ethash .
  - Constructing Merkle trees, which are data structures that allow efficient verification of large sets of data.
- **Digital signatures**: A digital signature is a cryptographic technique that allows a sender to prove the authenticity and integrity of a message to a receiver. A digital signature scheme consists of three algorithms:
  - A key generation algorithm that produces a pair of keys: a private key and a public key.
  - A signing algorithm that takes a message and a private key as inputs and produces a signature as output.
  - A verification algorithm that takes a message, a signature, and a public key as inputs and outputs either true or false, indicating whether the signature is valid or not.
- Digital signatures are used in blockchain for various purposes, such as:
  - Signing transactions and blocks to ensure their origin and validity.
  - Implementing public-key cryptography, which allows secure communication and authentication between parties.
  - Supporting various cryptographic protocols, such as encryption, zero-knowledge proofs, and multi-signatures.
  - The most common digital signature scheme used in blockchain is the Elliptic Curve Digital Signature Algorithm (ECDSA) .
- **Encryption**: Encryption is a cryptographic technique that allows a sender to transform a message into an unreadable form, called a ciphertext, using a secret key. Only the receiver who knows the corresponding secret key can decrypt the ciphertext and recover the original message. Encryption has the following properties:
  - It provides confidentiality, meaning that only the intended receiver can access the message.
  - It provides integrity, meaning that the message cannot be modified or tampered with during transmission.
  - It provides non-repudiation, meaning that the sender cannot deny sending the message.
- Encryption is used in blockchain for various purposes, such as:
  - Protecting sensitive or personal data from unauthorized access or disclosure.
  - Enabling secure and private communication between parties.
  - Supporting various cryptographic protocols, such as zero-knowledge proofs, homomorphic encryption, and secret sharing.
  - There are two main types of encryption schemes used in blockchain: symmetric-key encryption and asymmetric-key encryption.
  - Symmetric-key encryption uses the same key for both encryption and decryption, such as AES and DES.
  - Asymmetric-key encryption uses different keys for encryption and decryption, such as RSA and ECC.