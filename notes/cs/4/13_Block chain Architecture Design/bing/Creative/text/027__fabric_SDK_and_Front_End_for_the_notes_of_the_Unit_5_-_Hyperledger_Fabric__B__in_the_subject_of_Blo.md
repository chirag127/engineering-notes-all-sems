### Fabric SDK and Front End

- Fabric SDK is a set of libraries and tools that allow developers to interact with a Fabric network from various programming languages.
- Fabric SDK provides APIs for creating and managing channels, peers, orderers, smart contracts, and users.
- Fabric SDK also supports invoking and querying smart contracts, listening to events, and signing and verifying transactions.
- Fabric SDK can be used to build applications that run on top of a Fabric network, such as web or mobile apps, or to integrate Fabric with existing systems and platforms.
- Fabric SDK is available in different languages, such as Node.js, Java, Python, and Go.
- Fabric SDK follows a modular and pluggable design, allowing developers to customize and extend its functionality according to their needs.
- Fabric SDK requires a connection profile, which is a JSON or YAML file that contains the information about the Fabric network, such as the endpoints, certificates, and MSPs of the peers and orderers, the channel names, and the smart contract names and versions.
- Fabric SDK also requires a wallet, which is a secure storage for the cryptographic identities of the users who interact with the Fabric network. A wallet can be a file system, a database, or a hardware device.
- Fabric SDK uses the concept of a gateway, which is an abstraction that represents a connection to a Fabric network. A gateway can be created from a connection profile and a user identity from a wallet. A gateway allows developers to access a specific channel and smart contract on the Fabric network.
- Fabric SDK also uses the concept of a network, which is an abstraction that represents a channel on the Fabric network. A network can be obtained from a gateway, and it allows developers to invoke and query smart contracts, and to listen to events on the channel.
- Fabric SDK also uses the concept of a contract, which is an abstraction that represents a smart contract on the Fabric network. A contract can be obtained from a network, and it allows developers to invoke and query the smart contract's functions, and to get the smart contract's metadata.
- Fabric SDK also uses the concept of a transaction, which is an abstraction that represents an invocation or a query of a smart contract function on the Fabric network. A transaction can be created from a contract, and it allows developers to set the parameters, the endorsement policy, the timeout, and the transient data for the smart contract function. A transaction can be submitted or evaluated, depending on whether it modifies or reads the ledger state, respectively.
- Fabric SDK also uses the concept of an event, which is an abstraction that represents a notification of a change in the Fabric network, such as a block being committed, a smart contract being instantiated, or a smart contract emitting a custom event. An event can be obtained from a network or a contract, and it allows developers to register listeners and handlers for the event.

- Front End is the part of an application that interacts with the users, such as a web or mobile interface. Front End can be built using various technologies, such as HTML, CSS, JavaScript, React, Angular, etc.
- Front End can use Fabric SDK to communicate with a Fabric network, such as sending transactions, querying the ledger, or receiving events.
- Front End can also use other technologies to enhance the user experience, such as web sockets, RESTful APIs, or GraphQL.
- Front End can also use other services to store and process data, such as databases, cloud platforms, or analytics tools.