According to , the design primitives of blockchain are based on three aspects: transaction design, consensus design and block design. Transaction design refers to how the data is structured and validated on the blockchain. Consensus design refers to how the nodes agree on the state of the blockchain. Block design refers to how the transactions are grouped and linked on the blockchain.

A possible ASCII diagram for the design primitives of blockchain is shown below:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Block Design   |<--->| Consensus Design|<--->|Transaction Design|
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                       |                       |
       |                       |                       |
       v                       v                       v
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Block Header   |     |  Proof of Work  |     |  Digital        |
|  Block Body     |     |  Proof of Stake |     |  Signature      |
|  Block Hash     |     |  Byzantine      |     |  Cryptographic  |
|  Block Number   |     |  Fault Tolerance|     |  Hash           |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```