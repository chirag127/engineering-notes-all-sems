### Requirements for the consensus protocols for the notes of the Unit 2 - Consensus in the subject of Block chain Architecture Design

- Consensus protocols are the rules that govern how the nodes in a blockchain network agree on the validity and order of transactions.
- Consensus protocols are essential for ensuring the security, consistency, and decentralization of a blockchain network.
- Consensus protocols can be classified into two broad categories: **permissionless** and **permissioned**.
- Permissionless consensus protocols allow anyone to join and participate in the network, without requiring any prior authorization or identity verification. Examples of permissionless consensus protocols are **Proof-of-Work (PoW)**, **Proof-of-Stake (PoS)**, and **Delegated Proof-of-Stake (DPoS)**.
- Permissioned consensus protocols restrict the participation in the network to a predefined set of nodes, usually based on some criteria such as identity, reputation, or stake. Examples of permissioned consensus protocols are **Practical Byzantine Fault Tolerance (PBFT)**, **Raft**, and **Stellar Consensus Protocol (SCP)**.
- The requirements for the consensus protocols depend on the design goals and trade-offs of the blockchain network. Some of the common requirements are:

  - **Safety**: The consensus protocol should ensure that the network reaches a consistent and correct state, even in the presence of faulty or malicious nodes.
  - **Liveness**: The consensus protocol should ensure that the network can process and confirm transactions in a timely manner, without getting stuck or delayed indefinitely.
  - **Fault tolerance**: The consensus protocol should ensure that the network can tolerate a certain number of failures or attacks, without compromising the safety or liveness properties.
  - **Scalability**: The consensus protocol should ensure that the network can handle a large number of transactions and nodes, without sacrificing the performance or security.
  - **Incentive compatibility**: The consensus protocol should ensure that the nodes have an incentive to follow the rules and cooperate with each other, rather than deviate or cheat for their own benefit.
  - **Simplicity**: The consensus protocol should be easy to understand, implement, and verify, without introducing unnecessary complexity or overhead.