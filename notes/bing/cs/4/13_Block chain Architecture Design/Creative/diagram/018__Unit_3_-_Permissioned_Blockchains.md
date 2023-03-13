## Unit 3 - Permissioned Blockchains

A permissioned blockchain is a type of distributed ledger that is not publicly accessible. It can only be accessed by users with permissions. The users can only perform specific actions granted to them by the network administrator. A permissioned blockchain can have different levels of access control, such as read-only, write-only, or full access. A permissioned blockchain can also have different consensus mechanisms, such as proof-of-authority, proof-of-stake, or Byzantine fault tolerance.

The following diagram illustrates the basic architecture of a permissioned blockchain:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  User A         |    |  User B         |    |  User C         |
|  (Read-only)    |    |  (Write-only)   |    |  (Full access)  |
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
       v                     v                     v
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Node A         |    |  Node B         |    |  Node C         |
|  (Validator)    |    |  (Validator)    |    |  (Validator)    |
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
                             v
+-----------------+
|                 |
|  Blockchain     |
|  (Ledger)       |
|                 |
+-----------------+
```

In this diagram, there are three users and three nodes in the permissioned blockchain network. Each user has a different level of access to the blockchain. User A can only read the data on the blockchain, User B can only write new data to the blockchain, and User C can both read and write data to the blockchain. Each user communicates with a node that validates their transactions and broadcasts them to the other nodes. The nodes use a consensus mechanism to agree on the state of the blockchain and update the ledger accordingly. The ledger is the shared record of all the transactions that have occurred on the blockchain.