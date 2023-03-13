### Requirements for the consensus protocols for the nodes of the Unit 2 - Consensus in the subject of Blockchain Architecture Design

The consensus protocols are the rules that govern how the nodes in a blockchain network agree on the validity and order of transactions. The consensus protocols aim to achieve the following objectives :

- Agreement: All the nodes should have the same view of the state of the blockchain and the transactions that are included in it.
- Collaboration: The nodes should work together to maintain the security and integrity of the blockchain, without relying on a central authority or intermediary.
- Cooperation: The nodes should share the responsibility and reward of validating transactions and generating new blocks.
- Equal rights: Every node should have an equal opportunity to participate in the consensus process and influence the outcome.
- Mandatory participation: Every node should be required to follow the consensus rules and contribute to the network.

There are different types of consensus protocols that use different mechanisms to achieve these objectives. Some of the common types are  :

- Proof of Work (PoW): This protocol requires the nodes to solve a computationally hard puzzle to create a new block. The puzzle is based on the hash of the previous block and the transactions in the current block. The node that solves the puzzle first broadcasts the block to the network and receives a reward. The other nodes verify the validity of the block and append it to their blockchain. The longest chain is considered the valid one. This protocol is used by Bitcoin and Ethereum.
- Proof of Stake (PoS): This protocol assigns the right to create a new block to a node based on its stake, which is the amount of cryptocurrency that the node has locked up as a deposit. The node with the highest stake has the highest chance of being selected as the block producer. The node then broadcasts the block to the network and receives a reward. The other nodes verify the validity of the block and append it to their blockchain. The chain with the highest cumulative stake is considered the valid one. This protocol is used by Cardano and Polkadot.
- Proof of Authority (PoA): This protocol delegates the authority to create and validate new blocks to a set of pre-approved nodes, called validators. The validators are chosen based on their reputation and identity, and they take turns to produce blocks. The validators then broadcast the blocks to the network and receive a reward. The other nodes verify the validity of the blocks and append them to their blockchain. The chain with the most validators is considered the valid one. This protocol is used by VeChain and xDai.
- Delegated Proof of Stake (DPoS): This protocol combines the features of PoS and PoA. The nodes can stake their cryptocurrency to vote for a set of delegates, who act as the block producers. The delegates are ranked by the number of votes they receive, and the top ones are selected to form the consensus committee. The delegates then take turns to produce blocks and broadcast them to the network. The other nodes verify the validity of the blocks and append them to their blockchain. The chain with the most delegates is considered the valid one. This protocol is used by EOS and Tron.
- Byzantine Fault Tolerance (BFT): This protocol is based on a mathematical problem that involves reaching an agreement among a group of nodes, some of which may be faulty or malicious. The protocol assumes that there is a leader node that proposes a new block to the network. The other nodes then vote on whether to accept or reject the block. The block is accepted if more than two-thirds of the nodes agree on it. The leader node is changed periodically or randomly. This protocol is used by Stellar and Neo.

The following diagram illustrates the basic architecture of a blockchain network with a consensus protocol:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|     Node 1      |     |     Node 2      |     |     Node 3      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Consensus      |     |  Consensus      |     |  Consensus      |
|  Protocol       |     |  Protocol       |     |  Protocol       |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Blockchain     |     |  Blockchain     |     |  Blockchain