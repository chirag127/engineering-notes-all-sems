The following is a detailed ASCII diagram for Proof of Work (PoW) for the notes of the Unit 2 - Consensus in the subject of Blockchain Architecture Design.

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Miner 1       |    |   Miner 2       |    |   Miner 3       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       +---------------------+---------------------+
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             |
                             +---------------------+
                             |                     |
                             |   Blockchain       |
                             |   Network          |
                             |                     |
                             +---------------------+
```

The diagram illustrates the basic architecture of a Proof of Work (PoW) blockchain network. The network consists of multiple miners who compete to solve a cryptographic puzzle based on the transactions in the current block. The first miner who finds a valid solution (a hash that matches the target difficulty) broadcasts it to the rest of the network. The other miners verify the solution and append the new block to their copy of the blockchain. The miner who solved the puzzle receives a reward in the form of newly minted coins and transaction fees. The process repeats for the next block. This way, the PoW algorithm ensures that the transactions are verified and the blockchain is secure and immutable.