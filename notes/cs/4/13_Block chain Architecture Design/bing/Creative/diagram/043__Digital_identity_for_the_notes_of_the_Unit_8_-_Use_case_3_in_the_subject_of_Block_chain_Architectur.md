The following diagram illustrates the basic architecture of a blockchain-based digital identity system, using ASCII art. The diagram is based on the information from the web search results   .

### Digital identity

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    User A       |    |    User B       |    |    User C       |
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
       |                     |                     |
       v                     v                     v
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Wallet A     |    |    Wallet B     |    |    Wallet C     |
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
       v                     v                     v
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Verifier A   |    |    Verifier B   |    |    Verifier C   |
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
       v                     v                     v
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Issuer A     |    |    Issuer B     |    |    Issuer C     |
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
       v                     v                     v
+---------------------------------------------------------------+
|                                                               |
|                      Blockchain Network                       |
|                                                               |
+---------------------------------------------------------------+
```

The diagram shows the following components and interactions:

- Users are the individuals who own and control their digital identities. They can create, manage, and share their credentials using their wallets.
- Wallets are the applications that store and manage the users' credentials and keys. They can also interact with verifiers and issuers to request and receive credentials.
- Verifiers are the entities that need to verify the users' credentials for various purposes, such as access control, authentication, or authorization. They can request and validate the credentials from the users' wallets using the blockchain network.
- Issuers are the entities that issue the credentials to the users, such as governments, organizations, or institutions. They can create and sign the credentials using the blockchain network and send them to the users' wallets.
- Blockchain network is the distributed ledger that provides the infrastructure and security for the digital identity system. It records the transactions and events related to the credentials, such as issuance, verification, revocation, or expiration. It also enables the interoperability and trust among the participants, using open standards and protocols.