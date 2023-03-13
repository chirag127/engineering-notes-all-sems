The following is a possible ASCII diagram for digital identity using blockchain architecture, based on the information from the search results. The diagram shows how a user can request, verify, and share their identity credentials with different service providers, using a blockchain network and a smart contract. The diagram also shows how a certification authority can issue and revoke credentials on the blockchain.

### Digital identity using blockchain architecture

```
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  User device    |        | Service provider|        | Certification   |
|                 |        |                 |        | authority       |
+-----------------+        +-----------------+        +-----------------+
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |  +-----------------+
       |                         |                         |  |                 |
       |                         |                         |  |  Blockchain     |
       |                         |                         |  |  network        |
       |                         |                         |  |                 |
       |                         |                         |  +-----------------+
       |                         |                         |         |
       |                         |                         |         |
       |                         |                         |         |
       |                         |                         |         |
       |                         |                         |         |
       |                         |                         |         |
       |                         |                         |         |
       |                         |                         |         |
       |                         |                         |         |
       |                         |                         |         |
       |                         |                         |         |
       |                         |                         |         |  +-----------------+
       |                         |                         |         |  |                 |
       |                         |                         |         |  |  Smart contract |
       |                         |                         |         |  |                 |
       |                         |                         |         |  +-----------------+
       |                         |                         |         |         |
       |                         |                         |         |         |
       |                         |                         |         |         |
       |                         |                         |         |         |
       |                         |                         |         |         |
       |                         |                         |         |         |
       |                         |                         |         |         |
       |                         |                         |         |         |
       |                         |                         |         |         |
       |                         |                         |         |         |
       |------------------------>|                         |         |         |
       | Request service        |                         |         |         |
       |<------------------------|                         |         |         |
       | Send credential request|                         |         |         |
       |------------------------>|                         |         |         |
       |                         | Verify credential request|         |         |
       |                         |------------------------>|         |         |
       |                         |                         | Issue credential |
       |                         |                         |----------------->|
       |                         |                         |<-----------------|
       |                         |                         | Revoke credential|
       |                         |<------------------------|         |         |
       |                         | Send credential         |         |         |
       |<------------------------|                         |         |         |
       | Verify credential      |                         |         |         |
       |------------------------>|                         |         |         |
       |                         |<------------------------|         |         |
       |                         | Service granted         |         |         |
       |<------------------------|                         |         |         |
       |                         |                         |         |         |
```