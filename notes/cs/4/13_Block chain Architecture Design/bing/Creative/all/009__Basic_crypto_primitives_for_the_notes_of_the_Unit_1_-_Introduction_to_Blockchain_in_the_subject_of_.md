### Basic crypto primitives for the notes of the Unit 1 - Introduction to Blockchain in the subject of Block chain Architecture Design

Cryptographic primitives are well-established, low-level cryptographic algorithms that are frequently used to build cryptographic protocols for computer security systems. They are the basic building blocks of the cryptosystem. The programmers develop new cryptographic algorithms with the help of cryptographic primitives. Cryptographic primitives are similar in some ways to programming languages. A computer programmer rarely invents a new programming language while writing a new program; instead, they will use one of the already established programming languages to program in.

Below are some of the common cryptographic primitives:

- **One way Hash Functions**: It is a mathematical function used to encrypt variable length data to fixed binary data. It is a one-way function, meaning that it is easy to compute the output given the input, but hard to find the input given the output. One way hash functions are used for data integrity, authentication, digital signatures, proof of work, etc. Examples of one way hash functions are SHA-256, SHA-512, and Ethash.

- **Symmetric Key cryptography**: This is also known as Symmetric Encryption. It is a method of encryption where the same key is used for both encryption and decryption. Symmetric key cryptography is used for data confidentiality, encryption, and decryption. Examples of symmetric key cryptography are AES, DES, and RC4.

- **Asymmetric key cryptography**: It is also known as public key cryptography. It is a method of encryption where two different keys are used for encryption and decryption. One key is public and can be shared with anyone, while the other key is private and kept secret. Asymmetric key cryptography is used for data confidentiality, encryption, decryption, digital signatures, key exchange, etc. Examples of asymmetric key cryptography are RSA, ECC, and ElGamal.

- **Randomized Algorithms**: These algorithms produce random ciphertexts for encryption. They use a random number generator to generate a random key or a random nonce (a number used only once) to encrypt the plaintext. Randomized algorithms are used for data confidentiality, encryption, and decryption. Examples of randomized algorithms are CTR, CBC, and GCM.

- **Digital Signature**: It is a cryptographic technique that allows a sender to sign a message with their private key, and a receiver to verify the signature with the sender's public key. Digital signature is used for data integrity, authentication, non-repudiation, etc. Examples of digital signature are ECDSA, RSA, and DSA.

Some mnemonics and learning tricks for the basic crypto primitives are:

- **One way Hash Functions**: Remember the acronym **HIDE** - Hash functions are used to **H**ash, **I**ntegrity, **D**igital signatures, and **E**ncryption.
- **Symmetric Key cryptography**: Remember the acronym **SEE** - Symmetric encryption uses the **S**ame key to **E**ncrypt and d**E**crypt.
- **Asymmetric key cryptography**: Remember the acronym **APE** - Asymmetric encryption uses **A** different key to **P**ublicly **E**ncrypt and privately decrypt.
- **Randomized Algorithms**: Remember the acronym **RACE** - Randomized algorithms use **R**andom numbers to **A**dd **C**onfidentiality and **E**ntropy.
- **Digital Signature**: Remember the acronym **SAND** - Digital signature uses **S**igning, **A**uthentication, **N**on-repudiation, and **D**ecryption.