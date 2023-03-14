## Unit 3 - Permissioned Blockchains

A permissioned blockchain is a distributed ledger that is not publicly accessible. It can only be accessed by users with permissions. The users can only perform specific actions granted to them by the ledger administrators and are required to identify themselves through certificates or other digital means.

Permissioned blockchains are favored by entities who require security, identity, and role definition within the blockchain. They are becoming more common as businesses realize their benefits.

The following diagram illustrates the basic architecture of a permissioned blockchain:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Node 1         |      |  Node 2         |      |  Node 3         |
|                 |      |                 |      |                 |
|  +-----------+  |      |  +-----------+  |      |  +-----------+  |
|  |           |  |      |  |           |  |      |  |           |  |
|  |  Ledger   |  |      |  |  Ledger   |  |      |  |  Ledger   |  |
|  |           |  |      |  |           |  |      |  |           |  |
|  +-----------+  |      |  +-----------+  |      |  +-----------+  |
|                 |      |                 |      |                 |
|  +-----------+  |      |  +-----------+  |      |  +-----------+  |
|  |           |  |      |  |           |  |      |  |           |  |
|  |  Chain    |  |      |  |  Chain    |  |      |  |  Chain    |  |
|  |           |  |      |  |           |  |      |  |           |  |
|  +-----------+  |      |  +-----------+  |      |  +-----------+  |
|                 |      |                 |      |                 |
|  +-----------+  |      |  +-----------+  |      |  +-----------+  |
|  |           |  |      |  |           |  |      |  |           |  |
|  |  Access   |  |      |  |  Access   |  |      |  |  Access   |  |
|  |  Control  |  |      |  |  Control  |  |      |  |  Control  |  |
|  |           |  |      |  |           |  |      |  |           |  |
|  +-----------+  |      |  +-----------+  |      |  +-----------+  |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       +----------------------+----------------------+
                              |
                              |
                              v
                      +-----------------+
                      |                 |
                      |  Client         |
                      |                 |
                      |  +-----------+  |
                      |  |           |  |
                      |  |  Identity |  |
                      |  |           |  |
                      |  +-----------+  |
                      |                 |
                      |  +-----------+  |
                      |  |           |  |
                      |  |  Request  |  |
                      |  |           |  |
                      |  +-----------+  |
                      |                 |
                      +-----------------+
```

Each node in the permissioned blockchain has a ledger, a chain, and an access control layer. The ledger stores the state of the blockchain, the chain stores the history of transactions, and the access control layer regulates the actions of the authorized participants.

The client is the entity that interacts with the permissioned blockchain. The client has an identity that is verified by the access control layer of the nodes. The client can send requests to the nodes, such as reading or writing data, depending on the permissions granted to them.

The nodes communicate with each other to reach consensus on the validity of the transactions and update the ledger and the chain accordingly. The consensus mechanism may vary depending on the specific implementation of the permissioned blockchain.