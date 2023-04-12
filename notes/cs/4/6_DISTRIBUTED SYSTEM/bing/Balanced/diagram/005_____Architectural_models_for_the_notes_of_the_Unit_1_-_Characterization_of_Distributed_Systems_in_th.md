### Architectural models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Architectural models are system models that describe the organization of components across the network and their interrelationship.
- Architectural models can help to understand the design trade-offs, performance issues, and scalability challenges of distributed systems.
- Some common architectural models for distributed systems are:

  - Client-server architecture: A model where one or more servers provide services to multiple clients that request and consume them. The servers can be centralized or distributed, and the clients can be thin (minimal processing) or thick (more processing) depending on the application logic and data distribution.
  - Broker architecture: A model where a broker component acts as an intermediary between clients and servers, hiding the details of service location, invocation, and communication. The broker can also provide additional services such as security, caching, load balancing, and fault tolerance. An example of a broker architecture is CORBA (Common Object Request Broker Architecture).
  - Service-oriented architecture (SOA): A model where services are loosely coupled, reusable, and platform-independent components that communicate using standard protocols and interfaces. Services can be composed into workflows or business processes to achieve higher-level functionality. An example of a SOA is the web services architecture based on XML, SOAP, WSDL, and UDDI.
  - Peer-to-peer architecture: A model where nodes in the network act as both clients and servers, sharing resources and services without any central coordination or authority. Peer-to-peer systems can be classified into structured (based on a distributed hash table or DHT) or unstructured (based on flooding or random walks) depending on the overlay network topology. Examples of peer-to-peer systems are BitTorrent, Gnutella, and Skype.
  - Distributed object architecture: A model where objects are distributed across the network and communicate using remote method invocation (RMI) or remote procedure call (RPC) protocols. Distributed objects can be transparently accessed and manipulated by clients as if they were local objects. Examples of distributed object architectures are Java RMI, .NET Remoting, and DCOM.
  - Distributed component architecture: A model where components are distributed across the network and communicate using event-based or message-based protocols. Components can be dynamically deployed, configured, and composed into applications. Examples of distributed component architectures are Enterprise JavaBeans (EJB), COM+, and CORBA Component Model (CCM).

- A diagram showing the different architectural models for distributed systems is given below:

```
+---------------------+    +---------------------+    +---------------------+
|                     |    |                     |    |                     |
|  Client-server      |    |    Broker           |    |  Service-oriented   |
|                     |    |                     |    |                     |
|  +------+  +------+ |    |  +------+  +------+ |    |  +------+  +------+ |
|  |Client|  |Server| |    |  |Client|  |Server| |    |  |Client|  |Server| |
|  +------+  +------+ |    |  +------+  +------+ |    |  +------+  +------+ |
|     |         |     |    |     |         |     |    |     |         |     |
|     +----+----+     |    |     +----+----+     |    |     +----+----+     |
|          |          |    |          |          |    |          |          |
+----------|----------+    +----------|----------+    +----------|----------+
           |                       |                       |
           |                       |                       |
           |                       |                       |
           |                       |                       |
           |                       |                       |
           |                       |                       |
           |                       |                       |
           |                       |                       |
           |                       |                       |
           |                       |                       |
           |                       |                       |
           |                       |                       |
           |                       |                       |
           |                       |                       |
           |                       |                       |
+----------|----------+    +----------|----------+    +----------|----------+
|          |          |    |          |          |    |          |          |
|     +----+----+     |    |     +----+----+     |    |     +----+----

```
