### REST and Systems of Systems for the notes of the Unit 2 - Cloud Enabling Technologies Service Oriented Architecture in the subject of Cloud Computing

#### REST

- REST stands for Representational State Transfer, which is a software architectural style that defines a set of constraints to be used for creating web services.
- It is a lightweight and flexible approach that uses HTTP protocol to transfer data and is commonly used for building APIs for web-based applications.
- RESTful APIs follow a client-server model where the server exposes a set of endpoints (URLs) that the client can use to perform operations on the server-side resources.
- The four main principles of REST are:
  - Client-Server: The client and server are separate entities that communicate through HTTP protocol.
  - Stateless: Each request from the client to the server must contain all the necessary information to complete the request. The server does not store any client context between requests.
  - Cacheable: Responses from the server can be cached to improve performance.
  - Uniform Interface: The interface between the client and server should be uniform to allow for scalability and evolution of the system.
- Some advantages of using RESTful APIs are:
  - Flexibility: RESTful APIs can be used with any programming language or platform that supports HTTP protocol.
  - Scalability: RESTful APIs can be easily scaled horizontally by adding more servers to the system.
  - Simplicity: RESTful APIs have a simple and intuitive interface that makes them easy to use and understand.
- Some disadvantages of using RESTful APIs are:
  - Security: The stateless nature of RESTful APIs makes them vulnerable to security attacks such as cross-site scripting (XSS) and cross-site request forgery (CSRF).
  - Performance: RESTful APIs can have lower performance compared to other protocols that use binary data formats.

#### Systems of Systems

- Systems of Systems (SoS) is a collection of independent systems that are connected to each other to achieve a common goal.
- SoS can be used to build complex distributed systems that are more scalable and flexible than traditional monolithic systems.
- SoS can be classified into two types:
  - Hierarchical SoS: In this type of SoS, there is a clear hierarchy of systems where some systems are subordinates of other systems.
  - Networked SoS: In this type of SoS, all systems are equal and communicate with each other to achieve a common goal.
- Some advantages of using SoS are:
  - Scalability: SoS can be easily scaled by adding new systems to the network.
  - Flexibility: SoS can be easily modified by adding or removing systems from the network.
  - Resilience: SoS can be designed to be resilient to failure by using redundancy and fault-tolerant techniques.
- Some disadvantages of using SoS are:
  - Complexity: SoS can be difficult to design and manage due to the large number of components and interactions involved.
  - Interoperability: SoS can face interoperability issues when systems from different vendors or with different interfaces are connected to the network.

### Mnemonic

- To remember the four main principles of REST, you can use the acronym CRUD which stands for Create, Read, Update, and Delete. These are the basic operations that RESTful APIs use to interact with server-side resources.