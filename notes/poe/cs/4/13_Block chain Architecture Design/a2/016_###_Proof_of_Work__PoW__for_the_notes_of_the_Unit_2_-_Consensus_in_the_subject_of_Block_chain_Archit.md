 Here is the content in markdown format for the topic ### Proof of Work (PoW) for the notes of the Unit 2 - Consensus in the subject of Block chain Architecture Design:

### Proof of Work (PoW)

- Proof of Work is a consensus algorithm used in blockchain networks like Bitcoin to verify transactions and mint new blocks.
- It ensures that the miners have spent computational resources to verify the transactions and mint the block. This makes the blockchain resilient to spam and cyber attacks like DDoS as it is very resource intensive to verify transactions and mint blocks.
- In PoW, miners have to solve a cryptographic puzzle called proof of work problem. The miners use brute force method to repeatedly hash the block data and nonce to get a hash value smaller than the target. The first miner to achieve this announces the block to the network and claims the block reward.
- This makes PoW decentralized as any miner has equal opportunity to be the first to solve the puzzle and mint the block. But it is energy inefficient as a lot of computing power is wasted in repeated hashing.
- Popular PoW algorithms are SHA-256 used in Bitcoin and Scrypt used in Litecoin.

Advantages:
- Decentralized - No single entity controls the blockchain
- Resilient to spam and DDoS attacks due to high resource requirement

Disadvantages:
- Energy inefficient due to large amount of computing power wasted in repeated hashing
- Tendency towards centralization as only miners with powerful ASICs can profitably mine blocks leading to centralization of mining power with few pools

Applications:
- Bitcoin and other major cryptocurrencies use PoW for consensus

Mnemonics:
- Proof of Work = Solve puzzle = Brute force method = Repeated hashing
- Decentralized but energy inefficient