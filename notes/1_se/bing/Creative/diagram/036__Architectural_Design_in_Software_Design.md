Architectural design in software engineering is the process of defining a collection of hardware and software components and their interfaces to establish the framework for the development of a computer system. Architectural design is also used to represent how the system will act on the basis of software elements, relationships and properties. Architectural design can be expressed as a block diagram defining an overview of the system structure, features of the components, and how these components communicate with each other to share data.

There are many different types of architectural design patterns that can be used to address common software design challenges and goals. Some examples of architectural design patterns are:

- The client-server pattern, which is a peer-to-peer architecture that is comprised of a client, which requests a service, and a server, which provides the service.
- The command query responsibility segregation (CQRS) pattern, which separates read and write activities to provide greater stability, scalability, and performance.
- The controller-responder pattern, which divides the architecture into two components: The controller handles the data and distributes workloads, and the responder replicates data from the controller and generates results.
- The microservices pattern, which breaks down the system into small, independent, and loosely coupled services that communicate through well-defined interfaces.

The following diagram illustrates the basic architecture of a microservices pattern using ASCII art:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Service A      |     |  Service B      |     |  Service C      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       v                     v                     v
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Database A     |     |  Database B     |     |  Database C     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```