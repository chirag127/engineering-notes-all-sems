### Protocols for the notes of the Unit 1 - Introduction to Blockchain in the subject of Block chain Architecture Design

According to , blockchain protocols are a set of rules that govern the blockchain network. They define the interface of the network, the interaction between the nodes, the incentives, the kind of data, etc. The protocols aim to address the four principles:

- Security: Protocols maintain the security of the whole crypto network. They ensure that the transactions are valid, the data is immutable, and the network is resistant to attacks.
- Decentralization: Blockchain is a decentralized network. There is no central authority or intermediary that controls the network. Protocols enable the nodes to reach a consensus on the state of the network without relying on a trusted third party.
- Consistency: Whenever a transaction occurs, protocols update the whole database at each step so that each node is well versed with the whole crypto network. Protocols ensure that the network is synchronized and consistent across all nodes.
- Scalability: Scalability means an increase in the number of transactions. Protocols determine the trade-off between security, decentralization, and consistency on one hand, and scalability, speed, and efficiency on the other hand.

There are different types of blockchain protocols, depending on the design choices and trade-offs they make. Some of the common types are:

- Proof-of-Work (PoW): This is the protocol used by Bitcoin and Ethereum. It requires the nodes to solve a hard mathematical puzzle to create a new block and validate transactions. The node that solves the puzzle first gets a reward and broadcasts the block to the network. The other nodes verify the block and add it to their chain. This protocol is secure and decentralized, but it consumes a lot of energy and is slow and inefficient.
- Proof-of-Stake (PoS): This is the protocol used by Cardano and Polkadot. It requires the nodes to stake some amount of cryptocurrency to participate in the network. The node that creates a new block is randomly selected based on the amount of stake and other factors. The node gets a reward and broadcasts the block to the network. The other nodes verify the block and add it to their chain. This protocol is more energy-efficient and scalable than PoW, but it may introduce some centralization and security risks.
- Proof-of-Authority (PoA): This is the protocol used by VeChain and xDai. It requires the nodes to be authorized by a trusted entity to participate in the network. The node that creates a new block is selected based on a predefined algorithm. The node gets a reward and broadcasts the block to the network. The other nodes verify the block and add it to their chain. This protocol is fast and efficient, but it sacrifices decentralization and trustlessness.

The following diagram illustrates the basic architecture of a blockchain protocol:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|     Node 1      |     |     Node 2      |     |     Node 3      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Blockchain     |     |  Blockchain     |     |  Blockchain     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Protocol       |     |  Protocol       |     |  Protocol       |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Network        |     |  Network        |     |  Network        |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Hardware       |     |  Hardware       |     |  Hardware       |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```