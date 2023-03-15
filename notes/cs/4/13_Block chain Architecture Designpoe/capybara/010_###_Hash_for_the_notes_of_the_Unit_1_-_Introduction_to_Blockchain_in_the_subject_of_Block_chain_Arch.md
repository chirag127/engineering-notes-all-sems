### Hash for the notes of the Unit 1 - Introduction to Blockchain in the subject of Block chain Architecture Design

Hashing is a fundamental concept in blockchain technology. Hashing is the process of taking an input (such as a message or file) and generating a fixed-size output (known as a hash or digest) that represents the input. Hashing is used in many areas of computer science, including cryptography, data structures, and databases. In blockchain, hashing is used to secure transactions and blocks.

Here are some key points to remember about hashing in blockchain:

- A hash function takes an input (such as a message or file) and generates a fixed-size output (known as a hash or digest) that represents the input. Hash functions are deterministic, meaning that the same input will always produce the same output.
- Hashing is a one-way process, meaning that it is difficult (if not impossible) to reverse engineer the input from the output. This makes hashing useful for securing data, as it ensures that the original data cannot be tampered with without being detected.
- In blockchain, hashing is used to secure transactions and blocks. Each transaction is hashed and included in a block, along with other transactions. The block is then hashed, and the resulting hash is included in the next block. This creates a chain of blocks (hence the name blockchain) that is secured by hashing.
- One important property of hash functions is that even a small change to the input will result in a completely different output. This property is known as the avalanche effect and makes it difficult to create two inputs that produce the same output (known as a hash collision).
- Hashing is also used in mining, a process in which nodes compete to generate a new block and earn a reward. Miners must solve a cryptographic puzzle by finding a hash that meets a certain criteria (known as the target). This requires a large amount of computational power, and the first miner to find a valid hash is rewarded for their efforts.

Some learning tricks and mnemonics to remember about hashing in blockchain:

- Think of hashing as a digital fingerprint. Just like a fingerprint uniquely identifies a person, a hash uniquely identifies a piece of data. This makes it useful for securing transactions and blocks in blockchain.
- Remember that hashing is a one-way process. Once data has been hashed, it cannot be easily reversed. This is what makes it useful for securing data in blockchain.
- Think of mining as a race to find a needle in a haystack. Miners are searching for a hash that meets a certain criteria, and the first one to find it is rewarded. This requires a large amount of computational power, which is why mining is so competitive.