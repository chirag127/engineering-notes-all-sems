### Design Primitives for the notes of the Unit 1 - Introduction to Blockchain in the subject of Block chain Architecture Design

- Design primitives are the basic building blocks of a blockchain system that define its functionality, performance, and security.
- There are three main design primitives: transaction design, consensus design, and block design.
- Transaction design specifies how the data is stored and processed on the blockchain, such as the data format, validation rules, encryption methods, and smart contracts.
- Consensus design determines how the nodes in the network agree on the state of the blockchain, such as the consensus algorithm, the incentive mechanism, and the fault tolerance.
- Block design defines how the transactions are grouped and linked together, such as the block size, the block interval, the block header, and the hashing function.
- Different design primitives can be combined to create different types of blockchains, such as public, private, permissioned, or hybrid.
- The choice of design primitives depends on the application domain, the security requirements, the scalability challenges, and the user preferences.
- Some examples of design primitives for popular blockchains are:

| Blockchain | Transaction Design | Consensus Design | Block Design |
|------------|--------------------|-------------------|--------------|
| Bitcoin | UTXO model, ECDSA signatures, Script language | Proof-of-Work, Nakamoto consensus, block reward, 51% attack resistance | 1 MB block size, 10 min block interval, block header with nonce, SHA-256 hashing function |
| Ethereum | Account model, ECDSA signatures, Solidity language | Proof-of-Work (transitioning to Proof-of-Stake), Nakamoto consensus, block reward, gas fee, uncle blocks | Variable block size, 15 sec block interval, block header with nonce and mixhash, Keccak-256 hashing function |
| Hyperledger Fabric | Key-value store, X.509 certificates, chaincode | Practical Byzantine Fault Tolerance, endorsement policy, ordering service, channel | Variable block size, variable block interval, block header with previous hash and metadata, SHA-256 hashing function |

: BlockChain.pptx | Abdul-Hakam Shafi Botros Abdul-Hakam - Academia.edu
: What is Cryptographic Primitive in Blockchain? - GeeksforGeeks
: Cryptographic primitives in blockchains - ScienceDirect
: The principles of designing for blockchain - InVision