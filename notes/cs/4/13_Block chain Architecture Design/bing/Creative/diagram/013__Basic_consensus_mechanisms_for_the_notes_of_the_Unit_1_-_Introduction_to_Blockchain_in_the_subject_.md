Consensus mechanisms are methods used to achieve agreement, trust, and security across a decentralized computer network, such as a blockchain. They are essential for ensuring the integrity and validity of the data stored on the distributed ledger. Some of the most common consensus mechanisms used in blockchain are proof-of-work (PoW), proof-of-stake (PoS), and delegated proof-of-stake (DPoS).

The following diagram illustrates the basic architecture of a proof-of-work consensus mechanism, which requires computational power to solve a cryptographic puzzle and verify transactions. The first node to solve the puzzle broadcasts the solution to the network and proposes a new block of transactions. The other nodes validate the solution and the transactions, and if they agree, they append the new block to the existing chain. The node that solved the puzzle receives a reward in the form of cryptocurrency. This process repeats for every new block. 

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|     Node 1      |     |     Node 2      |     |     Node 3      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Transactions   |     |  Transactions   |     |  Transactions   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Puzzle: ?     |     |   Puzzle: ?     |     |   Puzzle: ?     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Solution: X   |     |   Solution: X   |     |   Solution: X   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   New Block: Y  |     |   New Block: Y  |     |   New Block: Y  |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Blockchain:   |     |   Blockchain:   |     |   Blockchain:   |
|                 |     |                 |     |                 |
|   A -> B -> C   |     |   A -> B -> C   |     |   A -> B -> C   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Reward: Z     |     |   Reward: Z     |     |   Reward: Z     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```
The following diagram illustrates the basic architecture of a proof-of-stake consensus mechanism, which requires nodes to stake a certain amount of cryptocurrency to participate in the network. The nodes are randomly selected to propose and validate new blocks of transactions, based on their stake and other factors. The nodes that propose and validate blocks receive a reward in the form of transaction fees. This process reduces the need for intensive computation and energy consumption. 

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|     Node 1      |     |     Node 2      |     |     Node 3      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Transactions   |     |  Transactions   |     |  Transactions   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Stake: 100    |     |   Stake: 50     |     |   Stake: 25     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Selection: P  |     |   Selection: