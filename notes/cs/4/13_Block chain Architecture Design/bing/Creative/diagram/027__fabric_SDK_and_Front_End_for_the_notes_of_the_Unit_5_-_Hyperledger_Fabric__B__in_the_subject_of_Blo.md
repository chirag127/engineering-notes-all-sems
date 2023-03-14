The following diagram illustrates the basic architecture of a Fabric SDK and Front End for the notes of the Unit 5 - Hyperledger Fabric (B) in the subject of Block chain Architecture Design:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    Front End    |       |    Fabric SDK   |       |    Fabric CA    |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Web or Mobile  |       |  Node.js, Java, |       |  Certificate    |
|  Application    |       |  Go, Python,    |       |  Authority      |
|                 |       |  REST, etc.     |       |                 |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Uses SDK APIs  |       |  Uses gRPC to   |       |  Issues and     |
|  to interact    |       |  interact with  |       |  manages        |
|  with network   |       |  network peers  |       |  identities     |
|                 |       |  and orderers   |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
```

The front end is the web or mobile application that provides the user interface for the blockchain network. It can use any framework or library that suits the developer's preference.

The Fabric SDK is the software development kit that provides the APIs for the front end to interact with the blockchain network. It can be written in various programming languages, such as Node.js, Java, Go, Python, or REST. The Fabric SDK uses gRPC to communicate with the network peers and orderers, and to submit transactions and queries to the ledger.

The Fabric CA is the certificate authority that issues and manages the identities of the network participants. It provides a secure way to enroll peers and users, and to generate transaction certificates for pseudonymous transactions. The Fabric CA can be integrated with other standard certificate authorities, such as OpenSSL.