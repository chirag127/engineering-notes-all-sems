 Here is the content in markdown format for the topic ### Basic crypto primitives for the notes of the Unit 1 - Introduction to Blockchain in the subject of Block chain Architecture Design:

### Basic crypto primitives

The basic cryptographic primitives used in blockchain are:

1. Hash functions:
- Produces a fixed-size hash value from a variable-sized input
- Deterministic - same input always produces the same hash
- Collision resistant - infeasible to find two inputs that hash to the same value
- Used for data integrity (detect changes) and proof-of-work
- Examples: SHA-256, RIPEMD-160, etc.

Mnemonics:
- Star Wars (SHA): May the hash be with you!
- RIPEd (RIPEMD): Data goes in, hash comes out - you can't explain that!

2. Digital signatures:
- Uses public-key cryptography to prove identity and validate messages/transactions
- Uses a private key to sign and a public key to verify
- Should be non-repudiable (cannot deny sending the message/transaction)
- Examples: ECDSA, DSA, RSA, etc.

3. Symmetric-key cryptography:
- Uses a single key to encrypt and decrypt
- Fast but key exchange is a challenge
- Examples: AES, DES, 3DES, Blowfish, etc.
- Used for encrypting blockchain data

4. Asymmetric (public-key) cryptography:
- Uses a public/private key pair
- Public key used to encrypt data and verify signatures
- Private key used to decrypt and sign data
- Examples: RSA, ECC, etc.
- Used for blockchain key exchange and digital signatures

Advantages, disadvantages, applications, examples, and diagrams can be included for each of the points if required. The content can be made more formal by changing phrases like 'used for' to 'utilized for the purpose of' etc. Mnemonics and learning tricks can be included if easy to remember.