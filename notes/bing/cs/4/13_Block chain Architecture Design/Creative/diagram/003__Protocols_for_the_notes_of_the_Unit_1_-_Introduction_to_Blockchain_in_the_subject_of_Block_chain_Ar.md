Protocols are the rules and standards that govern the communication and operation of a blockchain network. They aim to address the four principles of security, decentralization, consistency, and scalability. Depending on the type and design of the blockchain, different protocols may be used to achieve these goals.

One of the most important protocols in blockchain architecture is the consensus protocol, which is the mechanism by which the nodes in the network agree on the validity and order of transactions. Consensus protocols ensure that the blockchain is consistent, secure, and resilient to attacks. There are many types of consensus protocols, such as proof-of-work (PoW), proof-of-stake (PoS), proof-of-authority (PoA), and Byzantine fault tolerance (BFT).

Another protocol that affects the blockchain architecture is the access protocol, which determines who can join and participate in the network. Access protocols can be classified into public, private, and consortium blockchains. Public blockchains are open-source and permissionless, meaning anyone can join and validate transactions. Private blockchains are closed-source and permissioned, meaning only authorized entities can join and validate transactions. Consortium blockchains are a hybrid of public and private blockchains, where a group of trusted entities can join and validate transactions.

A third protocol that influences the blockchain architecture is the smart contract protocol, which is the layer that enables the execution of programmable logic and business rules on the blockchain. Smart contracts are self-enforcing agreements that can automate transactions and interactions between parties. Smart contracts can be written in different languages and run on different platforms, depending on the blockchain technology chosen. Some examples of smart contract platforms are Ethereum, Hyperledger Fabric, and Corda.

The following diagram illustrates the basic architecture of a blockchain network, showing the different protocols and components involved:

```
+-----------------------------------------------------------------+
|                                                                 |
|                          Blockchain Network                     |
|                                                                 |
+-----------------------------------------------------------------+
|                                                                 |
|   +-----------------+    +-----------------+    +-----------------+
|   |                 |    |                 |    |                 |
|   |      Node 1     |    |      Node 2     |    |      Node 3     |
|   |                 |    |                 |    |                 |
|   +-----------------+    +-----------------+    +-----------------+
|   |                 |    |                 |    |                 |
|   |  Smart Contract |    |  Smart Contract |    |  Smart Contract |
|   |    Protocol     |    |    Protocol     |    |    Protocol     |
|   |                 |    |                 |    |                 |
|   +-----------------+    +-----------------+    +-----------------+
|   |                 |    |                 |    |                 |
|   |   Consensus     |    |   Consensus     |    |   Consensus     |
|   |    Protocol     |    |    Protocol     |    |    Protocol     |
|   |                 |    |                 |    |                 |
|   +-----------------+    +-----------------+    +-----------------+
|   |                 |    |                 |    |                 |
|   |    Access       |    |    Access       |    |    Access       |
|   |    Protocol     |    |    Protocol     |    |    Protocol     |
|   |                 |    |                 |    |                 |
|   +-----------------+    +-----------------+    +-----------------+
|   |                 |    |                 |    |                 |
|   |    Ledger       |    |    Ledger       |    |    Ledger       |
|   |                 |    |                 |    |                 |
|   +-----------------+    +-----------------+    +-----------------+
|                                                                 |
+-----------------------------------------------------------------+
```