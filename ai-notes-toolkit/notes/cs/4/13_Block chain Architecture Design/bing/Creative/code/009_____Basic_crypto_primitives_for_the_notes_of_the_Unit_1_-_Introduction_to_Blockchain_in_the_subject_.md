### Basic crypto primitives for the notes of the Unit 1 - Introduction to Blockchain in the subject of Block chain Architecture Design

Cryptographic primitives are the basic building blocks for the development of security protocols. They are an integral part of the blockchain because they provide security, privacy, and integrity for the transactions and data stored in the distributed ledger. Some of the common cryptographic primitives used in blockchain are:

- **Hash functions**: A hash function is a mathematical function that maps data of arbitrary size to a fixed-size output, called a hash or a digest. A hash function has the following properties :
  - It is easy to compute the hash from the input, but hard to find the input from the hash (one-way property).
  - It is hard to find two different inputs that produce the same hash (collision resistance property).
  - A small change in the input results in a large change in the hash (avalanche effect property).
- Hash functions are used in blockchain for various purposes, such as:
  - Generating unique identifiers for transactions and blocks.
  - Creating digital fingerprints for data and documents.
  - Implementing proof-of-work consensus algorithms, such as SHA-256, SHA-512, and Ethash .
  - Ensuring the integrity and immutability of the blockchain.

- **Digital signatures**: A digital signature is a cryptographic technique that allows a sender to sign a message with a private key, and a receiver to verify the signature with a public key. A digital signature has the following properties :
  - It is easy to generate a signature from the message and the private key, but hard to forge a signature without the private key (unforgeability property).
  - It is easy to verify a signature with the message and the public key, but hard to verify a signature without the message or the public key (verifiability property).
  - It is hard to find two different messages that produce the same signature with the same private key (uniqueness property).
- Digital signatures are used in blockchain for various purposes, such as:
  - Authenticating the sender and the receiver of a transaction.
  - Ensuring the non-repudiation and accountability of the transaction.
  - Implementing public-key cryptography schemes, such as Elliptic Curve Digital Signature Algorithm (ECDSA), which is the current signature scheme in Bitcoin .

- **Encryption**: Encryption is a cryptographic technique that allows a sender to transform a message into a ciphertext with a key, and a receiver to recover the message from the ciphertext with the same or a different key. Encryption has the following properties :
  - It is easy to encrypt the message with the key, but hard to decrypt the ciphertext without the key (confidentiality property).
  - It is hard to modify the ciphertext without affecting the decryption (integrity property).
  - It is hard to infer any information about the message from the ciphertext (indistinguishability property).
- Encryption is used in blockchain for various purposes, such as:
  - Protecting the privacy and confidentiality of the transaction data and the user identities.
  - Implementing symmetric-key cryptography or asymmetric-key cryptography schemes, such as Advanced Encryption Standard (AES), RSA, or Elliptic Curve Cryptography (ECC) .
  - Enabling secure communication and data exchange between the nodes in the network.