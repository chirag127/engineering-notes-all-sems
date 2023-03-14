### Basic consensus mechanisms for the notes of the Unit 1 - Introduction to Blockchain in the subject of Block chain Architecture Design

- A consensus mechanism is any method used to achieve agreement, trust, and security across a decentralized computer network.
- In the context of blockchains and cryptocurrencies, consensus mechanisms are the methodologies used to ensure that all participants dispose of identical copies of the distributed database files.
- Consensus mechanisms play an essential part of securing information by encrypting it and using automated group verification.
- Consensus mechanisms also help to prevent data tampering and unauthorized access, whether it is malicious or not.
- Some of the objectives of a consensus mechanism are:
  - Agreement Seeking: A consensus mechanism should bring about as much agreement from the group as possible.
  - Collaborative: All the participants should aim to work together to achieve a result that puts the best interest of the group first.
  - Cooperative: All the participants shouldn't put their own interests first and work as a team more than individuals.
  - Egalitarian: A group trying to achieve consensus should be as egalitarian as possible. What this basically means that each and every vote has equal weightage. One person's vote can't be more important than another's.
  - Inclusive: As many people as possible should be involved in the consensus process. It shouldn't be like normal voting where people don't really feel like voting because they believe that their vote won't have any weightage in the long run.
- Some of the most prevalent consensus mechanisms in blockchain and cryptocurrency are :
  - Proof of Work (PoW): This mechanism requires computational power to solve an encrypted puzzle, called the hash. After the hash is solved by one miner (or a group working together), every node on the network verifies the data that has been changed by checking various parameters. This verification takes much less time than the process of solving the hash, which is called mining. PoW is used by Bitcoin, Ethereum, and many other cryptocurrencies.
    - Advantages: PoW is simple, robust, and secure. It creates a high level of trust and decentralization. It also incentivizes miners to contribute to the network and rewards them with new coins and transaction fees.
    - Disadvantages: PoW is energy-intensive, slow, and prone to scalability issues. It also creates a risk of 51% attacks, where a single entity or a group of miners can control more than half of the network's hashing power and manipulate the blockchain.
  - Proof of Stake (PoS): This mechanism does not require computational power to validate transactions, but rather relies on the stake or the amount of coins that a node holds. The more stake a node has, the more likely it is to be chosen as a validator and earn rewards. PoS is used by Cardano, Polkadot, and many other cryptocurrencies.
    - Advantages: PoS is more energy-efficient, faster, and scalable than PoW. It also reduces the risk of 51% attacks, as it would be very costly and irrational for a node to attack the network that it has a stake in.
    - Disadvantages: PoS is more complex, less secure, and less decentralized than PoW. It also creates a risk of nothing-at-stake attacks, where a node can validate multiple conflicting blocks without any penalty. It also favors the rich, as the more stake a node has, the more rewards it gets.
  - Delegated Proof of Stake (DPoS): This mechanism is a variation of PoS, where the nodes can delegate their stake to a group of representatives or delegates, who are responsible for validating transactions and maintaining the network. The delegates are elected by the nodes based on their stake and reputation. DPoS is used by EOS, Tron, and many other cryptocurrencies.
    - Advantages: DPoS is more efficient, faster, and scalable than PoS and PoW. It also allows for more democracy and participation, as the nodes can vote for their delegates and hold them accountable. It also incentivizes the delegates to act in the best interest of the network, as they can be voted out or penalized for any misconduct.
    - Disadvantages: DPoS is less secure and less decentralized than PoS and PoW. It also creates a risk of centralization, as the delegates can collude or become corrupted by external influences. It also favors the rich, as the more stake a node has, the more voting power it has.

- A possible mnemonic to remember the three consensus mechanisms is: **