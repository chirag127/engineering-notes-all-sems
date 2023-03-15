 Here is the content in markdown format:

### Hashchain to Blockchain for the notes of the Unit 1 - Introduction to Blockchain in the subject of Block chain Architecture Design

**Hashchain:** A hashchain is a cryptographic method to create a sequence of hash values such that each subsequent hash value is dependent on the previous hash value. Each hash value in the chain is an irreversible one-way function of the previous hash value. To create a hashchain:

1. Start with an initial value (e.g. 0).
2. Apply a hash function to get the first hash value.
3. Apply the hash function to the first hash value to get the second hash value.
4. Continue applying the hash function to get subsequent hash values.

Hashchains are useful for creating proofs of work and time-stamping/ordering data.

**Blockchain:** A blockchain is a distributed ledger that maintains a continuously growing list of records called blocks. New blocks are added to the blockchain in a linear, chronological order using cryptography to keep them secure. The blockchain allows multiple parties to have a secure and consistent view of digital information without the need for a trusted, third-party intermediary. Blockchain technology has numerous applications like cryptocurrencies, smart contracts, etc.

The key points in the transformation from a hashchain to a blockchain are:

1. Adding transaction data to each block in the chain.
2. Using the previous hash value as an input to calculate the next hash value (creating links between blocks).
3. Requiring proof of work to add a block to the chain, making the blockchain tamper-resistant and immutable.

**Mnemonics:**
Hashchain: Sequence of hashes
Blockchain: Chain of blocks with transactions and proofs

**Advantages:** Immutability, decentralization, security, transparency
**Disadvantages:** Scalability, interoperability, energy consumption
**Applications:** Cryptocurrencies, smart contracts, supply chain management, etc.