Hyperledger Composer is a set of open source tools that allows business owners, operators, and developers a way to create blockchain applications and smart contracts aimed at solving business problems and/or improving operational efficiencies. It is an example of a commercial application of blockchain-as-a-service (BaaS).

The following diagram illustrates the basic architecture of Hyperledger Composer:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Client         |       |  REST Server    |       |  Blockchain     |
|  Application    |       |                 |       |  Fabric         |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Angular, CLI,  |       |  LoopBack       |       |  Peer Nodes     |
|  etc.           |       |  Connector      |       |                 |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Composer       |       |  Composer       |       |  Composer       |
|  JavaScript SDK |       |  REST API       |       |  Runtime        |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Business       |       |  Business       |       |  Business       |
|  Network        |       |  Network        |       |  Network        |
|  Definition     |       |  Definition     |       |  Definition     |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
```

The diagram shows the following components:

- Client Application: This is the end-user interface that interacts with the blockchain network through the REST server or the JavaScript SDK. It can be built using various frameworks, such as Angular, CLI, etc.
- REST Server: This is a server that exposes the blockchain network as a REST API, using the LoopBack connector. It allows client applications to access the network without writing any code.
- Blockchain Fabric: This is the underlying distributed ledger platform that provides consensus, ordering, and security for the network. It consists of peer nodes that execute and validate transactions.
- Composer JavaScript SDK: This is a library that allows client applications to interact with the blockchain network programmatically, using JavaScript code. It provides methods for deploying, querying, and updating business networks.
- Composer REST API: This is a specification that defines the REST endpoints and payloads for accessing the blockchain network. It is implemented by the REST server and can be consumed by client applications.
- Composer Runtime: This is a component that runs on each peer node and executes the business logic of the network, such as transaction processor functions and access control rules. It also interacts with the Fabric chaincode API to submit and query transactions.
- Business Network Definition: This is a package that contains the model, logic, and access control of the network. It is written using the Composer modelling language, JavaScript, and ACL files. It is deployed to the Composer runtime and defines the assets, participants, transactions, and registries of the network.