 Here is the content in formal tone with points:

Blockchain: Implement a simple blockchain application

I. Introduction
- Blockchain is a decentralized, distributed and public digital ledger that underlies cryptocurrencies like Bitcoin.
- Blockchain allows multiple parties to have a secure and consistent view of digital information without the need for a trusted, third-party intermediary.
- We will implement a simple blockchain application using Python that stores transactions in a decentralized network.

II. Components
- Block: Group of transactions recorded at a specific time. Contains timestamp and link to previous block.
- Chain: Ordered list of blocks. New blocks are added to the end of the chain.
- Consensus: Agreement on the validity of the blockchain. Achieved through proof-of-work algorithm.
- Nodes: Participants in the blockchain network that hold a copy of the blockchain. New transactions/blocks are broadcast to the network by nodes.

III. Implementation
- We will use Python dictionaries to represent blocks. Blocks will contain transactions (tx) and timestamp (time) and a link (prevHash) to previous block.
- New blocks are added to the chain through mining. Mining involves solving a proof-of-work problem to find a number (nonce) that when hashed with other block data results in a hash with required number of leading 0s.
- The blockchain is decentralized - multiple nodes in the network hold a copy of the chain and any conflicts are resolved through consensus. Longest chain is considered valid.

IV. Conclusion
- We implemented a simple blockchain application in Python that allows recording transactions in a decentralized network.
- The blockchain data structure provides security and consistency without a central authority through mechanisms like proof-of-work and consensus.
- The concepts can be extended to build more complex blockchain applications for cryptocurrencies, supply chain management, health records, etc.