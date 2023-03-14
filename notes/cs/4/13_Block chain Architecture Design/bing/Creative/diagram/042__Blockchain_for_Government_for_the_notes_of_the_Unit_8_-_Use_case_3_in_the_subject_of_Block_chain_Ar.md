There are many possible use cases for blockchain technology in government applications, such as supply chain, voting, taxation, land ownership, identity, and citizen engagement. However, for the purpose of this assignment, I will focus on one specific use case: healthcare data sharing.

Healthcare data sharing is a challenge for many governments, as they need to balance the privacy and security of sensitive medical records with the efficiency and interoperability of health information systems. Blockchain technology can offer a solution to this problem, by creating a decentralized and immutable ledger of health data transactions that can be accessed by authorized parties with proper consent.

The following diagram illustrates the basic architecture of a blockchain-based healthcare data sharing system:

```
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|  Patient         |     |  Healthcare      |     |  Government      |
|                  |     |  Provider        |     |  Agency          |
|                  |     |                  |     |                  |
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|  - Generates     |     |  - Requests      |     |  - Requests      |
|    public/private|     |    patient's     |     |    patient's     |
|    key pair      |     |    consent and   |     |    consent and   |
|  - Grants or     |     |    public key    |     |    public key    |
|    revokes       |     |  - Encrypts      |     |  - Encrypts      |
|    consent to    |     |    health data   |     |    health data   |
|    access health |     |    with patient's|     |    with patient's|
|    data          |     |    public key    |     |    public key    |
|  - Stores        |     |  - Stores        |     |  - Stores        |
|    encrypted     |     |    encrypted     |     |    encrypted     |
|    health data   |     |    health data   |     |    health data   |
|    on blockchain |     |    on blockchain |     |    on blockchain |
|                  |     |                  |     |                  |
+------------------+     +------------------+     +------------------+
          |                      |                      |
          |                      |                      |
          |                      |                      |
          +----------------------+----------------------+
                                 |
                                 |
                                 v
                          +------------------+
                          |                  |
                          |  Blockchain      |
                          |                  |
                          +------------------+
                          |                  |
                          |  - Stores        |
                          |    encrypted     |
                          |    health data   |
                          |    transactions  |
                          |  - Validates     |
                          |    transactions  |
                          |    by consensus  |
                          |  - Provides      |
                          |    audit trail   |
                          |    of data       |
                          |    access        |
                          |                  |
                          +------------------+
```