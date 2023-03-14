The following diagram illustrates the basic architecture of a Proof of Work (PoW) blockchain using ASCII characters:

```
+-----------------+     +-----------------+     +-----------------+
| Block 1         |     | Block 2         |     | Block 3         |
|-----------------|     |-----------------|     |-----------------|
| Previous Hash:  |     | Previous Hash:  |     | Previous Hash:  |
| 000000000000000 |     | 0000000a1b2c3d4 |     | 0000000e5f6g7h8 |
|-----------------|     |-----------------|     |-----------------|
| Transactions:   |     | Transactions:   |     | Transactions:   |
| A -> B: 10 BTC  |     | B -> C: 5 BTC   |     | C -> D: 3 BTC   |
| C -> D: 2 BTC   |     | D -> E: 4 BTC   |     | E -> F: 6 BTC   |
|-----------------|     |-----------------|     |-----------------|
| Nonce: 12345678 |     | Nonce: 87654321 |     | Nonce: 13579246 |
|-----------------|     |-----------------|     |-----------------|
| Hash:           |     | Hash:           |     | Hash:           |
| 0000000a1b2c3d4 |     | 0000000e5f6g7h8 |     | 0000000i9j0k1l2 |
+-----------------+     +-----------------+     +-----------------+
```

Each block contains the following information:

- Previous Hash: The hash of the previous block in the chain, which links the blocks together and ensures the integrity of the blockchain.
- Transactions: The list of transactions that are included in the block, which are verified by the network nodes.
- Nonce: A random number that is used to find a valid hash for the block, which satisfies the difficulty level of the network.
- Hash: The result of applying a cryptographic hash function (such as SHA-256) to the block header, which consists of the previous hash, the transactions, and the nonce. The hash must start with a certain number of zeros, which is determined by the difficulty level of the network.

The process of finding a valid hash for a block is called mining, and it involves a lot of computational work. The miners compete with each other to solve the hash puzzle and receive a reward for adding a new block to the blockchain. The difficulty level of the network adjusts periodically to maintain a constant block time, which is the average time it takes to mine a new block. For Bitcoin, the block time is about 10 minutes.

The proof of work mechanism ensures that the blockchain is secure and decentralized, as it requires a lot of resources and time to alter the history of transactions. However, it also has some drawbacks, such as high energy consumption, low scalability, and vulnerability to 51% attacks. Therefore, some alternative consensus mechanisms have been proposed, such as proof of stake, proof of authority, and proof of space.