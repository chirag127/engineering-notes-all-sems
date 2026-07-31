

## Unit 1 - Characterization of Distributed Systems

A distributed system is a collection of independent computers that appear to the users as a single coherent system. Some examples of distributed systems are the Internet, the World Wide Web, peer-to-peer networks, cloud computing, and distributed databases.

Some of the main characteristics of distributed systems are:

- **Concurrency**: Multiple components can execute simultaneously and interact with each other.
- **Lack of a global clock**: There is no common notion of time among the components, which makes it hard to synchronize and order events.
- **Independent failures**: Each component can fail independently, without affecting the rest of the system. The system has to cope with partial failures and ensure availability and reliability.
- **Heterogeneity**: The components can have different hardware, software, network, and data formats, which requires interoperability and compatibility.
- **Scalability**: The system can grow in size and complexity without degrading its performance and functionality.
- **Transparency**: The system should hide its complexity and heterogeneity from the users and provide a consistent and uniform interface.

Some of the main challenges of designing and implementing distributed systems are:

- **Communication**: The components have to communicate with each other over unreliable and insecure networks, which can introduce delays, errors, and attacks.
- **Coordination**: The components have to coordinate their actions and reach agreement on common goals, which can be difficult due to concurrency, failures, and lack of a global clock.
- **Consistency**: The system has to maintain a consistent view of the data and the state of the system, which can be hard to achieve due to replication, caching, and updates.
- **Fault tolerance**: The system has to tolerate and recover from failures of components, networks, and data, which can affect its availability and reliability.
- **Security**: The system has to protect its data and resources from unauthorized access and malicious attacks, which can compromise its integrity and confidentiality.



Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Distributed System. Here is the introduction for the notes of the Unit 1 - Characterization of Distributed Systems:

### Introduction

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- The main challenges of designing and implementing a distributed system are:
  - Heterogeneity: The system should be able to cope with different hardware, software, networks, data formats, etc.
  - Transparency: The system should hide the complexity and diversity of its components from the users and applications.
  - Scalability: The system should be able to accommodate growth in the number of users, resources, and geographical distribution without compromising performance, reliability, or availability.
  - Fault tolerance: The system should be able to continue functioning despite failures of some of its components.
  - Security: The system should be able to protect its data and resources from unauthorized access, modification, or misuse.
  - Concurrency: The system should be able to handle multiple simultaneous requests and operations from different users and applications.
  - Consistency: The system should be able to maintain a coherent and accurate view of its data and state across all its components.
  - Coordination: The system should be able to synchronize and coordinate the actions and decisions of its components to achieve a common goal.



### Examples of Distributed Systems

A distributed system is a collection of independent computers that communicate and coordinate their actions by passing messages. The computers in a distributed system may be physically close or geographically dispersed, and they may be connected by a network or a bus. The main advantages of distributed systems are scalability, fault tolerance, resource sharing, and performance.

Some examples of distributed systems are:

- **Telecommunication networks**: Telephone networks are an early example of a peer-to-peer network, where each node can initiate or receive calls. Cellular and telephone networks are forms and examples of distributed networks .
- **Real-time systems**: Many industries use real-time systems distributed in various areas, locally and globally. For example, air traffic control systems, power grid systems, industrial control systems, and online gaming systems are all examples of real-time distributed systems .
- **Distributed database systems**: A distributed database has locations across multiple servers, physical locations, or both. The data is replicated or partitioned among the nodes, and the nodes communicate to maintain consistency and availability. Examples of distributed database systems are Google's Bigtable, Amazon's Dynamo, and MongoDB .
- **Distributed web applications**: A distributed web application is a web application that runs on multiple servers or locations, and uses a distributed architecture to handle requests, process data, and deliver content. Examples of distributed web applications are Google, Facebook, Twitter, and Netflix .
- **Distributed file systems**: A distributed file system is a file system that allows access to files from multiple hosts sharing via a computer network. The files are stored on one or more servers, and the clients can access them as if they were local files. Examples of distributed file systems are NFS, HDFS, and Ceph.



Hello, I am Sydney, your AI assistant. I can help you with your notes on Resource sharing for the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM. Here is a summary of the main points:

- Resource sharing is one of the main goals and challenges of distributed systems. It involves making the resources of a system (such as data, files, devices, services, etc.) available to multiple users or processes in a transparent, efficient, and secure way.
- Resource sharing can be classified into two types: sharing by communication and sharing by distribution. Sharing by communication means that the users or processes exchange messages to access the resources, while sharing by distribution means that the resources are replicated or moved to different locations.
- Resource sharing can also be classified into two modes: concurrent and sequential. Concurrent sharing means that multiple users or processes can access the same resource at the same time, while sequential sharing means that only one user or process can access the resource at a time.
- Resource sharing can have various benefits, such as improving performance, reliability, availability, scalability, and functionality of distributed systems. However, it can also introduce various challenges, such as managing concurrency, consistency, synchronization, security, and fault tolerance of distributed systems.
- Resource sharing can be implemented using various techniques, such as remote procedure calls, remote method invocation, message passing, middleware, distributed file systems, distributed databases, distributed objects, web services, etc. Each technique has its own advantages and disadvantages, and requires different design decisions and trade-offs.



### The Web Challenges for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Distributed systems are systems that consist of multiple independent components that communicate and coordinate with each other over a network.
- Distributed systems enable resource sharing, scalability, fault tolerance, and high availability, but also pose many challenges for their design, implementation, and management.
- Some of the major web challenges in distributed systems are  :

  - **Scalability**: The ability to handle increasing load and demand without degrading the performance or quality of service of the system. Scalability can be achieved by adding more resources, such as servers, storage, or bandwidth, or by redesigning the system architecture, such as using load balancing, caching, or replication techniques.
  - **Heterogeneity**: The diversity and variability of the components, platforms, protocols, and standards that make up the system. Heterogeneity can cause interoperability, compatibility, and consistency issues, and requires the use of common interfaces, middleware, and adapters to enable communication and coordination among different devices, software, and data formats.
  - **Security**: The protection of the system and its data from unauthorized access, modification, or disclosure. Security challenges include ensuring the privacy, integrity, and availability of the system and its resources, as well as providing authentication, authorization, encryption, and auditing mechanisms to prevent and detect attacks.
  - **Fault tolerance**: The ability to continue operating correctly and reliably in the presence of failures, errors, or faults in the system or its environment. Fault tolerance can be achieved by using techniques such as redundancy, replication, backup, recovery, or consensus algorithms to detect, isolate, mask, or correct faults and maintain the system state and functionality.
  - **Consistency**: The property that the system and its data present a coherent and accurate view to the users and applications, regardless of the distribution, replication, or concurrency of the system components. Consistency can be ensured by using techniques such as locking, transactions, or synchronization protocols to coordinate and order the operations and updates on the system and its data.
  - **Concurrency**: The property that the system and its components can execute multiple operations or tasks simultaneously or in parallel, without interfering or conflicting with each other. Concurrency can improve the performance, throughput, and responsiveness of the system, but also introduces challenges such as deadlock, livelock, race conditions, or starvation, which require the use of techniques such as scheduling, coordination, or communication primitives to manage and resolve.
  - **Transparency**: The property that the system and its distribution are hidden or abstracted from the users and applications, so that they perceive the system as a single, integrated, and uniform entity. Transparency can enhance the usability, portability, and interoperability of the system, but also requires the use of techniques such as naming, location, replication, or migration services to provide the illusion of a centralized and homogeneous system.



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



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of fundamental models for distributed systems:

### Fundamental Models

- Fundamental models describe the properties that are common to all distributed systems, regardless of their specific architectures, applications, or implementations.
- Fundamental models can be classified into three categories: interaction models, failure models, and security models.
- Interaction models deal with the issues related to the communication and coordination of processes in a distributed system, such as performance, timing, ordering, and consistency of events and messages.
- Failure models specify the types and causes of faults that can occur in a distributed system, such as process crashes, network partitions, message losses, and Byzantine failures.
- Security models define the threats and attacks that can compromise the confidentiality, integrity, and availability of a distributed system, such as eavesdropping, tampering, replaying, and denial-of-service.

#### Interaction Models

- Interaction models can be further divided into two subcategories: architectural models and fundamental models.
- Architectural models describe the structure and organization of a distributed system, such as client-server, peer-to-peer, publish-subscribe, and service-oriented architectures.
- Fundamental models describe the basic assumptions and properties of a distributed system, such as synchrony, causality, logical clocks, global states, and distributed snapshots.

##### Architectural Models

- Architectural models are based on the concept of components and connectors, where components are the entities that perform computations and connectors are the entities that enable communication and coordination among components.
- Architectural models can be classified according to the degree of decentralization, the nature of communication, and the type of service provided by the components.
- Client-server architecture is a centralized model, where clients request services from servers and servers provide services to clients. Communication is usually request-reply and service is usually stateless.
- Peer-to-peer architecture is a decentralized model, where peers act as both clients and servers and provide and consume services from each other. Communication is usually asynchronous and service is usually stateful.
- Publish-subscribe architecture is a decoupled model, where publishers produce events and subscribers consume events. Communication is usually event-driven and service is usually anonymous.
- Service-oriented architecture is a modular model, where services are self-contained, reusable, and interoperable components that provide functionality to other services or applications. Communication is usually message-oriented and service is usually standardized.

##### Fundamental Models

- Fundamental models are based on the concept of processes and messages, where processes are the entities that execute computations and messages are the entities that carry information among processes.
- Fundamental models can be classified according to the degree of synchrony, the notion of causality, and the representation of global states in a distributed system.
- Synchrony model defines the assumptions and bounds on the speed of processes and the delay of messages in a distributed system. It can be classified into three categories: synchronous, asynchronous, and partially synchronous.
- Synchronous model assumes that there are known upper bounds on the relative speed of processes and the transmission delay of messages. It enables deterministic algorithms and simplifies the design and analysis of distributed systems.
- Asynchronous model assumes that there are no bounds on the relative speed of processes and the transmission delay of messages. It reflects the reality of distributed systems and allows for more flexibility and scalability.
- Partially synchronous model assumes that there are bounds on the relative speed of processes and the transmission delay of messages, but they are unknown or may change over time. It captures the trade-offs between the synchronous and asynchronous models and allows for more robustness and adaptability.
- Causality model defines the notion of precedence and dependence among events and messages in a distributed system. It can be classified into two categories: physical causality and logical causality.
- Physical causality is based on the real-time ordering of events and messages, as observed by a global clock. It is objective and absolute, but difficult to implement and maintain in a distributed system.
- Logical causality is based on the potential influence of events and messages, as captured by a logical clock. It is subjective and relative, but easy to implement and maintain in a distributed system.
- Global state model defines the representation and observation of the state of a distributed system, which consists of the local states of processes and the messages in transit. It can be classified into two categories: consistent global state and distributed snapshot.
- Consistent global state is a global state that satisfies the causality relation among events and messages, i.e., it does not contain any causal anomaly. It is useful for reasoning about the behavior and properties of a distributed system.
- Distributed snapshot is a technique for capturing



### Theoretical Foundation for Distributed System

A distributed system is a collection of processes that are spatially separated and do not share a common memory and communicate with one another by exchanging messages with arbitrary delays .

Some of the theoretical foundations for distributed system are:

- **Limitation of Distributed System**: Due to the lack of global clock, shared memory, and reliable communication, distributed systems face challenges such as synchronization, consistency, fault tolerance, and security.
- **Logical Clocks**: Logical clocks are a way of ordering events in a distributed system without relying on physical clocks. They assign logical timestamps to events such that causally related events have consistent timestamps. There are different types of logical clocks, such as Lamport's clocks and vector clocks, that have different properties and trade-offs .
- **Message Passing System**: Message passing system is a model of communication in distributed systems where processes send and receive messages to each other. Message passing system can be synchronous or asynchronous, reliable or unreliable, and FIFO or non-FIFO. Message passing system can be used to implement various distributed algorithms, such as leader election, mutual exclusion, consensus, and broadcast .
- **Coordination Algorithms**: Coordination algorithms are fundamental in distributed systems to achieve agreement and consistency among processes. They can be used for dynamic role assignment, resource sharing, and action coordination. Some examples of coordination algorithms are Paxos, Raft, Two-Phase Commit, and Distributed Snapshots.
- **Distributed Information Systems**: Distributed information systems are systems that store, process, and disseminate information across multiple nodes in a network. They aim to provide scalability, availability, and fault tolerance for large-scale data management. They also face challenges such as data replication, consistency, and security. Some examples of distributed information systems are distributed databases, distributed file systems, and distributed web services.



### Limitation of Distributed system

A distributed system is a system that consists of multiple independent components that communicate with each other over a network. Distributed systems have many advantages, such as scalability, fault-tolerance, availability, and performance. However, they also face some limitations that affect their design and implementation. Some of the main limitations of distributed systems are:

- **Absence of a global state**: In a distributed system, there is no single point of control or coordination for the entire system. Each component has its own local state and view of the system, which may differ from the views of other components. This makes it difficult to reason about the behavior and correctness of the system as a whole, and to ensure consistency and coherence among the components. For example, it is hard to implement transactions, concurrency control, and replication in a distributed system without a global state  .
- **Absence of a global clock**: In a distributed system, there is no common notion of time or ordering of events among the components. Each component has its own local clock, which may drift or be inaccurate. This makes it challenging to synchronize the actions and data of the components, and to establish causality and precedence among the events. For example, it is hard to implement consensus, agreement, and coordination protocols in a distributed system without a global clock .
- **Network latency and failures**: In a distributed system, the communication between the components is subject to delays and errors due to the network. The network may be unreliable, unpredictable, or even malicious, causing messages to be lost, corrupted, duplicated, or reordered. This makes it complex to ensure the reliability, availability, and security of the system, and to handle the failure scenarios and recovery mechanisms. For example, it is hard to implement fault-tolerance, replication, and consistency models in a distributed system without considering the network characteristics  .

These limitations of distributed systems pose significant challenges for the developers and designers of such systems, and require them to adopt various techniques and principles to overcome them. Some of the common techniques and principles are:

- **Abstraction and modularity**: To cope with the complexity and diversity of distributed systems, it is useful to abstract away the details and provide a simpler and uniform interface for the components. For example, using middleware, RPC, or REST to hide the network communication details, or using virtualization, containers, or microservices to hide the hardware and software heterogeneity. Moreover, it is beneficial to modularize the system into smaller and independent units that can be composed and reused. For example, using layers, components, or services to separate the concerns and responsibilities of the system  .
- **Replication and distribution**: To enhance the scalability, availability, and performance of distributed systems, it is helpful to replicate and distribute the data and computation among multiple components. For example, using sharding, partitioning, or load balancing to distribute the workload, or using caching, mirroring, or backup to replicate the data. However, replication and distribution also introduce trade-offs and challenges, such as consistency, concurrency, and coordination, which need to be carefully addressed  .
- **Coordination and agreement**: To ensure the correctness and coherence of distributed systems, it is necessary to coordinate and agree on the actions and data of the components. For example, using transactions, locks, or atomic operations to ensure atomicity, isolation, and durability, or using consensus, leader election, or Paxos to ensure agreement, order, and finality. However, coordination and agreement also incur overhead and complexity, such as latency, failures, and conflicts, which need to be efficiently handled  .

These are some of the main limitations of distributed systems and the techniques and principles to overcome them. Distributed systems are a fascinating and challenging field of study and practice, and require a deep understanding of the underlying concepts and trade-offs.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is a summary of the topic of absence of global clock for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM.

### Absence of global clock

- A global clock is a system-wide clock that is equally accessible to all processes in a distributed system.
- A global clock would allow processes to synchronize their actions, measure the elapsed time between events, and determine the order of events across the system.
- However, a global clock is hard to realize in distributed systems due to the following reasons:
  - The communication channel between processes is unreliable and has unpredictable message delays.
  - The processes do not share common memory and have to exchange information via messages.
  - The processes may have different local clocks that drift apart over time and are not perfectly accurate.
  - The rate of event occurrence is very high and the granularity of time measurement is limited.
- Therefore, the absence of a global clock implies that:
  - The notion of common time does not exist in a distributed system; different processes may have different notions of time.
  - It is not always possible to determine the order in which two events on different processes were executed.
  - It is not possible for an individual process to obtain an up-to-date state of the entire system.
  - It is difficult to obtain a meaningful state of the system, in which states of different processes are consistent with each other.



### Shared Memory

- Shared memory is a programming model that allows multiple processes to access and modify the same data in a shared address space.
- Shared memory can be implemented in two ways: physically shared memory and distributed shared memory.
- Physically shared memory is when multiple processors or cores share the same physical memory, such as in a multiprocessor system or a multicore system.
- Distributed shared memory (DSM) is when multiple nodes or computers in a distributed system share a virtual address space, but do not have physical shared memory. The DSM system manages the memory across all the nodes and provides the illusion of a single shared memory.
- DSM can be achieved via software or hardware. Software DSM relies on the operating system or the middleware to handle the communication and synchronization of the shared data. Hardware DSM relies on special hardware components, such as cache coherence circuits or network interface controllers, to maintain the consistency of the shared data.
- DSM has several advantages, such as:
  - It simplifies the programming of distributed applications by hiding the details of data distribution and communication.
  - It allows the programmers to use the familiar shared memory model and synchronization primitives, such as locks, semaphores, or monitors.
  - It enables the exploitation of data locality and parallelism by allowing the processes to access the shared data in their local memory or cache.
  - It facilitates the dynamic load balancing and fault tolerance by allowing the migration and replication of the shared data across the nodes.
- DSM also has some challenges, such as:
  - It requires a high-performance and reliable network to support the frequent data transfers and updates.
  - It introduces the overhead of maintaining the coherence and consistency of the shared data, which may affect the performance and scalability of the system.
  - It may cause false sharing or thrashing, which are situations where multiple processes access or modify the same memory block or page, even though they do not share any data in that block or page. This may result in unnecessary data transfers and invalidations.
  - It may suffer from the granularity problem, which is the trade-off between the size of the memory blocks or pages that are shared and the frequency of the data transfers and updates. Smaller blocks or pages may reduce the false sharing and thrashing, but increase the communication overhead. Larger blocks or pages may reduce the communication overhead, but increase the false sharing and thrashing.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on logical clocks for the unit 1 of distributed systems.

### Logical clocks

- A logical clock is a mechanism for capturing chronological and causal relationships in a distributed system  .
- A distributed system may have no physically synchronous global clock, so a logical clock allows global ordering on events from different processes in such systems  .
- A logical clock is not a physical device, but a software algorithm that assigns a logical timestamp to each event in a distributed system .
- A logical clock must satisfy the following property: if event a causally precedes event b, then the logical timestamp of a is less than the logical timestamp of b .
- A logical clock does not necessarily reflect the real time of events, but only their relative order and causality .
- There are different types of logical clocks, such as Lamport's clocks, vector clocks, and matrix clocks, that have different advantages and disadvantages  .
- Lamport's clocks use a single integer value to represent the logical timestamp of each event, and increment it by one for each local event or message sent, and update it to the maximum of the current value and the received message timestamp plus one for each message received  .
- Lamport's clocks can totally order all events in a distributed system, but they cannot distinguish between concurrent events, that is, events that are not causally related  .
- Vector clocks use a vector of integer values to represent the logical timestamp of each event, where each element corresponds to the logical clock of a process in the system, and increment the element corresponding to the current process by one for each local event or message sent, and update the vector to the element-wise maximum of the current vector and the received message vector for each message received  .
- Vector clocks can partially order all events in a distributed system, and they can distinguish between concurrent events, but they require more space and communication overhead than Lamport's clocks  .
- Matrix clocks use a matrix of integer values to represent the logical timestamp of each event, where each row and column corresponds to a process in the system, and the diagonal elements are the logical clocks of the processes, and increment the diagonal element corresponding to the current process by one for each local event or message sent, and update the row and column corresponding to the current process to the element-wise maximum of the current row and column and the received message row and column for each message received  .
- Matrix clocks can totally order all events in a distributed system, and they can distinguish between concurrent events, but they require more space and communication overhead than vector clocks  .



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is some information on Lamport's logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM.

### Lamport's logical clocks

- Lamport's logical clocks are a way of ordering events in a distributed system based on their causal relationships, rather than their physical time.
- A Lamport logical clock is a numerical software counter value maintained in each process. It is incremented whenever a process performs an event, such as sending or receiving a message.
- The basic rules of Lamport's logical clocks are:
  - Each process has a logical clock, initialized to zero.
  - Each time a process performs an internal event, it increments its logical clock by one.
  - Each time a process sends a message, it piggybacks its current logical clock value with the message.
  - Each time a process receives a message, it updates its logical clock to the maximum of its own clock and the received clock value, and then increments it by one.
- Lamport's logical clocks ensure that if event a causally precedes event b, then the logical clock of a is less than the logical clock of b. This is denoted by a -> b.
- However, Lamport's logical clocks do not ensure that if the logical clock of a is less than the logical clock of b, then a causally precedes b. This is because two events may be concurrent, meaning that they are not causally related, but have different logical clock values due to the arbitrary order of message delivery.
- Lamport's logical clocks are also known as scalar clocks, because they use a single integer value to represent the logical time of each event.
- Lamport's logical clocks are widely used in distributed systems to provide a partial ordering of events, and to detect causality violations, such as message overtaking. They are also a basis for more advanced logical clock algorithms, such as vector clocks.



### Concepts in Message Passing Systems

- Message passing is a technique for invoking behavior on a computer by sending a message to a process.
- Message passing is used in distributed systems, which are systems that consist of multiple independent computers that communicate and coordinate their actions by passing messages.
- Message passing systems provide a set of message-based interprocess communication (IPC) protocols that allow processes to exchange information and synchronize their activities.
- Message passing systems can be classified into two categories: synchronous and asynchronous.
  - Synchronous message passing systems require the sender and the receiver to be ready at the same time for the message transfer. The sender blocks until the receiver acknowledges the message, and the receiver blocks until a message arrives.
  - Asynchronous message passing systems do not impose any timing constraints on the sender and the receiver. The sender can send a message and continue its execution without waiting for an acknowledgment, and the receiver can receive a message at any time without blocking.
- Message passing systems can also be classified into two types: direct and indirect.
  - Direct message passing systems require the sender to explicitly specify the identity of the receiver, such as its name or address. The communication link is established by the sender before sending the message.
  - Indirect message passing systems do not require the sender to know the identity of the receiver. The communication link is established by a third party, such as a message queue or a topic. The sender and the receiver can communicate by sending and receiving messages to and from the same queue or topic.
- Message passing systems have some advantages and disadvantages over other IPC methods, such as shared memory and remote procedure calls (RPCs).
  - Advantages of message passing systems include:
    - They are portable and scalable, as they do not depend on the underlying hardware or operating system.
    - They are flexible and expressive, as they can support different types of messages and communication patterns.
    - They are reliable and fault-tolerant, as they can handle message losses, duplications, and delays.
  - Disadvantages of message passing systems include:
    - They are complex and difficult to program, as they require the programmer to deal with low-level details of message formats, protocols, and error handling.
    - They are inefficient and costly, as they incur overheads of message encoding, decoding, buffering, and transmission.
    - They are insecure and vulnerable, as they expose the messages to unauthorized access, modification, or interception.
- Message passing interface (MPI) is a standardized and portable message-passing system developed for distributed and parallel computing. MPI provides parallel hardware vendors with a clearly defined base set of routines that can be efficiently implemented.
  - MPI supports both synchronous and asynchronous message passing, as well as both point-to-point and collective communication.
  - MPI allows processes to send and receive messages that contain data ranging from primitive types to actual objects.
  - MPI also provides features such as groups, communicators, topologies, and virtual channels to facilitate the organization and coordination of processes.



### Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- Causal order is a way of ordering events in a distributed system based on their causal relationships, rather than their physical timestamps or locations.
- Causal order captures the intuitive notion of "happened before" or "influenced by" among events, regardless of when or where they occurred.
- Causal order is important for ensuring consistency, correctness, and coordination in distributed systems, especially when dealing with concurrent or asynchronous events.
- Causal order can be defined formally using Lamport's logical clocks, which assign logical timestamps to events based on their causal dependencies, rather than their physical clocks.
- Causal order can be implemented using various algorithms, such as vector clocks, causal broadcast, or causal delivery, which ensure that messages are delivered or processed in a way that respects their causal order.
- Causal order is a weaker form of ordering than total order, which imposes a single linearization of all events in the system, even those that are concurrent or independent. Total order is more strict, but also more costly and less scalable than causal order.
- Causal order is also weaker than sequential order, which requires that all events appear in the same order to all observers, regardless of their causal relationships. Sequential order is more intuitive, but also more restrictive and less realistic than causal order.
- Causal order is a trade-off between performance and consistency in distributed systems, allowing more concurrency and flexibility, but also more potential for anomalies or conflicts. Causal order is often used as a minimal guarantee for distributed applications that need some form of consistency, but not necessarily strong consistency.



### Total Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent entities that communicate by message passing and coordinate their actions to achieve a common goal.
- Events are occurrences that happen at a specific point in time and space in a distributed system.
- A partial order is a binary relation that is reflexive, antisymmetric, and transitive. For example, the relation "happens before" is a partial order among events in a distributed system.
- A total order is a partial order that is also complete, meaning that any two elements are comparable. For example, the relation "less than or equal to" is a total order among natural numbers.
- A distributed system is said to have partial order if we can have a partial order relationship among the events in the system. For example, if event A causes event B, then A happens before B, and this relation is transitive.
- A distributed system is said to have total order if we can establish a causal relationship among all events in the system. For example, if we assign a unique timestamp to each event, and use some arbitrary mechanism to break ties, then we can compare any two events by their timestamps.
- Total order is very useful for distributed system implementation, as it can help ensure consistency, reliability, and fault-tolerance . For example, if we want to implement a shared resource that can be used by only one process at a time, we can use total order to decide which process gets the resource first.
- Total order can be achieved by various algorithms and protocols, such as Lamport timestamps, vector clocks, logical clocks, atomic broadcast, etc  . These methods have different trade-offs in terms of complexity, performance, and scalability  .
- A diagram that illustrates the total order of events in a distributed system is shown below:

```
Process 1: a -> b -> c -> d
Process 2: e -> f -> g -> h
Process 3: i -> j -> k -> l

Messages: a -> f, b -> j, c -> k, g -> d, h -> l

Total order: a -> f -> b -> j -> c -> k -> g -> d -> h -> l -> e -> i
```

- In this diagram, the events are labeled by letters, and the messages are shown by arrows. The total order is determined by using Lamport timestamps and process IDs to break ties. The total order is consistent with the partial order induced by the "happens before" relation.



### Total Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems in the Subject of Distributed System

- A distributed system is a collection of independent processes that communicate by exchanging messages over a network.
- Events are occurrences that happen at a specific point in time and space in a distributed system, such as sending or receiving a message, or executing a local operation.
- The order of events is important for understanding the behavior and correctness of a distributed system, especially in the presence of concurrency and failures.
- A partial order is a binary relation that satisfies three properties: reflexivity, antisymmetry, and transitivity. A partial order can be represented by a directed acyclic graph (DAG), where nodes are events and edges are ordering relations.
- A causal order is a partial order that captures the notion of potential causality between events. An event e1 is causally related to an event e2, denoted by e1 -> e2, if one of the following conditions holds:
  - e1 and e2 are events in the same process, and e1 occurred before e2.
  - e1 is the sending of a message m, and e2 is the receipt of the same message m.
  - There exists an event e3 such that e1 -> e3 and e3 -> e2.
- A total order is a partial order that satisfies an additional property: comparability. This means that for any two events e1 and e2, either e1 -> e2, or e2 -> e1, or both (if e1 and e2 are the same event). A total order can be represented by a linear sequence of events, where each event is preceded by all its causal predecessors and followed by all its causal successors.
- A total causal order is a total order that is consistent with the causal order. This means that if e1 -> e2 in the causal order, then e1 -> e2 in the total order as well. A total causal order is the strictest ordering in distributed systems; it establishes only one linearization, consistent with the causal order, among all the events that occur in the system, even those that occur concurrently .
- A total causal order can be implemented by using a logical clock, such as a vector clock, that assigns a timestamp to each event, such that the timestamp reflects the causal order. A vector clock is an array of integers, one for each process in the system, that is incremented by one when a process executes a local event, and is updated with the maximum of its own and the sender's vector clock when a process receives a message. A vector clock can be used to compare the order of events by using the following rules :
  - If VC(e1) < VC(e2), then e1 -> e2.
  - If VC(e1) > VC(e2), then e2 -> e1.
  - If VC(e1) = VC(e2), then e1 and e2 are the same event.
  - If none of the above holds, then e1 and e2 are concurrent events, denoted by e1 || e2.
- A total causal order can also be achieved by using a total order broadcast, which is a communication primitive that delivers messages to all processes in the same total order, such that the order is consistent with the causal order. A total order broadcast can be implemented by using a sequencer, which is a special process that assigns a sequence number to each message and broadcasts it to all processes. The processes then deliver the messages in the order of the sequence numbers .



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of message ordering techniques in distributed systems.

### Techniques for Message Ordering

- Message ordering is the problem of ensuring that messages sent by different processes in a distributed system are processed in a consistent and meaningful order.
- Message ordering is important for achieving correctness, consistency, and coordination in distributed systems.
- There are different types of message ordering techniques, depending on the desired level of ordering guarantee and the trade-off between performance and complexity.
- Some of the common message ordering techniques are:

  - **Unordered**: Messages are delivered in any order, without any guarantee of ordering. This is the simplest and fastest technique, but it may lead to incorrect or inconsistent results if the messages have dependencies or conflicts.
  - **FIFO**: Messages are delivered in the same order as they are sent by each sender. This technique ensures that messages from the same sender are processed in a sequential order, but it does not guarantee any order among messages from different senders.
  - **Causal**: Messages are delivered in a way that respects the causal dependencies among them. This technique ensures that if a message m1 causally precedes a message m2, then m1 is delivered before m2 at every receiver. A causal dependency exists if m1 and m2 are sent by the same sender, or if m1 is received by the sender of m2 before sending m2, or if there is a chain of such dependencies. Causal ordering is stronger than FIFO ordering, but it may still allow some non-determinism among concurrent messages.
  - **Total**: Messages are delivered in the same order at every receiver. This technique ensures that all receivers agree on a single global order of messages, regardless of their causal dependencies or concurrency. Total ordering is stronger than causal ordering, but it may require more communication and coordination among processes to achieve consensus on the order.
  - **Synchronous**: Messages are delivered in a way that synchronizes the actions of the processes. This technique ensures that all receivers process a message before the sender can send another message, or that all senders send a message before any receiver can process it. Synchronous ordering is stronger than total ordering, but it may impose a high latency and a low throughput on the system.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of causal ordering of messages in distributed systems.

### Causal ordering of messages

- Causal ordering of messages is a partial ordering of messages in a distributed computing environment .
- It places a restriction on communication between processes by requiring that if the transmission of message mi to process pk necessarily preceded the transmission of message mj to the same process, then the delivery of these messages to that process must be ordered such that mi is delivered before mj .
- Causal ordering of messages is one of the four semantics of multicast communication, namely unordered, totally ordered, causal, and sync-ordered communication.
- Multicast communication methods vary according to the message’s reliability guarantee and ordering guarantee.
- Causal ordering of messages is useful for ensuring consistency and correctness of distributed applications that depend on the causal relationships between events .
- Causal ordering of messages can be implemented using various algorithms, such as vector clocks, logical clocks, or piggybacking techniques  .
- Causal ordering of messages can also be achieved by using group communication protocols that provide synchronous order communication, which is a stronger form of ordering that ensures that all processes in a group receive the same messages in the same order.



### Global State for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent processes that communicate through message passing.
- The global state of a distributed system is the union of the local states of the individual processes and the channels .
- A local state of a process is the values of its variables, registers, program counter, etc. at a given point in time.
- A channel state is the set of messages that have been sent but not yet received by the processes.
- The global state of a distributed system may change due to the occurrence of events, such as local computation, message sending, message receiving, etc.
- A global state is consistent if it reflects a possible execution of the system, i.e., it does not contain any causal anomaly .
- A causal anomaly is a situation where a message is received before it is sent, or a process observes the effect of a message before it observes the message itself.
- A consistent global state can be computed along a consistent cut, which is a partition of the system's execution history into past and future events .
- A consistent cut satisfies the property that if an event is in the future of the cut, then all events that causally precede it are also in the future of the cut .
- A global snapshot is a technique for recording a consistent global state of a distributed system without stopping or synchronizing the processes.
- A global snapshot algorithm ensures that each process records its local state and the state of its incoming channels in such a way that the resulting global state is consistent.
- A global snapshot can be used for various purposes, such as checkpointing, debugging, monitoring, termination detection, etc.  .



### Termination Detection

Termination detection is a fundamental problem in distributed systems, where a set of processes cooperate to perform a computation. The problem is to determine if the computation has terminated, i.e., if all the processes are idle and there are no messages in transit.

One of the algorithms for termination detection is Huang's algorithm, proposed by Shing-Tsaan Huang in 1989. The algorithm is based on the following concepts:

- A process is either in an active state or in an idle state. An active process may become idle at any time, but an idle process may only become active again upon receiving a computational message (a message that affects the state of the process).
- A process maintains a counter, called the control message count (CMC), that records the number of control messages (messages that are used for termination detection) sent and received by the process. The CMC is initialized to zero and is incremented by one for each control message sent and decremented by one for each control message received.
- A process also maintains a boolean flag, called the termination flag (TF), that indicates whether the process has detected termination or not. The TF is initialized to false and is set to true when the process detects termination.
- A process periodically sends its CMC and TF values to a designated process, called the coordinator, using a control message. The coordinator collects the CMC and TF values from all the processes and decides whether termination has occurred or not.
- The coordinator decides that termination has occurred if and only if the following conditions are satisfied:
  - The sum of the CMC values from all the processes is zero, which means that there are no control messages in transit.
  - The TF values from all the processes are true, which means that all the processes have detected termination.
- The coordinator broadcasts a control message to all the processes to inform them about the termination decision.

The following diagram illustrates the algorithm:

Huang's algorithm

The algorithm has the following properties:

- The algorithm is correct, i.e., it detects termination if and only if termination has occurred.
- The algorithm is efficient, i.e., it uses a small number of control messages and has a low latency.
- The algorithm is distributed, i.e., it does not require a global clock or a global state.



## Unit 2 - Distributed Mutual Exclusion

- Mutual exclusion is a property of concurrency control, which is introduced to prevent race conditions.
- Race conditions occur when multiple processes access a shared resource or data simultaneously, and the outcome depends on the order of execution.
- Mutual exclusion ensures that only one process is allowed to execute the critical section (CS) at any given time, where the CS is the part of the code that accesses the shared resource or data  .
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion, because there is no global memory or clock .
- Message passing is the sole means for implementing distributed mutual exclusion .
- There are three basic approaches for implementing distributed mutual exclusion:
  - Token-based algorithms: A process can enter the CS only if it possesses a unique token, which is passed among the processes in a logical ring or a tree.
  - Permission-based algorithms: A process can enter the CS only if it obtains permission from all or a subset of the other processes in the system, using request and reply messages.
  - Quorum-based algorithms: A process can enter the CS only if it obtains permission from a majority or a weighted majority of the processes in the system, using voting sets.
- The performance of distributed mutual exclusion algorithms can be measured by the following criteria :
  - Message complexity: The number of messages exchanged per CS execution .
  - Synchronization delay: The time elapsed between the instant a process requests the CS and the instant it is granted the CS, assuming no other process is in the CS .
  - Response time: The time elapsed between the instant a process requests the CS and the instant it is granted the CS, assuming some other process may be in the CS .
  - System throughput: The number of times the CS is executed per unit time in the system .
  - Fault tolerance: The ability of the algorithm to handle process or message failures .



### Classification of distributed mutual exclusion

Distributed mutual exclusion is a problem of ensuring that only one process can access a shared resource or data at a time in a distributed system. It is a fundamental requirement for achieving consistency, reliability, and fault-tolerance in distributed systems.

There are three basic approaches for implementing distributed mutual exclusion:

- **Token-based approach**: A unique token is shared among the processes. A process can enter its critical section only if it possesses the token. Mutual exclusion is ensured because the token is unique. The token is passed from one process to another according to some algorithm. Examples of token-based algorithms are Ricart-Agrawala algorithm, Suzuki-Kasami algorithm, and Raymond's tree algorithm  .

- **Non-token-based approach**: There is no token in this approach. Instead, a process requests permission from other processes to enter its critical section. The other processes reply with either grant or deny messages. A process can enter its critical section only if it receives grant messages from all or a majority of other processes. Examples of non-token-based algorithms are Lamport's algorithm, Ricart-Agrawala algorithm, and Maekawa's algorithm  .

- **Quorum-based approach**: This is a generalization of the non-token-based approach. A process requests permission from a subset of processes, called a quorum, to enter its critical section. A process can enter its critical section only if it receives grant messages from all the processes in the quorum. The quorum can be defined in different ways, such as a majority, a fixed set, or a dynamic set. Examples of quorum-based algorithms are Maekawa's algorithm, Agrawala's algorithm, and Thomas's algorithm  .

The following diagram illustrates the classification of distributed mutual exclusion algorithms:

```
+-----------------------------------+
|   Distributed Mutual Exclusion    |
+-----------------------------------+
|                                   |
+-----------------+-----------------+
| Token-based    | Non-token-based |
+-----------------+-----------------+
|                 |                 |
| Ricart-Agrawala | Lamport         |
| Suzuki-Kasami   | Ricart-Agrawala |
| Raymond         | Maekawa         |
|                 |                 |
+-----------------+-----------------+
                  |
                  |
                  v
+-----------------+
| Quorum-based    |
+-----------------+
|                 |
| Maekawa         |
| Agrawala        |
| Thomas          |
|                 |
+-----------------+
```



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is the content I have generated for you in markdown format:

### Requirement of mutual exclusion theorem for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM

- Mutual exclusion is a concurrency control property which is introduced to prevent race conditions.
- Race conditions occur when multiple processes access a shared resource or data simultaneously and the outcome depends on the order of execution.
- Mutual exclusion ensures that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner  .
- Mutual exclusion in a distributed system states that only one process is allowed to execute the critical section (CS) at any given time  .
- A critical section is a piece of code that accesses a shared resource or data.
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion .
- Message passing is the sole means for implementing distributed mutual exclusion .
- There are three basic approaches for implementing distributed mutual exclusion:
  - Token-based algorithms: A process can enter the CS only if it possesses a unique token that circulates in the system.
  - Permission-based algorithms: A process can enter the CS only if it obtains permission from a set of processes in the system.
  - Quorum-based algorithms: A process can enter the CS only if it obtains permission from a subset of processes in the system that forms a quorum.
- The requirement of mutual exclusion theorem is to ensure the correctness and consistency of the distributed system.
- The mutual exclusion theorem states that any algorithm that solves the distributed mutual exclusion problem must satisfy the following properties:
  - Safety: No two processes can be in the CS at the same time.
  - Liveness: Every request to enter the CS is eventually granted.
  - Fairness: No process is indefinitely postponed from entering the CS.
- The mutual exclusion theorem provides a formal specification and a correctness criterion for the distributed mutual exclusion algorithms.



### Token based and non token based algorithms for distributed mutual exclusion

Distributed mutual exclusion (DME) is the problem of ensuring that only one process at a time can access a shared resource in a distributed system. There are two main types of algorithms for DME: token based and non token based.

#### Token based algorithms

- In token based algorithms, a unique token is shared among all the processes in the system. The token represents the permission to enter the critical section. Only the process that holds the token can access the shared resource.
- Token based algorithms are simple and efficient, as they require only one message (the token) to be exchanged per critical section entry. However, they have some drawbacks, such as:
  - The token may be lost or duplicated due to message failures or process crashes, leading to deadlock or violation of mutual exclusion.
  - The token may cause unnecessary delays if it is far away from the requesting process, leading to low system utilization.
  - The token may not reflect the current requests of the processes, leading to unfairness or starvation.
- Some examples of token based algorithms are:
  - The centralized algorithm, where one process acts as the token manager and grants the token to the processes in a fixed or dynamic order.
  - The ring algorithm, where the processes are arranged in a logical ring and pass the token along the ring in a clockwise or anticlockwise direction.
  - The Suzuki-Kasami algorithm, where the token contains a vector of requests from all the processes and is sent to the process with the highest request number.

#### Non token based algorithms

- In non token based algorithms, there is no token in the system. Instead, the processes communicate with each other using messages to request, grant, or release the permission to enter the critical section.
- Non token based algorithms are more robust and flexible, as they can tolerate message failures and process crashes, and can adapt to the changing requests of the processes. However, they have some drawbacks, such as:
  - They require more messages to be exchanged per critical section entry, leading to higher communication overhead and network congestion.
  - They may cause deadlock or livelock if the messages are delayed or lost, or if the processes do not follow the same protocol or order.
  - They may require global synchronization or knowledge of the system state, leading to scalability and privacy issues.
- Some examples of non token based algorithms are:
  - The Lamport's algorithm, where the processes use logical timestamps to order the requests and grant the permission to the process with the smallest timestamp.
  - The Ricart-Agrawala algorithm, where the processes use logical timestamps and multicast messages to request and reply the permission to enter the critical section.
  - The Maekawa's algorithm, where the processes form a voting set and request the permission from a majority of the voting set members .



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on the performance metric for distributed mutual exclusion algorithms for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM.

### Performance metric for distributed mutual exclusion algorithms

- Distributed mutual exclusion algorithms are protocols that allow processes in a distributed system to access a shared resource without violating the mutual exclusion property, which states that at most one process can be in the critical section (CS) at any time.
- The performance of distributed mutual exclusion algorithms is generally measured by the following four metrics :

  - **Message complexity**: It is the number of messages that are required per CS execution by a site. It reflects the communication overhead and network congestion caused by the algorithm. The lower the message complexity, the better the performance.
  - **Synchronization delay**: After a site leaves the CS, it is the time required before the next site enters the CS. It reflects the degree of concurrency and fairness achieved by the algorithm. The lower the synchronization delay, the better the performance.
  - **Response time**: It is the time interval between a site's request for the CS and its entry to the CS. It reflects the waiting time and latency experienced by the site. The lower the response time, the better the performance.
  - **Throughput**: It is the number of CS executions per unit time in the system. It reflects the efficiency and utilization of the shared resource. The higher the throughput, the better the performance.

- Different types of distributed mutual exclusion algorithms can be compared in terms of performance through simulations. A simulation-based approach can provide insights into the behavior and trade-offs of different algorithms under various scenarios and parameters .
- Some examples of distributed mutual exclusion algorithms are:

  - **Central server algorithm**: In this algorithm, one process takes the role of coordinator, receiving requests to access the CS from all other processes, and granting access based on a FIFO queue. This algorithm has a message complexity of 3 messages per CS execution, a synchronization delay of 0, and a response time of 2 message transmission times. However, it has a low throughput and a single point of failure.
  - **Ricart-Agrawala algorithm**: In this algorithm, each process broadcasts its request for the CS to all other processes, and enters the CS only when it receives a reply from all other processes. This algorithm has a message complexity of 2(n-1) messages per CS execution, where n is the number of processes, a synchronization delay of 0, and a response time of 2 message transmission times. However, it has a high communication overhead and network congestion.
  - **Lamport's algorithm**: In this algorithm, each process maintains a logical clock and a request queue, and sends its request for the CS with its timestamp to all other processes. A process enters the CS only when it has the smallest timestamp in the queue and has received a reply from all other processes. This algorithm has a message complexity of 3(n-1) messages per CS execution, a synchronization delay of 0, and a response time of 2 message transmission times. However, it has a higher communication overhead than Ricart-Agrawala algorithm and requires clock synchronization.




## Unit 3 - Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set.
- Deadlocks can occur in distributed systems when distributed transactions or concurrency control are utilized.
- Deadlock detection is the approach of identifying and resolving existing deadlocks in distributed systems.
- Deadlock detection requires examination of the status of process-resource interactions for presence of cyclic wait.
- Deadlock detection in distributed systems entails addressing two basic issues:
  - Detection of existing deadlocks
  - Resolution of detected deadlocks
- There are three main approaches to detect deadlocks in distributed systems:
  - Centralized deadlock detection
    - A single node is designated as the deadlock detector and maintains a global wait-for graph (WFG) of the system
    - The other nodes periodically send their local WFGs to the deadlock detector
    - The deadlock detector checks the global WFG for cycles and initiates recovery actions if needed
    - Advantages: simple, efficient, low overhead
    - Disadvantages: single point of failure, bottleneck, scalability issues
  - Distributed deadlock detection
    - Each node maintains its own local WFG and participates in a distributed algorithm to detect cycles in the global WFG
    - The distributed algorithm can be based on edge chasing, diffusing computation, or hierarchical deadlock detection
    - Advantages: fault tolerance, load balancing, scalability
    - Disadvantages: complex, high overhead, message delays
  - Hierarchical deadlock detection
    - The nodes are organized into a hierarchy of clusters, each with a coordinator node
    - The coordinator nodes maintain partial WFGs of their clusters and communicate with each other to detect cycles in the global WFG
    - The coordinator nodes can also delegate the deadlock detection to lower-level nodes if needed
    - Advantages: hybrid of centralized and distributed approaches, adaptable to system topology, reduced overhead
    - Disadvantages: complex, hierarchical structure, message delays
- To resolve the deadlock, one or more deadlocked processes have to be aborted and their resources have to be released.
- The selection of the processes to be aborted can be based on various criteria, such as priority, age, cost, or number of resources held.
- The aborted processes can be restarted from the beginning or from a checkpoint.



### System Model for Distributed Deadlock Detection

- A distributed system consists of a set of nodes that communicate by message passing.
- Each node has a set of resources that can be requested by processes running on the node or on other nodes.
- A process can request a resource by sending a message to the node that owns the resource.
- A node can grant a resource to a process by sending a message to the process or by placing the resource in a shared buffer.
- A process can release a resource by sending a message to the node that owns the resource or by removing the resource from a shared buffer.
- A process can hold multiple resources at a time and can request additional resources while holding some resources.
- A process can be blocked if it is waiting for a resource that is not available.
- A deadlock occurs when a set of processes are blocked and each process is waiting for a resource that is held by another process in the set.
- A wait-for graph (WFG) is a directed graph that represents the resource requests and grants in the system. Each node in the WFG is a process and each edge is a resource dependency. An edge from process P to process Q means that P is waiting for a resource that is held by Q.
- A cycle in the WFG indicates a deadlock in the system. A deadlock can be detected by finding a cycle in the WFG.
- There are three main approaches to deadlock detection in distributed systems: centralized, hierarchical, and distributed.
- In the centralized approach, there is a designated node that collects the local WFGs from all the nodes and constructs a global WFG. The designated node then searches for a cycle in the global WFG and initiates a recovery action if a deadlock is found.
- In the hierarchical approach, there is a tree structure of nodes that are responsible for deadlock detection. Each node collects the local WFGs from its children and constructs a partial WFG. The root node collects the partial WFGs from its children and constructs a global WFG. The root node then searches for a cycle in the global WFG and initiates a recovery action if a deadlock is found.
- In the distributed approach, there is no designated node or tree structure for deadlock detection. Each node participates in the deadlock detection algorithm by sending and receiving messages. There are two main types of distributed algorithms: path-pushing and edge-chasing.
- In the path-pushing algorithm, each node maintains a set of paths that represent the resource dependencies in the system. A path is a sequence of processes that are waiting for resources. Each node periodically sends its paths to its neighbors and updates its paths based on the received paths. A node detects a deadlock if it receives a path that contains itself.
- In the edge-chasing algorithm, each node initiates a probe message when it is blocked. A probe message is a token that contains the identity of the initiator and the sequence of processes that have forwarded the probe. Each node forwards the probe message to the process that holds the resource that it is waiting for. A node detects a deadlock if it receives a probe message that contains its own identity.



### Resource vs Communication Deadlocks

- A **resource deadlock** occurs when a set of processes requests resources that are already occupied by other processes in the group . Because each process possesses a resource and waits for another resource held by another process, the execution of two or more processes is blocked.
- A **communication deadlock** occurs when a set of processes is blocked due to message passing. A process may wait for a message that will never arrive, or a message may be lost or corrupted due to network failures.
- Resource deadlocks and communication deadlocks have different characteristics and require different detection and resolution techniques.
- Some of the differences are :

| Resource Deadlocks | Communication Deadlocks |
|--------------------|-------------------------|
| Processes access resources, such as data objects in database systems and buffers in store and forward communication networks. | Processes exchange messages, such as requests and replies in client-server systems and acknowledgments in reliable communication protocols. |
| A process acquires a resource before accessing it and releases it after using it. | A process sends a message before receiving a reply and waits for a reply after sending a message. |
| A resource can be shared by multiple processes or exclusively owned by one process. | A message can be broadcast to multiple processes or unicast to one process. |
| A resource can be preempted from a process or held until the process voluntarily releases it. | A message can be retransmitted or dropped if it is lost or corrupted. |
| A resource deadlock can be detected by constructing a wait-for graph that shows which process is waiting for which resource. | A communication deadlock can be detected by constructing a dependency graph that shows which process is waiting for which message. |
| A resource deadlock can be resolved by aborting one or more processes or preempting one or more resources. | A communication deadlock can be resolved by sending a dummy message or a timeout signal to one or more processes. |



### Deadlock Prevention for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process. In a distributed system, deadlocks are more difficult to detect and resolve because the processes and resources may be physically dispersed across different nodes.

Deadlock prevention is a technique to ensure that at least one of the necessary conditions for deadlock does not hold in the system. There are two main methods of deadlock prevention in a distributed system:

- Ordered request: In this method, each resource type is assigned a unique level, and a process can request resources only in increasing order of levels. This prevents circular wait condition, as no process can hold a resource of higher level and wait for a resource of lower level. For example, if there are three resource types A, B, and C with levels 1, 2, and 3 respectively, then a process can request A, then B, then C, but not C, then A, then B.
- Collective request: In this method, a process must request all the resources it needs at the same time, and either get all of them or none of them. This prevents hold and wait condition, as no process can hold some resources and wait for others. For example, if a process needs resources A, B, and C, then it must request them together, and not request A, then wait for B, then request C.

Both methods have some drawbacks, such as reduced concurrency, increased overhead, and wasted resources. Therefore, deadlock prevention may not be suitable for all distributed systems, and other techniques such as deadlock avoidance or deadlock detection and recovery may be preferred.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM:

### Avoidance

- Avoidance is a technique to prevent deadlocks from occurring in a distributed system by ensuring that the system is always in a safe state.
- A safe state is a state where there is a sequence of resource allocations that can satisfy the requests of all processes without causing a deadlock.
- A system is in an unsafe state if there is no such sequence of resource allocations.
- Avoidance requires the system to have some knowledge of the current and future resource requests of the processes, which may not be feasible or accurate in a distributed system.
- Avoidance also requires the system to make decisions about granting or denying resource requests based on the global state of the system, which may be difficult or costly to obtain in a distributed system.
- Therefore, avoidance is impractical in distributed systems and deadlock detection is preferred as a better approach to handle deadlocks in distributed systems .

### References

: Deadlock Detection in Distributed Systems - University of Illinois Chicago
: Deadlock Avoidance in Distributed System - GeeksforGeeks



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of distributed deadlock detection and resolution.

### Detection and Resolution

- A deadlock is a situation where a set of processes are blocked waiting for resources that are held by other processes in the same set.
- Deadlocks can be prevented, avoided, or detected and resolved in distributed systems.
- Deadlock detection involves two steps: maintaining a wait-for graph (WFG) that represents the dependencies among processes and resources, and searching the WFG for cycles or knots that indicate deadlocks.
- Deadlock resolution involves breaking the existing wait-for dependencies in the WFG by aborting or rolling back some of the deadlocked processes and releasing their resources to the blocked processes in the deadlock.
- Deadlock detection and resolution can be centralized, distributed, or hierarchical, depending on how the WFG is maintained and searched.
- Centralized deadlock detection and resolution involves a single coordinator process that collects information from all the processes in the system and maintains and searches the global WFG.
- Distributed deadlock detection and resolution involves each process maintaining and searching its local WFG and exchanging messages with other processes to detect global deadlocks.
- Hierarchical deadlock detection and resolution involves a tree structure of coordinators that maintain and search partial WFGs and communicate with each other to detect global deadlocks.
- Deadlock detection and resolution algorithms should be resilient to failures, such as process crashes, message losses, or network partitions.
- Deadlock detection and resolution algorithms should also be efficient, accurate, and scalable, minimizing the communication and computation overhead, the false or phantom deadlocks, and the response time.



### Centralized Deadlock Detection

- This is a technique used in distributed systems to handle deadlock detection.
- According to this approach, the system maintains one global wait-for graph in a single chosen site, which is named as deadlock-detection coordinator.
- The coordinator collects information about the local wait-for graphs of each site and constructs the global wait-for graph.
- The coordinator periodically runs a deadlock detection algorithm on the global wait-for graph to identify any cycles.
- If a cycle is detected, the coordinator selects a victim process from the cycle and sends an abort message to the corresponding site.
- The site that receives the abort message terminates the victim process and releases its resources.
- The advantages of this approach are simplicity and low communication overhead.
- The disadvantages of this approach are single point of failure, scalability issues, and lack of autonomy.

: https://www.exploredatabase.com/2014/06/centralized-deadlock-detection-approach-in-distributed-database.html
: https://www.javatpoint.com/deadlock-detection-in-distributed-systems
: https://people.cs.rutgers.edu/~pxk/417/notes/deadlock.html
: https://www.geeksforgeeks.org/deadlock-detection-in-distributed-systems/



### Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set.
- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems.
- Deadlock detection in distributed systems entails addressing two basic issues: detection of existing deadlocks and resolution of detected deadlocks.
- Deadlock detection requires examination of the status of process-resource interactions for presence of cyclic wait.
- There are three approaches to detect deadlocks in distributed systems:
  - Centralized approach: A single node is designated as the deadlock detector and collects information from all other nodes to construct a global wait-for graph (WFG) and check for cycles.
  - Hierarchical approach: The nodes are organized into a hierarchy of clusters and each cluster has a coordinator that collects information from its members and communicates with other coordinators to construct a partial WFG and check for cycles.
  - Distributed approach: Each node maintains a local WFG and initiates a probe message along the edges of the WFG to detect cycles.
- To resolve the deadlock, one or more processes involved in the deadlock have to be aborted or preempted.
- The criteria for selecting a victim process include: process priority, process age, process state, number of resources held, number of resources requested, etc.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on path pushing algorithms for distributed deadlock detection:

### Path Pushing Algorithms

- Path pushing algorithms detect distributed deadlocks by maintaining an explicit global wait-for graph (WFG) at each site of the distributed system .
- A WFG is a directed graph that represents the dependencies among processes or transactions in a system. A node in a WFG represents a process or a transaction, and an edge from node A to node B represents that A is waiting for a resource held by B .
- The basic idea of path pushing algorithms is to build a global WFG for each site by sending the local WFG to all the neighboring sites whenever a deadlock computation is performed .
- A site initiates a deadlock computation when it detects a local deadlock or receives a request from another site. A site can detect a local deadlock by checking for a cycle in its local WFG .
- A site can detect a global deadlock by checking for a cycle in its global WFG. If a cycle is found, the site can initiate a resolution procedure to break the deadlock .
- Path pushing algorithms have the advantage of detecting deadlocks quickly and accurately, since they maintain the complete global WFG at each site .
- However, path pushing algorithms have the disadvantage of requiring a large amount of communication and storage overhead, since they need to send and store the entire WFG at each site .

Here is a diagram that illustrates the path pushing algorithm:

Path Pushing Algorithm

- In this example, there are four sites (S1, S2, S3, S4) and six processes (P1, P2, P3, P4, P5, P6) in the distributed system.
- The edges in the WFGs represent the dependencies among the processes. For example, P1 is waiting for a resource held by P2, and P2 is waiting for a resource held by P3.
- Initially, each site has its own local WFG, which is a subgraph of the global WFG.
- S1 detects a local deadlock involving P1, P2, and P3, and initiates a deadlock computation by sending its local WFG to all the neighboring sites (S2, S3, S4).
- S2, S3, and S4 receive the local WFG from S1 and update their global WFGs by merging the received WFG with their own local WFGs.
- S2 detects a global deadlock involving P1, P2, P3, and P4, and initiates a resolution procedure by sending a message to S1 to abort P1.
- S1 receives the message from S2 and aborts P1, breaking the deadlock.




### Edge Chasing Algorithms for Distributed Deadlock Detection

- Edge chasing algorithms are a class of distributed deadlock detection algorithms that use special messages called probes to trace the dependency graph of processes and resources in a distributed system .
- A probe is a triplet (i, j, k) that denotes that the deadlock detection is initiated by process P_i and the message is being sent by the home site of process P_j to the home site of process P_k .
- The probe message contains the information about the initiator process, the sender process and the receiver process of the message, as well as the dependency path of the processes involved in the deadlock detection .
- The algorithm works as follows :
  - A process P_i initiates the deadlock detection by sending a probe message (i, i, j) to the home site of process P_j, where P_j is a process that P_i is waiting for.
  - The home site of process P_j forwards the probe message to the home site of process P_k, where P_k is a process that P_j is waiting for, and so on.
  - If a probe message (i, j, i) reaches the home site of process P_i, then a deadlock involving process P_i is detected.
  - If a probe message (i, j, k) reaches the home site of process P_k, where P_k is not waiting for any other process, then the probe message is discarded and no deadlock is detected.
  - If a probe message (i, j, k) reaches the home site of process P_k, where P_k is waiting for a process that is not in the dependency path of the probe message, then the probe message is updated with the new dependency path and forwarded to the home site of the process that P_k is waiting for.
- The algorithm terminates when either a deadlock is detected or all the probe messages are discarded .
- The algorithm is based on the AND model of requests, which means that a process can request multiple resources simultaneously and it will be blocked until it acquires all the requested resources .
- The algorithm has the following advantages and disadvantages :
  - Advantages:
    - It is simple and easy to implement.
    - It does not require any global information or synchronization among the sites.
    - It can detect deadlocks involving cycles of any length and complexity.
  - Disadvantages:
    - It may generate a large number of probe messages, which can cause network congestion and delay.
    - It may detect false deadlocks, which are deadlocks that do not exist in the actual system state but are caused by the delay or loss of messages.
    - It may miss some deadlocks, which are deadlocks that exist in the actual system state but are not detected by the algorithm due to the interference of other messages or events.



## Unit 4 - Agreement Protocols

- Agreement protocols are a class of distributed algorithms that allow a set of processes to reach a common decision or consensus, despite the possibility of failures or malicious behavior.
- Agreement protocols are useful for implementing fault-tolerant services, such as distributed databases, replicated state machines, leader election, atomic broadcast, etc.
- Agreement protocols can be classified into different types, depending on the assumptions and guarantees they provide. Some common types are:
  - **Byzantine agreement**: The processes can have arbitrary faults or behave maliciously, and the protocol guarantees that all correct processes agree on the same value, and the value is proposed by some correct process.
  - **Crash-recovery agreement**: The processes can only have crash faults or recover from faults, and the protocol guarantees that all correct processes agree on the same value, and the value is proposed by some correct process.
  - **Crash-stop agreement**: The processes can only have crash faults and do not recover, and the protocol guarantees that all correct processes agree on the same value, and the value is proposed by some correct process.
  - **Uniform agreement**: The protocol guarantees that all correct processes agree on the same value, regardless of the type of faults or behavior of the processes.
  - **Non-uniform agreement**: The protocol guarantees that all correct processes agree on the same value, only if they receive the same set of messages from other processes.
- Agreement protocols can also be classified into different models, depending on the communication and timing assumptions they make. Some common models are:
  - **Synchronous model**: The processes have bounded message delays and clock drifts, and the protocol can use timeouts and rounds to synchronize the processes.
  - **Asynchronous model**: The processes have no bounds on message delays and clock drifts, and the protocol cannot use timeouts and rounds to synchronize the processes.
  - **Partially synchronous model**: The processes have bounded message delays and clock drifts, but the bounds are unknown or may change over time, and the protocol can use adaptive timeouts and rounds to synchronize the processes.
  - **Hybrid model**: The processes have different communication and timing assumptions, depending on the type of faults or behavior they exhibit, and the protocol can use different mechanisms to synchronize the processes.
- Agreement protocols can also be classified into different variants, depending on the number and type of values they can agree on. Some common variants are:
  - **Binary agreement**: The processes can only propose and agree on two values, usually 0 and 1.
  - **Multi-valued agreement**: The processes can propose and agree on any value from a finite domain.
  - **Generalized agreement**: The processes can propose and agree on any value from an infinite domain, such as real numbers.
  - **Consensus**: The processes can propose and agree on any value, and the value is proposed by some correct process.
  - **k-set agreement**: The processes can propose and agree on any value, and the number of distinct values agreed on is at most k.



Hello, I am Sydney, your AI assistant. I can help you with writing notes on various topics. Here is the content I have generated for the introduction of the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM.

### Introduction

- Agreement protocols are a class of protocols that allow a set of processes in a distributed system to reach a consensus on some value or action, despite the presence of failures or uncertainties.
- Agreement protocols are essential for ensuring the correctness, consistency, and reliability of distributed systems, especially in applications such as distributed databases, fault-tolerant systems, distributed transactions, distributed consensus, and distributed coordination.
- Agreement protocols can be classified into different types based on the following criteria:
  - The type of failures that the protocol can tolerate, such as crash failures, omission failures, timing failures, or Byzantine failures.
  - The type of communication model that the protocol assumes, such as synchronous, asynchronous, or partially synchronous.
  - The type of value or action that the protocol aims to agree on, such as a single value, a set of values, a total order, or a partial order.
  - The type of termination condition that the protocol guarantees, such as always, eventually, or probabilistically.
- Some of the common agreement problems that are studied in distributed systems are:
  - Consensus: The processes have to agree on a single value proposed by one or more processes.
  - Atomic Commit: The processes have to agree on whether to commit or abort a distributed transaction.
  - Atomic Broadcast: The processes have to agree on a total order of messages broadcast by one or more processes.
  - Group Membership: The processes have to agree on the current set of processes that are alive and participating in the system.
  - Leader Election: The processes have to agree on a unique process that acts as the leader or coordinator of the system.
- Some of the challenges and limitations of designing agreement protocols are:
  - The impossibility of consensus in asynchronous systems with crash failures, as proved by the FLP theorem.
  - The impossibility of atomic broadcast in asynchronous systems with Byzantine failures, as proved by the CAP theorem.
  - The trade-off between fault tolerance and performance, as increasing the number of processes or the number of rounds of communication increases the resilience to failures but also increases the latency and overhead of the protocol.
  - The trade-off between safety and liveness, as ensuring that the protocol always satisfies some correctness property may prevent it from making progress or terminating in some scenarios.



### System models for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

A system model is a description of the properties and assumptions of a distributed system that are relevant for its design and analysis. System models can help us understand the behavior and limitations of a distributed system, and guide us in choosing appropriate algorithms and protocols for achieving certain goals.

There are different types of system models, depending on what aspects of a distributed system we want to focus on. Some of the most common system models are:

- Architectural models: These models describe the structure and organization of the components of a distributed system, and how they communicate and interact with each other. Examples of architectural models are client-server, peer-to-peer, publish-subscribe, and service-oriented architectures.
- Interaction models: These models describe the patterns and rules of communication and coordination among the components of a distributed system, and how they achieve consistency and agreement. Examples of interaction models are message passing, remote procedure call, remote method invocation, and distributed shared memory.
- Fault models: These models describe the types and causes of failures that can occur in a distributed system, and how they affect the system's behavior and performance. Examples of fault models are crash, omission, timing, response, arbitrary, and Byzantine faults.
- Timing models: These models describe the assumptions and properties of the clocks and timers of the components of a distributed system, and how they affect the system's behavior and performance. Examples of timing models are synchronous, asynchronous, and partially synchronous systems.

One of the main challenges of designing and analyzing distributed systems is to cope with the uncertainty and unpredictability of the system's environment, such as network delays, node failures, clock drifts, and malicious attacks. System models can help us abstract away some of the complexity and uncertainty of the system's environment, and provide us with a simplified and idealized view of the system's behavior and performance. However, system models also have limitations and trade-offs, and they may not always reflect the reality of the system's environment accurately or completely. Therefore, it is important to choose a system model that is appropriate and realistic for the problem domain and the system requirements.

One of the most important problems in distributed systems is the agreement problem, which is the problem of reaching a common decision or value among a set of nodes in the presence of faults and uncertainty. Agreement protocols are algorithms and protocols that solve the agreement problem under certain system models and assumptions. Examples of agreement protocols are consensus, atomic broadcast, atomic commit, and leader election.

The choice of a system model can have a significant impact on the feasibility and complexity of an agreement protocol. For example, consensus is impossible to achieve in an asynchronous system with crash faults, but it is possible in a partially synchronous system with crash faults, or in an asynchronous system with failure detectors. Similarly, atomic broadcast is impossible to achieve in an asynchronous system with Byzantine faults, but it is possible in a synchronous system with Byzantine faults, or in an asynchronous system with digital signatures. Therefore, it is important to understand the system model and its assumptions and limitations when designing and analyzing an agreement protocol.



### Classification of Agreement Problem

An agreement problem is a problem where a set of processes in a distributed system need to reach a common decision based on their local inputs and messages exchanged with each other. Agreement problems are important for achieving coordination, consistency, and fault tolerance in distributed systems. There are different types of agreement problems, depending on the assumptions and requirements of the system model. Some of the common agreement problems are:

- **Byzantine agreement problem**: In this problem, each process has an initial value and needs to decide on a final value, such that all correct processes agree on the same value and the value is the initial value of some correct process. The system may have some faulty processes that can behave arbitrarily (Byzantine faults). The goal is to tolerate as many faulty processes as possible and reach agreement despite their malicious behavior.
- **Consensus problem**: In this problem, each process has an initial value and needs to decide on a final value, such that all correct processes agree on the same value and the value is the initial value of some correct process. The system may have some faulty processes that can crash (fail-stop faults). The goal is to reach agreement despite the possibility of process crashes.
- **Interactive consistency problem**: In this problem, each process has an initial value and needs to decide on a vector of values, such that the vector contains the initial values of all processes and all correct processes agree on the same vector. The system may have some faulty processes that can behave arbitrarily (Byzantine faults). The goal is to achieve consistency among the processes and ensure that the correct processes know the initial values of all processes.
- **Atomic commitment problem**: In this problem, each process has an initial value that indicates whether it is willing to commit or abort a transaction, and needs to decide on a final value that indicates whether the transaction is committed or aborted, such that all correct processes agree on the same value and the value is commit only if all processes are willing to commit. The system may have some faulty processes that can crash (fail-stop faults) or send incorrect messages (Byzantine faults). The goal is to ensure atomicity and durability of the transaction.



### Byzantine agreement problem

- The Byzantine agreement problem is a fundamental problem in fault tolerant distributed computing that requires a set of parties in a distributed environment to agree on a value even if some of the parties are corrupted.
- The problem was first defined by Lamport and inspired by a hypothetical scenario of several divisions of the Byzantine army camped outside an enemy city, each division commanded by its own general.
- The generals can communicate with one another only by messenger and they must decide upon a common plan of action, such as attack or retreat.
- However, some of the generals may be traitors and try to prevent the loyal generals from reaching an agreement.
- A solution to the Byzantine agreement problem is a protocol that ensures that all loyal generals agree on the same value and that the value is the initial value of some loyal general.
- A solution must also be resilient to arbitrary failures, such as message loss, message delay, message alteration, or message duplication.
- A solution must also be efficient, meaning that it uses a reasonable amount of communication and computation resources.
- A number of solutions to the Byzantine agreement problem exist, such as the oral messages algorithm, the signed messages algorithm, the interactive consistency algorithm, and the practical Byzantine fault tolerance algorithm  .
- The Byzantine agreement problem is relevant for many applications in distributed systems, such as consensus protocols, distributed databases, distributed ledgers, peer-to-peer networks, and cloud computing .



### Consensus problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- The consensus problem is the problem of getting a set of nodes in a distributed system to agree on something - it might be a value, a course of action or a decision.
- Achieving consensus allows a distributed system to act as a single entity, with every individual node aware of and in agreement with the actions of the whole of the network.
- Consensus is a general agreement on a decision made by the majority of those involved.
- Consensus is needed in a distributed system to ensure overall system reliability on top of unreliable system components.
- Consensus is also needed to coordinate the actions of different nodes, such as committing transactions, electing leaders, replicating data, etc.
- Consensus is hard to achieve in a distributed system due to the possibility of failures, such as node crashes, network partitions, message losses, etc.
- Consensus algorithms are protocols that enable nodes to reach consensus in a distributed system despite failures.
- Consensus algorithms have to satisfy some properties, such as:
  - Termination: every correct node eventually decides on a value.
  - Agreement: every correct node that decides, decides on the same value.
  - Validity: if a correct node decides on a value, then that value was proposed by some node.
- Some examples of consensus algorithms are:
  - Two-phase commit: a simple protocol that involves a coordinator node and a set of participant nodes. The coordinator proposes a value and asks the participants to vote. If all participants agree, the coordinator commits the value and notifies the participants. Otherwise, the coordinator aborts the value and notifies the participants.
  - Paxos: a more complex protocol that involves a set of proposer nodes, a set of acceptor nodes, and a set of learner nodes. The proposers propose values and the acceptors vote on them. The learners learn the decided value from the acceptors. The protocol ensures that at most one value is decided and that value is chosen by a majority of acceptors.
  - Raft: a simpler protocol that involves a set of server nodes and a set of client nodes. The servers elect a leader among themselves and the leader proposes values to the followers. The followers append the values to their logs and acknowledge the leader. The leader commits the values when a majority of followers have appended them. The clients interact with the leader to propose values or query the system state.



### Interactive Consistency Problem

- Interactive consistency is the problem in which n distinct nodes, each having its own private value, where up to t may be Byzantine, run an algorithm that allows all non-faulty nodes to infer the values of each other node  .
- Byzantine nodes are nodes that can behave arbitrarily, such as sending conflicting or incorrect messages, or remaining silent .
- Interactive consistency is a generalization of the consensus problem, where the goal is to reach agreement on a single value among all non-faulty nodes.
- Interactive consistency is relevant to critical applications that rely on the combination of the opinions of multiple peers to provide a service, such as fault-tolerant distributed systems, blockchain systems, or voting systems.
- Interactive consistency is also known as the Byzantine Generals Problem, which is a metaphor for the situation where a group of generals must coordinate an attack or retreat, but some of them may be traitors who try to sabotage the plan .
- Interactive consistency is a hard problem to solve, especially in asynchronous or partially synchronous systems, where there is no guarantee on the delivery time or order of messages, or the accuracy of clocks .
- Interactive consistency requires at least n > 3t nodes to be solvable, where t is the maximum number of Byzantine nodes  .
- Interactive consistency can be solved using various algorithms, such as the Oral Messages Algorithm, the Signed Messages Algorithm, the Exponential Information Gathering Algorithm, or the Randomized Byzantine Consensus Algorithm  .
- Interactive consistency algorithms typically involve multiple rounds of message exchange, where each node broadcasts its value or a function of its value to all other nodes, and then updates its vector of inferred values based on the received messages  .
- Interactive consistency algorithms must satisfy two properties: validity and agreement  .
  - Validity: If a node is non-faulty, then every non-faulty node infers its value correctly.
  - Agreement: Every non-faulty node infers the same value for every other node.



### Solution to Byzantine Agreement problem

The Byzantine Agreement problem is a fundamental challenge in fault-tolerant distributed computing. It requires a set of processors in a distributed system to agree on a common value, even if some of the processors are faulty or malicious. The faulty processors may behave arbitrarily, sending inconsistent or incorrect messages to other processors, or colluding with each other to disrupt the agreement.

A solution to the Byzantine Agreement problem must satisfy the following properties:

- **Validity**: If all the processors start with the same initial value, then they must all agree on that value.
- **Agreement**: No two non-faulty processors can decide on different values.
- **Termination**: Every non-faulty processor must eventually decide on a value.

There are different variants of the Byzantine Agreement problem, depending on the assumptions about the communication model, the number and type of faults, and the synchrony of the system. Some of the variants are:

- **Oral messages**: The processors communicate by sending messages over a reliable but unauthenticated channel. The messages may be tampered by faulty processors, but not lost or duplicated.
- **Signed messages**: The processors communicate by sending messages over a reliable and authenticated channel. The messages are digitally signed by the sender, and cannot be forged or altered by faulty processors.
- **Broadcast**: The processors communicate by sending messages to all other processors in one step. The messages are either oral or signed, depending on the variant.
- **Byzantine Generals**: The processors are divided into two groups: loyal and traitorous. The loyal processors follow the protocol, while the traitorous processors may deviate from it. The goal is to reach agreement among the loyal processors, despite the presence of traitors.
- **Crash faults**: The processors may fail by crashing, i.e., stopping to send or receive messages. The processors do not behave maliciously or send incorrect messages.
- **Synchronous**: The processors have a common notion of time, and the messages are delivered within a known bounded delay.
- **Asynchronous**: The processors do not have a common notion of time, and the messages may be delivered with arbitrary delays.

Depending on the variant, different solutions to the Byzantine Agreement problem exist. Some of the solutions are:

- **Lamport, Shostak, and Pease (1982)**: This is the first solution to the Byzantine Agreement problem with oral messages. It assumes that the system is synchronous, and that the number of faulty processors is less than one-third of the total number of processors. The solution is based on a recursive algorithm that uses majority voting and message relaying to reach agreement.
- **Dolev, Strong, and Reischuk (1983)**: This is a solution to the Byzantine Agreement problem with signed messages. It assumes that the system is asynchronous, and that the number of faulty processors is less than half of the total number of processors. The solution is based on a graph-theoretic algorithm that uses message authentication and message propagation to reach agreement.
- **Bracha (1985)**: This is a solution to the Byzantine Agreement problem with broadcast and oral messages. It assumes that the system is asynchronous, and that the number of faulty processors is less than one-third of the total number of processors. The solution is based on a four-phase algorithm that uses broadcast, echo, and ready messages to reach agreement.
- **Castro and Liskov (1999)**: This is a solution to the Byzantine Agreement problem with broadcast and signed messages. It assumes that the system is asynchronous, and that the number of faulty processors is less than one-third of the total number of processors. The solution is based on a practical state machine replication algorithm that uses quorums, checkpoints, and view changes to reach agreement.

These are some of the main solutions to the Byzantine Agreement problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM. For more details, please refer to the following sources:

: https://www.thecode11.com/2022/07/byzantine-agreement-problem-in-distributed-system.html
: https://www.prismmodelchecker.org/casestudies/byzantine.php
: https://ijcsit.com/docs/Volume%209/vol9issue1/ijcsit2018090101.pdf
: https://en.wikipedia.org/wiki/Byzantine_fault
: https://komodoplatform.com/en/academy/byzantine-generals-problem/
:



### Application of Agreement problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- Agreement problem is a fundamental problem in distributed computing and multi-agent systems that requires coordinating processes to reach consensus, or agree on some data value that is needed during computation .
- Agreement problem is essential for achieving overall system reliability in the presence of a number of faulty processes .
- Agreement problem has many variants, such as consensus, atomic commitment, atomic broadcast, and group membership.
- Consensus is the problem of getting all processes to agree on a single value, such as the result of an election or the state of a replicated object .
- Atomic commitment is the problem of getting all processes to agree on whether to commit or abort a transaction, such as a database update or a money transfer .
- Atomic broadcast is the problem of getting all processes to deliver the same set of messages in the same order, such as a log of events or a sequence of commands .
- Group membership is the problem of getting all processes to agree on the current set of active processes in the system, such as a cluster of servers or a network of sensors .
- Agreement problem is challenging to solve in distributed systems because of the possibility of communication failures, process crashes, and malicious behavior  .
- Agreement problem has many applications in distributed systems, such as fault tolerance, replication, consistency, synchronization, distributed transactions, distributed consensus, and distributed ledger    .



### Atomic Commit in Distributed Database System

- A distributed database system consists of multiple database sites that are connected by a communication network.
- A distributed transaction is a transaction that accesses data from multiple sites and updates them atomically.
- Atomicity means that either all the updates are committed or none of them are committed, leaving the database in a consistent state.
- Atomic commit is the process of coordinating the decision to commit or abort a distributed transaction among all the participating sites.
- Atomic commit is essential to ensure the ACID properties of distributed transactions, especially the atomicity and durability properties.
- Atomic commit is challenging because of the possibility of site failures, network failures, and communication delays in a distributed system.
- Atomic commit protocols are algorithms that enable the participating sites to reach a consensus on the outcome of a distributed transaction, despite the presence of failures and uncertainties.
- Atomic commit protocols can be classified into two categories: blocking and non-blocking protocols.
- Blocking protocols are protocols that require the participation of all the sites to reach a decision. If some sites fail, the protocol blocks until they recover or are replaced.
- Non-blocking protocols are protocols that can reach a decision without waiting for the failed sites to recover. They use techniques such as timeouts, majority voting, and backup coordinators to cope with failures.
- Examples of blocking protocols are the two-phase commit protocol (2PC) and the three-phase commit protocol (3PC).
- Examples of non-blocking protocols are the Paxos commit protocol, the FLAC protocol, and the Skeen protocol.
- Atomic commit protocols have trade-offs between performance, availability, and fault-tolerance. Blocking protocols are simpler and faster, but less available and fault-tolerant. Non-blocking protocols are more available and fault-tolerant, but more complex and slower.
- Atomic commit protocols are an important component of distributed database systems, as they ensure the consistency and reliability of distributed transactions.



## Unit 5 - Distributed Resource Management

Distributed resource management (DRM) is an evolving discipline that aims to enable distributed enterprise systems to operate effectively in production. DRM involves a set of software, hardware, network tools, procedures and policies for managing the resources of a distributed system, such as computing, storage, communication, and energy. DRM can be applied to various domains, such as cloud computing, grid computing, edge computing, and distributed energy systems.

Some of the main objectives of DRM are:

- To optimize the utilization and performance of the distributed resources.
- To ensure the availability and reliability of the distributed resources.
- To balance the load and demand of the distributed resources.
- To coordinate the operation and interaction of the distributed resources.
- To provide security and privacy for the distributed resources.

Some of the main challenges of DRM are:

- To deal with the heterogeneity and dynamism of the distributed resources.
- To cope with the scalability and complexity of the distributed system.
- To handle the uncertainty and unpredictability of the distributed environment.
- To resolve the conflicts and trade-offs among the distributed resources.
- To adapt to the changing requirements and preferences of the distributed system.

Some of the main components of DRM are:

- Resource discovery: The process of finding and identifying the available and suitable resources in the distributed system.
- Resource scheduling: The process of allocating and assigning the resources to the tasks or applications in the distributed system.
- Resource monitoring: The process of collecting and analyzing the status and performance of the resources in the distributed system.
- Resource control: The process of adjusting and regulating the behavior and operation of the resources in the distributed system.
- Resource coordination: The process of synchronizing and harmonizing the actions and interactions of the resources in the distributed system.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of issues in distributed file systems for the unit 5 of distributed resource management in the subject of distributed system.

### Issues in distributed file systems

A distributed file system (DFS) is a system that allows users to access and manipulate files stored on multiple remote servers as if they were local files. A DFS provides transparency, reliability, scalability, and performance to the users and applications that use it. However, there are also some challenges and issues that need to be addressed in the design and implementation of a DFS. Some of the common issues are:

- **Naming and location:** How to assign unique and meaningful names to the files and directories in a DFS, and how to locate them efficiently in a large and dynamic network of servers. A DFS may use different naming schemes, such as flat, hierarchical, or attribute-based, and different location mechanisms, such as centralized, distributed, or hybrid, to achieve naming and location transparency.
- **Replication and consistency:** How to maintain multiple copies of the same file or directory on different servers for fault tolerance, load balancing, or performance enhancement, and how to ensure that the replicas are consistent with each other and with the original. A DFS may use different replication strategies, such as eager, lazy, or adaptive, and different consistency models, such as strict, causal, or eventual, to achieve replication and consistency transparency.
- **Caching and coherence:** How to store frequently accessed or recently modified files or directories in the local memory or disk of the clients or servers for faster access, and how to ensure that the cached data are coherent with the original data on the servers. A DFS may use different caching policies, such as write-through, write-back, or write-around, and different coherence protocols, such as invalidation, update, or callback, to achieve caching and coherence transparency.
- **Concurrency and locking:** How to allow multiple clients or processes to access and modify the same file or directory concurrently, and how to prevent or resolve conflicts or inconsistencies that may arise from concurrent operations. A DFS may use different concurrency control mechanisms, such as optimistic, pessimistic, or hybrid, and different locking schemes, such as centralized, distributed, or hierarchical, to achieve concurrency and locking transparency.
- **Security and privacy:** How to protect the files and directories in a DFS from unauthorized access, modification, or deletion, and how to preserve the confidentiality, integrity, and availability of the data and the system. A DFS may use different security and privacy techniques, such as encryption, authentication, authorization, or auditing, to achieve security and privacy transparency.

These are some of the main issues that a DFS needs to address in order to provide a reliable, scalable, and efficient service to the users and applications. However, there may be trade-offs and challenges in achieving these goals, and different DFSs may have different design choices and solutions depending on their requirements and assumptions. Therefore, it is important to understand the issues and the solutions of a DFS in order to evaluate its performance and suitability for a given scenario.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the mechanism for building distributed file systems:

### Mechanism for building distributed file systems

- A distributed file system (DFS) is a file system that is distributed on multiple file servers or multiple locations. It allows programs to access or store isolated files as they do with the local ones, allowing programmers to access files from any network or computer.
- A DFS uses different conceptual models of a file. The following are the two basic criteria for file modeling, which include file structure and modifiability:
  - The files can be unstructured or structured based on the applications used in file systems. Unstructured files are byte sequences that can be accessed randomly or sequentially. Structured files are organized into records, fields, or other logical units that can be accessed by name or key.
  - The files can be immutable or mutable based on the operations allowed on them. Immutable files are read-only and cannot be modified after creation. Mutable files can be updated, appended, or deleted by the users or programs.
- A DFS may use one of the following models to service a client’s file request:
  - Remote service model: The client sends the file request to the server, which performs the operation and returns the result. The client does not cache any file data locally. This model is simple and secure, but has high network overhead and latency.
  - Upload/download model: The client downloads the entire file from the server, performs the operation locally, and uploads the modified file back to the server. The client caches the file data locally until the upload is complete. This model reduces network traffic and latency, but has high storage overhead and consistency issues.
  - Demand caching model: The client caches only the portions of the file that are accessed, and fetches them from the server on demand. The client updates the cached data and invalidates or propagates them to the server as needed. This model balances network traffic, latency, storage overhead, and consistency, but requires sophisticated cache management and coherence protocols.
- A DFS may use file replication to improve file availability, reliability, and performance in a distributed systems environment. A replicated file is a file that has multiple copies with each copy located on a separate file server . File replication can be implemented using one of the following techniques:
  - Static replication: The number and location of file replicas are fixed and predetermined by the system administrator. This technique is simple and efficient, but lacks flexibility and adaptability to changing workloads and network conditions.
  - Dynamic replication: The number and location of file replicas are variable and determined by the system dynamically based on the file access patterns, network load, and server availability. This technique is flexible and adaptable, but requires complex and costly replication management and consistency algorithms.
- A DFS may use one of the following consistency models to ensure that the file replicas are coherent and up-to-date:
  - Strict consistency: The file replicas are always identical and reflect the latest update. This model provides the highest level of consistency, but has the highest network and server overhead and the lowest availability and performance.
  - Eventual consistency: The file replicas are allowed to be temporarily inconsistent and converge to the same state eventually. This model provides the lowest level of consistency, but has the lowest network and server overhead and the highest availability and performance.
  - Causal consistency: The file replicas are consistent with respect to the causal order of updates, that is, if update A causally precedes update B, then any replica that reflects B must also reflect A. This model provides a moderate level of consistency, but requires tracking and enforcing the causal dependencies among updates.
  - Session consistency: The file replicas are consistent within a session, that is, a sequence of file operations performed by a single client. This model provides a client-centric level of consistency, but requires maintaining and synchronizing the session state among the servers.
- A DFS may use one of the following update protocols to propagate the file updates among the replicas:
  - Primary-based protocol: One of the file replicas is designated as the primary, which receives and processes all the update requests from the clients. The primary then propagates the updates to the other replicas, which are called secondaries. This protocol ensures consistency and serializability, but introduces a single point of failure and a performance bottleneck.
  - Replicated-write protocol: All the file replicas receive and process the update requests from the clients. The replicas use a consensus algorithm to agree on the order and outcome of



### Design issues in Distributed Shared Memory

Distributed Shared Memory (DSM) is a mechanism that allows multiple processes on different nodes to share a common logical address space and access data transparently. DSM can simplify the programming of distributed systems by hiding the details of inter-process communication. However, DSM also introduces several design issues that affect its performance, scalability, and correctness. Some of the main design issues in DSM are:

- **Granularity**: Granularity refers to the size of the unit of sharing and the unit of coherence in DSM. A smaller granularity (such as a byte or a word) can reduce the amount of false sharing and improve the locality of access, but it can also increase the overhead of coherence maintenance and communication. A larger granularity (such as a page or a segment) can reduce the overhead of coherence and communication, but it can also increase the amount of false sharing and waste bandwidth and memory. Therefore, choosing an appropriate granularity is a trade-off between these factors.

- **Structure**: Structure refers to the organization of the shared data in the logical address space and the mapping of the shared data to the physical memory of the nodes. The structure of DSM can be flat, hierarchical, or object-based. A flat structure treats the shared data as a single linear array and maps it to the nodes using a static or dynamic hashing function. A hierarchical structure divides the shared data into multiple regions and maps each region to a node or a group of nodes. An object-based structure treats the shared data as a collection of objects and maps each object to a node or a group of nodes. The structure of DSM can affect the locality of access, the load balancing, and the fault tolerance of the system.

- **Coherence semantics**: Coherence semantics define the consistency model of DSM, which specifies the order and visibility of the updates to the shared data. Coherence semantics can be strict, relaxed, or weak. A strict coherence semantics (such as sequential consistency) guarantees that all processes see the same order of updates and the same value of the shared data at any time. A relaxed coherence semantics (such as release consistency) allows some reordering and delay of updates, but requires the processes to synchronize explicitly at certain points to ensure consistency. A weak coherence semantics (such as eventual consistency) does not guarantee any order or visibility of updates, but only ensures that the processes will eventually see the same value of the shared data. The coherence semantics of DSM can affect the performance, scalability, and programmability of the system.

- **Coherence protocol**: Coherence protocol defines the mechanism of maintaining the coherence of the shared data among the nodes. Coherence protocol can be centralized, distributed, or hybrid. A centralized coherence protocol relies on a single node or a group of nodes to manage the coherence of the shared data and to serve the requests from other nodes. A distributed coherence protocol distributes the responsibility of coherence management and request servicing among all the nodes. A hybrid coherence protocol combines the features of both centralized and distributed protocols. The coherence protocol of DSM can affect the overhead, scalability, and fault tolerance of the system.

- **Scalability**: Scalability refers to the ability of DSM to handle the increase in the number of nodes, the size of the shared data, and the frequency of access. Scalability can be measured by the throughput, the latency, and the memory consumption of the system. To achieve scalability, DSM needs to address the issues of load balancing, communication overhead, coherence overhead, and memory overhead. Load balancing refers to the distribution of the shared data and the workload among the nodes. Communication overhead refers to the cost of transferring the data and the coherence messages among the nodes. Coherence overhead refers to the cost of maintaining the consistency of the shared data among the nodes. Memory overhead refers to the cost of storing the data and the coherence information in the physical memory of the nodes.

- **Heterogeneity**: Heterogeneity refers to the diversity of the nodes in terms of the hardware, the software, and the network. Heterogeneity can affect the performance, the compatibility, and the portability of DSM. To cope with heterogeneity, DSM needs to address the issues of data representation, data access, and data synchronization. Data representation refers to the format and the layout of the shared data in the memory of the nodes. Data access refers to the mechanism of reading and writing the shared data from and to the memory of the nodes. Data synchronization refers to the mechanism of coordinating the updates to the shared data among the nodes.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on the algorithm for implementation of distributed shared memory for the notes of the Unit 5 - Distributed Resource Management in the subject of DISTRIBUTED SYSTEM.

### Algorithm for Implementation of Distributed Shared Memory

Distributed Shared Memory (DSM) is a technique that allows multiple nodes in a distributed system to access a common virtual address space that is not physically shared. DSM provides a convenient abstraction for parallel and distributed programming, as it hides the details of data distribution and communication from the programmers. However, DSM also introduces challenges such as maintaining consistency, coherence, and fault tolerance of the shared data.

There are different algorithms for implementing DSM, each with its own advantages and disadvantages. Some of the basic algorithms are:

- **Central Server Algorithm**: In this algorithm, a central server maintains all the shared data and services read and write requests from other nodes. The central server can use a page-based or an object-based approach to store and manage the shared data. The advantage of this algorithm is that it is simple and ensures consistency and coherence of the shared data. The disadvantage is that it introduces a single point of failure and a performance bottleneck, as all the requests have to go through the central server.    

- **Migration Algorithm**: In this algorithm, the shared data is initially stored at the central server, but it can migrate to other nodes upon request. When a node requests to read or write a data item, the central server transfers the ownership of that item to the requesting node, and invalidates the copies at other nodes. The requesting node can then access the data item locally, until another node requests it. The advantage of this algorithm is that it reduces the communication overhead and improves the locality of data access. The disadvantage is that it may cause frequent data migration and invalidation, which can increase the latency and network traffic.    

- **Replication Algorithm**: In this algorithm, the shared data is replicated at multiple nodes, and each node can access its local copy. The central server maintains a directory of the locations and states of the data items, and updates it whenever a node requests to read or write a data item. The central server also ensures the consistency and coherence of the data items by using a protocol such as invalidation or update. The advantage of this algorithm is that it allows concurrent and fast access to the shared data. The disadvantage is that it requires more storage space and synchronization overhead, as the data items have to be replicated and updated at multiple nodes.    

- **Distributed Algorithm**: In this algorithm, there is no central server, and the shared data is distributed among the nodes. Each node maintains a portion of the shared data and a directory of the locations and states of the other data items. The nodes communicate with each other directly to service read and write requests, and to ensure the consistency and coherence of the data items. The advantage of this algorithm is that it eliminates the single point of failure and the performance bottleneck of the central server. The disadvantage is that it increases the complexity and the communication overhead, as the nodes have to coordinate and exchange messages with each other.    

The choice of the algorithm for implementing DSM depends on various factors, such as the size and topology of the distributed system, the access pattern and granularity of the shared data, the consistency and coherence requirements, and the trade-off between performance and complexity.    

I hope this information is helpful for your study. If you have any questions or feedback, please let me know.😊



## Unit 6 - Failure Recovery in Distributed Systems

- Failure recovery is the process of restoring a distributed system to a consistent and correct state after a failure occurs.
- Failures can be classified into three types: crash failures, omission failures, and arbitrary failures.
- Crash failures occur when a process stops executing and does not resume. Omission failures occur when a process fails to send or receive a message. Arbitrary failures occur when a process behaves in an unpredictable or malicious way.
- Failure recovery techniques can be divided into two categories: backward recovery and forward recovery.
- Backward recovery involves undoing the effects of a failure and restoring the system to a previous consistent state. This can be done using checkpoints, logging, or rollback-recovery protocols.
- Forward recovery involves correcting the effects of a failure and continuing the execution from the current state. This can be done using redundancy, replication, or fault-tolerance protocols.
- Checkpoints are snapshots of the system state that are periodically saved on stable storage. They can be used to restart the system from a consistent state after a failure.
- Logging is the technique of recording the events or actions that occur in the system on stable storage. They can be used to replay or undo the events or actions after a failure.
- Rollback-recovery protocols are algorithms that coordinate the processes to roll back to a consistent state after a failure. They can be based on message logging, checkpointing, or both.
- Redundancy is the technique of having multiple copies or versions of the same data or service. They can be used to mask or tolerate failures by switching to an alternative copy or version.
- Replication is the technique of maintaining multiple copies of the same data or service on different processes or nodes. They can be used to improve availability, reliability, and performance of the system.
- Fault-tolerance protocols are algorithms that ensure the system can continue to function correctly despite the presence of failures. They can be based on consensus, voting, or quorum.



### Concepts in Backward and Forward Recovery

- Backward recovery and forward recovery are two techniques for restoring the system to a consistent state after a failure in a distributed system.
- Backward recovery involves rolling back the system to a previous error-free state by using checkpoints and logs. Forward recovery involves correcting the errors and continuing the execution from the current state.
- The main difference between backward and forward recovery is that backward recovery discards the work done after the error, while forward recovery preserves the work done before and after the error.
- Backward recovery is more general and independent of the nature of faults, but it may incur more overhead and latency. Forward recovery is more efficient and responsive, but it requires accurate assessment and removal of errors.
- Some examples of backward recovery protocols are checkpointing, logging, and message logging. Some examples of forward recovery protocols are redundancy, replication, and voting.



### Recovery in Concurrent Systems

- Recovery in concurrent systems is the process of restoring the system to a consistent state after a failure or an error.
- Recovery is essential to ensure the correctness and reliability of the system, especially in distributed systems where multiple nodes may be involved in a transaction or a computation.
- Recovery in concurrent systems can be classified into two types: backward recovery and forward recovery.

#### Backward Recovery

- Backward recovery is the technique of undoing the effects of the erroneous or failed operations and restoring the system to a previous consistent state.
- Backward recovery requires the system to maintain some form of history or log of the operations performed by the concurrent transactions or processes.
- Backward recovery can be further divided into two methods: transaction rollback and checkpointing.

##### Transaction Rollback

- Transaction rollback is the method of undoing the updates performed by a failed or aborted transaction and restoring the data to its original state before the transaction started.
- Transaction rollback requires the system to use a concurrency control scheme, such as locking or timestamping, to ensure the serializability and isolation of the transactions.
- Transaction rollback can be implemented using undo logging or redo logging.

###### Undo Logging

- Undo logging is the technique of recording the old values of the data items before they are updated by a transaction in a log file.
- Undo logging allows the system to undo the updates of a failed transaction by applying the inverse operations using the old values from the log file.
- Undo logging requires the system to follow the write-ahead logging (WAL) protocol, which ensures that the log records are written to the stable storage before the data items are updated in the main memory or the disk.

###### Redo Logging

- Redo logging is the technique of recording the new values of the data items after they are updated by a transaction in a log file.
- Redo logging allows the system to redo the updates of a committed transaction by applying the same operations using the new values from the log file in case of a system crash or a disk failure.
- Redo logging requires the system to follow the force and no-steal policies, which ensure that the updated data items are written to the disk before the transaction commits and that the uncommitted data items are not evicted from the main memory.

##### Checkpointing

- Checkpointing is the method of periodically saving the state of the system to a stable storage, such as a disk or a tape, to reduce the amount of work required for recovery.
- Checkpointing allows the system to restart the recovery from the most recent checkpoint instead of the beginning of the execution, thus avoiding the need to undo or redo the operations that occurred before the checkpoint.
- Checkpointing can be implemented using fuzzy checkpointing or shadow paging.

###### Fuzzy Checkpointing

- Fuzzy checkpointing is the technique of taking a checkpoint without blocking the execution of the transactions or processes.
- Fuzzy checkpointing allows the system to continue the normal operation while the checkpoint is being written to the disk, thus reducing the performance overhead.
- Fuzzy checkpointing requires the system to ensure the consistency of the checkpoint by using a checkpoint record, which indicates the start and the end of the checkpoint, and a dirty page table, which records the pages that are modified during the checkpoint.

###### Shadow Paging

- Shadow paging is the technique of taking a checkpoint by creating a copy of the data pages on the disk and updating the copy instead of the original pages.
- Shadow paging allows the system to avoid the logging overhead and the need to undo or redo the operations, as the original pages are preserved until the checkpoint is completed.
- Shadow paging requires the system to maintain a page table, which maps the logical addresses of the pages to their physical locations on the disk, and a shadow page table, which is a copy of the page table at the time of the checkpoint.

#### Forward Recovery

- Forward recovery is the technique of correcting the errors or failures without undoing the effects of the operations and continuing the execution from the current state.
- Forward recovery requires the system to detect the errors or failures and apply some form of error correction or fault tolerance mechanisms to resolve them.
- Forward recovery can be further divided into two methods: error masking and error compensation.

##### Error Masking

- Error masking is the method of hiding the errors or failures from the system or the user by using some form of redundancy or replication.
- Error masking allows the system to continue the normal operation without any interruption or degradation of the service quality.
- Error masking can be implemented using techniques such as majority voting, error-correcting codes, or replication.

###### Majority Voting

- Majority voting is the technique of using multiple



### Obtaining consistent Checkpoints

- Checkpoints are snapshots of the state of a process or a system at a given point in time.
- Checkpoints are useful for failure recovery in distributed systems, as they allow processes to roll back to a previous consistent state and resume execution.
- A consistent checkpoint is one that preserves the causal order of events in the system, i.e., if a process P sends a message m to another process Q, then P's checkpoint must be taken before Q's checkpoint.
- There are two main approaches for obtaining consistent checkpoints in distributed systems: coordinated checkpointing and communication-induced checkpointing.

#### Coordinated checkpointing

- In coordinated checkpointing, all processes in the system agree on when to take a checkpoint, either by using a central coordinator or by exchanging messages among themselves.
- Coordinated checkpointing ensures that no process takes a checkpoint while it has a message in transit, thus avoiding the creation of orphan messages (messages that are received after the checkpoint but were sent before the checkpoint).
- Coordinated checkpointing has the advantages of simplicity, low overhead, and minimal storage requirements, as each process only needs to keep one checkpoint at a time.
- Coordinated checkpointing has the disadvantages of blocking the normal execution of the system during the checkpointing process, and requiring global synchronization among all processes.

#### Communication-induced checkpointing

- In communication-induced checkpointing, processes take checkpoints based on the messages they send and receive, without any global coordination.
- Communication-induced checkpointing ensures that the checkpoints form a consistent global state by using a protocol that enforces some rules on when and how to take checkpoints.
- Communication-induced checkpointing has the advantages of avoiding blocking and synchronization, and allowing more flexibility and concurrency in the system.
- Communication-induced checkpointing has the disadvantages of complexity, high overhead, and large storage requirements, as each process may need to keep multiple checkpoints and dependencies among them.



### Recovery in Distributed Database Systems

- Recovery in distributed database systems is the process of restoring the database to a consistent and correct state after a failure .
- Failure in distributed database systems can be classified into two types: soft failures and hard failures.
  - Soft failures are temporary and do not cause physical damage to the database, such as network failures, transaction aborts, or deadlocks.
  - Hard failures are permanent and cause physical damage to the database, such as disk crashes, power outages, or site failures.
- Recovery in distributed database systems aims to maintain the atomicity and durability of distributed transactions, which means that either all or none of the subtransactions at different sites are committed, and the committed changes are permanent .
- Recovery in distributed database systems is more complicated than in centralized database systems because failures can occur at the communication links or a remote site, and the system may not have a global view of the transaction status.
- Recovery in distributed database systems can be divided into two phases: local recovery and global recovery.
  - Local recovery is the process of restoring a site to a consistent state after a failure, using techniques such as undo, redo, or compensation.
  - Global recovery is the process of coordinating the commit or abort of distributed transactions across multiple sites, using protocols such as two-phase commit, three-phase commit, or majority consensus.
- Recovery in distributed database systems faces several challenges, such as concurrency control, partial operability, network partitioning, and global rollback.
  - Concurrency control is the mechanism to ensure serializability and isolation of distributed transactions, which may conflict with the recovery protocols.
  - Partial operability is the ability of the system to continue processing transactions at some sites even if other sites are down, which may lead to inconsistency or deadlock.
  - Network partitioning is the situation where the system is divided into two or more disjoint subsets of sites that cannot communicate with each other, which may cause ambiguity or deadlock in the commit or abort decision.
  - Global rollback is the situation where the system has to undo all the committed subtransactions of a distributed transaction, which may be costly or impossible.



## Unit 7 - Fault Tolerance

- Fault tolerance is the ability of a system to continue functioning correctly in the presence of failures.
- Fault tolerance can be achieved by using techniques such as redundancy, replication, recovery, reconfiguration, and masking.
- Fault tolerance can be classified into two types: hardware fault tolerance and software fault tolerance.
- Hardware fault tolerance is the ability of a system to tolerate failures of physical components, such as processors, memory, disks, or network devices.
- Hardware fault tolerance can be achieved by using techniques such as RAID, mirroring, hot swapping, checkpointing, and voting.
- Software fault tolerance is the ability of a system to tolerate failures of software components, such as operating systems, applications, or protocols.
- Software fault tolerance can be achieved by using techniques such as exception handling, transactions, rollback, retry, and consensus.
- Fault tolerance can be measured by metrics such as reliability, availability, and maintainability.
- Reliability is the probability that a system will perform its intended function without failure for a given period of time.
- Availability is the fraction of time that a system is operational and ready to provide service.
- Maintainability is the ease with which a system can be repaired or restored after a failure.



### Issues in Fault Tolerance for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Fault tolerance is the ability of a system to continue functioning correctly in the presence of failures.
- Fault tolerance is important for distributed systems because they consist of multiple components that may be subject to different types of failures, such as hardware failures, software failures, network failures, malicious attacks, etc .
- Fault tolerance can be achieved by using various techniques, such as redundancy, replication, checkpointing, recovery, consensus, etc .
- Fault tolerance can be classified into different levels, such as detection, diagnosis, containment, masking, compensation, and recovery.
- Fault tolerance can also be categorized into different models, such as fail-stop, fail-silent, fail-safe, fail-recover, and Byzantine.
- Fault tolerance can be evaluated by using different metrics, such as reliability, availability, dependability, and resilience .
- Fault tolerance can be improved by using different strategies, such as fault prevention, fault removal, fault forecasting, and fault tolerance.
- Fault tolerance can be implemented by using different architectures, such as centralized, decentralized, hierarchical, or hybrid .
- Fault tolerance can be influenced by different factors, such as system size, complexity, heterogeneity, dynamism, scalability, etc .
- Fault tolerance can be challenged by different issues, such as consistency, concurrency, communication, coordination, security, etc .

: Fault Tolerance in Distributed Systems: A Survey - IEEE Xplore
: What is fault tolerance in distributed system - IT Release
: Fault Tolerance Mechanisms in Distributed Systems
: 13 - Fault Tolerance in Distributed Systems - Cambridge Core



### Commit Protocols

- Commit protocols are algorithms that ensure the atomicity of distributed transactions, i.e., all the sites involved in a transaction either commit or abort it unanimously, even in the presence of failures  .
- Commit protocols are initiated by a coordinator site, which communicates with the participating sites and directs them to execute, commit or abort the transaction .
- There are different types of commit protocols, such as one-phase commit, two-phase commit and three-phase commit, which differ in the number of phases and messages exchanged between the coordinator and the participants   .

#### One-Phase Commit Protocol

- A one-phase commit protocol involves a single phase, in which the coordinator sends a commit request to all the participants and waits for their replies.
- The participants execute the transaction and send back an acknowledgement to the coordinator, indicating whether they are ready to commit or not.
- The coordinator then decides to commit or abort the transaction based on the replies from the participants, and sends the final decision to all of them.
- The advantages of this protocol are simplicity and low message overhead, but the disadvantages are lack of fault tolerance and concurrency control.
- If the coordinator or any participant fails, the transaction may be left in an inconsistent state, as there is no way to recover or rollback the changes.
- If multiple transactions access the same data items, there may be conflicts or deadlocks, as there is no locking or synchronization mechanism.

#### Two-Phase Commit Protocol

- A two-phase commit protocol involves two phases, namely the voting phase and the commit phase  .
- In the voting phase, the coordinator sends a prepare request to all the participants, asking them to vote on whether they are ready to commit or not  .
- The participants execute the transaction and send back their votes to the coordinator, along with a promise to wait for the final decision  .
- The coordinator then collects all the votes and decides to commit or abort the transaction based on the majority rule, i.e., if all the votes are yes, then commit, otherwise abort  .
- In the commit phase, the coordinator sends the final decision to all the participants, and they either commit or abort the transaction accordingly  .
- The advantages of this protocol are fault tolerance and concurrency control, but the disadvantages are high message overhead and blocking problem  .
- If the coordinator or any participant fails, the transaction can be recovered or rolled back using the log records and the votes  .
- If multiple transactions access the same data items, there is a locking mechanism that prevents conflicts or deadlocks  .
- However, if the coordinator fails after sending the prepare request, the participants may be blocked indefinitely, as they do not know the final decision and cannot proceed with other transactions  .

#### Three-Phase Commit Protocol

- A three-phase commit protocol involves three phases, namely the prepare phase, the pre-commit phase and the commit phase .
- In the prepare phase, the steps are the same as in the two-phase commit protocol, i.e., the coordinator sends a prepare request to all the participants, and they send back their votes and wait for the final decision .
- In the pre-commit phase, the coordinator sends a pre-commit message to all the participants, indicating that it has decided to commit the transaction, and waits for their acknowledgements .
- The participants acknowledge the pre-commit message and enter a ready state, where they are prepared to commit the transaction, but have not done so yet .
- In the commit phase, the coordinator sends a commit message to all the participants, and they commit the transaction and send back their acknowledgements .
- The coordinator then collects all the acknowledgements and completes the transaction .
-



### Voting protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Voting protocols are a class of consensus algorithms that are used to achieve agreement among a set of distributed nodes on some value or decision.
- Voting protocols are useful for fault-tolerant systems, where some nodes may fail or behave maliciously, and the system needs to maintain consistency and availability.
- Voting protocols can be classified into two types: exact voting and inexact voting.
  - Exact voting requires that all nodes agree on the same value or decision, and that the value or decision is correct according to some predefined criterion. Examples of exact voting are two-phase commit, three-phase commit, and Paxos.
  - Inexact voting allows for some degree of disagreement or error among the nodes, as long as the value or decision is acceptable according to some predefined criterion. Examples of inexact voting are majority voting, weighted voting, and probabilistic voting.
- Voting protocols can also be classified based on the security and fairness properties they provide. Security means that the voting protocol is resilient to attacks from malicious nodes or external adversaries. Fairness means that the voting protocol does not favor or discriminate any node or group of nodes based on their reputation or weight.
  - Secure voting protocols ensure that the value or decision agreed upon by the nodes is correct and consistent, even in the presence of malicious nodes or external adversaries. Secure voting protocols typically use cryptographic techniques, such as digital signatures, encryption, or zero-knowledge proofs, to prevent or detect attacks. Examples of secure voting protocols are Byzantine fault-tolerant protocols, such as PBFT, Zyzzyva, and HoneyBadgerBFT.
  - Fair voting protocols ensure that the value or decision agreed upon by the nodes is representative and balanced, even in the presence of nodes with different reputation or weight. Fair voting protocols typically use mathematical techniques, such as game theory, social choice theory, or mechanism design, to incentivize or enforce fairness. Examples of fair voting protocols are proportional voting, liquid democracy, and quadratic voting.



### Dynamic voting protocols

- Dynamic voting protocols are techniques for maintaining consistency and availability of replicated data in distributed systems.
- The basic idea is to assign weights or votes to each replica of a data item, and to require a majority of votes to access or update the data item.
- Dynamic voting protocols can adapt to changes in the system state, such as site failures, network partitions, or load balancing, by reassigning votes to different replicas.
- Dynamic voting protocols can be classified into two categories: quorum-based and topology-based.
- Quorum-based protocols use a fixed or variable quorum size to determine the majority of votes. A quorum is a subset of replicas that satisfies some condition, such as having a minimum number of votes or being connected by a spanning tree.
- Topology-based protocols use the network topology to determine the majority of votes. A topology is a graph that represents the connectivity and reachability of the sites in the system. A topology can be static or dynamic, depending on whether it changes with the system state or not.
- Some examples of dynamic voting protocols are:

  - The dynamic weighted voting scheme  , which assigns weights to replicas based on their availability and reliability, and adjusts the quorum size according to the system state.
  - The protocols for dynamic vote reassignment, which reassign votes to different replicas upon node or link failures, to maintain a majority of votes in each partition of the system.
  - The efficient dynamic voting algorithms, which use a dynamic topology to determine the majority of votes, and perform better than other voting algorithms when two or more replicas reside in the same non-partitionable group.



## Unit 8 - Transactions and Concurrency Control

A transaction is a logical unit of work that consists of a sequence of database operations, such as queries, updates, inserts, or deletes. A transaction has the following properties:

- Atomicity: A transaction is either executed in its entirety or not at all. If a transaction fails, the database is restored to its state before the transaction started.
- Consistency: A transaction preserves the consistency of the database, meaning that it does not violate any integrity constraints or business rules.
- Isolation: A transaction is executed as if it were the only one running on the database, meaning that it does not interfere with or see the effects of other concurrent transactions.
- Durability: The effects of a transaction are permanent, meaning that they persist even if the system crashes or power fails.

Concurrency control is the process of managing the simultaneous execution of transactions on a shared database, such that the transactions do not conflict with each other and the database remains consistent. Concurrency control techniques can be classified into two categories:

- Locking-based: A locking-based technique uses locks to prevent transactions from accessing or modifying data that is being used by another transaction. A lock is a mechanism that grants exclusive or shared access to a data item or a set of data items. There are different types of locks, such as binary locks, shared/exclusive locks, or multiple granularity locks. Locking-based techniques can also use timestamps or validation rules to avoid deadlock or starvation situations.
- Non-locking-based: A non-locking-based technique does not use locks, but instead relies on other mechanisms, such as timestamps, version numbers, or optimistic validation, to ensure serializability of transactions. Serializability is the property that the concurrent execution of transactions is equivalent to some serial execution of the same transactions. Non-locking-based techniques can also use multiversion concurrency control or snapshot isolation to allow more concurrency and reduce conflicts.



### Transactions

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the operations in a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction does not interfere with other concurrent transactions.
- Durability means that the effects of a transaction are permanent even in the presence of failures.

### Concurrency Control

- Concurrency control is the process of managing simultaneous access to shared data in a database by multiple transactions.
- Concurrency control ensures that the transactions are executed in a correct and consistent manner, without violating the ACID properties.
- Concurrency control can be implemented using various techniques, such as locking, timestamping, validation, and multiversioning.
- Locking is a technique that grants exclusive access to a data item to one transaction at a time, preventing other transactions from reading or writing it.
- Timestamping is a technique that assigns a unique identifier to each transaction based on the time of its arrival, and uses it to order the transactions and resolve conflicts.
- Validation is a technique that checks the consistency of a transaction before committing it, and aborts it if it violates any integrity constraint or concurrency rule.
- Multiversioning is a technique that maintains multiple versions of a data item, and allows transactions to access the version that is appropriate for their timestamp.

### Distributed Systems

- A distributed system is a system that consists of multiple independent nodes that communicate and coordinate with each other over a network.
- A distributed system can provide advantages such as scalability, availability, fault-tolerance, and performance.
- A distributed system can also pose challenges such as heterogeneity, concurrency, transparency, security, and consistency.
- A distributed database system is a type of distributed system that stores and manages data across multiple nodes, and provides a unified view of the data to the users and applications.
- A distributed transaction is a transaction that spans multiple nodes in a distributed database system, and accesses or modifies data stored in different nodes.
- A distributed transaction requires a distributed concurrency control mechanism to ensure that the ACID properties are not violated by the interleaved execution of multiple distributed transactions.



### Nested transactions

- A nested transaction is a transaction that is composed of subtransactions, each of which may be committed or aborted independently.
- A nested transaction can be used to implement partial rollback, modular programming, and concurrency control in distributed systems.
- A nested transaction has a tree structure, where the root is the top-level transaction and the leaves are the subtransactions.
- A nested transaction is atomic, meaning that either all of its subtransactions commit or none of them do.
- A nested transaction is consistent, meaning that it preserves the integrity constraints of the data.
- A nested transaction is isolated, meaning that it does not interfere with other concurrent transactions.
- A nested transaction is durable, meaning that its effects are permanent once it commits.

#### Advantages of nested transactions

- Nested transactions allow for more concurrency and fault tolerance in distributed systems, as subtransactions can execute in parallel and recover from failures independently.
- Nested transactions enable modular programming, as subtransactions can encapsulate different operations or functions that can be reused and composed.
- Nested transactions support partial rollback, as subtransactions can be aborted without affecting the rest of the transaction.

#### Challenges of nested transactions

- Nested transactions require more complex protocols and algorithms to ensure serializability, consistency, and atomicity across multiple servers and levels of transactions.
- Nested transactions may incur more overhead and communication costs, as subtransactions need to coordinate with their parent and sibling transactions and exchange messages and locks.
- Nested transactions may introduce more conflicts and deadlocks, as subtransactions may access or modify the same data or resources as other transactions.



### Locks for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A lock is a mechanism that allows only one of the innumerable nodes (or processes) to access and modify a resource or data that is being shared commonly to prevent execution of same task twice and also maintain data integrity.
- Locks are designed to enforce a mutual exclusion concurrency control policy, which means that only one node can hold a lock on a resource at a time, and no other node can access or modify that resource until the lock is released.
- Locks can be classified into different types based on the following criteria  :
  - The granularity of the resource: locks can be applied to a whole database, a table, a page, a record, or a field.
  - The mode of the lock: locks can be either shared or exclusive. A shared lock allows multiple nodes to read the same resource, but not to modify it. An exclusive lock allows only one node to read and modify the resource, and blocks all other nodes from accessing it.
  - The duration of the lock: locks can be either long-lived or short-lived. A long-lived lock is held for the entire duration of a transaction, and is released only when the transaction commits or aborts. A short-lived lock is held only for the time needed to access or modify the resource, and is released as soon as possible.
  - The implementation of the lock: locks can be either centralized or distributed. A centralized lock is managed by a single node or a lock server, which maintains a global lock table and grants or denies lock requests from other nodes. A distributed lock is managed by multiple nodes or a consensus protocol, which coordinate with each other to agree on the lock state and handle lock conflicts.
- Locks can be used to ensure the ACID properties of transactions in a distributed system, where ACID stands for Atomicity, Consistency, Isolation, and Durability :
  - Atomicity means that a transaction is either executed completely or not at all, and no partial effects are visible to other transactions.
  - Consistency means that a transaction preserves the integrity constraints of the database, and does not leave it in an inconsistent state.
  - Isolation means that a transaction is executed as if it were the only one running in the system, and does not interfere with other concurrent transactions.
  - Durability means that the effects of a committed transaction are permanent and survive any system failures.
- Locks can also introduce some challenges and trade-offs in a distributed system, such as  :
  - Deadlocks: a deadlock occurs when two or more nodes are waiting for each other to release locks on resources that they need to complete their transactions. A deadlock can prevent any of the nodes from making progress, and can only be resolved by aborting one or more transactions and releasing their locks.
  - Livelocks: a livelock occurs when two or more nodes are repeatedly trying to acquire locks on resources that are held by other nodes, and keep changing their lock requests in response to each other. A livelock can also prevent any of the nodes from making progress, and can only be resolved by introducing some randomness or delay in the lock requests.
  - Starvation: starvation occurs when a node is repeatedly denied a lock on a resource that it needs to complete its transaction, because other nodes have higher priority or are faster in acquiring the lock. Starvation can cause a node to wait indefinitely, and can only be resolved by implementing some fairness or queueing mechanism in the lock manager.
  - Performance: locks can affect the performance of a distributed system in terms of throughput, latency, and scalability. Locks can reduce the throughput by limiting the concurrency and parallelism of transactions. Locks can increase the latency by introducing waiting and communication overheads. Locks can hinder the scalability by creating bottlenecks and hotspots in the lock manager or the lock table.
- Locks are not the only way to achieve transactions and concurrency control in a distributed system. There are other alternatives, such as optimistic concurrency control, timestamp ordering, snapshot isolation, multiversion concurrency control, and conflict-free replicated data types . Each of these alternatives has its own advantages and disadvantages, and the choice depends on the requirements and characteristics of the system.



### Optimistic Concurrency Control

- Optimistic concurrency control (OCC) is a concurrency control method applied to transactional systems such as relational database management systems and software transactional memory.
- OCC assumes that multiple transactions can frequently complete without interfering with each other, and avoids locking of data items that can reduce the performance of the system.
- OCC consists of three phases: read, validation and write.
  - In the read phase, the transaction reads the data items from the database and performs the necessary computations, but does not update the database.
  - In the validation phase, the transaction checks if any of the data items it has read have been modified by other transactions that committed after it started. If so, the transaction is aborted and restarted, otherwise it proceeds to the write phase.
  - In the write phase, the transaction updates the database with the new values of the data items it has modified.
- OCC has several advantages over locking-based concurrency control techniques, such as:
  - It allows more concurrency, as transactions do not block each other by holding locks.
  - It avoids deadlock, as transactions do not wait for locks to be released.
  - It reduces the overhead of lock management, as transactions do not need to acquire and release locks.
- OCC also has some disadvantages, such as:
  - It may cause more aborts and restarts, as transactions may conflict with each other at the validation phase.
  - It may increase the response time, as transactions have to perform the validation phase before committing.
  - It may not be suitable for applications that have high contention, as transactions are more likely to fail the validation phase.
- OCC can be implemented in distributed systems, where transactions may access data items stored in different nodes of the network.
  - One approach is to use a centralized validator, which collects the read and write sets of all transactions and performs the validation phase for them.
  - Another approach is to use a distributed validator, which partitions the data items among the nodes and performs the validation phase locally for each partition.
  - Both approaches have their trade-offs in terms of communication cost, scalability and fault tolerance.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on timestamp ordering for transactions and concurrency control in distributed systems.

### Timestamp ordering

- Timestamp ordering is a technique to ensure serializability of transactions in a distributed system, where different nodes or processes may have different physical clocks and communication delays.
- Timestamp ordering assigns a unique logical timestamp to each transaction, based on a logical clock function that takes into account the causal dependencies among transactions.
- A logical clock function is a function that maps each event in the system to a positive integer, such that if event A causally precedes event B, then the logical clock of A is less than the logical clock of B.
- One example of a logical clock function is the Lamport timestamp algorithm, which assigns a timestamp to each event as follows :
  - Each node maintains a local counter, initialized to zero.
  - Whenever a node executes an event, it increments its counter by one and assigns it as the timestamp of the event.
  - Whenever a node sends a message, it includes its current counter value in the message.
  - Whenever a node receives a message, it updates its counter to the maximum of its own counter and the counter value in the message, and then increments it by one.
- Timestamp ordering uses the logical timestamps to order the transactions and enforce serializability. There are two main approaches to timestamp ordering:
  - Basic timestamp ordering: Each transaction is assigned a timestamp when it starts, and the timestamp is used to order the conflicting operations of different transactions. If a transaction tries to execute an operation that violates the timestamp order, it is aborted and restarted with a new timestamp.
  - Conservative timestamp ordering: Each transaction is assigned a timestamp when it is submitted, and the timestamp is used to order the transactions. A transaction is allowed to start only if it has the smallest timestamp among all the transactions in the system, and it holds all the locks it needs to execute. If a transaction cannot start or acquire a lock, it is delayed until it can.
- Timestamp ordering has some advantages and disadvantages over other concurrency control techniques, such as locking or optimistic concurrency control:
  - Advantages:
    - Timestamp ordering avoids deadlock, since transactions do not wait for locks held by other transactions.
    - Timestamp ordering preserves the temporal order of transactions, which may be desirable for some applications.
    - Timestamp ordering can be implemented in a decentralized manner, without a central coordinator or a global clock.
  - Disadvantages:
    - Timestamp ordering may cause unnecessary aborts or delays, since transactions may conflict with other transactions that have not yet committed or started.
    - Timestamp ordering may not guarantee recoverability or cascadelessness, since transactions may read uncommitted or aborted data from other transactions.
    - Timestamp ordering may not be compatible with some isolation levels, such as snapshot isolation or repeatable read, since transactions may see inconsistent snapshots of the database.



### Comparison of methods for concurrency control

Concurrency control is the process of managing the concurrent access and modification of shared data in a distributed system, such that the ACID properties of transactions are preserved. Concurrency control methods can be classified into two main categories: pessimistic and optimistic.

- Pessimistic methods prevent conflicts from occurring by acquiring locks on data items before accessing them. Transactions that request locks on data items that are already locked by other transactions have to wait until the locks are released. This ensures serializability, but may cause deadlock, blocking, and reduced concurrency. Examples of pessimistic methods are two-phase locking (2PL), timestamp ordering (TO), and distributed locking (DL).

- Optimistic methods allow conflicts to occur, but detect and resolve them before committing transactions. Transactions do not acquire locks on data items, but instead keep track of their read and write sets. Before committing, transactions validate their read and write sets against other concurrent transactions, and abort and restart if any conflict is detected. This avoids deadlock, blocking, and increases concurrency, but may cause more aborts and restarts. Examples of optimistic methods are validation (or certification), multiversion concurrency control (MVCC), and snapshot isolation (SI).

The following table summarizes some of the advantages and disadvantages of the different concurrency control methods:

| Method | Advantages | Disadvantages |
|--------|------------|---------------|
| 2PL | Simple, ensures serializability and strictness | May cause deadlock, blocking, reduced concurrency, and high locking overhead |
| TO | Avoids deadlock, ensures serializability and strictness | May cause blocking, reduced concurrency, and high timestamp management overhead |
| DL | Allows distributed transactions to acquire locks on multiple data servers | May cause deadlock, blocking, reduced concurrency, and high communication overhead |
| Validation | Avoids deadlock, blocking, and increases concurrency | May cause more aborts and restarts, and high validation overhead |
| MVCC | Avoids deadlock, blocking, and increases concurrency | May cause more storage and garbage collection overhead, and non-serializable anomalies |
| SI | Avoids deadlock, blocking, and increases concurrency | May cause non-serializable anomalies, such as write skew and read skew |



## Unit 9 - Distributed Transactions

- A distributed transaction is a type of transaction that involves two or more network hosts, usually providing transactional resources, such as databases, message queues, file systems, etc.   
- A distributed transaction is coordinated by a transaction manager, which is responsible for creating and managing a global transaction that encompasses all the operations against the transactional resources.  
- A distributed transaction has the same ACID properties as a local transaction, which are atomicity, consistency, isolation, and durability. However, achieving these properties in a distributed environment is more challenging and requires additional protocols and mechanisms. 
- Some of the challenges and issues in distributed transactions are:
  - Network failures and partitions, which may cause communication problems between the transaction manager and the transactional resources, or among the transactional resources themselves. 
  - Concurrency and locking, which may cause deadlocks or conflicts when multiple transactions access the same data across different hosts. 
  - Data replication and consistency, which may cause data inconsistency or divergence when multiple copies of the same data are stored on different hosts and updated by different transactions. 
  - Performance and scalability, which may degrade as the number of hosts and transactions increases, due to the overhead of coordination and communication. 
- Some of the common protocols and mechanisms for distributed transactions are:
  - Two-phase commit (2PC), which is a protocol that ensures atomicity and durability of a distributed transaction by using a coordinator (usually the transaction manager) and a set of participants (usually the transactional resources) to vote and commit on the outcome of the transaction.  
  - Three-phase commit (3PC), which is a protocol that improves the availability and fault-tolerance of 2PC by introducing a third phase of pre-commit, which allows the participants to recover from network failures or partitions without blocking or aborting the transaction.  
  - Saga, which is a mechanism that relaxes the atomicity and isolation of a distributed transaction by allowing partial commits and compensating actions, which are used to undo the effects of a failed or aborted transaction. 
  - Eventual consistency, which is a mechanism that relaxes the consistency and isolation of a distributed transaction by allowing temporary data inconsistency or divergence, which is resolved over time by applying updates or reconciling conflicts.



### Flat and nested distributed transactions

- A **distributed transaction** is a transaction that accesses objects managed by multiple servers .
- A distributed transaction must maintain the **ACID** properties of atomicity, consistency, isolation, and durability across all the servers involved .
- A distributed transaction can be structured in two different ways: **flat** or **nested** .

#### Flat transactions

- A **flat transaction** has a single initiating point (Begin) and a single end point (Commit or Abort) .
- A flat transaction is usually simple and short-lived, and does not allow subtransactions .
- A flat transaction uses a **two-phase commit protocol** (2PC) to coordinate the commit or abort decision among all the servers .
- A flat transaction has the following phases :
  - **Voting phase**: The coordinator asks each server to vote on whether to commit or abort the transaction. Each server replies with a Yes or No vote.
  - **Decision phase**: The coordinator decides to commit the transaction if all the servers voted Yes, or to abort the transaction if any server voted No. The coordinator informs all the servers of the final decision.

#### Nested transactions

- A **nested transaction** is a transaction that can be decomposed into subtransactions, each with its own Begin and End points .
- A nested transaction is usually complex and long-lived, and allows subtransactions to be executed in parallel or sequentially .
- A nested transaction uses a **sagacommunication protocol** (SCP) to coordinate the commit or abort decision among all the servers .
- A nested transaction has the following phases :
  - **Execution phase**: The coordinator executes each subtransaction and collects the results. Each subtransaction can be committed or aborted independently, but the coordinator keeps track of the dependencies among them.
  - **Completion phase**: The coordinator decides to commit the transaction if all the subtransactions committed, or to abort the transaction if any subtransaction aborted. The coordinator informs all the servers of the final decision. If the transaction is aborted, the coordinator invokes the **compensation actions** of the committed subtransactions to undo their effects.



### Atomic Commit Protocols for Distributed Transactions

- A distributed transaction is a transaction that involves multiple servers or nodes in a distributed system. A distributed transaction may span across different databases, applications, or networks.
- An atomic commit protocol is a protocol that ensures that a distributed transaction is either committed or aborted in its entirety, even if some of the nodes fail or crash. This is important for maintaining the consistency and integrity of the data in the system.
- There are different types of atomic commit protocols, such as two-phase commit (2PC), three-phase commit (3PC), parallel commit, and failure-aware commit. Each protocol has its own advantages and disadvantages in terms of performance, availability, and fault tolerance.
- Two-phase commit (2PC) is the most widely used atomic commit protocol. It consists of two phases: a prepare phase and a commit phase. In the prepare phase, the coordinator node asks all the participant nodes to vote on whether they are ready to commit or abort the transaction. In the commit phase, the coordinator node decides on the final outcome of the transaction based on the votes and informs all the participant nodes to either commit or abort accordingly. 2PC ensures atomicity and consistency, but it has some drawbacks, such as blocking, high latency, and vulnerability to coordinator failures .
- Three-phase commit (3PC) is an extension of 2PC that adds a pre-commit phase between the prepare and commit phases. In the pre-commit phase, the coordinator node informs all the participant nodes that they have agreed to commit the transaction and asks them to acknowledge. In the commit phase, the coordinator node instructs all the participant nodes to commit the transaction. 3PC avoids blocking and reduces the vulnerability to coordinator failures, but it increases the latency and the number of messages .
- Parallel commit is a new atomic commit protocol that reduces the latency of distributed transactions to a single round-trip of distributed consensus. It does not use a coordinator node, but instead relies on the participant nodes to independently decide on the outcome of the transaction based on a timestamp and a commit trigger. Parallel commit avoids blocking, coordinator failures, and network partitions, but it requires clock synchronization and a reliable commit trigger.
- Failure-aware commit (FLAC) is another new atomic commit protocol that improves the performance and availability of distributed transactions in the presence of failures. It uses a coordinator node and a backup node to monitor the status of the participant nodes and decide on the outcome of the transaction. FLAC avoids blocking, reduces the number of messages, and tolerates up to f failures, where f is the replication factor of the system.



### Concurrency control in distributed transactions

Concurrency control is the process of managing the concurrent access and modification of shared data by multiple transactions in a distributed database system. Concurrency control ensures that the transactions preserve the ACID (Atomicity, Consistency, Isolation, Durability) properties and do not interfere with each other or cause data inconsistency.

Some of the challenges of concurrency control in distributed transactions are:

- The transactions may span multiple data servers that are connected by a network, which introduces communication and coordination overhead.
- The transactions may access and update data that is replicated or partitioned across different data servers, which requires maintaining data consistency and availability.
- The transactions may encounter failures or conflicts during their execution, which requires recovery and resolution mechanisms.

Some of the techniques of concurrency control in distributed transactions are:

- Locking-based concurrency control protocols, which use locks to prevent concurrent transactions from accessing or modifying the same data item. Locks can be granted or denied by a centralized or distributed lock manager, depending on the locking mode and the conflict detection algorithm. Locking-based protocols can be classified into two-phase locking (2PL), rigorous 2PL, conservative 2PL, and tree-structured locking (TSL)  .
- Timestamp-based concurrency control algorithms, which use timestamps to order the transactions and determine their precedence. Timestamps can be assigned by a centralized or distributed timestamp server, or generated by the transactions themselves. Timestamp-based algorithms can be classified into basic timestamp ordering (BTO), optimistic concurrency control (OCC), and multiversion concurrency control (MVCC)  .
- Optimistic replication, which allows transactions to access and update local copies of data without locking or coordination, and then propagate the changes to other data servers asynchronously. Optimistic replication relies on conflict detection and resolution mechanisms to handle concurrent updates and ensure eventual consistency. Some examples of optimistic replication are epidemic protocols, quorum protocols, and anti-entropy protocols .
- Distributed commit protocols, which ensure that a distributed transaction either commits or aborts atomically across all the data servers involved. Distributed commit protocols require a coordinator and a set of participants to exchange messages and reach a consensus. Some examples of distributed commit protocols are two-phase commit (2PC), three-phase commit (3PC), and Paxos commit  .



### Distributed Deadlocks

- A **distributed deadlock** is a situation where a set of processes in a distributed system are waiting for each other to release resources or messages, and none of them can proceed .
- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems .
- Distributed deadlocks are harder to detect, avoid, and prevent than deadlocks in centralized systems, because there is no single authority that can oversee resource allocation and dependency graphs.
- There are three main types of distributed deadlocks:
  - **Communication deadlocks**: occur when processes are waiting for messages from each other that will never arrive.
  - **Resource deadlocks**: occur when processes are holding some resources and requesting others that are held by other processes.
  - **Hybrid deadlocks**: occur when both communication and resource deadlocks are involved.
- There are three main approaches to handle distributed deadlocks :
  - **Deadlock prevention**: avoid creating cycles in the resource allocation graph by imposing some ordering or restrictions on resource requests and releases.
  - **Deadlock avoidance**: use some information about resource availability and process requirements to make safe decisions about resource allocation that will not lead to deadlocks.
  - **Deadlock detection**: allow deadlocks to occur, but detect them and resolve them by aborting or restarting some processes or releasing some resources.
- There are several techniques to detect distributed deadlocks, such as  :
  - **Global wait-for graph**: construct a global graph of resource dependencies from local graphs at each node, and check for cycles in the global graph.
  - **Edge chasing**: propagate probe messages along the edges of the local wait-for graphs, and detect cycles when a probe returns to its originator.
  - **Diffusing computation**: initiate a diffusing computation from each blocked process, and detect a deadlock when the computation terminates without finding a free resource.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on transaction recovery for the unit 9 - distributed transactions in the subject of distributed system.

### Transaction recovery

- Transaction recovery is the process of restoring the consistency and integrity of a distributed database after a failure or an abort of a transaction.
- Transaction recovery is essential for ensuring the ACID properties of transactions, especially atomicity and durability.
- Transaction recovery involves two main steps: detecting and resolving the failures or aborts, and restoring the database to a consistent state.
- There are different types of failures or aborts that can occur in a distributed system, such as site failures, network failures, communication failures, deadlock, concurrency control violations, etc.
- There are different techniques for detecting and resolving the failures or aborts, such as timeout, voting, two-phase commit protocol, three-phase commit protocol, etc.
- There are different techniques for restoring the database to a consistent state, such as undo, redo, undo/redo, shadow versions, etc.
- Transaction recovery requires the use of logging and checkpointing mechanisms to record the changes made by transactions and to mark the stable points in the database.
- Transaction recovery also requires the coordination and cooperation of the participating sites and the transaction manager to ensure the global consistency and correctness of the database.



## Unit 10 - Replication

Replication is the process of creating and maintaining multiple copies of the same data on different database servers. Replication can improve the availability, performance, and scalability of a database system.

Some benefits of replication are:

- Availability: Replication can provide fault tolerance and disaster recovery by allowing the system to continue functioning even if one or more servers fail or become inaccessible.
- Performance: Replication can reduce the load on the primary server by distributing read requests among multiple replicas. Replication can also reduce the network latency and bandwidth consumption by serving data from local replicas to geographically dispersed clients.
- Scalability: Replication can increase the capacity of the system by adding more replicas to handle more read requests. Replication can also enable horizontal partitioning or sharding, where different subsets of data are stored on different servers.

Some challenges of replication are:

- Consistency: Replication can introduce inconsistency among replicas if updates are not propagated or applied in the same order. Replication can also cause conflicts if concurrent updates are made to the same data on different replicas. Different replication strategies have different trade-offs between consistency and availability, such as synchronous versus asynchronous replication, and strong versus eventual consistency.
- Overhead: Replication can increase the complexity and cost of the system by requiring additional hardware, software, and network resources. Replication can also increase the workload on the primary server by requiring it to send updates to all replicas. Replication can also introduce additional latency and bandwidth consumption for update propagation.
- Management: Replication can require more administration and monitoring to ensure the health and synchronization of all replicas. Replication can also require more coordination and communication among replicas to handle failures, conflicts, and schema changes. Replication can also pose security and privacy risks if replicas are not properly protected or authorized.



### System model and group communication for replication in distributed systems

- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by exchanging messages.
- Replication is a technique to improve the availability, reliability, performance, and fault-tolerance of a distributed system by creating and maintaining multiple copies of data or services across different processes or nodes.
- A system model is a set of assumptions and properties that describe the behavior and characteristics of a distributed system, such as the communication model, the failure model, the timing model, and the security model.
- A group is a subset of processes in a distributed system that share some common interest or functionality, such as a replicated service, a multicast group, or a cluster.
- Group communication is a mechanism to send and receive messages among the members of a group in a distributed system, such as broadcast, multicast, or anycast.
- Group communication can be classified into two types: reliable and unreliable.
  - Reliable group communication guarantees that a message sent by a group member is delivered to all other group members in the same order, and that no message is lost, duplicated, or corrupted.
  - Unreliable group communication does not provide any guarantee on the delivery, order, or integrity of messages, and may result in message loss, duplication, or reordering.
- Group communication can also be classified into two modes: atomic and non-atomic.
  - Atomic group communication ensures that a message sent by a group member is delivered to all other group members atomically, meaning that either all or none of them receive the message, and that they all agree on the delivery status of the message.
  - Non-atomic group communication does not ensure atomicity, and may result in some group members receiving a message while others do not, or in different group members having different views on the delivery status of a message.
- Group communication is essential for replication in distributed systems, as it enables the coordination and synchronization of replicated data or services among different group members, and the dissemination of updates or requests to all or some of the replicas.
- Group communication can also be used to implement various replication strategies, such as primary-backup, active replication, passive replication, or quorum-based replication, depending on the consistency and availability requirements of the replicated data or service.
- Group communication can also be used to handle failures and recovery of replicated data or services, such as by detecting and excluding faulty replicas, electing new leaders or coordinators, or restoring the state of failed replicas from other group members.



### Fault-tolerant services for the notes of the Unit 10 - Replication in the subject of DISTRIBUTED SYSTEM

- Fault-tolerant services are services that can continue to function correctly even in the presence of failures, such as server crashes, network partitions, or malicious attacks.
- Replication is a technique to implement fault-tolerant services by creating and maintaining multiple copies of the same service (or object) on different servers in a distributed system.
- Replication can improve availability, performance, and reliability of the service, but also introduces challenges such as consistency, concurrency, and communication overhead.
- The correctness criterion for replicated services is linearizability, which means that every operation on the service appears to take effect atomically at some point between its invocation and response, and that the order of operations is consistent with the real-time order of their invocations.
- There are two main classes of replication techniques: primary-backup replication and active replication.
  - Primary-backup replication assigns one server as the primary and the others as backups. The primary executes the operations and sends the updates to the backups. The backups apply the updates in the same order as the primary. If the primary fails, one of the backups takes over as the new primary.
  - Active replication assigns all servers as actives. The operations are multicast to all actives, which execute them in the same order and send the responses to the clients. If one or more actives fail, the others can still provide the service.
- Both replication techniques require a consensus protocol to ensure agreement among the servers on the order of operations and the identity of the primary. Consensus protocols can tolerate different types of faults, such as crash faults or Byzantine faults, depending on the assumptions and the number of servers.
- Replication can also be combined with coding theory to reduce the number of copies and the communication overhead, while still ensuring fault-tolerance. Coding theory uses mathematical techniques to encode data into smaller or more resilient units that can be used to reconstruct the original data. For example, erasure coding can split a data object into n pieces, such that any k pieces can be used to recover the object. This reduces the storage and message cost from n to k, but increases the computation cost during recovery.



### Highly Available Services for the Notes of the Unit 10 - Replication in the Subject of Distributed System

- A highly available service is a service that can provide continuous and reliable functionality to its clients, even in the presence of failures or faults in the system.
- Replication is a technique for achieving high availability by creating and maintaining multiple copies of the same data or service across different nodes or locations in a distributed system.
- Replication can improve the availability, performance, scalability, and fault tolerance of a distributed system, but it also introduces challenges such as consistency, concurrency, and communication.
- Replication can be classified into different types based on the following criteria:
  - The degree of replication: how many copies of the data or service are maintained and where they are located.
  - The timing of replication: when the copies are updated or synchronized with each other.
  - The granularity of replication: what is the unit of replication, such as a file, a record, a block, or a service.
  - The location of replication: where the copies are stored, such as in the same or different sites, networks, or regions.
  - The direction of replication: whether the updates are propagated from one master copy to the others, or from any copy to the others, or both.
  - The mode of replication: whether the updates are applied eagerly or lazily, synchronously or asynchronously, or optimistically or pessimistically.
- Some examples of replication techniques are :
  - Primary-backup replication: a master copy is designated as the primary, and the other copies are backups. The primary receives and executes all the requests from the clients, and sends the updates to the backups. The backups apply the updates in the same order as the primary. If the primary fails, one of the backups takes over as the new primary.
  - Quorum-based replication: each copy has a vote, and a quorum is a subset of copies that has enough votes to perform an operation. For example, a read quorum is a subset of copies that can provide a consistent read, and a write quorum is a subset of copies that can ensure a consistent write. A quorum-based system can tolerate failures as long as a quorum is available.
  - Lazy replication: the copies are updated asynchronously and periodically, rather than synchronously and immediately. This can improve the performance and availability of the system, but it can also cause temporary inconsistencies and conflicts among the copies. A lazy replication system needs to resolve the conflicts and reconcile the copies eventually.



### Transactions with replicated data

- Transactions are a sequence of operations that are executed atomically, consistently, isolatedly, and durably (ACID properties) on a database system.
- Replication is the process of copying data and storing it in different locations, such as multiple servers or nodes in a distributed system.
- Transactions with replicated data are transactions that involve accessing or updating data that is replicated across multiple locations.
- The main challenges of transactions with replicated data are:
  - How to ensure consistency and correctness of the replicated data after transactions, especially when there are concurrent or conflicting transactions .
  - How to handle failures or network partitions that may affect the availability and reliability of the replicated data and transactions .
- The main benefits of transactions with replicated data are:
  - Improved performance and scalability of the database system, as transactions can access or update data from the nearest or least loaded location .
  - Enhanced fault tolerance and availability of the database system, as transactions can continue to operate even if some locations are down or unreachable .
- The main types of replication schemes for transactions with replicated data are:
  - Synchronous replication: transactions wait for acknowledgments from all locations before committing, ensuring strong consistency but increasing latency and reducing availability .
  - Asynchronous replication: transactions commit without waiting for acknowledgments from all locations, ensuring high availability but risking data inconsistency or loss .
  - Quorum-based replication: transactions commit based on a quorum of acknowledgments from a subset of locations, balancing consistency and availability .
- The main types of concurrency control protocols for transactions with replicated data are:
  - Primary-copy protocol: one location is designated as the primary copy for each data item, and transactions must access or update the primary copy first, ensuring serializability but creating a bottleneck and a single point of failure .
  - Majority protocol: transactions must access or update a majority of locations for each data item, ensuring serializability but increasing communication and reducing availability .
  - Voting protocol: transactions must obtain votes from a subset of locations for each data item, ensuring serializability but requiring a voting algorithm and a coordinator .
  - Timestamp protocol: transactions are assigned timestamps and must access or update data items in timestamp order, ensuring serializability but requiring synchronization and conflict resolution .
  - Certification protocol: transactions are executed optimistically and certified at commit time, ensuring serializability but requiring validation and aborting .

