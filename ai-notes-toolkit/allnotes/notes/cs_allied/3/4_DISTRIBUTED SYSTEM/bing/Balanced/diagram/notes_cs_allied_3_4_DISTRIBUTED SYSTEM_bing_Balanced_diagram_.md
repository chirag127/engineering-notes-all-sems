

# Distributed System

A distributed system is a system whose components are located on different networked computers, which communicate and coordinate their actions by passing messages to one another. A distributed system can also be defined as a number of independent computers linked by a network.

Some characteristics of distributed systems are:

- The components are autonomous, meaning they can operate independently and have their own failure modes.
- The components are heterogeneous, meaning they can have different hardware, software, operating systems, and protocols.
- The components are scalable, meaning the system can handle increasing load and complexity by adding more components.
- The components are transparent, meaning the system hides the details of distribution from the users and applications.

Some advantages of distributed systems are:

- They can improve performance, reliability, availability, and fault-tolerance by distributing the workload and replicating the data across multiple components.
- They can enable resource sharing, collaboration, and interoperability among different users and applications.
- They can support dynamic and flexible architectures that can adapt to changing requirements and environments.

Some challenges of distributed systems are:

- They have to deal with concurrency, consistency, synchronization, and coordination issues among the components.
- They have to handle partial failures, network delays, and message losses that can affect the correctness and timeliness of the system.
- They have to cope with security, privacy, and trust issues that can arise from exposing the system to malicious attacks and unauthorized access.

Some examples of distributed systems are:

- The internet, which is a global network of interconnected computers and devices that communicate using standard protocols.
- The web, which is a collection of web servers and web browsers that exchange information using HTTP and other protocols.
- Cloud computing, which is a model of providing on-demand access to shared computing resources and services over the internet.
- Peer-to-peer systems, which are networks of equal nodes that cooperate to share resources and data without a central authority.
- Distributed databases, which are databases that store and process data across multiple computers that can be geographically distributed.



## Unit 1 - Characterization of Distributed Systems

A distributed system is a collection of independent computers that appear to the users as a single coherent system. Examples of distributed systems include the Internet, peer-to-peer networks, cloud computing, and distributed databases.

Some of the main characteristics of distributed systems are:

- **Concurrency**: Multiple components can execute simultaneously and interact with each other.
- **Lack of a global clock**: There is no shared physical clock among the components, so it is hard to synchronize events or order messages.
- **Independent failures**: Each component can fail independently without affecting the whole system, but failures are hard to detect and handle.
- **Heterogeneity**: The components can have different hardware, software, network, and data formats, which require interoperability and compatibility.
- **Scalability**: The system can grow in size and complexity without degrading its performance or functionality.
- **Transparency**: The system should hide its complexity and heterogeneity from the users and provide a consistent and uniform interface.

Some of the main challenges of designing and implementing distributed systems are:

- **Communication**: The components need to exchange messages over unreliable and unpredictable networks, which can cause delays, losses, errors, or duplication.
- **Coordination**: The components need to agree on common goals, actions, and decisions, which can be difficult due to concurrency, failures, and lack of a global clock.
- **Consistency**: The system should provide a consistent view of the data and the state of the system, which can be hard to achieve due to replication, caching, and updates.
- **Fault tolerance**: The system should be able to cope with failures and recover from them, which can require redundancy, replication, and recovery mechanisms.
- **Security**: The system should protect its data and resources from unauthorized access, modification, or disclosure, which can require authentication, authorization, encryption, and auditing.



### Introduction for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- The main characteristics of distributed systems are concurrency, scalability, fault tolerance, transparency, and heterogeneity.
- The main challenges of distributed systems are coordination, communication, consistency, reliability, security, and performance.
- The main benefits of distributed systems are resource sharing, load balancing, increased availability, and improved performance.
- The main applications of distributed systems are web services, cloud computing, distributed databases, distributed file systems, peer-to-peer networks, and mobile computing.



### Examples of Distributed Systems

A distributed system is a collection of independent computers that communicate and coordinate their actions by passing messages. The computers in a distributed system may be physically close or geographically dispersed, and they may be connected by a network or a bus. Distributed systems can provide higher performance, reliability, scalability, and availability than centralized systems.

Some examples of distributed systems are:

- **Telecommunication networks**: Telephone networks are an early example of a peer-to-peer network, where each node can initiate or receive calls. Cellular and telephone networks are forms and examples of distributed networks. They use protocols such as TCP/IP, HTTP, and SMTP to exchange data and messages.  
- **Real-time systems**: Many industries use real-time systems distributed in various areas, locally and globally. For example, air traffic control systems, power grid systems, industrial control systems, and online gaming systems are all examples of real-time distributed systems. They require fast and accurate communication and synchronization among the nodes, and they often use specialized hardware and software to meet the timing constraints.  
- **Distributed database systems**: A distributed database has locations across multiple servers, physical locations, or both. The data can be replicated or partitioned, and the system can provide concurrency control, transaction management, and fault tolerance. Examples of distributed database systems are Google's Bigtable, Amazon's Dynamo, and MongoDB.  
- **Distributed computing platforms**: A distributed computing platform is a system that allows multiple computers to work together on a common task, such as scientific computing, data analysis, or web crawling. The platform can provide load balancing, fault tolerance, and parallelism. Examples of distributed computing platforms are Apache Hadoop, Apache Spark, and Google's MapReduce.



### Resource sharing and the web challenges

Resource sharing is the process of making the resources of a distributed system available to the users and applications in a transparent and efficient way. Resources can be hardware, software, or data. The web is an example of a distributed system that enables resource sharing on a global scale.

Some of the challenges for resource sharing and the web are:

- **Scalability**: The ability to handle increasing load and demand without degrading the performance or functionality of the system. The web faces scalability challenges due to the rapid growth of users, data, and services. Some of the techniques to achieve scalability are replication, caching, load balancing, and partitioning.
- **Heterogeneity**: The diversity of hardware, software, network, and data formats in a distributed system. The web has to deal with heterogeneity at different levels, such as browsers, protocols, servers, and data formats. Some of the techniques to cope with heterogeneity are standardization, interoperability, and adaptation.
- **Fault tolerance**: The ability to continue operating correctly in the presence of failures or errors. The web has to deal with various types of faults, such as network failures, server crashes, malicious attacks, and data corruption. Some of the techniques to achieve fault tolerance are redundancy, recovery, consistency, and security.
- **Transparency**: The property of hiding the complexity and diversity of a distributed system from the users and applications. The web aims to provide transparency in terms of location, access, concurrency, replication, failure, and migration. Some of the techniques to achieve transparency are naming, middleware, synchronization, and caching.



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



### Fundamental Models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Fundamental models are descriptions of properties that are present in all distributed architectures  .
- They help us understand the characteristics, challenges and trade-offs of designing and implementing distributed systems.
- There are three main types of fundamental models: interaction models, failure models and security models  .

#### Interaction Models
- Interaction models deal with the issues of communication and coordination among processes in a distributed system  .
- They include aspects such as performance, timing, ordering and synchronization of events, and consistency and replication of data  .
- Some examples of interaction models are:
  - Synchronous vs. asynchronous communication: whether the sender and receiver of a message have to wait for each other or not  .
  - Remote procedure call (RPC) vs. message passing: whether the communication is based on invoking a procedure on a remote machine or sending a message to a destination  .
  - Client-server vs. peer-to-peer: whether the communication is based on a centralized or decentralized architecture  .
  - Publish-subscribe vs. message queue: whether the communication is based on a topic or a queue  .

#### Failure Models
- Failure models specify the types of faults that can occur in a distributed system and how they can be detected and handled  .
- They include aspects such as availability, reliability, fault tolerance and recovery  .
- Some examples of failure models are:
  - Crash vs. omission vs. arbitrary failures: whether a process stops working, misses some messages, or behaves unpredictably  .
  - Fail-stop vs. fail-silent vs. fail-noisy: whether a process can notify others of its failure, remains silent, or sends incorrect messages  .
  - Byzantine vs. non-Byzantine failures: whether a process can lie or cheat to other processes or not  .
  - Detection vs. masking vs. tolerance: whether a failure can be detected, hidden, or tolerated by the system  .

#### Security Models
- Security models specify the types of threats and attacks that can compromise the confidentiality, integrity and availability of a distributed system and how they can be prevented and mitigated  .
- They include aspects such as authentication, authorization, encryption, digital signatures and firewalls  .
- Some examples of security models are:
  - Symmetric vs. asymmetric cryptography: whether the same or different keys are used for encryption and decryption  .
  - Kerberos vs. public key infrastructure (PKI): whether a trusted third party or a distributed network of certificates is used for authentication  .
  - Denial-of-service (DoS) vs. distributed denial-of-service (DDoS) attacks: whether a single or multiple sources are used to overwhelm a target with requests  .
  - Intrusion detection vs. intrusion prevention systems: whether a system can detect or prevent unauthorized access or malicious activity  .



### Theoretical Foundation for Distributed System

A distributed system is a collection of processes that are spatially separated and do not share a common memory and communicate with one another by exchanging messages with arbitrary delays .

Some of the theoretical foundations for distributed systems are:

- **Limitations of distributed systems**: Due to the lack of a global clock, shared memory, and reliable communication, distributed systems face some inherent challenges such as synchronization, consistency, fault tolerance, and scalability .
- **Logical clocks**: Logical clocks are a way of ordering events in a distributed system based on their causal relationships, rather than their physical timestamps. Logical clocks can be implemented using Lamport's clocks or vector clocks, which assign logical timestamps to events and messages that reflect their partial or total order .
- **Concepts in message passing systems**: Message passing systems are a model of distributed computation where processes communicate by sending and receiving messages. Some of the concepts in message passing systems are: message types, message ordering, message delivery, message buffering, message passing primitives, and message passing protocols .



### Limitation of Distributed System

A distributed system is a system that consists of multiple independent components that communicate and coordinate with each other over a network. Distributed systems have many advantages, such as scalability, fault-tolerance, availability, and performance. However, they also face some limitations that make them challenging to design and implement. Some of the main limitations of distributed systems are:

- **Absence of a global state**: In a distributed system, there is no single point of control or authority that can maintain a consistent view of the system's state. Each component has its own local state, which may differ from the states of other components due to network delays, failures, or concurrency. This makes it difficult to reason about the system's behavior, ensure correctness, and coordinate actions across components. For example, it is hard to implement transactions, consensus, or synchronization in a distributed system without a global state.

- **Absence of a global clock**: In a distributed system, there is no common notion of time or ordering of events that can be agreed upon by all components. Each component has its own local clock, which may drift or skew from the clocks of other components due to hardware differences, network delays, or failures. This makes it difficult to measure the duration of events, compare the timestamps of messages, or establish causality among events. For example, it is hard to implement ordering guarantees, deadlock detection, or concurrency control in a distributed system without a global clock.

- **Network issues**: In a distributed system, the network is an essential but unreliable medium for communication and coordination among components. The network may suffer from various issues, such as latency, bandwidth limitations, congestion, packet loss, duplication, reordering, or corruption. These issues may affect the performance, availability, and correctness of the system. For example, it is hard to implement reliable communication, fault detection, or replication in a distributed system without considering network issues .

- **Security risks**: In a distributed system, the network is also a potential source of security threats and attacks. The network may be accessed by malicious or unauthorized parties, who may try to intercept, modify, or inject messages, or launch denial-of-service attacks. These attacks may compromise the confidentiality, integrity, or availability of the system. For example, it is hard to implement authentication, authorization, encryption, or digital signatures in a distributed system without addressing security risks .

These limitations of distributed systems pose significant challenges for the developers and users of such systems. They require careful design choices, trade-offs, and techniques to overcome or mitigate them. Some of the common techniques include distributed algorithms, protocols, middleware, frameworks, and tools that provide abstractions, guarantees, or services for distributed systems. However, these techniques may also introduce additional complexity, overhead, or limitations to the system. Therefore, it is important to understand the limitations of distributed systems and their implications for the system's functionality, performance, and quality.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of absence of global clock for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM.

### Absence of global clock

- A global clock is a hypothetical clock that can synchronize all the processes in a distributed system.
- A global clock would allow the processes to agree on a common notion of time and order events according to their timestamps.
- However, a global clock is impossible to implement in a distributed system due to the following reasons:
  - Physical limitations: The speed of light and the propagation delays of messages prevent the processes from having a consistent view of the global clock at any given instant.
  - Logical limitations: The processes may have different clock rates and drifts, and the clock synchronization algorithms may introduce errors and uncertainties in the clock values.
  - Fault tolerance: The global clock may fail or be corrupted by malicious processes, and the system may need to cope with clock failures and recoveries.
- Therefore, a distributed system has to deal with the absence of global clock and use other methods to coordinate and order events, such as logical clocks, vector clocks, causal ordering, etc.



### Shared Memory

- Shared memory is a programming model that allows multiple processes to access and modify the same data in a shared address space.
- Shared memory can be implemented in two ways: physically shared memory and distributed shared memory.
- Physically shared memory is when multiple processors or cores share the same physical memory, such as in a multiprocessor system or a multicore system.
- Distributed shared memory (DSM) is when multiple nodes or computers in a distributed system share a virtual address space, but do not have physical shared memory. The DSM system manages the memory across all the nodes and provides the illusion of a single shared memory.
- DSM can be achieved via software or hardware. Software DSM relies on the operating system or the middleware to handle the communication and synchronization of the shared data. Hardware DSM relies on special hardware components, such as cache coherence circuits or network interface controllers, to handle the communication and synchronization of the shared data.
- DSM has several advantages, such as:
  - It simplifies the programming of distributed applications by hiding the details of data distribution and communication.
  - It allows the programmers to use the familiar shared memory model and synchronization primitives, such as locks, semaphores, or monitors.
  - It enables the exploitation of data locality and parallelism by allowing the processes to access the shared data in their local memory or cache.
  - It supports dynamic load balancing and fault tolerance by allowing the system to migrate the shared data across the nodes according to the workload or the availability of the nodes.
- DSM also has some challenges, such as:
  - It requires a high-performance and reliable network to support the communication and synchronization of the shared data.
  - It may incur high overhead and latency due to the data transfer and consistency maintenance of the shared data.
  - It may suffer from false sharing, which is when multiple processes access different parts of the same memory block or cache line, causing unnecessary invalidations and updates of the shared data.
  - It may have scalability issues due to the limited address space or the increased contention of the shared data.



### Logical Clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A logical clock is a mechanism for capturing chronological and causal relationships in a distributed system  .
- A distributed system may have no physically synchronous global clock, so a logical clock allows global ordering on events from different processes in such systems .
- A logical clock is not a physical device, but a software counter that is incremented according to some rules .
- A logical clock can be used for computation analysis, distributed algorithm design, individual event tracking, and exploring computational progress.
- Some examples of logical clock algorithms are:
  - Lamport timestamps, which are monotonically increasing software counters that are updated based on the send and receive events of messages .
  - Vector clocks, which are arrays of software counters that are updated based on the send, receive, and local events of processes .
  - Matrix clocks, which are matrices of software counters that are updated based on the send, receive, and local events of processes and also capture the concurrency of events.
- A logical clock must satisfy the following property: if event A causally precedes event B, then the logical clock value of A is less than the logical clock value of B .
- A logical clock may not reflect the real-time order of events, as it depends on the communication delays and the synchronization protocols of the distributed system .



### Lamport's logical clocks

- Lamport's logical clocks are a way of ordering events in a distributed system without relying on physical clocks.
- Lamport's logical clocks are based on the idea of a **happens-before** relation, denoted by `->`, which captures the causal order of events.
- If `a` and `b` are events on the same process, then `a -> b` if `a` occurs before `b` based on the local clock.
- If `a` is the event of sending a message by one process and `b` is the event of receiving that message by another process, then `a -> b`.
- The happens-before relation is transitive, meaning that if `a -> b` and `b -> c`, then `a -> c`.
- Lamport's logical clocks assign a numerical value, called a **timestamp**, to each event that reflects its position in the happens-before order.
- A timestamp is a software counter that is maintained by each process and incremented after each event.
- When a process sends a message, it attaches its current timestamp to the message.
- When a process receives a message, it updates its timestamp to be the maximum of its own timestamp and the timestamp of the message, and then increments it by one.
- Lamport's logical clocks ensure that if `a -> b`, then the timestamp of `a` is less than the timestamp of `b`.
- However, the converse is not true, meaning that if the timestamp of `a` is less than the timestamp of `b`, it does not imply that `a -> b`.
- Lamport's logical clocks are also known as **scalar clocks** or **total order clocks**, because they assign a unique and totally ordered value to each event.
- Lamport's logical clocks are simple and easy to implement, but they do not capture the **concurrent** events, which are events that are not causally related and can happen in any order.
- Lamport's logical clocks are a basis for the more advanced **vector clocks**, which can capture the concurrent events and provide a **partial order** of events.



### Concepts in Message Passing Systems for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Message passing is a technique for invoking behavior (i.e., running a program) on a computer.
- Message passing is used in distributed systems, where communication is carried out between processes by passing messages from one process to another .
- A message-passing system is a subsystem of a distributed operating system (DOS) that provides a set of message-based interprocess communication (IPC) protocols.
- A message-passing system hides the complexities of sophisticated network protocols and many heterogeneous platforms from the programmers.
- A message-passing system requires a communication link to be established between the cooperating processes before messages can be sent.
- A message-passing system can support different types of messages, such as unicast, multicast, broadcast, anycast, etc.
- A message-passing system can also support different types of communication, such as synchronous, asynchronous, reliable, unreliable, etc.
- A message-passing system can have different features, such as buffering, ordering, delivery guarantees, security, etc.
- A message-passing system can be implemented using different methods, such as sockets, remote procedure calls (RPCs), remote method invocation (RMI), message-oriented middleware (MOM), etc.
- A message-passing system can have different challenges, such as network failures, message losses, message delays, message duplication, message reordering, etc.
- A message-passing system can have different solutions, such as acknowledgments, timeouts, retransmissions, sequence numbers, checksums, encryption, etc.



### Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- Causal order is a way of ordering events in a distributed system based on their causal relationships, rather than their physical timestamps or locations.
- Causal order captures the intuitive notion of "happened before" or "influenced by" among events that may occur concurrently or at different nodes in the system.
- Causal order is important for ensuring consistency, correctness, and coordination in distributed systems, especially for applications that involve communication, replication, synchronization, or concurrency control.
- Causal order can be defined formally using Lamport's logical clocks, which assign logical timestamps to events such that if event A causally precedes event B, then the timestamp of A is less than the timestamp of B.
- Causal order can also be implemented using vector clocks, which maintain a vector of logical timestamps for each node in the system, such that the ith entry of the vector represents the latest timestamp of an event that occurred at node i or was causally influenced by an event at node i.
- Causal order can be enforced by various protocols, such as causal broadcast, causal multicast, or causal delivery, which ensure that messages are delivered to the recipients in a causal order, i.e., if message m1 causally precedes message m2, then m1 is delivered before m2 at every node that receives both messages.
- Causal order is a weaker form of ordering than total order, which imposes a single linear order on all events in the system, regardless of their causal relationships. Total order is more strict and deterministic, but also more costly and restrictive for concurrency.
- Causal order is a stronger form of ordering than unordered or partial order, which do not guarantee any order among events that are not causally related. Unordered or partial order are more flexible and efficient, but also more prone to anomalies or inconsistencies.



### Total Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent entities that communicate by message passing and coordinate their actions to achieve a common goal.
- Events are occurrences that happen at a specific point in time and space in a distributed system.
- A partial order is a binary relation that is reflexive, antisymmetric, and transitive. For example, the relation "happened before" is a partial order among events in a distributed system.
- A total order is a partial order that is also complete, meaning that any two elements are comparable. For example, the relation "less than or equal to" is a total order among natural numbers.
- A distributed system is said to have partial order if we can have a partial order relationship among the events in the system . For example, if two events are causally related, meaning that one event influenced the other, then they have a partial order.
- A distributed system is said to have total order if we can have a total order relationship among all the events in the system . For example, if we can assign a unique timestamp to each event and compare them by their timestamps, then we have a total order.
- Total order is useful for distributed system implementation because it can help ensure consistency, coordination, and agreement among the entities in the system. For example, if we want to implement a shared resource that can be accessed by only one entity at a time, we can use a total order to decide which entity has the priority to access the resource.
- Total order can be implemented by using various algorithms and protocols, such as Lamport timestamps, vector clocks, logical clocks, consensus algorithms, etc . These methods can help assign a unique identifier to each event and compare them by some arbitrary mechanism to break ties .



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is some information on the topic of total causal order for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM.

### Total Causal Order

- A distributed system is a collection of independent processes that communicate by exchanging messages over a network.
- Events in a distributed system are actions that occur at a specific point in time, such as sending or receiving a message, or performing a local computation.
- The order of events in a distributed system is important for ensuring the consistency and correctness of the system's behavior and state.
- A partial order is a relation that defines a precedence among some events, but not all. For example, if event A happens before event B in the same process, then A is partially ordered before B. However, if event C happens in a different process, then there is no partial order between A and C, or between B and C.
- A causal order is a partial order that captures the potential causal influence of events on each other. For example, if event A causes event B, then A is causally ordered before B. Causality can be inferred from the message passing between processes. If event A sends a message to event B, then A is causally ordered before B. If event B sends a message to event C, then B is causally ordered before C. Therefore, by transitivity, A is causally ordered before C.
- A total order is a relation that defines a precedence among all events in the system. For example, if event A happens before event B in the global clock, then A is totally ordered before B. However, a global clock is not always available or reliable in a distributed system, so other methods are needed to establish a total order.
- A total causal order is a total order that is consistent with the causal order. It means that if event A is causally ordered before event B, then A is also totally ordered before B. However, a total causal order may not be unique, as there may be different ways to linearize the events that are concurrent (not causally related) in the system.
- A total causal order can be implemented by using a logical clock, such as a vector clock, that assigns a timestamp to each event, such that the timestamp reflects the causal order of the event. Then, a total order can be obtained by comparing the timestamps of the events, using a predefined rule, such as lexicographic order.
- A total causal order is useful for ensuring the consistency and agreement of the processes in the system, especially for applications that require atomic broadcast, distributed snapshots, or consensus.



### Techniques for Message Ordering in Distributed Systems

Message ordering is the problem of ensuring that messages sent by different processes in a distributed system are processed in a consistent and meaningful order. Message ordering is important for achieving correctness, consistency, and coordination in distributed systems.

There are different types of message ordering techniques, depending on the desired level of ordering guarantee and the trade-off between performance and complexity. Some of the common techniques are:

- **Unordered message ordering**: This is the simplest and fastest technique, where messages are delivered to the recipients as soon as they arrive, without any regard for their order. This technique is suitable for applications that do not require any ordering guarantee, such as broadcasting or gossiping.
- **FIFO (First-In-First-Out) message ordering**: This is a technique where messages sent by the same sender are delivered to the recipients in the same order as they were sent. This technique is suitable for applications that require a partial ordering guarantee, such as implementing a queue or a stack.
- **Causal message ordering**: This is a technique where messages that are causally related are delivered to the recipients in the same order as they were sent. Two messages are causally related if one message could have influenced the other, either directly or indirectly. For example, if process A sends a message to process B, and then process B sends a message to process C, then the message from A to B is causally related to the message from B to C. This technique is suitable for applications that require a logical ordering guarantee, such as implementing a distributed shared memory or a distributed database.
- **Total message ordering**: This is a technique where all messages are delivered to the recipients in the same order, regardless of their sender or causal relation. This technique is suitable for applications that require a global ordering guarantee, such as implementing a distributed consensus or a distributed transaction.

There are different protocols that can implement these message ordering techniques, such as:

- **Unicast protocols**: These are protocols that send messages to a single recipient, such as TCP or UDP. Unicast protocols can provide unordered or FIFO message ordering, depending on the underlying network layer.
- **Multicast protocols**: These are protocols that send messages to a group of recipients, such as IP multicast or reliable multicast. Multicast protocols can provide unordered, FIFO, causal, or total message ordering, depending on the design of the protocol and the use of additional mechanisms, such as timestamps, vector clocks, or sequencers.
- **Group communication protocols**: These are protocols that provide a higher-level abstraction for multicast communication, such as virtual synchrony or atomic broadcast. Group communication protocols can provide unordered, FIFO, causal, or total message ordering, as well as other properties, such as reliability, fault tolerance, or membership management.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of causal ordering of messages in distributed systems.

### Causal ordering of messages

- Causal ordering of messages is a partial ordering of messages in a distributed computing environment .
- It places a restriction on communication between processes by requiring that if the transmission of message mi to process pk necessarily preceded the transmission of message mj to the same process, then the delivery of these messages to that process must be ordered such that mi is delivered before mj.
- Causal ordering of messages is one of the four semantics of multicast communication, namely unordered, totally ordered, causal, and sync-ordered communication.
- Multicast communication methods vary according to the message’s reliability guarantee and ordering guarantee.
- Causal ordering of messages is useful for ensuring consistency and correctness of distributed applications that depend on the causal relationships between events .
- Causal ordering of messages can be implemented using various algorithms, such as vector clocks, logical clocks, or message timestamps  .
- Causal ordering of messages can be violated due to transmission delays, network congestion, or clock synchronization errors .



### Global State

- The global state of a distributed system is the **union** of the states of the individual processes and the channels .
- A process that wishes to construct a global state must infer the remote components of that state through message exchanges.
- A global state is **consistent** if it reflects a possible state of the system that could have occurred during the execution .
- A global state is **correct** if it is computed along a **consistent cut**, which is a set of local states that are causally related.
- A global state can be used for various purposes, such as debugging, checkpointing, recovery, termination detection, etc .
- A global state can be recorded by using **snapshot algorithms**, which are protocols that allow each process to record its local state and the state of its incoming channels without blocking the system execution.



### Termination Detection

Termination detection is a fundamental problem in distributed systems, where a set of processes cooperate to perform a computation. The goal is to determine when all the processes have finished their work and there are no more messages in transit between them. This is non-trivial because no process has complete knowledge of the global state, and global time does not exist.

There are different algorithms for termination detection, depending on the assumptions and properties of the distributed system. One of them is Huang's algorithm, proposed by Shing-Tsaan Huang in 1989. Huang's algorithm is based on the concept of a process' state, which can be either active or idle. An active process may become idle at any time, but an idle process may only become active again upon receiving a computational message (a message that affects the computation).

Huang's algorithm works as follows:

- Each process maintains a counter of the number of messages it has sent and received, called the local control state (LCS).
- Each process also maintains a global control state (GCS), which is a vector of the LCS of all the processes.
- Initially, the GCS is set to zero, and each process sets its LCS to zero when it becomes idle.
- Whenever a process sends a message, it increments its LCS by one, and attaches a copy of its current GCS to the message.
- Whenever a process receives a message, it increments its LCS by one, and updates its GCS by taking the component-wise maximum of its own GCS and the GCS received in the message.
- A process initiates termination detection by sending a special message, called a probe, to its neighbor in a logical ring of processes. The probe contains the initiator's GCS.
- When a process receives a probe, it compares its GCS with the probe's GCS. If they are equal, it means that the process has not sent or received any message since the probe was initiated, and it forwards the probe to its neighbor. If they are not equal, it means that the process has participated in some communication since the probe was initiated, and it updates the probe's GCS by taking the component-wise maximum of its own GCS and the probe's GCS, and forwards the probe to its neighbor.
- When the probe returns to the initiator, the initiator checks if the probe's GCS is equal to its own GCS. If they are equal, it means that the system has terminated. If they are not equal, it means that some communication has occurred since the probe was initiated, and the initiator repeats the termination detection process.

The following diagram illustrates an example of Huang's algorithm:

Huang's algorithm example

Some properties of Huang's algorithm are:

- It is a distributed algorithm, meaning that each process executes it independently and communicates with other processes only through messages.
- It is a diffusing computation algorithm, meaning that it starts from a single initiator and propagates to other processes through messages.
- It is a wave algorithm, meaning that it uses a logical ring of processes to propagate a probe message that carries information about the system state.
- It is a snapshot algorithm, meaning that it captures a consistent global state of the system at some point in time.
- It is a correct algorithm, meaning that it always detects termination if it occurs, and never detects termination if it does not occur.
- It is a fair algorithm, meaning that it does not favor any process or message over another.
- It is an efficient algorithm, meaning that it uses a minimal number of messages and computations to detect termination.



## Unit 2 - Distributed Mutual Exclusion

- Distributed mutual exclusion is a fundamental problem in distributed computing systems that ensures that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner .
- Mutual exclusion in a distributed system states that only one process is allowed to execute the critical section (CS) at any given time. In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion. Message passing is the sole means for implementing distributed mutual exclusion.
- There are two types of distributed mutual exclusion algorithms: permission-based and token-based .
- Permission-based algorithms require a process to obtain permission from other processes before entering the CS. These algorithms can be further classified into centralized, distributed, and hierarchical algorithms .
- Token-based algorithms use a special message called a token that circulates among the processes and grants the right to enter the CS. The process that holds the token can enter the CS, and then passes the token to another process. These algorithms can be further classified into ring-based, tree-based, and graph-based algorithms .
- The performance of distributed mutual exclusion algorithms can be measured by the following criteria: message complexity, synchronization delay, system throughput, and fault tolerance .
- Message complexity is the number of messages exchanged per CS execution. Synchronization delay is the time elapsed between a process requesting the CS and actually entering the CS. System throughput is the rate of CS executions in the system. Fault tolerance is the ability of the system to cope with failures of processes or communication links .
- Some examples of distributed mutual exclusion algorithms are: Ricart-Agrawala algorithm, Lamport's algorithm, Suzuki-Kasami algorithm, Raymond's algorithm, and Maekawa's algorithm .



### Classification of distributed mutual exclusion

Distributed mutual exclusion is a problem of ensuring that only one process in a distributed system can access a shared resource or data at a time. It is a fundamental requirement for achieving consistency, coordination and synchronization among the processes.

There are three basic approaches for implementing distributed mutual exclusion:

- **Token-based approach**: A unique token is shared among the sites. A site is allowed to enter its critical section if it possesses the token. Mutual exclusion is ensured because the token is unique. Examples of token-based algorithms are Ricart-Agrawala algorithm, Suzuki-Kasami algorithm and Raymond's algorithm.
- **Non-token-based approach**: A site requests permission from other sites before entering its critical section. A site is allowed to enter its critical section if it receives permission from all or a majority of other sites. Mutual exclusion is ensured by using a logical or physical clock to order the requests. Examples of non-token-based algorithms are Lamport's algorithm, Ricart-Agrawala algorithm and Maekawa's algorithm.
- **Quorum-based approach**: A site requests permission from a subset of sites, called a quorum, before entering its critical section. A site is allowed to enter its critical section if it receives permission from all the sites in the quorum. Mutual exclusion is ensured by ensuring that any two quorums have at least one site in common. Examples of quorum-based algorithms are Maekawa's algorithm, Sankaranarayanan's algorithm and Agrawala's algorithm.



### Requirement of mutual exclusion theorem for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM

- Mutual exclusion is a concurrency control property which is introduced to prevent race conditions.
- It is the requirement that a process can not enter its critical section while another concurrent process is currently present or executing in its critical section i.e only one process is allowed to execute the critical section at any given time.
- A critical section is a segment of code that accesses a shared resource or data.
- Mutual exclusion in a distributed system states that only one process is allowed to execute the critical section at any given time  .
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion.
- Message passing is the sole means for implementing distributed mutual exclusion .
- There are three basic approaches for implementing distributed mutual exclusion:
  - Token-based algorithms: A process can enter the critical section only if it possesses a unique token. The token is passed among the processes in a predefined order or by request.
  - Permission-based algorithms: A process can enter the critical section only if it obtains permission from all or a subset of the other processes in the system. The process sends request messages and waits for reply messages before entering the critical section.
  - Quorum-based algorithms: A process can enter the critical section only if it obtains permission from a majority or a quorum of the processes in the system. The process sends request messages and waits for reply messages from a quorum before entering the critical section.
- The performance of distributed mutual exclusion algorithms can be measured by the following metrics:
  - Message complexity: The number of messages exchanged per critical section entry.
  - Synchronization delay: The time elapsed between a process requesting to enter the critical section and being granted permission to do so.
  - System throughput: The number of times the critical section is executed per unit time in the system.



### Token based and non token based algorithms for distributed mutual exclusion

Distributed mutual exclusion (DME) is the problem of ensuring that only one process at a time can access a shared resource in a distributed system. There are two main types of algorithms for DME: token based and non token based.

#### Token based algorithms

- In token based algorithms, a unique token is shared among all the processes in the system. The token represents the permission to enter the critical section. Only the process that holds the token can access the shared resource.
- Token based algorithms are simple and efficient, as they do not require any message exchange between processes to request or grant the access to the resource. However, they have some drawbacks, such as the possibility of losing the token due to node or link failures, or the delay in passing the token from one process to another.
- Some examples of token based algorithms are:
  - **Suzuki-Kasami algorithm**: This is a modification of the Ricart-Agrawala algorithm, a non token based algorithm that uses request and reply messages to ensure mutual exclusion. In the Suzuki-Kasami algorithm, the token is a vector that records the number of requests made by each process. The token is passed to the process that has the highest request number in the vector. This algorithm reduces the number of messages compared to the Ricart-Agrawala algorithm, as it does not require reply messages.
  - **Raymond's algorithm**: This is a tree-based algorithm, where the processes are organized in a logical tree structure. The token is initially held by the root of the tree. A process that wants to enter the critical section sends a request message to its parent in the tree. The parent forwards the request to its parent, and so on, until it reaches the token holder. The token holder then sends the token to the requester along the reverse path of the request messages. This algorithm minimizes the number of messages and the token passing distance, as it uses the shortest path between the token holder and the requester.

#### Non token based algorithms

- In non token based algorithms, also known as permission based algorithms, a process that wants to enter the critical section communicates with a set of other processes to determine who should execute the critical section next. The communication is done by exchanging request and reply messages, which may contain timestamps to order the requests and resolve conflicts.
- Non token based algorithms are more robust and fault-tolerant, as they do not depend on a single token. However, they have higher message complexity and latency, as they require multiple message exchanges for each request.
- Some examples of non token based algorithms are:
  - **Lamport's algorithm**: This is a basic algorithm that uses logical clocks to order the requests. A process that wants to enter the critical section broadcasts a request message with its logical timestamp to all other processes. It waits for a reply message from each process, indicating that they have received the request and they are not in the critical section. The process with the smallest timestamp has the highest priority to enter the critical section. This algorithm ensures mutual exclusion and fairness, but it requires 2(N-1) messages for each request, where N is the number of processes.
  - **Ricart-Agrawala algorithm**: This is an optimization of the Lamport's algorithm, that reduces the number of messages to N-1 for each request. A process that wants to enter the critical section broadcasts a request message with its logical timestamp to all other processes. It waits for a reply message from each process that has a smaller timestamp or is not interested in the critical section. A process that has a larger timestamp or is already in the critical section defers its reply until it exits the critical section or receives a request with a smaller timestamp. This algorithm ensures mutual exclusion and fairness, but it may cause starvation, as a process may defer its reply indefinitely.



### Performance metric for distributed mutual exclusion algorithms

Distributed mutual exclusion algorithms are algorithms that ensure that only one process at a time can access a shared resource in a distributed system. The performance of these algorithms can be evaluated by the following metrics:

- **Message complexity**: It is the number of messages that are required per critical section (CS) execution by a process. It measures the communication overhead of the algorithm. A lower message complexity is desirable for better performance.
- **Synchronization delay**: It is the time interval between the departure of a process from the CS and the entry of the next process into the CS. It measures the degree of concurrency of the algorithm. A lower synchronization delay is desirable for better performance.
- **Response time**: It is the time interval between the request of a process to enter the CS and the end of its CS execution. It measures the waiting time of the process. A lower response time is desirable for better performance.
- **Throughput**: It is the number of CS executions per unit time in the system. It measures the efficiency of the algorithm. A higher throughput is desirable for better performance.

Different algorithms may have different trade-offs among these metrics. For example, a token-based algorithm may have low message complexity but high synchronization delay, while a non-token-based algorithm may have high message complexity but low synchronization delay. A quorum-based algorithm may have moderate message complexity and synchronization delay, but may suffer from quorum unavailability. Therefore, the choice of an algorithm depends on the application requirements and the system characteristics.



## Unit 3 - Distributed Deadlock Detection

- A **deadlock** is a condition where a set of processes request resources that are held by other processes in the set, and none of the processes can proceed until some of the resources are released.
- A **distributed deadlock** can occur when distributed transactions or concurrency control are utilized in distributed systems.
- **Deadlock detection** is a strategy to deal with deadlocks by examining the status of the process-resource interactions for the presence of a cyclic wait .
- **Deadlock detection** in distributed systems can be done by either a **centralized** or a **distributed** technique.
- A **centralized** technique involves a designated **deadlock detector** that collects information from all the sites and constructs a global **wait-for graph (WFG)** to detect cycles .
- A **distributed** technique involves each site maintaining a local **wait-for graph (WFG)** and exchanging messages with other sites to detect cycles .
- Some examples of distributed techniques are **edge chasing**, **path pushing**, and **diffusing computation**.
- **Edge chasing** is a technique where each site sends a **probe** message along the edges of its local WFG and waits for an **echo** message to return. If a site receives a probe message that originated from itself, it detects a cycle.
- **Path pushing** is a technique where each site sends the **path** of its local WFG along the edges and updates the path at each site. If a site receives a path that contains itself, it detects a cycle.
- **Diffusing computation** is a technique where each site initiates a **diffusing computation** when it requests a resource and waits for a reply. A diffusing computation consists of a **query** phase and a **reply** phase. In the query phase, the initiator sends a query message to all its neighbors and waits for their replies. In the reply phase, each site sends a reply message to the initiator after receiving replies from all its neighbors. If the initiator receives a reply message that indicates a cycle, it detects a deadlock.
- **Deadlock resolution** is the process of breaking the deadlock by aborting one or more of the deadlocked processes .
- **Deadlock resolution** can be done by either a **centralized** or a **distributed** technique.
- A **centralized** technique involves a designated **deadlock resolver** that decides which processes to abort based on some criteria, such as priority, age, or number of resources held.
- A **distributed** technique involves each site participating in the decision of which processes to abort based on some criteria, such as global or local timestamps, or random numbers.



### System Model for Distributed Deadlock Detection

- A distributed system consists of a collection of nodes that communicate and cooperate to achieve a common goal.
- A node can be a process, a processor, a computer, or a cluster of computers.
- A node can request, hold, and release resources that are shared among other nodes.
- A resource can be a physical device, a file, a message, a lock, or a token.
- A node can be in one of the following states: running, blocked, or terminated.
- A node is running if it is executing its own instructions and not waiting for any resource.
- A node is blocked if it is waiting for a resource that is held by another node.
- A node is terminated if it has completed its execution or aborted due to an error or a deadlock.
- A deadlock is a situation where a set of nodes are blocked and each node is waiting for a resource that is held by another node in the set.
- A deadlock can be detected by examining the status of the node-resource interactions and looking for a cycle in the wait-for graph.
- A wait-for graph is a directed graph that represents the node-resource interactions in the system.
- A node in the wait-for graph is a process or a processor that requests or holds resources.
- An edge in the wait-for graph is a directed link from a node A to a node B if A is waiting for a resource that is held by B.
- A cycle in the wait-for graph indicates a deadlock in the system.
- There are three main approaches to deadlock detection in distributed systems: centralized, hierarchical, and distributed.
- In the centralized approach, there is a designated node that collects the local wait-for graphs from all the nodes and constructs a global wait-for graph to detect deadlocks.
- In the hierarchical approach, there are multiple nodes that handle a subset of nodes or clusters of nodes and are responsible for deadlock detection within their scope. These nodes can communicate with each other to detect global deadlocks.
- In the distributed approach, there is no designated node and each node participates in deadlock detection by sending and receiving messages to other nodes. There are different algorithms for distributed deadlock detection, such as edge chasing, probe-based, and diffusing computation.



### Resource vs Communication Deadlocks

- A deadlock is a condition where a process cannot proceed because it needs to obtain a resource held by another process, and it itself is holding a resource that the other process needs.
- There are two types of deadlocks in distributed systems: resource deadlocks and communication deadlocks.
- Resource deadlocks occur when processes access resources, such as data objects in database systems and buffers in store and forward communication networks. A process acquires a resource before accessing it and releasing it after using it.
- Communication deadlocks occur when processes exchange messages, such as in message passing systems and distributed algorithms. A process sends a message to another process and waits for a reply before continuing.
- The main difference between resource deadlocks and communication deadlocks is that in resource deadlocks, the resources are held by the processes until they are released, whereas in communication deadlocks, the resources are the messages themselves, which are consumed by the processes when they are received.
- Another difference is that resource deadlocks can be detected by analyzing the resource allocation graph, which shows the processes and the resources they request and hold, whereas communication deadlocks can be detected by analyzing the wait-for graph, which shows the processes and the messages they send and wait for.
- A special case of communication deadlock is the lock | communication buffer resources deadlock, which occurs when a process is waiting for a lock on a resource and another process is waiting for a communication buffer to send a message to the first process. This deadlock can be resolved by increasing the size of the communication buffer or by using a deadlock detection algorithm.



### Deadlock Prevention for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process. In a distributed system, deadlocks are more difficult to detect and resolve because the processes and resources may be physically dispersed across multiple nodes.

Deadlock prevention is a technique to avoid the occurrence of deadlocks by ensuring that at least one of the four necessary conditions for deadlock (mutual exclusion, hold and wait, no preemption, and circular wait) is never met. There are two main methods of deadlock prevention in a distributed system:

- Ordered request: In this method, each resource type is assigned a unique number or level, and a process can request resources only in an increasing order of levels. This prevents circular wait condition, as there is a total ordering of resources.
- Collective request: In this method, a process must request all the resources it needs in one single message, and wait for the grant of all of them before proceeding. This prevents hold and wait condition, as a process does not hold any resource while waiting for another.

Both methods have some drawbacks, such as reduced concurrency, increased overhead, and wasted resources. Therefore, deadlock prevention is not always feasible or desirable in a distributed system. Alternatively, deadlock detection and recovery can be used to deal with deadlocks after they occur.



### Avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- Deadlock avoidance is a technique that tries to prevent a deadlock from occurring by ensuring that the system is always in a safe state.
- A safe state is one where there is at least one sequence of resource allocation that does not lead to a deadlock.
- Deadlock avoidance requires the system to have some knowledge of the current and future resource requests and releases of each process.
- However, deadlock avoidance is impractical in distributed systems for several reasons, such as:
  - The system may not have complete or accurate information about the global state of resources and processes.
  - The system may not be able to predict the future resource requests and releases of each process, especially if they are dynamic or unpredictable.
  - The system may incur a high overhead of communication and synchronization to maintain and update the global state information.
  - The system may have to deny some resource requests even if they do not cause a deadlock, which may reduce the system performance and utilization.
- Therefore, deadlock detection is often preferred over deadlock avoidance in distributed systems.
- Deadlock detection is a technique that tries to discover a deadlock after it has occurred by examining the status of the process-resource interactions for the presence of a cyclic wait.
- Deadlock detection requires the system to collect and analyze the global wait-for graph, which is a variant of the resource allocation graph that shows which processes are waiting for which resources.
- Deadlock detection algorithms can be classified into four categories, based on how the global wait-for graph is constructed and analyzed:
  - Path-pushing algorithms: Each process maintains a set of paths in the wait-for graph that start from itself and end at some other process. The processes exchange these paths periodically to detect cycles.
  - Edge-chasing algorithms: Each process sends a probe message along the edges of the wait-for graph to detect cycles. The probe messages are forwarded or discarded by the processes based on some rules.
  - Diffusion computation algorithms: Each process initiates a computation to detect cycles in the wait-for graph. The computation involves sending and receiving messages among the processes until a termination condition is met.
  - Global state detection algorithms: Each process periodically records its local state and sends it to a coordinator process. The coordinator process constructs and analyzes the global wait-for graph based on the collected local states.



### Detection and Resolution of Distributed Deadlocks

- A distributed deadlock is a situation where a set of processes in a distributed system are waiting for each other to release resources or send messages, and none of them can proceed.
- Detection and resolution of distributed deadlocks involve two steps: finding the existing deadlocks and breaking them by releasing some resources or aborting some processes.
- Detection of distributed deadlocks requires the maintenance and analysis of a wait-for graph (WFG), which is a directed graph that represents the dependencies among processes and resources in the system.
- There are three main approaches to maintain and search the WFG for cycles, which indicate deadlocks:
  - Centralized approach: A single site is designated as the deadlock detector, which collects the local WFG information from all other sites and constructs a global WFG. The deadlock detector periodically searches the global WFG for cycles and notifies the involved sites if a deadlock is detected. This approach is simple and efficient, but it has a single point of failure and a high communication overhead.
  - Distributed approach: Each site maintains its own local WFG and periodically exchanges it with its neighbors. Each site also runs a cycle detection algorithm on its local WFG and the received WFGs from other sites. If a cycle is detected, the site initiates a probe message along the cycle to confirm the deadlock. This approach is fault-tolerant and scalable, but it may detect false or phantom deadlocks due to inconsistent or outdated WFG information.
  - Hierarchical approach: The sites are organized into a logical tree structure, where each site has a parent and zero or more children. Each site maintains its local WFG and sends it to its parent periodically. The root of the tree constructs a global WFG and searches it for cycles. If a cycle is detected, the root sends a probe message along the cycle to confirm the deadlock. This approach combines the advantages of the centralized and distributed approaches, but it may introduce additional delays and complexities due to the tree structure.
- Resolution of distributed deadlocks involves breaking the existing wait-for dependencies in the system WFG. There are two main strategies to do so:
  - Preemption: Some processes are rolled back and their resources are released to other processes in the deadlock. This strategy preserves the atomicity and consistency of the transactions, but it may incur a high overhead and a loss of work.
  - Termination: Some processes are aborted and their resources are released to other processes in the deadlock. This strategy is simple and fast, but it may violate the atomicity and consistency of the transactions.



### Centralized Deadlock Detection

- This is a technique used in distributed systems to handle deadlock detection.
- According to this technique, the system maintains one global wait-for graph in a single chosen site, which is named as deadlock-detection coordinator.
- The coordinator collects information about the local wait-for graphs of each site and constructs the global wait-for graph.
- The coordinator periodically runs a deadlock detection algorithm on the global wait-for graph to find cycles, which indicate deadlocks.
- If a deadlock is detected, the coordinator selects a victim process to abort and sends a message to the corresponding site to terminate the process.
- The advantages of this technique are simplicity and low communication overhead.
- The disadvantages of this technique are the dependency on a single site, which may become a bottleneck or a single point of failure, and the possibility of false or phantom deadlocks due to outdated information .

: Centralized deadlock detection approach in distributed database. https://www.exploredatabase.com/2014/06/centralized-deadlock-detection-approach-in-distributed-database.html
: Deadlock Detection in Distributed Systems - javatpoint. https://www.javatpoint.com/deadlock-detection-in-distributed-systems
: Distributed Transactions - Rutgers University. https://people.cs.rutgers.edu/~pxk/417/notes/deadlock.html
: Deadlock detection in Distributed systems - GeeksforGeeks. https://www.geeksforgeeks.org/deadlock-detection-in-distributed-systems/
: Deadlock detection in distributed systems (Chapter 10) - Distributed Computing. https://www.cambridge.org/core/books/distributed-computing/deadlock-detection-in-distributed-systems/9A6629FF01607C520BC2AA034B647792



# Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set.
- Deadlocks can occur in distributed systems when distributed transactions or concurrency control are utilized.
- Deadlock detection is the approach of identifying and resolving existing deadlocks in the system.
- Deadlock detection in distributed systems entails two basic issues:
  - Detection of existing deadlocks
  - Resolution of detected deadlocks
- Deadlock detection requires examination of the status of process-resource interactions for presence of cyclic wait.
- There are three main approaches to deadlock detection in distributed systems:
  - Centralized approach
  - Hierarchical approach
  - Distributed approach
- Centralized approach:
  - One site is designated as the deadlock detector and maintains the global wait-for graph (WFG).
  - Each site sends its local WFG to the deadlock detector periodically or when a change occurs.
  - The deadlock detector checks the global WFG for cycles and initiates recovery if a deadlock is found.
  - Advantages: simple and efficient.
  - Disadvantages: single point of failure, bottleneck, and lack of scalability.
- Hierarchical approach:
  - The sites are organized into a hierarchy of clusters, each with a local deadlock detector.
  - Each site sends its local WFG to its cluster deadlock detector periodically or when a change occurs.
  - Each cluster deadlock detector sends its cluster WFG to its parent cluster deadlock detector periodically or when a change occurs.
  - The deadlock detection is performed at different levels of the hierarchy, starting from the lowest level.
  - Advantages: reduced communication and computation overhead, and improved fault tolerance.
  - Disadvantages: complex and may detect false deadlocks.
- Distributed approach:
  - There is no central or hierarchical deadlock detector, and each site participates in the deadlock detection.
  - Each site maintains its local WFG and initiates a probe message when it suspects a deadlock.
  - The probe message is propagated along the edges of the global WFG and returns to the initiator if a cycle is found.
  - The initiator then initiates the recovery if a deadlock is detected.
  - Advantages: no single point of failure, no bottleneck, and scalable.
  - Disadvantages: high communication and computation overhead, and may detect false deadlocks.



### Path Pushing Algorithms

- Path pushing algorithms detect distributed deadlocks by maintaining an explicit global wait-for graph (WFG) at each site of the distributed system .
- The global WFG is constructed by sending the local WFG of each site to all its neighboring sites whenever a deadlock computation is performed .
- The global WFG contains all the edges of the local WFGs and the edges between the sites that are waiting for resources from other sites .
- A site initiates a deadlock computation when it detects a local deadlock or receives a request from another site .
- A site detects a global deadlock if it finds a cycle in its global WFG that includes itself .
- A site can resolve a global deadlock by aborting one of the processes involved in the cycle or sending a message to another site to abort a process .
- Path pushing algorithms have the advantage of reducing the number of messages exchanged for deadlock detection, but they have the disadvantage of increasing the storage and computation overhead at each site .



### Edge Chasing Algorithms for Distributed Deadlock Detection

- Edge chasing algorithms are a class of distributed deadlock detection algorithms that use special messages called probes to trace the dependency graph of processes and resources in a distributed system.
- A probe is a triplet (i, j, k) that denotes that the deadlock detection is initiated by process P_i and the message is being sent by the home site of process P_j to the home site of process P_k.
- The probe message follows the edges of the dependency graph from the waiting processes to the blocking processes until either a cycle is detected or all the edges are traversed.
- A cycle in the dependency graph indicates a deadlock, and the processes involved in the cycle are notified to resolve the deadlock.
- Edge chasing algorithms can be classified into two types: the AND model and the OR model, depending on whether a process waits for all or any of its requested resources to be granted.
- The most well-known edge chasing algorithm for the AND model is the Chandy-Misra-Haas algorithm, which has the following steps:

  - Each process maintains a wait-for graph that contains the processes and resources that it is waiting for and the processes and resources that are waiting for it.
  - When a process P_i requests a resource R_k that is held by another process P_j, it sends a probe message (i, i, j) to the home site of P_j.
  - When a process P_j receives a probe message (i, l, j), it checks if it is involved in a deadlock with P_i. If yes, it sends a message to P_i to inform it of the deadlock. If no, it forwards the probe message (i, j, k) to the home site of each process P_k that holds a resource that P_j is waiting for.
  - When a process P_k receives a probe message (i, j, k), it checks if it is involved in a deadlock with P_i. If yes, it sends a message to P_i to inform it of the deadlock. If no, it discards the probe message.

- The advantages of edge chasing algorithms are that they are simple, efficient, and decentralized. They do not require global information or synchronization among the processes or sites.
- The disadvantages of edge chasing algorithms are that they may generate a large number of probe messages, especially in the presence of multiple initiators or concurrent requests. They may also incur false positives, meaning that they may detect a deadlock that does not exist due to the delay or loss of messages.



## Unit 4 - Agreement Protocols

- Agreement protocols are a class of distributed algorithms that allow a set of processes to reach a common decision or consensus, despite the possibility of failures or malicious behavior.
- Agreement protocols are useful for implementing fault-tolerant services, such as distributed databases, replicated state machines, leader election, atomic broadcast, etc.
- Agreement protocols can be classified into different types, depending on the assumptions and guarantees they provide, such as:
  - Crash fault tolerance: The protocol can tolerate processes that fail by halting (crashing), but not by deviating from the protocol specification (Byzantine).
  - Byzantine fault tolerance: The protocol can tolerate processes that fail by behaving arbitrarily (Byzantine), including sending conflicting or malicious messages to other processes.
  - Synchronous: The protocol assumes that there are known bounds on the message delay and the process speed, and can use timeouts to detect failures.
  - Asynchronous: The protocol does not assume any bounds on the message delay and the process speed, and cannot use timeouts to detect failures.
  - Partially synchronous: The protocol assumes that the system is asynchronous most of the time, but eventually becomes synchronous, and can use adaptive timeouts to detect failures.
  - Deterministic: The protocol guarantees that all correct processes will reach the same decision, regardless of the inputs or the message order.
  - Randomized: The protocol guarantees that all correct processes will reach the same decision with high probability, depending on the inputs and the message order.
- Some examples of agreement protocols are:
  - Paxos: A deterministic, partially synchronous, crash fault tolerant protocol that allows a set of processes to agree on a single value, such as the identity of a leader or the state of a replicated service.
  - Raft: A deterministic, partially synchronous, crash fault tolerant protocol that simplifies the design of Paxos by separating the agreement into two phases: leader election and log replication.
  - Byzantine Generals: A deterministic, synchronous, Byzantine fault tolerant protocol that allows a set of generals (processes) to agree on a common plan of action, such as attacking or retreating, despite the presence of traitors (Byzantine processes).
  - Practical Byzantine Fault Tolerance (PBFT): A deterministic, partially synchronous, Byzantine fault tolerant protocol that extends the Byzantine Generals protocol to handle multiple requests and optimize the message complexity.
  - Bitcoin: A randomized, asynchronous, Byzantine fault tolerant protocol that allows a set of nodes to agree on a distributed ledger of transactions, using a proof-of-work mechanism to prevent double-spending and Sybil attacks.



### Introduction

- Agreement protocols are a class of protocols that enable a set of processes to reach a common decision or consensus on some value or action, despite the presence of failures or uncertainties in the system.
- Agreement protocols are essential for ensuring the consistency, reliability, and availability of distributed systems, especially in the face of faults, attacks, or network partitions.
- Agreement protocols can be classified into different types, depending on the problem they aim to solve, the assumptions they make about the system model, and the properties they guarantee. Some of the common types of agreement protocols are:
  - **Atomic commit**: A protocol that ensures that a set of processes either all commit to execute a transaction or all abort it, even if some processes or the coordinator fail.
  - **Consensus**: A protocol that ensures that a set of processes agree on a single value, chosen from the set of proposed values, even if some processes fail or behave maliciously.
  - **Byzantine agreement**: A protocol that ensures that a set of processes agree on a single value, chosen from the set of proposed values, even if some processes fail or behave maliciously, and the communication channels are unreliable or compromised.
  - **Leader election**: A protocol that ensures that a set of processes elect a unique leader, who can coordinate the actions of the other processes, even if some processes fail or leave the system.
  - **Group membership**: A protocol that ensures that a set of processes maintain a consistent view of the current members of the system, even if some processes join, leave, or fail.
- Agreement protocols can be implemented using various techniques, such as message passing, shared memory, logical clocks, vector clocks, timestamps, quorums, Paxos, Raft, blockchain, etc.
- Agreement protocols can be evaluated based on various criteria, such as correctness, termination, validity, agreement, fault tolerance, resilience, safety, liveness, complexity, scalability, performance, etc.



# System Models for Distributed Systems

A system model is a description of the properties and assumptions of a distributed system that are relevant for its design, analysis, and implementation. System models can help us understand the behavior and limitations of a distributed system, as well as compare different approaches and solutions.

There are different types of system models that capture different aspects of a distributed system, such as:

- **Architectural models**: These models describe the structure and organization of the components of a distributed system and their interactions. For example, the client-server model, the peer-to-peer model, the broker model, etc.
- **Interaction models**: These models describe the communication and coordination mechanisms used by the components of a distributed system. For example, the message-passing model, the remote procedure call model, the publish-subscribe model, etc.
- **Fault models**: These models describe the types and causes of failures that can occur in a distributed system and their effects. For example, the crash model, the omission model, the byzantine model, etc.
- **Timing models**: These models describe the assumptions and guarantees about the timing and ordering of events and messages in a distributed system. For example, the synchronous model, the asynchronous model, the partially synchronous model, etc.
- **Consensus models**: These models describe the conditions and requirements for achieving agreement among the components of a distributed system on some common value or decision. For example, the Paxos model, the Raft model, the Byzantine Generals model, etc.

Each system model has its own advantages and disadvantages, and may be more or less suitable for different applications and scenarios. Therefore, it is important to understand the trade-offs and implications of choosing a particular system model for a distributed system.



### Classification of Agreement Problem

An agreement problem is a problem where a set of processes in a distributed system have to agree on a common value or decision, despite the possibility of failures or malicious behavior. Agreement problems are fundamental to the design of fault-tolerant distributed systems, as they provide a way to achieve consistency and coordination among the processes.

There are different types of agreement problems, depending on the assumptions and requirements of the system. Some of the well-known agreement problems are:

- **Byzantine agreement problem**: A single value, which is to be agreed on, is initialized by an arbitrary process and all non-faulty processes have to agree on that value. The processes may be subject to Byzantine failures, which means they can behave arbitrarily or maliciously, such as sending conflicting or incorrect messages. The goal is to ensure that all non-faulty processes agree on the same value, and that value is the initial value of some non-faulty process.   

- **Consensus problem**: A generalization of the Byzantine agreement problem, where each process can propose its own initial value, and all non-faulty processes have to agree on a common value. The value agreed on must be one of the proposed values. The processes may be subject to different types of failures, such as crash failures, omission failures, or Byzantine failures. The goal is to ensure that all non-faulty processes agree on the same value, and that value satisfies some validity condition.   

- **Interactive consistency problem**: A variation of the Byzantine agreement problem, where each process has its own initial value, and all non-faulty processes have to agree on a vector of values, one for each process. The vector agreed on must satisfy two conditions: (1) the value for each non-faulty process is its initial value, and (2) the value for each faulty process is the same for all non-faulty processes. The processes may be subject to Byzantine failures. The goal is to ensure that all non-faulty processes agree on the same vector, and that vector is consistent with the initial values of the non-faulty processes.  

These agreement problems are related to each other, and can be solved using similar techniques, such as message passing, voting, or cryptography. However, they also have different levels of difficulty and impossibility results, depending on the number of processes, the number and type of failures, the communication model, and the synchrony assumptions. For example, the Byzantine agreement problem is impossible to solve in a synchronous system with less than 3f+1 processes, where f is the number of faulty processes, while the consensus problem is impossible to solve in an asynchronous system with even one faulty process.



### Byzantine agreement problem

- The Byzantine agreement problem is a fundamental problem in fault tolerant distributed computing that requires a set of parties in a distributed environment to agree on a value even if some of the parties are corrupted.
- The problem was first defined by Lamport  and inspired by a hypothetical scenario of several divisions of the Byzantine army camped outside an enemy city, each division commanded by its own general. The generals can communicate with one another only by messenger. After observing the enemy, they must decide upon a common plan of action.
- The problem is that some of the generals may be traitors and try to prevent the loyal generals from reaching agreement. The traitors may send conflicting messages to different generals, or send no messages at all. The loyal generals need a secure way to come to agreement on a plan (known as consensus) and carry out their chosen plan (known as coordination).
- A solution to the Byzantine agreement problem is a protocol that ensures that all the loyal generals agree on the same value, and that the value is the initial value of one of the loyal generals. The protocol must be resilient to any number of traitors, as long as they do not outnumber the loyal generals.
- A number of solutions to the Byzantine agreement problem exist, depending on the assumptions made about the communication model, the synchrony of the system, the number of parties, the number of traitors, and the computational power of the parties. Some examples of solutions are:
  - The oral messages algorithm, which assumes synchronous and reliable communication, and requires more than two-thirds of the generals to be loyal.
  - The signed messages algorithm, which assumes asynchronous and reliable communication, and requires more than half of the generals to be loyal and to have digital signatures.
  - The practical Byzantine fault tolerance algorithm, which assumes partially synchronous and reliable communication, and requires more than two-thirds of the parties to be loyal and to use public-key cryptography.
- The Byzantine agreement problem is relevant for many applications in distributed systems, such as distributed databases, consensus protocols, blockchain systems, and fault-tolerant systems .



### Consensus problem

- The consensus problem is the problem of getting a set of nodes in a distributed system to agree on something - it might be a value, a course of action or a decision.
- Achieving consensus allows a distributed system to act as a single entity, with every individual node aware of and in agreement with the actions of the whole of the network.
- Consensus is a general agreement on a decision made by the majority of those involved.
- Consensus is essential for ensuring the reliability, consistency and fault-tolerance of a distributed system.
- Consensus is challenging to achieve in a distributed system because of the possibility of failures, delays, asynchrony and malicious behavior of the nodes  .
- There are many ways in which processes in a distributed system can reach a consensus, but there is usually a trade-off between security and performance.
- Some of the common consensus protocols are:
  - Two-phase commit: A simple and centralized protocol that requires a coordinator node to initiate and finalize the consensus among the participant nodes.
  - Three-phase commit: An extension of the two-phase commit protocol that adds a pre-commit phase to avoid blocking in case of coordinator failure.
  - Paxos: A family of decentralized protocols that use a quorum-based approach to tolerate failures and asynchrony among the nodes.
  - Raft: A simplified version of Paxos that uses a leader election mechanism and a replicated state machine to achieve consensus.



### Interactive Consistency Problem

- Interactive consistency is the problem in which n distinct nodes, each having its own private value, where up to t may be Byzantine, run an algorithm that allows all non-faulty nodes to infer the values of each other node  .
- Byzantine nodes are nodes that can behave arbitrarily, such as sending conflicting or incorrect messages, or remaining silent .
- Interactive consistency is a generalization of the consensus problem, where the goal is to reach agreement on a single value among all non-faulty nodes.
- Interactive consistency is relevant to critical applications that rely on the combination of the opinions of multiple peers to provide a service, such as fault-tolerant distributed systems, blockchain systems, or voting systems.
- Interactive consistency is also known as the Byzantine Generals Problem, which is a metaphor for the situation where a group of generals must coordinate an attack or retreat, but some of them may be traitors who try to sabotage the plan .
- Interactive consistency is a hard problem to solve, especially in asynchronous or partially synchronous systems, where there is no global clock or bounded message delays .
- Interactive consistency requires at least 3t + 1 nodes to be solvable, where t is the maximum number of Byzantine nodes .
- Interactive consistency can be solved using various algorithms, such as broadcast, consensus, or secret sharing algorithms  .
- Interactive consistency algorithms must satisfy the following properties :
  - Validity: If a node is non-faulty, then its value is inferred correctly by all non-faulty nodes.
  - Agreement: All non-faulty nodes infer the same value for each node.
  - Termination: All non-faulty nodes eventually infer the values of all nodes.



### Solution to Byzantine Agreement problem

- The Byzantine agreement problem is a fundamental problem in fault tolerant distributed computing that requires a set of parties to agree on a value even if some of the parties are corrupted or faulty.
- The problem was first defined by Lamport and is also known as the interactive consistency problem.
- The problem can be illustrated by the analogy of the Byzantine generals problem, where several divisions of the Byzantine army are camped outside an enemy city, each division commanded by its own general. The generals can communicate with one another only by messenger. After observing the enemy, they must decide upon a common plan of action, such as attack or retreat. However, some of the generals may be traitors and try to sabotage the plan. The loyal generals need a secure way to come to agreement on a plan (known as consensus) and carry out their chosen plan (known as coordination).
- A solution to the Byzantine agreement problem must satisfy the following properties:
  - **Agreement**: All honest parties must agree on the same value.
  - **Validity**: If all honest parties start with the same value, they must agree on that value.
  - **Termination**: All honest parties must eventually decide on a value.
- A solution to the Byzantine agreement problem also depends on the following assumptions:
  - **Synchronous communication**: There is a known upper bound on the time it takes for a message to be delivered.
  - **Authenticated messages**: The sender and the content of a message can be verified by the receiver.
  - **Number of faulty parties**: The number of faulty parties is less than a certain fraction of the total number of parties.
- One of the classical solutions to the Byzantine agreement problem is the **Oral Messages Algorithm** proposed by Lamport. The algorithm works as follows:
  - There is one source party that has an initial value and n-1 other parties that need to agree on that value.
  - The source party sends its value to all other parties.
  - Each party that receives a value from the source party sends that value to all other parties.
  - Each party that receives n-1 identical values from other parties decides on that value.
  - The algorithm repeats for m rounds, where m is the maximum number of faulty parties.
  - The algorithm guarantees that if there are at most m faulty parties, then all honest parties will agree on the same value as the source party, if the source party is honest.
  - The algorithm requires n ≥ 3m+1 parties and m+1 rounds of communication.



### Application of Agreement Problem in Distributed System

An agreement problem in distributed system is a problem where a set of processes need to reach a common decision or value based on their local inputs and messages exchanged with each other. Agreement problems are fundamental for ensuring the reliability and consistency of distributed systems, especially in the presence of faults or failures. Some examples of agreement problems are:

- **Consensus**: Each process proposes a value and all correct processes have to agree on the same value, which must be one of the proposed values .
- **Atomic Commitment**: Each process decides whether to commit or abort a transaction and all correct processes have to agree on the same decision .
- **Atomic Broadcast**: Each process broadcasts a message to all other processes and all correct processes have to deliver the same set of messages in the same order .
- **Group Membership**: Each process maintains a view of the current set of processes in the system and all correct processes have to agree on the same view .

Agreement problems have many applications in distributed systems, such as:

- **Replication**: Agreement problems can be used to ensure that multiple copies of the same data or service are consistent and available across different nodes in the system .
- **Coordination**: Agreement problems can be used to synchronize the actions or states of different processes in the system, such as leader election, distributed locking, or distributed transactions .
- **Fault Tolerance**: Agreement problems can be used to tolerate or mask the effects of faults or failures in the system, such as byzantine faults, network partitions, or message losses .

Solving agreement problems in distributed systems is challenging, as there are many factors that can affect the feasibility and complexity of the solutions, such as:

- **Synchrony**: The degree of synchrony in the system affects the assumptions and guarantees of the agreement protocols. For example, in a synchronous system, processes and messages have bounded delays, while in an asynchronous system, there are no such bounds .
- **Communication**: The type and reliability of the communication medium affects the design and performance of the agreement protocols. For example, in a reliable communication medium, messages are guaranteed to be delivered, while in an unreliable communication medium, messages can be lost, duplicated, or reordered .
- **Faults**: The number and nature of faults in the system affects the correctness and resilience of the agreement protocols. For example, in a system with byzantine faults, processes can behave arbitrarily or maliciously, while in a system with crash faults, processes can only stop functioning .

There are many algorithms and techniques for solving agreement problems in distributed systems, such as:

- **Paxos**: A family of consensus algorithms that can tolerate crash faults in asynchronous systems with reliable communication .
- **Raft**: A consensus algorithm that is similar to Paxos but easier to understand and implement, and can tolerate crash faults in partially synchronous systems with reliable communication .
- **Two-Phase Commit**: An atomic commitment protocol that can tolerate crash faults in synchronous systems with reliable communication .
- **Three-Phase Commit**: An atomic commitment protocol that can tolerate network partitions in asynchronous systems with reliable communication .
- **Total Order Broadcast**: An atomic broadcast protocol that can tolerate crash faults in synchronous systems with reliable communication .
- **Virtual Synchrony**: A group membership protocol that can tolerate crash faults and network partitions in asynchronous systems with reliable communication .
- **Byzantine Agreement**: A consensus protocol that can tolerate byzantine faults in synchronous systems with reliable communication.
- **Practical Byzantine Fault Tolerance**: A consensus protocol that can tolerate byzantine faults in partially synchronous systems with reliable communication .
- **Nakamoto Consensus**: A consensus protocol that can tolerate byzantine faults in asynchronous systems with unreliable communication, based on proof-of-work and longest chain rule .



### Atomic Commit in Distributed Database System

- An atomic commit is an operation that applies a set of distinct changes as a single operation. If the changes are applied, then the atomic commit is said to have succeeded. If the changes are not applied, then the atomic commit is said to have failed or aborted.
- In distributed database systems, the primary need for atomic commit protocols is to maintain the atomicity of distributed transactions. Atomicity means that either all the changes made by a transaction are committed, or none of them are  .
- Atomic commit protocols are used to coordinate the decision of multiple sites participating in a distributed transaction, whether to commit or abort the transaction, in the presence of failures  .
- Atomic commit protocols can be classified into two categories: blocking and non-blocking. Blocking protocols require some sites to wait for the recovery of other failed sites before making a decision. Non-blocking protocols allow some sites to make a decision without waiting for the recovery of other failed sites .
- Examples of blocking protocols are two-phase commit (2PC) and three-phase commit (3PC). Examples of non-blocking protocols are Paxos commit, Skeen's algorithm, and FLAC   .
- The performance of atomic commit protocols depends on several factors, such as the number of sites, the number of messages, the failure rate, the recovery time, and the network latency   .
- The trade-off between blocking and non-blocking protocols is that blocking protocols are simpler and faster in the absence of failures, but may cause indefinite delays or aborts in the presence of failures. Non-blocking protocols are more complex and slower in the absence of failures, but can tolerate failures and ensure progress   .



## Unit 5 - Distributed Resource Management

- Distributed resource management (DRM) is an evolving discipline that aims to enable distributed enterprise systems to operate effectively in production.
- DRM involves the coordination and optimization of various resources, such as computing, storage, network, energy, and human, across multiple locations and domains  .
- DRM can provide benefits such as improved performance, scalability, reliability, availability, security, and cost-efficiency for distributed systems  .
- DRM can also support the integration and management of distributed energy resources (DERs), such as solar panels, batteries, and demand response, which can enhance the resiliency and sustainability of the power grid .
- DRM faces challenges such as heterogeneity, dynamism, uncertainty, complexity, and scalability of distributed systems and resources .
- DRM requires a set of software, hardware, network tools, procedures, and policies to achieve its objectives  .
- DRM can be implemented in a centralized, decentralized, or hybrid manner, depending on the trade-offs between efficiency, robustness, and flexibility .
- DRM can employ various techniques and algorithms, such as resource discovery, resource allocation, resource scheduling, resource monitoring, resource adaptation, and resource negotiation, to manage distributed resources .
- DRM can leverage artificial intelligence, machine learning, optimization, game theory, and blockchain to enhance its capabilities and performance   .



### Issues in Distributed File Systems

A distributed file system (DFS) is a system that allows multiple clients to access and manipulate files stored on one or more servers over a network. A DFS provides the abstraction of a single, shared namespace for files and directories, hiding the details of their physical locations and distribution. A DFS can improve the performance, reliability, scalability, and security of file access and management.

However, designing and implementing a DFS also poses many challenges and issues, such as:

- **Naming and transparency**: How to assign unique and meaningful names to files and directories, and how to support different levels of transparency for clients, such as location transparency, access transparency, replication transparency, failure transparency, etc.
- **Consistency and caching**: How to ensure that the clients see a consistent view of the files and directories, and how to use caching techniques to reduce the network traffic and improve the performance. How to handle concurrent updates, conflicts, and coherence issues among multiple caches.
- **Replication and fault tolerance**: How to replicate files and directories across multiple servers for improving availability, reliability, and performance, and how to handle failures and recoveries of servers, clients, and network components. How to maintain consistency and synchronization among replicas, and how to balance the load among servers.
- **Security and access control**: How to protect the files and directories from unauthorized access, modification, or deletion, and how to enforce different access policies and permissions for different users and groups. How to provide authentication, encryption, and auditing mechanisms for ensuring the security and integrity of the data and the communication.
- **Scalability and performance**: How to support a large number of clients, servers, files, and directories, and how to handle the increasing demand for storage and bandwidth. How to optimize the performance of the DFS by using techniques such as caching, prefetching, striping, compression, etc.
- **Interoperability and compatibility**: How to enable the DFS to work with different types of clients, servers, operating systems, file formats, and protocols, and how to ensure the compatibility and interoperability among them. How to support the migration and integration of legacy systems and applications.

These are some of the main issues that need to be addressed in the design and use of a DFS. Different DFSs may adopt different solutions and trade-offs for these issues, depending on their requirements and goals. Some examples of DFSs are NFS, AFS, Coda, HDFS, etc.



### Mechanism for building distributed file systems

A distributed file system (DFS) is a file system that is distributed on multiple file servers or locations. It allows programs to access or store isolated files as they do with the local ones, allowing programmers to access files from any network or computer.

The mechanism for building distributed file systems involves the following aspects:

- Use of file models: The DFS uses different conceptual models of a file. The following are the two basic criteria for file modeling, which include file structure and modifiability. The files can be unstructured or structured based on the applications used in file systems. The files can also be immutable or mutable depending on whether they can be modified or not.
- Use of file accessing models: A distributed file system may use one of the following models to service a client’s file request: upload/download, remote access, or remote service. The upload/download model involves transferring the entire file between the client and the server. The remote access model involves sending file operations to the server and receiving the results. The remote service model involves executing the file operations on the server and sending the results to the client.
- Use of file replication: File replication is the primary mechanism for improving file availability in a distributed systems environment. A replicated file is a file that has multiple copies with each copy located on a separate file server. The challenges of file replication include maintaining consistency, coherence, and fault tolerance among the replicas .
- Use of file caching: File caching is the mechanism of storing frequently accessed files or parts of files in the local memory of the client or the server. This reduces the network traffic and improves the performance of the file system. The challenges of file caching include maintaining cache consistency, coherence, and fault tolerance.
- Use of file naming: File naming is the mechanism of assigning unique and meaningful names to the files in a distributed file system. A file name consists of two parts: a file identifier and a file path. A file identifier is a unique and immutable name that refers to the file content. A file path is a logical and mutable name that refers to the file location. A distributed file system may use one of the following naming schemes: flat, hierarchical, or attribute-based.
- Use of file namespaces: A file namespace is a logical structure that organizes the files in a distributed file system. A file namespace may consist of one or more file servers, each with its own local namespace. A distributed file system may use one of the following mechanisms to create a global namespace: mounting, unioning, or linking. Mounting involves attaching a local namespace to a specific point in another namespace. Unioning involves merging two or more namespaces into one. Linking involves creating symbolic links that refer to files in other namespaces .



### Design issues in Distributed Shared Memory

Distributed Shared Memory (DSM) is a mechanism that allows multiple processes on different nodes to share a common logical address space and access data transparently. DSM can simplify the programming of distributed systems by hiding the details of inter-process communication. However, DSM also introduces several design issues that affect its performance, scalability, and correctness. Some of the main design issues in DSM are:

- **Granularity**: Granularity refers to the size of the unit of sharing and the unit of coherence in DSM. A smaller granularity (such as a byte or a word) can reduce the amount of false sharing and improve the locality of access, but it can also increase the overhead of coherence maintenance and communication. A larger granularity (such as a page or a segment) can reduce the overhead of coherence and communication, but it can also increase the amount of false sharing and waste bandwidth and memory. Therefore, choosing an appropriate granularity is a trade-off between these factors.

- **Structure**: Structure refers to the organization of the shared data in the logical address space and the mapping of the shared data to the physical memory of the nodes. The structure of DSM can be flat, hierarchical, or object-based. A flat structure treats the shared data as a single linear array and maps it to the nodes using a static or dynamic hashing function. A hierarchical structure divides the shared data into multiple regions and assigns each region to a node or a group of nodes. An object-based structure organizes the shared data into objects and allows the nodes to access the objects by name or reference. The structure of DSM affects the ease of programming, the locality of access, and the scalability of the system.

- **Coherence semantics**: Coherence semantics define the consistency model of DSM, which specifies the order and visibility of the updates to the shared data. Coherence semantics can be strict, relaxed, or weak. A strict coherence semantics (such as sequential consistency) guarantees that all the nodes see the same order of updates and the updates are immediately visible to all the nodes. A relaxed coherence semantics (such as release consistency) allows some reordering and delay of updates, but requires the programmer to use synchronization operations to ensure the correctness of the program. A weak coherence semantics (such as eventual consistency) does not impose any order or visibility constraints on the updates, but relies on the application logic to handle the possible inconsistencies. The coherence semantics of DSM affect the performance, scalability, and programmability of the system.

- **Coherence protocols**: Coherence protocols implement the coherence semantics of DSM by maintaining the consistency of the shared data among the nodes. Coherence protocols can be classified into two categories: directory-based and broadcast-based. A directory-based protocol uses a directory to keep track of the location and state of each unit of shared data and sends messages to the nodes that have a copy of the data when an update occurs. A broadcast-based protocol uses a broadcast medium (such as a bus or a network) to propagate the updates to all the nodes and relies on the nodes to invalidate or update their copies of the data. The coherence protocols of DSM affect the overhead, scalability, and fault-tolerance of the system.

- **Scalability**: Scalability refers to the ability of DSM to handle the increase in the number of nodes, the size of the shared data, and the frequency of the accesses to the shared data. Scalability depends on several factors, such as the granularity, the structure, the coherence semantics, and the coherence protocols of DSM. A scalable DSM should minimize the communication and synchronization overhead, balance the load and memory usage among the nodes, and adapt to the changes in the workload and the environment.

- **Heterogeneity**: Heterogeneity refers to the diversity of the nodes in terms of their hardware, software, and network characteristics. Heterogeneity can affect the performance, compatibility, and portability of DSM. A heterogeneous DSM should be able to handle the differences in the processor architectures, the operating systems, the programming languages, the network protocols, and the network topologies of the nodes. A heterogeneous DSM should also be able to cope with the variations in the processing speed, the memory capacity, the network bandwidth, and the network latency of the nodes.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is a summary of the algorithm for implementation of distributed shared memory for the notes of the Unit 5 - Distributed Resource Management in the subject of DISTRIBUTED SYSTEM.

### Algorithm for Implementation of Distributed Shared Memory

Distributed shared memory (DSM) is a technique that allows multiple processes on different nodes of a distributed system to access a common virtual address space as if they were running on a single machine. DSM can simplify the programming of distributed applications by providing a shared memory abstraction. However, DSM also introduces challenges such as maintaining consistency, coherence, and performance of the shared data.

There are different algorithms for implementing DSM, each with its own advantages and disadvantages. Some of the basic algorithms are:

- **Central Server Algorithm**: In this algorithm, a central server maintains all the shared data and services read and write requests from other nodes. The central server can use a page-based or an object-based approach to manage the shared data. The advantage of this algorithm is that it is simple and ensures consistency and coherence of the shared data. The disadvantage is that it introduces a single point of failure and a bottleneck for communication and computation.  

- **Migration Algorithm**: In this algorithm, the shared data is distributed among the nodes and can migrate from one node to another based on the access patterns. Each data item has a home node that keeps track of its current location and grants read or write permissions to other nodes. When a node requests to access a data item that is not locally available, the home node sends the data item to the requesting node and updates its location. The advantage of this algorithm is that it reduces the communication overhead and improves the locality of the shared data. The disadvantage is that it may cause frequent data migrations and increase the complexity of managing the shared data.  

- **Replication Algorithm**: In this algorithm, the shared data is replicated on multiple nodes and can be accessed locally by the processes. Each data item has a home node that maintains a list of replicas and coordinates the updates. When a node requests to read a data item, it can access its local copy. When a node requests to write a data item, it sends the update to the home node, which then propagates the update to all the replicas. The advantage of this algorithm is that it enhances the availability and fault-tolerance of the shared data. The disadvantage is that it may incur high storage and bandwidth costs and create consistency and coherence issues.  

- **Invalidation Algorithm**: In this algorithm, the shared data is distributed among the nodes and can be cached locally by the processes. Each data item has a home node that maintains a list of caches and invalidates them when necessary. When a node requests to access a data item that is not locally cached, the home node sends the data item to the requesting node and adds it to the list of caches. When a node requests to write a data item, it sends the update to the home node, which then invalidates all the other caches of the data item. The advantage of this algorithm is that it reduces the communication and storage overhead and preserves the coherence of the shared data. The disadvantage is that it may cause cache misses and invalidate useful data.  

The choice of the algorithm for implementing DSM depends on various factors such as the size and structure of the shared data, the access patterns and frequency of the processes, the network topology and bandwidth, and the consistency and performance requirements of the application.  




## Unit 6 - Failure Recovery in Distributed Systems

- Failure recovery is the process of restoring a distributed system to a consistent and correct state after a failure occurs.
- Failures can be classified into three types: crash failures, omission failures, and Byzantine failures.
- Crash failures occur when a process stops executing and does not resume. Omission failures occur when a process fails to send or receive a message. Byzantine failures occur when a process behaves arbitrarily or maliciously, such as sending incorrect or conflicting messages.
- Failure recovery techniques can be divided into two categories: backward recovery and forward recovery.
- Backward recovery involves undoing the effects of a failure and restoring the system to a previous consistent state. This can be achieved by using checkpoints, logging, and rollback protocols.
- Forward recovery involves correcting the effects of a failure and continuing the execution from the current state. This can be achieved by using redundancy, replication, and fault tolerance protocols.
- Checkpoints are snapshots of the system state that are periodically saved on stable storage. They can be used to restart the execution from a consistent point after a failure.
- Logging is the process of recording the events and actions that occur in the system. Logs can be used to replay or undo the events and actions after a failure.
- Rollback protocols are algorithms that coordinate the processes to restore a consistent state after a failure. They can be based on synchronous or asynchronous communication, and on pessimistic or optimistic assumptions.
- Redundancy is the provision of extra resources or components that can take over the functionality of a failed component. Redundancy can be static or dynamic, and can be applied at different levels of granularity.
- Replication is the creation and maintenance of multiple copies of the same data or service. Replication can improve availability, performance, and fault tolerance of the system.
- Fault tolerance protocols are algorithms that enable the system to tolerate a certain number of failures and continue to provide correct service. They can be based on consensus, voting, or quorum techniques.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on the concepts of backward and forward recovery in distributed systems.

### Concepts in Backward and Forward Recovery

- Backward recovery and forward recovery are two techniques to deal with failures in distributed systems.
- A failure is an event that causes a deviation from the expected behavior of a system or a component.
- A recovery is a process that restores the system or the component to a correct state after a failure.

#### Backward Recovery

- Backward recovery is a technique that moves the system or the component from its current state back to a previous correct state.
- Backward recovery requires periodic checkpointing, which is the process of saving the state of the system or the component at certain points in time.
- Checkpoints can be local or global. A local checkpoint is taken by a single component independently. A global checkpoint is a consistent set of local checkpoints taken by all the components in the system.
- Backward recovery also requires logging, which is the process of recording the actions or events that occur in the system or the component.
- Logging can be pessimistic or optimistic. A pessimistic logging records every action or event before it is executed. An optimistic logging records every action or event after it is executed.
- Backward recovery involves rolling back, which is the process of restoring the state of the system or the component from a checkpoint and undoing the actions or events that occurred after the checkpoint.
- Rolling back can be selective or non-selective. A selective rolling back restores only the state of the failed component and its dependent components. A non-selective rolling back restores the state of the entire system.
- Backward recovery can be coordinated or non-coordinated. A coordinated backward recovery requires the agreement of all the components in the system to roll back to a global checkpoint. A non-coordinated backward recovery allows each component to roll back to its own local checkpoint independently.

#### Forward Recovery

- Forward recovery is a technique that moves the system or the component from its current state to a new correct state.
- Forward recovery requires error detection, which is the process of identifying the presence of a failure in the system or the component.
- Error detection can be active or passive. An active error detection periodically probes the system or the component to check its status. A passive error detection waits for the system or the component to report its status or an exception.
- Forward recovery also requires error correction, which is the process of removing the cause or the effect of a failure in the system or the component.
- Error correction can be masking or compensation. A masking error correction hides the failure from the rest of the system or the component by providing an alternative service or output. A compensation error correction modifies the state or the behavior of the system or the component to overcome the failure.
- Forward recovery involves retrying, which is the process of repeating the action or the event that caused the failure or was affected by the failure.
- Retrying can be backward or forward. A backward retrying executes the action or the event from the same state as before the failure. A forward retrying executes the action or the event from a different state than before the failure.



### Recovery in Concurrent Systems

- Recovery in concurrent systems is the process of restoring the system to a consistent state after a failure, while multiple transactions are being executed simultaneously.
- Recovery in concurrent systems is challenging because the interleaving of logs from different transactions makes it difficult to backtrack and undo the effects of failed transactions.
- Recovery in concurrent systems can be done in two ways: backward recovery and forward recovery.
- Backward recovery is the process of moving the system from its current state back to a previously correct state by undoing the changes made by failed transactions. This requires periodically recording the system's state (checkpoints) and restoring it when a failure occurs.
- Forward recovery is the process of moving the system from its current state to a new correct state by redoing the changes made by committed transactions. This requires maintaining a log of all the actions performed by each transaction and applying them to the system after a failure.
- Recovery in concurrent systems also depends on the concurrency control scheme that is used to ensure serializability and avoid conflicts among transactions. Some of the concurrency control schemes are:
  - Locking: Transactions acquire locks on the data items they access and release them after they commit or abort. Locks prevent other transactions from accessing the same data items concurrently. Locking can be done at different levels of granularity, such as records, pages, or tables.
  - Timestamping: Transactions are assigned timestamps based on their arrival order and use them to order their accesses to the data items. Timestamps ensure that older transactions have priority over newer transactions and avoid conflicts. Timestamping can be done in two ways: optimistic and pessimistic.
  - Validation: Transactions execute without any concurrency control and validate their results before committing. Validation checks whether the transaction's execution is equivalent to some serial execution and aborts the transaction if it is not. Validation can be done in two ways: pre-validation and post-validation.
  - Multiversion: Transactions access multiple versions of the data items and create new versions when they update them. Multiversion concurrency control allows transactions to read consistent snapshots of the database and avoid conflicts. Multiversion concurrency control can be done in two ways: multiversion timestamping and multiversion locking.



### Obtaining consistent Checkpoints for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Failure recovery in distributed systems is the process of restoring the system to a consistent and correct state after a failure occurs.
- A failure can be a crash, a communication loss, a data corruption, or a malicious attack.
- A consistent state is one that satisfies the system's correctness properties, such as atomicity, consistency, isolation, and durability.
- A checkpoint is a snapshot of the system state at a certain point in time, which can be used to resume the execution after a failure.
- Obtaining consistent checkpoints is a challenge in distributed systems, because different components may have different views of the global state, and concurrent events may cause inconsistencies.
- There are different techniques for obtaining consistent checkpoints, such as:
  - Coordinated checkpointing: All components coordinate to take a checkpoint at the same time, or use a global clock to synchronize their checkpoints. This ensures a consistent global state, but may incur high overhead and blocking.
  - Uncoordinated checkpointing: Each component takes a checkpoint independently, without any coordination with others. This reduces the overhead and blocking, but may result in inconsistent global state and orphan processes.
  - Communication-induced checkpointing: Each component takes a checkpoint based on the messages it receives from others, and piggybacks checkpoint information on the messages it sends. This avoids blocking and reduces the number of checkpoints, but may require complex algorithms to ensure consistency.
- The choice of checkpointing technique depends on the characteristics of the system, such as the frequency and type of failures, the communication pattern, the performance requirements, and the availability of global clock.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on recovery in distributed database systems:

### Recovery in Distributed Database Systems

- Recovery is the process of restoring the database to a consistent state after a failure or an error.
- Recovery is essential to maintain the atomicity and durability of transactions, which are the properties that ensure that a transaction either completes entirely or has no effect, and that the effects of a committed transaction are permanent.
- Recovery in distributed database systems is more complicated than in centralized systems, because failures can occur at different sites or communication links, and transactions can span multiple sites.
- There are two types of failures that can affect a distributed database system: soft failures and hard failures.
  - Soft failures are temporary and do not cause physical damage to the database, such as power outages, network failures, or software errors. Soft failures can result in inconsistency of the database, such as lost updates, uncommitted data, or incorrect data.
  - Hard failures are permanent and cause physical damage to the database, such as disk crashes, fire, or theft. Hard failures can result in loss of data or availability of the database.
- There are two types of recovery techniques that can be used to handle failures in distributed database systems: local recovery and global recovery.
  - Local recovery is the process of restoring a single site or a single transaction to a consistent state after a failure. Local recovery can use techniques such as undo, redo, or undo/redo, which are based on logging the changes made by transactions and applying them in reverse or forward order to restore the database.
  - Global recovery is the process of restoring the entire distributed database to a consistent state after a failure. Global recovery can use techniques such as two-phase commit, three-phase commit, or voting, which are based on coordinating the commit or abort decisions of all the sites involved in a distributed transaction.



## Unit 7 - Fault Tolerance

- Fault tolerance is the ability of a system to continue functioning correctly in the presence of failures.
- Fault tolerance can be achieved by using techniques such as redundancy, replication, recovery, and reconfiguration.
- Fault tolerance can be classified into two types: hardware fault tolerance and software fault tolerance.
- Hardware fault tolerance is the ability of a system to tolerate failures of physical components, such as processors, memory, disks, or network devices.
- Hardware fault tolerance can be achieved by using techniques such as:
  - RAID (Redundant Array of Independent Disks): a technique that uses multiple disks to store data in a way that improves performance and reliability.
  - N-modular redundancy: a technique that uses multiple identical components to perform the same function, and uses a voting mechanism to select the correct output.
  - Hot swapping: a technique that allows replacing a faulty component with a spare one without shutting down the system.
- Software fault tolerance is the ability of a system to tolerate failures of software components, such as processes, threads, or messages.
- Software fault tolerance can be achieved by using techniques such as:
  - Checkpointing and rollback: a technique that periodically saves the state of a process, and restores it to a previous state in case of a failure.
  - Exception handling: a technique that allows a process to detect and handle errors that occur during its execution, and resume normal operation or terminate gracefully.
  - Fault masking: a technique that hides the occurrence of a fault from the rest of the system, and provides a correct output despite the fault.
  - Fault injection: a technique that deliberately introduces faults into a system to test its fault tolerance and identify potential vulnerabilities.



### Issues in Fault Tolerance for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Fault tolerance is the ability of a system to continue functioning correctly in the presence of failures.
- Fault tolerance is important for distributed systems because they consist of multiple components that may be subject to different types of failures, such as hardware failures, software failures, network failures, malicious attacks, etc.
- Fault tolerance can be achieved by using various techniques, such as redundancy, replication, checkpointing, recovery, consensus, etc.
- Fault tolerance faces several challenges in distributed systems, such as:
  - How to detect and identify failures in a timely and accurate manner?
  - How to coordinate and synchronize the actions of multiple components that may have inconsistent or incomplete views of the system state?
  - How to cope with the trade-offs between performance, availability, consistency, and cost?
  - How to handle the dynamic and heterogeneous nature of distributed systems, such as changes in network topology, resource availability, workload, etc?



### Commit Protocols

- Commit protocols are algorithms that ensure the atomicity of distributed transactions, i.e., all the sites involved in a transaction either commit or abort it unanimously, even in the presence of failures  .
- Commit protocols are necessary to maintain the consistency and reliability of distributed systems, as they prevent partial commits or inconsistent states  .
- There are different types of commit protocols, such as one-phase commit (1PC), two-phase commit (2PC), and three-phase commit (3PC)    .
- One-phase commit (1PC) is the simplest protocol, where a coordinator sends a commit request to all the participants, and they either commit or abort the transaction based on their local state .
- One-phase commit (1PC) has the advantage of being fast and simple, but it has the disadvantage of being unreliable, as it does not handle failures or concurrency issues .
- Two-phase commit (2PC) is the most widely used protocol, where a coordinator initiates a voting phase, where it asks all the participants to prepare to commit or abort the transaction, and then a commit phase, where it decides to commit or abort based on the votes    .
- Two-phase commit (2PC) has the advantage of being reliable and consistent, as it ensures that all the participants agree on the outcome of the transaction, and it handles failures by using timeouts and log records    .
- Two-phase commit (2PC) has the disadvantage of being blocking, as it requires all the participants to wait for the coordinator's decision, and it may cause deadlock or livelock if the coordinator or some participants fail or lose communication    .
- Three-phase commit (3PC) is an extension of 2PC, where a coordinator adds a pre-commit phase, where it asks all the participants to enter a prepared state, before sending the final commit or abort decision .
- Three-phase commit (3PC) has the advantage of being non-blocking, as it allows the participants to decide the outcome of the transaction independently if the coordinator fails or loses communication, and it avoids deadlock or livelock by using timeouts and majority voting .
- Three-phase commit (3PC) has the disadvantage of being more complex and costly, as it requires an extra phase and more messages, and it may still fail in some scenarios, such as network partitions or simultaneous failures .



### Voting protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Voting protocols are a type of consensus protocols that allow a set of distributed nodes to agree on a common value or decision.
- Voting protocols are useful for achieving fault tolerance in distributed systems, as they can tolerate the failure or malicious behavior of some nodes, as long as a majority of nodes are correct and reachable.
- Voting protocols can be classified into two categories: exact voting and inexact voting.
  - Exact voting requires that all nodes agree on the same value or decision, and that the value or decision is correct according to some predefined criterion. Examples of exact voting are two-phase commit, three-phase commit, and Paxos.
  - Inexact voting allows some nodes to have different or incorrect values or decisions, as long as the majority of nodes have the same or correct value or decision. Examples of inexact voting are majority voting, weighted voting, and probabilistic voting.
- Voting protocols can also be classified into two categories based on the security properties they provide: secure voting and non-secure voting.
  - Secure voting ensures that the voting process is resilient to attacks from malicious nodes or external adversaries, who may try to manipulate, forge, or disrupt the votes. Secure voting typically involves cryptographic techniques such as encryption, digital signatures, or zero-knowledge proofs. Examples of secure voting are Byzantine fault tolerance, Practical Byzantine fault tolerance, and HoneyBadgerBFT.
  - Non-secure voting does not provide any security guarantees, and assumes that the nodes are honest and cooperative. Non-secure voting is simpler and faster than secure voting, but more vulnerable to attacks. Examples of non-secure voting are majority voting, weighted voting, and probabilistic voting.



### Dynamic voting protocols

- Dynamic voting protocols are a technique for maintaining consistency and availability of replicated data in distributed systems.
- The idea is to assign a number of votes to each replica of a data item, and require a majority of votes to access or update the data item.
- The number of votes can be dynamically adjusted based on the availability and reliability of the replicas, the network topology, and the access patterns of the data item.
- Dynamic voting protocols can improve the performance and fault tolerance of distributed systems by reducing the communication and synchronization overhead, and by allowing flexible trade-offs between consistency and availability.
- Some examples of dynamic voting protocols are:

  - Dynamic weighted voting: A protocol that assigns different weights to different replicas based on their availability and reliability, and requires a weighted majority of votes to access or update the data item  .
  - Topological dynamic voting: A protocol that assigns votes to replicas based on their network proximity and connectivity, and requires a majority of votes from the same non-partitionable group to access or update the data item.
  - Quorum-based voting: A protocol that defines a set of quorums (subsets of replicas) for each data item, and requires a quorum to access or update the data item. The quorums can be dynamically chosen or reassigned based on the availability and reliability of the replicas, and the consistency and availability requirements of the data item .



## Unit 8 - Transactions and Concurrency Control

A transaction is a logical unit of work that consists of a sequence of database operations, such as insertions, deletions, updates, and queries. A transaction has the following properties:

- Atomicity: A transaction is either executed in its entirety or not at all. If a transaction fails, the database is restored to its state before the transaction started.
- Consistency: A transaction preserves the consistency of the database, meaning that it does not violate any integrity constraints or business rules.
- Isolation: A transaction is executed as if it is the only one running on the database, meaning that it does not interfere with or see the effects of other concurrent transactions.
- Durability: The effects of a transaction are permanent, meaning that they persist even if the system fails or restarts.

Concurrency control is the process of managing the simultaneous execution of transactions on a shared database, such that the transactions do not conflict with each other and the database remains consistent. Concurrency control techniques can be classified into two categories:

- Locking-based: A locking protocol is a set of rules that determines when a transaction can acquire or release a lock on a data item. A lock is a mechanism that grants exclusive or shared access to a data item to a transaction. Locking protocols can prevent concurrency problems such as lost updates, uncommitted data, and inconsistent reads, but they may also cause deadlock, where two or more transactions are waiting for each other to release locks.
- Timestamp-based: A timestamp is a unique identifier that indicates the order of transactions. A timestamp-based protocol is a set of rules that determines whether a transaction can read or write a data item based on its timestamp and the timestamps of other transactions that have accessed the same data item. Timestamp-based protocols can prevent concurrency problems such as lost updates, uncommitted data, and inconsistent reads, but they may also cause aborts, where a transaction is rolled back because it has violated the timestamp order.



### Transactions
- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the operations in a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction does not interfere with other concurrent transactions.
- Durability means that the effects of a committed transaction are permanent and survive failures.

### Concurrency Control
- Concurrency control is the process of managing simultaneous access to shared data in a database by multiple transactions.
- Concurrency control ensures that the transactions are executed in a correct and consistent manner, without violating the ACID properties.
- Concurrency control can be implemented using various techniques, such as locking, timestamping, validation, and multiversioning.

### Distributed Transactions and Distributed Concurrency Control
- A distributed transaction is a transaction that spans multiple data servers in a distributed database system.
- A distributed transaction consists of a set of subtransactions, each of which is executed by one data server.
- A distributed transaction coordinator is responsible for coordinating the execution and commitment of the subtransactions across the data servers.
- A distributed transaction has the same ACID properties as a local transaction, but it also requires global atomicity and global consistency.
- Global atomicity means that either all the subtransactions of a distributed transaction are committed or all of them are aborted.
- Global consistency means that a distributed transaction preserves the integrity constraints of the distributed database.
- Distributed concurrency control is the concurrency control of a distributed database system, where relevant data is hosted by a group of linked data servers.
- Distributed concurrency control makes sure that all subtransactions of a set of distributed transactions are serialized identically in all data servers involved.
- Distributed concurrency control can be implemented using various techniques, such as two-phase locking, two-phase commit, distributed timestamping, distributed validation, and distributed multiversioning.



### Nested transactions

- A nested transaction is a transaction that is composed of subtransactions, each of which may have its own begin and end points.
- A nested transaction can be used to implement partial rollback, modular programming, and concurrency control in distributed systems.
- A nested transaction has a tree structure, where the root is the top-level transaction and the leaves are the subtransactions.
- A nested transaction can be either flat or nested distributed, depending on whether it accesses objects handled by different servers or not.
- A nested transaction can be either open or closed, depending on whether it allows communication with other transactions or not.
- A nested transaction can have different commit protocols, such as two-phase commit, nested two-phase commit, or multilevel commit, depending on how the subtransactions coordinate their decisions.
- A nested transaction can have different serializability criteria, such as conflict serializability, strict serializability, or snapshot serializability, depending on how the subtransactions order their operations.
- A nested transaction can have different recovery mechanisms, such as undo, redo, or compensation, depending on how the subtransactions handle failures.
- A nested transaction can have different deadlock detection and resolution strategies, such as timeout, wound-wait, or wait-die, depending on how the subtransactions handle conflicts.



### Locks for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A lock is a mechanism that allows only one of the innumerable nodes (or processes) to access and modify a resource or data that is being shared commonly to prevent execution of same task twice and also maintain data integrity.
- Locks are designed to enforce a mutual exclusion concurrency control policy, which means that only one node can hold a lock on a resource at a time, and other nodes have to wait until the lock is released before they can access the resource.
- Locks can be classified into different types based on the following criteria:
  - The granularity of the resource: locks can be applied to the whole database, a table, a page, a record, or a field.
  - The mode of the lock: locks can be either shared or exclusive. A shared lock allows multiple nodes to read the same resource, but prevents any node from writing to it. An exclusive lock allows only one node to read and write the resource, and prevents any other node from accessing it.
  - The duration of the lock: locks can be either long-lived or short-lived. A long-lived lock is held by a node for the entire duration of a transaction, and is released only when the transaction commits or aborts. A short-lived lock is held by a node only for the time it needs to access the resource, and is released as soon as possible.
  - The security of the lock: locks can be either safe or unsafe. A safe lock guarantees that the resource will not be modified by another node while the lock is held, even if the node holding the lock fails or disconnects. An unsafe lock does not provide such a guarantee, and may allow the resource to be corrupted by another node in case of a failure or a network partition.
- Locks can be implemented in different ways in a distributed system, depending on the architecture and the requirements of the system. Some of the common methods are:
  - Using a centralized lock manager: a single node or a cluster of nodes acts as the authority for granting and releasing locks on the resources. Other nodes have to communicate with the lock manager to request and release locks. This method simplifies the lock management, but introduces a single point of failure and a performance bottleneck.
  - Using a distributed lock manager: each node acts as a lock manager for a subset of the resources, and coordinates with other nodes to grant and release locks on the resources. This method distributes the load and avoids a single point of failure, but increases the complexity and the communication overhead of the lock management.
  - Using a consensus-based lock manager: each node participates in a consensus protocol, such as Paxos or Raft, to agree on the state of the locks on the resources. This method ensures the consistency and the safety of the locks, but requires a majority of the nodes to be online and reachable for the lock management to work.
  - Using a database or a shared resource as a lock manager: a common database or a shared resource, such as Redis or ZooKeeper, is used to store and manipulate the locks on the resources. Other nodes have to access the database or the shared resource to request and release locks. This method leverages the existing features and guarantees of the database or the shared resource, but depends on its availability and scalability for the lock management .



### Optimistic Concurrency Control

- Optimistic concurrency control (OCC) is a concurrency control method applied to transactional systems such as relational database management systems and software transactional memory.
- OCC assumes that multiple transactions can frequently complete without interfering with each other, and does not require locking or timestamping techniques to prevent conflicts .
- Instead, a transaction is executed without restrictions until it is committed, and then it is validated to ensure that no conflicts have occurred with other concurrent transactions.
- If a conflict is detected, the transaction is aborted and restarted, otherwise it is committed.
- OCC has three phases: read, validation and write.
  - In the read phase, the transaction reads the data from the database and performs its operations, without acquiring any locks or checking any timestamps.
  - In the validation phase, the transaction checks if any of the data it has read or written has been modified by another concurrent transaction that has committed earlier.
  - In the write phase, the transaction writes its updates to the database, if the validation phase succeeds, otherwise it aborts and restarts.
- OCC is suitable for distributed systems, where locking or timestamping may incur high communication overhead or introduce delays.
- OCC can improve the performance and scalability of distributed transaction systems, by allowing more concurrency and reducing blocking and waiting .
- However, OCC may also incur high costs of validation and aborting, especially when the conflict rate is high or the transactions are long and complex .
- Therefore, OCC should be used carefully, depending on the characteristics of the workload and the system .

: https://en.wikipedia.org/wiki/Optimistic_concurrency_control
: https://people.cs.rutgers.edu/~pxk/417/notes/concurrency.html
: https://ieeexplore.ieee.org/document/77186/
: https://www.geeksforgeeks.org/concurrency-control-techniques/
: https://www.slideshare.net/mridulmishra2/optimistic-concurrency-control-in-distributed-systems



### Timestamp ordering

- Timestamp ordering is a technique to ensure serializability of transactions in a distributed system.
- A transaction is a sequence of operations that must be executed atomically, i.e., either all or none of them are executed.
- Serializability is the property that the concurrent execution of transactions produces the same result as some sequential execution of them.
- Timestamp ordering assigns a unique timestamp to each transaction when it starts, and uses these timestamps to order the operations of different transactions.
- The timestamp of a transaction reflects its logical start time in the system, and is independent of the physical clocks of the nodes.
- Timestamp ordering can be implemented using logical clocks, such as Lamport timestamps, which are based on the causal relationships between events in the system.
- Lamport timestamps are generated by a simple algorithm that increments a local counter for each event, and updates it with the maximum of the local counter and the received timestamp for each message.
- Timestamp ordering ensures that if a transaction T1 has a smaller timestamp than another transaction T2, then T1 appears to execute before T2 in the final result.
- Timestamp ordering can be applied to different levels of granularity, such as read and write operations, data items, or database pages.
- Timestamp ordering can prevent some types of concurrency anomalies, such as lost updates, dirty reads, and inconsistent reads, by rejecting or delaying conflicting operations based on their timestamps.
- Timestamp ordering can also cause some problems, such as deadlock, starvation, and cascading aborts, which require additional mechanisms to handle them.



### Comparison of methods for concurrency control

Concurrency control is the process of managing the simultaneous execution of transactions in a distributed system, such that the ACID properties are preserved and the system remains consistent and correct. There are various methods for concurrency control, each with its own advantages and disadvantages. Some of the common methods are:

- **Two-phase locking protocol (2PL)**: This method uses locks to grant exclusive access to data items for transactions. A transaction must acquire a lock on a data item before reading or writing it, and release the lock after finishing the operation. There are two phases in this protocol: the growing phase, where a transaction acquires locks and does not release any; and the shrinking phase, where a transaction releases locks and does not acquire any. This protocol ensures serializability, which means that the concurrent execution of transactions is equivalent to some serial execution. However, it may cause deadlock, where two or more transactions are waiting for each other to release locks, and thus cannot proceed. It may also cause starvation, where some transactions are repeatedly blocked by others and never get a chance to execute. Moreover, it does not guarantee strictness, which means that a transaction may read a data item that is written by another uncommitted transaction, leading to inconsistency.

- **Timestamp ordering protocol (TO)**: This method assigns a unique timestamp to each transaction, which reflects its start time. The timestamp is used to order the transactions and determine their precedence. A transaction can read or write a data item only if its timestamp is greater than the timestamp of the last transaction that wrote the data item, and less than the timestamp of the last transaction that read the data item. Otherwise, the transaction is aborted and restarted with a new timestamp. This protocol ensures serializability and strictness, as it prevents transactions from reading or writing uncommitted data. However, it may cause cascading aborts, where one aborted transaction causes other transactions to abort, and thus waste resources. It may also cause starvation, where some transactions are repeatedly aborted and restarted due to conflicts with other transactions.

- **Multi-version concurrency control (MVCC)**: This method maintains multiple versions of each data item, each with a timestamp that indicates when it was created. A transaction can read the latest version of a data item that is older than its timestamp, and write a new version of a data item with its timestamp. This protocol allows concurrent read operations without locking, and thus improves performance and reduces contention. It also ensures serializability and strictness, as it prevents transactions from reading or writing uncommitted data. However, it requires more storage space and overhead to maintain multiple versions of data items. It may also cause write skew, where two transactions read the same data item and update different data items based on it, leading to inconsistency.

- **Validation concurrency control (VCC)**: This method divides the execution of a transaction into three phases: the read phase, where a transaction reads data items and stores them in a private workspace; the validation phase, where a transaction checks for conflicts with other transactions and decides whether to commit or abort; and the write phase, where a transaction writes its updates to the database. This protocol ensures serializability and strictness, as it prevents transactions from reading or writing uncommitted data. However, it may cause cascading aborts, where one aborted transaction causes other transactions to abort, and thus waste resources. It may also cause starvation, where some transactions are repeatedly aborted and restarted due to conflicts with other transactions.



## Unit 9 - Distributed Transactions

- A distributed transaction is a type of transaction that involves two or more network hosts, usually providing transactional resources, such as databases, message queues, file systems, etc.
- A distributed transaction is coordinated by a transaction manager, which is responsible for creating and managing a global transaction that encompasses all the operations against the transactional resources.
- A distributed transaction ensures the ACID properties (atomicity, consistency, isolation, durability) across multiple hosts, meaning that either all the operations succeed or none of them, and the data remains consistent, isolated and durable after the transaction.
- A distributed transaction can be implemented using different protocols, such as two-phase commit, three-phase commit, Paxos commit, etc. These protocols typically involve communication and coordination among the transaction manager, the resource managers and the participants (the hosts that execute the operations).
- A distributed transaction faces various challenges, such as network failures, concurrency issues, deadlock detection, recovery mechanisms, etc. These challenges require careful design and implementation of the distributed transaction system.



### Flat and Nested Distributed Transactions

- A distributed transaction is a transaction that accesses objects managed by multiple servers in a distributed system.
- A distributed transaction must maintain the ACID properties of a transaction, especially the atomicity property, which requires that either all of the servers involved in the transaction commit the transaction or all of them abort the transaction.
- There are two ways to structure a distributed transaction: flat or nested.

#### Flat Transactions

- A flat transaction has a single begin point and a single end point (commit or abort).
- A flat transaction is usually simple and short-lived, and does not involve any subtransactions.
- A flat transaction can use a two-phase commit protocol to coordinate the commit or abort decision among the servers.

#### Nested Transactions

- A nested transaction has a hierarchical structure, where a top-level transaction can have one or more subtransactions, and each subtransaction can have its own subtransactions, and so on.
- A nested transaction can have multiple begin points and multiple end points, corresponding to the different levels of the hierarchy.
- A nested transaction allows more concurrency and fault tolerance, as subtransactions can commit or abort independently, and the top-level transaction can decide whether to commit or abort based on the outcomes of the subtransactions.
- A nested transaction can use a nested two-phase commit protocol or a multilevel commit protocol to coordinate the commit or abort decision among the servers.



### Atomic Commit Protocols for Distributed Transactions

- A distributed transaction is a transaction that involves multiple servers or nodes in a distributed system.
- An atomic commit protocol is a protocol that ensures that a distributed transaction is either committed or rolled back in its entirety, even if the system fails or some of the nodes fail or crash.
- Ensuring atomic commit is important for maintaining the consistency and integrity of the data in a distributed system.
- There are different types of atomic commit protocols, such as two-phase commit, three-phase commit, parallel commit, and failure-aware commit.
- Two-phase commit (2PC) is the most widely used atomic commit protocol. It consists of two phases: a prepare phase and a commit phase. In the prepare phase, a coordinator node asks all the participant nodes to vote on whether they are ready to commit or not. In the commit phase, the coordinator node decides whether to commit or abort the transaction based on the votes, and informs all the participant nodes of the decision.
- Three-phase commit (3PC) is an extension of 2PC that adds a pre-commit phase between the prepare and commit phases. In the pre-commit phase, the coordinator node informs all the participant nodes that they have agreed to commit, and waits for their acknowledgments. In the commit phase, the coordinator node sends the final commit message to all the participant nodes. 3PC can tolerate more failures than 2PC, but it also introduces more latency and message overhead.
- Parallel commit is a new atomic commit protocol that reduces the latency of transactions down to only a single round-trip of distributed consensus. It does not use a coordinator node, but instead relies on each participant node to independently determine whether the transaction can be committed or not, based on the state of the other participant nodes. Parallel commit can achieve high performance and availability, but it requires strong consistency guarantees from the underlying distributed consensus protocol.
- Failure-aware commit (FLAC) is another new atomic commit protocol that aims to improve the performance and availability of distributed transactions in the presence of failures. It uses a hybrid approach that combines 2PC and parallel commit, depending on the failure scenarios. FLAC can dynamically adapt to different failure patterns and optimize the transaction latency and message overhead accordingly.



### Concurrency control in distributed transactions

- Concurrency control is the process of ensuring that multiple transactions can access and modify shared data in a consistent and correct manner, without violating the ACID properties of transactions.
- Distributed transactions are transactions that span multiple data servers that are connected by a network, and may involve data replication, fragmentation, or partitioning .
- Distributed concurrency control provides a mechanism to synchronize distributed transactions in such a way that the ACID properties are not violated by their interleaved execution .
- There are different types of distributed concurrency control algorithms, such as locking-based, timestamp-based, optimistic, and certification-based .
- Locking-based algorithms use locks to prevent concurrent transactions from accessing or modifying the same data item. Locks can be exclusive or shared, and can be granted or denied by a central or distributed lock manager .
- Timestamp-based algorithms assign a unique timestamp to each transaction, and use the timestamp order to determine the precedence and validity of transactions. Transactions with smaller timestamps have higher priority, and transactions with larger timestamps may be aborted or restarted if they conflict with earlier transactions .
- Optimistic algorithms assume that conflicts are rare, and allow transactions to execute without any synchronization until the commit phase. At the commit phase, transactions are validated by checking if they have read or written any data item that was concurrently modified by another transaction. If validation fails, transactions are aborted or restarted .
- Certification-based algorithms are a variant of optimistic algorithms, where transactions are validated by a set of certifiers, which are data servers that store the data items accessed by the transactions. Certifiers use a certification table to keep track of the latest committed transactions that have modified each data item, and compare the timestamps of the transactions to certify with the certification table. If certification succeeds, transactions are committed; otherwise, they are aborted or restarted .
- Distributed concurrency control algorithms face various challenges, such as network delays, communication failures, data inconsistencies, deadlock detection, and distributed commit .
- Network delays and communication failures can affect the performance and correctness of distributed transactions, as they may cause transactions to wait for messages or locks that never arrive, or to miss messages or locks that are essential for their execution .
- Data inconsistencies can arise due to data replication, fragmentation, or partitioning, as different data servers may have different versions or copies of the same data item. Data inconsistencies can lead to incorrect or conflicting results of distributed transactions, and require mechanisms to ensure data consistency, such as quorum protocols, primary copy protocols, or update propagation protocols .
- Deadlock detection is the problem of identifying and resolving situations where two or more transactions are waiting for each other to release locks or resources that they hold. Deadlock detection can be centralized or distributed, and can use techniques such as timeout, wait-for graphs, or probe messages .
- Distributed commit is the problem of ensuring that all data servers involved in a distributed transaction agree on the final outcome of the transaction, either commit or abort. Distributed commit can use protocols such as two-phase commit (2PC), three-phase commit (3PC), or Paxos .



### Distributed Deadlocks

- A distributed deadlock is a situation where a set of processes in a distributed system are waiting for each other to release resources or messages, and none of them can proceed .
- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems .
- Distributed deadlocks are harder to detect, avoid, and prevent than deadlocks in centralized systems, because there is no single authority that can oversee resource allocation and dependency graphs.
- There are three main approaches to handle distributed deadlocks :
  - Prevention: This approach tries to ensure that at least one of the necessary conditions for deadlock (mutual exclusion, hold and wait, no preemption, circular wait) is never satisfied. For example, by using timeouts, ordering resources, or aborting transactions.
  - Avoidance: This approach tries to ensure that the system will always remain in a safe state, where there is at least one possible sequence of resource allocation that will not lead to deadlock. For example, by using the banker's algorithm or timestamps.
  - Detection: This approach tries to identify the existence of deadlocks after they occur, and then resolve them by breaking the circular wait. For example, by constructing a global wait-for graph or using edge chasing algorithms.
- The techniques of deadlock detection in distributed systems require the following properties:
  - Progress: The method should be able to detect all the deadlocks in the system.
  - Safety: The method should not detect false or phantom deadlocks.
- There are two main types of distributed deadlocks:
  - Communication deadlocks: These occur when processes are waiting for messages from each other, and no message can be delivered. For example, by using synchronous message passing or circular buffer queues.
  - Resource deadlocks: These occur when processes are waiting for resources held by other processes, and no resource can be released. For example, by using distributed mutual exclusion or distributed locking.



### Transaction recovery for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

- Transaction recovery is the process of restoring the consistency and integrity of a distributed database after a failure or an abort of a transaction .
- A failure in a distributed system can be caused by various reasons, such as network partition, site crash, communication link failure, disk failure, or software error.
- A transaction in a distributed system may involve multiple sites, each executing a subtransaction on a local database. If any of the subtransactions fails or aborts, the whole transaction must be rolled back to ensure atomicity.
- Transaction recovery in a distributed system involves two main tasks: failure detection and failure handling.
  - Failure detection is the process of identifying the sites or subtransactions that have failed or aborted, and notifying the other sites or subtransactions involved in the same transaction.
  - Failure handling is the process of taking appropriate actions to recover from the failure, such as aborting, committing, or restarting the subtransactions, depending on the state of the transaction and the type of the failure.
- There are different techniques for transaction recovery in a distributed system, such as logging, shadow versions, two-phase commit protocol, three-phase commit protocol, and presumed abort/commit protocols   .
  - Logging is a technique that records the changes made by a subtransaction in a log file, which can be used to undo or redo the changes in case of a failure .
  - Shadow versions is a technique that creates a copy of the data before modifying it, and updates a pointer to the latest version after committing the subtransaction. If a subtransaction aborts, the pointer is restored to the previous version.
  - Two-phase commit protocol is a protocol that coordinates the commit or abort decision of a transaction among all the sites involved, using a coordinator site and two phases: prepare and commit  .
  - Three-phase commit protocol is a protocol that extends the two-phase commit protocol by adding a pre-commit phase, which reduces the possibility of blocking in case of a failure .
  - Presumed abort/commit protocols are protocols that optimize the two-phase commit protocol by reducing the amount of logging or communication required, based on the assumption that most transactions abort or commit .



## Unit 10 - Replication

- Replication is the process of copying data from one database server to another, either synchronously or asynchronously.
- Replication can be used for various purposes, such as:
  - High availability: Replication can provide redundancy and fault tolerance by maintaining multiple copies of data on different servers.
  - Load balancing: Replication can distribute the workload among multiple servers, reducing the load on a single server and improving performance.
  - Data distribution: Replication can enable data access across different locations, regions, or networks, facilitating data sharing and collaboration.
  - Backup and recovery: Replication can provide a backup copy of data that can be used for recovery in case of data loss or corruption.
- Replication can be classified into different types, based on the following criteria:
  - The number of servers involved: Replication can be either one-to-one, one-to-many, many-to-one, or many-to-many.
  - The direction of data flow: Replication can be either unidirectional, bidirectional, or multidirectional.
  - The timing of data transfer: Replication can be either synchronous, asynchronous, or semi-synchronous.
  - The granularity of data transfer: Replication can be either snapshot, transactional, or merge.
- Replication can also be categorized into different models, based on the role and responsibility of each server involved:
  - Master-slave replication: In this model, one server (the master) is the primary source of data, and the other servers (the slaves) are the secondary copies of data. The master is responsible for accepting write operations, and the slaves are responsible for accepting read operations. The master propagates the changes to the slaves, either synchronously or asynchronously. The master-slave replication can be either one-to-many or many-to-one.
  - Peer-to-peer replication: In this model, all servers are equal and can accept both read and write operations. The servers propagate the changes to each other, either synchronously or asynchronously. The peer-to-peer replication can be either bidirectional or multidirectional.
  - Multi-master replication: In this model, multiple servers (the masters) can accept write operations, and the other servers (the slaves) can accept read operations. The masters propagate the changes to the slaves, either synchronously or asynchronously. The multi-master replication can be either one-to-many or many-to-many.



### System model and group communication for replication in distributed systems

- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by passing messages .
- Replication is a technique to improve the availability, performance, and fault tolerance of a distributed system by creating and maintaining multiple copies of data or services .
- A system model is an abstraction that defines the properties and assumptions of a distributed system, such as the communication model, the failure model, the timing model, and the security model .
- A group is a set of processes that share some common state or interest and need to communicate and cooperate with each other .
- Group communication is a mechanism that allows a process to send a message to a group of processes, either reliably or unreliably, either ordered or unordered, either atomically or non-atomically .
- Group communication can be implemented using different methods, such as multicast, broadcast, or gossip  .
- Group communication can be used for replication in distributed systems, for example, to disseminate updates to replicated data or services, to coordinate the actions of replicated processes, or to detect and recover from failures of replicated components  .
- Group communication can also pose challenges for replication in distributed systems, such as ensuring consistency, concurrency control, fault tolerance, and scalability  .



Hello, I am Sydney, your AI assistant. I can help you with your topic of fault-tolerant services for the notes of the unit 10 - replication in the subject of distributed system. Here is a summary of the main points:

- Fault-tolerant services are services that can continue to function correctly even in the presence of failures, such as server crashes, network partitions, or malicious attacks.
- Replication is a technique for implementing fault-tolerant services by creating multiple copies of the same service (or state machine) and coordinating the interactions of clients with these copies.
- Replication can improve the availability, performance, and reliability of the service, but also introduces challenges such as consistency, concurrency, and communication overhead.
- There are two main classes of replication techniques: primary-backup replication and active replication.
- Primary-backup replication assigns one copy of the service as the primary and the others as backups. The primary receives all the client requests and executes them, while sending updates to the backups. The backups apply the updates in the same order as the primary and are ready to take over if the primary fails.
- Active replication assigns equal roles to all the copies of the service. All the copies receive the same client requests and execute them independently, using a consensus protocol to ensure agreement on the order of execution. Active replication can tolerate more failures than primary-backup replication, but also requires more communication and computation.
- Replication can be combined with coding theory to reduce the number of copies needed to achieve fault-tolerance, while maintaining low overhead during normal operations. Coding theory can also help recover from failures more efficiently by using erasure codes or network coding.



### Highly Available Services

- A highly available service is a service that can provide continuous and reliable operation even in the presence of failures or faults in the system.
- Replication is a technique for achieving high availability by creating and maintaining multiple copies of the same data or service on different nodes in a distributed system .
- Replication can improve the availability, performance, scalability, and fault tolerance of a service .
- Replication can be classified into two types: eager replication and lazy replication .
  - Eager replication ensures that all replicas are updated as soon as a change occurs, thus providing strong consistency and fault tolerance, but at the cost of higher communication and synchronization overhead .
  - Lazy replication allows some replicas to be updated later than others, thus providing higher availability and performance, but at the cost of weaker consistency and possible conflicts .
- Replication can also be classified into two modes: active replication and passive replication .
  - Active replication executes the same request on all replicas in parallel, thus providing high availability and fault masking, but at the cost of higher resource consumption and possible non-determinism .
  - Passive replication executes the request on a primary replica and propagates the result to the backup replicas, thus providing lower resource consumption and deterministic behavior, but at the cost of lower availability and fault detection .
- Replication can be implemented at different levels of abstraction, such as data replication, process replication, or service replication.
  - Data replication focuses on replicating the state of the data objects, such as files, databases, or memory pages .
  - Process replication focuses on replicating the behavior of the application processes, such as servers, clients, or threads .
  - Service replication focuses on replicating the functionality of the service, such as web services, message queues, or distributed transactions .



### Transactions with replicated data

- Transactions are a sequence of operations that are executed atomically, consistently, isolated, and durably (ACID properties) on a database system.
- Replication is a technique to distribute data across multiple servers or locations, so that users can access data relevant to their activities without interfering with the work of others.
- Transactions with replicated data are transactions that involve data items that have multiple copies on different servers or locations.
- The main challenges of transactions with replicated data are:
  - How to ensure atomicity and consistency of transactions across multiple servers or locations, especially in the presence of failures or network partitions.
  - How to ensure isolation and concurrency control of transactions that access or update the same data items on different servers or locations.
  - How to balance the trade-offs between availability, performance, and consistency of replicated data.
- The main approaches to transactions with replicated data are:
  - Primary-copy approach: One copy of each data item is designated as the primary copy, and all transactions must access or update the primary copy. The primary copy is responsible for propagating the updates to the other copies (replicas). This approach ensures strong consistency and serializability of transactions, but it may suffer from low availability and performance if the primary copy fails or is unreachable .
  - Replicated-commit approach: All copies of each data item are treated equally, and transactions can access or update any copy. A distributed commit protocol, such as two-phase commit, is used to ensure atomicity and consistency of transactions across all copies. This approach improves availability and performance, but it may incur high communication and coordination overhead, and it may block or abort transactions in case of failures or network partitions .
  - Quorum-based approach: A subset of copies of each data item, called a quorum, is required to participate in a transaction. A read quorum is the minimum number of copies that must be read to ensure a consistent read, and a write quorum is the minimum number of copies that must be updated to ensure a consistent write. The quorum sizes are determined by the replication factor (the number of copies of each data item) and the desired consistency level. This approach allows for flexible trade-offs between availability, performance, and consistency, but it may require complex quorum management and conflict resolution .

