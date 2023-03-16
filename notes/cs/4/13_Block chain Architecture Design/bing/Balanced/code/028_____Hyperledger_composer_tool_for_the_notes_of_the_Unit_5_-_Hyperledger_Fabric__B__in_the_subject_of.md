### Hyperledger Composer Tool

Hyperledger Composer is a set of open source tools that allows business owners, operators, and developers a way to create blockchain applications and smart contracts aimed at solving business problems and/or improving operational efficiencies. It is an example of a commercial application of blockchain-as-a-service (BaaS)  .

Some of the features and benefits of Hyperledger Composer are:

- It simplifies the development of blockchain applications by providing a high-level abstraction layer that hides the complexity of the underlying blockchain platform (Hyperledger Fabric).
- It enables the modeling of business assets, participants, transactions, and access control rules using a domain-specific language (DSL) called Composer Modeling Language (CML).
- It allows the generation of REST APIs and user interfaces from the business model, enabling easy integration with existing systems and applications.
- It supports the testing and deployment of business networks across multiple peers and channels using a command-line interface (CLI) or a web-based playground.
- It fosters collaboration and innovation within and across business networks by enabling the sharing and reuse of business models, smart contracts, and components   .

Hyperledger Composer is composed of the following components:

- Composer Modeling Language (CML): A DSL for defining the structure and behavior of a business network, including assets, participants, transactions, and access control rules.
- Composer Runtime: A smart contract that implements the logic and validation of the business network, and interacts with the ledger and world state of Hyperledger Fabric.
- Composer CLI: A command-line tool for creating, testing, and deploying business networks, and interacting with the Composer Runtime.
- Composer REST Server: A Node.js application that exposes the business network as a REST API, allowing external applications to invoke transactions and query the ledger.
- Composer Playground: A web-based tool for creating, testing, and deploying business networks, and interacting with the Composer Runtime and the Composer REST Server.
- Composer LoopBack Connector: A LoopBack connector that enables the creation of LoopBack models from the business network definition, and the mapping of CRUD operations to transactions.
- Composer Angular Generator: A Yeoman generator that creates Angular applications from the business network definition, and the Composer REST Server   .