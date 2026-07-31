### Architectural models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Architectural models are system models that describe the organization of components across the network and their interrelationship.
- Architectural models can help to understand the design trade-offs, performance issues, and scalability challenges of distributed systems.
- Some common architectural models for distributed systems are:

  - Client-server architecture: A model where one or more servers provide services to multiple clients that request and consume them. The servers and clients can be distributed across different machines and communicate over a network.
  - Broker architecture: A model where a broker component acts as an intermediary between clients and servers, hiding the details of service location, invocation, and communication. The broker can also provide additional services such as security, load balancing, and fault tolerance.
  - Service-oriented architecture (SOA): A model where services are loosely coupled, reusable, and interoperable components that can be composed to create complex applications. Services are described by their functionality, interface, and quality of service, and are accessed through standard protocols such as SOAP and REST.
  - Peer-to-peer architecture: A model where each node in the network can act as both a client and a server, and can communicate directly with other nodes without a central authority. Peer-to-peer systems can be decentralized, self-organizing, and resilient to failures.
  - Distributed object architecture: A model where objects are distributed across the network and can be accessed by remote method invocation (RMI) or remote procedure call (RPC). Distributed objects can encapsulate state and behavior, and can support inheritance, polymorphism, and dynamic binding.
  - Distributed component architecture: A model where components are distributed across the network and can be assembled into applications by using connectors that specify the communication protocols and contracts. Distributed components can be deployed, updated, and replaced independently, and can support interfaces, events, and properties.

- Each architectural model has its own advantages and disadvantages, and can be suitable for different types of distributed systems and applications. The choice of an architectural model depends on various factors such as the system requirements, the network characteristics, the available resources, and the security and reliability constraints.