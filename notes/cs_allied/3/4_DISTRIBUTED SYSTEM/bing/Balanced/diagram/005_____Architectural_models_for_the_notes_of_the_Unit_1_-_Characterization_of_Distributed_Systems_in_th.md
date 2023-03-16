### Architectural models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Architectural models are types of system models that deal with the organization of components across the network and their interrelationship.
- Architectural models describe the placement of parts in a distributed system and the relationship between them.
- Architectural models can be classified into different styles, such as:
  - Client-server architecture: A style where one or more servers provide services to multiple clients that request them. Servers can be centralized or distributed, and clients can be thin or fat.
  - Broker architecture: A style where a broker component acts as an intermediary between clients and servers, hiding the details of communication and location from them. Examples of broker architectures are CORBA, Java RMI, and DCOM.
  - Service-oriented architecture: A style where services are loosely coupled and communicate through standardized protocols and interfaces. Services can be composed, orchestrated, and discovered dynamically. Examples of service-oriented architectures are SOAP, REST, and microservices .
  - Peer-to-peer architecture: A style where nodes in the network act as both clients and servers, sharing resources and collaborating without a central authority. Examples of peer-to-peer architectures are BitTorrent, Napster, and Gnutella.
  - Layered architecture: A style where components are organized in layers, each layer communicating with its adjacent layer by sending requests and getting responses. Layers can be hierarchical or horizontal, and can be distributed or replicated. Examples of layered architectures are TCP/IP, OSI, and MVC.
- Architectural models can have different properties and trade-offs, such as:
  - Scalability: The ability of the system to handle increased workload or number of users without degrading performance or quality of service.
  - Availability: The degree to which the system is operational and accessible to users at any given time.
  - Reliability: The probability that the system will perform its intended function correctly and without failure.
  - Fault-tolerance: The ability of the system to continue functioning in the presence of faults or errors, such as hardware failures, network partitions, or malicious attacks.
  - Consistency: The degree to which the system maintains a coherent and agreed-upon state of data and operations across all components.
  - Transparency: The extent to which the system hides the details of its distribution and heterogeneity from users and applications, such as location, replication, concurrency, and failure transparency.
  - Security: The protection of the system and its data from unauthorized access, modification, or disclosure, such as confidentiality, integrity, and authentication.