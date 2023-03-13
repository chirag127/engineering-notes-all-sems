The following diagram illustrates the basic architecture of a privacy and security on blockchain system:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   User A        |      |   User B        |      |   User C        |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Private Key   |      |   Private Key   |      |   Private Key   |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Public Key    |      |   Public Key    |      |   Public Key    |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         +---------------------->                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      +----------------------+
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         +--------------------------------------------->|
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         v                      v                      v
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Node A        |      |   Node B        |      |   Node C        |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Blockchain    |      |   Blockchain    |      |   Blockchain    |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```

The diagram shows how users can use private and public keys to secure transactions on a blockchain network. Each user has a pair of keys, one for encryption and one for decryption. The private key is kept secret and the public key is shared with other users. When a user wants to send a transaction to another user, they encrypt the transaction with the recipient's public key. Only the recipient can decrypt the transaction with their private key. The encrypted transaction is then broadcasted to the network and verified by the nodes. The nodes also maintain a copy of the blockchain, which is a distributed ledger of all transactions. The blockchain is immutable and transparent, meaning that anyone can see the history of transactions but cannot alter or delete them. This way, the blockchain provides security and privacy for the users.