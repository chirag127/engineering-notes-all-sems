### Hyperledger Composer Tool

Hyperledger Composer is a set of open source tools that allows business owners, operators, and developers a way to create blockchain applications and smart contracts aimed at solving business problems and/or improving operational efficiencies. It is an example of a commercial application of blockchain-as-a-service (BaaS) .

Hyperledger Composer is part of the Hyperledger project, which is a collaborative effort to advance cross-industry blockchain technologies. Composer was designed to facilitate the creation of open-source blockchain applications that foster collaboration within organizations and business networks .

Some of the features and benefits of Hyperledger Composer are:

- A modeling language that allows non-developers and developers to model their business network in a simple but expressive way. The language features keywords such as asset, participant, transaction, and registry .
- A transaction processor function that allows developers to encode business logic as JavaScript code that can run on any platform that supports standard JavaScript .
- A declarative access control mechanism that allows developers to specify what resources can be accessed by which participants. Access control is automatically enforced by the runtime .
- A client and administrative API, as well as a command-line interface, that allows developers and operators to deploy and interact with business networks from Node.js applications or automation scripts .
- A web-based playground that allows new and experienced users to learn the language, model their business network, and test that network from their web browser. The playground can work in both offline mode, using a simulated network, and online mode, when connected to a real running network .
- A REST API support and integration capabilities that expose a running network as a REST API that can easily be consumed by client applications. A LoopBack connector for business networks has been developed for this purpose .
- A syntax highlighting support for two popular open-source editors, Atom and VS Code, with future plans to include testing/debugging capabilities .
- An application generation using the Yeoman framework that allows client application developers to quickly generate a skeleton Angular 2 or CLI application to use as a starting point, allowing them to focus on UI/UX rather than business network interactions .

Hyperledger Composer is currently in end-of-life status, meaning that none of the maintainers are actively developing new features or providing support via GitHub issues. However, pull requests from the community are still accepted and merged. It is highly recommended that developers use Hyperledger Fabric v1.4+ instead, which features significant improvements to the developer experience, including a new programming model .