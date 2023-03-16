# Hyperledger Composer Tool

Hyperledger Composer is a set of open source tools that allows business owners, operators, and developers a way to create blockchain applications and smart contracts aimed at solving business problems and/or improving operational efficiencies. It is an example of a commercial application of blockchain-as-a-service (BaaS)  .

Some of the features and benefits of Hyperledger Composer are:

- It simplifies the development of blockchain applications by providing a high-level abstraction layer that hides the complexity of the underlying blockchain platform (Hyperledger Fabric).
- It enables the modeling of business assets, participants, transactions, and access control rules using a domain-specific language (DSL) called Composer Modeling Language (CML).
- It allows the generation of REST APIs and user interfaces (UIs) from the business model, enabling easy integration with existing systems and applications.
- It supports the testing and deployment of blockchain applications across multiple environments, such as local, cloud, or hybrid networks.
- It fosters collaboration and innovation among business network members by enabling the sharing of business models, smart contracts, and applications through an online repository called Composer Playground.

Hyperledger Composer consists of the following components:

- Composer Modeling Language (CML): A DSL for defining the structure and behavior of a business network, including assets, participants, transactions, and access control rules.
- Composer Runtime: A component that executes the smart contracts (also called chaincode) defined in CML on a Hyperledger Fabric peer node.
- Composer CLI: A command-line interface for interacting with the Composer Runtime and managing the lifecycle of a business network.
- Composer REST Server: A component that exposes the business network as a RESTful web service, allowing external applications to invoke transactions and query the ledger state.
- Composer Playground: A web-based tool for creating, testing, and deploying business networks using a graphical user interface (GUI).
- Composer UI: A component that generates a UI for a business network based on the CML definition, allowing end-users to interact with the blockchain application.

Hyperledger Composer is no longer actively maintained or supported by its original developers as of August 2021. It is recommended to use other tools and frameworks for developing blockchain applications on Hyperledger Fabric, such as Hyperledger Fabric SDKs, Hyperledger Caliper, or Hyperledger Cello  .