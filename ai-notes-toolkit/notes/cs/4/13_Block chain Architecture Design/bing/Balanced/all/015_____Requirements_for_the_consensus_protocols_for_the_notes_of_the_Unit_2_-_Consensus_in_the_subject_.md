# Requirements for the consensus protocols for the notes of the Unit 2 - Consensus in the subject of Block chain Architecture Design

- A consensus protocol is a set of rules that determines how a decentralized computer network reaches agreement on which transactions are valid and which are not .
- A consensus protocol prevents a single entity from controlling a blockchain or distorting the "truth" of what should be recorded.
- A consensus protocol ensures that all participating nodes agree on the state of a blockchain and that the blockchain is immutable, consistent, and secure .
- A consensus protocol should be able to handle various challenges, such as network latency, malicious nodes, forks, and scalability .
- A consensus protocol should also be able to balance the trade-offs between decentralization, security, and performance .
- Some of the common consensus protocols used in blockchain networks are:
  - Proof of Work (PoW): This protocol requires nodes to solve a cryptographic puzzle to validate blocks and earn rewards. It is used by Bitcoin, Ethereum, and other networks. It is secure and decentralized, but consumes a lot of energy and has low throughput .
  - Proof of Stake (PoS): This protocol requires nodes to stake a certain amount of tokens to validate blocks and earn rewards. It is used by Ethereum 2.0, Cardano, and other networks. It is more energy-efficient and scalable than PoW, but has some risks of centralization and attacks .
  - Delegated Proof of Stake (DPoS): This protocol requires nodes to vote for a set of delegates who validate blocks and earn rewards. It is used by EOS, Tron, and other networks. It is faster and more scalable than PoS, but has less decentralization and security .
  - Byzantine Fault Tolerance (BFT): This protocol requires nodes to reach a quorum of agreement on the validity of blocks. It is used by Hyperledger Fabric, Stellar, and other networks. It is fast and secure, but has less decentralization and scalability .