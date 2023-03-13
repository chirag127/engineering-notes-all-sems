The following is a detailed ASCII diagram for Hyperledger Composer tool for the notes of the Unit 5 - Hyperledger Fabric (B) in the subject of Block chain Architecture Design.

Hyperledger Composer is an open-source platform that supports smart contract development. The platform focuses on allowing users to create business networks by means of making use of pre-built components. It’s designed for supporting blockchain applications in order to make them compatible with other Hyperledger tools.

Hyperledger Composer enables architects and developers to quickly create "full-stack" blockchain solutions. I.e. business logic that runs on the blockchain, REST APIs that expose the blockchain logic to web or mobile applications, as well as integrating the blockchain with existing enterprise systems of record.

Hyperledger Composer includes the following main components:

- Business Network Archive: Capturing the core data in a business network, including the business model, transaction logic and access controls, the Business Network Archive packages these elements up and deploys them to a runtime.
- Composer Runtime: The Composer Runtime is a component that runs on the Hyperledger Fabric peers and executes the business logic defined in the Business Network Archive.
- Composer Playground: The Composer Playground is a web-based tool that allows users to create, test and deploy business networks using a graphical user interface.
- Composer REST Server: The Composer REST Server is a component that generates a REST API from a deployed Business Network Archive, allowing web or mobile applications to interact with the blockchain network.
- Composer CLI: The Composer CLI is a command-line tool that allows users to perform various tasks related to Hyperledger Composer, such as creating, deploying, updating and testing business networks.

The following diagram illustrates the basic architecture of Hyperledger Composer:

```
+------------------+       +------------------+       +------------------+
|                  |       |                  |       |                  |
|  Web or Mobile   |       |  Enterprise      |       |  Hyperledger     |
|  Application     |       |  System of       |       |  Fabric          |
|                  |       |  Record          |       |                  |
+------------------+       +------------------+       +------------------+
       |                          |                          |
       |                          |                          |
       |                          |                          |
       |                          |                          |
       |                          |                          |
       |                          |                          |
       |                          |                          |
       |                          |                          |
       |                          |                          |
       |                          |                          |
       |                          |                          |
       |                          |                          |
       |                          |                          |
       |                          |                          |
+------------------+       +------------------+       +------------------+
|                  |       |                  |       |                  |
|  Composer REST   |       |  Composer        |       |  Composer        |
|  Server          |       |  Playground      |       |  Runtime         |
|                  |       |                  |       |                  |
+------------------+       +------------------+       +------------------+
       |                          |                          |
       |                          |                          |
       |                          |                          |
       |                          |                          |
       |                          |                          |
       |                          |                          |
       |                          |                          |
       |                          |                          |
+------------------+       +------------------+       +------------------+
|                  |       |                  |       |                  |
|  Business        |       |  Composer CLI    |       |  Business        |
|  Network Archive |       |                  |       |  Network Archive |
|                  |       |                  |       |                  |
+------------------+       +------------------+       +------------------+
```