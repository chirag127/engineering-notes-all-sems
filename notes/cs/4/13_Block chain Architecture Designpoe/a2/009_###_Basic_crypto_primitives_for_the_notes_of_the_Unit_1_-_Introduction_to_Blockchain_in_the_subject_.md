 Here is the content in markdown format for the topic ### Basic crypto primitives for the notes of the Unit 1 - Introduction to Blockchain in the subject of Block chain Architecture Design:

### Basic crypto primitives

The basic cryptographic primitives used in blockchain are:

- Hash functions: Produce a fixed-size hash value from a variable size input. Used for generating blockchain proof-of-work, consensus algorithm, etc. Example: SHA-256.
- Digital signatures: Used to sign transactions. Uses public key cryptography. Example: ECDSA.
- symmetric-key cryptography: Uses a single key to encrypt and decrypt data. Fast but key sharing is a problem. Example: AES.
- Public-key cryptography: Uses two keys - public and private. Public key is shared, private key is kept secret. Used for digital signatures and encryption. Example: RSA, ECC.

Advantages:

- Hash functions: Fast, determnistic, non-malleable (can't be modified), pseudo-random output.
- Digital signatures: Authentication, non-repudiation (can't deny signed data).
- Symmetric-key crypto: Fast, small key sizes (less data to transmit/store).
- Public-key crypto: Secure key distribution (public key can be shared).

Disadvantages:

- Hash functions: Vulnerable to length-extension and collision attacks.
- Symmetric-key crypto: Key distribution problem (how to share secret key securely).
- Public-key crypto: Slow, large key sizes (more data to transmit/store).

Applications:

- Bitcoin uses SHA-256 for proof-of-work and transaction/block hashing.
- ECDSA is used for digital signatures in Bitcoin.
- AES is used for encrypting/decrypting keys and wallet data.

Mnemonics:

- Never roll your own crypto. Use standard and vetted algorithms.
- Select algorithms based on requirements - speed vs security.
- Combine primitives to get advantages of each (eg. use symmetric-key crypto for data, public-key crypto for key distribution).