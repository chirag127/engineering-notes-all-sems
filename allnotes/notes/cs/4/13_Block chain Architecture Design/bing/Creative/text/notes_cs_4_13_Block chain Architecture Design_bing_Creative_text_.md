

## Unit 1 - Introduction to Blockchain

- Blockchain is a distributed ledger technology that allows multiple parties to securely store, verify, and share data without relying on a central authority.
- Blockchain consists of a network of nodes that communicate using a consensus protocol to maintain a shared and immutable record of transactions, events, or any other information.
- Blockchain can be used for various applications, such as cryptocurrencies, smart contracts, supply chain management, digital identity, voting, and more.
- Blockchain has several advantages over traditional databases, such as transparency, security, immutability, decentralization, and trustlessness.
- Blockchain also has some challenges and limitations, such as scalability, privacy, interoperability, governance, and regulation.



### Digital Money to Distributed Ledgers

- Digital money is a form of electronic money that can be used to store, transfer, and exchange value digitally without the need for physical cash or intermediaries.
- Digital money can be classified into two types: centralized and decentralized. Centralized digital money is issued and controlled by a single authority, such as a central bank or a private company. Decentralized digital money is created and managed by a network of users, such as a cryptocurrency or a community currency.
- Distributed ledgers are systems that record and synchronize data across multiple nodes or devices in a network, without the need for a central authority or intermediary. Distributed ledgers can provide transparency, security, and efficiency for data transactions and verification.
- Distributed ledgers can be implemented using different technologies, such as blockchain, hashgraph, directed acyclic graph (DAG), or holochain. Each technology has its own advantages and disadvantages in terms of scalability, performance, consensus, and security.
- Blockchain is the most popular and widely used distributed ledger technology. It is a system of linked blocks that contain data and a cryptographic hash of the previous block, forming a chain of immutable records. Blockchain can be used to create and manage digital currencies, such as Bitcoin, as well as other applications, such as smart contracts, digital identity, and supply chain management.
- Bitcoin was the first digital currency to use blockchain technology to solve the double-spending problem in a decentralized way. It functions by linking transactions in a public ledger that is verified by a network of nodes using a proof-of-work (PoW) algorithm. Bitcoin has inspired many other cryptocurrencies and blockchain platforms, such as Ethereum, Litecoin, and Ripple.
- Distributed ledger technology has the potential to transform the financial sector, as well as other industries and sectors, by enabling faster, cheaper, and more secure transactions, reducing intermediation and fraud, and increasing financial inclusion and innovation. However, it also faces many challenges and risks, such as regulatory uncertainty, technical complexity, scalability limitations, and cyberattacks.



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



### Protocols for the notes of the Unit 1 - Introduction to Blockchain in the subject of Block chain Architecture Design

- A protocol is a set of rules and standards that define how different entities communicate and interact with each other.
- A blockchain is a distributed ledger that records transactions and events in a secure, verifiable, and immutable way.
- A blockchain protocol is a set of rules and standards that define how a blockchain operates, such as how transactions are validated, how blocks are created, how consensus is reached, and how data is stored and shared.
- Some examples of blockchain protocols are Bitcoin, Ethereum, Hyperledger Fabric, and Corda.
- Blockchain protocols can be classified into different types based on various criteria, such as:
  - The level of decentralization: public, private, or hybrid.
  - The consensus mechanism: proof-of-work, proof-of-stake, proof-of-authority, or others.
  - The smart contract functionality: Turing-complete, Turing-incomplete, or none.
  - The scalability and performance: sharding, sidechains, layer 2 solutions, or others.
- Blockchain protocols can also be designed for specific purposes and applications, such as finance, supply chain, identity, healthcare, or others.
- Blockchain protocols can be compared and evaluated based on various metrics, such as:
  - Security: the ability to resist attacks and ensure data integrity and availability.
  - Efficiency: the use of resources and the speed of transactions and confirmations.
  - Scalability: the ability to handle increasing demand and volume of transactions and users.
  - Interoperability: the ability to communicate and exchange data with other blockchains and systems.
  - Governance: the process and mechanism of decision making and updating the protocol.



### Security for the notes of the Unit 1 - Introduction to Blockchain in the subject of Block chain Architecture Design

- Security is a crucial aspect of blockchain technology, as it ensures the integrity, confidentiality and availability of the data stored and exchanged on the network.
- Security in blockchain is based on the following principles:
  - Cryptography: Blockchain networks use cryptographic algorithms to secure transactions and data. This means that the security of the network depends on the strength of the cryptographic algorithms and the keys used to encrypt and decrypt the data .
  - Decentralization: Blockchain networks are distributed among multiple nodes, each of which maintains a copy of the ledger. This means that there is no single point of failure or control, and that the network can resist attacks or censorship by malicious actors .
  - Consensus: Blockchain networks use consensus mechanisms to ensure that all nodes agree on the state of the ledger and validate transactions. This means that the network can prevent double-spending, fraud and tampering, and that the transactions are irreversible .
- Security in blockchain is also a comprehensive risk management system, which involves using cybersecurity frameworks, assurance services and best practices to reduce the risks of attacks and fraud .
- Security in blockchain is a dynamic and evolving field, as new threats and challenges emerge with the development and adoption of the technology. Some of the current and future security issues in blockchain include:
  - Cryptojacking: This is a type of malware that hijacks the computing resources of infected devices to mine cryptocurrencies without the user's consent or knowledge.
  - Rug pulls: This is a type of scam that involves the creators of a decentralized application (DApp) or a decentralized finance (DeFi) project withdrawing or stealing the funds invested by the users, leaving them with worthless tokens or contracts.
  - 51% attacks: This is a type of attack that involves a malicious actor gaining control of more than 50% of the network's computing power, which allows them to manipulate the ledger, reverse transactions, double-spend or halt the network.
  - Quantum computing: This is a type of computing that uses quantum physics to perform operations that are faster and more powerful than classical computers. This poses a potential threat to the security of blockchain networks, as quantum computers could break the cryptographic algorithms and keys that secure the data.



### Consensus for the notes of the Unit 1 - Introduction to Blockchain in the subject of Block chain Architecture Design

- Consensus is the process of reaching agreement among a group of participants on a shared state of a system.
- Consensus is essential for blockchain systems, which are distributed, decentralized, and trustless networks of nodes that maintain a shared ledger of transactions.
- Consensus ensures that all nodes in the network have the same view of the ledger, and that any changes to the ledger are valid and consistent with the rules of the system.
- Consensus also prevents malicious or faulty nodes from compromising the integrity, security, or availability of the system.
- There are different types of consensus algorithms that vary in their design, assumptions, performance, and security properties.
- Some of the common consensus algorithms used in blockchain systems are:
  - Proof-of-Work (PoW): A node has to solve a computationally hard puzzle to propose a new block to the ledger. The other nodes validate the solution and the transactions in the block. The node that solves the puzzle receives a reward for its work. PoW is used by Bitcoin, Ethereum, and other cryptocurrencies.
  - Proof-of-Stake (PoS): A node has to stake some amount of its own tokens to participate in the consensus process. The node with the highest stake or a random selection of staked nodes gets to propose a new block to the ledger. The other nodes validate the block and the transactions in it. The node that proposes the block receives a reward for its stake. PoS is used by Cardano, Polkadot, and other cryptocurrencies.
  - Proof-of-Authority (PoA): A node has to be authorized by a trusted entity or a set of entities to propose a new block to the ledger. The other nodes validate the block and the transactions in it. The node that proposes the block receives a reward for its authority. PoA is used by private or permissioned blockchains, such as Quorum, Hyperledger, and Binance Smart Chain.
  - Byzantine Fault Tolerance (BFT): A node has to communicate with a quorum of other nodes to reach a consensus on a new block to the ledger. The nodes use a voting mechanism to agree on the block and the transactions in it. The node that proposes the block receives a reward for its participation. BFT is used by public or permissionless blockchains, such as Stellar, Ripple, and Cosmos.



### Permissions for the notes of the Unit 1 - Introduction to Blockchain in the subject of Block chain Architecture Design

- Permissions are the rules that define who can access, modify, or delete the notes of the Unit 1 - Introduction to Blockchain in the subject of Block chain Architecture Design.
- Permissions can be set by the owner or creator of the notes, or by the administrator of the platform where the notes are stored or shared.
- Permissions can be classified into three types: read, write, and execute.
  - Read permission allows the user to view the content of the notes, but not to edit or delete them.
  - Write permission allows the user to edit or delete the content of the notes, but not to execute them.
  - Execute permission allows the user to run the notes as a program or script, if they contain executable code.
- Permissions can be granted or denied to different users or groups of users, depending on their roles, identities, or affiliations.
  - For example, the owner of the notes can grant read and write permissions to the instructor and the teaching assistants of the subject, but only read permission to the other students.
  - Alternatively, the owner of the notes can grant read and write permissions to anyone who has a valid email address from the university domain, but deny access to anyone else.
- Permissions can be enforced by different mechanisms, such as passwords, encryption, digital signatures, or smart contracts.
  - For example, the owner of the notes can encrypt the notes with a secret key, and only share the key with the authorized users.
  - Alternatively, the owner of the notes can sign the notes with a digital signature, and only allow the users who can verify the signature to access the notes.
  - Alternatively, the owner of the notes can store the notes on a blockchain platform, and use a smart contract to control the access and modification of the notes.



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
- The private key is used to sign the transactions and to decrypt the data that is encrypted with the public key .
- The private key should be kept secret and never shared with anyone .
- The public key can be seen as a pseudonym that protects the real identity of the user .
- However, pseudonymity is not the same as anonymity, and there are ways to link the public key to the real identity of the user, such as through network analysis, metadata, or third-party services .
- Therefore, privacy in blockchains is not guaranteed by default and requires additional measures to enhance it .
- There are different types of blockchains that offer different levels of privacy, such as public, private, or hybrid blockchains.
- Public blockchains are open to anyone who wishes to join and participate in the network, such as Bitcoin or Ethereum.
- Public blockchains are transparent and decentralized, but they also expose the transaction history and the balance of each user to anyone who can access the blockchain.
- Private blockchains are restricted to a specific group of authorized participants, such as a consortium or an organization.
- Private blockchains are more centralized and less transparent, but they also offer more control and privacy over the data and the transactions.
- Hybrid blockchains are a combination of public and private blockchains, where some parts of the data or the transactions are public and some are private.
- Hybrid blockchains aim to balance the trade-offs between transparency and privacy, security and scalability, and trust and efficiency.
- There are also various techniques and tools that can enhance privacy in blockchains, such as encryption, zero-knowledge proofs, ring signatures, mixers, or privacy coins .
- Encryption is the process of transforming data into an unreadable form that can only be decrypted with the corresponding key .
- Encryption can be used to protect the confidentiality and the integrity of the data and the transactions on the blockchain .
- Zero-knowledge proofs are a cryptographic method that allows one party to prove to another party that a statement is true without revealing any information beyond the validity of the statement .
- Zero-knowledge proofs can be used to verify the correctness and the validity of the transactions on the blockchain without disclosing the details of the transactions, such as the sender, the receiver, or the amount .
- Ring signatures are a cryptographic technique that allows a user to sign a message on behalf of a group of users without revealing which user in the group is the actual signer .
- Ring signatures can be used to obfuscate the identity of the sender of a transaction on the blockchain by mixing the public keys of the sender with the public keys of other users in the network .
- Mixers are services that pool and mix the transactions of different users on the blockchain to break the link between the sender and the receiver of the transactions[^2^



### Blockchain Architecture and Design

Blockchain is a distributed ledger technology that enables peer-to-peer transactions without intermediaries. Blockchain architecture and design are the key aspects of building and deploying blockchain solutions for various use cases. Some of the main components and concepts of blockchain architecture and design are:

- **Node**: A node is a user or a computer that participates in the blockchain network by running a software that validates and relays transactions. Nodes can have different roles and permissions depending on the type of blockchain. For example, in a public blockchain, anyone can join as a node and verify transactions, while in a private blockchain, only authorized nodes can access the network and perform transactions.
- **Block**: A block is a data structure that stores a set of transactions and other information, such as the block header, the block hash, the previous block hash, the nonce, and the merkle root. A block is created by a node that solves a cryptographic puzzle, known as proof-of-work, and broadcasts it to the network. Other nodes validate the block and add it to their copy of the ledger, forming a chain of blocks.
- **Transaction**: A transaction is the smallest unit of data that can be recorded on the blockchain. A transaction contains the details of the sender, the receiver, the amount, and the timestamp of the transfer. Transactions are digitally signed by the sender using a private key, and verified by the receiver using a public key. Transactions are grouped together in blocks and appended to the ledger.
- **Consensus**: Consensus is the mechanism that ensures that all nodes in the network agree on the state of the ledger and the validity of the transactions. Consensus prevents double-spending, malicious attacks, and network forks. Different types of consensus algorithms exist, such as proof-of-work, proof-of-stake, proof-of-authority, and Byzantine fault tolerance.
- **Smart contract**: A smart contract is a self-executing program that runs on the blockchain and defines the rules and logic of a transaction or a business process. Smart contracts can automate complex workflows, enforce contractual agreements, and create decentralized applications. Smart contracts are written in a specific programming language, such as Solidity, and deployed on the blockchain.



### Basic crypto primitives for the notes of the Unit 1 - Introduction to Blockchain in the subject of Block chain Architecture Design

- Cryptographic primitives are the low-level algorithms that are used to build cryptographic protocols for a strong secured network.
- They are the basic building blocks of the cryptosystem and the programmers develop new cryptographic algorithms with the help of cryptographic primitives.
- Basic cryptographic primitives include the hash functions, digital signature, encryption primitives, and randomized algorithms which are incorporated in Blockchain.
- Below are some of the common cryptographic primitives:
  - One way Hash Functions: It is a mathematical function used to encrypt variable length data to fixed binary data. It is a one-way function, meaning that it is easy to compute the hash value for a given message, but hard to find the message that corresponds to a given hash value. Examples of hash functions are SHA-256, SHA-512, and Ethash.
  - Symmetric Key cryptography: This is also known as Symmetric Encryption. It is a method of encryption where the same key is used to encrypt and decrypt the data. The key is shared between the sender and the receiver of the data. Examples of symmetric key algorithms are AES, DES, and RC4.
  - Asymmetric key cryptography: It is also known as public key cryptography. It is a method of encryption where two different keys are used to encrypt and decrypt the data. One key is public and can be shared with anyone, while the other key is private and kept secret by the owner. The public key is used to encrypt the data, while the private key is used to decrypt the data. Examples of asymmetric key algorithms are RSA, ECC, and ElGamal.
  - Randomized Algorithms: These algorithms produce random ciphertexts for encryption. They use a random number generator to generate a random key or a random nonce (a number used only once) to encrypt the data. The randomness ensures that the same plaintext will produce different ciphertexts each time it is encrypted. Examples of randomized algorithms are CTR, CBC, and GCM modes of operation for block ciphers.



### Hash

- A hash is a mathematical function that takes any input and produces a fixed-length output, also called a digest or a fingerprint.
- A hash function has the following properties:
  - It is deterministic, meaning that the same input always produces the same output.
  - It is one-way, meaning that it is easy to compute the output from the input, but hard to find the input from the output.
  - It is collision-resistant, meaning that it is hard to find two different inputs that produce the same output.
- A hash function can be used to verify the integrity and authenticity of data, by comparing the hash of the original data with the hash of the received data.
- A hash function can also be used to index data, by mapping the input to a smaller space of possible outputs, such as a table or a list.
- A hash function can also be used to anonymize data, by hiding the identity or the content of the input, while preserving some properties of the input, such as its frequency or its relation to other inputs.
- A hash function can also be used to generate random numbers, by applying the hash function to a seed or a nonce, and extracting some bits from the output.
- A hash function can also be used to create digital signatures, by combining the hash of the data with a secret key, and verifying the signature with a public key.
- A hash function can also be used to create proof-of-work, by requiring the output of the hash function to satisfy some difficulty criteria, such as having a certain number of leading zeros.
- A hash function can also be used to create hash-based data structures, such as hash tables, hash lists, hash trees, or hash chains, which can store, retrieve, or verify data efficiently.
- A hash function can also be used to create hash-based cryptography, such as hash-based message authentication codes (HMACs), hash-based signatures (HBSs), or hash-based encryption (HBE).
- A hash function can also be used to create hash-based protocols, such as hash-based commitment schemes, hash-based zero-knowledge proofs, or hash-based consensus algorithms.



### Signature for the notes of the Unit 1 - Introduction to Blockchain in the subject of Block chain Architecture Design

- A signature is a cryptographic mechanism that allows a user to prove their identity and ownership of a message or a transaction.
- A signature consists of two components: a public key and a private key.
- A public key is a string of characters that can be shared with anyone and used to verify a signature. A private key is a secret string of characters that can be used to generate a signature. A user should never reveal their private key to anyone.
- A signature is generated by applying a mathematical function, called a signing algorithm, to a message or a transaction and a private key. The output of the function is a unique string of characters, called a signature.
- A signature can be verified by applying another mathematical function, called a verification algorithm, to the message or transaction, the signature, and the public key. The output of the function is a boolean value, either true or false, indicating whether the signature is valid or not.
- A signature is valid if and only if it was generated by the same private key that corresponds to the public key used for verification, and the message or transaction has not been altered or tampered with.
- A signature provides two main properties: authenticity and non-repudiation.
- Authenticity means that the signature proves that the message or transaction was sent by the owner of the private key, and not by an impostor or a malicious actor.
- Non-repudiation means that the signature prevents the owner of the private key from denying that they sent the message or transaction, or claiming that it was forged or modified by someone else.
- A signature is essential for blockchain systems, as it allows users to securely and verifiably exchange information and value without relying on a trusted third party or intermediary.



### Hashchain to Blockchain

- A hashchain is a data structure that applies a cryptographic hash function to a piece of data repeatedly, producing a sequence of hash values that are linked to each other.
- A hashchain can be used to generate many one-time keys from a single key or password, or to record the chronology of data's existence.
- A blockchain is a data structure that stores data in blocks, where each block contains a hash of the previous block, forming a chain of blocks.
- A blockchain can be used to secure information and make the ledger immutable, as any tampering with a block would invalidate the subsequent blocks' hashes.
- A blockchain is a type of hashchain, but not all hashchains are blockchains. A blockchain has additional features, such as consensus mechanisms, peer-to-peer networks, and smart contracts, that enable distributed, decentralized, and programmable applications .
- A hashchain is a simpler and more efficient data structure than a blockchain, but it has less functionality and security. A hashchain can be used for specific purposes, such as authentication, digital signatures, or proof-of-work, but it cannot support general-purpose applications or transactions.



### Basic consensus mechanisms for the notes of the Unit 1 - Introduction to Blockchain in the subject of Block chain Architecture Design

- A consensus mechanism is any method used to achieve agreement, trust, and security across a decentralized computer network.
- In the context of blockchains and cryptocurrencies, consensus mechanisms are essential for ensuring the validity and integrity of the shared ledger, as well as preventing malicious attacks and double-spending.
- There are different types of consensus mechanisms, each with its own advantages and disadvantages. Some of the most common ones are:
  - Proof-of-work (PoW): This mechanism requires the network validators, or miners, to solve complex mathematical puzzles in order to create new blocks and earn rewards. The difficulty of the puzzles adjusts according to the network's hash rate, or computing power. PoW is used by Bitcoin, Ethereum, and many other blockchains. PoW provides a high level of security and decentralization, but it also consumes a lot of energy and resources, and it is vulnerable to 51% attacks  .
  - Proof-of-stake (PoS): This mechanism assigns the right to create new blocks and earn rewards to the network validators, or stakers, based on the amount of coins they have locked up as stake. The more stake a validator has, the higher the chance of being selected as the next block producer. PoS is used by Cardano, Polkadot, and many other blockchains. PoS is more energy-efficient and scalable than PoW, but it also poses some challenges, such as the risk of centralization, the lack of incentives for network security, and the possibility of nothing-at-stake attacks  .
  - Delegated proof-of-stake (DPoS): This mechanism is a variation of PoS, where the network validators, or delegates, are elected by the coin holders based on their stake. The delegates are responsible for creating new blocks and maintaining the network, while the coin holders can vote them out if they misbehave. DPoS is used by EOS, Tron, and many other blockchains. DPoS is faster and more flexible than PoS, but it also sacrifices some decentralization and security, and it may lead to collusion and corruption among the delegates.
  - Proof-of-authority (PoA): This mechanism relies on a set of pre-approved validators, or authorities, who are trusted by the network to create new blocks and validate transactions. The authorities are usually chosen based on their reputation, identity, or expertise. PoA is used by VeChain, xDai, and many other blockchains. PoA is suitable for private or permissioned blockchains, where speed and efficiency are more important than decentralization and censorship-resistance. However, PoA is not very transparent or democratic, and it depends on the honesty and competence of the authorities.
  - Byzantine fault tolerance (BFT): This mechanism is based on a mathematical solution to the Byzantine generals' problem, which is a classic dilemma of how to achieve consensus among distributed nodes that may be faulty or malicious. BFT algorithms allow the network to reach agreement as long as less than a third of the nodes are dishonest. BFT is used by Stellar, NEO, and many other blockchains. BFT is fast and secure, but it also requires a small and fixed number of validators, which limits its scalability and decentralization.



## Unit 2 - Consensus

- Consensus is the process of reaching agreement among a group of participants on a common state or value.
- Consensus is essential for distributed systems that need to coordinate their actions and maintain consistency across multiple replicas or nodes.
- Consensus can be achieved by using various algorithms or protocols, such as Paxos, Raft, Byzantine Fault Tolerance, Proof of Work, Proof of Stake, etc.
- Consensus algorithms or protocols have different properties and trade-offs, such as fault tolerance, availability, latency, throughput, scalability, security, etc.
- Consensus algorithms or protocols can be classified into two categories: leader-based and leaderless.
  - Leader-based consensus algorithms or protocols elect a leader or a coordinator among the participants, who is responsible for proposing and committing values, and resolving conflicts. Examples are Paxos and Raft.
  - Leaderless consensus algorithms or protocols do not rely on a leader or a coordinator, but instead allow participants to propose and commit values independently, and use some form of voting or validation to reach agreement. Examples are Byzantine Fault Tolerance, Proof of Work, and Proof of Stake.
- Consensus algorithms or protocols can also be classified into two categories: deterministic and probabilistic.
  - Deterministic consensus algorithms or protocols guarantee that the participants will eventually agree on the same value, as long as a certain number or fraction of them are honest and reachable. Examples are Paxos, Raft, and Byzantine Fault Tolerance.
  - Probabilistic consensus algorithms or protocols do not guarantee that the participants will agree on the same value, but instead make it very unlikely that they will disagree, by using randomization or incentives. Examples are Proof of Work and Proof of Stake.



### Requirements for the consensus protocols for the nodes of the Unit 2 - Consensus in the subject of Blockchain Architecture Design

- A consensus protocol is a set of rules that determines how a decentralized computer network reaches agreement on which transactions are valid and which are not .
- A consensus protocol prevents a single entity from controlling a blockchain or distorting the “truth” of what should be recorded.
- A consensus protocol ensures that all participating nodes agree on the state of a blockchain and that the blockchain is immutable, consistent, and secure .
- A consensus protocol should be able to handle various scenarios, such as network latency, malicious nodes, network partitioning, and scalability .
- A consensus protocol should also be able to balance the trade-offs between decentralization, security, and performance .
- Some of the common consensus protocols used in blockchain networks are Proof of Work (PoW), Proof of Stake (PoS), Delegated Proof of Stake (DPoS), Byzantine Fault Tolerance (BFT), and Practical Byzantine Fault Tolerance (PBFT) .
- Each consensus protocol has its own advantages and disadvantages, and different protocols may suit different use cases and requirements .



### Proof of Work (PoW) for the notes of the Unit 2 - Consensus in the subject of Block chain Architecture Design

- Proof of work (PoW) is a **decentralized system** used to verify the accuracy of transactions on the blockchain network  .
- Proof of work removes the need for a central authority like a bank, business, or government agency to monitor and manage transactions and their corresponding accounts .
- Proof of work lets blockchain networks operate by **consensus rules** rather than “trust.”
- Proof of work involves the following steps:
  - When a new transaction is broadcasted to the network, it is added to a pool of unconfirmed transactions.
  - A group of unconfirmed transactions is formed into a block, which has a header that contains metadata such as the previous block's hash, the timestamp, and a nonce (a random number).
  - The block header is then hashed using a cryptographic function, such as SHA-256, to produce a fixed-length output called a hash or a digest.
  - The hash must satisfy a certain condition, such as having a specific number of leading zeros, to be considered valid. This condition is called the **difficulty** and it determines how hard it is to find a valid hash.
  - The process of finding a valid hash is called **mining** and it requires a lot of computational power and energy. The miners are the nodes that compete to find a valid hash and earn a reward for doing so.
  - The first miner to find a valid hash broadcasts the block to the network, where other nodes verify the hash and the transactions in the block.
  - If the block is valid, it is added to the blockchain and the transactions are confirmed. The miner also receives a reward in the form of newly created coins and transaction fees.
  - The process repeats for the next block, using the hash of the previous block as an input.
- Proof of work provides the following benefits:
  - It ensures the **security** of the network by making it costly and difficult for malicious actors to tamper with the blockchain or create fake transactions.
  - It ensures the **immutability** of the blockchain by creating a chain of blocks that are linked by hashes, making it impossible to alter or delete previous blocks without invalidating the subsequent ones.
  - It ensures the **fairness** of the network by rewarding the miners for their contribution and incentivizing them to follow the consensus rules.
- Proof of work also has some drawbacks:
  - It consumes a lot of **energy** and generates a lot of **heat** and **noise**, which have environmental and social impacts.
  - It creates a **scalability** problem, as the network can only process a limited number of transactions per second, depending on the block size and the block time.
  - It creates a **centralization** risk, as the mining power becomes concentrated in the hands of a few large and powerful entities, such as mining pools or corporations, which can influence the network or collude to attack it.



### Scalability aspects of Blockchain consensus protocols

- Scalability is the ability of a blockchain to support high transactional throughput and future growth without compromising its performance, security, or decentralization.
- Scalability is one of the main challenges faced by blockchain systems, especially those that aim to achieve global adoption and support a variety of use cases.
- Scalability is often considered as part of the "scalability trilemma", which states that it is impossible to achieve optimal levels of decentralization, security, and scalability simultaneously in a blockchain system.
- Different blockchain consensus protocols have different trade-offs and approaches to address the scalability challenge, depending on their design goals, assumptions, and limitations.
- Some of the factors that affect the scalability of blockchain consensus protocols are:
  - The size and frequency of blocks: Larger and more frequent blocks can increase the transaction throughput, but also increase the network bandwidth and storage requirements, and the risk of forks and orphaned blocks.
  - The number and diversity of nodes: More and diverse nodes can enhance the decentralization and security of the network, but also increase the communication overhead and the difficulty of reaching consensus.
  - The complexity and validity of transactions: Complex and valid transactions can enable more functionality and use cases, but also increase the computational and verification costs, and the potential for invalid or malicious transactions.
  - The consensus algorithm and parameters: The consensus algorithm and parameters determine the rules and incentives for reaching agreement among the nodes, and affect the speed, finality, and robustness of the consensus process.
- Some of the strategies and techniques that have been proposed or implemented to improve the scalability of blockchain consensus protocols are:
  - Sharding: Sharding is the process of dividing the network into smaller and parallel subnetworks, each with its own subset of nodes, transactions, and blocks, and a local consensus mechanism. Sharding can reduce the load and latency of the network, and increase the transaction throughput, but also introduce new challenges such as cross-shard communication, security, and coordination.
  - Layering: Layering is the process of creating additional layers on top of the base layer of the blockchain, such as second-layer protocols, sidechains, or off-chain solutions. Layering can enable faster and cheaper transactions, and more functionality and scalability, but also rely on different assumptions, trade-offs, and trust models than the base layer.
  - Optimizing: Optimizing is the process of improving the efficiency and performance of the existing consensus protocols, such as by using more advanced cryptographic techniques, reducing the block size or time, adjusting the difficulty or reward, or introducing new consensus rules or mechanisms.



## Unit 3 - Permissioned Blockchains

- A permissioned blockchain is a distributed ledger that is not publicly accessible. It can only be accessed by users with permissions .
- Permissioned blockchains provide an additional level of security over typical blockchain systems like Bitcoin, as they require an access control layer. These blockchains are favored by entities who require security, identity, and role definition within the blockchain.
- Permissioned blockchains can be classified into two types: private and consortium.
  - A private blockchain is a blockchain that is controlled by a single entity, such as a company or an organization. The entity can decide who can join, read, write, and validate transactions on the blockchain. An example of a private blockchain is Hyperledger Fabric.
  - A consortium blockchain is a blockchain that is controlled by a group of entities, such as a consortium or an alliance. The group can decide who can join, read, write, and validate transactions on the blockchain. An example of a consortium blockchain is R3 Corda.
- Permissioned blockchains have some advantages and disadvantages compared to permissionless blockchains.
  - Advantages:
    - Higher scalability: Permissioned blockchains can process more transactions per second, as they have fewer nodes and less consensus overhead.
    - Lower cost: Permissioned blockchains can reduce the cost of transactions, as they do not require fees or incentives for miners or validators.
    - Higher privacy: Permissioned blockchains can protect the confidentiality of transactions and data, as they can restrict the access and visibility of the ledger.
    - Higher compliance: Permissioned blockchains can comply with the regulations and standards of the industry or the jurisdiction, as they can enforce the rules and policies of the governing entity or group.
  - Disadvantages:
    - Lower decentralization: Permissioned blockchains have a higher degree of centralization, as they depend on the authority and trust of the entity or group that controls the blockchain.
    - Lower innovation: Permissioned blockchains have a lower degree of openness, as they limit the participation and contribution of the community and the developers.
    - Lower interoperability: Permissioned blockchains have a lower degree of compatibility, as they may not be able to communicate or exchange data with other blockchains or systems.



### Design goals for the notes of the Unit 3 - Permissioned Blockchains in the subject of Block chain Architecture Design

- The notes should provide a clear and concise overview of the main concepts, features, and challenges of permissioned blockchains.
- The notes should explain the differences and similarities between permissioned and permissionless blockchains, and the trade-offs involved in choosing one over the other.
- The notes should cover the following topics:
  - The definition and characteristics of permissioned blockchains, such as identity management, access control, governance, consensus, and scalability.
  - The advantages and disadvantages of permissioned blockchains, such as security, privacy, efficiency, interoperability, and compliance.
  - The use cases and applications of permissioned blockchains, such as supply chain management, trade finance, healthcare, and digital identity.
  - The examples and platforms of permissioned blockchains, such as Hyperledger Fabric, Corda, Quorum, and Binance Smart Chain.
- The notes should include diagrams, tables, and code snippets to illustrate the concepts and examples of permissioned blockchains.
- The notes should provide references and links to additional resources for further reading and learning.



### Consensus protocols for Permissioned Blockchains

- A consensus protocol is a mechanism that allows all the nodes in a distributed network to agree on the current state of the shared ledger, without relying on a central authority or intermediary .
- A consensus protocol is essential for maintaining the security, integrity, and consistency of the blockchain data, as well as preventing malicious attacks or faulty nodes from compromising the network.
- In a permissioned blockchain, all the nodes are known and authorized to participate in the network, unlike in a public or permissionless blockchain, where anyone can join or leave the network at any time .
- However, a permissioned blockchain still requires a consensus protocol, because not all the nodes can be trusted to act honestly or correctly, and there may be conflicts or disputes among the nodes regarding the validity or order of the transactions .
- A permissioned blockchain can use different types of consensus protocols, depending on the level of decentralization, scalability, performance, and security required by the network .
- Some of the common consensus protocols for permissioned blockchains are:

  - **Proof of Authority (PoA)**: This protocol assigns a set of validators or authorities who are responsible for validating and appending the transactions to the ledger. The validators are chosen based on their reputation, identity, or stake in the network. The protocol is fast, efficient, and scalable, but it sacrifices some degree of decentralization and trustlessness, as the validators have more power and influence over the network.
  - **Proof of Stake (PoS)**: This protocol selects a validator or leader for each block based on their stake or amount of cryptocurrency they have locked in the network. The validator proposes the block and other nodes vote on its acceptance. The protocol is more decentralized, secure, and energy-efficient than PoW, but it may suffer from low participation, centralization of wealth, or long-range attacks.
  - **Delegated Proof of Stake (DPoS)**: This protocol improves upon PoS by allowing the stakeholders to delegate their voting power to a group of delegates or witnesses, who are elected to validate and produce the blocks. The protocol is more democratic, scalable, and flexible than PoS, but it may introduce some risks of collusion, corruption, or bribery among the delegates.
  - **Practical Byzantine Fault Tolerance (PBFT)**: This protocol is based on the Byzantine Generals' Problem, which is a classic problem of achieving consensus among distributed nodes that may be faulty or malicious. The protocol works by having a leader propose a block and other nodes send messages to each other to confirm its validity. The protocol can tolerate up to one-third of the nodes being faulty or malicious, and it is fast, consistent, and final, but it may not scale well to large networks or handle high transaction volumes.
  - **Raft**: This protocol is a simplified version of PBFT, which also uses a leader-follower model to achieve consensus. The protocol works by having a leader elected by a majority of the nodes, and then the leader replicates the log of transactions to the followers. The protocol is simple, easy to implement, and efficient, but it may not be very robust or secure against network failures or malicious attacks.



## Unit 4 - Hyperledger Fabric (A)

- Hyperledger Fabric is an open source project from the Linux Foundation that provides a modular blockchain framework and a de facto standard for enterprise blockchain platforms  .
- Hyperledger Fabric is intended as a foundation for developing applications or solutions with a modular architecture that allows components, such as consensus and membership services, to be plug-and-play .
- Hyperledger Fabric is designed for use within private enterprises that require high levels of security, scalability, performance, and governance  .
- Hyperledger Fabric supports smart contracts written in general-purpose programming languages, such as Java, Go, and Node.js, and enables rich queries over the ledger data using SQL-like syntax .
- Hyperledger Fabric leverages a novel approach to consensus that involves a separation of transaction validation from transaction ordering, enabling multiple ordering services and parallel validation of transactions .
- Hyperledger Fabric also supports a flexible endorsement model, where different transactions can have different endorsement policies depending on the business logic and the trust assumptions .
- Hyperledger Fabric is compatible with various standards and protocols, such as the Interledger Protocol, the Token Taxonomy Framework, and the Decentralized Identity Foundation.
- Hyperledger Fabric has a large and active community of contributors and users, and has been deployed in various industries, such as finance, banking, healthcare, IoT, supply chain, manufacturing, and technology  .
- Hyperledger Fabric 2.0 is the latest version of the framework, released in January 2020, that introduces new features and improvements, such as decentralized governance for smart contracts, improved performance and scalability, and enhanced privacy and confidentiality .



### Decomposing the consensus process for the notes of the Unit 4 - Hyperledger Fabric (A) in the subject of Block chain Architecture Design

- Consensus in Hyperledger Fabric is a process where the nodes in the network provide a guaranteed ordering of the transactions and validate those blocks of transactions that need to be committed to the ledger.
- Consensus in Hyperledger Fabric must ensure the following properties in the network:
  - Agreement: All honest nodes must agree on the same set of transactions and their order.
  - Validity: Only valid transactions that satisfy the endorsement policy and other rules must be committed to the ledger.
  - Integrity: No node can tamper with or forge transactions or blocks.
  - Finality: Once a transaction is committed to the ledger, it cannot be reversed or modified.
- Consensus in Hyperledger Fabric is broken out into three phases: Endorsement, Ordering, and Validation .
  - Endorsement: This phase is driven by policy (m out of n signatures) upon which participants endorse a transaction. An endorsing peer executes a chaincode (smart contract) and signs the input and output of the transaction. The client collects the endorsements and submits the transaction proposal to the ordering service.
  - Ordering: This phase will get the endorsed transaction proposals and agrees on the order to be committed to the ledger. The ordering service is a cluster of nodes that use a consensus algorithm (such as Solo or Kafka) to reach agreement on the order of transactions. The ordering service creates blocks of transactions and delivers them to the committing peers.
  - Validation: This phase will validate the transactions in a block and decide whether to commit or reject them. A committing peer checks the endorsement policy, the read-write set, and the versioning of the ledger state. If the transaction is valid, it is committed to the ledger and the state is updated. If the transaction is invalid, it is marked as such and not applied to the ledger.



### Hyperledger Fabric Components

Hyperledger Fabric is a blockchain framework that allows for the development of applications or solutions with a modular architecture. It supports different types of consensus mechanisms, membership services, and smart contracts (called chaincode) that can be customized and configured according to the needs of the network participants. Hyperledger Fabric consists of various major components, such as:

- **Peer nodes**: These are the nodes that maintain the state of the ledger and execute chaincode transactions. Each peer node belongs to a specific organization and can have different roles, such as endorser, committer, or anchor. Peer nodes communicate with each other through gossip protocol to ensure ledger consistency and data privacy.
- **Clients**: These are the applications that interact with the peer nodes to submit transactions or query the ledger state. Clients can be written in any programming language and use the Hyperledger Fabric SDK to communicate with the network. Clients also need to sign and verify transactions using digital certificates issued by a certificate authority (CA).
- **Ordering service**: This is the component that ensures the global ordering of transactions and delivers them to the peer nodes in batches (called blocks). The ordering service can use different algorithms to achieve consensus, such as Solo, Kafka, or Raft. The ordering service is independent of the peer nodes and does not have access to the ledger state or the chaincode logic.
- **Membership service**: This is the component that manages the identities and access rights of the network participants. The membership service uses a CA to issue and revoke digital certificates that are used to authenticate and authorize the clients and the peer nodes. The membership service also defines the policies and rules that govern the network operations, such as endorsement, validation, and channel creation.
- **Chaincode**: This is the term used for the smart contracts that define the business logic and rules of the network. Chaincode can be written in any programming language that supports the Hyperledger Fabric chaincode shim, such as Go, Node.js, or Java. Chaincode can be deployed and instantiated on specific peer nodes and channels, and can be invoked by the clients or other chaincode. Chaincode can also access the ledger state and invoke external services through APIs.



### Chaincode Design and Implementation for the notes of the Unit 4 - Hyperledger Fabric (A) in the subject of Block chain Architecture Design

- Chaincode is a program, written in Go, node.js , or Java that implements a prescribed interface.
- Chaincode runs in a secured Docker container isolated from the endorsing peer process.
- Chaincode initializes and manages ledger state through transactions submitted by applications.
- Chaincode can also query the ledger state, invoke other chaincodes, or communicate with external data sources.
- Chaincode is also known as smart contracts, as they define the rules for interacting with the data stored on a blockchain.
- Chaincode can be deployed on a channel, which is a private subnet of communication between two or more network members.
- Chaincode can be installed, instantiated, upgraded, and invoked by the network members using the Hyperledger Fabric API.
- Chaincode can be written using the fabric-contract-api, which provides a high level API for application developers to implement smart contracts.
- Chaincode can also use the fabric-shim-api, which provides a lower level API for accessing the ledger, the transaction context, and the chaincode stub.
- Chaincode can be packaged, signed, and approved by the network members before being committed to the channel ledger.
- Chaincode can be versioned and have different endorsement policies for different functions.
- Chaincode can be tested using various tools, such as the chaincode-dev-mode, the fabric-samples, and the fabric-test.



## Unit 5 - Hyperledger Fabric (B)

- Hyperledger Fabric is an open source project from the Linux Foundation that provides a modular blockchain framework and a de facto standard for enterprise blockchain platforms  .
- Hyperledger Fabric is intended as a foundation for developing applications or solutions with a modular architecture that allows components, such as consensus and membership services, to be plug-and-play .
- Hyperledger Fabric is designed to support various industry use cases, such as finance, banking, healthcare, IoT, supply chain, manufacturing and technology .
- Hyperledger Fabric delivers a uniquely elastic and extensible architecture, distinguishing it from alternative blockchain solutions .
- Hyperledger Fabric supports smart contracts written in general-purpose programming languages, such as Java, Go, and Node.js .
- Hyperledger Fabric enables a network of participants to agree on a shared ledger of transactions, while preserving privacy and confidentiality of the data .
- Hyperledger Fabric 2.0 is the latest version of the framework, which introduces new features and improvements, such as decentralized governance for smart contracts, improved performance and scalability, and enhanced security and operational capabilities .



### Beyond Chaincode

- Chaincode is the term used for smart contracts in Hyperledger Fabric. It is a program that runs on the peers and interacts with the ledger.
- Chaincode can be written in various languages, such as Go, Node.js, or Java. It can implement any logic or functionality that the application requires.
- Chaincode can be invoked by clients through transactions, or by other chaincodes through chaincode-to-chaincode calls. It can also query the ledger state or history, or emit events to notify external applications.
- Chaincode can be installed and instantiated on one or more channels, depending on the endorsement policy and the access control requirements. It can also be upgraded to a new version when needed.
- Chaincode is not the only way to implement business logic or functionality in Hyperledger Fabric. There are other components and features that can complement or extend the capabilities of chaincode, such as:

  - **Private data collections**: These are subsets of the ledger data that are shared among a subset of organizations in a channel, and are not stored on the ledger or available to unauthorized parties. They can be used to implement data privacy or confidentiality for sensitive or regulated information, such as medical records or trade secrets.
  - **State-based endorsement**: This is a feature that allows the endorsement policy of a chaincode to be specified as a key-value pair in the ledger state, rather than as a static policy in the chaincode definition. This enables the endorsement policy to be dynamic and changeable, depending on the state of the ledger or the application logic.
  - **Chaincode events**: These are events that are emitted by the chaincode when a transaction is committed, and can be used to notify external applications or systems about the changes in the ledger state or the execution of the chaincode logic. They can be used to implement event-driven architectures, such as triggering workflows, alerts, or notifications.
  - **System chaincodes**: These are special chaincodes that are part of the Fabric system and provide core functionality, such as configuration, lifecycle, or governance. They can be invoked by clients or other chaincodes, and can access the ledger or other Fabric components. They can be used to implement system-level logic or functionality, such as managing the channel configuration, the chaincode lifecycle, or the identity management.



### Fabric SDK and Front End

- A Fabric SDK is a software development kit that allows an application front-end to communicate with a Fabric network using a programming language of choice, such as Node.js, Java, Python, etc.
- A Fabric SDK provides APIs to perform various operations on the Fabric network, such as creating channels, joining peers, installing and invoking chaincodes, querying the ledger, etc.
- A Fabric SDK also handles the cryptographic aspects of the communication, such as signing transactions, verifying signatures, and managing certificates.
- A Fabric SDK can be used to develop different types of applications, such as web applications, mobile applications, IoT applications, etc.
- A Fabric SDK can be integrated with various front-end frameworks, such as React, Angular, Vue, etc., to create user interfaces for the applications.
- A front-end application with Fabric SDK typically consists of the following components:
  - A web server that hosts the front-end files and serves them to the clients.
  - A client-side script that interacts with the web server and the Fabric SDK to send and receive data from the Fabric network.
  - A Fabric SDK instance that connects to the Fabric network and performs the required operations.
  - A Fabric network that consists of peers, orderers, channels, chaincodes, and other components.
- A front-end application with Fabric SDK can follow different architectures, such as MVC, MVVM, etc., depending on the design choices and requirements.
- A front-end application with Fabric SDK can leverage various tools and libraries, such as Bootstrap, Material UI, Axios, etc., to enhance the functionality and appearance of the user interface.



### Hyperledger Composer Tool

- Hyperledger Composer is a set of open source tools that allows business owners, operators, and developers a way to create blockchain applications and smart contracts aimed at solving business problems and/or improving operational efficiencies .
- It is an example of a commercial application of blockchain-as-a-service (BaaS) .
- It is a collaboration tool for building “blockchain business networks,” accelerating the development of smart contracts and their deployment across a distributed ledger .
- It is based on the Hyperledger Fabric framework, which provides the underlying blockchain infrastructure and security .
- It has four main components:
  - **Modeling language**: A domain-specific language for defining the assets, participants, transactions, and access control rules of a business network.
  - **Business logic**: JavaScript code that implements the transaction logic of a business network, also known as chaincode or smart contracts.
  - **REST API**: A web service that exposes the business network as a set of RESTful endpoints, allowing applications to interact with the blockchain via HTTP requests.
  - **Web UI**: A graphical user interface that allows users to test and demonstrate the business network, as well as generate application skeletons and network cards.
- It also provides a set of tools for developing, testing, deploying, and managing blockchain applications, such as:
  - **Composer Playground**: A web-based IDE for creating and testing business network definitions and smart contracts.
  - **Composer CLI**: A command-line interface for installing, starting, and upgrading business networks and smart contracts on a Hyperledger Fabric instance.
  - **Composer Generator**: A tool for generating application skeletons and network cards from business network definitions.
  - **Composer Admin**: A tool for administering business networks and smart contracts on a Hyperledger Fabric instance.
  - **Composer Query Language**: A query language for retrieving data from a business network, similar to SQL.
- Hyperledger Composer is designed to simplify and accelerate the development of blockchain applications, by providing a high-level abstraction of the blockchain concepts and a user-friendly interface .
- However, Hyperledger Composer is no longer actively maintained or supported by its developers, and has been declared as End of Life as of August 2021 .
- Users are advised to migrate to other Hyperledger tools or frameworks, such as Hyperledger Fabric SDKs, Hyperledger Caliper, or Hyperledger Cactus .



## Unit 6 - Use case 1

- A use case is a description of how a system interacts with one or more actors to achieve a specific goal.
- An actor is a role that a user or another system plays in relation to the system under consideration.
- A use case diagram is a graphical representation of the use cases and actors involved in a system.
- A use case diagram consists of the following elements:
  - A system boundary, which is a rectangle that encloses the use cases and represents the scope of the system.
  - Use cases, which are oval shapes that represent the goals or functions that the system provides to the actors.
  - Actors, which are stick figures or icons that represent the roles that interact with the system.
  - Associations, which are lines that connect the actors and the use cases and indicate the communication or participation between them.
  - Generalizations, which are lines with a hollow triangle at one end that indicate a specialization or inheritance relationship between actors or use cases.
  - Include relationships, which are dashed lines with an open arrowhead at one end that indicate that a use case includes the behavior of another use case as a part of its normal execution.
  - Extend relationships, which are dashed lines with an open arrowhead at one end that indicate that a use case extends the behavior of another use case under certain conditions.
- A use case diagram can be used to model the functional requirements of a system, to identify the actors and their goals, to show the relationships and dependencies among the use cases, and to communicate and validate the system scope and functionality with the stakeholders.
- A use case diagram can be drawn at different levels of abstraction, depending on the purpose and audience of the diagram. The levels of abstraction are:
  - Summary level, which shows the main goals of the system and the actors involved, without going into details of the use cases.
  - User-goal level, which shows the use cases that correspond to the goals or tasks that the actors want to achieve with the system, without going into details of the scenarios or steps.
  - Subfunction level, which shows the use cases that correspond to the subfunctions or steps that are performed within a user-goal level use case, with more details of the scenarios or steps.
- A use case diagram can be complemented by other diagrams and documents, such as:
  - Use case specifications, which are textual descriptions of the use cases that provide more details of the scenarios, preconditions, postconditions, main flow, alternative flows, and exceptions of each use case.
  - Activity diagrams, which are graphical representations of the workflows or sequences of actions and decisions that occur within a use case.
  - Sequence diagrams, which are graphical representations of the interactions and messages exchanged among the objects or components that participate in a use case.
  - Class diagrams, which are graphical representations of the static structure and relationships of the classes or entities that are involved in a use case.



### Blockchain in Financial Software and Systems (FSS)

- Blockchain is a decentralized ledger that records transactions in a distributed network of nodes, without the need for intermediaries or central authorities.
- Blockchain can provide various benefits for the financial software and systems industry, such as:
  - Faster and cheaper transactions and trades, by eliminating intermediaries, reducing fees, and enabling peer-to-peer exchange of value .
  - Greater security and transparency, by using cryptography, consensus mechanisms, and immutability to prevent fraud, tampering, and unauthorized access .
  - More liquidity and efficiency, by creating digital representations of financial instruments, such as tokens, securities, or stablecoins, that can be traded on blockchain platforms with lower friction and higher speed.
  - More innovation and inclusion, by enabling new business models, products, and services, such as decentralized finance (DeFi), smart contracts, or digital identity, that can reach more customers and markets  .
- Some examples of use cases for blockchain in financial software and systems are:
  - Cross-border payments, by using blockchain to facilitate fast, low-cost, and secure remittances and transfers across different currencies and jurisdictions .
  - Trade finance, by using blockchain to streamline and automate the processes and documentation involved in international trade, such as letters of credit, invoices, or bills of lading .
  - Asset management, by using blockchain to create and manage digital assets, such as tokenized securities, funds, or derivatives, that can be traded on secondary markets or platforms.
  - Lending and borrowing, by using blockchain to enable peer-to-peer lending and borrowing, without intermediaries, using smart contracts, collateral, or credit scores .
  - Insurance, by using blockchain to improve the efficiency and trust of the insurance industry, by enabling smart contracts, parametric insurance, or decentralized autonomous organizations (DAOs) .



### Settlements

- Settlements are the process of transferring ownership and value of assets between parties after a trade or transaction.
- Settlements can involve various types of assets, such as securities, derivatives, commodities, currencies, etc.
- Settlements can be complex, costly, and time-consuming, as they often require intermediaries, such as clearinghouses, custodians, banks, etc., to verify and facilitate the exchange of assets and payments.
- Blockchain technology can offer a solution for improving settlement efficiency, security, and transparency, by enabling peer-to-peer transactions, eliminating intermediaries, and providing immutable records of ownership and value.
- Blockchain-based settlements can use smart contracts, which are self-executing agreements that encode the terms and conditions of a trade or transaction, and automatically execute them upon predefined triggers or events.
- Blockchain-based settlements can also use tokens, which are digital representations of assets that can be issued, transferred, and exchanged on a blockchain network, without the need for physical delivery or verification.
- Some of the benefits of blockchain-based settlements are:
  - Faster and cheaper settlements, as transactions can be completed in near real-time, with lower fees and operational costs.
  - Reduced counterparty and settlement risk, as transactions are verified and validated by the consensus of the network, and assets are transferred simultaneously and irrevocably.
  - Enhanced transparency and auditability, as transactions are recorded and stored on a distributed ledger, which can be accessed and verified by authorized parties.
  - Increased liquidity and access, as transactions can be executed across borders and jurisdictions, and assets can be fractionalized and traded more easily.
- Some of the challenges of blockchain-based settlements are:
  - Regulatory and legal uncertainty, as different jurisdictions may have different rules and standards for blockchain-based transactions and assets, and the enforceability of smart contracts may be unclear or disputed.
  - Scalability and interoperability issues, as blockchain networks may have limited capacity and speed to handle large volumes and varieties of transactions and assets, and may not be compatible or integrated with existing systems and platforms.
  - Security and privacy concerns, as blockchain networks may be vulnerable to cyberattacks, data breaches, or unauthorized access, and may expose sensitive or confidential information of the parties involved.
- Some of the use cases of blockchain-based settlements are:
  - Securities trade clearing and settlement, where blockchain can enable faster and cheaper settlement of securities trades, such as stocks, bonds, etc., by eliminating the need for clearinghouses and custodians, and providing direct and simultaneous delivery versus payment (DVP) of assets and funds .
  - Cross-border payments and settlements, where blockchain can enable faster and cheaper settlement of cross-border payments, such as remittances, trade finance, etc., by eliminating the need for intermediaries, such as banks and payment processors, and providing direct and secure transfer of value and information .
  - Supply chain and trade finance document handling, where blockchain can enable faster and cheaper settlement of supply chain and trade finance transactions, such as invoices, bills of lading, letters of credit, etc., by eliminating the need for paper-based and manual processes, and providing digital and verifiable proof of ownership and delivery of goods and services.



### KYC for the notes of the Unit 6 - Use case 1 in the subject of Block chain Architecture Design

- KYC stands for Know Your Customer, which is a process of verifying the identity and credentials of customers or users of a service or platform.
- KYC is often required by financial institutions, regulators, or service providers to comply with anti-money laundering (AML) and counter-terrorism financing (CTF) laws and regulations, as well as to prevent fraud and identity theft.
- KYC can involve collecting and verifying various types of information and documents from customers or users, such as name, address, date of birth, phone number, email, photo ID, proof of address, bank statements, tax returns, etc.
- KYC can also involve performing background checks, risk assessments, and due diligence on customers or users, such as checking their credit history, criminal records, sanctions lists, political exposure, etc.
- KYC can be performed at different stages of the customer or user lifecycle, such as onboarding, transaction, periodic, or trigger-based.
- KYC can be performed manually or automatically, using various methods and tools, such as online forms, biometric verification, facial recognition, document scanning, blockchain verification, etc.
- KYC can have various benefits and challenges for customers or users, service providers, and regulators, such as:

  - Benefits:
    - Enhancing trust and security among parties
    - Reducing fraud and identity theft
    - Improving customer or user experience and retention
    - Enabling access to more services and markets
    - Complying with laws and regulations
    - Supporting social and financial inclusion
  - Challenges:
    - Increasing cost and complexity of verification
    - Raising privacy and data protection concerns
    - Creating barriers and friction for customers or users
    - Exposing vulnerabilities and risks of data breaches
    - Facing interoperability and standardization issues
    - Balancing trade-offs between compliance and innovation

- KYC can be applied to various use cases and scenarios in the context of blockchain architecture design, such as:

  - Use case 1: Decentralized identity and self-sovereign identity (SSI)
    - Decentralized identity is a concept of using blockchain technology to create and manage digital identities that are controlled by the users themselves, rather than by centralized authorities or intermediaries.
    - Self-sovereign identity (SSI) is a subset of decentralized identity that emphasizes the principles of user autonomy, privacy, and consent over their identity data and interactions.
    - SSI enables users to create, store, and share their identity credentials on a blockchain, using cryptographic keys and digital signatures, without relying on third-party verifiers or issuers.
    - SSI also enables users to selectively disclose their identity attributes or claims, using zero-knowledge proofs or other techniques, to prove their identity or eligibility for a service or transaction, without revealing unnecessary or sensitive information.
    - SSI can potentially simplify and streamline the KYC process, by allowing users to reuse their verified identity credentials across multiple platforms and services, without having to undergo repeated verification or share their personal data with multiple parties.
    - SSI can also potentially enhance the privacy and security of the KYC process, by allowing users to control their identity data and consent, and by reducing the risk of data breaches or misuse by centralized authorities or intermediaries.
    - SSI can face various challenges and limitations, such as:
      - Achieving interoperability and standardization among different SSI platforms and protocols
      - Ensuring the validity and revocability of identity credentials and claims
      - Addressing the legal and regulatory recognition and compliance of SSI
      - Providing user-friendly and accessible interfaces and tools for SSI
      - Educating and incentivizing users and service providers to adopt SSI



### Capital markets for the notes of the Unit 6 - Use case 1 in the subject of Block chain Architecture Design

- Capital markets are the markets where securities such as stocks, bonds, derivatives and other financial instruments are issued, traded and settled.
- Blockchain is a distributed ledger technology (DLT) that enables peer-to-peer transactions without intermediaries, using cryptography and consensus mechanisms to ensure data integrity and security.
- Blockchain has the potential to transform various aspects of capital markets, such as issuance, trading, clearing, settlement, collateral management, asset servicing and custody, by streamlining processes, reducing costs, increasing transparency and enhancing security.
- Some of the use cases of blockchain in capital markets are:

  - Issuance: Blockchain can facilitate the issuance of digital securities, such as tokenized assets, smart contracts and stablecoins, that can represent various types of assets, such as equity, debt, commodities, real estate and art. Blockchain can also enable fractional ownership, programmable features and automated compliance of digital securities, increasing their liquidity, accessibility and efficiency .
  - Trading: Blockchain can enable peer-to-peer trading of digital securities, without the need for intermediaries, such as brokers, dealers and exchanges. Blockchain can also provide real-time price discovery, market depth and order matching, reducing latency, information asymmetry and market manipulation .
  - Clearing and settlement: Blockchain can enable instant and final settlement of digital securities, without the need for clearing houses, custodians and settlement agents. Blockchain can also eliminate counterparty risk, operational risk and settlement risk, reducing capital requirements, collateral needs and reconciliation costs  .
  - Collateral management: Blockchain can enable the tracking, valuation and optimization of collateral across multiple platforms, entities and jurisdictions, using smart contracts and tokenization. Blockchain can also enable the automation of collateral allocation, margin calls and liquidation, reducing operational complexity, liquidity risk and systemic risk  .
  - Asset servicing: Blockchain can enable the automation of post-trade services and infrastructure, such as corporate actions, dividends, voting, tax reporting and regulatory reporting, using smart contracts and tokenization. Blockchain can also enable the verification and auditability of asset ownership, performance and compliance, reducing errors, fraud and disputes .
  - Custody: Blockchain can enable the secure storage and transfer of digital securities, using cryptography and distributed consensus. Blockchain can also enable the self-custody and multi-signature custody of digital securities, reducing the reliance on third-party custodians and the risk of theft, loss or hacking .



### Insurance for the notes of the Unit 6 - Use case 1 in the subject of Block chain Architecture Design

- Blockchain is a distributed ledger technology that enables secure, transparent, and immutable transactions among multiple parties without intermediaries.
- Blockchain can be applied to various aspects of the insurance industry, such as policy issuance, claims processing, fraud detection, risk management, and data sharing.
- Some of the benefits of blockchain in insurance are:
  - Reduced operational costs and inefficiencies by automating processes and eliminating manual tasks and paperwork.
  - Enhanced trust and customer satisfaction by providing faster, fairer, and more accurate services and payouts.
  - Increased security and compliance by encrypting data and ensuring its integrity and traceability.
  - Improved collaboration and innovation by enabling new business models and partnerships across the insurance value chain.
- Some of the challenges of blockchain in insurance are:
  - Regulatory uncertainty and legal issues regarding the validity, enforceability, and jurisdiction of smart contracts and blockchain transactions.
  - Technical complexity and scalability issues related to the performance, interoperability, and integration of blockchain systems with existing infrastructure and standards.
  - Cultural and organizational barriers to adoption and change management, such as lack of awareness, skills, and incentives among stakeholders.
- Some of the real-world examples of blockchain in insurance are:
  - Ryskex, a German insurtech company that provides a blockchain-based platform for risk exchange and alternative risk transfer solutions for insurers and corporates.
  - Lemonade, a US-based peer-to-peer insurance company that uses blockchain and artificial intelligence to offer renters and homeowners insurance with instant claims settlement and social impact.
  - B3i, a consortium of insurers, reinsurers, and brokers that aims to develop and implement blockchain standards and solutions for the insurance industry.



## Unit 7 - Use case 2

- Use case 2 is about designing and implementing a chatbot that can answer questions about a company's products and services.
- The chatbot should be able to:
  - Greet the user and introduce itself as the company's chatbot.
  - Ask the user for their name and use it in the conversation.
  - Identify the user's intent and provide relevant information or suggestions.
  - Handle multiple intents and follow-up questions.
  - Handle chit-chat and off-topic questions gracefully.
  - Apologize and redirect the user to a human agent if the chatbot cannot answer the question or fulfill the request.
  - Thank the user and ask for feedback at the end of the conversation.
- The chatbot should use natural language processing (NLP) techniques such as:
  - Intent classification: to determine the user's goal or purpose of the message.
  - Entity extraction: to identify and extract important information from the user's message, such as product names, features, preferences, etc.
  - Dialog management: to maintain the context and flow of the conversation, and to generate appropriate responses based on the user's intent and entities.
  - Natural language generation (NLG): to produce natural and coherent responses that match the tone and style of the company and the chatbot.
- The chatbot should be trained and tested on a large and diverse dataset of user messages and chatbot responses, covering various scenarios and use cases.
- The chatbot should be evaluated and improved based on metrics such as:
  - Accuracy: the percentage of user messages that the chatbot correctly identifies the intent and entities, and provides the correct information or suggestion.
  - User satisfaction: the degree to which the user is satisfied with the chatbot's performance, based on feedback surveys, ratings, reviews, etc.
  - Engagement: the degree to which the user is interested and involved in the conversation with the chatbot, based on metrics such as number of messages, duration of conversation, retention rate, etc.



### Blockchain in trade/supply chain

- Blockchain is a decentralized ledger technology that records and protects transaction data shared among multiple parties in a network .
- Blockchain can improve supply chain transparency and traceability by recording product statuses at every phase of the product’s lifecycle, from production to consumption.
- Blockchain can also reduce administrative costs and inefficiencies by automating data collection, verification, and exchange among supply chain participants .
- Blockchain can enable smart contracts, which are self-executing agreements that can enforce predefined rules and conditions for supply chain transactions .
- Blockchain can enhance supply chain resilience and security by preventing data tampering, fraud, and cyberattacks, as well as ensuring responsible and ethical sourcing .
- Blockchain can facilitate cross-border trade and supply chain integration by simplifying customs clearance, compliance, and payment processes .



### Provenance of goods

- Provenance of goods refers to the **chain of custody** of a product from the point of origin to the point of consumption .
- Provenance of goods is important for ensuring the **authenticity**, **quality**, **safety**, and **sustainability** of products, as well as preventing **fraud** and **counterfeiting**  .
- Blockchain is a technology that can provide **transparent**, **secure**, **immutable**, and **decentralized** records of the provenance of goods   .
- Blockchain can enable **traceability** of goods throughout the supply chain, by linking physical products with digital identifiers, such as QR codes, RFID tags, or serial numbers  .
- Blockchain can also facilitate **verification** of goods provenance, by allowing stakeholders to access and validate the information stored on the blockchain, such as the origin, location, ownership, quality, and condition of goods  .
- Blockchain can benefit various industries and sectors that rely on provenance of goods, such as **art**, **luxury goods**, **land ownership**, **agriculture**, **pharmaceuticals**, **food**, and **fashion**  .
- Some examples of blockchain applications for provenance of goods are:

  - **Everledger**: a platform that uses blockchain to track and protect the provenance of diamonds, gemstones, and other high-value assets.
  - **Provenance**: a platform that uses blockchain to provide transparency and traceability for products, such as organic food, fair trade coffee, and sustainable fashion.
  - **Artory**: a platform that uses blockchain to create and store digital certificates of authenticity and provenance for artworks.
  - **OriginTrail**: a platform that uses blockchain to enable interoperability and data exchange among different supply chain systems.
  - **VeChain**: a platform that uses blockchain to provide end-to-end supply chain management solutions for various industries, such as food, wine, luxury goods, and automotive.



### Visibility for the notes of the Unit 7 - Use case 2 in the subject of Blockchain Architecture Design

- Visibility is the ability to see and access the data stored on a blockchain network by different participants.
- Visibility can be affected by various factors, such as the type of blockchain (public or private), the consensus mechanism, the encryption methods, the access control policies, and the network topology.
- Visibility can have different levels, such as full, partial, or zero visibility, depending on the needs and preferences of the participants.
- Visibility can have different implications for the security, privacy, scalability, and performance of a blockchain network.
- Visibility can be achieved by using various techniques, such as:
  - Hashing: a process of transforming data into a fixed-length string that can be verified but not reversed.
  - Digital signatures: a process of using cryptographic keys to prove the identity and authenticity of a sender and a message.
  - Merkle trees: a data structure that organizes data into a tree of hashes, where each node is the hash of its children, and the root node is the hash of the entire data set.
  - Smart contracts: self-executing programs that run on a blockchain and enforce the rules and logic of a transaction or a process.
  - Oracles: external sources of information that provide data or services to a blockchain network, such as weather, prices, or events.
  - Zero-knowledge proofs: a cryptographic technique that allows a prover to convince a verifier that a statement is true without revealing any information about the statement.



### Trade/Supply Chain Finance

- Trade finance is the process of financing international trade transactions, such as the exchange of goods and services across borders.
- Supply chain finance is the optimization of cash flows and working capital for buyers and suppliers in a supply chain network.
- Blockchain is a distributed ledger technology that enables secure and transparent transactions among multiple parties without intermediaries.
- Blockchain can provide various benefits for trade and supply chain finance, such as:

  - Increased efficiency and reduced costs by automating and digitizing the trade finance lifecycle, from order placement to payment settlement.
  - Enhanced security and trust by using cryptography and consensus mechanisms to ensure data integrity and prevent fraud, tampering, and duplication.
  - Improved transparency and traceability by creating a single source of truth for all parties involved in the trade network, from origin to destination.
  - Greater inclusion and access by enabling more participants, especially small and medium enterprises (SMEs), to access trade finance services and markets.

- Some of the use cases of blockchain in trade and supply chain finance are:

  - Letters of credit: Blockchain can simplify and speed up the issuance and verification of letters of credit, which are contractual agreements between banks to guarantee payment for goods and services.
  - Invoice financing: Blockchain can enable faster and cheaper invoice financing, which is the practice of selling unpaid invoices to a third party at a discount for immediate cash.
  - Asset tokenization: Blockchain can enable the creation and exchange of digital tokens that represent real-world assets, such as commodities, inventory, or receivables, and facilitate their liquidity and transferability.
  - Supply chain visibility: Blockchain can provide end-to-end visibility and traceability of the physical and financial flows of goods and services in a supply chain, and enable real-time tracking and verification of their quality, quantity, and location.



### Invoice Management Discounting for the Notes of the Unit 7 - Use Case 2 in the Subject of Block Chain Architecture Design

- Invoice discounting is a funding option available to small businesses to tide over cash flow vagaries.
- Under the invoice discounting arrangement, the supplier (business) uses the account receivable as collateral to access instant funds to improve the cash flow position.
- The supplier pays a fee to the bank or the financier for this service.
- Invoice discounting is a market with a double-digit potential growth rate over the next years in Europe and worldwide.
- The main benefit of invoice discounting is the acceleration of cash flow from customers to suppliers: suppliers get advance payments from the bank rather than waiting for the customers to pay.
- However, invoice discounting also involves some challenges and risks, such as fraud, double-financing, and information asymmetry.
- Blockchain technology can offer a solution to these challenges and risks by providing a secure, transparent, and decentralized platform for invoice discounting  .
- Blockchain technology can enable businesses to upload their financial data on the chain and only share it with the entity they wish to show the data.
- This enables banks to quickly assess the risk and accordingly disburse the credit in a quick and efficient manner.
- Blockchain technology can also eliminate the need for on-site audits of receivables and debtors, of receivables' notification and debtors' verification, and of month-end reconciliation processes.
- Blockchain technology can also prevent fraud and double-financing by creating a unique digital identity for each invoice and ensuring its immutability and traceability .
- Blockchain technology can also reduce the cost and time of invoice discounting by automating the processes and eliminating intermediaries .
- Blockchain technology can also improve the trust and collaboration among the parties involved in invoice discounting by providing a shared ledger of transactions and a smart contract mechanism for enforcing the terms and conditions .
- Therefore, blockchain technology can enhance the invoice discounting process and offer benefits to both the suppliers and the banks or financiers  .



## Unit 8 - Use case 3

- Use case 3 is about designing and implementing a chatbot that can answer questions about a company's products and services.
- The chatbot should be able to:
  - Greet the user and introduce itself.
  - Understand the user's intent and extract relevant information from the user's message.
  - Provide accurate and relevant answers to the user's questions based on the company's knowledge base.
  - Handle multiple turns of conversation and maintain the context.
  - Handle errors and exceptions gracefully and provide helpful feedback to the user.
  - End the conversation politely and thank the user for their interest.
- The chatbot should not:
  - Provide personal opinions or recommendations that are not based on the company's data or policies.
  - Disclose sensitive or confidential information about the company or the user.
  - Engage in off-topic or inappropriate conversations with the user.
  - Use slang, jargon, or informal language that may confuse or offend the user.
- The chatbot should follow the best practices of chatbot design, such as:
  - Use clear and concise language that is easy to understand and follow.
  - Use natural and friendly tone that matches the company's brand and voice.
  - Use appropriate punctuation, capitalization, and grammar.
  - Use emojis, images, or other rich media to enhance the user experience and engagement.
  - Provide feedback and confirmation to the user's actions and requests.
  - Provide options and suggestions to the user to guide them through the conversation.
  - Provide fallback and help messages when the chatbot cannot understand or answer the user's message.



### Blockchain for Government

Blockchain is a distributed ledger technology that enables secure and transparent transactions among multiple parties without intermediaries. Blockchain can offer various benefits for government applications, such as:

- Enhancing trust and accountability among citizens, public agencies, and private entities.
- Improving efficiency and reducing costs of administrative processes and service delivery.
- Increasing security and resilience of critical data and infrastructure.
- Fostering innovation and collaboration across sectors and domains.

Some of the use cases of blockchain for government are:

- **Supply chain**: Blockchain can enable traceability and verification of the origin, quality, and movement of goods and services across the supply chain. This can improve transparency, compliance, and safety of public procurement, food safety, defense, and humanitarian aid. For example, the World Food Programme uses blockchain to track and distribute food vouchers to refugees.
- **Medical records**: Blockchain can enable secure and interoperable exchange of health data among patients, providers, and payers. This can improve patient care, privacy, and consent management, as well as reduce fraud and errors. For example, Estonia uses blockchain to protect the health records of its citizens.
- **Transportation**: Blockchain can enable smart mobility solutions that leverage data from various sources, such as vehicles, sensors, and users. This can improve traffic management, congestion, safety, and environmental impact. For example, Dubai uses blockchain to integrate its transportation modes and services.
- **Voting**: Blockchain can enable secure and verifiable voting systems that prevent tampering, manipulation, and coercion. This can improve voter turnout, confidence, and participation. For example, Sierra Leone used blockchain to audit its presidential election in 2018.
- **Energy**: Blockchain can enable decentralized and peer-to-peer energy markets that allow consumers and producers to trade and share energy resources. This can improve efficiency, reliability, and sustainability of energy systems. For example, Brooklyn Microgrid uses blockchain to enable local energy trading among residents.
- **Taxation**: Blockchain can enable automated and transparent tax collection and compliance. This can reduce tax evasion, fraud, and errors, as well as improve revenue and fairness. For example, China uses blockchain to streamline its tax invoice system.
- **Land ownership**: Blockchain can enable immutable and verifiable records of land titles and transactions. This can improve property rights, dispute resolution, and land administration. For example, Sweden uses blockchain to digitize its land registry.
- **Tokenization of social benefits**: Blockchain can enable the issuance and distribution of digital tokens that represent social benefits, such as welfare, subsidies, or vouchers. This can improve targeting, delivery, and accountability of social programs. For example, Singapore uses blockchain to issue and redeem digital tokens for public transport.
- **Citizen engagement**: Blockchain can enable participatory and collaborative governance models that empower citizens to co-create and co-deliver public services and policies. This can improve civic engagement, feedback, and trust. For example, Decidim uses blockchain to enable participatory democracy in Barcelona.
- **Digital currencies**: Blockchain can enable the creation and adoption of digital currencies that can complement or replace fiat currencies. This can improve financial inclusion, stability, and sovereignty. For example, the Bahamas launched its own digital currency, the Sand Dollar, in 2020.



### Digital identity for the notes of the Unit 8 - Use case 3 in the subject of Block chain Architecture Design

- Digital identity is the representation of a person, organization, or device in the digital world.
- Blockchain is a distributed ledger technology that enables secure, transparent, and decentralized transactions and data sharing.
- Blockchain can be used for digital identity management and verification in various ways, such as  :
  - Self-sovereign identity: This is a model where individuals have full control and ownership of their own identity data and can decide how, when, and with whom to share it. Blockchain provides a platform for creating and managing self-sovereign identities that are portable, interoperable, and tamper-proof.
  - Data monetization: This is a process where individuals can earn rewards or incentives for sharing their identity data with trusted parties or platforms. Blockchain enables data monetization by creating a marketplace for identity data where users can set their own terms and conditions and receive tokens or other benefits in exchange for their data.
  - Data portability: This is a feature where individuals can easily access and transfer their identity data across different platforms or services without losing their privacy or security. Blockchain enables data portability by providing a common infrastructure and standard for identity data that can be verified and validated by any party.
- Blockchain for digital identity has several benefits for enterprises, users, and IoT management systems, such as :
  - Enhanced security: Blockchain reduces the risk of identity theft, fraud, and data breaches by eliminating the need for centralized databases or intermediaries that can be hacked or compromised. Blockchain also uses cryptography and consensus mechanisms to ensure the integrity and authenticity of identity data and transactions.
  - Improved efficiency: Blockchain speeds up the process of identity verification and authentication by enabling near-instant and automated validation of credentials and claims. Blockchain also reduces the cost and complexity of identity management by eliminating the need for multiple systems or processes that can be redundant or inconsistent.
  - Increased trust: Blockchain fosters trust and transparency among all participants in the identity ecosystem by providing a shared and immutable record of identity data and transactions. Blockchain also empowers individuals to have more control and choice over their own identity data and how it is used or shared.



### Land records and other kinds of record keeping between government entities for the notes of the Unit 8 - Use case 3 in the subject of Block chain Architecture Design

- Land records are documents that contain information about the ownership, rights, and transactions of land or real estate properties.
- Land records are essential for ensuring legal certainty, preventing disputes, facilitating taxation, and promoting development.
- However, land records are often fragmented, outdated, inaccurate, or inaccessible, especially in developing countries, where land administration systems are weak or corrupt.
- Blockchain technology is a distributed ledger that can store and verify transactions in a secure, transparent, and immutable way, without the need for intermediaries or central authorities.
- Blockchain technology can be used to create a land registry system that can improve the efficiency, reliability, and accessibility of land records, as well as reduce costs, fraud, and conflicts.
- Some of the benefits of using blockchain for land registry are   :
  - Transparency: Blockchain can provide a public and verifiable record of land ownership and transactions, which can increase trust and accountability among stakeholders.
  - Security: Blockchain can protect land records from tampering, hacking, or loss, by using cryptography, consensus mechanisms, and distributed storage.
  - Verifiability: Blockchain can enable the validation of land records and transactions, by using smart contracts, digital signatures, and timestamps.
  - Searchability: Blockchain can enable the easy and fast retrieval of land records and transactions, by using unique identifiers, indexes, and queries.
  - Interoperability: Blockchain can enable the integration and exchange of land records and transactions among different government entities, such as tax authorities, courts, or banks.
- Some of the challenges of using blockchain for land registry are  :
  - Legal recognition: Blockchain may not be compatible with the existing legal frameworks and regulations for land administration, which may require amendments or reforms.
  - Data quality: Blockchain may not be able to verify the accuracy or completeness of the land records and transactions that are entered into the system, which may depend on the quality of the data sources and the verification processes.
  - Scalability: Blockchain may not be able to handle the large volume and complexity of the land records and transactions that are generated and stored in the system, which may affect the performance and cost of the system.
  - Adoption: Blockchain may not be widely accepted or adopted by the stakeholders involved in the land administration, such as landowners, buyers, sellers, agents, or officials, who may lack the awareness, skills, or incentives to use the system.
- Some of the examples of using blockchain for land registry are  :
  - Sweden: The Swedish land authority, Lantmäteriet, has been testing a blockchain-based land registry system since 2016, in collaboration with several private partners, such as banks, telecom companies, and blockchain startups. The system aims to streamline and automate the land transfer process, by using smart contracts, digital signatures, and online verification.
  - Ghana: The Ghanaian government, in partnership with Medici Land Governance, a subsidiary of Overstock.com, has been piloting a blockchain-based land registry system since 2018, in several regions of the country. The system aims to create a digital and decentralized land registry, by using LiDAR, artificial intelligence, and cryptography, to map, record, and verify land ownership and transactions.
  - India: The Indian state of Andhra Pradesh, in collaboration with ChromaWay, a blockchain company, has been implementing a blockchain-based land registry system since 2017, in several districts of the state. The system aims to improve the transparency and security of land records, by using a hybrid blockchain model, that combines a public blockchain for verification and a private blockchain for storage.



### Public Distribution System Social Welfare Systems

- Public distribution system (PDS) is a system where the government creates a supply chain to reach towards the public, such as providing subsidized food and essential commodities to the poor and vulnerable sections of the society.
- Blockchain is an emerging technology that can provide security, transparency, and efficiency to the PDS by recording all transactions and events in a distributed ledger that is immutable, verifiable, and traceable  .
- Some of the benefits of using blockchain in PDS are:
  - It can prevent leakage, corruption, and diversion of the supplies by ensuring that the beneficiaries receive the correct quantity and quality of the goods .
  - It can reduce the intermediaries and the operational costs involved in the PDS by enabling direct and peer-to-peer transactions between the government and the beneficiaries .
  - It can improve the accountability and the governance of the PDS by providing real-time data and audit trails of the transactions and events .
  - It can enhance the user experience and the satisfaction of the beneficiaries by providing them with digital identities, smart contracts, and mobile applications to access the PDS .
- Some of the challenges and limitations of using blockchain in PDS are:
  - It requires a high level of technical expertise, infrastructure, and coordination among the stakeholders to implement and maintain the blockchain system .
  - It faces legal, regulatory, and social barriers to ensure the compliance, privacy, and inclusion of the beneficiaries in the blockchain system  .
  - It may encounter scalability, interoperability, and security issues to handle the large volume and variety of data and transactions in the PDS .
- Some of the examples of using blockchain in PDS are:
  - The government of Andhra Pradesh in India has partnered with a blockchain startup to pilot a blockchain-based PDS that aims to eliminate the middlemen and the fake beneficiaries in the system.
  - The World Food Programme (WFP) has launched a blockchain-based PDS in Jordan that uses biometric authentication and smart contracts to provide cash assistance to the Syrian refugees.
  - The researchers from the Indian Institute of Technology (IIT) have proposed a blockchain-based PDS that uses solidity language and smart contracts to automate the public food distribution system.



### Blockchain Cryptography for the notes of the Unit 8 - Use case 3

- Blockchain cryptography is the method of securing data and transactions on a blockchain network using cryptographic keys and algorithms.
- Cryptography in blockchain has two main functions: to ensure the integrity and authenticity of data, and to enable privacy and confidentiality of transactions.
- Blockchain cryptography uses two types of keys: public keys and private keys. Public keys are used to identify and verify the sender and receiver of a transaction, while private keys are used to sign and encrypt the transaction data.
- Blockchain cryptography also uses hashing, which is the process of transforming any input data into a fixed-length output, called a hash or a digest. Hashing is used to create a unique identifier for each block in the blockchain, and to ensure that the data in the block has not been tampered with.
- Blockchain cryptography can be applied to various use cases across different industries, such as:
  - Cryptocurrencies: Blockchain cryptography enables the creation and transfer of digital currencies, such as Bitcoin, Ethereum, and others, without the need for a central authority or intermediary. Cryptocurrencies use cryptographic algorithms, such as SHA-256 and ECDSA, to generate and validate transactions on the blockchain.
  - Identity management: Blockchain cryptography can help prevent identity theft and fraud by using cryptographic keys to authenticate identity attributes and credentials, such as name, address, biometrics, and others. Blockchain identity management can also enable self-sovereign identity, which is the ability of individuals to control their own identity data and access rights.
  - Supply chain management: Blockchain cryptography can help improve the transparency and traceability of supply chains by using cryptographic keys and hashes to record and verify the provenance, location, and condition of goods and materials, from the source to the destination. Blockchain supply chain management can also reduce costs, errors, and delays, and enhance security and compliance.
  - IoT: Blockchain cryptography can help secure and manage the data and devices in the Internet of Things, which is the network of interconnected physical objects that can collect and exchange data. Blockchain IoT can use cryptographic keys and hashes to identify and authenticate devices, encrypt and decrypt data, and ensure the integrity and reliability of data and transactions.
  - Government: Blockchain cryptography can help improve the efficiency and accountability of government services and processes, such as voting, taxation, land registry, health records, and others. Blockchain government can use cryptographic keys and hashes to ensure the identity and eligibility of citizens, protect the privacy and confidentiality of data, and prevent corruption and fraud.



### Privacy and Security on Blockchain

- Privacy and security are two important aspects of blockchain technology that affect its adoption and use cases.
- Privacy refers to the ability of users to control their own data and identity, and to prevent unauthorized access or disclosure of their information.
- Security refers to the ability of the system to resist attacks, ensure data integrity, and provide reliable and consistent service.
- Some of the privacy and security challenges and solutions in blockchain environments are:

  - **Private and public keys**: Blockchain systems use asymmetric cryptography to secure transactions between users. Each user has a public and private key. The public key is used to identify the user and verify their signature, while the private key is used to sign transactions and decrypt messages. Users need to protect their private keys from theft or loss, and use secure key management practices.  
  - **Pseudo-anonymity**: Blockchain transactions are pseudo-anonymous, meaning that users are identified by their public keys, not by their real names or personal information. This provides some level of privacy, but also poses some challenges. For example, users may be linked to their transactions by analyzing their behavior patterns, or by using external data sources. Users may also face legal or regulatory issues if their transactions are not compliant with the laws of their jurisdiction.  
  - **Data privacy**: Blockchain data is stored and replicated across multiple nodes in the network, which makes it transparent and immutable. However, this also means that sensitive or confidential data may be exposed to unauthorized parties, or used for malicious purposes. Users may need to encrypt their data, use zero-knowledge proofs, or employ privacy-preserving techniques such as homomorphic encryption, secure multiparty computation, or differential privacy.   
  - **Secure communication**: Blockchain nodes communicate with each other through peer-to-peer protocols, which may be vulnerable to network attacks, such as denial-of-service, man-in-the-middle, or sybil attacks. Nodes need to use secure communication channels, such as TLS, VPN, or Tor, and implement security mechanisms such as firewalls, intrusion detection systems, or reputation systems.  
  - **Smart contract security**: Smart contracts are self-executing programs that run on the blockchain and enforce the rules and logic of transactions. Smart contracts can provide automation, efficiency, and transparency, but they can also introduce security risks, such as bugs, vulnerabilities, or malicious code. Smart contract developers need to follow best practices, such as code review, testing, auditing, and formal verification, and use security tools, such as static analysis, dynamic analysis, or symbolic execution.

