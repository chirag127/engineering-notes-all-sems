Architectural design in software engineering is the process of defining a collection of hardware and software components and their interfaces to establish the framework for the development of a computer system. It is expressed as a block diagram defining an overview of the system structure, features of the components, and how these components communicate with each other to share data.

There are many different types of architectural design patterns that can be used to represent the software architecture, such as layered, client-server, microservices, event-driven, etc. Each pattern has its own advantages and disadvantages, and the choice of the best pattern depends on the requirements, goals, and constraints of the software project.

The following diagram illustrates the basic architecture of a client-server pattern, which is one of the most common and simple patterns. In this pattern, the software system is divided into two components: a client and a server. The client is the component that requests services from the server, and the server is the component that provides services to the client. The client and the server communicate with each other using a network protocol, such as HTTP, TCP, etc. The client and the server can be deployed on different machines, and there can be multiple clients and servers in the system.

### Architectural Design in Software Design

```
+-----------------+        +-----------------+
|                 |        |                 |
|    Client 1     |        |    Server 1     |
|                 |        |                 |
+-----------------+        +-----------------+
      |   |                      |   |
      |   |                      |   |
      |   |                      |   |
      |   |                      |   |
      |   |                      |   |
      |   |                      |   |
      |   |                      |   |
      |   |                      |   |
      |   |                      |   |
      |   |                      |   |
      |   |                      |   |
+-----------------+        +-----------------+
|                 |        |                 |
|    Client 2     |        |    Server 2     |
|                 |        |                 |
+-----------------+        +-----------------+
```