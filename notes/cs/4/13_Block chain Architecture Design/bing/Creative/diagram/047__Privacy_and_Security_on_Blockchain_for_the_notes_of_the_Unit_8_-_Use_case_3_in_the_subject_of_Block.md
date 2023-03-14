The following diagram illustrates the basic architecture of a privacy and security on blockchain system:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   User A        |     |   User B        |     |   User C        |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Private Key   |     |   Private Key   |     |   Private Key   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Public Key    |     |   Public Key    |     |   Public Key    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
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
+---------------------------------------------------------------+
|                                                               |
|                      Blockchain Network                       |
|                                                               |
+---------------------------------------------------------------+
|                                                               |
|                      Consensus Mechanism                      |
|                                                               |
+---------------------------------------------------------------+
|                                                               |
|                      Data Validation                          |
|                                                               |
+---------------------------------------------------------------+
|                                                               |
|                      Data Encryption                          |
|                                                               |
+---------------------------------------------------------------+
|                                                               |
|                      Data Storage                             |
|                                                               |
+---------------------------------------------------------------+
```

The diagram shows how users can interact with the blockchain network using their private and public keys. The private key is used to sign transactions and prove ownership of the data, while the public key is used to verify transactions and encrypt or decrypt data. The blockchain network uses a consensus mechanism to agree on the validity of transactions and the state of the ledger. The data is encrypted using cryptographic algorithms to ensure confidentiality and integrity. The data is stored in blocks that are linked together by hashes to form a chain that is distributed across the network. The blockchain network provides security and privacy for the users by using asymmetric cryptography, decentralization and consensus.