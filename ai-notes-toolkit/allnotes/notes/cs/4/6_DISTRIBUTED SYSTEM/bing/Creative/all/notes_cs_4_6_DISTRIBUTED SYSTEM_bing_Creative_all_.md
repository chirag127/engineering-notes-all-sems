

## Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- The main characteristics of distributed systems are:
  - Concurrency: Multiple components can operate in parallel and interact with each other.
  - No global clock: There is no shared physical clock among the components, so synchronization and coordination are challenging.
  - Independent failures: Each component can fail independently without affecting the whole system, so fault tolerance and recovery are essential.
  - Heterogeneity: The components can have different hardware, software, network, data, and protocols, so interoperability and compatibility are required.
- The main advantages of distributed systems are:
  - Scalability: The system can grow in size and performance by adding more components without affecting the existing ones.
  - Availability: The system can tolerate failures of some components and still provide services to the users.
  - Transparency: The system can hide the complexity and diversity of its components and provide a uniform interface to the users.
  - Resource sharing: The system can allow the components to access and utilize the resources of other components, such as files, printers, sensors, etc.
- The main challenges of distributed systems are:
  - Communication: The system has to ensure reliable, efficient, and secure data exchange among the components over the network.
  - Coordination: The system has to manage the concurrent activities and interactions of the components and ensure consistency and correctness of the system state.
  - Security: The system has to protect the data and resources of the components from unauthorized access, modification, or disclosure.
  - Quality of service: The system has to provide acceptable levels of performance, reliability, availability, and usability to the users.



# Introduction for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- A distributed system has the following characteristics:
  - Concurrency: The components of a distributed system can execute concurrently, without having to wait for each other.
  - No global clock: There is no global notion of time in a distributed system, and the components may have different local clocks that are not synchronized.
  - Independent failures: The components of a distributed system may fail independently, without affecting the whole system.
  - Heterogeneity: The components of a distributed system may have different hardware, software, network, and data formats.
  - Scalability: A distributed system should be able to accommodate an increasing number of components and users, without degrading the performance or functionality of the system.
  - Transparency: A distributed system should hide the complexity and diversity of its components from the users, and provide a uniform and consistent interface to access the system.
- A distributed system can be classified into different types based on the degree of coupling among the components, such as:
  - Client-server systems: A client-server system consists of a set of servers that provide services to a set of clients. The clients and servers communicate through a network using a request-reply protocol. The servers are usually centralized and have a fixed location, while the clients are distributed and mobile.
  - Peer-to-peer systems: A peer-to-peer system consists of a set of peers that act as both clients and servers. The peers communicate through a network using a message-passing protocol. The peers are usually decentralized and have no fixed location, and they can join and leave the system dynamically.
  - Distributed object systems: A distributed object system consists of a set of objects that encapsulate data and behavior. The objects communicate through a network using a remote method invocation protocol. The objects are usually distributed and heterogeneous, and they can be replicated and migrated across the system.
  - Distributed file systems: A distributed file system consists of a set of files that are stored and accessed by a set of processes. The files communicate through a network using a file access protocol. The files are usually distributed and replicated, and they provide a consistent and transparent view of the file system to the processes.
  - Distributed database systems: A distributed database system consists of a set of databases that are stored and manipulated by a set of transactions. The databases communicate through a network using a database access protocol. The databases are usually distributed and replicated, and they provide a consistent and transparent view of the data to the transactions.



# Examples of Distributed Systems

A distributed system is a collection of independent computers that communicate and coordinate their actions by passing messages. The computers in a distributed system may be physically close or geographically dispersed, and they may be connected by a network or a bus. Distributed systems enable applications to achieve high performance, scalability, fault tolerance, and availability.

Some examples of distributed systems are:

- **Telecommunication networks**: Telephone networks are an early example of a peer-to-peer network, where each node can initiate or receive calls. Cellular and telephone networks are forms and examples of distributed networks. They use protocols such as TCP/IP, UDP, and SIP to exchange data and signals. Telecommunication networks also include the Internet, which is a global network of networks that connects millions of computers and devices. The Internet uses protocols such as HTTP, FTP, SMTP, and DNS to provide various services and applications.  

- **Real-time systems**: Many industries use real-time systems distributed in various areas, locally and globally. Real-time systems are systems that have strict timing constraints and must respond to events within a specified deadline. For example, air traffic control systems, industrial control systems, and autonomous vehicles are real-time systems that rely on distributed sensors, actuators, and controllers to monitor and control the environment. Real-time systems use protocols such as CAN, RTSP, and RTP to ensure timely and reliable communication.  

- **Distributed database systems**: A distributed database is a database that has locations across multiple servers, physical locations, or both. A distributed database system is a system that manages a distributed database and provides access, concurrency, and consistency mechanisms. For example, Google's Bigtable, Amazon's Dynamo, and Facebook's Cassandra are distributed database systems that store and process large amounts of data across many nodes. Distributed database systems use protocols such as SQL, NoSQL, and MapReduce to query and manipulate data.  

- **Distributed computing systems**: A distributed computing system is a system that uses multiple computers to perform a computation or a task that is too complex or resource-intensive for a single computer. For example, SETI@home, Folding@home, and Bitcoin are distributed computing systems that use the idle cycles of volunteers' computers to search for extraterrestrial intelligence, simulate protein folding, and generate digital currency, respectively. Distributed computing systems use protocols such as MPI, P2P, and Blockchain to coordinate and synchronize the computation.  

- **Distributed gaming systems**: A distributed gaming system is a system that enables multiple players to interact and play a game in a virtual world. For example, World of Warcraft, Fortnite, and Minecraft are distributed gaming systems that support millions of players online. Distributed gaming systems use protocols such as TCP, UDP, and RMI to exchange game state, events, and commands. Distributed gaming systems also use techniques such as replication, consistency, and load balancing to ensure a smooth and fair gaming experience.



# Resource sharing for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Resource sharing is one of the main goals and benefits of distributed systems.
- Resource sharing means that the users and applications can access and use the resources (such as data, files, devices, services, etc.) that are available in a distributed system, regardless of their physical location, ownership, or access policy.
- Resource sharing can improve the performance, reliability, scalability, and availability of distributed systems, as well as reduce the cost and complexity of managing them.
- Resource sharing can be achieved by different methods, such as:
  - File sharing: the users and applications can access and manipulate files that are stored on remote servers or peers, using protocols such as NFS, SMB, FTP, HTTP, etc.
  - Data sharing: the users and applications can access and query databases or data warehouses that are distributed across multiple nodes, using protocols such as SQL, ODBC, JDBC, etc.
  - Device sharing: the users and applications can access and use devices (such as printers, scanners, cameras, etc.) that are connected to remote nodes, using protocols such as IPP, SANE, etc.
  - Service sharing: the users and applications can access and invoke services (such as web services, cloud services, microservices, etc.) that are provided by remote nodes, using protocols such as SOAP, REST, RPC, etc.
- Resource sharing can be classified into two types, depending on the degree of transparency and coordination among the nodes that share the resources:
  - Unstructured resource sharing: the nodes that share the resources do not have any global knowledge or agreement about the availability, location, or state of the resources, and rely on mechanisms such as discovery, advertisement, or negotiation to find and access the resources. Examples of unstructured resource sharing are peer-to-peer systems, service-oriented systems, etc.
  - Structured resource sharing: the nodes that share the resources have some global knowledge or agreement about the availability, location, or state of the resources, and rely on mechanisms such as replication, caching, or consistency to access and update the resources. Examples of structured resource sharing are distributed file systems, distributed databases, etc.



# The Web Challenges for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- The web is an example of a distributed system that allows resource sharing and communication among different devices across the internet.
- However, the web also poses several challenges for the design and implementation of distributed systems, such as   :

  - Scalability: The ability to handle increasing load and demand without degrading the performance or functionality of the system. This requires efficient algorithms, protocols, and architectures that can cope with large numbers of users, requests, and data.
  - Heterogeneity: The diversity of devices, platforms, languages, and formats that are involved in the web. This requires interoperability, standardization, and adaptation mechanisms that can ensure compatibility and usability across different systems.
  - Security: The protection of the system and its resources from unauthorized access, modification, or damage. This requires authentication, authorization, encryption, and auditing techniques that can prevent or detect attacks and ensure privacy and availability.
  - Fault tolerance: The ability to cope with failures and errors that may occur in the system or its components. This requires redundancy, replication, recovery, and consensus methods that can ensure reliability and consistency of the system.
  - Transparency: The hiding of the complexity and diversity of the system from the users and applications. This requires abstraction, naming, caching, and location services that can provide a simple and uniform view of the system.



# Architectural models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Architectural models are a type of system model that describe the organization of components across the network and their interrelationship .
- Architectural models can help to design, analyze, and implement distributed systems by providing a high-level view of the system structure and behavior.
- Architectural models can also help to identify the challenges and trade-offs involved in distributed systems, such as scalability, reliability, security, and performance.
- Some common architectural models for distributed systems are:

  - **Client-server architecture**: This model consists of two types of components: clients and servers. Clients request services from servers, and servers provide services to clients. Clients and servers can be located on different machines and communicate over the network. This model is widely used for web applications, email systems, database systems, etc. 
  - **Multi-tier architecture**: This model is an extension of the client-server architecture, where the server is divided into multiple tiers or layers, each providing a specific functionality. For example, a three-tier architecture may consist of a presentation tier (user interface), a business logic tier (application logic), and a data tier (database). This model can improve the modularity, scalability, and security of the system by separating the concerns of different tiers. 
  - **Broker architecture**: This model introduces a third type of component: brokers. Brokers act as intermediaries between clients and servers, and provide services such as location transparency, load balancing, fault tolerance, and security. Brokers can also implement a common interface or protocol for communication, such as CORBA, RMI, or SOAP. This model can simplify the development and integration of heterogeneous and distributed components. 
  - **Service-oriented architecture (SOA)**: This model treats the system as a collection of loosely coupled and interoperable services, each providing a specific functionality. Services can be discovered, composed, and invoked dynamically by other services or clients, using standard protocols such as HTTP, XML, and WSDL. This model can enhance the reusability, flexibility, and adaptability of the system by enabling service-oriented computing. 
  - **Peer-to-peer architecture**: This model eliminates the distinction between clients and servers, and allows every component to act as both a service provider and a service consumer. Components can communicate directly with each other, without relying on a central authority or broker. This model can increase the scalability, robustness, and autonomy of the system by enabling distributed and decentralized computing. Examples of peer-to-peer systems are BitTorrent, Skype, and Bitcoin. 
  - **Layered architecture**: This model organizes the components in layers, each providing a specific functionality. Each layer communicates with its adjacent layer by sending requests and getting responses. This model can improve the modularity, abstraction, and portability of the system by separating the concerns of different layers. Examples of layered systems are TCP/IP, OSI, and JEE.



# Fundamental Models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

Fundamental models are abstract descriptions of the properties and behaviors that are common to all distributed systems. They help us to understand the challenges and trade-offs involved in designing and implementing distributed systems. There are three main types of fundamental models: architectural, interaction, and failure models.

## Architectural Models
Architectural models describe the structure and organization of the components of a distributed system and their relationships. They also define the roles and responsibilities of each component and the assumptions and guarantees they make. Some examples of architectural models are:

- **Client-server model**: A client-server model consists of two types of components: clients and servers. Clients request services from servers, and servers provide services to clients. Servers are usually passive and wait for client requests, while clients are active and initiate communication. Servers may be stateful or stateless, depending on whether they maintain information about the clients or not. Clients and servers may communicate using different protocols, such as HTTP, FTP, or RPC .
- **Peer-to-peer model**: A peer-to-peer model consists of a set of peers that are both clients and servers. Peers can request and provide services to each other, without relying on a central authority or coordinator. Peers are usually autonomous and self-organizing, and may join or leave the system at any time. Peers may communicate using different protocols, such as Gnutella, BitTorrent, or Chord .
- **Publish-subscribe model**: A publish-subscribe model consists of a set of publishers and subscribers that communicate through a broker or a middleware. Publishers produce events or messages and publish them to the broker, and subscribers express their interest in certain types of events or messages and subscribe to the broker. The broker is responsible for filtering and delivering the events or messages to the appropriate subscribers, without revealing the identities of the publishers or subscribers. Publishers and subscribers may communicate using different protocols, such as MQTT, AMQP, or JMS .

## Interaction Models
Interaction models describe the patterns and mechanisms of communication and coordination among the components of a distributed system. They also define the properties and guarantees of the communication and coordination, such as performance, ordering, reliability, and consistency. Some examples of interaction models are:

- **Synchronous model**: A synchronous model assumes that there are known bounds on the processing time, communication delay, and clock drift of the components of a distributed system. This allows the components to coordinate their actions and agree on a common notion of time. A synchronous model simplifies the design and implementation of distributed algorithms, such as consensus, leader election, and mutual exclusion. However, a synchronous model is often unrealistic and impractical, as it does not account for the variability and unpredictability of the real world .
- **Asynchronous model**: An asynchronous model assumes that there are no known bounds on the processing time, communication delay, and clock drift of the components of a distributed system. This means that the components cannot coordinate their actions or agree on a common notion of time. An asynchronous model is more realistic and practical, as it reflects the nature of the real world. However, an asynchronous model complicates the design and implementation of distributed algorithms, as it requires the components to cope with uncertainty and inconsistency .
- **Hybrid model**: A hybrid model combines the features of both synchronous and asynchronous models. A hybrid model assumes that there are some bounds on the processing time, communication delay, and clock drift of the components of a distributed system, but they are not known or fixed. A hybrid model tries to balance the trade-offs between simplicity and realism, and between performance and reliability. A hybrid model may use different techniques, such as timeouts, retries, acknowledgments, and clocks, to achieve the desired level of synchronization and coordination among the components .

## Failure Models
Failure models describe the types and causes of faults that can occur in the components of a distributed system and their effects on the system. They also define the strategies and techniques to detect, tolerate, and recover from the faults. Some examples of failure models are:

- **Crash failure model**: A crash failure model assumes that a component of a distributed system can fail by stopping its execution and not resuming it. A crash failure model is the simplest and most common type of failure model, as it covers the cases of power outage, hardware malfunction, software bug,



# Theoretical Foundation for Distributed System

A distributed system is a collection of processes that are spatially separated and do not share a common memory and communicate with one another by exchanging messages with arbitrary delays .

Some of the theoretical foundations for distributed system are:

- **Limitations of distributed system**: Due to the lack of a global clock, shared memory, and reliable communication, distributed systems face challenges such as synchronization, consistency, fault tolerance, and security.
- **Logical clocks**: Logical clocks are a way of ordering events in a distributed system without relying on physical clocks. They assign logical timestamps to events such that causally related events have consistent timestamps. There are different types of logical clocks, such as Lamport's clocks and vector clocks, that have different properties and trade-offs .
- **Concepts in message passing system**: Message passing is the basic communication mechanism in a distributed system. It involves sending and receiving messages between processes. Some of the concepts in message passing system are: message types, message ordering, message delivery, message buffering, message encoding, and message security.
- **Coordination algorithms**: Coordination algorithms are fundamental in distributed systems to achieve agreement and consistency among processes. They are used for tasks such as leader election, resource allocation, mutual exclusion, consensus, and atomic commit.
- **Distributed information systems**: Distributed information systems are systems that store, process, and disseminate information across a network of nodes. They aim to provide efficient, reliable, and scalable access to data and services. Some of the topics in distributed information systems are: distributed databases, distributed file systems, distributed web services, distributed search engines, and distributed machine learning.



# Limitation of Distributed System

A distributed system is a system that consists of multiple independent components that communicate with each other over a network. Distributed systems have many advantages, such as scalability, fault-tolerance, availability, and performance. However, they also face some limitations that make them challenging to design and implement. Some of the main limitations of distributed systems are:

- **Absence of a global state**: In a distributed system, there is no single point of control or coordination for the entire system. Each component has its own local state and view of the system, which may differ from the views of other components. This makes it difficult to reason about the behavior and correctness of the system, especially in the presence of concurrency, failures, and network delays. To cope with this limitation, distributed systems need to use techniques such as consensus algorithms, distributed transactions, and replication protocols to achieve some form of consistency and agreement among the components.

- **Absence of a global clock**: In a distributed system, there is no common notion of time or ordering of events across the components. Each component has its own local clock, which may not be synchronized with the clocks of other components. This makes it hard to measure and compare the durations and sequences of events in the system, and to coordinate the actions of the components. To deal with this limitation, distributed systems need to use methods such as logical clocks, vector clocks, and Lamport timestamps to establish some form of causal or total ordering of events.

- **Absence of shared memory**: In a distributed system, there is no shared memory or storage that can be accessed by all the components. Each component has its own local memory or storage, which may not be visible or accessible to other components. This makes it challenging to share and exchange data and information among the components, and to maintain the consistency and integrity of the data. To overcome this limitation, distributed systems need to use mechanisms such as message passing, remote procedure calls, distributed file systems, and distributed databases to enable data communication and synchronization among the components.

- **Heterogeneity**: In a distributed system, the components may have different hardware, software, operating systems, programming languages, data formats, and protocols. This makes it complex to ensure the interoperability and compatibility of the components, and to handle the diversity and variability of the system. To address this limitation, distributed systems need to use standards such as TCP/IP, HTTP, JSON, and REST to enable the communication and integration of the components.

- **Security**: In a distributed system, the components are exposed to various threats and attacks from malicious entities, such as hackers, viruses, worms, and denial-of-service attacks. These attacks may compromise the confidentiality, integrity, and availability of the system and its data. This makes it essential to protect the system and its components from unauthorized access, modification, and disruption. To mitigate this limitation, distributed systems need to use techniques such as encryption, authentication, authorization, and firewall to secure the system and its communication.

- **Complexity**: In a distributed system, the components are distributed across different locations, networks, and domains, and may have different behaviors, states, and views of the system. This makes it complicated to design, implement, test, debug, and maintain the system and its components, and to handle the various issues and challenges that may arise in the system, such as concurrency, failures, delays, inconsistencies, and conflicts. To reduce this limitation, distributed systems need to use principles such as modularity, abstraction, encapsulation, and transparency to simplify the system and its components.



# Absence of Global Clock

- A global clock is a system-wide clock that is equally accessible to all processes in a distributed system and provides a common notion of time.
- A global clock is useful for determining the order of events and the state of the system across different processes.
- However, a global clock is hard to realize in distributed systems due to two inherent limitations: lack of shared memory and unpredictable message delays.
- Lack of shared memory means that processes in a distributed system do not have access to a common storage that can store and update the global clock value.
- Unpredictable message delays mean that the communication channel between processes is unreliable and the transmission time of messages is variable and unknown.
- Therefore, the absence of a global clock implies that:
  - Different processes may have different local clocks that are not synchronized and may drift apart over time.
  - It is not always possible to determine the exact order of events that occur on different processes, especially if they are concurrent or causally unrelated.
  - It is not possible for an individual process to obtain an up-to-date and consistent state of the entire system, as the state may change during the transmission of messages.
  - It is difficult to obtain a meaningful global state of the system, in which the states of different processes are consistent with each other and reflect a common point in time.



# Shared Memory

Shared memory is a programming model for distributed systems, where multiple processes can access and modify the same data in a shared address space. Shared memory can be implemented in different ways, such as:

- **Hardware-based**: using special hardware devices, such as cache coherence circuits or network interface controllers, to maintain consistency and coherence of the shared data across different nodes.
- **Software-based**: using software mechanisms, such as virtual memory or message passing, to emulate the shared memory abstraction on top of a physically distributed memory system.

## Advantages of Shared Memory

Some of the advantages of using shared memory in distributed systems are:

- **Ease of programming**: shared memory provides a familiar and natural programming model for developers, who can use the same techniques and tools as in uniprocessor systems. Shared memory also hides the details of data distribution and communication from the programmers, making the code more portable and scalable.
- **Performance**: shared memory can reduce the communication overhead and latency in distributed systems, by allowing direct and fast access to the shared data. Shared memory can also exploit the locality and caching of the data, improving the throughput and efficiency of the system.
- **Flexibility**: shared memory can support different types of applications and data structures, such as parallel algorithms, databases, or graphs. Shared memory can also be combined with other programming models, such as message passing or remote procedure calls, to achieve the best of both worlds.

## Challenges of Shared Memory

Some of the challenges of implementing and using shared memory in distributed systems are:

- **Consistency**: shared memory requires maintaining a consistent view of the shared data across different nodes, which can be difficult and costly in the presence of concurrency, failures, or network delays. Different consistency models, such as sequential, causal, or eventual, can be used to trade off between performance and correctness.
- **Coherence**: shared memory requires ensuring that the cached copies of the shared data are coherent with the original data, which can involve invalidating, updating, or migrating the data across different nodes. Different coherence protocols, such as write-invalidate, write-update, or write-broadcast, can be used to trade off between bandwidth and latency.
- **Synchronization**: shared memory requires coordinating the access and modification of the shared data by different processes, which can involve using locks, semaphores, or atomic operations. Different synchronization techniques, such as mutual exclusion, conditional synchronization, or optimistic concurrency control, can be used to trade off between deadlock and livelock.



# Logical Clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A logical clock is a mechanism for capturing chronological and causal relationships in a distributed system  .
- A distributed system may have no physically synchronous global clock, so a logical clock allows global ordering on events from different processes in such systems  .
- A logical clock is not a physical device, but a protocol that assigns logical timestamps to events based on some rules .
- A logical clock can be implemented using different algorithms, such as Lamport's clocks, vector clocks, or matrix clocks  .
- A logical clock must satisfy the following property: if event a causally precedes event b, then the logical timestamp of a is less than the logical timestamp of b  .
- A logical clock can provide a total order or a partial order on events, depending on the algorithm used  .
- A logical clock can help in solving problems such as mutual exclusion, deadlock detection, distributed snapshots, and distributed debugging in a distributed system  .



# Lamport's Logical Clocks

- Lamport's logical clocks are a way of ordering events in a distributed system without relying on physical clocks.
- Lamport's logical clocks are based on the idea of a **happens-before** relation, denoted by `->`, which captures the causal order of events.
- If `a` and `b` are events on the same process, then `a -> b` if `a` occurs before `b` based on the local clock.
- If `a` is the event of sending a message by one process and `b` is the event of receiving that message by another process, then `a -> b`.
- If `a -> b` and `b -> c`, then `a -> c`.
- Two events `a` and `b` are **concurrent**, denoted by `a || b`, if neither `a -> b` nor `b -> a`.
- Lamport's logical clocks assign a numerical value, called a **timestamp**, to each event that is consistent with the happens-before relation.
- A timestamp is a positive integer that represents the logical time of an event.
- Each process maintains a local logical clock, which is a counter that is incremented before each event on that process.
- When a process sends a message, it attaches its current logical clock value to the message.
- When a process receives a message, it updates its logical clock to be the maximum of its own clock and the timestamp in the message, and then increments it by one.
- Lamport's logical clocks ensure that if `a -> b`, then the timestamp of `a` is less than the timestamp of `b`.
- However, the converse is not true: if the timestamp of `a` is less than the timestamp of `b`, it does not imply that `a -> b`.
- Therefore, Lamport's logical clocks can only partially order events, and cannot distinguish between concurrent events.
- Lamport's logical clocks are also known as **scalar clocks** or **single-value clocks**, because they use only one integer to represent the logical time of an event.



# Concepts in Message Passing Systems

- Message passing is a technique for invoking behavior on a computer by sending a message to a process.
- Message passing is used in distributed systems to enable communication and coordination among processes that may be located on different machines .
- Message passing systems provide a set of message-based interprocess communication (IPC) protocols that allow processes to exchange data, synchronize, and request services .
- Message passing systems can be classified into two categories: synchronous and asynchronous .
  - Synchronous message passing systems require the sender and the receiver to be ready at the same time for a message exchange. The sender blocks until the receiver acknowledges the message, and the receiver blocks until a message arrives .
  - Asynchronous message passing systems do not impose any timing constraints on the sender and the receiver. The sender can send a message and continue without waiting for an acknowledgment, and the receiver can receive a message at any time from a message queue .
- Message passing systems can also be classified into two types: direct and indirect .
  - Direct message passing systems require the sender and the receiver to explicitly name each other in the message exchange. A communication link must be established between the cooperating processes before messages can be sent .
  - Indirect message passing systems do not require the sender and the receiver to know each other's identities. Instead, they use an intermediary entity, such as a mailbox, a port, or a topic, to route messages between processes .
- Message passing systems can support various communication models, such as point-to-point, multicast, broadcast, and publish-subscribe .
  - Point-to-point communication model involves sending a message from one process to another process. It can be either one-to-one or one-to-many .
  - Multicast communication model involves sending a message from one process to a subset of processes. It can be either many-to-one or many-to-many .
  - Broadcast communication model involves sending a message from one process to all processes. It can be either one-to-all or all-to-all .
  - Publish-subscribe communication model involves sending a message from one process to a set of processes that have subscribed to a certain topic. It can be either one-to-many or many-to-many .
- Message passing systems can have different properties, such as reliability, ordering, and atomicity .
  - Reliability refers to the guarantee that a message sent by a process will be delivered to the intended recipient(s) without being lost, duplicated, or corrupted .
  - Ordering refers to the guarantee that messages sent by a process will be delivered to the recipient(s) in the same order as they were sent .
  - Atomicity refers to the guarantee that messages sent by a process will be delivered to all or none of the recipient(s) .
- Message passing systems can use different protocols, such as TCP, UDP, HTTP, and MPI  .
  - TCP (Transmission Control Protocol) is a reliable, ordered, and connection-oriented protocol that provides error detection and correction, flow control, and congestion control.
  - UDP (User Datagram Protocol) is an unreliable, unordered, and connectionless protocol that provides low latency and high throughput, but does not guarantee delivery, order, or integrity of messages.
  - HTTP (Hypertext Transfer Protocol) is an application-level protocol that supports request-response communication between clients and servers over TCP.
  - MPI (Message Passing Interface) is a standardized and portable message-passing system developed for distributed and parallel computing. MPI provides parallel hardware vendors with a clearly defined base set of routines that can be efficiently implemented .



# Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent and autonomous processes that communicate by exchanging messages over a network.
- The processes in a distributed system may have different views of the system state and the order of events, due to network delays, failures, or concurrency.
- Causal order is a partial order relation that captures the potential causal dependencies between events in a distributed system.
- Causal order is defined as follows: an event e1 is causally before an event e2 (denoted as e1 -> e2) if and only if one of the following conditions holds:
  - e1 and e2 are events in the same process, and e1 occurred before e2 in that process.
  - e1 is the sending of a message m, and e2 is the receipt of that message m.
  - There exists some event e3 such that e1 -> e3 and e3 -> e2 (transitivity).
- Causal order is important for ensuring the consistency and correctness of distributed applications, such as replicated data stores, collaborative editing, or distributed algorithms.
- Causal order can be implemented by various mechanisms, such as vector clocks, logical clocks, or message ordering protocols.
- Causal order can be classified into different levels of strictness, depending on how much concurrency is allowed between causally independent events:
  - Total-causal order is the strictest ordering in distributed systems; it establishes only one linearization, consistent with the causal ordering, among all the events that occur in the system, even those that occur concurrently. For that reason, the execution of the system is considered as synchronous .
  - Causal order is a weaker ordering than total-causal order; it allows different linearizations of concurrent events, as long as they respect the causal dependencies. For that reason, the execution of the system is considered as asynchronous .
  - Fuzzy causal order is a weaker ordering than causal order; it allows some violations of causal dependencies, as long as they are within a certain tolerance. For that reason, the execution of the system is considered as partially synchronous .
- Causal order is a trade-off between performance and consistency; the stricter the ordering, the more overhead and coordination is required, but the more predictable and reliable the system behavior is. The weaker the ordering, the more concurrency and scalability is possible, but the more anomalies and conflicts may arise.



# Total Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent entities that communicate by message passing and coordinate their actions to achieve a common goal.
- A distributed system can be characterized by various properties, such as scalability, reliability, availability, fault tolerance, consistency, transparency, etc.
- One of the challenges of distributed systems is to deal with the uncertainty and partial failure of the network and the processes.
- To reason about the behavior and correctness of distributed systems, we need to define some concepts of time and order among the events that occur in the system.
- An event is an occurrence that changes the state of a process or the system. Events can be local (internal to a process) or global (involving communication between processes).
- A physical clock is a device that measures the passage of time based on some physical phenomenon, such as the oscillation of a quartz crystal. Physical clocks are imperfect and may drift or skew from each other.
- A logical clock is an abstraction that assigns logical timestamps to events, such that the order of events is preserved. Logical clocks do not need to be synchronized with physical clocks, but they must be consistent with the causality of events.
- Causality is a relation that captures the potential influence of events on each other. If event a causes event b, then we say that a happens before b, denoted by a -> b. The happens before relation is transitive, irreflexive, and antisymmetric.
- A distributed system is said to have partial order if we can have a partial order relationship among the events in the system. If 'totality', i.e., causal relationship among all events in the system, can be established, then the system is said to have total order.
- A total order is a relation that is reflexive, antisymmetric, transitive, and total, meaning that for any two events a and b, either a -> b or b -> a or a = b.
- A total order can be useful for ensuring consistency and agreement among the processes in a distributed system, such as when implementing a replicated state machine or a distributed database.
- A total order can be achieved by using various algorithms, such as logical clocks, vector clocks, Lamport timestamps, or atomic broadcast   .
- A logical clock is a function C that maps each event to a natural number, such that if a -> b, then C(a) < C(b). A logical clock can be implemented by using a counter that is incremented by each process for each local event, and piggybacked on each message sent. The receiver of a message updates its counter to the maximum of its own counter and the received counter, plus one.
- A vector clock is a function V that maps each event to a vector of natural numbers, such that V(a)[i] is the logical time of process i when a occurred. A vector clock can be implemented by using a vector of counters that is maintained by each process, and piggybacked on each message sent. The receiver of a message updates its vector by taking the element-wise maximum of its own vector and the received vector.
- A Lamport timestamp is a special case of a logical clock that assigns a single number to each event, such that if a -> b, then L(a) < L(b), and if L(a) = L(b), then a and b are concurrent. A Lamport timestamp can be used to create a total ordering of events in a distributed system by using some arbitrary mechanism to break ties (e.g. the ID of the process).
- An atomic broadcast is a communication primitive that guarantees that a message sent by a process is delivered to all processes in the same order, and that no messages are lost or duplicated. An atomic broadcast can be used to implement a total order of events in a distributed system by assigning a sequence number to each message and delivering the messages in the order of their sequence numbers.



# Total Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems in the Subject of Distributed System

- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by passing messages.
- A distributed system may exhibit different types of ordering among the messages exchanged by the processes, depending on the application requirements and the system model.
- One of the ordering types is **total causal order**, which is the strictest ordering in distributed systems.
- Total causal order has the following properties  :
  - It establishes only one linearization, consistent with the causal ordering, among all the events that occur in the system, even those that occur concurrently.
  - It ensures that if any process delivers a message m1 before m2, then all processes will deliver m1 before m2.
  - It implies FIFO ordering, since any two multicasts by the same process are related by the happened-before relation.
  - It does not imply causal ordering, just says that all processes must agree on the same order of messages.
- Total causal order can be achieved by using different algorithms, such as vector clocks, logical clocks, or sequencer-based algorithms .
- Total causal order can be useful for providing fault tolerance, consistency, and synchronization for constructing reliable distributed systems.



# Techniques for Message Ordering in Distributed Systems

A distributed system is a collection of independent computers that communicate with each other via messages. The order in which messages are processed determines the final outcome of the actions in any distributed system. However, message ordering is not trivial, as messages may be delayed, lost, or reordered by the network. Therefore, different techniques are needed to ensure a consistent and correct message ordering in distributed systems.

Some of the common techniques for message ordering in distributed systems are:

- **Non-FIFO ordering**: This is the simplest and most basic technique, where messages are processed in the order they are received, regardless of the order they were sent. This technique does not guarantee any ordering property, and may lead to inconsistent or incorrect results. For example, if a process sends two messages m1 and m2 to another process, and m1 arrives later than m2, then the receiver may process m2 before m1, which may violate the sender's intention or the application logic.

- **FIFO ordering**: This technique ensures that messages sent by the same process are processed in the order they were sent. This technique requires each process to maintain a sequence number for each message it sends, and each receiver to keep track of the expected sequence number for each sender. When a message arrives, the receiver checks if its sequence number matches the expected one. If yes, the message is processed and the expected sequence number is incremented. If no, the message is buffered until the missing messages arrive. This technique guarantees that the order of messages sent by the same process is preserved, but does not guarantee any order among messages sent by different processes. For example, if two processes send messages m1 and m2 to a third process, and m1 is sent before m2, then the receiver may process m2 before m1, if m2 arrives earlier than m1.

- **Causal ordering**: This technique ensures that messages that are causally related are processed in the order they were sent. Two messages are causally related if one message is sent as a result of receiving or sending another message. For example, if a process sends a message m1 to another process, and then sends a message m2 to a third process, then m1 and m2 are causally related, as m2 is sent after m1. This technique requires each process to maintain a vector clock, which is an array of sequence numbers, one for each process in the system. When a process sends a message, it attaches its current vector clock to the message. When a process receives a message, it compares its vector clock with the one in the message. If the message's vector clock is less than or equal to the receiver's vector clock, then the message is processed and the receiver's vector clock is updated. If the message's vector clock is greater than the receiver's vector clock, then the message is buffered until the causal dependencies are satisfied. This technique guarantees that the order of causally related messages is preserved, but does not guarantee any order among messages that are not causally related. For example, if two processes send messages m1 and m2 to a third process, and m1 and m2 are not causally related, then the receiver may process m1 or m2 first, depending on their vector clocks.

- **Total ordering**: This technique ensures that all messages are processed in the same order by all processes in the system. This technique requires a global agreement among all processes on the order of messages, which can be achieved by using a centralized coordinator, a distributed consensus algorithm, or a logical clock. When a process wants to send a message, it requests an order from the coordinator or the consensus algorithm, or assigns a logical timestamp to the message. When a process receives a message, it waits until it receives all the messages with lower orders or timestamps, and then processes the message. This technique guarantees that the order of all messages is consistent and deterministic, but may incur a high overhead in terms of communication, synchronization, and latency. For example, if two processes send messages m1 and m2 to a third process, and m1 is assigned a lower order or timestamp than m2, then the receiver will process m1 before m2, regardless of their arrival times.



# Causal ordering of messages

- Causal ordering of messages is a partial ordering of messages in a distributed computing environment .
- It places a restriction on communication between processes by requiring that if the transmission of message mi to process pk necessarily preceded the transmission of message mj to the same process, then the delivery of these messages to that process must be ordered such that mi is delivered before mj.
- Causal ordering of messages is one of the four semantics of multicast communication, namely unordered, totally ordered, causal, and sync-ordered communication.
- Multicast communication methods vary according to the message’s reliability guarantee and ordering guarantee.
- Causal ordering of messages is useful for ensuring consistency and correctness of distributed applications that depend on the causal relationships between events.
- Causal ordering of messages can be implemented using various algorithms, such as vector clocks, logical clocks, or message acknowledgments  .
- Causal ordering of messages can be violated due to transmission delays, network congestion, or clock synchronization errors .
- Causal ordering of messages is not the same as FIFO ordering, which only guarantees that messages sent by the same process are delivered in the order they were sent.
- Causal ordering of messages is also not the same as synchronous ordering, which guarantees that all processes deliver the same messages in the same order.



# Global State for the Notes of the Unit 1 - Characterization of Distributed Systems

- A **distributed system** is a collection of independent processes that communicate through message passing to achieve a common goal.
- The **local state** of a process is the set of values of its variables and data structures at a given point in time.
- The **global state** of a distributed system is the union of the local states of all the processes and the channels .
- A **channel** is a communication link between two processes that can store messages in transit.
- A **global state** can be used to reason about the properties and behavior of a distributed system, such as deadlock detection, termination detection, checkpointing, debugging, etc.
- However, capturing a global state of a distributed system is challenging, because the processes are concurrent and asynchronous, and there is no global clock or shared memory.
- Therefore, a global state must be **consistent**, meaning that it reflects a possible execution of the distributed system, and does not contain any causal anomalies.
- A **causal anomaly** is a situation where a global state contains an effect of an event, but not the event itself, or vice versa.
- For example, a global state that shows a message being received by a process, but not being sent by another process, is inconsistent and causally anomalous.
- A **consistent cut** is a set of local states of the processes that form a consistent global state.
- A **cut** is a partition of the set of events of a distributed system into two subsets: past and future.
- A **consistent cut** satisfies the property that if an event is in the future of the cut, then all the events that causally precede it are also in the future of the cut.
- A **snapshot** is an algorithm that records a consistent cut of a distributed system.
- A **snapshot** can be initiated by any process, and requires each process to record its local state and the state of its incoming channels.
- A **snapshot** must ensure that no message is recorded twice or missed by the algorithm.
- A **snapshot** can be implemented using different techniques, such as markers, vector clocks, or logical clocks.
- A **marker** is a special message that is used to indicate the start and end of a snapshot.
- A **vector clock** is a data structure that maintains a logical timestamp for each process, and is updated whenever an event occurs or a message is sent or received.
- A **logical clock** is a function that assigns a logical timestamp to each event, such that the timestamps respect the causal order of the events.
- A **snapshot** can be used to determine various properties of a distributed system, such as:
  - Whether the system is in a **deadlock** state, meaning that no process can make any progress.
  - Whether the system has **terminated**, meaning that all the processes have completed their tasks.
  - What is the **minimum consistent recovery line**, meaning the earliest consistent cut that can be used to restore the system after a failure.
  - What is the **global predicate**, meaning a logical expression that evaluates to true or false based on the global state of the system.



# Termination Detection for Distributed Systems

Termination detection is a fundamental problem in distributed systems, where a set of processes cooperate to perform a computation. The problem is to determine when all the processes have finished their work and there are no more messages in transit between them. This is non-trivial because no process has complete knowledge of the global state, and global time does not exist.

There are different algorithms for termination detection, depending on the assumptions and properties of the distributed system. One of the most well-known algorithms is Huang's algorithm, proposed by Shing-Tsaan Huang in 1989.

Huang's algorithm is based on the concept of a process' state, which can be either active or idle. An active process may become idle at any time, but an idle process may only become active again upon receiving a computational message (a message that affects the computation). A process is also associated with a control message counter, which records the number of control messages (messages that are used for termination detection) sent and received by the process.

The algorithm works as follows:

- Initially, all processes are active and their control message counters are zero.
- Each process maintains a local variable called `diff`, which is the difference between the number of computational messages sent and received by the process. A process updates its `diff` value whenever it sends or receives a computational message.
- The algorithm uses a special process called the initiator, which initiates and coordinates the termination detection. The initiator can be any process in the system, and it is assumed to be known by all processes.
- The initiator periodically sends a control message called a probe to one of its neighbors. The probe contains the initiator's `diff` value and a sequence number, which is incremented by one for each probe sent.
- When a process receives a probe, it does the following:
  - If the process is idle and its `diff` value is zero, it forwards the probe to one of its neighbors, without changing the probe's contents.
  - If the process is idle and its `diff` value is not zero, it adds its `diff` value to the probe's `diff` value, resets its own `diff` value to zero, and forwards the probe to one of its neighbors.
  - If the process is active, it holds the probe until it becomes idle, and then performs one of the above actions.
- When the initiator receives a probe, it does the following:
  - If the probe's sequence number is smaller than the current sequence number, it discards the probe.
  - If the probe's sequence number is equal to the current sequence number, and the probe's `diff` value is zero, it declares termination.
  - If the probe's sequence number is equal to the current sequence number, and the probe's `diff` value is not zero, it adds the probe's `diff` value to its own `diff` value, and sends a new probe with the updated `diff` value and sequence number.

The algorithm guarantees that termination will be detected if and only if the following conditions hold:

- The underlying computation eventually terminates, i.e., all processes become idle and there are no more computational messages in transit.
- The initiator does not fail, and the communication channels are reliable and FIFO (first-in first-out).
- The initiator sends probes frequently enough, i.e., the time between two consecutive probes is smaller than the time it takes for a probe to traverse the entire system.

The algorithm has some advantages and disadvantages:

- The algorithm is simple and easy to implement, and does not require any additional communication channels or global synchronization.
- The algorithm is efficient in terms of message complexity, as it only uses one control message per process per probe cycle, and the probe size is constant.
- The algorithm is adaptive, as it adjusts the probe's `diff` value according to the current state of the system, and avoids unnecessary probes when the system is stable.
- The algorithm is sensitive to the choice of the initiator and the neighbor selection, as they affect the probe's path and the termination detection time.
- The algorithm is not fault-tolerant, as it relies on the initiator's correctness and the channel's reliability. If the initiator fails or a probe is lost, the algorithm may fail to detect termination or falsely declare termination.



# Unit 2 - Distributed Mutual Exclusion

- Distributed mutual exclusion is a fundamental problem in distributed computing systems  .
- It ensures that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner  .
- It states that only one process is allowed to execute the critical section (CS) at any given time  .
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion . Message passing is the sole means for implementing distributed mutual exclusion.
- There are three basic approaches for implementing distributed mutual exclusion:
  - Token-based algorithms: A unique token is circulated among the processes in the system. Only the process that holds the token can enter the CS.
  - Permission-based algorithms: A process that wants to enter the CS must request permission from other processes in the system. Only if it receives permission from all or a majority of them, it can enter the CS.
  - Quorum-based algorithms: A process that wants to enter the CS must request permission from a subset of processes in the system, called a quorum. Only if it receives permission from all the processes in the quorum, it can enter the CS.
- The performance of distributed mutual exclusion algorithms can be measured by the following criteria :
  - Message complexity: The number of messages exchanged per CS execution .
  - Synchronization delay: The time elapsed between the instant a process requests to enter the CS and the instant it is allowed to do so .
  - System throughput: The rate at which the processes execute the CS .
  - Fault tolerance: The ability of the algorithm to handle failures of processes or communication links .
- Some examples of distributed mutual exclusion algorithms are:
  - Ricart-Agrawala algorithm: A permission-based algorithm that uses a logical clock to order the requests and a total ordering multicast to send the requests and replies .
  - Suzuki-Kasami algorithm: A token-based algorithm that uses a vector of sequence numbers to keep track of the requests and a broadcast to send the token .
  - Maekawa algorithm: A quorum-based algorithm that uses a voting set of processes to grant permission and a request queue to handle conflicts .



# Classification of distributed mutual exclusion

Distributed mutual exclusion is a problem of ensuring that only one process can access a shared resource or data at a time in a distributed system. It is a fundamental requirement for achieving consistency, coordination and synchronization among the processes in a distributed system.

There are three basic approaches for implementing distributed mutual exclusion:

- Token-based approach
- Non-token-based approach
- Quorum-based approach

## Token-based approach

In this approach, a unique token is shared among the sites or processes in the system. A site or process is allowed to enter its critical section (CS) if it possesses the token. Mutual exclusion is ensured because the token is unique and only one site or process can have it at a time. The token is passed from one site or process to another according to some predefined order or algorithm. Some examples of token-based algorithms are:

- Suzuki-Kasami algorithm
- Raymond's algorithm
- Singhal's heuristic algorithm

## Non-token-based approach

In this approach, there is no token in the system. Instead, a site or process requests permission from other sites or processes to enter its CS. The other sites or processes reply with either a grant or a deny message. A site or process can enter its CS only if it receives grant messages from all or a majority of the other sites or processes. Mutual exclusion is ensured by the agreement or voting among the sites or processes. Some examples of non-token-based algorithms are:

- Ricart-Agrawala algorithm
- Lamport's algorithm
- Maekawa's algorithm

## Quorum-based approach

In this approach, a site or process requests permission from a subset of sites or processes, called a quorum, to enter its CS. The quorum is chosen such that any two quorums have at least one site or process in common. A site or process can enter its CS only if it receives grant messages from all the sites or processes in its quorum. Mutual exclusion is ensured by the intersection property of the quorums. Some examples of quorum-based algorithms are:

- Sankararaman's algorithm
- Naimi-Trehel's algorithm
- Agrawal-El Abbadi's algorithm



# Requirement of mutual exclusion theorem for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM

- Mutual exclusion is a concurrency control property which is introduced to prevent race conditions.
- Race conditions occur when multiple processes access a shared resource or data concurrently and the outcome depends on the order of execution.
- Mutual exclusion ensures that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner .
- Mutual exclusion in a distributed system states that only one process is allowed to execute the critical section (CS) at any given time .
- A critical section (CS) is a piece of code that accesses a shared resource or data .
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion .
- Message passing is the sole means for implementing distributed mutual exclusion .
- There are three basic approaches for implementing distributed mutual exclusion:
  - Token-based algorithms: A process can enter the CS only if it possesses a unique token that is passed among the processes in a logical ring or a tree.
  - Permission-based algorithms: A process can enter the CS only if it receives permission messages from all or a subset of the other processes in the system.
  - Quorum-based algorithms: A process can enter the CS only if it receives permission messages from a majority or a weighted majority of the processes in the system.
- The requirement of mutual exclusion theorem is to ensure the correctness and consistency of the distributed system and to avoid conflicts and inconsistencies among the processes .
- The mutual exclusion theorem also imposes some performance criteria for the distributed mutual exclusion algorithms, such as fairness, bounded delay, message complexity, and synchronization delay .



# Token based and non token based algorithms for distributed mutual exclusion

Distributed mutual exclusion (DME) is the problem of ensuring that only one process at a time can access a shared resource in a distributed system. There are two main types of algorithms for DME: token based and non token based.

## Token based algorithms

- In token based algorithms, a unique token is shared among all the sites in the distributed system. The token represents the permission to enter the critical section. Only the site that holds the token can access the shared resource.
- Token based algorithms guarantee mutual exclusion and freedom from deadlock, but they may suffer from starvation and high message complexity.
- Examples of token based algorithms are:
  - **Suzuki-Kasami algorithm**: This is a modification of Ricart-Agrawala algorithm, a permission based (non token based) algorithm that uses REQUEST and REPLY messages to ensure mutual exclusion. In Suzuki-Kasami algorithm, the token is a vector that records the number of requests made by each site. The token is passed to the site with the highest request number that has not yet received the token. This algorithm reduces the number of messages from O(n^2) to O(n) per critical section execution, where n is the number of sites.
  - **Raymond's algorithm**: This is a tree-based algorithm that organizes the sites into a logical tree. The token is initially held by the root of the tree. A site that wants to enter the critical section sends a REQUEST message to its parent in the tree. The parent forwards the request to its parent, and so on, until it reaches the token holder. The token holder then sends the token along the reverse path to the requester. A site that receives the token becomes the new root of the tree. This algorithm reduces the number of messages to O(log n) per critical section execution, but it may cause starvation and high delay.

## Non token based algorithms

- In non token based algorithms, also known as permission based algorithms, a site communicates with a set of other sites to determine who should execute the critical section next. A site that wants to enter the critical section sends a REQUEST message to the other sites and waits for their REPLY messages. The REPLY messages indicate the permission or denial of the request. A site can enter the critical section only if it receives permission from all the other sites.
- Non token based algorithms do not require a unique token, but they may cause deadlock, starvation, and high message complexity.
- Examples of non token based algorithms are:
  - **Lamport's algorithm**: This is a timestamp based algorithm that uses logical clocks to order the requests for the critical section. A site that wants to enter the critical section sends a REQUEST message with its timestamp to all the other sites. A site that receives a REQUEST message replies with a REPLY message if it is not interested in the critical section or if its timestamp is larger than the requester's timestamp. Otherwise, it defers the reply until it exits the critical section. A site can enter the critical section only if it receives REPLY messages from all the other sites and its timestamp is the smallest among all the requests. This algorithm ensures mutual exclusion and freedom from starvation, but it requires O(n^2) messages per critical section execution, where n is the number of sites.
  - **Ricart-Agrawala algorithm**: This is an optimization of Lamport's algorithm that reduces the number of messages to O(n) per critical section execution. A site that wants to enter the critical section sends a REQUEST message with its timestamp to all the other sites. A site that receives a REQUEST message replies with a REPLY message if it is not interested in the critical section or if it has already sent a REPLY message to a site with a smaller timestamp. Otherwise, it defers the reply until it exits the critical section. A site can enter the critical section only if it receives REPLY messages from all the other sites.

: https://www.geeksforgeeks.org/suzuki-kasami-algorithm-for-mutual-exclusion-in-distributed-system/
: https://www.geeksforgeeks.org/raymonds-algorithm-for-mutual-exclusion-in-distributed-system/
: https://www.geeksforgeeks.org/lamports-algorithm-for-mutual-exclusion-in-distributed-system/
: https://www.geeksforgeeks.org/ricart-agrawala-algorithm-for-mutual-exclusion-in-distributed-system/
: https://



# Performance Metric for Distributed Mutual Exclusion Algorithms

Distributed mutual exclusion algorithms are algorithms that ensure that only one process at a time can access a shared resource in a distributed system. There are different types of distributed mutual exclusion algorithms, such as token-based, non-token-based, and quorum-based algorithms .

The performance of distributed mutual exclusion algorithms can be evaluated by the following four metrics :

- **Message complexity**: It is the number of messages that are required per critical section (CS) execution by a process. It measures the communication overhead of the algorithm. The lower the message complexity, the better the performance.
- **Synchronization delay**: It is the time elapsed between the moment when a process leaves the CS and the moment when the next process enters the CS. It measures the degree of concurrency of the algorithm. The lower the synchronization delay, the better the performance.
- **Response time**: It is the time elapsed between the moment when a process requests to enter the CS and the moment when it actually enters the CS. It measures the waiting time of the process. The lower the response time, the better the performance.
- **Throughput**: It is the number of CS executions per unit time in the system. It measures the efficiency of the algorithm. The higher the throughput, the better the performance.

Different algorithms may have different trade-offs among these metrics. For example, a token-based algorithm may have low message complexity but high synchronization delay, while a non-token-based algorithm may have high message complexity but low synchronization delay . Therefore, the choice of the best algorithm depends on the application requirements and the system characteristics.



# Unit 3 - Distributed Deadlock Detection

- A **deadlock** is a condition where a set of processes request resources that are held by other processes in the set, and none of the processes can proceed until some of the resources are released.
- A **distributed deadlock** is a deadlock that involves processes and resources located on different machines in a distributed system.
- **Deadlock detection** is a strategy to handle deadlocks by examining the status of the process-resource interactions for the presence of cyclic wait.
- **Deadlock resolution** is a strategy to handle deadlocks by aborting or preempting some of the deadlocked processes or resources to break the cycle.
- Deadlock detection in distributed systems can be done by two main approaches:
  - **Global wait-for graph (WFG)**: A graph that represents the waiting relationships among processes and resources in the system. A node in the graph can be either a process or a resource, and an edge from node A to node B means that A is waiting for B. A cycle in the graph indicates a deadlock. To construct a global WFG, each machine in the system maintains a local WFG and periodically sends it to a designated deadlock detector, which merges the local WFGs and checks for cycles.
  - **Edge chasing**: A distributed algorithm that uses probe messages to detect cycles in the system. A probe message contains the identity of the sender and a list of visited nodes. When a process sends a request for a resource, it also sends a probe message to the resource holder. The resource holder appends its identity to the list and forwards the probe message to the next resource holder in its wait-for list. If a process receives a probe message that contains its own identity, it detects a cycle and initiates deadlock resolution.



# System Model for Distributed Deadlock Detection

- A distributed system consists of a collection of processes that communicate and share resources over a network.
- A deadlock is a situation where a set of processes are blocked waiting for resources that are held by other processes in the set.
- Distributed deadlock detection is the problem of finding and resolving deadlocks in a distributed system.
- There are three main approaches to distributed deadlock detection  :
  - Centralized approach: A single node is designated as the deadlock detector and collects information from all other nodes about their resource requests and allocations. The deadlock detector constructs a global wait-for graph (WFG) and checks for cycles in the graph. If a cycle is found, it indicates a deadlock and the detector aborts one or more processes to break the cycle.
  - Hierarchical approach: The nodes are organized into clusters and each cluster has a local deadlock detector that handles the deadlock detection within the cluster. The clusters are further grouped into higher-level clusters and so on, forming a hierarchy of deadlock detectors. The deadlock detectors at each level exchange information with their neighbors and construct a partial WFG. If a cycle is detected at any level, it indicates a deadlock and the detector aborts one or more processes to break the cycle.
  - Distributed approach: There is no central or hierarchical authority for deadlock detection. Each node maintains its own local WFG and periodically initiates a distributed algorithm to detect cycles in the global WFG. One such algorithm is edge chasing, where each node sends a probe message along the edges of its local WFG and waits for a reply. If a node receives a probe message that originated from itself, it indicates a cycle and the node aborts itself or another process to break the cycle.
- The advantages and disadvantages of each approach depend on factors such as the frequency and size of deadlocks, the communication and computation overhead, the accuracy and timeliness of deadlock detection, and the fairness and efficiency of deadlock resolution.



# Resource Vs Communication Deadlocks

- A deadlock is a condition where a process cannot proceed because it needs to obtain a resource held by another process, and it itself is holding a resource that the other process needs.
- Four requirements must be met for a deadlock to occur:
  - Mutual exclusion: each resource can be assigned to only one process at a time.
  - Hold and wait: a process holding a resource can request additional resources without releasing the ones it already holds.
  - No preemption: a resource can be released only by the process that holds it, voluntarily or after completing its task.
  - Circular wait: there exists a circular chain of processes, each of which is waiting for a resource held by the next process in the chain.
- There are two types of deadlocks in distributed systems: resource deadlocks and communication deadlocks.
- Resource deadlocks occur when processes access resources, such as data objects in database systems and buffers in store and forward communication networks. A process acquires a resource before accessing it and releasing it after using it.
- Communication deadlocks occur when processes exchange messages, such as in message passing systems and distributed algorithms. A process sends a message to another process and waits for a reply before continuing its execution.
- The main difference between resource deadlocks and communication deadlocks is that in resource deadlocks, the resources are passive entities that do not initiate any action, whereas in communication deadlocks, the resources are active entities that can send and receive messages.
- Another difference is that in resource deadlocks, the processes are aware of the resources they need and request them explicitly, whereas in communication deadlocks, the processes are unaware of the messages they need and wait for them implicitly.
- A third difference is that in resource deadlocks, the processes can release the resources they hold at any time, whereas in communication deadlocks, the processes cannot release the messages they hold until they receive a reply.
- A fourth difference is that in resource deadlocks, the processes can detect the deadlock by examining the resource allocation graph, whereas in communication deadlocks, the processes cannot detect the deadlock by examining the message passing graph.
- A fifth difference is that in resource deadlocks, the deadlock can be resolved by aborting one or more processes or preempting one or more resources, whereas in communication deadlocks, the deadlock can be resolved by sending dummy messages or breaking the circular wait.



# Deadlock Prevention for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process. In a distributed system, deadlocks are more difficult to detect and resolve because the processes and resources may be physically dispersed across different nodes.

Deadlock prevention is a technique to avoid the occurrence of deadlocks by ensuring that at least one of the four necessary conditions for deadlock (mutual exclusion, hold and wait, no preemption, and circular wait) is never satisfied.

There are two main methods of deadlock prevention in a distributed system:

- Ordered request
- Collective request

## Ordered Request

In this method, each resource type is assigned a certain level to maintain a resource request policy for a process. This is known as the resource allocation policy. The policy states that a process can request resources only in an increasing order of levels. For example, if there are three resource types A, B, and C with levels 1, 2, and 3 respectively, then a process can request A before B, and B before C, but not C before A or B.

This method prevents circular wait condition, as there is no cycle in the resource allocation graph. However, this method may be inefficient and impractical, as it may force a process to request resources that it does not need or to release resources that it still needs.

## Collective Request

In this method, a process must request all the resources it needs at the same time before starting execution. This is known as the atomic allocation policy. The policy states that a process can either get all the resources it requests or none of them. For example, if a process needs resources A, B, and C, then it must request them together and wait until they are all available.

This method prevents hold and wait condition, as a process does not hold any resources while waiting for others. However, this method may also be inefficient and impractical, as it may cause a lot of resource wastage and starvation.



# Avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- Avoidance is a technique to prevent deadlocks from occurring in a distributed system by ensuring that the system is always in a safe state.
- A safe state is a state where there is at least one sequence of resource allocation that does not lead to a deadlock.
- Avoidance requires the system to have some knowledge of the current and future resource requests and releases of each process.
- Avoidance can be implemented by using either a centralized or a decentralized approach.
- In the centralized approach, there is a single coordinator that maintains the global state of the system and decides whether to grant or deny a resource request based on the safe state criterion.
- In the decentralized approach, there is no coordinator and each process maintains its own local state and communicates with other processes to determine the safe state of the system.
- Some of the advantages of avoidance are:
  - It does not require the detection and recovery of deadlocks, which can be costly and complex.
  - It does not impose any restrictions on the resource requests and releases of the processes, unlike prevention.
  - It can achieve a higher degree of resource utilization and system throughput than prevention.
- Some of the disadvantages of avoidance are:
  - It requires the system to have accurate and complete information about the current and future resource demands of the processes, which may not be feasible or realistic in a distributed system.
  - It may incur a high overhead of maintaining and exchanging the state information among the processes or the coordinator.
  - It may result in a conservative resource allocation policy that may deny some requests that are actually safe, leading to a loss of concurrency and performance.



# Detection and Resolution of Distributed Deadlocks

- A distributed deadlock is a situation where a set of processes in a distributed system are waiting for each other to release resources or messages, and none of them can proceed.
- Distributed deadlock detection is the problem of finding and resolving such deadlocks in a distributed system.
- Distributed deadlock resolution is the process of breaking the deadlock by aborting or rolling back some of the deadlocked processes, and releasing their resources or messages to other processes.
- There are two main approaches to distributed deadlock detection and resolution: centralized and distributed.

## Centralized Approach

- In the centralized approach, there is a designated coordinator process that is responsible for maintaining and analyzing the global wait-for graph (WFG) of the system.
- The WFG is a directed graph that represents the dependencies among processes and resources in the system. A node in the WFG is either a process or a resource, and an edge from node A to node B means that A is waiting for B.
- A cycle in the WFG indicates a deadlock. The coordinator periodically collects the local WFG information from each process, and merges them into a global WFG. Then, it searches the global WFG for cycles, and initiates the resolution of any detected deadlocks.
- The advantages of the centralized approach are simplicity and efficiency. The disadvantages are the single point of failure and the communication overhead of the coordinator.

## Distributed Approach

- In the distributed approach, there is no coordinator process, and each process participates in the deadlock detection and resolution.
- There are three main techniques for distributed deadlock detection: edge chasing, path pushing, and diffusing computation.
- Edge chasing is a technique where each process sends a probe message along the edges of the WFG, and waits for an acknowledgment. If a process receives a probe message that it has sent before, it means that there is a cycle in the WFG, and a deadlock has occurred.
- Path pushing is a technique where each process maintains a list of processes that are dependent on it, and sends this list along with any request or reply message. If a process receives a message that contains its own identifier in the list, it means that there is a cycle in the WFG, and a deadlock has occurred.
- Diffusing computation is a technique where each process initiates a distributed computation when it requests a resource, and terminates it when it releases the resource. The computation involves sending and receiving messages among the processes that are involved in the resource allocation. If a process detects that its computation has terminated without receiving the resource, it means that there is a deadlock in the system.
- The advantages of the distributed approach are fault tolerance and scalability. The disadvantages are the complexity and the message overhead of the techniques.



# Centralized Deadlock Detection

- This is a technique used in distributed systems to handle deadlock detection.
- According to this technique, the system maintains one global wait-for graph in a single chosen site, which is named as deadlock-detection coordinator.
- The coordinator collects information about the local wait-for graphs of all the sites and constructs the global wait-for graph.
- The coordinator periodically runs a deadlock detection algorithm on the global wait-for graph and identifies any cycles that indicate deadlocks.
- The coordinator then informs the involved sites to abort one or more processes to resolve the deadlock.
- The advantages of this technique are simplicity and low communication overhead.
- The disadvantages of this technique are the dependency on a single site, the possibility of false or phantom deadlocks, and the scalability issues for large systems .

: https://www.exploredatabase.com/2014/06/centralized-deadlock-detection-approach-in-distributed-database.html
: https://www.javatpoint.com/deadlock-detection-in-distributed-systems
: https://people.cs.rutgers.edu/~pxk/417/notes/deadlock.html
: https://www.geeksforgeeks.org/deadlock-detection-in-distributed-systems/



# Distributed Deadlock Detection

- A **deadlock** is a condition where a set of processes request resources that are held by other processes in the set, and none of the processes can proceed until they obtain the resources they need.
- A **distributed deadlock** is a deadlock that involves processes and resources located on different machines in a distributed system.
- **Deadlock detection** is a strategy to deal with deadlocks by identifying and resolving them after they occur.
- **Distributed deadlock detection** is a technique to detect and resolve deadlocks in distributed systems by using either a global or a local perspective.
- There are three main approaches to distributed deadlock detection:
  - **Global wait-for graph (WFG)**: A WFG is a directed graph that represents the waiting relationships among processes and resources in the system. A node in the WFG can be either a process or a resource, and an edge from node A to node B means that A is waiting for B. A deadlock exists if and only if the WFG contains a cycle. To construct a global WFG, each machine in the system maintains a local WFG and periodically sends it to a designated deadlock detector, which merges the local WFGs and checks for cycles. This approach requires a lot of communication and computation overhead, and may not reflect the current state of the system due to message delays.
  - **Edge chasing**: Edge chasing is a distributed algorithm that detects cycles in the WFG without constructing it explicitly. The basic idea is to send probe messages along the edges of the WFG, and if a probe message returns to its originator, a cycle is detected. There are different variants of edge chasing, such as the path-pushing, the edge-pushing, and the diffusing computation algorithms, which differ in the amount and direction of information carried by the probe messages. This approach reduces the communication and computation overhead, but may still incur false positives due to message delays and concurrency.
  - **Hierarchical deadlock detection**: Hierarchical deadlock detection is a hybrid approach that combines the advantages of the global WFG and the edge chasing methods. The basic idea is to partition the system into clusters of machines, and assign a coordinator for each cluster. The coordinators are responsible for detecting deadlocks within their clusters using either the global WFG or the edge chasing method, and for detecting inter-cluster deadlocks using a higher-level WFG or edge chasing algorithm. This approach reduces the complexity and overhead of deadlock detection, but requires a stable and efficient clustering scheme.



# Path Pushing Algorithms

- Path pushing algorithms are a class of distributed deadlock detection algorithms that use an explicit global wait-for graph (WFG) to detect cycles  .
- A WFG is a directed graph that represents the dependencies among processes in a distributed system. A node in the WFG is a process and an edge from node P to node Q means that P is waiting for a resource held by Q  .
- The basic idea of path pushing algorithms is to build a global WFG for each site of the distributed system. A site is a logical unit that contains one or more processes  .
- In this class of algorithms, at each site, whenever a deadlock computation is performed, it sends its local WFG to all the neighboring sites. A neighboring site is a site that has an edge to or from the current site in the global WFG  .
- Each site maintains a local WFG that contains the nodes and edges of the processes at that site, as well as the nodes and edges of the processes at the neighboring sites that are reachable from the current site  .
- Each site also maintains a path matrix that records the paths from the processes at the current site to the processes at the neighboring sites. A path is a sequence of nodes and edges in the WFG that represents a dependency chain  .
- When a site receives a local WFG from a neighboring site, it updates its own local WFG and path matrix by adding or deleting nodes and edges, and by merging or splitting paths. It also sends its updated local WFG to all its neighboring sites  .
- A site detects a deadlock when it finds a cycle in its local WFG. A cycle is a path that starts and ends at the same node. A cycle indicates that there is a circular dependency among the processes in the cycle, and thus they are deadlocked  .
- A site initiates a deadlock resolution when it detects a deadlock. It sends a message to all the processes in the cycle, asking them to release their resources or abort. It also informs the neighboring sites about the deadlock resolution  .
- Path pushing algorithms have the advantage of being simple and efficient, as they only require local information and communication. They also have the disadvantage of being prone to false deadlocks, as they may detect cycles that do not exist in the global WFG  .

: https://www.javatpoint.com/deadlock-detection-in-distributed-systems
: https://www.geeksforgeeks.org/deadlock-handling-strategies-in-distributed-system/
: https://www.cs.uic.edu/~ajayk/Chapter10.pdf



# Edge Chasing Algorithms for Distributed Deadlock Detection

- Edge chasing algorithms are a class of distributed deadlock detection algorithms that use special messages called probes to trace the dependency graph of processes and resources in a distributed system  .
- A probe is a triplet (i, j, k) that denotes that the deadlock detection is initiated by process P_i and the message is being sent by the home site of process P_j to the home site of process P_k .
- The probe message follows the edges of the dependency graph from the waiting processes to the blocking processes until either a cycle is detected or all the edges are traversed  .
- A cycle is detected when a probe message returns to the initiator process or when a process receives a probe message with its own identifier in the triplet  .
- If a cycle is detected, then a deadlock exists and the processes involved in the cycle are notified to resolve the deadlock  .
- If no cycle is detected, then no deadlock exists and the probe messages are discarded  .
- Edge chasing algorithms are also known as Chandy-Misra-Haas's algorithms, as they were proposed by K. Mani Chandy, Jayadev Misra, and Laura M. Haas in 1983  .
- Edge chasing algorithms can be applied to different request models, such as AND model, OR model, and AND-OR model, depending on the type of resource requests made by the processes .
- Edge chasing algorithms have some advantages and disadvantages over other classes of distributed deadlock detection algorithms, such as path-pushing, diffusion computation, and global state detection .
- Some advantages are:
  - Edge chasing algorithms are simple and easy to implement.
  - Edge chasing algorithms do not require the maintenance of global or local wait-for graphs .
  - Edge chasing algorithms can detect deadlocks in a distributed system without a central coordinator or a leader process .
- Some disadvantages are:
  - Edge chasing algorithms may generate a large number of probe messages, which can increase the network traffic and the message overhead .
  - Edge chasing algorithms may detect false deadlocks, which are cycles that do not involve all the processes in the system .
  - Edge chasing algorithms may not detect some deadlocks, which are cycles that involve processes that are not reachable by the probe messages .



# Unit 4 - Agreement Protocols

- Agreement protocols are a class of distributed algorithms that help processes in a network to reach a common decision in the presence of failures .
- Agreement protocols are useful for ensuring reliability, consistency, and fault tolerance in distributed systems, such as distributed databases, distributed consensus, leader election, and atomic broadcast  .
- Agreement protocols can be classified into two types: **consensus protocols** and **atomic commitment protocols** .
  - Consensus protocols require that all non-faulty processes agree on a single value proposed by one or more processes .
  - Atomic commitment protocols require that all non-faulty processes agree on whether to commit or abort a transaction that involves multiple processes .
- Agreement protocols face several challenges in distributed systems, such as asynchronous communication, message delays, message losses, process crashes, and process failures  .
- Agreement protocols must satisfy three properties: **validity**, **agreement**, and **termination** .
  - Validity means that the agreed value must be one of the proposed values .
  - Agreement means that all non-faulty processes must agree on the same value .
  - Termination means that all non-faulty processes must eventually decide on a value .
- Agreement protocols can be implemented using various techniques, such as message passing, voting, quorums, timeouts, and failure detectors   .
- Agreement protocols can be evaluated based on their performance, complexity, and fault tolerance .
  - Performance measures the time and communication costs of reaching an agreement .
  - Complexity measures the number of rounds and messages required to reach an agreement .
  - Fault tolerance measures the resilience of the protocol to different types of failures, such as crash failures, omission failures, and Byzantine failures .



# Introduction for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- Agreement protocols are a class of protocols that allow a set of processes in a distributed system to reach a consensus on some value or action, despite the possibility of failures or malicious behavior.
- Agreement protocols are essential for ensuring the correctness and consistency of distributed systems, especially in the presence of faults or attacks.
- Some examples of agreement problems are:
  - Leader election: electing a unique process to coordinate some task or decision.
  - Atomic commit: ensuring that a set of processes either all commit or all abort a transaction.
  - Byzantine agreement: reaching a consensus on a value even if some processes are faulty or malicious.
  - Consensus: reaching a consensus on a value in a fault-tolerant way.
- Agreement protocols can be classified according to the following criteria:
  - Synchronous vs asynchronous: whether the system has bounded or unbounded delays in message delivery and process execution.
  - Crash vs Byzantine: whether the system can tolerate only crash failures or also arbitrary (Byzantine) failures.
  - Deterministic vs randomized: whether the protocol always guarantees a correct outcome or only with some probability.
  - Binary vs multivalued: whether the protocol agrees on a binary value (0 or 1) or a value from a larger domain.
- The difficulty and feasibility of agreement protocols depend on the combination of these criteria. For example, in a synchronous system with crash failures, consensus can be achieved deterministically with a simple majority of processes. However, in an asynchronous system with Byzantine failures, consensus is impossible to achieve deterministically, even with a single faulty process.
- In this unit, we will study some of the fundamental agreement protocols and their properties, such as:
  - The FLP impossibility result: proving that consensus is impossible in an asynchronous system with crash failures.
  - The Paxos protocol: achieving consensus in a partially synchronous system with crash failures.
  - The Raft protocol: a simplified and practical variant of Paxos for leader election and log replication.
  - The Lamport's Byzantine Generals problem: defining the Byzantine agreement problem and its requirements.
  - The Byzantine agreement protocol: achieving Byzantine agreement in a synchronous system with a 2/3 majority of honest processes.
  - The Practical Byzantine Fault Tolerance (PBFT) protocol: achieving Byzantine agreement in a partially synchronous system with a 2/3 majority of honest processes.



# System Models for Distributed Systems

A system model is a simplified representation of a distributed system that captures its essential properties and design choices. System models help us to reason about the behavior, performance, and correctness of distributed systems. There are different types of system models that focus on different aspects of distributed systems, such as:

- Network behavior: how reliable, fast, and secure are the communication links between the nodes?
- Node behavior: how reliable, fast, and secure are the nodes themselves?
- Timing behavior: how synchronized are the clocks of the nodes and how predictable are the delays in the system?
- Consensus behavior: how do the nodes agree on a common value or action in the presence of failures and asynchrony?

Some of the common system models for distributed systems are:

- Synchronous model: assumes that there are known bounds on the network delay, the node speed, and the clock drift. This model simplifies the design and analysis of distributed algorithms, but it is unrealistic in practice.
- Asynchronous model: assumes that there are no bounds on the network delay, the node speed, and the clock drift. This model is more realistic and general, but it makes the design and analysis of distributed algorithms more difficult and sometimes impossible.
- Partially synchronous model: assumes that there are bounds on the network delay, the node speed, and the clock drift, but they are unknown or may change over time. This model is a compromise between the synchronous and asynchronous models, and it captures the behavior of many real-world distributed systems.
- Crash-stop model: assumes that nodes can only fail by crashing (stopping to execute) and that crashed nodes do not recover. This model simplifies the design and analysis of fault-tolerant distributed algorithms, but it does not account for other types of failures or recoveries.
- Crash-recovery model: assumes that nodes can fail by crashing and that crashed nodes can recover after some time. This model is more realistic and general, but it requires the use of persistent storage and recovery mechanisms to ensure consistency and progress.
- Byzantine model: assumes that nodes can fail in arbitrary ways, such as sending incorrect or malicious messages, or colluding with other faulty nodes. This model is the most pessimistic and challenging, but it captures the worst-case scenarios of distributed systems.

Some of the popular consensus algorithms for distributed systems, such as Paxos and Raft, assume a partially synchronous and crash-recovery system model, meaning that they can tolerate network delays and node crashes, but not Byzantine failures. They also require a majority of nodes to be correct and reachable to achieve consensus.



# Classification of Agreement Problem in Distributed System

An agreement problem in a distributed system is a problem where a set of processes need to reach a common decision based on their local inputs and messages exchanged with each other. Agreement problems are fundamental for achieving coordination, consistency, and fault tolerance in distributed systems. There are different types of agreement problems, depending on the assumptions and requirements of the system model and the application domain. Some of the common agreement problems are:

- **Byzantine agreement problem**: In this problem, each process has an initial value and needs to decide on a final value, such that all correct processes agree on the same value and the value is equal to the initial value of some correct process. The system may contain faulty processes that can behave arbitrarily, called Byzantine faults. The goal is to tolerate as many Byzantine faults as possible and ensure agreement among the correct processes .
- **Consensus problem**: In this problem, each process has an initial value and needs to decide on a final value, such that all correct processes agree on the same value and the value is equal to the initial value of some process. The system may contain faulty processes that can fail by crashing, called crash faults. The goal is to tolerate as many crash faults as possible and ensure agreement among the correct processes .
- **Interactive consistency problem**: In this problem, each process has an initial value and needs to decide on a vector of values, such that the vector contains the initial values of all processes and all correct processes agree on the same vector. The system may contain faulty processes that can behave arbitrarily, called Byzantine faults. The goal is to tolerate as many Byzantine faults as possible and ensure agreement among the correct processes .
- **Atomic commitment problem**: In this problem, each process has an initial value of either commit or abort and needs to decide on a final value of either commit or abort, such that all correct processes agree on the same value and the value is commit only if all processes have the initial value of commit. The system may contain faulty processes that can fail by crashing, called crash faults. The goal is to tolerate as many crash faults as possible and ensure agreement among the correct processes. This problem is often used in distributed transactions to ensure atomicity .
- **Atomic broadcast problem**: In this problem, each process can send a message to all other processes and needs to deliver the messages, such that all correct processes deliver the same set of messages in the same order. The system may contain faulty processes that can fail by crashing, called crash faults. The goal is to tolerate as many crash faults as possible and ensure agreement among the correct processes. This problem is often used in distributed replication to ensure consistency .
- **Group membership problem**: In this problem, each process needs to decide on a set of processes that are currently alive and reachable, called the group view, such that all correct processes agree on the same group view and the group view contains only correct processes. The system may contain faulty processes that can fail by crashing or become unreachable due to network partitions, called network faults. The goal is to tolerate as many network faults as possible and ensure agreement among the correct processes. This problem is often used in distributed fault detection and recovery to ensure availability .

: Distributed System:- (Agreement Protocols, Classification of ... - Stuvia
: Agreement Problems in Fault-Tolerant Distributed Systems
: Consensus and agreement algorithms - Cambridge Core
: Group Membership Service - an overview | ScienceDirect Topics



# Byzantine Agreement Problem

The Byzantine agreement problem is a fundamental problem in fault tolerant distributed computing. It requires a set of parties in a distributed environment to agree on a value even if some of the parties are corrupted. A corrupted party may behave arbitrarily, sending conflicting or misleading messages to different parties, or remaining silent. The problem is also known as the Byzantine generals problem, the interactive consistency problem, or the source congruency problem.

The problem was first defined by Lamport in the context of a source processor broadcasting its initial value to other processors in the system. The processors must agree on the value sent by the source, even if the source or some of the processors are faulty. Lamport also gave the first solution to the problem under the assumption of processor failure.

The problem can be illustrated by the following analogy  :

- Several divisions of the Byzantine army are camped outside an enemy city, each division commanded by its own general. The generals can communicate with one another only by messenger.
- After observing the enemy, they must decide upon a common plan of action. The possible plans are to attack or retreat.
- Some of the generals may be traitors, who try to prevent the loyal generals from reaching agreement.
- The generals must have an algorithm to guarantee that:
  - All loyal generals decide upon the same plan of action.
  - A small number of traitors cannot cause the loyal generals to adopt a bad plan.

The Byzantine agreement problem is challenging because of the following reasons:

- The communication channels may be unreliable, and messages may be lost, delayed, or corrupted.
- The number and identity of the traitors may be unknown to the loyal generals.
- The traitors may collude and coordinate their actions to maximize their impact.
- The traitors may adapt their behavior based on the messages they receive or observe.

The Byzantine agreement problem has many applications in distributed systems, such as:

- Consensus protocols, which aim to achieve agreement on a shared state among a set of nodes, such as in blockchain or distributed databases.
- Fault-tolerant replication, which aims to maintain consistent copies of data or services across multiple nodes, such as in distributed file systems or web servers.
- Secure multiparty computation, which aims to enable a set of parties to jointly compute a function on their private inputs, such as in privacy-preserving data analysis or electronic voting.

The Byzantine agreement problem is also related to other problems in distributed computing, such as:

- Reliable broadcast, which aims to ensure that a message sent by a source is received by all nodes, even if the source or some of the nodes are faulty.
- Atomic commit, which aims to ensure that a set of transactions are either all committed or all aborted, even if some of the nodes are faulty.
- Leader election, which aims to elect a unique leader among a set of nodes, even if some of the nodes are faulty.



# Consensus problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- The consensus problem is the problem of getting a set of nodes in a distributed system to agree on something - it might be a value, a course of action or a decision.
- Achieving consensus allows a distributed system to act as a single entity, with every individual node aware of and in agreement with the actions of the whole of the network.
- Consensus is a general agreement on a decision made by the majority of those involved.
- Consensus is needed in a distributed system to ensure overall system reliability on top of unreliable system components.
- Consensus is also needed to coordinate the actions of different nodes, such as committing transactions, electing leaders, replicating data, etc.
- Consensus is hard to achieve in a distributed system due to the possibility of failures, such as node crashes, network partitions, message losses, etc.
- Consensus algorithms are protocols that enable nodes to reach consensus in a distributed system despite failures.
- Consensus algorithms have to satisfy some properties, such as validity, agreement, termination, integrity, etc.
- There are many ways in which processes in a distributed system can reach consensus, but there is usually a trade-off between security and performance.
- Some examples of consensus algorithms are two-phase commit, three-phase commit, Paxos, Raft, etc .



# Interactive Consistency Problem in Distributed System

- Interactive consistency is the problem in which **n** nodes, each having its own private value, where up to **t** may be Byzantine, run an algorithm that allows all non-faulty nodes to infer the values of each other node  .
- Byzantine nodes are those that can behave arbitrarily, such as sending different messages to different nodes, lying about their values, or crashing.
- Interactive consistency is also known as **Byzantine Generals Problem** or **Byzantine Agreement Problem** .
- Interactive consistency is a fundamental problem in distributed systems, especially for critical applications that rely on the combination of the opinions of multiple peers to provide a service, such as fault-tolerant control systems, distributed databases, or blockchain systems  .
- Interactive consistency is a challenging problem because of the possibility of network failures, message delays, or malicious attacks that can prevent the nodes from reaching a consistent agreement  .
- Interactive consistency has two variants: **weak interactive consistency** and **strong interactive consistency** .
  - Weak interactive consistency requires that all non-faulty nodes agree on the values of all non-faulty nodes, but not necessarily on the values of faulty nodes .
  - Strong interactive consistency requires that all non-faulty nodes agree on the values of all nodes, including faulty ones .
- Interactive consistency has two types of solutions: **deterministic** and **randomized** .
  - Deterministic solutions use a fixed protocol that guarantees to reach a consistent agreement in a finite number of rounds, regardless of the randomness in the system .
  - Randomized solutions use a probabilistic protocol that can reach a consistent agreement with high probability in a finite number of rounds, but may fail with low probability due to the randomness in the system .
- Interactive consistency has two types of assumptions: **synchronous** and **asynchronous** .
  - Synchronous assumptions imply that there is a known upper bound on the message delivery time and the node processing time, and that all nodes have synchronized clocks .
  - Asynchronous assumptions imply that there is no known upper bound on the message delivery time and the node processing time, and that the nodes have no synchronized clocks .
- Interactive consistency has two types of communication models: **broadcast** and **point-to-point** .
  - Broadcast communication model implies that a node can send a message to all other nodes in one round, and that all non-faulty nodes receive the same message .
  - Point-to-point communication model implies that a node can send a message to one or more other nodes in one round, and that the messages may be different or lost .
- Interactive consistency has a lower bound on the number of nodes and the number of rounds required to solve the problem, depending on the variant, the type of solution, the type of assumption, and the type of communication model .
  - For weak interactive consistency, the lower bound on the number of nodes is **n > 3t** for deterministic solutions, and **n > t** for randomized solutions, regardless of the type of assumption and the type of communication model .
  - For strong interactive consistency, the lower bound on the number of nodes is **n > 3t** for deterministic solutions, and **n > 2t** for randomized solutions, regardless of the type of assumption and the type of communication model .
  - For synchronous assumptions, the lower bound on the number of rounds is **t + 1** for deterministic solutions, and **1** for randomized solutions, regardless of the variant and the type of communication model .
  - For asynchronous assumptions, the lower bound on the number of rounds is **unbounded** for deterministic solutions, and **log n** for randomized solutions, regardless of the variant and the type of communication model[^2



# Solution to Byzantine Agreement problem

- The Byzantine agreement problem is a fundamental problem in fault tolerant distributed computing that requires a set of parties to agree on a value even if some of the parties are corrupted or faulty.
- The problem was first defined by Lamport who also gave a solution under the situation of processor failure. The problem is also known as the interactive consistency problem or the Byzantine Generals problem.
- The Byzantine Generals problem is an analogy that illustrates the difficulty of achieving consensus in a distributed system. The scenario is as follows :

  - Several divisions of the Byzantine army are camped outside an enemy city, each division commanded by its own general. The generals can communicate with one another only by messenger.
  - After observing the enemy, they must decide upon a common plan of action. However, some of the generals may be traitors and try to prevent the loyal generals from reaching agreement.
  - The generals must have an algorithm to guarantee that: (a) All loyal generals decide upon the same plan of action, and (b) A small number of traitors cannot cause the loyal generals to adopt a bad plan.

- A solution to the Byzantine agreement problem must satisfy the following properties:

  - **Validity**: If all parties start with the same value, then they must all decide on that value.
  - **Agreement**: All honest parties must decide on the same value.
  - **Termination**: All honest parties must eventually decide on a value.

- A simple solution to the Byzantine agreement problem is to use a majority voting scheme, where each party broadcasts its value to all other parties, and then decides on the value that is received by the majority of the parties. However, this solution only works if there are more than two-thirds of honest parties in the system, i.e., if the number of faulty parties is less than one-third of the total number of parties.
- A more general solution to the Byzantine agreement problem is to use a recursive algorithm that involves multiple rounds of message exchange, where each party sends and receives messages from a subset of other parties, and then decides on a value based on the received messages. This solution can tolerate any number of faulty parties, as long as they are less than half of the total number of parties.
- One example of such a recursive algorithm is the Byzantine Agreement protocol by Pease, Shostak, and Lamport , which works as follows:

  - The protocol assumes that there are n parties, and that each party has a unique identifier from 1 to n. The protocol also assumes that there is a source party, denoted by p1, that has an initial value v, and that all other parties have no initial value.
  - The protocol consists of m rounds, where m is the maximum number of faulty parties in the system. In each round, each party sends and receives messages from a subset of other parties, and then updates its value based on the received messages. The subset of parties that each party communicates with depends on the round number and the party's identifier.
  - In the first round, the source party p1 broadcasts its value v to all other parties. Each party that receives v from p1 sets its value to v, and each party that does not receive v from p1 sets its value to null.
  - In the second round, each party pi, where i > 1, sends its value to all parties with identifiers greater than i. Each party that receives a value from pi sets its value to that value, and each party that does not receive a value from pi sets its value to null.
  - In the third round, each party pi, where i > 2, sends its value to all parties with identifiers greater than i. Each party that receives a value from pi sets its value to that value, and each party that does not receive a value from pi sets its value to null.
  - And so on, until the m-th round, where each party pi, where i > m, sends its value to all parties with identifiers greater than i. Each party that receives a value from pi sets its value to that value, and each party that does not receive a value from pi sets its value to null.
  - After the m-th round, each party decides on its value as follows: If the party has a non-null value, then it decides on that value. If the party has a null value, then it



# Application of Agreement problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- Agreement problem is a fundamental problem in distributed computing and multi-agent systems, where a set of processes need to coordinate and reach a common decision or value, despite the presence of failures or faults .
- Agreement problem has many variants, such as consensus, atomic commitment, atomic broadcast, and group membership. Each variant has different assumptions, requirements, and guarantees for the processes involved.
- Consensus is the most basic and general form of agreement problem, where each process proposes a value and all correct processes must agree on the same value, which must be one of the proposed values . Consensus is essential for implementing fault-tolerant services, such as replicated state machines, distributed transactions, and leader election.
- Atomic commitment is a special case of consensus, where each process has a binary value (commit or abort) and all correct processes must agree on the same value, which must be commit if and only if all processes have commit as their initial value . Atomic commitment is useful for ensuring the atomicity and durability of distributed transactions, where each participant must either commit or abort the transaction.
- Atomic broadcast is another special case of consensus, where each process broadcasts a message and all correct processes must deliver the same set of messages in the same order . Atomic broadcast is useful for implementing total order multicast, where each message is delivered to all processes in a consistent order, regardless of the sender or the network delays.
- Group membership is a related problem to consensus, where each process maintains a view of the current set of processes in the system, and all correct processes must agree on the same view, which must reflect the actual failures and recoveries of processes . Group membership is useful for managing the membership and configuration of distributed systems, such as clusters, peer-to-peer networks, and distributed databases.



# Atomic Commit in Distributed Database System

- An atomic commit is an operation that applies a set of distinct changes as a single operation.
- If the changes are applied, then the atomic commit is said to have succeeded. If the changes are not applied, then the atomic commit is said to have failed or aborted.
- In distributed database systems, the primary need for atomic commit protocols is to maintain the atomicity of distributed transactions .
- Atomicity is the property that ensures that either all the data changes made by a transaction are committed or none of them are.
- Atomic commit protocols coordinate the distinct operations of a transaction across different database sites and decide whether to commit or abort the transaction  .
- Atomic commit protocols can be classified into two categories: blocking and non-blocking .
- Blocking protocols are those that may block the progress of some transactions if some of the sites participating in the transaction fail .
- Non-blocking protocols are those that guarantee the progress of some transactions even if some of the sites participating in the transaction fail .
- Examples of blocking protocols are two-phase commit (2PC) and three-phase commit (3PC)  .
- Examples of non-blocking protocols are Paxos commit, consensus commit, and FLAC  .
- Blocking protocols are simpler and more efficient than non-blocking protocols in the absence of failures, but they may cause unnecessary aborts or delays in the presence of failures .
- Non-blocking protocols are more resilient and fault-tolerant than blocking protocols, but they may incur more communication and computation overheads .
- Atomic commit protocols can also be integrated with other protocols, such as concurrency control, replication, and recovery, to optimize the performance and reliability of distributed database systems.



## Unit 5 - Distributed Resource Management

- Distributed resource management (DRM) is an evolving discipline consisting of a set of software, hardware, network tools, procedures and policies for enabling distributed enterprise systems to operate effectively in production.
- Distributed enterprise systems are systems that span multiple locations, platforms, and domains, and that require coordination and collaboration among different entities to achieve a common goal.
- DRM aims to optimize the utilization, performance, availability, and security of distributed resources, such as computing, storage, network, data, and energy resources.
- DRM faces various challenges, such as heterogeneity, scalability, dynamism, uncertainty, and complexity of distributed systems, as well as conflicting and changing requirements, preferences, and policies of different stakeholders.
- DRM can be applied to various domains and scenarios, such as cloud computing, grid computing, edge computing, Internet of Things, smart grid, and smart cities.
- DRM can be implemented in a centralized or decentralized manner, depending on the trade-off between control and autonomy, and the communication and coordination overhead.
- DRM involves two main processes: resource discovery and resource scheduling.
  - Resource discovery is the process of finding and selecting suitable resources that match the requirements and preferences of a requestor or a task.
  - Resource scheduling is the process of allocating and managing resources to execute tasks or services, while satisfying the constraints and objectives of the system and the stakeholders.
- DRM can use various techniques and methods, such as optimization, heuristics, machine learning, game theory, multi-agent systems, and blockchain, to achieve efficient and effective resource management.



# Issues in Distributed File Systems

A distributed file system (DFS) is a system that allows multiple clients to access and manipulate files stored on one or more servers over a network. A DFS provides the abstraction of a single, shared namespace for files, regardless of their physical location or the network topology. A DFS can improve the performance, reliability, scalability, and security of file access in a distributed system.

However, designing and implementing a DFS also involves many challenges and trade-offs, such as:

- **Consistency**: How to ensure that all clients see a consistent view of the files and directories, especially when concurrent updates are allowed? How to handle conflicts and resolve inconsistencies when they occur? How to deal with network partitions and failures that may cause temporary or permanent loss of communication between clients and servers?
- **Replication**: How to replicate files and directories across multiple servers for fault tolerance and load balancing? How to maintain the consistency and coherence of replicas? How to handle replication failures and recover from them? How to optimize the replication strategy for different types of files and access patterns?
- **Caching**: How to cache files and directories on the client side for faster access and reduced network traffic? How to maintain the consistency and coherence of caches? How to handle cache misses and evictions? How to optimize the caching strategy for different types of files and access patterns?
- **Security**: How to protect the confidentiality, integrity, and availability of files and directories from unauthorized or malicious access? How to authenticate and authorize clients and servers? How to encrypt and decrypt files and directories? How to audit and monitor file access activities?
- **Performance**: How to optimize the performance of file access in terms of latency, throughput, bandwidth, and resource utilization? How to balance the trade-offs between performance and other design goals, such as consistency, replication, caching, and security? How to adapt to the dynamic changes in the workload, network, and system conditions?
- **Scalability**: How to scale the DFS to support a large number of clients, servers, files, and directories? How to handle the growth and shrinkage of the system? How to distribute the load and balance the workload among servers? How to avoid bottlenecks and hotspots in the system?
- **Usability**: How to provide a user-friendly and intuitive interface for file access? How to support various file types, formats, and semantics? How to support various file operations, such as creation, deletion, renaming, copying, moving, linking, etc.? How to support various file attributes, such as ownership, permissions, timestamps, etc.?
- **Compatibility**: How to interoperate with other file systems and protocols? How to support legacy applications and systems? How to support heterogeneous platforms and devices? How to support cross-domain and cross-organization file sharing?

These are some of the major issues that need to be addressed in the design and use of a DFS. Different DFSs may adopt different solutions and approaches to deal with these issues, depending on their specific requirements, assumptions, and constraints. Therefore, it is important to understand the design principles, architectures, algorithms, and protocols of various DFSs, and compare and evaluate their advantages and disadvantages.



# Mechanism for building distributed file systems

A distributed file system (DFS) is a file system that enables clients to access file storage from multiple hosts through a computer network as if the user was accessing local storage. Files are spread across multiple storage servers and in multiple locations, which enables users to share data and storage resources.

Some of the benefits of using a DFS are:

- Improved availability and reliability: A DFS can tolerate failures of individual servers or network links by replicating or caching data on multiple servers. A DFS can also provide load balancing and fault tolerance by distributing requests among multiple servers.
- Improved performance and scalability: A DFS can improve the access speed and throughput of file operations by distributing the workload among multiple servers and locations. A DFS can also support large amounts of data and users by adding more servers or storage devices as needed.
- Improved transparency and consistency: A DFS can provide a uniform namespace and a consistent view of the file system to the users, regardless of the physical location or organization of the files. A DFS can also ensure the consistency of the file system by using various techniques such as locking, versioning, or quorum.

Some of the challenges of building a DFS are:

- Naming and location: A DFS needs to provide a way to name and locate files across multiple servers and locations, such as using a hierarchical namespace, a flat namespace, or a hash-based namespace. A DFS also needs to handle issues such as name conflicts, name resolution, or name caching.
- Replication and consistency: A DFS needs to provide a way to replicate or cache files across multiple servers and locations, such as using full replication, partial replication, or lazy replication. A DFS also needs to handle issues such as consistency models, update propagation, or concurrency control.
- Security and access control: A DFS needs to provide a way to secure and control the access to files across multiple servers and locations, such as using encryption, authentication, or authorization. A DFS also needs to handle issues such as trust management, access policies, or auditing.

Some of the examples of DFS are:

- NFS (Network File System): A widely used DFS that allows clients to access files on remote servers as if they were local files, using a stateless protocol and a hierarchical namespace.
- HDFS (Hadoop Distributed File System): A DFS that supports large-scale data-intensive applications, using a master-slave architecture and a flat namespace.
- DFS (Distributed File System) Namespaces: A DFS that enables users to group shared folders located on different servers into one or more logically structured namespaces, using a referral mechanism and a hierarchical namespace.



# Design issues in Distributed Shared Memory

Distributed Shared Memory (DSM) is a mechanism that allows multiple processes on different nodes to share a common logical address space and access data transparently. DSM can simplify the programming of distributed systems by hiding the details of inter-process communication and data consistency. However, DSM also introduces several design issues that affect its performance, scalability, and correctness. Some of the main design issues in DSM are:

- **Granularity**: Granularity refers to the size of the unit of sharing and the unit of transfer in a DSM system. A finer granularity (such as a byte or a word) can reduce the amount of data transferred and the false sharing problem, but it can also increase the overhead of coherence maintenance and network communication. A coarser granularity (such as a page or a segment) can reduce the overhead, but it can also increase the amount of data transferred and the false sharing problem. Therefore, choosing an appropriate granularity is a trade-off between communication and computation costs.   

- **Structure**: Structure refers to the organization of the shared data in the memory. The structure can be flat, hierarchical, or object-based. A flat structure treats the shared memory as a single linear address space that can be accessed by any process. A hierarchical structure divides the shared memory into multiple regions that can be mapped to different processes. An object-based structure treats the shared memory as a collection of objects that can be accessed by methods. The structure can affect the ease of programming, the coherence semantics, and the scalability of the DSM system.   

- **Coherence semantics**: Coherence semantics refers to the rules that define the consistency and ordering of the shared data accesses. Different coherence semantics can provide different guarantees and trade-offs for the programmers and the system designers. Some of the common coherence semantics are:

  - **Sequential consistency**: Sequential consistency requires that the result of any execution of a DSM program is the same as if the operations of all the processes were executed in some sequential order, and the operations of each individual process appear in this sequence in the order specified by its program. Sequential consistency is the most intuitive and strongest coherence semantics, but it can also impose high overhead and limit the concurrency and performance of the DSM system.  

  - **Release consistency**: Release consistency relaxes the sequential consistency by allowing different processes to have different views of the shared data until a synchronization operation (such as a lock or a barrier) occurs. Release consistency requires that all the writes performed by a process before a release operation are made visible to all the other processes after an acquire operation. Release consistency can reduce the overhead and increase the concurrency and performance of the DSM system, but it can also complicate the programming and debugging of the DSM applications.  

  - **Weak consistency**: Weak consistency further relaxes the release consistency by allowing different processes to have different views of the shared data even after a synchronization operation. Weak consistency requires that all the writes performed by a process before a synchronization operation are made visible to all the other processes that perform a synchronization operation. Weak consistency can further reduce the overhead and increase the concurrency and performance of the DSM system, but it can also require more explicit synchronization and coordination among the processes.  

- **Scalability**: Scalability refers to the ability of the DSM system to handle the increase in the number of processes, the size of the shared memory, and the frequency of the shared data accesses. Scalability can be affected by several factors, such as the network topology, the coherence protocol, the caching policy, the update policy, the fault tolerance mechanism, and the heterogeneity of the nodes. A scalable DSM system should be able to maintain a reasonable performance and reliability as the system grows in size and complexity.   

- **Heterogeneity**: Heterogeneity refers to the diversity of the nodes in the DSM system in terms of hardware, software, and network characteristics. Heterogeneity can pose several challenges for the DSM system, such as the compatibility of the data formats, the interoperability of the communication protocols, the adaptation of the coherence policies, and the fairness of the resource allocation. A heterogeneous DSM system should be able to support the integration and collaboration of different nodes with minimal overhead and complexity.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on the algorithm for implementation of distributed shared memory for the notes of the Unit 5 - Distributed Resource Management in the subject of DISTRIBUTED SYSTEM.

# Algorithm for Implementation of Distributed Shared Memory

Distributed shared memory (DSM) is a technique that allows multiple processes on different nodes of a distributed system to access a common virtual address space as if they were running on a single machine. DSM can simplify the programming of distributed applications by providing a shared memory abstraction. However, DSM also introduces challenges such as maintaining consistency, coherence, and performance of the shared data.

There are different algorithms for implementing DSM, each with its own advantages and disadvantages. Some of the basic algorithms are:

- **Central Server Algorithm**: In this algorithm, a central server maintains all the shared data and services read and write requests from other nodes. The central server can use a page-based or an object-based approach to manage the shared data. The advantage of this algorithm is that it is simple and ensures consistency and coherence of the shared data. The disadvantage is that it introduces a single point of failure and a bottleneck for communication and computation.

- **Migration Algorithm**: In this algorithm, the shared data is initially stored at the central server, but it can migrate to other nodes upon request. When a node wants to read or write a shared data item, it requests the central server to send the data item to it. The central server then transfers the ownership and the copy of the data item to the requesting node, and invalidates any other copies that may exist. The advantage of this algorithm is that it reduces the communication overhead and improves the locality of the shared data. The disadvantage is that it may cause frequent migrations and inconsistencies if the shared data is accessed by multiple nodes concurrently.

- **Replication Algorithm**: In this algorithm, the shared data is replicated on multiple nodes, and each node can read or write its local copy. The central server keeps track of the locations and versions of the shared data items, and ensures that the copies are coherent and consistent. The advantage of this algorithm is that it enhances the availability and fault-tolerance of the shared data, and reduces the communication latency. The disadvantage is that it increases the storage and synchronization overhead, and may cause stale reads and write conflicts.

- **Invalidation Algorithm**: In this algorithm, the shared data is also replicated on multiple nodes, but each node can only read its local copy. When a node wants to write a shared data item, it requests the central server to invalidate all other copies of the data item, and then writes its local copy. The central server then broadcasts the invalidation message to all other nodes, and updates its version number for the data item. The advantage of this algorithm is that it reduces the write latency and the synchronization overhead. The disadvantage is that it increases the read latency and the communication overhead, and may cause false invalidations and coherence misses.



## Unit 6 - Failure Recovery in Distributed Systems

- In distributed systems, failures are inevitable and can affect the availability, consistency, and performance of the system.
- Failure recovery is the process of restoring the system to a correct and consistent state after a failure occurs.
- Failure recovery techniques can be classified into two categories: backward recovery and forward recovery.
- Backward recovery involves undoing the effects of a failure and restoring the system to a previous consistent state. This can be done by using checkpoints, logging, or rollback.
- Checkpoints are snapshots of the system state taken periodically and stored in stable storage. They can be used to restart the system from a known good state after a failure.
- Logging is the recording of system events and actions in a persistent log. The log can be used to replay or undo the events and actions after a failure.
- Rollback is the process of undoing the effects of a failure by restoring the system state to a previous checkpoint or a consistent point in the log.
- Forward recovery involves masking or tolerating the effects of a failure and continuing the system execution from the current state. This can be done by using redundancy, replication, or fault tolerance.
- Redundancy is the provision of extra resources or components in the system that can take over the functionality of a failed component.
- Replication is the creation and maintenance of multiple copies of the same data or service in the system. Replication can improve availability, consistency, and performance of the system.
- Fault tolerance is the ability of the system to continue functioning correctly in the presence of failures. Fault tolerance can be achieved by using techniques such as consensus, voting, or quorum.



# Concepts in Backward and Forward Recovery

- Backward recovery and forward recovery are two techniques for restoring the system to a consistent state after a failure in a distributed system.
- Backward recovery involves rolling back the system to a previous error-free state by using checkpoints and logs. Forward recovery involves correcting the errors and continuing the execution from the current state.
- The main difference between backward and forward recovery is that backward recovery discards the work done after the error, while forward recovery preserves the work done before and after the error.
- Backward recovery is more general and independent of the nature of faults, but it may incur more overhead and latency. Forward recovery is more efficient and responsive, but it requires accurate assessment and removal of errors.
- Some examples of backward recovery protocols are checkpointing, logging, message logging, and rollback-recovery. Some examples of forward recovery protocols are retry, compensation, and redundancy.



# Recovery in Concurrent Systems

Recovery in concurrent systems is the process of restoring the system to a consistent state after a failure, while preserving the effects of the transactions that were committed before the failure. Recovery in concurrent systems is more complex than in sequential systems, because the system may have multiple transactions executing in parallel, and their operations may be interleaved in the log. Therefore, the recovery system needs to consider the following aspects:

- Interaction with concurrency control: The recovery system depends on the concurrency control system that is used to ensure the serializability and isolation of transactions. For example, if the system uses locking, then the recovery system needs to release the locks held by the aborted transactions and restore the data values to their original state. If the system uses timestamps, then the recovery system needs to discard the operations of the aborted transactions and adjust the timestamps of the surviving transactions.
- Transaction rollback: The recovery system needs to undo the effects of the transactions that were not committed before the failure, and restore the system to a consistent state. This can be done by using the log to backtrack the operations of the aborted transactions, and applying the inverse operations to the data. For example, if the log records that a transaction T wrote a value x to a data item A, then the recovery system needs to read the previous value of A from the log and write it back to A.
- Checkpoints: The recovery system can use checkpoints to reduce the amount of work needed to recover from a failure. A checkpoint is a point in time when the system records the state of the data and the log on a stable storage, such as a disk. After a checkpoint, the recovery system only needs to consider the transactions that started after the checkpoint, and ignore the transactions that were committed before the checkpoint.
- Restart recovery: The recovery system can use restart recovery to handle system failures that affect the entire system, such as a power outage or a disk crash. Restart recovery involves restoring the system state from the most recent checkpoint, and then applying the log to redo the operations of the committed transactions and undo the operations of the aborted transactions. Restart recovery ensures that the system recovers to a consistent and correct state after a system failure.



# Obtaining consistent Checkpoints for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Failure recovery in distributed systems is the process of restoring the system to a consistent and correct state after a failure occurs.
- Failure recovery is essential for fault tolerance, which is the ability of the system to continue functioning despite the presence of errors.
- Failure recovery can be achieved by using checkpoints, which are snapshots of the system state at certain points in time.
- Checkpoints can be used to roll back the system to a previous state in case of a failure, and to resume the execution from that point.
- Checkpoints can be classified into two types: local and global.
  - Local checkpoints are taken by individual processes independently, without any coordination with other processes.
  - Global checkpoints are taken by all processes in the system in a coordinated manner, such that they form a consistent global state.
- A global state is consistent if it does not contain any orphan messages, which are messages that are sent by a process before taking a checkpoint, but are received by another process after taking a checkpoint.
- A global state is also consistent if it does not contain any lost messages, which are messages that are sent by a process after taking a checkpoint, but are lost due to a failure before reaching the destination.
- To obtain consistent global checkpoints, the system can use different algorithms, such as the following :
  - Synchronous checkpointing: All processes take checkpoints simultaneously, after exchanging messages to synchronize their clocks.
  - Asynchronous checkpointing: Each process takes checkpoints independently, without any synchronization with other processes.
  - Coordinated checkpointing: Each process takes checkpoints in a coordinated manner, after receiving a checkpoint request message from a coordinator process.
  - Communication-induced checkpointing: Each process takes checkpoints based on the messages it receives from other processes, using a dependency tracking mechanism.
- The advantages and disadvantages of these algorithms depend on various factors, such as the frequency of checkpoints, the overhead of communication, the storage space required, the number of processes involved, the failure rate, and the recovery time .
- The choice of the checkpointing algorithm should be based on the trade-off between these factors, and the specific requirements and characteristics of the distributed system .



# Recovery in Distributed Database Systems

Recovery in distributed database systems is the process of restoring the database to a consistent and correct state after a failure. A failure can be caused by various factors, such as hardware malfunction, software bugs, network partition, power outage, malicious attacks, or human errors. Recovery is essential to ensure the atomicity and durability of distributed transactions, which are transactions that span multiple sites or nodes in a distributed system.

There are two main types of failures that can affect a distributed database system: soft failures and hard failures.

- Soft failures are temporary and do not cause permanent damage to the database. They can result in inconsistency or incompleteness of the database, such as lost updates, uncommitted changes, or deadlocks. Soft failures can be handled by applying transaction recovery techniques, such as undo or redo, to restore the database to a consistent state. Transaction recovery is based on the use of logs, which record the actions and states of transactions, and checkpoints, which mark the points of consistent states in the logs .
- Hard failures are permanent and cause irreversible damage to the database. They can result in loss or corruption of data, such as disk crashes, site failures, or network failures. Hard failures can be handled by applying system recovery techniques, such as backup and restore, to recover the database from a previous copy. System recovery is based on the use of backups, which store the copies of the database or its parts, and recovery points, which mark the points of consistent backups .

Recovery in distributed database systems is more complicated than in centralized database systems, because failures can occur at different levels and locations, such as communication links, nodes, sites, or regions. Moreover, failures can affect the coordination and communication among the distributed transactions and the distributed database components. Therefore, recovery in distributed database systems requires additional mechanisms and protocols, such as:

- Failure detection and notification, which are used to identify and report the occurrence and type of failures to the relevant components or transactions.
- Failure classification and isolation, which are used to categorize and separate the failed components or transactions from the rest of the system.
- Failure recovery and compensation, which are used to apply the appropriate recovery techniques and actions to the failed components or transactions, and to adjust the effects of the recovery on the rest of the system.

Some of the challenges and issues that arise in recovery in distributed database systems are:

- How to ensure the consistency and correctness of the distributed database and the distributed transactions after a failure and a recovery.
- How to minimize the overhead and performance degradation caused by the recovery techniques and protocols.
- How to maximize the availability and operability of the distributed database and the distributed transactions during and after a failure and a recovery.
- How to avoid or reduce the global rollback or restart of the distributed transactions or the distributed database after a failure and a recovery.



## Unit 7 - Fault Tolerance

- Fault tolerance is the property that enables a system to continue operating properly in the event of the failure of one or more faults within some of its components.
- The objective of creating a fault-tolerant system is to prevent disruptions arising from a single point of failure, ensuring the high availability and business continuity of the system.
- Fault tolerance can be achieved by using various techniques, such as redundancy, replication, backup, failover, recovery, self-healing, etc.
- Fault tolerance can be applied at different levels of a system, such as hardware, software, network, data, etc.
- Fault tolerance can be measured by various metrics, such as reliability, availability, mean time to failure, mean time to repair, etc.
- Fault tolerance can be classified into different types, such as active, passive, hybrid, etc., depending on the degree of redundancy and the mode of operation of the system components.



# Issues in Fault Tolerance for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Fault tolerance is the ability of a system to continue functioning correctly in the presence of failures.
- Fault tolerance is important for distributed systems because they consist of multiple components that may be subject to failures, such as hardware faults, software errors, network congestion, malicious attacks, etc .
- Fault tolerance mechanisms in distributed systems aim to detect, mask, tolerate, or recover from failures, and to maintain the consistency, availability, and reliability of the system .
- Some of the issues in fault tolerance for distributed systems are:
  - How to classify and model different types of faults and failures .
  - How to design and implement fault-tolerant algorithms and protocols that can cope with various failure scenarios .
  - How to measure and evaluate the performance and dependability of fault-tolerant systems .
  - How to balance the trade-offs between fault tolerance and other system properties, such as complexity, scalability, efficiency, security, etc .
  - How to adapt to dynamic and heterogeneous environments, where failures may be unpredictable and diverse .



# Commit Protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Commit protocols are algorithms that ensure the atomicity of distributed transactions, i.e., all the sites involved in a transaction either commit or abort it unanimously, even in the presence of failures.
- Commit protocols are essential for maintaining the consistency and reliability of distributed systems, as they prevent partial execution or data loss due to network or site failures.
- There are different types of commit protocols, such as one-phase, two-phase, and three-phase commit protocols, each with its own advantages and disadvantages.
- One-phase commit protocol (1PC) is the simplest and fastest commit protocol, but it is not fault-tolerant. It involves a coordinator site that sends a commit request to all the participating sites, and waits for their acknowledgments. If all the sites reply with OK, the coordinator commits the transaction and informs the sites. If any site replies with NO or fails to reply, the coordinator aborts the transaction and informs the sites.
- Two-phase commit protocol (2PC) is the most widely used commit protocol, as it is fault-tolerant and ensures atomicity. It involves two phases: voting and decision. In the voting phase, the coordinator site sends a prepare request to all the participating sites, and waits for their votes. If all the sites vote YES, the coordinator moves to the decision phase. If any site votes NO or fails to reply, the coordinator aborts the transaction and informs the sites. In the decision phase, the coordinator site decides whether to commit or abort the transaction based on the votes, and sends the decision to all the sites. The sites then execute the decision and send an acknowledgment to the coordinator .
- Three-phase commit protocol (3PC) is an extension of 2PC that aims to overcome the blocking problem of 2PC, i.e., the possibility of some sites waiting indefinitely for the coordinator's decision in case of failures. It involves three phases: prepare, pre-commit, and commit/abort. In the prepare phase, the steps are the same as in 2PC. In the pre-commit phase, the coordinator site sends an enter prepared state message to all the sites that voted YES, and waits for their OKs. If all the sites reply with OK, the coordinator moves to the commit/abort phase. If any site fails to reply, the coordinator aborts the transaction and informs the sites. In the commit/abort phase, the coordinator site decides whether to commit or abort the transaction based on the OKs, and sends the decision to all the sites. The sites then execute the decision and send an acknowledgment to the coordinator.



# Voting protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Voting protocols are a type of consensus protocols that allow a set of distributed nodes to agree on a common value or decision, despite the presence of faults or attacks in the system    .
- Voting protocols are based on the idea of collecting votes from a majority or a quorum of nodes, and choosing the value that has the most votes as the consensus value    .
- Voting protocols can be classified into two categories: exact voting and inexact voting .
  - Exact voting requires that all nodes agree on the same value, and that the value is correct and consistent with the initial inputs of the nodes .
  - Inexact voting allows some degree of divergence or approximation in the consensus value, as long as it satisfies some quality criteria or constraints .
- Voting protocols can also be distinguished by the number of rounds or phases they use to reach consensus  .
  - One-phase voting protocols collect and count the votes in a single round, and do not require any confirmation or acknowledgement from the nodes .
  - Two-phase voting protocols use a first round to collect the votes, and a second round to confirm or abort the consensus value, depending on the agreement of the nodes  .
  - Multi-phase voting protocols use more than two rounds to iteratively refine or update the consensus value, until a termination condition is met .
- Voting protocols can also be characterized by the level of security or fault-tolerance they provide   .
  - Secure voting protocols aim to protect the voting process from malicious attacks, such as tampering, impersonation, denial-of-service, or collusion   .
  - Fault-tolerant voting protocols aim to cope with benign faults, such as crashes, failures, or errors, that may affect the availability or correctness of the nodes   .
  - Some voting protocols combine both security and fault-tolerance features, by using cryptographic techniques, redundancy, or verification mechanisms   .
- Voting protocols can also be influenced by the properties or assumptions of the distributed system, such as the network topology, the communication model, the node heterogeneity, or the synchrony    .
  - Some voting protocols assume a fully connected or a partially connected network, where nodes can communicate directly or indirectly with each other    .
  - Some voting protocols assume a reliable or an unreliable communication model, where messages can be lost, delayed, duplicated, or reordered    .
  - Some voting protocols assume a homogeneous or a heterogeneous network, where nodes may have different levels of reputation, weight, or computational power .
  - Some voting protocols assume a synchronous or an asynchronous system, where nodes may have different speeds, clocks, or timeouts    .
- Voting protocols can also be evaluated by the performance or the quality metrics they achieve, such as the latency, the throughput, the scalability, the resilience, or the fairness    .
  - Latency measures the time it takes for a voting protocol to reach consensus, from the start of the voting process to the end    .
  - Throughput measures the number of consensus values that a voting protocol can produce per unit of time[^1



# Dynamic voting protocols

- Dynamic voting protocols are techniques for consistency and recovery control of replicated files in distributed systems  .
- The purpose of a replicated file is to improve the availability of a logical file in the presence of site failures and network partitions  .
- A dynamic voting protocol assigns a number of votes to each replica of a file, and requires a majority of votes to access or update the file   .
- The number of votes assigned to each replica can change dynamically depending on the system state, such as the number of active replicas, the network connectivity, and the access pattern   .
- A dynamic voting protocol can achieve the following objectives   :
  - Maintain the consistency of replicated files by ensuring that only one group of replicas can access or update the file at a time.
  - Maximize the availability of replicated files by allowing access or update even when some replicas or links are faulty or unreachable.
  - Minimize the communication overhead by reducing the number of messages and votes required for each access or update operation.
  - Adapt to the changing system state by reassigning votes to balance the load and improve the performance.
- Some examples of dynamic voting protocols are     :
  - The dynamic weighted voting scheme, which assigns votes to replicas based on their availability and reliability  .
  - The topological dynamic voting algorithm, which assigns votes to replicas based on their network proximity and connectivity.
  - The quorum-based voting scheme, which assigns votes to replicas based on their membership in a quorum, which is a subset of replicas that can reach a consensus.
  - The protocols for dynamic vote reassignment, which reassign votes to replicas based on their failure or recovery events.



# Unit 8 - Transactions and Concurrency Control

## Transactions
- A transaction is a logical unit of work that consists of a sequence of operations on a database.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the operations of a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction does not interfere with other concurrent transactions.
- Durability means that the effects of a committed transaction are permanent and survive any system failures.

## Concurrency Control
- Concurrency control is the management of simultaneously executing transactions in a shared database.
- Concurrency control ensures that correct results for concurrent operations are generated while getting those results as quickly as possible.
- Concurrency control also keeps each transaction isolated as it is executed which helps data remain consistent even after the transaction ends especially in multi-user systems.
- Concurrency control can be implemented using various techniques, such as locking, timestamping, validation, and multiversioning.
- Locking is a technique where a transaction acquires a lock on a data item before reading or writing it, and releases the lock after finishing the operation.
- Timestamping is a technique where a transaction is assigned a unique timestamp when it starts, and the order of conflicting operations is determined by the timestamps.
- Validation is a technique where a transaction is executed without any locks, but is validated before committing to ensure that it does not violate any consistency rules.
- Multiversioning is a technique where a transaction operates on a snapshot of the database taken at a certain point in time, and the changes are merged with the current database state after committing.



# Transactions

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the operations in a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction does not interfere with other concurrent transactions.
- Durability means that the effects of a committed transaction are permanent and survive failures.

# Distributed Transactions

- A distributed transaction is a transaction that spans multiple data servers in a distributed database system.
- A distributed transaction consists of a set of subtransactions, each of which is executed by one data server.
- A distributed transaction coordinator (DTC) is a component that manages the execution and coordination of distributed transactions.
- A distributed transaction has two phases: prepare and commit.
- In the prepare phase, the DTC sends a prepare message to each data server involved in the transaction, asking them to vote on whether they are ready to commit or abort the transaction.
- In the commit phase, the DTC collects the votes from the data servers and decides whether to commit or abort the transaction. If all the data servers vote to commit, the DTC sends a commit message to each data server, asking them to make the changes permanent. If any data server votes to abort, the DTC sends an abort message to each data server, asking them to undo the changes.

# Distributed Concurrency Control

- Distributed concurrency control is the concurrency control of a system distributed over a computer network.
- Distributed concurrency control provides a mechanism to synchronize distributed transactions in such a way that the ACID properties are not violated by their interleaved execution.
- Distributed concurrency control makes sure that all subtransactions of a set of distributed transactions are serialized identically in all data servers involved.
- Distributed concurrency control can be classified into two categories: pessimistic and optimistic.
- Pessimistic concurrency control assumes that conflicts are likely to occur and prevents them by locking the data items accessed by a transaction until it commits or aborts.
- Optimistic concurrency control assumes that conflicts are rare and detects them by validating the read and write sets of a transaction before it commits.
- Some common distributed concurrency control protocols are two-phase locking (2PL), timestamp ordering (TO), and optimistic concurrency control (OCC).



# Nested transactions for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A transaction is a unit of work that accesses and possibly modifies data in a database or a system.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- A distributed transaction is a transaction that accesses data from multiple servers or systems that are connected by a network.
- A nested transaction is a transaction that contains other transactions as subtransactions.
- A nested transaction can be used to improve the performance, modularity, and fault tolerance of distributed transactions.
- A nested transaction has the following characteristics:
  - It has a parent transaction and zero or more child transactions.
  - It inherits the ACID properties from its parent transaction.
  - It can commit or abort independently of its parent or child transactions.
  - It can be partially committed, meaning that some of its subtransactions are committed and some are aborted.
  - It can be flattened, meaning that it is treated as a single transaction by the system.
- A nested transaction can be classified into two types: closed nested transactions and open nested transactions.
- A closed nested transaction is a nested transaction that does not allow any communication or interaction between its subtransactions and the outside world until it commits or aborts.
- A closed nested transaction has the following advantages and disadvantages:
  - It preserves the serializability and recoverability of the transactions.
  - It simplifies the concurrency control and deadlock detection mechanisms.
  - It reduces the network overhead and the number of messages exchanged.
  - It limits the parallelism and concurrency of the subtransactions.
  - It increases the locking time and the risk of blocking or aborting other transactions.
  - It requires a two-phase commit protocol to coordinate the commit or abort of the subtransactions.
- An open nested transaction is a nested transaction that allows some communication or interaction between its subtransactions and the outside world before it commits or aborts.
- An open nested transaction has the following advantages and disadvantages:
  - It increases the parallelism and concurrency of the subtransactions.
  - It reduces the locking time and the risk of blocking or aborting other transactions.
  - It allows the subtransactions to access external resources or services.
  - It violates the serializability and recoverability of the transactions.
  - It complicates the concurrency control and deadlock detection mechanisms.
  - It increases the network overhead and the number of messages exchanged.
  - It requires a compensation mechanism to undo the effects of the subtransactions in case of abort.



# Locks for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A **lock** is a variable associated with a data item that determines whether read/write operations can be performed on that data item .
- A lock can have different modes, such as **shared** (S), **exclusive** (X), **update** (U), **intention shared** (IS), **intention exclusive** (IX), etc.
- A lock **compatibility matrix** is used to state whether a data item can be locked by two transactions at the same time.
- A lock **manager** is a component of the distributed system that grants or denies lock requests from transactions.
- A lock **protocol** is a set of rules that governs how transactions acquire and release locks on data items.
- Lock protocols can be classified into **binary** (two-phase) or **generalized** (multi-phase) locking.
- Binary locking protocols require transactions to follow two phases: a **growing** phase, where locks can be acquired but not released, and a **shrinking** phase, where locks can be released but not acquired.
- Generalized locking protocols allow transactions to acquire and release locks in any order, as long as they do not violate the **conflict serializability** property.
- Lock protocols can also be classified into **centralized**, **primary copy**, **majority consensus**, or **distributed** locking, depending on how the lock manager is implemented.
- Centralized locking protocols use a single lock manager for the entire distributed system, which can be a bottleneck or a single point of failure.
- Primary copy locking protocols use a designated lock manager for each data item, which can be the primary copy holder or a separate node.
- Majority consensus locking protocols use a quorum of lock managers for each data item, which can improve availability and fault tolerance.
- Distributed locking protocols use a network of lock managers for each data item, which can reduce communication overhead and increase concurrency.
- Lock protocols can also be classified into **pessimistic** or **optimistic** concurrency control, depending on how they handle conflicts among transactions.
- Pessimistic concurrency control protocols use locks to prevent conflicts from occurring, which can reduce aborts but also reduce concurrency.
- Optimistic concurrency control protocols use timestamps or validation to detect and resolve conflicts after they occur, which can increase concurrency but also increase aborts.
- Lock protocols can also be classified into **static** or **dynamic**, depending on how they handle changes in the data items or the transactions.
- Static lock protocols use a fixed set of locks for each data item or transaction, which can simplify the lock management but also limit the flexibility.
- Dynamic lock protocols use a variable set of locks for each data item or transaction, which can adapt to the changing needs but also increase the complexity.
- Lock protocols can also be classified into **conservative** or **aggressive**, depending on how they handle deadlock situations.
- Conservative lock protocols use a **pre-claiming** strategy, where transactions request all the locks they need before starting, which can avoid deadlocks but also waste resources.
- Aggressive lock protocols use a **wait-die** or **wound-wait** strategy, where transactions wait for or abort other transactions based on their timestamps, which can resolve deadlocks but also increase overhead.
- Lock protocols can also be classified into **flat** or **hierarchical**, depending on how they handle nested or sub-transactions.
- Flat lock protocols treat nested or sub-transactions as independent transactions, which can simplify the lock management but also increase the conflicts.
- Hierarchical lock protocols use a **tree** or **graph** structure to represent the nesting or subordination of transactions, which can reduce the conflicts but also increase the complexity.



# Optimistic Concurrency Control

- Optimistic concurrency control (OCC) is a concurrency control method applied to transactional systems such as relational database management systems and software transactional memory.
- OCC assumes that multiple transactions can frequently complete without interfering with each other, and does not require locking or timestamping techniques to prevent conflicts .
- Instead, a transaction is executed without restrictions until it is committed, and then it is validated to ensure that no conflicts have occurred with other concurrent transactions.
- If a conflict is detected, the transaction is aborted and restarted, possibly with some backoff or priority adjustment mechanism to reduce the likelihood of further conflicts .
- OCC has the advantage of allowing a high degree of concurrency and avoiding the overhead of locking or timestamping, but it also has the drawback of wasting resources and increasing latency when conflicts are frequent and transactions have to be restarted .
- OCC can be implemented in a centralized or distributed manner, depending on the architecture of the transactional system .
- In a centralized system, there is a single validation server that checks the read and write sets of each transaction and decides whether to commit or abort it.
- In a distributed system, there are multiple validation servers that communicate with each other to detect and resolve conflicts among transactions that access data stored in different sites.
- OCC can be further classified into different variants based on the validation phase, such as basic OCC, forward validation, backward validation, and hybrid validation.
- Each variant has different trade-offs in terms of concurrency, complexity, and performance.



# Timestamp ordering

Timestamp ordering is a technique for ensuring serializability of transactions in a distributed system. It assigns a unique timestamp to each transaction and uses it to order the execution of conflicting operations. The main idea is that a transaction should not read or write data that has been or will be modified by another transaction with a different timestamp.

## Lamport timestamps

Lamport timestamps are a type of logical clocks that define a partial order over events in a distributed system. They are based on the principle of causality: if an event A causes or influences another event B, then the timestamp of A should be less than the timestamp of B. Lamport timestamps are generated by the following rules:

- Each node in the system maintains a local counter that is incremented after each event.
- When a node sends a message, it attaches its current counter value as the timestamp of the message.
- When a node receives a message, it updates its counter to be the maximum of its own value and the timestamp of the message, plus one.
- The timestamp of an event is the value of the counter when the event occurs.

## Timestamp ordering algorithm

The timestamp ordering algorithm uses Lamport timestamps to order the execution of read and write operations on data items in a distributed system. The algorithm assumes that each data item has a read timestamp (RTS) and a write timestamp (WTS) that record the latest timestamps of read and write operations on that item. The algorithm works as follows:

- When a transaction T wants to read a data item X, it sends a read request with its timestamp TS(T) to the node that stores X.
- The node that stores X checks if TS(T) is greater than or equal to WTS(X). If yes, it grants the read permission and updates RTS(X) to be the maximum of RTS(X) and TS(T). If no, it aborts the transaction T and sends a negative reply.
- When a transaction T wants to write a data item X, it sends a write request with its timestamp TS(T) to the node that stores X.
- The node that stores X checks if TS(T) is greater than both RTS(X) and WTS(X). If yes, it grants the write permission and updates WTS(X) to be TS(T). If no, it aborts the transaction T and sends a negative reply.

The timestamp ordering algorithm ensures that conflicting operations are executed in the order of their timestamps, which reflects the causal order of events in the system. This guarantees serializability of transactions and prevents anomalies such as lost updates, dirty reads, and inconsistent reads. However, the algorithm may also abort some transactions that are not actually conflicting, which reduces the concurrency and throughput of the system. Moreover, the algorithm relies on the assumption that the timestamps are unique and monotonically increasing, which may not be true in some scenarios. Therefore, some variations and extensions of the algorithm have been proposed to address these issues, such as using vector clocks, synchronized clocks, or hybrid clocks.



# Comparison of methods for concurrency control

Concurrency control is the process of managing the simultaneous execution of transactions in a distributed system, such that the consistency and correctness of the data are preserved. There are various methods for concurrency control, each with its own advantages and disadvantages. Some of the common methods are:

- **Two-phase locking (2PL)**: This method requires each transaction to acquire locks on the data items it needs to access, and release them when it is done. There are two phases: the growing phase, where the transaction can only acquire locks, and the shrinking phase, where the transaction can only release locks. The transaction must hold all the locks until it commits or aborts. This method ensures serializability, which means the concurrent execution of transactions is equivalent to some serial execution. However, it may cause deadlock, where two or more transactions are waiting for each other to release locks, and starvation, where some transactions are delayed indefinitely due to lock contention.  

- **Timestamp ordering (TO)**: This method assigns a unique timestamp to each transaction, and uses it to order the transactions. Each data item has two timestamps: the read timestamp (RTS), which records the timestamp of the last transaction that read the item, and the write timestamp (WTS), which records the timestamp of the last transaction that wrote the item. A transaction can read or write a data item only if its timestamp is compatible with the timestamps of the item, otherwise it is aborted and restarted with a new timestamp. This method avoids deadlock, but may cause more aborts and restarts than 2PL.  

- **Multi-version concurrency control (MVCC)**: This method allows multiple versions of the same data item to coexist, and assigns a timestamp to each version. A transaction can read the latest version of a data item that is older than or equal to its timestamp, and can write a new version of a data item only if its timestamp is greater than the timestamp of the current version. This method allows more concurrency than 2PL and TO, as readers do not block writers and vice versa. However, it requires more storage space and garbage collection to manage the versions.  

- **Validation concurrency control (VCC)**: This method divides the execution of a transaction into three phases: the read phase, where the transaction reads the data items and stores them in a private workspace, the validation phase, where the transaction checks if it can commit without violating serializability, and the write phase, where the transaction writes the updated data items to the database. The validation phase uses a validation test, such as the precedence graph test or the serial validation test, to determine if the transaction can commit. This method avoids locking and deadlock, but may cause more aborts and restarts than 2PL.  

The choice of the concurrency control method depends on the characteristics of the distributed system, such as the network latency, the communication cost, the degree of data replication, the transaction workload, and the performance requirements.



## Unit 9 - Distributed Transactions

- A distributed transaction is a type of transaction that involves two or more network hosts, usually providing transactional resources, such as databases, message queues, file systems, etc.   
- A distributed transaction is coordinated by a transaction manager, which is responsible for creating and managing a global transaction that encompasses all the operations against the transactional resources.  
- A distributed transaction requires the following properties to ensure data consistency and reliability: atomicity, consistency, isolation, and durability (ACID). 
- Atomicity means that either all the operations in a distributed transaction are executed successfully, or none of them are. If any operation fails, the transaction manager should roll back the changes made by the previous operations. 
- Consistency means that the distributed transaction should preserve the integrity constraints and business rules of the data. The transaction manager should ensure that the data is in a valid state before and after the transaction. 
- Isolation means that the distributed transaction should not interfere with other concurrent transactions. The transaction manager should prevent the data from being accessed or modified by other transactions until the current transaction is committed or aborted. 
- Durability means that the effects of a committed distributed transaction should be permanent and survive any system failures. The transaction manager should ensure that the data is written to persistent storage and can be recovered in case of a crash. 
- A distributed transaction can be implemented using different protocols, such as two-phase commit (2PC), three-phase commit (3PC), or the saga pattern. Each protocol has its own advantages and disadvantages in terms of performance, availability, and fault tolerance.  
- Two-phase commit (2PC) is a protocol that involves two phases: prepare and commit. In the prepare phase, the transaction manager asks each transactional resource to vote on whether they are ready to commit or abort the transaction. If all the resources vote yes, the transaction manager proceeds to the commit phase, where it instructs each resource to commit the changes. If any resource votes no, the transaction manager aborts the transaction and tells each resource to roll back the changes.  
- Three-phase commit (3PC) is a protocol that involves three phases: prepare, pre-commit, and commit. In the prepare phase, the transaction manager asks each transactional resource to vote on whether they are ready to commit or abort the transaction. If all the resources vote yes, the transaction manager proceeds to the pre-commit phase, where it tells each resource to prepare to commit the changes. If any resource votes no, the transaction manager aborts the transaction and tells each resource to roll back the changes. In the pre-commit phase, the transaction manager waits for an acknowledgement from each resource that they are prepared to commit. If all the resources acknowledge, the transaction manager proceeds to the commit phase, where it instructs each resource to commit the changes. If any resource fails to acknowledge, the transaction manager aborts the transaction and tells each resource to roll back the changes.  
- The saga pattern is a protocol that involves a sequence of compensating actions. A compensating action is an operation that reverses the effect of a previous operation. In the saga pattern, each operation in a distributed transaction is followed by a compensating action that can be executed in case of a failure. If the transaction succeeds, the compensating actions are discarded. If the transaction fails, the compensating actions are executed in reverse order to undo the changes made by the previous operations.



# Flat and Nested Distributed Transactions

## Introduction

- A **transaction** is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction has four properties: **atomicity**, **consistency**, **isolation**, and **durability** (ACID).
- A **flat or nested transaction** that accesses objects handled by different servers is referred to as a **distributed transaction**.
- When a distributed transaction reaches its end, in order to maintain the atomicity property of the transaction, it is mandatory that all of the servers involved in the transaction either **commit** the transaction or **abort** it.
- Distributed transactions can be structured in two different ways: **flat transactions** and **nested transactions**.

## Flat Transactions

- A **flat transaction** has a single initiating point (**Begin**) and a single end point (**Commit** or **Abort**) .
- They are usually very simple and are generally used for short activities rather than larger ones .
- A flat transaction can be coordinated by a **two-phase commit protocol** (2PC) or a **three-phase commit protocol** (3PC) .
- The 2PC protocol consists of two phases: a **voting phase** and a **decision phase** .
- In the voting phase, the **coordinator** (the server that initiates the transaction) sends a **prepare** message to all the **participants** (the servers that execute the transaction) and waits for their replies .
- The participants execute the transaction and send either a **yes** vote (if they are ready to commit) or a **no** vote (if they want to abort) to the coordinator .
- In the decision phase, the coordinator decides whether to commit or abort the transaction based on the votes received .
- If the coordinator receives a yes vote from all the participants, it sends a **commit** message to all of them and commits the transaction .
- If the coordinator receives a no vote from any participant, it sends an **abort** message to all of them and aborts the transaction .
- The 3PC protocol is an extension of the 2PC protocol that adds a third phase: a **pre-commit phase** .
- The pre-commit phase is used to avoid blocking in case of failures .
- In the pre-commit phase, the coordinator sends a **pre-commit** message to all the participants after receiving a yes vote from all of them in the voting phase .
- The participants acknowledge the pre-commit message and wait for the final decision from the coordinator .
- In the final decision phase, the coordinator sends either a **commit** or an **abort** message to all the participants based on the outcome of the pre-commit phase .
- If the coordinator receives an acknowledgment from all the participants in the pre-commit phase, it sends a commit message and commits the transaction .
- If the coordinator fails to receive an acknowledgment from any participant in the pre-commit phase, it sends an abort message and aborts the transaction .

## Nested Transactions

- A **nested transaction** is a transaction that contains other transactions as subtransactions .
- A nested transaction has a **root transaction** that initiates the nested transaction and a set of **subtransactions** that are executed by the root transaction or by other subtransactions .
- A nested transaction can be represented by a **transaction tree**, where the nodes are transactions and the edges are parent-child relationships .
- A nested transaction can be coordinated by a **sagas protocol** or a **nested two-phase commit protocol** (N2PC) .
- The sagas protocol is based on the idea of **compensating actions** .
- A compensating action is an action that undoes the effect of a previous action .
- For example, if a subtransaction books a flight, the compensating action is to cancel the flight .
- The sagas protocol works as follows :
  - The root transaction executes the subtransactions in a sequential order and records their compensating actions.
  - If a subtransaction commits successfully, the root transaction proceeds to the next subtransaction.
  - If a subtransaction aborts, the root transaction aborts and executes



# Atomic Commit Protocols for Distributed Transactions

- A distributed transaction is a transaction that involves multiple servers or nodes in a distributed system. A distributed transaction needs to ensure the ACID properties, especially the atomicity property, which means that either all the operations in the transaction are executed successfully, or none of them are executed at all.
- An atomic commit protocol is a protocol that coordinates the nodes in a distributed system to reach a consensus on whether to commit or abort a distributed transaction, even in the presence of failures or network partitions. An atomic commit protocol guarantees that all the nodes agree on the same outcome and that no partial commits or aborts occur.
- There are different types of atomic commit protocols, such as two-phase commit (2PC), three-phase commit (3PC), parallel commit, and failure-aware commit. Each protocol has its own advantages and disadvantages in terms of performance, availability, and fault tolerance.
- Two-phase commit (2PC) is the most widely used atomic commit protocol. It consists of two phases: a prepare phase and a commit phase. In the prepare phase, a coordinator node sends a prepare message to all the participant nodes, asking them to vote on whether they are ready to commit or not. Each participant node replies with a yes or no vote. If all the votes are yes, the coordinator node sends a commit message to all the participants, instructing them to commit the transaction. If any vote is no, or if the coordinator does not receive all the votes within a timeout, the coordinator sends an abort message to all the participants, instructing them to abort the transaction. 2PC ensures atomicity, but it has some drawbacks, such as blocking, single point of failure, and vulnerability to network partitions.
- Three-phase commit (3PC) is an extension of 2PC that adds a pre-commit phase between the prepare and commit phases. In the pre-commit phase, the coordinator node sends a pre-commit message to all the participants, indicating that all the votes are yes and that the transaction will be committed. The participants acknowledge the pre-commit message and wait for the final commit message. The commit phase is the same as in 2PC. 3PC reduces the blocking problem of 2PC, but it introduces more messages and latency, and it still has a single point of failure and is vulnerable to network partitions.
- Parallel commit is a new atomic commit protocol that aims to reduce the latency of distributed transactions to a single round-trip of distributed consensus. It leverages the concept of transaction records, which are immutable and durable records that store the transaction's status and dependencies. A transaction can be committed if and only if all its dependencies are committed. In parallel commit, a transaction is divided into two stages: a staging stage and a committing stage. In the staging stage, the transaction writes its transaction record to a distributed consensus system, such as Raft or Paxos, and waits for the record to be replicated to a majority of the nodes. In the committing stage, the transaction reads the transaction records of its dependencies and determines whether it can commit or not. If it can commit, it writes its final value to the database. If it cannot commit, it aborts. Parallel commit reduces the latency of distributed transactions, but it requires a reliable and fast distributed consensus system and a mechanism to track and resolve transaction dependencies.
- Failure-aware commit (FLAC) is a practical atomic commit protocol that is aware of the failure status of the nodes and adapts the commit protocol accordingly. It uses a two-phase transaction processing framework, similar to 2PC, but it adds a failure detection and recovery mechanism that allows the nodes to switch between different commit protocols depending on the failure scenario. FLAC supports four commit protocols: 2PC, 3PC, Paxos commit, and fast commit. Paxos commit is a variant of 2PC that uses Paxos to elect a new coordinator in case of a coordinator failure. Fast commit is a variant of 2PC that skips the prepare phase and directly sends a commit message to the participants, assuming that they are all ready to commit. FLAC dynamically selects the best commit protocol for each transaction based on the failure status of the nodes, the transaction size, and the network latency. FLAC improves the performance and availability of distributed transactions, but it requires a failure detection and recovery mechanism and a protocol selection algorithm.



# Concurrency control in distributed transactions

- Concurrency control is the process of managing the concurrent execution of transactions in a distributed database system, such that the ACID properties are preserved.
- Concurrency control aims to ensure the correctness and consistency of the database state, while allowing a high degree of concurrency and performance.
- Concurrency control can be classified into two main categories: pessimistic and optimistic.
  - Pessimistic concurrency control assumes that conflicts are likely to occur and uses locking mechanisms to prevent them. Locking protocols can be centralized, decentralized, or hierarchical, depending on the location and authority of the lock manager .
  - Optimistic concurrency control assumes that conflicts are rare and allows transactions to execute without locking. Conflicts are detected at the end of the transaction and resolved by aborting and restarting some transactions. Optimistic protocols can be based on timestamps, validation, or multiversioning .
- Concurrency control in distributed transactions faces some additional challenges, such as network delays, communication failures, partial failures, and distributed deadlock detection and resolution .
- Some of the techniques and algorithms used for concurrency control in distributed transactions are  :
  - Two-phase locking (2PL): a locking protocol that requires each transaction to acquire all the locks it needs before releasing any lock. 2PL ensures serializability, but may cause deadlocks and reduce concurrency.
  - Two-phase commit (2PC): a commit protocol that ensures atomicity of distributed transactions by coordinating the commit or abort decision among all the participating sites. 2PC consists of a prepare phase and a commit phase, and requires a coordinator site and a reliable communication network.
  - Three-phase commit (3PC): a commit protocol that improves the availability and fault-tolerance of 2PC by introducing a pre-commit phase and allowing some sites to commit independently of others. 3PC reduces the blocking time and the possibility of inconsistent decisions, but increases the message overhead and the latency.
  - Timestamp ordering (TO): a concurrency control protocol that assigns a unique timestamp to each transaction and orders the execution of conflicting operations according to their timestamps. TO ensures serializability and avoids deadlocks, but may cause cascading aborts and waste of resources.
  - Basic timestamp ordering (BTO): a variant of TO that assigns timestamps to operations instead of transactions, and uses wound-wait or wait-die schemes to resolve conflicts. BTO reduces the abort rate and the blocking time, but increases the complexity and the overhead of timestamp management.
  - Optimistic concurrency control (OCC): a concurrency control protocol that allows transactions to execute without locking and validates their correctness at the end. OCC consists of three phases: read, validation, and write. OCC avoids deadlocks and reduces blocking time, but may cause high abort rate and validation overhead.
  - Multiversion concurrency control (MVCC): a concurrency control protocol that maintains multiple versions of each data item and assigns them to transactions based on their timestamps. MVCC allows read-only transactions to access older versions of data without locking, and reduces the conflict rate and the abort rate. MVCC requires additional storage space and garbage collection mechanisms.
  - 2PC*: a distributed transaction control protocol that can extract more concurrent processing capabilities under high-intensity competitive workloads than previous approaches for a multi-microservice. 2PC* is an optimized protocol based on the traditional 2PC, that uses a pre-locking mechanism and a dynamic timeout adjustment mechanism to reduce the blocking time and the abort rate.



# Distributed Deadlocks

- A **distributed deadlock** is a situation where a set of processes in a distributed system are waiting for each other to release resources or messages, and none of them can proceed  .
- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems .
- Distributed deadlocks are harder to detect, avoid, and prevent than deadlocks in centralized systems, because there is no single authority that can oversee resource allocation and monitor the state of the system.
- There are different types of distributed deadlocks, depending on the nature of the resources or messages involved:
  - **Communication deadlocks**: occur when processes are waiting for messages from each other that will never arrive.
  - **Resource deadlocks**: occur when processes are holding some resources and requesting others that are held by other processes.
  - **Hybrid deadlocks**: occur when both communication and resource deadlocks are present in the system.
- There are different approaches to handle distributed deadlocks :
  - **Deadlock prevention**: aims to ensure that the system never enters a deadlock state by imposing some constraints on resource allocation or message passing.
  - **Deadlock avoidance**: aims to ensure that the system does not enter a deadlock state by making informed decisions based on the current and future requests and availability of resources or messages.
  - **Deadlock detection**: aims to identify and resolve deadlock situations after they have occurred by using some algorithms or techniques.
  - **Deadlock ignorance**: ignores the possibility of deadlocks and assumes that they will not occur or will not affect the system performance significantly.



# Transaction recovery for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A distributed transaction is a transaction that spans multiple sites or nodes in a distributed system.
- A distributed transaction system must ensure the ACID properties of transactions: atomicity, consistency, isolation, and durability.
- Atomicity means that either all the operations of a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction does not interfere with other concurrent transactions.
- Durability means that the effects of a committed transaction are permanent and survive failures.

- Transaction recovery is the process of restoring the database to a consistent state after a failure or an abort.
- Transaction recovery is essential for maintaining the atomicity and durability properties of transactions.
- Transaction recovery in a distributed system is more complex than in a centralized system because of the following challenges:
  - Communication failures: A site may not be able to communicate with other sites due to network problems or partitioning.
  - Site failures: A site may crash or become unavailable due to hardware or software faults.
  - Distributed commit: A distributed transaction must ensure that all the sites involved agree on the outcome of the transaction (commit or abort).
  - Distributed concurrency control: A distributed transaction must coordinate with other transactions to ensure the isolation property.

- Transaction recovery in a distributed system relies on the following techniques:
  - Logging: A log is a record of the operations performed by a transaction and their effects on the database. A log is used to undo or redo the operations of a transaction in case of a failure or an abort. A log can be stored locally at each site or globally at a coordinator site.
  - Checkpointing: A checkpoint is a point in time when the database is consistent and all the log records have been written to stable storage. A checkpoint reduces the amount of work needed for recovery by limiting the number of transactions that need to be examined or redone.
  - Two-phase commit protocol: A two-phase commit protocol is a protocol that ensures that all the sites involved in a distributed transaction agree on the outcome of the transaction. The protocol consists of two phases: a prepare phase and a commit phase. In the prepare phase, the coordinator site asks all the participant sites to vote on whether they are ready to commit or abort the transaction. In the commit phase, the coordinator site decides on the final outcome based on the votes and informs all the participant sites to commit or abort accordingly.
  - Shadow versions: A shadow version is a copy of a data item that is created by a transaction before modifying it. A shadow version is used to restore the original value of the data item in case of an abort. A shadow version can be stored locally at each site or globally at a coordinator site.



## Unit 10 - Replication

- Replication is the process of creating and maintaining multiple copies of the same data on different database servers.
- Replication provides benefits such as high availability, fault tolerance, load balancing, and scalability.
- Replication can be classified into two types: synchronous and asynchronous.
  - Synchronous replication ensures that all copies of the data are updated at the same time, but it may incur performance overhead and network latency.
  - Asynchronous replication allows updates to be applied to different copies of the data at different times, but it may introduce data inconsistency and conflict resolution issues.
- Replication can be implemented using different architectures, such as master-slave, peer-to-peer, multi-master, and hybrid.
  - Master-slave replication involves one primary server (master) that receives all the updates and propagates them to one or more secondary servers (slaves) that are read-only.
  - Peer-to-peer replication involves multiple servers that can receive and send updates to each other, and each server maintains a full copy of the data.
  - Multi-master replication involves multiple servers that can receive and send updates to each other, but each server maintains only a partial copy of the data (a subset of tables or rows).
  - Hybrid replication involves a combination of different replication architectures, such as master-slave and peer-to-peer, to achieve different objectives.
- Replication can be configured using different parameters, such as replication scope, replication frequency, replication mode, replication filter, and conflict resolution.
  - Replication scope defines what data is replicated, such as the entire database, a specific schema, a specific table, or a specific column.
  - Replication frequency defines how often the data is replicated, such as continuously, periodically, or on demand.
  - Replication mode defines how the data is replicated, such as full, incremental, or differential.
    - Full replication copies the entire data set from the source to the destination.
    - Incremental replication copies only the changes that have occurred since the last replication.
    - Differential replication copies only the changes that have occurred since the last full replication.
  - Replication filter defines what data is excluded from replication, such as certain rows, columns, or transactions.
  - Conflict resolution defines how to handle data conflicts that may arise due to concurrent updates, such as using timestamps, version numbers, or custom logic.



# System model and group communication for replication in distributed systems

- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by passing messages .
- Replication is a technique to improve the availability, performance, and fault tolerance of a distributed system by creating and maintaining multiple copies of data or services .
- A system model is a set of assumptions and properties that describe the behavior and characteristics of a distributed system, such as the communication model, the failure model, the timing model, and the security model .
- Group communication is a form of communication between multiple processes in a distributed system that share some common interest or goal, such as replicating data or coordinating actions .
- Group communication can be classified into two types: broadcast communication and multicast communication .
  - Broadcast communication is when a source process sends a message to all other processes in the system, regardless of their group membership or interest .
  - Multicast communication is when a source process sends a message to a subset of processes in the system that belong to a specific group .
- Group communication can also be characterized by the reliability and ordering guarantees it provides, such as reliable, atomic, causal, or total order multicast .
  - Reliable multicast is when a message sent by a source process is delivered to all processes in the group, or none at all, in the presence of failures .
  - Atomic multicast is when a message sent by a source process is delivered to all processes in the group, or none at all, and all processes agree on the same set of messages delivered .
  - Causal multicast is when a message sent by a source process is delivered to all processes in the group, or none at all, and the delivery order respects the causal dependencies between messages .
  - Total order multicast is when a message sent by a source process is delivered to all processes in the group, or none at all, and the delivery order is the same for all processes .
- Group communication is useful for replication in distributed systems because it allows processes to disseminate and synchronize their data or state efficiently and consistently .
- Group communication can also be used to implement consensus protocols, which are algorithms that allow processes to agree on a common value or decision in the presence of failures .
- Consensus protocols are essential for replication in distributed systems because they enable processes to maintain a consistent view of the system state and resolve conflicts or inconsistencies that may arise due to concurrent updates or failures .
- Some examples of consensus protocols are Paxos, Raft, and Zab, which are used by distributed systems such as Google Chubby, Apache ZooKeeper, and Kafka .
- Replication in distributed systems can also be influenced by the consistency model, which defines the rules and expectations for reading and writing data across multiple replicas .
- Consistency models can be classified into two categories: strong consistency and weak consistency .
  - Strong consistency models guarantee that all replicas have the same value for a given data item at any point in time, and that any read operation returns the most recent write operation .
  - Weak consistency models allow replicas to have different values for a given data item at some point in time, and that some read operations may return stale or outdated values .
- Strong consistency models provide a simpler and more intuitive abstraction for replication in distributed systems, but they incur higher communication and coordination overhead and may reduce availability and performance .
- Weak consistency models provide a more flexible and efficient abstraction for replication in distributed systems, but they require more complex application logic and may introduce anomalies or inconsistencies .
- Some examples of strong consistency models are linearizability, sequential consistency, and serializability .
- Some examples of weak consistency models are eventual consistency, causal consistency, and session consistency .

: https://www.geeksforgeeks.org/group-communication-in-distributed-systems/
: https://medium.com/@queirozgustavo/group-communication-in-distributed-systems-385b8a44b8c9
: https://distributedsystemsblog.com/docs/group-communication/
: https://cs.gmu.edu/~setia/cs707/slides/replication2.pdf
: https://www-users.cselabs.umn.edu/classes



# Fault-Tolerant Services for the Notes of the Unit 10 - Replication in the Subject of Distributed System

- Fault-tolerant services are services that can continue to function correctly even in the presence of failures, such as server crashes, network partitions, or malicious attacks.
- Replication is a technique for implementing fault-tolerant services by creating multiple copies of the same service (or state machine) and coordinating the interactions of clients with these copies.
- Replication can improve the availability, performance, and reliability of distributed systems, but also introduces challenges such as consistency, concurrency, and communication overhead.
- There are two main classes of replication techniques: primary-backup replication and active replication.
  - Primary-backup replication assigns one replica as the primary and the others as backups. The primary receives all the client requests and executes them, while sending updates to the backups. The backups apply the updates in the same order as the primary and send acknowledgments. If the primary fails, one of the backups takes over as the new primary.
  - Active replication involves all the replicas receiving and executing the same client requests in the same order. The replicas use a consensus protocol to agree on the order of requests and send replies to the clients. If some replicas fail, the others can still provide the service.
- Replication can tolerate different types of faults, such as crash faults or Byzantine faults.
  - Crash faults occur when a replica stops functioning or becomes unreachable. To tolerate f crash faults, primary-backup replication requires n(f+1) replicas, while active replication requires n(2f+1) replicas.
  - Byzantine faults occur when a replica behaves arbitrarily or maliciously, such as sending incorrect or conflicting messages. To tolerate f Byzantine faults, primary-backup replication requires n(3f+1) replicas, while active replication requires n(3f+1) replicas.
- Replication can also be classified based on the consistency model that it provides, such as linearizability, sequential consistency, causal consistency, or eventual consistency.
  - Linearizability is the strongest consistency model, which requires that every operation appears to take effect atomically at some point between its invocation and response, and that the order of operations is consistent with the real-time order of invocations.
  - Sequential consistency is a weaker consistency model, which requires that every operation appears to take effect atomically at some point between its invocation and response, and that the order of operations is consistent with the order of invocations by each individual client.
  - Causal consistency is a weaker consistency model, which requires that every operation appears to take effect atomically at some point between its invocation and response, and that the order of operations is consistent with the causal order of invocations, i.e., the order implied by the dependencies among operations.
  - Eventual consistency is the weakest consistency model, which requires that every operation appears to take effect atomically at some point between its invocation and response, and that the order of operations is eventually consistent, i.e., all replicas converge to the same state after some finite time without failures or updates.
- Replication can also be classified based on the location of the replicas, such as local replication or geo-replication.
  - Local replication involves replicas that are located within the same data center or network. Local replication can provide low latency and high throughput, but also has limited fault tolerance and scalability.
  - Geo-replication involves replicas that are located across different geographical regions or continents. Geo-replication can provide high availability and global scalability, but also has high latency and communication overhead.



# Highly Available Services for the Notes of the Unit 10 - Replication in the Subject of Distributed System

- Replication is the process of creating and maintaining multiple copies of data or services across different nodes or locations in a distributed system.
- Replication can improve the availability, reliability, performance, and scalability of distributed systems by reducing the impact of failures, network congestion, and data access latency.
- Replication can also enable fault tolerance, load balancing, data locality, and disaster recovery in distributed systems.
- Replication can be classified into two types: eager replication and lazy replication.
  - Eager replication ensures that all copies of data or services are updated synchronously or atomically whenever a change occurs. Eager replication provides strong consistency and high availability, but it can incur high overhead and low scalability.
  - Lazy replication allows some copies of data or services to be updated asynchronously or eventually after a change occurs. Lazy replication provides weak consistency and high performance, but it can introduce conflicts and inconsistencies among copies.
- Replication can be implemented at different levels of abstraction in distributed systems, such as data replication, service replication, and process replication.
  - Data replication involves creating and maintaining multiple copies of data items or databases across different nodes or locations. Data replication can improve the availability and performance of data access, but it can also introduce challenges such as concurrency control, conflict resolution, and consistency maintenance.
  - Service replication involves creating and maintaining multiple copies of services or functionalities across different nodes or locations. Service replication can improve the availability and reliability of service provision, but it can also introduce challenges such as service discovery, load balancing, and fault tolerance.
  - Process replication involves creating and maintaining multiple copies of processes or threads across different nodes or locations. Process replication can improve the availability and scalability of process execution, but it can also introduce challenges such as process coordination, state synchronization, and group communication.
- Replication can be based on different models or techniques, such as primary-backup, quorum, state machine, viewstamped, and gossip.
  - Primary-backup replication involves designating one copy of data or service as the primary and the other copies as backups. The primary is responsible for processing requests and propagating updates to the backups. The backups are responsible for taking over the primary role in case of failure. Primary-backup replication provides high availability and strong consistency, but it can also introduce a single point of failure and performance bottleneck.
  - Quorum replication involves assigning weights or votes to each copy of data or service and requiring a minimum number of votes to perform read or write operations. Quorum replication can balance the trade-off between availability and consistency, but it can also incur high communication and computation costs.
  - State machine replication involves modeling each copy of data or service as a deterministic state machine and ensuring that they execute the same sequence of commands in the same order. State machine replication can provide high availability and strong consistency, but it can also require high coordination and synchronization among copies.
  - Viewstamped replication involves organizing the copies of data or service into a dynamic group or view and electing a leader for each view. The leader is responsible for ordering and executing requests and sending viewstamps to the other copies. The other copies are responsible for validating and applying the viewstamps. Viewstamped replication can provide high availability and strong consistency, but it can also require high leader election and view change costs.
  - Gossip replication involves disseminating updates or information among the copies of data or service using a probabilistic or randomized communication protocol. Gossip replication can provide high performance and scalability, but it can also introduce uncertainty and inconsistency among copies.



# Transactions with Replicated Data

- Transactions are a sequence of operations that are executed atomically, consistently, isolatedly, and durably (ACID properties) on a database system.
- Replication is the process of copying data and storing it in different locations, such as multiple servers or nodes in a distributed system.
- Replication serves to make the data widely available, improve performance, and protect from data loss or failures.
- Transactions with replicated data are transactions that involve operations on data items that are replicated across multiple locations.
- Transactions with replicated data pose some challenges for maintaining the ACID properties, such as:
  - How to ensure that all copies of a data item are updated consistently and atomically?
  - How to prevent conflicts or anomalies when concurrent transactions access or update replicated data items?
  - How to recover from failures or network partitions that may affect some or all copies of a data item?
- There are different approaches or protocols for managing transactions with replicated data, such as:
  - Primary-copy protocol: One copy of each data item is designated as the primary copy, and all transactions must access or update the primary copy first. The primary copy then propagates the updates to the other copies (secondary copies) asynchronously or synchronously. This protocol ensures serializability and atomicity, but introduces a single point of failure and a bottleneck for the primary copy.
  - Majority protocol: Each data item has a version number that is incremented whenever it is updated. Transactions must read or write a majority of the copies of a data item to ensure consistency and atomicity. This protocol tolerates failures or partitions as long as a majority of the copies are accessible, but increases the communication and latency costs.
  - Quorum protocol: Each data item has a read quorum and a write quorum, which are subsets of the copies that must be accessed for reading or writing respectively. The read and write quorums must satisfy some conditions, such as the write quorum must include a majority of the copies, and the read and write quorums must have a non-empty intersection. This protocol allows for more flexibility and trade-offs between availability and consistency, but also increases the complexity and overhead of managing the quorums.
  - Optimistic protocol: Transactions are allowed to read or write any copy of a data item without locking or coordination. However, before committing, transactions must validate their operations by checking if they have read or written the latest version of the data items. If not, the transactions must abort and restart. This protocol reduces the contention and blocking of transactions, but may incur more aborts and restarts if there are many concurrent updates or conflicts.

