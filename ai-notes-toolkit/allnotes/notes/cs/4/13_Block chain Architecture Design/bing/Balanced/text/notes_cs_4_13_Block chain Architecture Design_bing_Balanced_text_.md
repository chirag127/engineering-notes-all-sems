

## Unit 1 - Introduction to Blockchain

- Blockchain is a distributed ledger technology that allows multiple parties to share and verify data without relying on a central authority or intermediary.
- Blockchain consists of a network of nodes that communicate and reach consensus on the state of the ledger, which is composed of blocks that store transactions or other data.
- Blockchain has several features that make it suitable for various applications, such as:
  - **Immutability**: Once a block is added to the ledger, it cannot be altered or deleted, ensuring data integrity and auditability.
  - **Transparency**: All the transactions or data on the ledger are visible to all the nodes, enabling trust and accountability among the participants.
  - **Security**: Blockchain uses cryptographic techniques to protect the data and the network from unauthorized access or manipulation.
  - **Decentralization**: Blockchain does not depend on a single entity or point of failure, enhancing its resilience and availability.
- Blockchain can be classified into different types based on the level of access and governance, such as:
  - **Public blockchain**: Anyone can join and participate in the network, and the consensus is achieved by a majority of nodes. Examples are Bitcoin and Ethereum.
  - **Private blockchain**: Only authorized entities can join and participate in the network, and the consensus is achieved by a predefined set of nodes. Examples are Hyperledger Fabric and Corda.
  - **Consortium blockchain**: A group of entities can join and participate in the network, and the consensus is achieved by a subset of nodes. Examples are Quorum and R3.
- Blockchain can also be classified into different types based on the underlying data structure and consensus mechanism, such as:
  - **Chain-based blockchain**: The ledger is organized as a linear chain of blocks, and the consensus is achieved by a proof-of-work or proof-of-stake algorithm. Examples are Bitcoin and Ethereum.
  - **DAG-based blockchain**: The ledger is organized as a directed acyclic graph (DAG) of blocks, and the consensus is achieved by a voting or reputation system. Examples are IOTA and Nano.
  - **Hashgraph-based blockchain**: The ledger is organized as a hashgraph of events, and the consensus is achieved by a gossip protocol and virtual voting. Examples are Hedera Hashgraph and Swirlds.



### Digital Money to Distributed Ledgers

- Digital money is a form of electronic money that can be used to store, transfer, and exchange value digitally, without the need for physical cash or intermediaries.
- Digital money can be classified into two types: centralized and decentralized. Centralized digital money is issued and controlled by a single authority, such as a central bank or a private company. Decentralized digital money is created and managed by a network of users, without a central authority or intermediary.
- Decentralized digital money is also known as cryptocurrency, which is a subset of digital currency that uses cryptography to secure transactions and prevent double-spending. Cryptography is the science of encoding and decoding information using mathematical techniques.
- Cryptocurrency relies on a distributed ledger, which is a shared database that records transactions and balances of digital money across a network of nodes. A node is a computer or device that participates in the network by validating and storing transactions. A distributed ledger can also be referred to as a blockchain, which is a specific type of distributed ledger that organizes transactions into blocks and links them together using cryptographic hashes. A hash is a unique fingerprint of data that can be used to verify its integrity and authenticity.
- A distributed ledger enables a decentralized payment system, where users can transact directly with each other, without the need for intermediaries or trusted third parties. A distributed ledger also provides transparency, immutability, and security, as transactions are publicly visible, verified by consensus, and resistant to tampering or fraud.
- The first and most well-known cryptocurrency that uses a distributed ledger is Bitcoin, which was launched in 2009 by an anonymous person or group using the pseudonym Satoshi Nakamoto. Bitcoin was designed to solve the problem of double-spending in a decentralized way, by using a proof-of-work mechanism to create and validate blocks. Proof-of-work is a process that requires nodes to solve complex mathematical puzzles to create new blocks and earn rewards in the form of bitcoins. The difficulty of the puzzles adjusts dynamically to maintain a constant rate of block creation and ensure the security of the network.
- Since the inception of Bitcoin, many other cryptocurrencies and distributed ledger platforms have emerged, offering different features, functionalities, and applications. Some examples are Ethereum, Ripple, Litecoin, Stellar, and Hyperledger. These platforms can support not only digital money, but also smart contracts, tokens, digital assets, and decentralized applications. Smart contracts are self-executing agreements that are encoded on the distributed ledger and executed automatically when certain conditions are met. Tokens are digital representations of value or utility that can be issued and exchanged on the distributed ledger. Digital assets are any form of data or information that can be stored, transferred, and verified on the distributed ledger. Decentralized applications are software programs that run on the distributed ledger and provide various services or functions to users.
- Distributed ledger technology (DLT) is the general term that encompasses the concepts, protocols, and architectures of distributed ledgers and their applications. DLT has the potential to transform various sectors and industries, such as finance, trade, supply chain, health, education, and governance, by enabling more efficient, resilient, and reliable systems and processes. DLT also poses various challenges and risks, such as scalability, interoperability, regulation, privacy, and security, that need to be addressed and overcome.



### Design Primitives for the notes of the Unit 1 - Introduction to Blockchain in the subject of Block chain Architecture Design

Design primitives are the basic elements or components that are used to construct a blockchain system. They can be categorized into three types: transaction design, consensus design and block design.

- Transaction design refers to how the data or information is structured, validated and recorded on the blockchain. It includes aspects such as the format of transactions, the types of transactions, the cryptographic primitives used to secure transactions, the scripting language used to express transaction logic, and the incentives or fees associated with transactions.
- Consensus design refers to how the nodes or participants of the blockchain network agree on the state or history of the blockchain. It includes aspects such as the consensus algorithm, the consensus rules, the consensus protocol, the network topology, the fault tolerance, and the scalability of the consensus mechanism.
- Block design refers to how the transactions are grouped, linked and stored on the blockchain. It includes aspects such as the block size, the block interval, the block header, the block hash, the block reward, and the block difficulty.

These design primitives can be combined and customized to create different types of blockchains, such as public, private, permissioned, permissionless, hybrid, federated, etc. Each type of blockchain has its own advantages and disadvantages, depending on the application domain and the requirements of the users. Some examples of blockchain applications are cryptocurrencies, smart contracts, supply chain management, digital identity, voting systems, etc.



### Protocols for the notes of the Unit 1 - Introduction to Blockchain in the subject of Block chain Architecture Design

- A blockchain protocol is a set of underlying rules that define how a blockchain will work.
- A blockchain protocol specifies the interface of the network, the interaction between the computers, the incentives, the kind of data, and the consensus methods.
- A blockchain protocol aims to address the four principles of blockchain: decentralization, transparency, immutability, and security.
- There are different types of blockchain protocols, such as:
  - Hyperledger: an open-source framework that is developed by Linux. It helps the enterprises to provide solutions for various industries, such as finance, healthcare, supply chain, etc. It uses a modular architecture and supports various consensus algorithms, such as PBFT, Raft, Kafka, etc.
  - Quorum: an enterprise blockchain protocol that aims to address the problems related to finance. It is based on Ethereum and supports smart contracts and private transactions. It uses a voting-based consensus algorithm, such as Istanbul BFT, or a proof-of-authority algorithm, such as Clique.
  - Bitcoin: the first and most popular blockchain protocol that enables peer-to-peer transactions of digital currency. It uses a proof-of-work consensus algorithm, which requires miners to solve complex mathematical problems and validate transactions. It has a limited supply of 21 million coins and a fixed block time of 10 minutes.
  - Ethereum: a blockchain protocol that enables the creation and execution of smart contracts and decentralized applications. It uses a proof-of-work consensus algorithm, but plans to transition to a proof-of-stake algorithm, which requires validators to stake their coins and validate transactions. It has a native currency called Ether and a variable block time of around 15 seconds.
  - Cardano: a blockchain protocol that aims to provide a scalable, secure, and sustainable platform for smart contracts and decentralized applications. It uses a proof-of-stake consensus algorithm, called Ouroboros, which divides the network into epochs and slots and elects slot leaders and validators. It has a native currency called ADA and a fixed block time of 20 seconds.
- A blockchain protocol can be classified into three categories, based on the level of access and participation: public, private, and hybrid.
  - Public blockchain protocols are open and permissionless, meaning anyone can join and participate in the network without any restriction. They are transparent and immutable, but they may suffer from scalability and privacy issues. Examples of public blockchain protocols are Bitcoin, Ethereum, and Cardano.
  - Private blockchain protocols are closed and permissioned, meaning only authorized entities can join and participate in the network. They are more scalable and private, but they may compromise on decentralization and security. Examples of private blockchain protocols are Hyperledger and Quorum.
  - Hybrid blockchain protocols are a combination of public and private blockchain protocols, meaning they have both public and private components. They aim to balance the trade-offs between scalability, privacy, decentralization, and security. Examples of hybrid blockchain protocols are Corda and Dragonchain.



### Security for the notes of the Unit 1 - Introduction to Blockchain in the subject of Blockchain Architecture Design

- Blockchain is a distributed database of records of all transactions or digital events that have been executed and shared among participating parties.
- Blockchain uses advanced cryptography to ensure that the information is locked inside the blockchain and only authorized parties can access it.
- Blockchain also uses decentralization and consensus to ensure trust in transactions, as each party holds a copy of the original chain and can verify the validity of the data.
- Blockchain security is about understanding the risks and threats to the blockchain network and managing them with appropriate controls and measures.
- Blockchain security can be divided into three layers: Layer 0, Layer 1, and Layer 2.
  - Layer 0 is the underlying network infrastructure that supports the blockchain, such as the internet, routers, servers, etc. It is vulnerable to attacks such as denial-of-service, spoofing, or hijacking.
  - Layer 1 is the core protocol of the blockchain, such as the consensus algorithm, the cryptographic primitives, the data structure, etc. It is vulnerable to attacks such as double-spending, 51% attack, or selfish mining.
  - Layer 2 is the application layer that runs on top of the blockchain, such as smart contracts, decentralized applications, oracles, etc. It is vulnerable to attacks such as reentrancy, front-running, or logic bugs.
- Blockchain security requires a holistic approach that considers all the layers and the interactions among them. It also requires a trade-off between security, scalability, and other desirable features of the blockchain.
- Blockchain security is an evolving and dynamic field that requires constant research and innovation to cope with new challenges and opportunities.



### Consensus for the notes of the Unit 1 - Introduction to Blockchain in the subject of Block chain Architecture Design

- Consensus is the process by which a group of peers – or nodes – on a network determine which blockchain transactions are valid and which are not.
- Consensus mechanisms are the methodologies used to achieve this agreement. They are sets of rules that help to protect networks from malicious behaviour and hacking attacks.
- Consensus mechanisms are essential for blockchain systems to achieve distributed agreement about the ledger's state, which is the record of all transactions and data on the network.
- Consensus mechanisms also ensure the reliability and trust of the blockchain network, as well as its environmental security and scalability.
- There are different types of consensus mechanisms, each with its own advantages and disadvantages. Some of the most common ones are:
  - Proof of Work (PoW): This mechanism requires nodes to solve complex mathematical puzzles to validate transactions and create new blocks. The first node to solve the puzzle gets a reward in the form of cryptocurrency. PoW is used by Bitcoin and Ethereum, among others. PoW is secure and decentralized, but it consumes a lot of energy and is prone to congestion.
  - Proof of Stake (PoS): This mechanism assigns nodes a stake, or a portion of cryptocurrency, that they have to lock up as a collateral to participate in the validation process. The higher the stake, the higher the chance of being selected to create a new block and earn a reward. PoS is used by Cardano and Polkadot, among others. PoS is more energy-efficient and scalable than PoW, but it may introduce centralization and security risks.
  - Delegated Proof of Stake (DPoS): This mechanism allows nodes to delegate their stake to a group of validators, who are elected by the network to validate transactions and create new blocks. The validators share the rewards with their delegators. DPoS is used by EOS and Tron, among others. DPoS is faster and more democratic than PoS, but it may also suffer from centralization and corruption.
  - Proof of Authority (PoA) & Proof of Importance (PoI): These mechanisms rely on the reputation and identity of the nodes, rather than their stake or computational power, to validate transactions and create new blocks. PoA is used by VeChain and PoI is used by NEM, among others. PoA and PoI are more efficient and secure than PoW and PoS, but they may also compromise the anonymity and decentralization of the network.



### Permissions for the notes of the Unit 1 - Introduction to Blockchain in the subject of Block chain Architecture Design

- Permissions are the rules that determine who can access, modify, or delete the notes of the Unit 1 - Introduction to Blockchain in the subject of Block chain Architecture Design.
- Permissions can be set by the owner or creator of the notes, or by the administrator of the platform where the notes are stored or shared.
- Permissions can be classified into three types: read, write, and execute.
  - Read permission allows the user to view the content of the notes, but not to edit or delete them.
  - Write permission allows the user to edit or delete the content of the notes, but not to execute them.
  - Execute permission allows the user to run the notes as a program or script, if they contain executable code.
- Permissions can be granted or denied to different users or groups of users, depending on their roles, identities, or affiliations.
  - For example, the owner of the notes can grant read and write permissions to themselves, read permission to their classmates, and no permission to anyone else.
  - Alternatively, the owner of the notes can grant read permission to everyone, write permission to a specific group of collaborators, and execute permission to a trusted instructor.
- Permissions can be enforced by different mechanisms, depending on the platform where the notes are stored or shared.
  - For example, the notes can be stored in a local file system, where the permissions are controlled by the operating system of the device.
  - Alternatively, the notes can be stored in a cloud service, where the permissions are controlled by the service provider or the application interface.
  - Another option is to store the notes in a blockchain, where the permissions are controlled by the consensus protocol and the smart contracts of the network.



### Privacy for the notes of the Unit 1 - Introduction to Blockchain in the subject of Block chain Architecture Design

- Privacy is the ability to control the access and use of one's personal information.
- Privacy in blockchains is rather complicated as it contradicts with some highly praised properties of blockchain such as immutability.
- Immutability is considered a cornerstone of blockchains’ security and, therefore, an indisputable property according to which transactional blockchain data cannot be edited nor deleted.
- However, immutability may pose challenges for privacy compliance, such as the right to be forgotten or the right to rectification under the General Data Protection Regulation (GDPR).
- A key aspect of privacy in blockchains is the use of private and public keys .
- Blockchain systems use asymmetric cryptography to secure transactions between users .
- In these systems, each user has a public and private key .
- These keys are random strings of numbers and are cryptographically related .
- The public key is used to identify the user on the blockchain and to verify the authenticity of the transactions .
- The private key is used to sign the transactions and to prove the ownership of the funds .
- The private key should be kept secret and never shared with anyone .
- If the private key is lost or compromised, the user may lose access to their funds or have their funds stolen by malicious actors .
- Another aspect of privacy in blockchains is the distinction between public and private blockchains.
- Public blockchains (or permissionless blockchains) are open to anyone who wishes to join the network and participate in the consensus process.
- Public blockchains are transparent and decentralized, but they may also expose the transaction history and balances of the users to anyone who can access the blockchain.
- Private blockchains (or permissioned blockchains) are restricted to a predefined set of participants who are authorized to access the network and validate the transactions.
- Private blockchains are more scalable and efficient, but they may also sacrifice some degree of transparency and decentralization.
- Private blockchains may offer more privacy protection to the users, as they can implement access control mechanisms and encryption techniques to limit the visibility of the data .
- However, private blockchains may also introduce more risks of data breaches, corruption, or collusion, as they rely on trusted intermediaries to manage the network and the data .
- Therefore, privacy in blockchains is a trade-off between different design choices and objectives, and it requires careful consideration of the legal, technical, and ethical implications of each option  .



### Blockchain Architecture and Design

- Blockchain is a distributed ledger technology that enables peer-to-peer transactions without intermediaries or central authorities.
- Blockchain architecture consists of the following elements:
  - Nodes: Users or computers that participate in the network and have a copy of the ledger.
  - Blocks: Data structures that store a set of transactions and a reference to the previous block.
  - Transactions: Records or information that are validated and appended to the ledger by consensus mechanisms.
  - Consensus mechanisms: Rules or algorithms that ensure the agreement and integrity of the ledger among the nodes.
  - Smart contracts: Self-executing programs that define and enforce the business logic and rules of the transactions.
- Blockchain architecture design involves selecting the appropriate frameworks and platforms to meet the business objectives and requirements of the application.
- Blockchain architecture design also involves defining the infrastructure and security aspects of the application, such as:
  - Network topology: The structure and configuration of the nodes and their connections.
  - Data storage: The location and format of the data stored on the ledger or off-chain.
  - Identity and access management: The methods and protocols for verifying and controlling the access of the users and nodes.
  - Encryption and hashing: The techniques and standards for securing and verifying the data and transactions.
  - Performance and scalability: The metrics and strategies for measuring and improving the speed and capacity of the application.
  - Governance and compliance: The policies and regulations for managing and auditing the application and its participants.



### Basic crypto primitives for the notes of the Unit 1 - Introduction to Blockchain in the subject of Block chain Architecture Design

- Cryptographic primitives are the low-level algorithms that are used to build cryptographic protocols for a strong secured network.
- They are the basic building blocks of the cryptosystem and the programmers develop new cryptographic algorithms with the help of cryptographic primitives.
- Basic cryptographic primitives include hash functions, digital signatures, symmetric key cryptography, asymmetric key cryptography, and randomized algorithms .
- Hash functions are mathematical functions that map arbitrary length data to fixed length binary data, also known as hashes or digests. They are one-way functions, meaning that it is easy to compute the hash from the input, but hard to find the input from the hash .
- Digital signatures are schemes that allow a sender to sign a message with their private key, and a receiver to verify the signature with the sender's public key. They provide authenticity, integrity, and non-repudiation of the message .
- Symmetric key cryptography is a type of encryption where the same key is used to encrypt and decrypt the message. The key must be shared securely between the sender and the receiver. Examples of symmetric key algorithms are AES, DES, and RC4 .
- Asymmetric key cryptography, also known as public key cryptography, is a type of encryption where different keys are used to encrypt and decrypt the message. The sender uses the receiver's public key to encrypt the message, and the receiver uses their own private key to decrypt it. The public key can be shared openly, while the private key must be kept secret. Examples of asymmetric key algorithms are RSA, ECC, and ElGamal .
- Randomized algorithms are algorithms that produce random ciphertexts for encryption. They add randomness to the input or the key to make the encryption more secure and unpredictable. Examples of randomized algorithms are OAEP, CTR, and CBC .



### Hash for the notes of the Unit 1 - Introduction to Blockchain in the subject of Block chain Architecture Design

- A hash is a function that converts any data form into a unique text string of a fixed length .
- A hash is also called a digest, a fingerprint, or a checksum of the data.
- A hash has the following properties  :
  - It is deterministic, meaning that the same input data will always produce the same hash value.
  - It is one-way, meaning that it is easy to compute the hash from the input data, but hard to find the input data from the hash.
  - It is collision-resistant, meaning that it is very unlikely that two different input data will produce the same hash value.
- Hashes are used in several parts of a blockchain system :
  - Each block header contains the previous block's hash, which ensures that nothing has been tampered with as new blocks are added.
  - Cryptocurrency blockchains use hashes to secure information and make the ledger immutable.
  - Miners create new blocks by finding a hash that meets a certain difficulty criterion, which is called proof-of-work.
  - Transactions are hashed and grouped into a data structure called a Merkle tree, which allows for efficient verification of the transactions.
- The most common hash algorithm used in blockchain is SHA-256 or Secure Hashing Algorithm 256 bits.
  - SHA-256 takes any input data and produces a 256-bit (32-byte) hash value, which is usually represented as a 64-digit hexadecimal number.
  - SHA-256 is considered to be a secure and reliable hash algorithm, as no collisions or vulnerabilities have been found so far.
  - SHA-256 is also used in other cryptographic applications, such as digital signatures, encryption, and authentication.



### Signature for the notes of the Unit 1 - Introduction to Blockchain in the subject of Block chain Architecture Design

- A signature is a way of verifying the authenticity and integrity of a message or document.
- A signature can be digital or physical, depending on the medium and the context of the message or document.
- A digital signature is a mathematical scheme that uses cryptographic algorithms to generate and verify a signature.
- A digital signature consists of two parts: a private key and a public key.
- A private key is a secret value that only the signer knows and uses to generate a signature.
- A public key is a value that is derived from the private key and is publicly available to anyone who wants to verify a signature.
- A signature is generated by applying a signing algorithm to the message or document and the private key, resulting in a signature value.
- A signature is verified by applying a verification algorithm to the message or document, the signature value, and the public key, resulting in a boolean value that indicates whether the signature is valid or not.
- A digital signature provides two main properties: authentication and non-repudiation.
- Authentication means that the signature proves that the message or document was signed by the owner of the private key, and not by anyone else.
- Non-repudiation means that the signer cannot deny having signed the message or document, since only they know the private key.
- A digital signature can also provide a third property: integrity, which means that the signature proves that the message or document was not altered after being signed.
- A digital signature can be used for various purposes, such as securing online transactions, verifying software updates, signing contracts, and certifying documents.
- A blockchain is a distributed ledger that records transactions or events in a secure and verifiable way.
- A blockchain consists of a series of blocks that are linked together by cryptographic hashes.
- A block contains a header and a body. The header contains metadata, such as the block number, the timestamp, the previous block hash, and the nonce. The body contains the transactions or events that are recorded in the block.
- A hash is a fixed-length value that is computed from an arbitrary input using a hash function. A hash function is a mathematical function that maps any input to a unique output, such that it is easy to compute the output from the input, but hard to compute the input from the output, or to find two different inputs that produce the same output.
- A nonce is a random value that is used to vary the input of the hash function, in order to produce a hash that satisfies a certain condition, such as having a certain number of leading zeros. This condition is called the difficulty, and it determines how hard it is to find a valid nonce for a given block.
- The process of finding a valid nonce for a block is called mining, and it requires a lot of computational power and energy. The first miner who finds a valid nonce for a block is rewarded with some cryptocurrency, such as Bitcoin or Ethereum.
- The previous block hash is a hash of the header of the previous block in the blockchain. It serves as a link that connects the blocks together, and ensures that the blocks are in a chronological order.
- The blockchain is maintained by a network of nodes that communicate with each other using a peer-to-peer protocol. A node is a computer that runs the blockchain software and stores a copy of the blockchain.
- The nodes follow a consensus mechanism to agree on the state of the blockchain and to validate new blocks. A consensus mechanism is a set of rules or algorithms that determine how the nodes reach a common agreement on the blockchain data.
- There are different types of consensus mechanisms, such as proof-of-work, proof-of-stake, proof-of-authority, and proof-of-elapsed-time. Each consensus mechanism has its own advantages and disadvantages, such as security, scalability, efficiency, and decentralization.
- A blockchain can be public or private, depending on who can access and participate in the network. A public blockchain is open to anyone who wants to join the network and verify the transactions or events. A private blockchain is restricted to a specific group of authorized participants who have a shared interest or trust in the network.
- A blockchain can also be permissionless or permissioned, depending on who can create and validate new blocks. A permissionless blockchain allows anyone who has the necessary resources and incentives to mine new blocks and receive rewards. A permissioned blockchain requires the nodes to have a certain level of authority or reputation to create and validate new blocks.
- A blockchain can be used for various applications, such as cryptocurrencies, smart contracts, supply chain management, digital identity, voting systems, and decentralized applications. Each application has its own requirements and challenges, such as scalability, privacy, interoperability, and regulation.



### Hashchain to Blockchain

- A hash chain is a data structure that applies a cryptographic hash function to a piece of data repeatedly, producing a sequence of hash values.
- A hash function is a mathematical function that maps an input of any size to an output of a fixed size, called a hash or a digest.
- A hash chain can be used to generate many one-time keys from a single key or password, or to record the chronology of data's existence.
- A blockchain is a data structure that consists of a chain of blocks, where each block contains a header and a body.
- The block header contains metadata, such as the previous block's hash, the timestamp, the nonce, and the difficulty.
- The block body contains transactions, which are records of data transfers or operations between participants.
- A blockchain is similar to a hash chain, as they both utilize a cryptographic hash function for creating a link between two nodes.
- However, a blockchain is more than a hash chain, as it also incorporates a consensus mechanism, a peer-to-peer network, and a distributed ledger.
- A consensus mechanism is a set of rules and procedures that allow the network nodes to agree on the validity and order of transactions and blocks.
- A peer-to-peer network is a system of interconnected nodes that communicate and exchange data without a central authority or intermediary.
- A distributed ledger is a shared and synchronized database that records the state of the network and the history of transactions.
- A blockchain is a type of distributed ledger that uses a hash chain to ensure the integrity and immutability of the data.
- A blockchain can be used for various applications, such as cryptocurrency, smart contracts, supply chain, identity, and voting.
- A hashgraph is another type of distributed ledger that uses a directed acyclic graph (DAG) instead of a hash chain to store and access information.
- A DAG is a data structure that consists of nodes and edges, where each node represents an event and each edge represents a causal relationship between events.
- A hashgraph claims to have advantages over a blockchain, such as faster speed, higher scalability, lower energy consumption, and fairer ordering.
- However, a hashgraph also has some drawbacks, such as being patented, centralized, and less secure.
- A hash chain, a blockchain, and a hashgraph are all examples of data structures that use hashing to achieve various goals and functionalities  .



### Basic consensus mechanisms for the notes of the Unit 1 - Introduction to Blockchain in the subject of Block chain Architecture Design

- A consensus mechanism is any method used to achieve agreement, trust, and security across a decentralized computer network .
- In the context of blockchains and cryptocurrencies, consensus mechanisms are the methodologies used to validate transactions and update the shared ledger .
- Consensus mechanisms play an essential part of securing information by encrypting it and using automated group verification .
- There are different types of consensus mechanisms, each with its own advantages and disadvantages. Some of the most prevalent ones are:
  - Proof-of-work (PoW): This mechanism requires network validators (also called miners) to solve complex mathematical puzzles in order to create new blocks and earn rewards. PoW is used by Bitcoin, Ethereum, and many other blockchains. PoW provides a high level of security and decentralization, but it also consumes a lot of energy and resources  .
  - Proof-of-stake (PoS): This mechanism assigns network validators based on their stake, or the amount of cryptocurrency they own or deposit. PoS does not require validators to perform intensive computations, but rather to lock up their funds as a form of collateral. PoS is used by Cardano, Polkadot, and Ethereum 2.0. PoS is more energy-efficient and scalable than PoW, but it also poses some challenges such as the risk of centralization and the lack of incentives for validators  .
  - Proof-of-authority (PoA): This mechanism relies on a set of trusted and verified validators who have the authority to create and validate new blocks. PoA does not depend on the amount of resources or stake that validators have, but rather on their reputation and identity. PoA is used by some private or permissioned blockchains, such as VeChain and POA Network. PoA offers fast and low-cost transactions, but it also sacrifices some degree of decentralization and security .
  - Proof-of-space (PoSpace): This mechanism requires network validators to prove that they have allocated a certain amount of disk space to store data related to the blockchain. PoSpace is used by some blockchains that aim to provide decentralized storage solutions, such as Filecoin and Chia. PoSpace is more environmentally friendly and accessible than PoW, but it also faces some technical and economic challenges such as data availability and storage costs .
  - Proof-of-elapsed-time (PoET): This mechanism randomly selects network validators based on the amount of time they have waited for their turn. PoET uses a trusted execution environment (TEE) to ensure that validators do not cheat or manipulate the system. PoET is used by some blockchains that aim to provide high scalability and low latency, such as Hyperledger Sawtooth. PoET is more fair and efficient than PoW, but it also depends on the reliability and security of the TEE .



## Unit 2 - Consensus

- Consensus is the process of reaching agreement among a group of participants on a common state of a system or a value of a variable.
- Consensus is essential for distributed systems that need to coordinate their actions or maintain a consistent view of the system state, such as databases, blockchains, or peer-to-peer networks.
- Consensus is challenging to achieve in the presence of faults, such as network delays, message losses, or node failures.
- Consensus algorithms are designed to ensure that the group of participants can eventually agree on a value, even if some of them are faulty or malicious.
- Consensus algorithms have different properties and trade-offs, such as:
  - Safety: the property that the participants will not agree on conflicting values.
  - Liveness: the property that the participants will eventually agree on a value.
  - Fault tolerance: the ability to withstand a certain number of faulty or malicious participants.
  - Performance: the efficiency and scalability of the algorithm in terms of communication, computation, and latency.
- Some examples of consensus algorithms are:
  - Paxos: a family of algorithms that ensure safety and liveness in asynchronous networks with up to half of the participants being faulty.
  - Raft: a simplified version of Paxos that is easier to understand and implement, and that uses a leader-based approach to achieve consensus.
  - Byzantine fault tolerance (BFT): a class of algorithms that ensure safety and liveness in asynchronous networks with up to one-third of the participants being malicious or arbitrary.
  - Proof-of-work (PoW): a probabilistic consensus algorithm that relies on cryptographic puzzles to elect a leader and validate transactions, such as in Bitcoin.
  - Proof-of-stake (PoS): a consensus algorithm that relies on the stake or wealth of the participants to elect a leader and validate transactions, such as in Ethereum 2.0.



### Requirements for the consensus protocols for the notes of the Unit 2 - Consensus in the subject of Block chain Architecture Design

- A consensus protocol is a set of rules that determines how a decentralized computer network reaches agreement on which transactions are valid and which are not .
- A consensus protocol prevents a single entity from controlling a blockchain or distorting the “truth” of what should be recorded.
- A consensus protocol ensures that all participating nodes agree on the state of a blockchain and that the blockchain is immutable, secure, and consistent .
- A consensus protocol should be able to handle various challenges, such as network latency, malicious nodes, network partitioning, and scalability .
- A consensus protocol should also be able to balance the trade-offs between decentralization, security, and performance .
- Some of the common consensus protocols used in blockchain networks are Proof of Work (PoW), Proof of Stake (PoS), Delegated Proof of Stake (DPoS), Byzantine Fault Tolerance (BFT), and Practical Byzantine Fault Tolerance (PBFT) .
- Each consensus protocol has its own advantages and disadvantages, and different protocols may be suitable for different use cases and applications .



### Proof of Work (PoW) for the notes of the Unit 2 - Consensus in the subject of Block chain Architecture Design

- Proof of work (PoW) is a **decentralized system** used to **verify the accuracy** of transactions on the blockchain network  .
- Proof of work **removes the need** for a central authority like a bank, business, or government agency to monitor and manage transactions and their corresponding accounts.
- Proof of work **lets blockchain networks operate by consensus rules** rather than “trust.”
- Proof of work **consumes a lot of energy**, prompting blockchain developers to create alternative verification systems.
- Proof of work **involves solving complex mathematical problems** that require a lot of computational power and time .
- Proof of work **uses hashes**, which are unique identifiers for each block of data on the blockchain.
- Proof of work **requires a nonce**, which is a random number that is added to the block data before hashing.
- Proof of work **solves the hash** by finding a nonce that produces a hash that meets a certain difficulty level, which is determined by the network.
- Proof of work **rewards the miners**, who are the programs on the nodes that work to solve the hash, with newly created coins or transaction fees .
- Proof of work **prevents double-spending**, which is the attempt to use the same coins for more than one transaction, by making it hard to alter or reverse the transactions on the blockchain .
- Proof of work **ensures the security and immutability** of the blockchain by making it costly and impractical for malicious actors to attack or manipulate the network .



### Scalability aspects of blockchain consensus protocols

- Scalability is the ability of a blockchain protocol to support high transactional throughput and future growth without compromising performance or security.
- Scalability is one of the main challenges faced by blockchain networks, especially those that use Proof of Work (PoW) as their consensus protocol .
- PoW is a consensus protocol that requires nodes to solve a computationally hard puzzle to validate transactions and create new blocks. PoW is secure and decentralized, but it is also slow, energy-intensive, and prone to congestion  .
- To improve scalability, blockchain networks can adopt different consensus protocols or use scaling solutions that enhance the existing protocols  .
- Some of the alternative consensus protocols that aim to improve scalability are:
  - Proof of Stake (PoS): a consensus protocol that selects validators based on their stake (amount of coins) in the network. PoS is faster, cheaper, and more energy-efficient than PoW, but it may introduce centralization and security risks  .
  - Delegated Proof of Stake (DPoS): a consensus protocol that allows coin holders to delegate their voting power to a set of elected validators. DPoS is more scalable and democratic than PoS, but it may also suffer from centralization and corruption.
  - Delegated Byzantine Fault Tolerance (dBFT): a consensus protocol that uses a two-phase voting process among a group of validators to reach agreement. dBFT is fast, final, and tolerant to malicious nodes, but it requires a high degree of trust and coordination among validators.
  - Casper: a hybrid consensus protocol that combines PoW and PoS to achieve a gradual transition from the former to the latter . Casper is designed to preserve the security and decentralization of PoW while improving the scalability and efficiency of PoS .
- Some of the scaling solutions that aim to improve scalability are:
  - Sharding: a technique that splits the blockchain network into smaller and parallel subnetworks (shards) that process transactions independently and communicate with each other when needed . Sharding increases the transactional capacity and speed of the network, but it also introduces complexity and security challenges .
  - Layer 2: a term that refers to solutions that operate on top of the blockchain layer (layer 1) and use it as a settlement layer . Layer 2 solutions include payment channels, sidechains, and state channels, which enable faster and cheaper transactions without compromising the security and decentralization of the underlying blockchain .
- Scalability is a trade-off between security, decentralization, and performance, and different blockchain networks may prioritize different aspects depending on their use cases and goals . This trade-off is known as the blockchain trilemma .



## Unit 3 - Permissioned Blockchains

- Permissioned blockchains are a type of distributed ledger technology (DLT) that allow only authorized participants to join the network, validate transactions, and execute smart contracts.
- Permissioned blockchains are also known as private or consortium blockchains, depending on the degree of centralization and control over the network.
- Permissioned blockchains offer some advantages over public or permissionless blockchains, such as:
  - Higher scalability and performance, as the number of nodes and transactions are limited and optimized.
  - Greater privacy and security, as the identity and role of the participants are verified and protected by encryption and access control mechanisms.
  - Lower cost and energy consumption, as the consensus algorithm does not require intensive computation and competition among nodes.
  - Easier compliance and governance, as the network rules and policies are defined and enforced by the authorized entities.
- Permissioned blockchains also have some challenges and limitations, such as:
  - Reduced decentralization and trustlessness, as the network relies on the authority and integrity of the permissioned entities.
  - Increased complexity and coordination, as the network requires more layers of administration and management to maintain the permissions and roles of the participants.
  - Potential for collusion and corruption, as the permissioned entities may act in their own interest or abuse their power over the network.
- Permissioned blockchains are suitable for use cases that involve sensitive or confidential data, regulated or legal transactions, and complex or customized business logic.
- Some examples of permissioned blockchains are:
  - Hyperledger Fabric, a modular and flexible platform that supports various consensus algorithms, smart contract languages, and data privacy options.
  - Corda, a platform that focuses on enabling interoperability and atomicity among different business networks and applications.
  - Quorum, a platform that is based on Ethereum and provides features such as private transactions, permissioned nodes, and pluggable consensus.



### Design goals for the notes of the Unit 3 - Permissioned Blockchains in the subject of Block chain Architecture Design

- The notes should provide a clear and concise overview of the main concepts and features of permissioned blockchains, such as:
  - The definition and characteristics of permissioned blockchains, such as the need for identity management, access control, and governance mechanisms.
  - The advantages and disadvantages of permissioned blockchains compared to public and private blockchains, such as the trade-offs between scalability, security, and decentralization.
  - The use cases and applications of permissioned blockchains in various domains, such as finance, supply chain, healthcare, and government.
  - The challenges and open issues of permissioned blockchains, such as interoperability, privacy, and regulation.
- The notes should also include examples and diagrams to illustrate the key concepts and features of permissioned blockchains, such as:
  - The architecture and components of a permissioned blockchain system, such as the nodes, the ledger, the consensus protocol, and the smart contracts.
  - The types and roles of the participants in a permissioned blockchain network, such as the validators, the endorsers, the clients, and the auditors.
  - The process and steps of creating, validating, and executing transactions and smart contracts on a permissioned blockchain, such as the endorsement policy, the ordering service, and the validation policy.
  - The comparison and contrast of different permissioned blockchain platforms, such as Hyperledger Fabric, Corda, and Quorum.
- The notes should also provide exercises and questions to test the understanding and application of the concepts and features of permissioned blockchains, such as:
  - The identification and explanation of the main components and functions of a permissioned blockchain system given a diagram or a scenario.
  - The evaluation and comparison of the advantages and disadvantages of different permissioned blockchain platforms given a use case or a requirement.
  - The design and implementation of a simple smart contract or a transaction on a permissioned blockchain platform given a specification or a problem.



### Consensus protocols for Permissioned Blockchains

- A consensus protocol enables all the parties of the blockchain network to come to a common agreement (consensus) on the present data state of the ledger .
- In a permissioned blockchain, all the participating nodes are known and chosen, but consensus is still required because we can’t assume that every node is trustworthy .
- Choosing the right consensus protocol for permissioned blockchain depends on factors like the extent of decentralization required, the number of permissions that must be granted to all the participants to carry out important tasks on the network, the speed and scalability of the network, and the security and fault tolerance of the protocol .
- Some of the common consensus protocols for permissioned blockchains are:

  - **Delegated Proof of Stake (DPoS)**: This protocol allows the network participants to vote for a set of delegates, who are responsible for validating transactions and maintaining the ledger. The delegates are rewarded for their service and can be replaced by the voters if they misbehave or underperform .
  - **Delegated Byzantine Fault Tolerance (dBFT)**: This protocol uses a leader-follower model, where a leader node is randomly selected to propose a new block, and a group of follower nodes (called validators) are chosen to endorse the block. The block is accepted if it receives a two-thirds majority of endorsements. If the leader node is faulty or malicious, the validators can switch to a new leader .
  - **Proof of Elapsed Time (PoET)**: This protocol relies on a trusted execution environment (TEE) to ensure that each node has a fair chance of proposing a new block. The TEE generates a random waiting time for each node, and the node with the shortest waiting time gets to propose the block. The TEE also verifies that the node did not cheat by altering the waiting time .
  - **Proof of Authority (PoA)**: This protocol assigns the role of validating transactions and creating blocks to a set of pre-approved nodes (called authorities), who are trusted by the network. The authorities do not receive any rewards for their service, but they stake their reputation on the network. The protocol is fast and scalable, but it sacrifices some degree of decentralization.



## Unit 4 - Hyperledger Fabric (A)

- Hyperledger Fabric is an open source project from the Linux Foundation that provides a modular blockchain framework and a de facto standard for enterprise blockchain platforms  .
- Hyperledger Fabric is intended as a foundation for developing applications or solutions with a modular architecture that allows components, such as consensus and membership services, to be plug-and-play .
- Hyperledger Fabric is designed to support various industry use cases, such as finance, banking, healthcare, IoT, supply chain, manufacturing and technology .
- Hyperledger Fabric delivers a uniquely elastic and extensible architecture, distinguishing it from alternative blockchain solutions .
- Hyperledger Fabric supports smart contracts written in general-purpose programming languages, such as Java, Go and Node.js .
- Hyperledger Fabric enables a network of participants to agree on a shared ledger of transactions, while preserving privacy, confidentiality and scalability  .
- Hyperledger Fabric is composed of several core components, such as:
  - Peer nodes: responsible for endorsing and validating transactions, maintaining the ledger state and running chaincode (smart contracts) .
  - Orderer nodes: responsible for ordering transactions into blocks and broadcasting them to peer nodes .
  - Certificate authority: responsible for issuing and managing digital certificates for identity and access control .
  - Channel: a private communication channel that allows a subset of network participants to share a ledger and execute transactions .
  - Chaincode: the business logic that defines the rules and operations for a specific asset or function on the ledger .
- Hyperledger Fabric 2.0 is the latest version of the framework, released in January 2020, that introduces several new features and improvements, such as:
  - Decentralized chaincode lifecycle: allows network participants to agree on the parameters and policies for deploying and upgrading chaincode, without requiring a central authority.
  - State-based endorsement: allows chaincode to specify different endorsement policies for different states or keys on the ledger, enabling more flexibility and efficiency.
  - Private data collections: allows network participants to store and share sensitive data in a private and secure way, without revealing it to the entire network.
  - Raft-based ordering service: allows network participants to use a crash fault tolerant consensus algorithm that is easier to set up and maintain than the previous Kafka-based one.
  - External chaincode launcher: allows network participants to use external builders and launchers to run chaincode, enabling more control and customization.



### Decomposing the consensus process for the notes of the Unit 4 - Hyperledger Fabric (A) in the subject of Block chain Architecture Design

- Consensus is a process where the nodes in the network provide a guaranteed ordering of the transactions and validate those blocks of transactions that need to be committed to the ledger.
- Consensus must ensure the following in the network:
  - Agreement on the order and results of transactions
  - Fault tolerance and finality
  - Network performance and scalability
  - Network security and privacy
- Consensus in Hyperledger Fabric is broken out into three phases: Endorsement, Ordering, and Validation .
- Endorsement is driven by policy (m out of n signatures) upon which participants endorse a transaction.
- Ordering phase will get the endorsed transaction and agrees to the order to be committed to the ledger.
- Validation phase will check the endorsement policy and read-write sets for conflicts before committing the transaction to the ledger.
- Hyperledger Fabric follows a modular approach wherein different consensus techniques can be plugged in as per the requirement.
- Currently, Hyperledger Fabric uses Solo and Kafka to reach consensus, which requires a node to validate a batch of transactions and add them as a new block to the blockchain.
- Solo is a single node ordering service that is used for development and testing purposes.
- Kafka is a distributed messaging system that provides a crash fault tolerant and scalable ordering service for production environments.
- Hyperledger Fabric is intended as a foundation for developing applications or solutions with a modular architecture.
- Hyperledger Fabric allows components, such as consensus and membership services, to be plug-and-play.
- Its modular and versatile design satisfies a broad range of industry use cases.



### Hyperledger Fabric Components

Hyperledger Fabric is a distributed ledger technology (DLT) platform that allows participants to create and manage private, permissioned blockchain networks. Hyperledger Fabric consists of various major components that have different roles and functions in the network. Some of the main components are:

- **Certificate Authority (CA)**: This is a service that issues and manages digital certificates for the network participants. The CA verifies the identities of the participants and assigns them roles and permissions. The CA also provides a mechanism for revoking or renewing certificates. The CA can be implemented using different protocols, such as Fabric-CA or Fabric-SDK  .

- **Peer Nodes**: These are the nodes that store and process the ledger data and execute the smart contracts (also known as chaincode) on the network. Peer nodes can have different roles, such as endorsing peers, committing peers, or anchor peers. Endorsing peers are responsible for validating and endorsing transactions, committing peers are responsible for updating the ledger with the ordered transactions, and anchor peers are responsible for communicating with other peer nodes across different organizations  .

- **Ordering Service**: This is a service that maintains the global ordering of transactions and delivers them to the peer nodes in batches (also known as blocks). The ordering service can use different consensus algorithms, such as Solo, Kafka, or Raft, to ensure the consistency and finality of the transactions. The ordering service can be composed of multiple ordering nodes that belong to different organizations  .

- **Private Channel**: This is a mechanism that allows a subset of network participants to create and join a private and secure communication channel, where they can share ledger data and chaincode among themselves. Private channels enable data privacy and confidentiality, as well as scalability and performance, by reducing the amount of data that needs to be broadcasted to the whole network  .

- **Membership Service**: This is a service that manages the identities and access rights of the network participants. The membership service can be implemented using different frameworks, such as Fabric-CA or Fabric-SDK, or integrated with external identity providers, such as LDAP or OAuth. The membership service ensures that only authorized and authenticated entities can join and interact with the network  .

- **Chaincode**: This is the term used for the smart contracts that run on the Hyperledger Fabric network. Chaincode is a program that defines the business logic and rules for the network transactions. Chaincode can be written in different languages, such as Go, Node.js, or Java, and can be deployed and invoked by the peer nodes. Chaincode can also interact with the ledger state and external services, such as databases or APIs  .

These are some of the main components of Hyperledger Fabric that enable the creation and management of private, permissioned blockchain networks. Hyperledger Fabric also provides a modular and versatile design that allows components, such as consensus and membership services, to be plug-and-play. This satisfies a broad range of industry use cases and requirements .



### Chaincode Design and Implementation for the notes of the Unit 4 - Hyperledger Fabric (A) in the subject of Block chain Architecture Design

- Chaincode is a program that implements a prescribed interface and runs in a secured Docker container isolated from the endorsing peer process.
- Chaincode is also known as smart contracts, and it defines the rules for interacting with the data stored on a blockchain, such as reading and writing data to the ledger, verifying the identity of users, and enforcing access controls.
- Chaincode can be written in Go, node.js, or Java, and it can use the fabric-contract-api, a high level API for application developers to implement smart contracts.
- Chaincode can be deployed on a Hyperledger Fabric network through a chaincode lifecycle, which consists of the following steps:
  - Packaging: The chaincode source code and metadata are packaged into a tar file that can be installed on peers.
  - Installing: The chaincode package is installed on the peers that will endorse the chaincode transactions.
  - Approving: The organizations that are part of the channel approve the chaincode definition, which specifies the name, version, endorsement policy, and other parameters of the chaincode.
  - Committing: The chaincode definition is committed to the channel, which makes it available for invocation by applications.
  - Invoking: The chaincode is invoked by applications through the peer API, which sends proposals to the endorsing peers and collects the endorsements.
  - Querying: The chaincode can be queried by applications to read the current state of the ledger or the history of transactions.
  - Upgrading: The chaincode can be upgraded to a new version by following the same steps as deploying, but with a different version number and a new package.



## Unit 5 - Hyperledger Fabric (B)

- In this unit, you will learn about the following topics:
  - The architecture and components of Hyperledger Fabric
  - The process of creating and joining a Fabric network
  - The roles and responsibilities of Fabric participants
  - The types and features of Fabric smart contracts
  - The lifecycle and endorsement policies of Fabric chaincode
  - The mechanisms and tools for Fabric security and privacy
- Hyperledger Fabric is a permissioned, modular, and extensible blockchain platform that supports distributed ledger solutions for various business domains.
- Hyperledger Fabric has a unique architecture that separates the transaction execution from the transaction ordering, allowing for scalability, flexibility, and confidentiality.
- Hyperledger Fabric consists of the following components:
  - Peer nodes: The nodes that execute transactions, maintain the ledger state, and host chaincode.
  - Ordering nodes: The nodes that order transactions into blocks and broadcast them to the peer nodes.
  - Certificate authorities: The entities that issue and manage digital certificates for Fabric participants.
  - Membership service providers: The components that validate the identity and permissions of Fabric participants.
  - Channels: The private communication channels that isolate transactions and ledger data among a subset of Fabric participants.
  - Chaincode: The smart contracts that define the business logic and rules for transactions on the Fabric network.
  - Clients: The applications or users that interact with the Fabric network by invoking or querying chaincode, or by performing administrative tasks.
- To create and join a Fabric network, you need to perform the following steps:
  - Generate the cryptographic material and configuration files for the Fabric participants using tools such as cryptogen and configtxgen.
  - Start the ordering nodes and peer nodes using tools such as docker-compose or Kubernetes.
  - Create a genesis block and a system channel for the ordering service using the configtxgen tool.
  - Create and join application channels for the peer nodes using the peer CLI tool or the Fabric SDKs.
  - Install and instantiate chaincode on the peer nodes using the peer CLI tool or the Fabric SDKs.
- Fabric participants have different roles and responsibilities depending on their type and function. Some of the common roles are:
  - Endorsers: The peer nodes that endorse transactions by executing chaincode and signing the results.
  - Committers: The peer nodes that validate transactions and update the ledger state.
  - Leaders: The peer nodes that coordinate the endorsement and validation of transactions for a channel.
  - Orderers: The ordering nodes that batch transactions into blocks and maintain the order of transactions for a channel.
  - Administrators: The clients that perform administrative tasks such as creating channels, installing chaincode, or updating policies.
  - Clients: The clients that submit transactions or queries to the Fabric network.
- Fabric smart contracts are chaincode that define the business logic and rules for transactions on the Fabric network. Fabric supports two types of chaincode:
  - System chaincode: The chaincode that provides system functionality such as configuration, lifecycle, or endorsement policies.
  - Application chaincode: The chaincode that provides application functionality such as asset transfer, voting, or supply chain management.
- Fabric chaincode has a lifecycle that consists of four phases:
  - Install: The phase where the chaincode is installed on the peer nodes that will execute it.
  - Approve: The phase where the chaincode is approved by the organizations that participate in a channel.
  - Commit: The phase where the chaincode is committed to the channel ledger and becomes active.
  - Invoke: The phase where the chaincode is invoked by the clients to perform transactions or queries.
- Fabric chaincode has an endorsement policy that specifies the set of peer nodes that must endorse a transaction before it can be committed to the ledger. The endorsement policy can be defined using expressions such as `AND`, `OR`, or `OutOf`, or using signature policies that reference the identity or role of the endorsers.
- Fabric provides various mechanisms and tools for security and privacy, such as:
  - Cryptography: The use of digital certificates, signatures, and encryption to ensure the authenticity, integrity, and confidentiality of transactions and data.
  - Identity management: The use of certificate authorities and membership service providers to issue and validate the identity and permissions of Fabric participants.
  - Access control: The use of policies and ACLs to regulate the access and visibility of channels, chaincode, and data among Fabric participants.
  - Private data: The use of private data collections and side databases to store and share sensitive data among a subset of Fabric participants.
  - Channels: The use of channels to isolate transactions and ledger data among a subset of Fabric participants.



### Beyond Chaincode

- Chaincode is the term used for smart contracts in Hyperledger Fabric. It is a program that implements the logic and rules for a specific application on the blockchain network.
- Chaincode can be written in various languages, such as Go, Node.js, or Java. It can access the ledger state, invoke other chaincodes, and interact with external systems.
- Chaincode runs in a separate container from the peer node, and communicates with the peer node through a gRPC interface. This provides isolation and security for the chaincode execution.
- Chaincode can be installed and instantiated on one or more channels, depending on the endorsement policy and the access control requirements. Each channel has its own ledger and chaincode state.
- Chaincode can be upgraded to a new version, or replaced by a different chaincode, by following a specific process that involves the endorsement and validation of the new chaincode proposal.
- Chaincode can be queried or invoked by client applications, using the Fabric SDK or the Fabric Gateway service. The client applications need to specify the channel, the chaincode name, the function name, and the arguments for the query or invocation.
- Chaincode can emit events that can be subscribed by client applications or other chaincodes. Events can be used to notify external systems or trigger actions based on the state changes in the ledger or the chaincode.



### Fabric SDK and Front End

- A Fabric SDK is a software development kit that allows an application front-end to communicate with a Fabric network back-end using a programming language of choice.
- A Fabric SDK provides APIs to perform various operations on a Fabric network, such as creating channels, joining peers, installing and invoking chaincodes, querying ledger data, and listening to events.
- A Fabric SDK also handles the cryptographic aspects of the communication, such as signing transactions, verifying signatures, and encrypting and decrypting data.
- Fabric SDKs are available for different programming languages, such as Node.js, Java, Python, and Go.
- A front-end application is a user interface that interacts with a Fabric network through a Fabric SDK. It can be a web application, a mobile application, a desktop application, or any other type of application that can use a Fabric SDK.
- A front-end application can use various frameworks and libraries to create a user-friendly and responsive interface, such as React, Angular, Vue, Bootstrap, etc.
- A front-end application can also use various tools and services to enhance its functionality, such as databases, cloud platforms, authentication providers, etc.
- A front-end application can perform various tasks on a Fabric network, such as creating and managing users, submitting and querying transactions, displaying ledger data, and monitoring network events.



### Hyperledger Composer Tool

- Hyperledger Composer is a set of open source tools that allows business owners, operators, and developers a way to create blockchain applications and smart contracts aimed at solving business problems and/or improving operational efficiencies .
- It is an example of a commercial application of blockchain-as-a-service (BaaS) .
- It is a collaboration tool for building “blockchain business networks,” accelerating the development of smart contracts and their deployment across a distributed ledger .
- It is based on the Hyperledger Fabric framework, which provides the underlying blockchain infrastructure and security .
- It has four main components:
  - **Modeling language**: A domain-specific language for defining the assets, participants, transactions, and access control rules of a business network.
  - **Business network archive**: A deployable unit that contains the business network definition and any external dependencies.
  - **Runtime**: A component that runs on the Hyperledger Fabric peers and executes the transactions defined by the smart contracts.
  - **Composer Playground**: A web-based user interface for testing and deploying business networks, as well as creating and submitting transactions.
- It also provides a set of tools and APIs for integrating blockchain applications with existing systems and data sources.
- It is designed to simplify and accelerate the development of blockchain applications, by providing a high-level abstraction of the blockchain concepts and logic  .
- It is intended to foster collaboration and innovation within organizations and business networks, by enabling the creation of open-source blockchain applications that can be shared and reused  .



## Unit 6 - Use case 1

- A use case is a description of how a system interacts with one or more external entities, called actors, to achieve a specific goal.
- A use case diagram is a graphical representation of the use cases and actors involved in a system.
- A use case diagram consists of the following elements:
  - Actors: The external entities that interact with the system. They are represented by stick figures or icons.
  - Use cases: The goals or functions that the system provides to the actors. They are represented by ovals with names inside.
  - Associations: The relationships between actors and use cases. They are represented by solid lines with optional arrows to indicate the direction of communication.
  - System boundary: An optional rectangle that encloses the use cases and represents the scope of the system. It has a name on the top left corner.
  - Packages: An optional way to group related use cases or actors. They are represented by tabbed rectangles with names on the top.
  - Generalization: A relationship that indicates that one actor or use case inherits the characteristics of another actor or use case. It is represented by a dashed line with a hollow triangle pointing to the parent actor or use case.
  - Include: A relationship that indicates that one use case includes the behavior of another use case as a part of its normal execution. It is represented by a dashed line with an open arrowhead pointing to the included use case and a label <<include>>.
  - Extend: A relationship that indicates that one use case extends the behavior of another use case under certain conditions. It is represented by a dashed line with an open arrowhead pointing to the extended use case and a label <<extend>> with an optional extension point.

- An example of a use case diagram for an online shopping system is shown below:

Use case diagram for online shopping system

- The use case diagram shows the following elements:
  - Actors: Customer, Administrator, and Bank
  - Use cases: View Items, Search Items, Add Item to Shopping Cart, Remove Item from Shopping Cart, Check Out, Process Payment, Ship Order, Manage Orders, Manage Items, and Manage Users
  - Associations: Customer is associated with View Items, Search Items, Add Item to Shopping Cart, Remove Item from Shopping Cart, and Check Out. Administrator is associated with Manage Orders, Manage Items, and Manage Users. Bank is associated with Process Payment.
  - System boundary: Online Shopping System
  - Packages: None
  - Generalization: None
  - Include: Check Out includes Process Payment and Ship Order
  - Extend: View Items extends Search Items with an extension point Filter by Category



### Blockchain in Financial Software and Systems (FSS) for the notes of the Unit 6 - Use case 1

- Blockchain is a distributed ledger technology that enables secure and transparent transactions among multiple parties without intermediaries.
- Blockchain has the potential to transform the financial industry by improving efficiency, security, trust, and innovation.
- Some of the use cases of blockchain in financial software and systems are:

  - **Payments, especially cross-border payments**: Blockchain can facilitate faster, cheaper, and more secure payments across borders by eliminating intermediaries, reducing fees, and enhancing transparency. Blockchain can also enable the issuance and exchange of digital currencies, such as cryptocurrencies or central bank digital currencies (CBDCs), that can offer more financial inclusion and stability .
  - **Digital identity management**: Blockchain can provide a decentralized and verifiable way of managing and verifying digital identities, such as biometric data, credentials, or certificates. Blockchain can also enable self-sovereign identity, which gives users full control and ownership of their personal data and how it is shared. This can improve customer experience, privacy, and compliance with KYC/AML regulations.
  - **Lending and borrowing**: Blockchain can streamline the lending and borrowing process by automating the verification, origination, servicing, and repayment of loans. Blockchain can also enable peer-to-peer lending platforms that can offer lower interest rates, more access, and more transparency. Moreover, blockchain can enable the use of cryptoassets as collateral for loans, which can create new liquidity and investment opportunities .
  - **Trade finance**: Blockchain can improve the efficiency and security of trade finance transactions, such as letters of credit, bills of lading, or invoices. Blockchain can enable the digitization, verification, and sharing of trade documents among multiple parties, such as exporters, importers, banks, and customs. This can reduce fraud, errors, costs, and delays, and increase trust and visibility .
  - **Asset management**: Blockchain can enhance the asset management industry by enabling the tokenization, issuance, and exchange of various types of assets, such as stocks, bonds, commodities, real estate, or art. Blockchain can also enable the creation and management of smart contracts, which are self-executing agreements that can automate the execution and settlement of transactions. This can increase liquidity, efficiency, transparency, and innovation in the asset management space .



### Settlements

- Settlements are the process of transferring ownership and value of assets between parties after a trade or transaction.
- Settlements can involve various types of assets, such as securities, derivatives, commodities, currencies, and digital assets.
- Settlements can be costly, slow, and risky, especially when they involve multiple intermediaries, jurisdictions, and regulations.
- Blockchain technology can offer a solution for improving settlement efficiency, speed, security, and transparency.
- Blockchain is a distributed ledger that records transactions in a verifiable, immutable, and consensus-based way.
- Blockchain can enable peer-to-peer settlement without the need for intermediaries, such as clearinghouses, custodians, or banks.
- Blockchain can also enable smart contracts, which are self-executing agreements that can automate settlement processes and enforce predefined rules and conditions.
- Blockchain can support different types of settlement models, such as delivery versus payment (DVP), payment versus payment (PVP), and atomic swaps.
- Some of the use cases of blockchain for settlements are:

  - Securities trade clearing and settlement: Blockchain can reduce the settlement time, cost, and risk of securities trades, such as stocks, bonds, and derivatives. Blockchain can also enable real-time settlement, fractional ownership, and tokenization of securities. Some examples of blockchain platforms for securities settlement are Paxos, tZERO, and Fnality.
  - Cross-border payments and settlements: Blockchain can facilitate faster, cheaper, and more secure cross-border payments and settlements, especially for remittances, trade finance, and foreign exchange. Blockchain can also enable interoperability and integration of different payment systems and currencies. Some examples of blockchain platforms for cross-border payments and settlements are Ripple, Stellar, and SWIFT GPI.
  - Supply chain and trade finance document handling: Blockchain can improve the traceability, authenticity, and efficiency of supply chain and trade finance documents, such as invoices, bills of lading, and letters of credit. Blockchain can also enable smart contracts to automate document verification, validation, and payment. Some examples of blockchain platforms for supply chain and trade finance document handling are TradeLens, Marco Polo, and we.trade.



### KYC for the notes of the Unit 6 - Use case 1 in the subject of Block chain Architecture Design

- KYC stands for Know Your Customer, a process of verifying the identity and background of customers, especially in the financial sector.
- KYC is important for preventing fraud, money laundering, terrorism financing, and other illicit activities.
- KYC is also costly, time-consuming, and repetitive for both customers and service providers, as they have to provide and verify the same information across multiple platforms and institutions.
- Blockchain can be used to improve KYC by creating a decentralized, secure, and transparent platform for storing and sharing customer identity data.
- Blockchain KYC can reduce the operational costs, enhance the customer experience, and increase the compliance efficiency for service providers.
- Blockchain KYC can also empower customers to have more control and ownership over their own data, and to choose who can access it and for what purpose.
- Some of the use cases of blockchain KYC are:

  - IBM Blockchain Trusted Identity: a decentralized platform for identification processes based on the blockchain and biometric technologies .
  - UAE KYC Blockchain Platform: a national KYC ecosystem launched by Dubai's Department of Economic Development and Dubai International Financial Centre, powered by Norbloc, a consortium of banks and regulators.
  - uPort: an open identification system that allows users to create and manage their own identities on the Ethereum blockchain, and to share them with other applications and services.
  - Civic: a secure identity platform that leverages blockchain and smart contracts to verify and protect the identity of users and businesses.
  - SelfKey: a self-sovereign identity system that enables users to create and manage their own identity wallets, and to access a marketplace of services that require KYC verification.



### Capital markets for the notes of the Unit 6 - Use case 1 in the subject of Block chain Architecture Design

- Capital markets are the markets where securities such as stocks, bonds, derivatives and other financial instruments are issued, traded and settled.
- Blockchain is a distributed ledger technology (DLT) that enables peer-to-peer transactions without intermediaries, using cryptography and consensus mechanisms to ensure data integrity and security.
- Blockchain has the potential to transform various aspects of capital markets, such as issuance, trading, clearing, settlement, collateral management, asset servicing and custody, by streamlining processes, reducing costs, increasing transparency and enhancing security.
- Some of the use cases of blockchain in capital markets are:

  - Issuance: Blockchain can facilitate the issuance of digital securities, such as tokenized assets, stablecoins, digital bonds and equity, by enabling faster, cheaper and more inclusive access to capital for issuers and investors. Blockchain can also automate the compliance and governance processes of issuance, such as KYC, AML, disclosure and reporting, using smart contracts and digital identities .
  - Trading: Blockchain can enable peer-to-peer trading of securities, without the need for intermediaries such as brokers, dealers, exchanges and clearing houses, by providing a shared and trusted source of truth for market participants. Blockchain can also enable real-time price discovery, liquidity provision, market making and execution of trades, using decentralized protocols and platforms .
  - Clearing and settlement: Blockchain can eliminate the need for centralized clearing and settlement entities, such as central securities depositories (CSDs) and central counterparties (CCPs), by enabling instant and final settlement of trades on the same ledger, using atomic swaps and delivery-versus-payment (DvP) mechanisms. Blockchain can also reduce the settlement risk, operational risk, counterparty risk and systemic risk, by ensuring data accuracy, transparency and immutability  .
  - Collateral management: Blockchain can optimize the collateral management process, by enabling real-time tracking, valuation and allocation of collateral across multiple parties and jurisdictions, using tokenization and smart contracts. Blockchain can also reduce the collateral costs, risks and inefficiencies, by enabling collateral reuse, netting, optimization and automation  .
  - Asset servicing: Blockchain can improve the asset servicing functions, such as corporate actions, dividends, coupons, voting and proxy, by enabling automated and standardized execution of events, using smart contracts and digital identities. Blockchain can also enhance the transparency, accuracy and timeliness of asset servicing, by providing a single source of truth for all stakeholders .
  - Custody: Blockchain can enable secure and efficient custody of digital securities, by providing cryptographic proof of ownership and control, using public-key encryption and digital signatures. Blockchain can also enable self-custody or decentralized custody of assets, by allowing investors to hold and manage their own private keys, using wallets and protocols .



### Insurance for the notes of the Unit 6 - Use case 1 in the subject of Block chain Architecture Design

- Blockchain is a distributed ledger technology that enables secure, transparent, and immutable transactions among multiple parties without intermediaries.
- Blockchain can be applied to various aspects of the insurance industry, such as policy issuance, claims processing, fraud prevention, customer engagement, and data sharing.
- Some of the benefits of blockchain in insurance are:
  - Reduced operational costs and risks by automating manual processes and verifying data integrity.
  - Enhanced customer trust and satisfaction by providing faster and fairer claims settlement and personalized products.
  - Increased market efficiency and innovation by enabling new business models and collaborations across the insurance value chain.
- Some of the challenges of blockchain in insurance are:
  - Regulatory uncertainty and compliance issues due to the lack of clear and consistent legal frameworks and standards for blockchain applications.
  - Technical complexity and scalability issues due to the high resource requirements and performance limitations of some blockchain platforms.
  - Cultural and organizational barriers due to the need for a paradigm shift and a collaborative mindset among the insurance stakeholders.
- Some of the examples of blockchain use cases in insurance are:
  - Smart contracts: Blockchain-based contracts that can execute predefined rules and actions based on predefined conditions and events. For example, smart contracts can automate the payment of claims based on verifiable data from external sources, such as weather reports, flight delays, or IoT devices  .
  - Parametric insurance: Blockchain-based insurance products that can provide coverage for specific events or parameters that are objectively measurable and verifiable. For example, parametric insurance can cover crop losses due to drought or flood based on rainfall or soil moisture data from satellites or sensors .
  - Peer-to-peer insurance: Blockchain-based insurance models that can enable customers to pool their risks and premiums and share the benefits and losses among themselves. For example, peer-to-peer insurance can allow customers to form their own mutual insurance groups and vote on claims and payouts .
  - Identity and data management: Blockchain-based solutions that can enable customers to control and share their personal and financial data securely and selectively with insurers and other parties. For example, identity and data management can facilitate the verification of customer identity and credentials, the creation of comprehensive health records, and the protection of data privacy and ownership  .



## Unit 7 - Use case 2

- Use case 2 is a scenario that describes how a user interacts with a system to achieve a specific goal.
- Use case 2 is also a document that captures the requirements and specifications of the system from the user's perspective.
- Use case 2 consists of the following elements:

  - **Actor**: The user or external entity that initiates the use case and interacts with the system.
  - **System**: The software or hardware that provides the functionality or service to the actor.
  - **Goal**: The objective or outcome that the actor wants to achieve by using the system.
  - **Precondition**: The state or condition that must be true before the use case can begin.
  - **Postcondition**: The state or condition that must be true after the use case is completed.
  - **Main flow**: The sequence of steps or actions that the actor and the system perform to achieve the goal.
  - **Alternative flow**: The sequence of steps or actions that the actor and the system perform when the main flow is interrupted or deviated by an exception or a variation.
  - **Exception**: An unexpected event or situation that prevents the use case from continuing or completing normally.
  - **Variation**: A possible variation or option that the actor or the system can choose during the use case execution.

- Use case 2 can be represented in different formats, such as text, diagram, table, or template.
- Use case 2 can be used for different purposes, such as analysis, design, testing, or documentation of the system.



### Blockchain in trade/supply chain

- Blockchain is a decentralized ledger technology that records and protects transaction data shared among multiple parties in a network.
- Blockchain can improve supply chain transparency and traceability by recording product statuses at every phase of the product’s lifecycle, from production to consumption.
- Blockchain can also reduce administrative costs and inefficiencies by automating data collection, verification, and exchange among supply chain participants.
- Blockchain can enhance supply chain resilience and security by preventing data tampering, fraud, and cyberattacks, and by enabling faster and more accurate dispute resolution.
- Blockchain can facilitate cross-border trade and supply chain collaboration by simplifying and standardizing data formats, protocols, and regulations, and by enabling smart contracts that execute automatically based on predefined rules .
- Some examples of blockchain applications in supply chain are:
  - IBM Food Trust: a platform that connects farmers, processors, distributors, and retailers to share data and trace food products across the supply chain.
  - TradeLens: a platform that connects shipping companies, ports, customs, and other stakeholders to share data and documents and track cargo movements across the global trade network.
  - Everledger: a platform that tracks and verifies the provenance, quality, and ethical sourcing of diamonds, gemstones, and other high-value assets.



### Provenance of goods

- Provenance of goods refers to the **chain of custody** of a product from the point of origin to the point of consumption .
- Provenance of goods is important for ensuring the **authenticity**, **quality**, **safety**, and **sustainability** of products, as well as preventing **fraud** and **counterfeiting**  .
- Blockchain is a technology that can provide **transparency**, **accuracy**, and **trust** in the provenance of goods by creating a **decentralized**, **immutable**, and **verifiable** record of transactions and events   .
- Blockchain can enable the **traceability** of goods throughout the supply chain, allowing the stakeholders to track the **location**, **status**, **ownership**, and **history** of goods at any point in time   .
- Blockchain can also facilitate the **verification** of goods by using **smart contracts**, **digital signatures**, **cryptographic hashes**, and **oracles** to ensure the validity and integrity of the data and the compliance with the rules and standards   .
- Some examples of use cases for blockchain provenance of goods are:
  - Art: Blockchain can help to establish the **identity**, **ownership**, and **value** of artworks, as well as to protect the **intellectual property rights** and **royalties** of artists.
  - Luxury goods: Blockchain can help to verify the **origin**, **quality**, and **authenticity** of luxury goods, such as jewelry, precious metals and stones, wine collections, and limited collection apparel and accessories.
  - Land ownership: Blockchain can help to create a **secure**, **transparent**, and **efficient** registry of land titles and deeds, as well as to reduce the **costs**, **delays**, and **risks** of land transactions.
  - Supply chain information: Blockchain can help to improve the **visibility**, **accountability**, and **collaboration** among the supply chain actors, as well as to optimize the **performance**, **efficiency**, and **resilience** of the supply chain operations   .



### Visibility for the notes of the Unit 7 - Use case 2 in the subject of Blockchain Architecture Design

- Visibility refers to the degree of transparency and confidentiality of the data and transactions stored on a blockchain ledger.
- By default, blockchain technologies lead to a visibility of all data written to the blockchain ledger for all participants for all times.
- However, visibility can be adjusted according to the specific requirements and design choices of the blockchain-based application.
- Some factors that affect the visibility of a blockchain are:
  - The type of blockchain: public, private, or hybrid.
  - The consensus mechanism: proof-of-work, proof-of-stake, or other.
  - The encryption and hashing methods: symmetric, asymmetric, or homomorphic.
  - The access control policies: role-based, attribute-based, or policy-based.
  - The data storage and retrieval methods: on-chain, off-chain, or side-chain.
- Visibility can have different implications for different use cases of blockchain, such as:
  - Supply chain management: visibility can improve the traceability, accountability, and efficiency of the supply chain processes and transactions.
  - Financial services: visibility can enhance the security, compliance, and auditability of the financial transactions and records.
  - Healthcare: visibility can protect the privacy, integrity, and availability of the patient data and medical records.



### Trade/Supply Chain Finance

- Trade finance is the process of financing international trade transactions, such as the exchange of goods and services across borders.
- Trade finance involves multiple parties, such as exporters, importers, banks, intermediaries, insurers, regulators, and customs authorities, who need to coordinate and exchange information, documents, and payments.
- Trade finance is often complex, costly, time-consuming, and prone to errors, fraud, and disputes, due to the lack of trust, transparency, and standardization among the parties.
- Blockchain is a distributed ledger technology that can enable more efficient, secure, and transparent trade finance processes, by providing a shared and immutable record of transactions and assets among the parties.
- Blockchain can also enable smart contracts, which are self-executing agreements that can automate and enforce the terms and conditions of trade finance contracts, such as payment, delivery, and quality assurance.
- Blockchain can digitize the entire trade finance lifecycle with increased security and efficiency. It can enable more transparent governance, decreased processing times, lower capital requirements and reduced risks of fraud, human error, and overall counterparty risk.

#### Use Case 2: Letters of Credit

- A letter of credit (LC) is a common trade finance instrument that guarantees the payment from the buyer's bank to the seller's bank, upon the presentation of the required documents, such as the bill of lading, invoice, and certificate of origin.
- LCs are used to mitigate the risk of non-payment or non-delivery in cross-border trade transactions, especially when the parties are unfamiliar with each other or operate in different legal jurisdictions.
- However, LCs are also cumbersome, expensive, and slow to process, as they involve multiple intermediaries, paper-based documents, manual verification, and reconciliation.
- Blockchain can streamline and simplify the LC process, by enabling the parties to share and verify the documents and payments in real-time, on a secure and immutable ledger.
- Blockchain can also enable smart contracts to automate the issuance, execution, and settlement of LCs, based on predefined rules and triggers, such as the receipt of the goods or the confirmation of the shipment.
- Blockchain can reduce the cost, time, and risk of LC transactions, by eliminating the need for intermediaries, paper-based documents, manual verification, and reconciliation.
- Blockchain can also increase the trust, transparency, and traceability of LC transactions, by providing a single source of truth and a tamper-proof record of the trade events and assets   .



### Invoice Management Discounting for the Notes of the Unit 7 - Use Case 2 in the Subject of Blockchain Architecture Design

- Invoice discounting is a funding option available to small businesses to tide over cash flow vagaries.
- Under the invoice discounting arrangement, the supplier (business) uses the account receivable as collateral to access instant funds to improve the cash flow position.
- The supplier pays a fee to the bank (or the financier) for this service, and the bank collects the full amount from the customer (debtor) when the invoice is due.
- Invoice discounting is a market with a double-digit potential growth rate over the next years in Europe and worldwide.
- The main benefit of invoice discounting is the acceleration of cash flow from customers to suppliers: suppliers get advance payments from the bank rather than waiting for the customers to pay.
- However, invoice discounting also involves some challenges and risks, such as fraud, duplication, verification, reconciliation, and transparency.
- Blockchain technology can offer a solution to these challenges and risks by providing a distributed ledger that records and verifies the transactions and invoices in a secure and transparent way.
- Blockchain can enable businesses to upload their financial data on the chain and only share it with the entity they wish to show the data.
- This enables banks to quickly assess the risk and accordingly disburse the credit in a quick and efficient manner.
- Blockchain can also eliminate the need for on-site audits of receivables and debtors, receivables' notification and debtors' verification, and month-end reconciliation processes.
- Blockchain can reduce the operational costs and risks for both suppliers and banks, and increase the trust and efficiency in the invoice discounting process.
- A blockchain-based invoice discounting system can involve the following steps:
  - The supplier issues an invoice to the customer and uploads it to the blockchain.
  - The bank verifies the invoice and the customer's creditworthiness, and approves the invoice discounting request.
  - The bank transfers the funds to the supplier's account, minus the fee.
  - The customer pays the full invoice amount to the bank when it is due.
  - The blockchain records and updates the transactions and balances of all the parties involved.



## Unit 8 - Use case 3

- Use case 3 is about designing and implementing a chatbot that can answer questions about a specific domain, such as travel, health, or education.
- The main steps involved in use case 3 are:
  - Define the scope and purpose of the chatbot, such as the target audience, the domain knowledge, and the expected functionalities.
  - Collect and analyze data from relevant sources, such as websites, documents, or user feedback, to identify the common questions and intents of the users, as well as the possible answers and actions of the chatbot.
  - Design the chatbot architecture, such as the natural language understanding (NLU) module, the dialogue management (DM) module, and the natural language generation (NLG) module, and choose the appropriate tools and frameworks to implement them.
  - Train and test the chatbot using the collected data, and evaluate its performance and usability using metrics such as accuracy, response time, user satisfaction, and engagement.
  - Deploy and maintain the chatbot on the desired platform, such as a website, a mobile app, or a messaging service, and monitor its usage and feedback, and update it as needed.
- Some of the challenges and best practices of use case 3 are:
  - Ensure the chatbot is consistent, coherent, and relevant in its responses, and avoid giving misleading, inaccurate, or inappropriate information.
  - Handle the user's queries that are out of the scope or domain of the chatbot gracefully, and provide alternative options or referrals when possible.
  - Use a friendly, polite, and engaging tone and style in the chatbot's messages, and adapt to the user's preferences and context.
  - Provide feedback and confirmation to the user's inputs, and allow the user to correct or modify them if needed.
  - Use rich media and interactive elements, such as images, videos, buttons, or links, to enhance the chatbot's functionality and user experience.



### Blockchain for Government

- Blockchain is a technology that enables secure and transparent data sharing among multiple parties over a distributed network.
- Blockchain can improve government services and foster fair and transparent citizen rights by eliminating intermediaries, reducing fraud, waste, and abuse, and increasing trust and accountability.
- Some of the use cases of blockchain for government are:

  - **Digital identity**: Blockchain can provide a decentralized and self-sovereign identity system that allows citizens to control their own personal data and access government services without relying on third-party verifiers. For example, Estonia's e-Residency program allows anyone in the world to obtain a digital identity and access Estonian public and private services online.
  - **Land registry**: Blockchain can enable a secure and immutable record of land ownership and transactions that can prevent disputes, corruption, and forgery. For example, Georgia's land registry department uses blockchain to track land ownership and real estate transactions within the country's borders.
  - **Voting**: Blockchain can enhance the security and transparency of voting systems by allowing voters to cast their ballots anonymously and verifiably over a distributed ledger. For example, Sierra Leone used blockchain to audit the results of its 2018 presidential election.
  - **Supply chain**: Blockchain can improve the efficiency and traceability of government procurement and distribution processes by creating a shared and tamper-proof ledger of goods and services. For example, the World Food Programme uses blockchain to deliver food aid to refugees in Jordan.
  - **Central bank digital currency**: Blockchain can enable central banks to issue and manage digital versions of their national currencies that can facilitate faster and cheaper cross-border payments, financial inclusion, and monetary policy. For example, China's digital yuan is a blockchain-based currency that aims to challenge the dominance of the US dollar in global trade.



### Digital identity for the notes of the Unit 8 - Use case 3 in the subject of Block chain Architecture Design

- Digital identity is the representation of a person, organization, or device in the digital world.
- Blockchain is a distributed ledger technology that enables secure, transparent, and decentralized transactions and data sharing.
- Blockchain can be used to create and manage digital identities that are more secure, interoperable, and user-centric than the traditional identity systems  .
- Some of the benefits of blockchain for digital identity are  :
  - Enhanced security and privacy: Blockchain can protect the identity data from unauthorized access, tampering, and theft by using encryption, hashing, and digital signatures. No personal identifiable information (PII) is stored on the blockchain, but only the references or pointers to the data stored off-chain. Users can control who can access their data and revoke the access at any time.
  - Increased efficiency and convenience: Blockchain can reduce the cost and time of identity verification and authentication by eliminating the need for intermediaries, paper-based processes, and redundant data entry. Users can store their identity data in a digital wallet and share it with the verified parties in a matter of seconds. Issuers can easily connect with others and provide nearly instant verification of credentials.
  - Improved trust and transparency: Blockchain can provide a single source of truth for identity data by creating an immutable and auditable record of the transactions and data changes. Users can verify the authenticity and validity of the identity data and credentials by checking the blockchain ledger. Issuers can ensure the integrity and quality of the identity data and credentials by using blockchain standards and protocols.
- Some of the use cases of blockchain for digital identity are   :
  - Self-sovereign identity: Blockchain can enable users to create and manage their own digital identities without relying on centralized authorities or intermediaries. Users can own and control their identity data and credentials, and decide how, when, and with whom to share them . Self-sovereign identity can empower users to exercise their digital rights and access various services and opportunities .
  - Data monetization: Blockchain can enable users to monetize their identity data and credentials by selling or renting them to the interested parties in a secure and transparent way. Users can set their own terms and conditions for the data sharing, and receive rewards or incentives in the form of cryptocurrencies or tokens. Data monetization can create new revenue streams for users and new business models for data buyers.
  - Data portability: Blockchain can enable users to transfer their identity data and credentials across different platforms, domains, and jurisdictions in a seamless and interoperable way. Users can avoid the hassle of creating multiple accounts, profiles, and passwords, and reuse their existing identity data and credentials for various purposes. Data portability can enhance the user experience and convenience, and foster innovation and competition.
  - Healthcare: Blockchain can enable patients to create and manage their own digital health records and share them with the authorized healthcare providers in a secure and efficient way. Patients can control their health data and consent, and access better and personalized care . Healthcare providers can verify the identity and medical history of the patients, and improve the quality and coordination of care .
  - Financial services: Blockchain can enable customers to create and manage their own digital financial identities and access various financial services and products in a secure and convenient way. Customers can reduce the friction and cost of identity verification and compliance, and access more inclusive and affordable financial services . Financial institutions can verify the identity and creditworthiness of the customers, and offer more tailored and efficient financial services .
  - Supply chain: Blockchain can enable the participants in the supply chain to create and manage their own digital identities and track the provenance and movement of the goods and assets in a secure and transparent way. Participants can ensure the authenticity and quality of the goods and assets, and comply with the regulations and standards . Consumers can verify the origin and history of the goods and assets, and make informed and ethical choices .
  - Web3: Blockchain can



### Land records and other kinds of record keeping between government entities for the notes of the Unit 8 - Use case 3 in the subject of Block chain Architecture Design

- Land records are documents that contain information about the ownership, rights, and transactions of land or real estate properties.
- Land records are important for establishing legal ownership, resolving disputes, preventing fraud, and facilitating transactions.
- Land records are usually maintained by government entities, such as land registries, cadastral agencies, or local authorities.
- However, land records are often outdated, incomplete, inaccurate, or inaccessible, especially in developing countries, where land administration systems are weak or non-existent.
- Blockchain technology is a distributed ledger system that allows multiple parties to share and verify data without relying on a central authority or intermediary.
- Blockchain technology can be used to improve land records by:
  - Creating a transparent, secure, verifiable, and immutable record of land ownership and transactions, that can be accessed by anyone with the appropriate permissions.
  - Reducing the cost, time, and complexity of land registration and transfer, by automating the process using smart contracts, which are self-executing agreements encoded on the blockchain.
  - Enhancing the interoperability and coordination of land records among different government entities, by creating a common platform that can integrate data from various sources and systems.
  - Increasing the trust and confidence of land owners, buyers, sellers, and other stakeholders, by providing a reliable and tamper-proof source of truth for land information.
- Some examples of blockchain-based land records projects are:
  - BloqFile, an Ethereum-based land registry that allows users to create, store, and search land records on the blockchain  .
  - Medici Land Governance, a company that uses blockchain and other technologies, such as cryptography, artificial intelligence, and LiDAR, to modernize land management in countries like Rwanda, Zambia, and Liberia.
  - Bitland, a project that aims to provide land titles and dispute resolution services using blockchain and satellite imagery in Ghana and other African countries.
  - ChromaWay, a company that develops blockchain solutions for land administration, such as the eLand Registry in Sweden and the Land LayBy in Kenya.



### Public Distribution System Social Welfare Systems

- Public distribution system (PDS) is a system where the government creates a supply chain to reach towards the public, such as providing subsidized food and essential commodities to the poor and vulnerable sections of the society.
- Blockchain is an emerging technology that can provide security, transparency, and efficiency to the PDS by recording all transactions and events in a distributed ledger that is immutable, verifiable, and traceable  .
- Some of the benefits of using blockchain in PDS are:
  - It can prevent leakage, corruption, and diversion of the supplies by ensuring that the beneficiaries receive the correct quantity and quality of the goods .
  - It can reduce the intermediaries and the operational costs involved in the PDS by enabling direct and peer-to-peer transactions between the government and the beneficiaries .
  - It can improve the accountability and the governance of the PDS by providing real-time data and feedback on the performance and the impact of the system .
- Some of the challenges of using blockchain in PDS are:
  - It requires a high level of technical expertise, infrastructure, and awareness among the stakeholders to implement and maintain the system .
  - It faces legal, regulatory, and social barriers that may hinder the adoption and the acceptance of the system by the government and the beneficiaries  .
  - It may raise privacy and security issues that need to be addressed by ensuring the protection and the consent of the data and the identity of the beneficiaries  .



### Blockchain Cryptography for the notes of the Unit 8 - Use case 3

- Blockchain cryptography is a method of securing data and transactions on a distributed ledger using cryptographic keys and algorithms.
- Cryptography in blockchain has two main functions: to ensure the integrity and authenticity of data, and to enable privacy and confidentiality of transactions.
- The main cryptographic components of blockchain are hashing, digital signatures, and encryption.
- Hashing is a process of transforming any input data into a fixed-length output, called a hash or a digest, using a mathematical function, called a hash function.
- Hashing ensures the integrity of data, as any change in the input data will result in a different hash, making it easy to detect tampering.
- Hashing also enables the creation of unique identifiers for blocks and transactions, as well as the linking of blocks in a chain using the previous block's hash.
- The most common hash functions used in blockchain are SHA-2 and SHA-3, which produce 256-bit or 512-bit hashes, respectively.
- Digital signatures are a way of proving the authenticity and ownership of data, using a pair of cryptographic keys: a private key and a public key.
- A private key is a secret and random string of bits that is used to sign data, while a public key is derived from the private key and is used to verify the signature.
- A digital signature is generated by applying a hash function to the data, and then encrypting the hash with the private key.
- A digital signature can be verified by decrypting the signature with the public key, and comparing the resulting hash with the hash of the data.
- Digital signatures ensure that only the owner of the private key can sign data, and that the data has not been altered after signing.
- Digital signatures also enable the creation of digital identities and wallets for blockchain users, as well as the authorization of transactions.
- Encryption is a process of transforming data into an unreadable form, using a secret key and an algorithm, called a cipher.
- Encryption ensures the privacy and confidentiality of data, as only the holder of the secret key can decrypt the data and access its original form.
- Encryption can be symmetric or asymmetric, depending on whether the same key or different keys are used for encryption and decryption.
- Symmetric encryption uses the same key for both encryption and decryption, and is faster and more efficient than asymmetric encryption.
- Symmetric encryption is used to encrypt the data within blocks, as well as to secure the communication between nodes in a blockchain network.
- Asymmetric encryption uses different keys for encryption and decryption, and is also known as public-key encryption.
- Asymmetric encryption is used to encrypt and decrypt the digital signatures, as well as to establish secure connections between nodes using protocols such as SSL/TLS.
- The most common encryption algorithms used in blockchain are AES for symmetric encryption, and RSA or ECDSA for asymmetric encryption.

- Use case 3: Blockchain for cybersecurity
- Blockchain can be used to enhance the security of various domains and applications, such as identity management, access control, data protection, and IoT.
- Some of the benefits of blockchain for cybersecurity are:

  - Decentralization: Blockchain eliminates the need for centralized servers or intermediaries, which are often the targets of cyberattacks. By distributing the data and transactions across a network of nodes, blockchain reduces the risk of single points of failure, data breaches, or denial-of-service attacks.
  - Immutability: Blockchain ensures that the data and transactions on the ledger are immutable, meaning that they cannot be modified or deleted once recorded. This prevents data tampering, fraud, or corruption, and enables the verification and auditability of data history.
  - Cryptography: Blockchain uses cryptography to secure the data and transactions on the ledger, as well as the communication and identity of the nodes. This prevents unauthorized access, modification, or disclosure of data, and ensures the authenticity and ownership of data.
  - Consensus: Blockchain uses consensus mechanisms to validate and confirm the data and transactions on the ledger, as well as to maintain the synchronization and agreement of the nodes. This prevents malicious or faulty nodes from compromising the integrity or availability of the ledger, and enables the detection and resolution of conflicts or errors.

- Some of the challenges of blockchain



### Privacy and Security on Blockchain

- Privacy and security are two important aspects of blockchain technology that affect its adoption and use cases.
- Privacy refers to the ability of users to control their own data and identity, and to protect them from unauthorized access or disclosure.
- Security refers to the ability of the system to resist attacks and ensure the integrity, availability, and authenticity of the data and transactions.
- Some of the privacy and security challenges and solutions in blockchain are:

  - **Public and private keys**: Blockchain systems use asymmetric cryptography to secure transactions between users. Each user has a public and private key. The public key is used to identify the user and verify their signature, while the private key is used to sign and encrypt the transactions. The private key should be kept secret and protected from loss or theft. Users can also use different public keys for different transactions to enhance their privacy .
  - **Data privacy**: Blockchain transactions are recorded and stored on a distributed ledger that is shared and synchronized among all the nodes in the network. This means that anyone can see the transaction history and data of any user or address. This can pose a risk to the privacy of the users, especially if the data contains sensitive or personal information. Some of the solutions to improve data privacy include: using encryption, zero-knowledge proofs, or homomorphic encryption to hide the data content; using mixing, shuffling, or ring signatures to obfuscate the data origin or destination; using permissioned or private blockchains to restrict the data access or visibility  .
  - **Secure communication**: Blockchain nodes communicate with each other through a peer-to-peer network that can be vulnerable to attacks such as eavesdropping, spoofing, or denial-of-service. To ensure secure communication, blockchain nodes should use encryption, authentication, and verification protocols to protect the data transmission and prevent malicious interference .
  - **Smart contract security**: Smart contracts are self-executing programs that run on the blockchain and enforce the rules and logic of the transactions. Smart contracts can enable automation, efficiency, and transparency, but they can also introduce new security risks such as bugs, errors, or vulnerabilities that can be exploited by attackers. To ensure smart contract security, developers should use formal verification, testing, auditing, and monitoring tools to detect and fix any flaws or defects in the code  .
  - **Identity and access management**: Blockchain systems rely on digital identities to identify and authenticate the users and entities involved in the transactions. Identity and access management is the process of managing the creation, verification, and authorization of the digital identities and their associated permissions and roles. Identity and access management can enhance the privacy and security of the users by allowing them to control their own identity and data, and by preventing unauthorized or fraudulent access or transactions  .
  - **Key management**: Key management is the process of generating, storing, and managing the cryptographic keys that are used to sign and encrypt the transactions and data on the blockchain. Key management is crucial for the privacy and security of the users, as the keys are the only proof of ownership and authorization on the blockchain. Key management can be challenging, as the users have to keep their keys safe and accessible, and avoid losing or compromising them. Some of the solutions to improve key management include: using hardware or software wallets, multi-signature schemes, or threshold cryptography to store and protect the keys; using recovery or backup mechanisms, or key rotation or revocation protocols to restore or update the keys  .

