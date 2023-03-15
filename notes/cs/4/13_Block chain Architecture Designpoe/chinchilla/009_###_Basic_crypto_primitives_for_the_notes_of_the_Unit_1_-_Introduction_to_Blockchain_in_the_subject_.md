### Basic crypto primitives for the notes of the Unit 1 - Introduction to Blockchain in the subject of Block chain Architecture Design

Cryptography is a crucial aspect of blockchain technology. It provides secure and private communication, integrity of data, and authentication of transactions. In this unit, we will discuss the basic crypto primitives used in blockchain technology.

1. Hash functions: 
   - A hash function is a mathematical function that takes an input and produces a fixed-sized output called a hash value. 
   - The hash function is a one-way function, which means that given an input, it is easy to compute the hash value, but given the hash value, it is almost impossible to compute the original input. 
   - Hash functions are used in blockchain technology to create unique digital fingerprints of data, such as transactions, blocks, and addresses. 
   - Examples of hash functions are SHA-256, RIPEMD-160, and Keccak-256.

2. Public-key cryptography: 
   - Public-key cryptography, also known as asymmetric cryptography, is a cryptographic system that uses a pair of keys, a public key, and a private key, to encrypt and decrypt messages. 
   - The public key is used to encrypt messages, and the private key is used to decrypt messages. 
   - Public-key cryptography is used in blockchain technology to create digital signatures, which are used to authenticate transactions and ensure the integrity of the blockchain. 
   - Examples of public-key cryptography algorithms are RSA, DSA, and ECDSA.

3. Digital signatures: 
   - A digital signature is a mathematical scheme for verifying the authenticity of digital messages or documents. 
   - Digital signatures are created using a combination of a private key and a hash function. 
   - The private key is used to sign the message, and the public key is used to verify the signature. 
   - Digital signatures are used in blockchain technology to ensure the authenticity of transactions and prevent tampering. 
   - Examples of digital signature schemes are ECDSA and RSA.

4. Merkle trees: 
   - A Merkle tree, also known as a hash tree, is a tree in which every leaf node is labeled with the hash of a data block, and every non-leaf node is labeled with the hash of the labels of its child nodes. 
   - Merkle trees are used in blockchain technology to efficiently verify the integrity of large data structures, such as the blockchain. 
   - By verifying the hash of a single node, the entire tree can be verified. 
   - This reduces the amount of data that needs to be transmitted and stored, making the blockchain more efficient. 

5. Consensus algorithms: 
   - Consensus algorithms are used in blockchain technology to ensure that all nodes in the network agree on the current state of the blockchain. 
   - Consensus algorithms use a variety of techniques, such as proof-of-work, proof-of-stake, and Byzantine fault tolerance, to ensure that the blockchain is secure and tamper-proof. 
   - Examples of consensus algorithms are Bitcoin's proof-of-work, Ethereum's proof-of-stake, and Ripple's Byzantine fault tolerance.

Learning tricks:
- Mnemonic for the basic crypto primitives: H - P - D - M - C (Hash functions, Public-key cryptography, Digital signatures, Merkle trees, Consensus algorithms)
- To remember the purpose of digital signatures, think of the signature on a physical document. Just as a signature on a physical document verifies the authenticity of the signed document, a digital signature verifies the authenticity of a digital message or document. 

In conclusion, understanding the basic crypto primitives used in blockchain technology is essential for designing and implementing secure and efficient blockchain systems. Hash functions, public-key cryptography, digital signatures, Merkle trees, and consensus algorithms are the building blocks of blockchain technology, and a solid understanding of these concepts is crucial for success in the field.