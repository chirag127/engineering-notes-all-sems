

# Distributed System

A distributed system is a system whose components are located on different networked computers, which communicate and coordinate their actions by passing messages to one another. A distributed system can also be defined as a number of independent computers linked by a network, or a computing environment in which various components are spread across multiple computers (or other computing devices) on a network.

Some of the main characteristics of a distributed system are:

- The components are autonomous, meaning they can operate independently and have their own failure modes.
- The components are heterogeneous, meaning they can have different hardware, software, operating systems, and protocols.
- The components are scalable, meaning the system can handle increasing workload or number of components without significant degradation of performance or reliability.
- The components are transparent, meaning the system hides the complexity and distribution of the components from the users and applications.

Some of the main challenges of a distributed system are:

- The components are prone to failures, such as crashes, network partitions, or malicious attacks, and the system must be able to tolerate and recover from them.
- The components are subject to concurrency, meaning they can execute simultaneously and access shared resources, and the system must ensure consistency and correctness of the data and operations.
- The components are subject to latency, meaning there is a delay in the communication and coordination of the components, and the system must optimize the performance and availability of the system.
- The components are subject to security, meaning they can be vulnerable to unauthorized access or modification of the data and operations, and the system must protect the confidentiality, integrity, and authenticity of the system.

Some of the main benefits of a distributed system are:

- The components are modular, meaning they can be reused, replaced, or added without affecting the rest of the system.
- The components are flexible, meaning they can adapt to changing requirements, environments, or technologies.
- The components are efficient, meaning they can utilize the resources of multiple computers and achieve higher throughput, lower cost, or better quality of service.
- The components are resilient, meaning they can cope with failures, errors, or faults and maintain the functionality and availability of the system.



## Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- The main characteristics of distributed systems are:
  - Concurrency: Multiple components can execute simultaneously and interact with each other.
  - No global clock: There is no shared physical clock among the components, so synchronization and coordination are challenging.
  - Independent failures: Each component can fail independently, without affecting the whole system. Fault tolerance and recovery are essential.
  - Heterogeneity: The components can have different hardware, software, network, and data formats. Interoperability and compatibility are required.
- The main advantages of distributed systems are:
  - Scalability: The system can grow in size and performance by adding more components, without affecting the existing ones.
  - Availability: The system can tolerate failures of some components, and still provide the service to the users.
  - Transparency: The system can hide the complexity and diversity of the components, and present a uniform and consistent interface to the users.
- The main challenges of distributed systems are:
  - Communication: The components need to exchange messages over unreliable and insecure networks, with variable delays and bandwidths.
  - Coordination: The components need to agree on common goals, actions, and states, despite the lack of global clock and the possibility of failures.
  - Consistency: The system needs to maintain a coherent and correct view of the data and the state, despite the concurrent and distributed updates.
  - Security: The system needs to protect the data and the resources from unauthorized access, modification, or disclosure.



### Introduction for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- A distributed system has the following characteristics:
  - Concurrency: The components of the system can execute concurrently, without interfering with each other.
  - No global clock: The components of the system do not share a common notion of time, and may have different local clocks.
  - Independent failures: The components of the system can fail independently, without affecting the whole system.
  - Heterogeneity: The components of the system can have different hardware, software, network, and data formats.
- A distributed system has the following challenges:
  - Transparency: The system should hide the complexity and diversity of the components from the users, and provide a uniform interface and behavior.
  - Scalability: The system should be able to accommodate an increasing number of components, users, and resources, without degrading the performance or functionality.
  - Reliability: The system should be able to tolerate and recover from failures of the components, and ensure the consistency and availability of the data and services.
  - Security: The system should be able to protect the data and services from unauthorized access, modification, or disclosure.
- A distributed system has the following advantages:
  - Resource sharing: The system can enable the sharing of hardware, software, data, and services among the components and users.
  - Fault tolerance: The system can increase the availability and reliability of the data and services by replicating and distributing them among the components.
  - Performance: The system can improve the efficiency and throughput of the data and services by parallelizing and distributing the computation and communication among the components.
  - Modularity: The system can facilitate the development and maintenance of the data and services by decomposing them into modular and reusable components.



### Examples of Distributed Systems

A distributed system is a collection of independent computers that communicate and coordinate their actions by passing messages. The computers in a distributed system may be physically close or geographically dispersed, and they may be connected by a network or a bus. Distributed systems can provide higher performance, reliability, scalability, and availability than centralized systems.

Some examples of distributed systems are:

- **Telecommunication networks**: Telephone networks are an early example of a peer-to-peer network, where each node can initiate or receive calls. Cellular and telephone networks are forms and examples of distributed networks. They use protocols such as TCP/IP, UDP, and SIP to exchange data and signals. Telecommunication networks also include the Internet, which is a global network of networks that connects millions of computers and devices. The Internet uses protocols such as HTTP, FTP, SMTP, and DNS to provide various services and applications.

- **Real-time systems**: Many industries use real-time systems distributed in various areas, locally and globally. Real-time systems are systems that have strict timing constraints and must respond to events within a specified deadline. For example, air traffic control systems, industrial control systems, and online gaming systems are real-time systems that use distributed components to monitor, control, and coordinate their activities.

- **Distributed database systems**: A distributed database is a database that has locations across multiple servers, physical locations, or both. A distributed database can improve performance, availability, and scalability by allowing concurrent access and updates from multiple sites. A distributed database can also provide fault tolerance and data replication. Examples of distributed database systems are Oracle, MySQL, MongoDB, and Cassandra.

- **Distributed computing systems**: A distributed computing system is a system that uses multiple computers to perform a computation or a task that is too large or complex for a single computer. A distributed computing system can exploit the parallelism and heterogeneity of the computers to achieve higher efficiency and speed. Examples of distributed computing systems are grid computing, cloud computing, and peer-to-peer computing. Grid computing is a form of distributed computing that uses a network of computers to share resources and solve large-scale problems. Cloud computing is a form of distributed computing that provides on-demand access to computing resources and services over the Internet. Peer-to-peer computing is a form of distributed computing that uses a network of equal nodes to share data and resources without a central server.



### Resource sharing and the web challenges in distributed systems

- Resource sharing is the process of making the resources of a distributed system available to the users and applications in a transparent and efficient way .
- Resources can be hardware (such as CPU, memory, disk, printer), software (such as files, databases, web pages, services), or data (such as documents, images, videos).
- Resource sharing can be achieved by different methods, such as data migration, computation migration, task migration, and service migration.
- Data migration is the process of transferring data from one location to another location in the system.
- Computation migration is the process of transferring a computation (such as a process or a thread) from one node to another node in the system.
- Task migration is the process of transferring a task (such as a job or a request) from one node to another node in the system.
- Service migration is the process of transferring a service (such as a web server or a database server) from one node to another node in the system.
- The web is an example of a distributed system that enables resource sharing among millions of users and applications   .
- The web challenges in distributed systems are the issues and problems that arise from the design, implementation, and operation of the web as a large-scale, open, heterogeneous, and dynamic distributed system  .
- Some of the major web challenges in distributed systems are  :
  - Scalability: the ability of the system to handle increasing load and demand without degrading the performance or quality of service  .
  - Heterogeneity: the diversity and compatibility of the hardware, software, data, and protocols involved in the system   .
  - Fault tolerance: the ability of the system to cope with failures and errors of the components and the network  .
  - Security: the protection of the system from unauthorized access, modification, or damage of the resources and the data  .
  - Consistency: the maintenance of the correctness and coherence of the data and the state of the system  .
  - Transparency: the hiding of the complexity and diversity of the system from the users and the applications  .



### Architectural models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Architectural models are system models that describe the organization of components across the network and their interrelationship.
- Architectural models can help to understand the design trade-offs, performance issues, and scalability challenges of distributed systems.
- Some common architectural models for distributed systems are:

  - **Client-server architecture**: This model consists of two types of components: clients and servers. Clients request services from servers, and servers provide services to clients. Clients and servers can be located on different machines and communicate over the network. This model is widely used for web applications, email systems, database systems, etc.
  - **Broker architecture**: This model introduces an intermediate component called a broker, which acts as a mediator between clients and servers. The broker is responsible for locating servers, forwarding requests, and returning responses. The broker can also provide additional services such as caching, load balancing, security, etc. This model is used by some middleware platforms such as CORBA, Java RMI, etc.
  - **Service-oriented architecture (SOA)**: This model views the distributed system as a collection of loosely coupled and interoperable services. Services are self-contained units of functionality that can be discovered, invoked, and composed by other services or clients. Services communicate using standard protocols and formats such as SOAP, REST, XML, JSON, etc. This model is used by many web services, cloud computing, and microservices applications.
  - **Peer-to-peer architecture**: This model eliminates the distinction between clients and servers and allows every component to act as both a service provider and a service consumer. Components can join and leave the network dynamically and share resources among themselves. This model is used by some file-sharing, content distribution, and collaborative applications such as BitTorrent, Skype, etc.
  - **Layered architecture**: This model organizes the components of the distributed system into a hierarchy of layers. Each layer communicates with its adjacent layer by sending requests and getting responses. Each layer provides a level of abstraction and hides the details of the lower layers. This model is used by some network protocols, operating systems, and software architectures such as TCP/IP, OSI, MVC, etc.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of fundamental models for distributed systems:

### Fundamental Models for Distributed Systems

- Fundamental models are descriptions of properties that are present in all distributed architectures, such as concurrency, scalability, transparency, and heterogeneity  .
- Fundamental models can be classified into three categories: interaction models, failure models, and security models  .
- Interaction models deal with the issues of communication and coordination among processes in a distributed system, such as performance, timing, ordering, and synchronization of events  .
- Failure models specify the types of faults that can occur in processes and communication channels in a distributed system, such as crash, omission, timing, response, and Byzantine faults  .
- Security models define the threats and countermeasures for protecting the confidentiality, integrity, and availability of data and resources in a distributed system, such as encryption, authentication, authorization, and auditing  .

Some points to remember about fundamental models are:

- Fundamental models help to abstract the complexity and diversity of distributed systems and provide a common framework for designing, analyzing, and evaluating them  .
- Fundamental models are not mutually exclusive, but rather interrelated and complementary. For example, interaction models depend on failure models to handle communication errors, and security models depend on interaction models to establish secure channels  .
- Fundamental models are not fixed or universal, but rather evolving and adaptable. They can be refined, extended, or modified to suit different application domains, system requirements, and environmental conditions  .




### Theoretical Foundation for Distributed System

- A distributed system is a collection of processes that are spatially separated and do not share a common memory and communicate with one another by exchanging messages with arbitrary delays .
- Theoretical foundation for distributed system aims to understand the inherent limitations, capabilities, and trade-offs of a distributed system and to develop mathematical models and algorithms for solving problems in a distributed environment  .
- Some of the topics covered by the theoretical foundation for distributed system are:
  - Limitation of distributed system: such as the impossibility of consensus, the lower bounds on communication and computation, the effects of failures and asynchrony, the complexity of coordination and synchronization, etc  .
  - Absence of global clock: the lack of a common notion of time among the processes in a distributed system and the challenges of ordering events and ensuring consistency and causality  .
  - Shared memory: the abstraction of a global memory that can be accessed by all processes in a distributed system and the issues of concurrency control, replication, consistency models, and fault tolerance  .
  - Logical clocks: the mechanisms for assigning logical timestamps to events in a distributed system and for comparing the order of events based on their timestamps, such as Lamport's logical clocks and vector clocks    .
  - Concepts in message passing system: the principles and techniques for designing and implementing distributed algorithms that use message passing as the communication paradigm, such as leader election, mutual exclusion, distributed snapshots, termination detection, etc   .



### Limitation of Distributed system

A distributed system is a system that consists of multiple independent components that communicate with each other over a network. Distributed systems have many advantages, such as scalability, fault-tolerance, availability, and performance. However, they also face some limitations that make them challenging to design and implement. Some of the main limitations of distributed systems are:

- **Absence of a global state**: In a distributed system, there is no single entity that has a complete and consistent view of the system's state. Each component has only a partial and possibly outdated information about the system. This makes it difficult to coordinate and synchronize the actions of different components, and to ensure the consistency and correctness of the system's behavior. For example, in a distributed database, there is no guarantee that all the replicas of the same data are identical at any given time, and there may be conflicts or inconsistencies when updating or querying the data. To overcome this limitation, distributed systems need to use various techniques, such as consensus algorithms, distributed transactions, replication protocols, and consistency models, to achieve a desired level of consistency and coordination among the components.

- **Absence of a global clock**: In a distributed system, there is no common physical clock that can be used to measure the time and order of events. Each component has its own local clock, which may not be synchronized with the clocks of other components, and which may drift or skew over time. This makes it hard to determine the causal and temporal relationships between events that occur in different components, and to implement time-dependent functionalities, such as timeouts, deadlines, scheduling, and synchronization. For example, in a distributed system, it may not be possible to tell which of two messages arrived first, or which of two operations happened before the other. To overcome this limitation, distributed systems need to use various techniques, such as logical clocks, vector clocks, timestamps, and lamport clocks, to establish a partial or total order of events and to reason about the causality and concurrency of the system.

- **Network issues**: In a distributed system, the communication between the components depends on the underlying network, which may be unreliable, unpredictable, or insecure. The network may experience failures, delays, losses, duplications, or reordering of messages, which may affect the correctness and performance of the system. For example, in a distributed system, it may not be possible to tell whether a component has crashed or is just slow, or whether a message has been lost or delayed. To overcome this limitation, distributed systems need to use various techniques, such as fault-tolerance, reliability, timeout, retransmission, acknowledgement, encryption, and authentication, to cope with the network issues and to ensure the availability and security of the system.



### Absence of Global Clock

- A global clock is a system-wide clock that is equally accessible to all processes in a distributed system and provides a common notion of time.
- A global clock is useful for determining the order of events, synchronizing processes, and obtaining consistent states of the system.
- However, a global clock is hard to realize in distributed systems due to two inherent limitations: lack of shared memory and unpredictable message delays.
- Lack of shared memory means that processes in a distributed system do not have access to a common storage that can store and update the global clock value.
- Unpredictable message delays mean that the communication channel between processes is unreliable and the transmission time of messages is variable and unknown.
- Therefore, processes in a distributed system may have different and inaccurate views of the global clock value, and the notion of common time does not exist.
- As a result, it is not always possible to determine the order of events, synchronize processes, and obtain consistent states of the system in a distributed system without a global clock.
- To overcome the absence of a global clock, distributed systems use various techniques such as logical clocks, vector clocks, causal ordering, snapshot algorithms, etc. to achieve some form of partial or approximate global time and state.



### Shared Memory

- Shared memory is a programming model that allows multiple processes to access and modify the same data in a shared address space.
- Shared memory can be implemented in two ways: physically shared memory and distributed shared memory.
- Physically shared memory is when multiple processors or cores share the same physical memory, such as in a multiprocessor system or a multicore system.
- Distributed shared memory (DSM) is when multiple nodes or computers in a distributed system share a virtual address space, but do not have physical access to the same memory, such as in a cluster or a grid.
- DSM systems can provide the illusion of a shared memory model on a distributed system that has no physically shared memory, by using software or hardware mechanisms to manage the data movement and consistency across the nodes.
- DSM systems can have different architectures, such as page-based, object-based, or tuple-based, depending on how the shared data is organized and accessed.
- DSM systems can have different consistency models, such as sequential, causal, or eventual, depending on how the updates to the shared data are propagated and ordered among the nodes.
- DSM systems can have different advantages, such as:
  - Transparency: DSM systems can hide the details of data distribution and communication from the programmer, making the programming model simpler and more portable.
  - Scalability: DSM systems can scale up to a large number of nodes and support dynamic addition and removal of nodes, without affecting the performance or correctness of the shared memory model.
  - Fault-tolerance: DSM systems can tolerate node failures and network partitions, by using replication, caching, or checkpointing techniques to ensure the availability and consistency of the shared data.



### Logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A logical clock is a mechanism for capturing chronological and causal relationships in a distributed system  .
- A distributed system may have no physically synchronous global clock, so a logical clock allows global ordering on events from different processes in such systems .
- A logical clock is not a physical device, but a software counter that is incremented according to some rules .
- A logical clock can be used for computation analysis, distributed algorithm design, individual event tracking, and exploring computational progress.
- Some examples of logical clock algorithms are:
  - Lamport timestamps, which are monotonically increasing software counters that are updated based on the send and receive events of messages .
  - Vector clocks, which are arrays of software counters that are updated based on the send, receive, and local events of processes .
  - Matrix clocks, which are matrices of software counters that are updated based on the send, receive, and local events of processes and also capture the concurrency of events.
- A logical clock must satisfy the following property: if event A causally precedes event B, then the logical clock value of A is less than the logical clock value of B .
- A logical clock may not reflect the real-time order of events, as it depends on the communication delays and the clock synchronization errors in the distributed system .
- A logical clock can be used to implement distributed synchronization primitives, such as mutual exclusion, deadlock detection, and snapshot algorithms .



### Lamport's logical clocks

- Lamport's logical clocks are a way of ordering events in a distributed system based on their causal relationships, rather than their physical timestamps.
- Lamport's logical clocks are also known as **logical timestamps** or **logical counters**.
- Lamport's logical clocks are based on the idea of a **happens-before** relation, denoted by `->`, which captures the notion of causality between events.
- If `a` and `b` are events on the same process, then `a -> b` if `a` occurs before `b` based on the local clock.
- If `a` is the event of sending a message by one process and `b` is the event of receiving that message by another process, then `a -> b`.
- The happens-before relation is **transitive**, meaning that if `a -> b` and `b -> c`, then `a -> c`.
- The happens-before relation is **irreflexive**, meaning that no event happens before itself.
- The happens-before relation is **antisymmetric**, meaning that if `a -> b`, then `b` does not happen before `a`.
- Lamport's logical clocks assign a **logical clock value** to each event, denoted by `C(e)`, which is a non-negative integer that increases monotonically with each event.
- Lamport's logical clocks follow two rules:
  - Rule 1: Each process increments its logical clock value by one before each event it executes.
  - Rule 2: When a process sends a message, it includes its current logical clock value in the message. When a process receives a message, it sets its logical clock value to the maximum of its own value and the value received in the message, and then increments it by one.
- Lamport's logical clocks ensure that if `a -> b`, then `C(a) < C(b)`. However, the converse is not true, meaning that if `C(a) < C(b)`, it does not imply that `a -> b`.
- Lamport's logical clocks are useful for determining a **partial order** of events in a distributed system, but they cannot distinguish between **concurrent** events, which are events that are not causally related.



### Concepts in Message Passing Systems for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Message passing is a technique for invoking behavior on a computer by sending messages from one process to another.
- Message passing systems are subsystems of distributed operating systems that provide a set of message-based interprocess communication (IPC) protocols.
- Message passing systems can be classified into two types: synchronous and asynchronous.
  - Synchronous message passing systems require the sender and the receiver to be ready at the same time for communication. The sender blocks until the receiver acknowledges the message, and the receiver blocks until a message arrives.
  - Asynchronous message passing systems do not require the sender and the receiver to be ready at the same time for communication. The sender does not block after sending a message, and the receiver does not block if no message is available. Instead, messages are stored in buffers or queues until they are delivered or retrieved.
- Message passing systems can also be classified into two types: direct and indirect.
  - Direct message passing systems require the sender and the receiver to know each other's identities or addresses. The sender specifies the destination of the message, and the receiver specifies the source of the message.
  - Indirect message passing systems do not require the sender and the receiver to know each other's identities or addresses. The sender and the receiver communicate through a shared entity, such as a mailbox, a port, a topic, or a channel. The sender specifies the name of the shared entity, and the receiver retrieves messages from the shared entity.
- Message passing systems can have different features, such as reliability, ordering, multicasting, and security.
  - Reliability refers to the ability of the message passing system to ensure that messages are delivered correctly and completely, without loss, duplication, or corruption.
  - Ordering refers to the ability of the message passing system to preserve the temporal or causal relationships among messages, such as FIFO, causal, or total ordering.
  - Multicasting refers to the ability of the message passing system to deliver a message to multiple receivers at once, such as broadcast, multicast, or anycast.
  - Security refers to the ability of the message passing system to protect the messages from unauthorized access, modification, or disclosure, such as encryption, authentication, or access control.
- Message passing systems can face different challenges, such as network heterogeneity, network failures, network congestion, and network latency.
  - Network heterogeneity refers to the diversity of the network architectures, protocols, and platforms that the message passing system has to support and interoperate with.
  - Network failures refer to the possibility of the network components, such as links, routers, or hosts, to malfunction or become unavailable, causing message loss, delay, or corruption.
  - Network congestion refers to the situation where the network traffic exceeds the network capacity, causing message queuing, retransmission, or dropping.
  - Network latency refers to the time it takes for a message to travel from the sender to the receiver, which can affect the performance and correctness of the message passing system.



### Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- Causal order is a way of ordering events in a distributed system based on their causal relationships, rather than their physical timestamps or locations.
- Causal order captures the notion of "happened before" or "influenced by" among events, regardless of when or where they occurred.
- Causal order is important for ensuring consistency, correctness, and coordination in distributed systems, especially when dealing with concurrent or asynchronous events.
- Causal order can be defined formally using Lamport's logical clocks, which assign logical timestamps to events based on their causal dependencies.
- Causal order can be implemented using various algorithms, such as vector clocks, causal broadcast, or causal delivery, which ensure that messages are delivered or processed in a way that respects their causal order.
- Causal order can be relaxed or strengthened depending on the application requirements and trade-offs. For example, total-causal order is a stricter version of causal order that imposes a single linearization of all events, while fuzzy causal order is a weaker version that allows some degree of uncertainty or ambiguity in the ordering of events.



### Total Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent entities that communicate by message passing and coordinate their actions to achieve a common goal.
- Events are occurrences that happen at a specific point in time and space in a distributed system.
- A partial order is a binary relation that is reflexive, antisymmetric, and transitive, meaning that for any events A, B, and C in a distributed system, the following hold:
  - A ≤ A (reflexivity)
  - If A ≤ B and B ≤ A, then A = B (antisymmetry)
  - If A ≤ B and B ≤ C, then A ≤ C (transitivity)
- A total order is a partial order that is also complete, meaning that for any events A and B in a distributed system, either A ≤ B or B ≤ A .
- A total order can be used to establish a causal relationship among all events in a distributed system, which is useful for ensuring consistency, synchronization, and fault tolerance .
- A total order can be implemented by using logical clocks, such as Lamport timestamps or vector clocks, that assign a unique and monotonically increasing value to each event in a distributed system .
- A logical clock is a mechanism that assigns a logical time to each event in a distributed system, such that if event A happens before event B, then the logical time of A is less than the logical time of B .
- Lamport timestamps are a type of logical clock that assign a logical time to each event in a distributed system based on the following rules :
  - Each entity in the system maintains a counter that is initialized to zero.
  - Each time an entity performs an internal event, it increments its counter by one.
  - Each time an entity sends a message, it increments its counter by one and attaches its counter value to the message.
  - Each time an entity receives a message, it updates its counter to the maximum of its own counter and the counter value in the message, and then increments it by one.
- Lamport timestamps can be used to create a total order of events in a distributed system by using some arbitrary mechanism to break ties (e.g. the ID of the process).
- Vector clocks are a type of logical clock that assign a logical time to each event in a distributed system based on the following rules:
  - Each entity in the system maintains a vector of counters, one for each entity in the system, that is initialized to zero.
  - Each time an entity performs an internal event, it increments its own counter in the vector by one.
  - Each time an entity sends a message, it increments its own counter in the vector by one and attaches its vector to the message.
  - Each time an entity receives a message, it updates each counter in its vector to the maximum of its own counter and the counter in the message vector.
- Vector clocks can be used to create a partial order of events in a distributed system by using the following relation:
  - A vector clock V1 is less than or equal to another vector clock V2 if and only if for every counter i in the vectors, V1[i] ≤ V2[i].
  - A vector clock V1 is equal to another vector clock V2 if and only if for every counter i in the vectors, V1[i] = V2[i].
  - A vector clock V1 is concurrent with another vector clock V2 if and only if neither V1 ≤ V2 nor V2 ≤ V1.
- Vector clocks can be used to create a total order of events in a distributed system by using some arbitrary mechanism to break ties (e.g. the lexicographic order of the vectors).



### Total Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems in the Subject of Distributed System

- A distributed system is a collection of independent and autonomous processes that communicate and coordinate with each other by exchanging messages.
- Events are the actions or occurrences that happen in a distributed system, such as sending or receiving a message, executing a local operation, or detecting a failure.
- The order of events is important for understanding the behavior and correctness of a distributed system, especially in the presence of concurrency and failures.
- A partial order is a binary relation that satisfies three properties: reflexivity, antisymmetry, and transitivity. A partial order can be represented by a directed acyclic graph (DAG), where the nodes are the events and the edges are the order relation.
- A causal order is a partial order that captures the notion of potential causality between events. An event e1 is causally related to another event e2, denoted by e1 -> e2, if one of the following conditions holds:
  - e1 and e2 are events in the same process, and e1 happened before e2.
  - e1 is the sending of a message m, and e2 is the receipt of the same message m.
  - There exists an event e3 such that e1 -> e3 and e3 -> e2.
- A total order is a partial order that satisfies an additional property: comparability. This means that for any two events e1 and e2, either e1 -> e2, or e2 -> e1, or both (if e1 and e2 are the same event). A total order can be represented by a linear sequence of events, where the order relation is the same as the sequence order.
- A total causal order is a total order that is consistent with the causal order. This means that if e1 -> e2 in the causal order, then e1 -> e2 in the total order as well. A total causal order can be obtained by extending the causal order with a tie-breaking rule that determines the order of concurrent events (events that are not causally related).
- A total causal order is the strictest ordering in distributed systems; it establishes only one linearization, consistent with the causal order, among all the events that occur in the system, even those that occur concurrently. For that reason, the execution of the system is considered as synchronous.
- A total causal order is useful for implementing reliable and consistent services in distributed systems, such as atomic broadcast, distributed snapshots, consensus, and replication  .
- A total causal order can be implemented by using logical clocks, such as vector clocks, that capture the causal dependencies between events, and by using a deterministic algorithm, such as a sequencer or a leader, that assigns a unique and increasing identifier to each message .



### Techniques for Message Ordering in Distributed Systems

- Message ordering is the problem of ensuring that messages are processed in a consistent and predictable order in a distributed system .
- Message ordering is important because it affects the final outcome of the actions and the consistency of the system state .
- There are different types of message ordering techniques, depending on the desired level of ordering guarantee and the trade-off between performance and complexity  .
- Some of the common message ordering techniques are:

  - **Unordered**: Messages are delivered in any order, without any guarantee of ordering. This is the simplest and fastest technique, but it may lead to inconsistent or incorrect results .
  - **FIFO**: Messages are delivered in the same order as they are sent by each sender. This ensures that messages from the same sender are processed in a sequential order, but it does not guarantee any ordering among messages from different senders .
  - **Causal**: Messages are delivered in a way that preserves the causal dependencies among them. This means that if a message m1 causally precedes a message m2, then m1 is delivered before m2 at every receiver. Causal ordering captures the logical order of events in a distributed system, but it may incur some overhead in terms of message buffering and timestamping  .
  - **Total**: Messages are delivered in the same order at every receiver. This ensures that all receivers have a consistent view of the message sequence, but it may require a global agreement among the senders and the receivers, which can be costly and complex .
  - **Synchronous**: Messages are delivered in a way that synchronizes the actions of the senders and the receivers. This means that a sender waits for an acknowledgment from all receivers before sending the next message, and a receiver waits for a message from all senders before processing the next message. Synchronous ordering provides the strongest guarantee of ordering and consistency, but it may introduce a lot of delay and blocking in the system .

- Different message ordering techniques can be implemented using different protocols, such as:

  - **Unicast**: A message is sent from one sender to one receiver. Unicast can be used to implement unordered or FIFO ordering, depending on the underlying network layer .
  - **Broadcast**: A message is sent from one sender to all receivers. Broadcast can be used to implement unordered, FIFO, or causal ordering, depending on the message header and the delivery algorithm  .
  - **Multicast**: A message is sent from one sender to a subset of receivers. Multicast can be used to implement unordered, FIFO, causal, total, or synchronous ordering, depending on the message header, the delivery algorithm, and the group membership management  .



### Causal ordering of messages

- Causal ordering of messages is a partial ordering of messages in a distributed computing environment .
- It places a restriction on communication between processes by requiring that if the transmission of message mi to process pk necessarily preceded the transmission of message mj to the same process, then the delivery of these messages to that process must be ordered such that mi is delivered before mj  .
- Causal ordering of messages is one of the four semantics of multicast communication, namely unordered, totally ordered, causal, and sync-ordered communication.
- Multicast communication methods vary according to the message’s reliability guarantee and ordering guarantee.
- Causal ordering of messages is based on the notion of potential causality, which captures the idea that if an event A can possibly have influenced an event B, then A is causally prior to B.
- Potential causality can be defined in terms of message passing, since sending messages is the only way for processes to affect each other in a distributed system.
- A causal ordering protocol ensures that messages are delivered to each process in the same order as they are potentially caused.
- Causal ordering protocols can be classified into two categories: timestamp-based and acknowledgement-based.
- Timestamp-based protocols use logical clocks to assign timestamps to messages, and deliver messages according to their timestamps.
- Acknowledgement-based protocols use acknowledgements from other processes to determine the delivery order of messages.
- Causal ordering of messages is useful for applications that need to maintain consistency and coherence among replicated data or processes.
- Causal ordering of messages can also help to avoid anomalies and conflicts that may arise from concurrent or out-of-order updates.



### Global State for the Notes of the Unit 1 - Characterization of Distributed Systems in the Subject of Distributed System

- A **distributed system** is a collection of independent processes that communicate by exchanging messages over a network.
- A **global state** of a distributed system is a collection of the **local states** of the processes and the channels .
- A **local state** of a process is the values of its variables and its program counter at a given point in time.
- A **channel state** is the set of messages that have been sent but not yet received by the processes.
- A global state is **consistent** if it reflects a possible execution of the system, i.e., it does not contain any causal anomalies  .
- A **causal anomaly** is a situation where a message is received before it is sent, or a process observes the effect of a message before it observes the message itself.
- A **cut** is a partition of the set of events in the system into two subsets: past and future.
- A cut is **consistent** if it respects the causal order of events, i.e., it does not cut any message from sender to receiver .
- A **snapshot** is a mechanism to capture a consistent global state of a distributed system .
- A snapshot can be used for various purposes, such as checkpointing, debugging, monitoring, or termination detection .
- A snapshot algorithm must satisfy two properties: **safety** and **liveness** .
- **Safety** means that the snapshot is consistent and does not contain any causal anomalies .
- **Liveness** means that the snapshot eventually terminates and does not interfere with the normal execution of the system .
- There are different types of snapshot algorithms, depending on the assumptions about the system, such as synchronous or asynchronous, reliable or unreliable, FIFO or non-FIFO, etc .
- One of the most famous snapshot algorithms is the **Chandy-Lamport algorithm**, which works for asynchronous and reliable systems with FIFO channels .
- The Chandy-Lamport algorithm works as follows :
  - A process initiates the snapshot by recording its local state and sending a special marker message on each outgoing channel.
  - Upon receiving a marker message for the first time on an incoming channel, a process records its local state and the state of the channel as empty, and then sends a marker message on each outgoing channel.
  - Upon receiving a marker message on an incoming channel that has already been recorded, a process records the state of the channel as the set of messages received on that channel since the previous marker message.
  - The snapshot terminates when each process has recorded its local state and the state of each incoming channel.



### Termination Detection

Termination detection is a fundamental problem in distributed systems, where a set of processes cooperate to perform a computation. The problem is to determine when all the processes have finished their work and there are no more messages in transit between them. This is non-trivial because no process has complete knowledge of the global state, and there is no global time to synchronize the processes.

There are different algorithms for termination detection, depending on the assumptions and properties of the distributed system. One of the most well-known algorithms is Huang's algorithm, proposed by Shing-Tsaan Huang in 1989. Huang's algorithm is based on the concept of a process' state, which can be either active or idle. An active process may become idle at any time, but an idle process may only become active again upon receiving a computational message (a message that affects the computation). A process is also associated with a control message counter, which keeps track of the number of control messages (messages that are used for termination detection) sent and received by the process.

Huang's algorithm works as follows:

- Initially, all processes are active and their control message counters are zero.
- A process becomes idle when it has no more work to do and no more messages to send. When a process becomes idle, it sends a control message containing its counter value to a designated coordinator process.
- The coordinator process maintains a global counter, which is the sum of the counter values received from the idle processes. The coordinator also maintains a set of active processes, which is initially empty.
- When the coordinator receives a control message from an idle process, it adds the counter value to the global counter and adds the process to the set of active processes.
- When the coordinator receives a computational message from an active process, it subtracts one from the global counter and removes the process from the set of active processes.
- The coordinator detects termination when the global counter is zero and the set of active processes is empty.

Huang's algorithm has the following properties:

- It is correct, i.e., it detects termination if and only if termination has occurred.
- It is efficient, i.e., it uses a minimal number of control messages (one per process) and a minimal amount of information (one counter value per process).
- It is distributed, i.e., it does not require a central authority or a global clock to coordinate the processes.
- It is non-intrusive, i.e., it does not interfere with the underlying computation or require additional communication channels between processes.



## Unit 2 - Distributed Mutual Exclusion

- Distributed mutual exclusion is a fundamental problem in distributed computing systems .
- It ensures that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner  .
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion. Message passing is the sole means for implementing distributed mutual exclusion .
- A distributed mutual exclusion algorithm must satisfy the following requirements :
  - Safety: Only one process can execute the critical section (CS) at any given time.
  - Liveness: Every request for the CS is eventually granted.
  - Fairness: No process is indefinitely postponed or starved while requesting the CS.
- Distributed mutual exclusion algorithms can be classified into two categories :
  - Permission-based algorithms: A process must obtain permission from other processes before entering the CS. Examples are Lamport's algorithm, Ricart-Agrawala algorithm, Maekawa's algorithm, etc.
  - Token-based algorithms: A process must hold a special message called token to enter the CS. The token is passed among the processes in a predefined order. Examples are Suzuki-Kasami's algorithm, Raymond's algorithm, etc.



### Classification of distributed mutual exclusion

Distributed mutual exclusion is a problem of ensuring that only one process in a distributed system can access a shared resource or data at a time. It is a fundamental requirement for achieving consistency, coordination and synchronization among the processes.

There are three basic approaches for implementing distributed mutual exclusion:

- **Token-based approach**: A unique token is shared among the sites. A site is allowed to enter its critical section if it possesses the token. Mutual exclusion is ensured because the token is unique. Examples of token-based algorithms are Suzuki-Kasami's algorithm, Raymond's algorithm and Maekawa's algorithm.
- **Non-token-based approach**: A site requests permission from other sites before entering its critical section. A site is allowed to enter its critical section if it receives permission from all or a majority of other sites. Mutual exclusion is ensured by the voting mechanism. Examples of non-token-based algorithms are Lamport's algorithm, Ricart-Agrawala's algorithm and Singhal's algorithm.
- **Quorum-based approach**: A site requests permission from a subset of sites, called a quorum, before entering its critical section. A site is allowed to enter its critical section if it receives permission from all the sites in its quorum. Mutual exclusion is ensured by the intersection property of quorums. Examples of quorum-based algorithms are Naimi-Trehel's algorithm, Agrawal-El Abbadi's algorithm and Thomas's algorithm.



### Requirement of mutual exclusion theorem for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM

- Mutual exclusion is a concurrency control property which is introduced to prevent race conditions.
- It is the requirement that a process can not enter its critical section while another concurrent process is currently present or executing in its critical section i.e only one process is allowed to execute the critical section at any given time.
- A critical section is a segment of code that accesses a shared resource or data.
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion.
- Message passing is the sole means for implementing distributed mutual exclusion .
- There are three basic approaches for implementing distributed mutual exclusion:
  - Token-based algorithms: A process can enter its critical section only if it possesses a unique token. The token is passed among the processes in a predefined order or by request.
  - Permission-based algorithms: A process can enter its critical section only if it obtains permission from all or a subset of other processes in the system. The process sends request messages and waits for reply messages before entering the critical section.
  - Quorum-based algorithms: A process can enter its critical section only if it obtains permission from a majority or a quorum of other processes in the system. The process sends request messages and waits for reply messages from a quorum before entering the critical section.
- The mutual exclusion theorem states that any algorithm that solves the mutual exclusion problem in a distributed system must satisfy the following four properties:
  - Safety: At most one process can execute in its critical section at any given time.
  - Liveness: If a process requests to enter its critical section, it will eventually be granted permission to do so.
  - Fairness: No process is indefinitely postponed or starved from entering its critical section.
  - Fault-tolerance: The algorithm can tolerate failures of some processes or messages without violating the safety property.



### Token based and non token based algorithms for distributed mutual exclusion

Distributed mutual exclusion (DME) is the problem of ensuring that only one process at a time can access a shared resource in a distributed system. There are two main types of algorithms for DME: token based and non token based.

- Token based algorithms

  - In token based algorithms, a unique token is shared among all the processes in the system. The process that holds the token has the exclusive right to enter the critical section. A process that wants to enter the critical section must request the token from the current holder and wait until it receives the token. After exiting the critical section, the process must pass the token to another process that is waiting for it.
  - Token based algorithms have the advantage of avoiding unnecessary message exchanges and ensuring fairness among the processes. However, they also have some drawbacks, such as the possibility of losing the token due to node or link failures, the overhead of maintaining the token, and the delay of waiting for the token to arrive.
  - Examples of token based algorithms are:
    - Suzuki-Kasami algorithm: This is a modification of Ricart-Agrawala algorithm, a permission based (non token based) algorithm that uses REQUEST and REPLY messages to ensure mutual exclusion. In Suzuki-Kasami algorithm, the token is a data structure that contains a vector of sequence numbers, one for each process. The token holder maintains a queue of pending requests and sends the token to the process with the highest sequence number in the queue. The process that receives the token updates its sequence number and enters the critical section. After exiting the critical section, the process checks the queue and sends the token to the next process in the queue, or keeps the token if the queue is empty.
    - Raymond's algorithm: This is a tree based algorithm that organizes the processes into a logical tree. The root of the tree holds the token and can enter the critical section. A process that wants to enter the critical section sends a REQUEST message to its parent in the tree. The parent forwards the request to its parent until it reaches the root. The root sends the token to the process that requested it, and the process becomes the new root. After exiting the critical section, the process sends the token to its parent, and the parent becomes the new root. The process also sends a RELEASE message to its children to inform them that it no longer holds the token.

- Non token based algorithms

  - In non token based algorithms, there is no token in the system. Instead, the processes use timestamps to order the requests for the critical section and to resolve conflicts between simultaneous requests. A process that wants to enter the critical section sends a REQUEST message with its timestamp to a set of other processes and waits for their REPLY messages. The process can enter the critical section only when it has received all the REPLY messages and its request has the highest priority among all the pending requests. After exiting the critical section, the process sends a RELEASE message to the other processes to inform them that it has finished using the resource.
  - Non token based algorithms have the advantage of tolerating node or link failures, as there is no single point of failure. However, they also have some drawbacks, such as the high message complexity, the lack of fairness, and the possibility of deadlock or starvation.
  - Examples of non token based algorithms are:
    - Lamport's algorithm: This is a basic algorithm that uses logical clocks to generate timestamps. A process that wants to enter the critical section sends a REQUEST message with its timestamp to all the other processes and waits for their REPLY messages. The process can enter the critical section only when it has received all the REPLY messages and its request has the smallest timestamp among all the pending requests. After exiting the critical section, the process sends a RELEASE message to all the other processes to inform them that it has finished using the resource. The processes use a FIFO queue to order the requests and reply to them in the order of their timestamps.
    - Ricart-Agrawala algorithm: This is an optimization of Lamport's algorithm that reduces the message complexity. A process that wants to enter the critical section sends a REQUEST message with its timestamp to all the other processes and waits for their REPLY messages. The process can enter the critical section only when it has received all the REPLY messages and its request has the smallest timestamp among all the pending requests. After exiting the critical section, the process sends a RELEASE message to all the other processes to inform them that it has finished using the resource. The processes use a deferred



### Performance metric for distributed mutual exclusion algorithms

Distributed mutual exclusion algorithms are algorithms that ensure that only one process at a time can access a shared resource in a distributed system. The performance of these algorithms can be evaluated by the following metrics :

- **Message complexity**: It is the number of messages that are required per critical section (CS) execution by a process. It measures the communication overhead of the algorithm. A lower message complexity is desirable.
- **Synchronization delay**: It is the time elapsed between the departure of a process from the CS and the entry of the next process into the CS. It measures the degree of concurrency achieved by the algorithm. A lower synchronization delay is desirable.
- **Response time**: It is the time interval between the request of a process to enter the CS and the end of its CS execution. It measures the waiting time of the process. A lower response time is desirable.
- **Throughput**: It is the number of CS executions per unit time in the system. It measures the efficiency of the algorithm. A higher throughput is desirable.

Different algorithms may have different trade-offs among these metrics. For example, a token-based algorithm may have low message complexity but high synchronization delay, while a non-token-based algorithm may have high message complexity but low synchronization delay. A quorum-based algorithm may have lower message complexity and synchronization delay than both token-based and non-token-based algorithms, but it may require more knowledge of the system state. Therefore, the choice of the algorithm depends on the application requirements and the system characteristics.



## Unit 3 - Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set.
- Deadlocks can be handled by three strategies: deadlock prevention, deadlock avoidance, and deadlock detection.
- Deadlock prevention and avoidance are impractical in distributed systems, because they require global knowledge and coordination of all processes and resources.
- Deadlock detection is the best approach to handle deadlocks in distributed systems. It involves two steps: detecting the existence of deadlocks and resolving the detected deadlocks.
- Deadlock detection requires examining the status of process-resource interactions for the presence of cyclic wait. A cycle in the wait-for graph indicates a deadlock.
- Deadlock detection can be done by two methods: centralized and distributed.
- Centralized deadlock detection involves a designated node that collects the local wait-for graphs from all nodes and constructs a global wait-for graph to detect cycles. This method has the advantages of simplicity and efficiency, but also the disadvantages of single point of failure and communication overhead.
- Distributed deadlock detection involves a distributed algorithm that runs on all nodes and detects cycles in the wait-for graph without constructing a global wait-for graph. This method has the advantages of fault tolerance and scalability, but also the disadvantages of complexity and message overhead.
- Distributed deadlock detection can be further classified into two types: path-pushing and edge-chasing.
- Path-pushing algorithms propagate the dependency information along the wait-for graph and detect cycles when a node receives its own dependency information. Examples of path-pushing algorithms are the Chandy-Misra-Haas algorithm and the Ho-Ramamoorthy algorithm.
- Edge-chasing algorithms initiate probes along the wait-for graph and detect cycles when a probe returns to its initiator. Examples of edge-chasing algorithms are the Huang algorithm and the Menasce-Muntz algorithm.
- Deadlock resolution involves selecting and aborting some of the deadlocked processes to break the cycle and release the resources. The selection criteria can be based on factors such as priority, age, number of resources, etc.



### System Model for Distributed Deadlock Detection

- A distributed system consists of a set of nodes that communicate by message passing.
- Each node has a set of resources that can be requested by processes running on the node or on other nodes.
- A process can request a resource by sending a message to the node that owns the resource.
- A node can grant a resource to a process by sending a message to the process or by placing the resource in a shared buffer.
- A process can release a resource by sending a message to the node that owns the resource or by removing the resource from a shared buffer.
- A process can hold multiple resources at a time and can request additional resources while holding some resources.
- A process can block while waiting for a resource that is not available.
- A deadlock occurs when a set of processes are waiting for resources that are held by other processes in the set, forming a cycle of dependencies.
- A system model for distributed deadlock detection should specify the following aspects:
  - The representation of the process-resource interactions, such as wait-for graphs, request graphs, or dependency matrices.
  - The algorithm for detecting cycles in the process-resource interactions, such as edge chasing, diffusing computation, or global wait-for graph construction.
  - The location and frequency of deadlock detection, such as centralized, hierarchical, or distributed, and periodic, on-demand, or triggered.
  - The resolution of deadlock, such as aborting, preempting, or migrating processes or resources.



### Resource Vs Communication Deadlocks

- A deadlock occurs when a set of processes requests resources that are already occupied by other processes in the group. Because each process possesses a resource and waits for another resource held by another process, the execution of two or more processes is blocked.
- There are two types of deadlock in distributed systems: resource deadlock and communication deadlock.
- In resource deadlocks, processes access resources, such as data objects in database systems and buffers in store and forward communication networks. A process acquires a resource before accessing it and releasing it after using it.
- In communication deadlocks, processes communicate by message passing. A process sends a message to another process and waits for a reply. A communication deadlock occurs when there are pending messages (at least one) on a server, but they cannot be served.
- Resource deadlocks are more common and easier to detect than communication deadlocks. Resource deadlocks can be detected by using techniques such as wait-for graphs, timestamps, timeouts, and probes.
- Communication deadlocks are more difficult to detect and resolve than resource deadlocks. Communication deadlocks can be caused by factors such as loss or corruption of signals, network congestion, buffer overflow, or process failure. Communication deadlocks can be prevented by using techniques such as reliable message delivery, acknowledgement, retransmission, and deadlock-free routing.



### Deadlock Prevention for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

- A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
- Deadlock prevention is a technique to ensure that at least one of the necessary conditions for deadlock does not hold in a system.
- In a distributed system, deadlock prevention is more challenging than in a centralized system, because the processes and resources may be located in different nodes and there is no global information or control.
- There are two main approaches to deadlock prevention in a distributed system: ordered request and collective request.
- Ordered request: In this approach, each resource type is assigned a unique level and each process must request resources in increasing order of levels. This prevents circular wait condition and hence deadlock.
- Collective request: In this approach, each process must request all the resources it needs at once, before starting its execution. This prevents hold and wait condition and hence deadlock.
- Both approaches have some drawbacks, such as reduced concurrency, increased overhead, and wasted resources.
- Therefore, deadlock prevention is not widely used in distributed systems, and deadlock detection and recovery are preferred.



### Avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- Deadlock avoidance is a technique that prevents the occurrence of deadlocks by ensuring that the system is always in a safe state.
- A safe state is one where there exists a sequence of processes that can finish their execution without causing a deadlock.
- In a distributed system, deadlock avoidance is impractical due to several problems, such as:
  - Lack of global information about the resource allocation and requests of all processes.
  - High communication and synchronization overhead for maintaining and updating the global state.
  - Dynamic and unpredictable nature of the distributed system, where processes and resources may join or leave at any time.
- Therefore, deadlock detection is preferred over deadlock avoidance in distributed systems, as it allows more concurrency and flexibility.
- Deadlock detection involves examining the status of the process-resource interactions for the presence of cyclic wait, which indicates a deadlock.
- Deadlock detection in distributed systems can be classified into four categories, based on the type of information and algorithm used:
  - Path-pushing: Each process maintains a wait-for graph that represents the dependencies among processes, and periodically sends it to a coordinator node. The coordinator node merges the graphs and checks for cycles.
  - Edge-chasing: Each process sends a probe message to the process it is waiting for, and the message is forwarded along the dependency chain until it reaches a deadlocked process or returns to the sender. A cycle in the probe messages indicates a deadlock.
  - Diffusion computation: Each process initiates a computation to detect a deadlock involving itself, and propagates the computation to its neighbors. The computation terminates when all processes involved in the deadlock are identified or when no deadlock exists.
  - Global state detection: Each process periodically records its local state and sends it to a coordinator node. The coordinator node constructs a global state of the system and checks for deadlocks using a global wait-for graph or a global resource allocation graph.



### Detection and Resolution of Distributed Deadlocks

- A distributed deadlock is a situation where a set of processes in a distributed system are waiting for each other to release resources or send messages, and none of them can proceed.
- Detection and resolution of distributed deadlocks involve two steps: finding the existing deadlocks in the system and breaking them by aborting or rolling back some of the deadlocked processes.
- There are three main approaches to detect distributed deadlocks: centralized, distributed, and hierarchical.
  - Centralized approach: One designated node, called the coordinator, is responsible for maintaining and searching the global wait-for graph (WFG), which represents the dependencies among processes and resources in the system. The coordinator periodically collects information from other nodes about their local WFGs and merges them into the global WFG. Then, the coordinator searches the global WFG for cycles, which indicate deadlocks. The coordinator also initiates the resolution of the detected deadlocks by sending messages to the involved nodes. The advantages of this approach are simplicity and efficiency, but the disadvantages are high communication overhead, single point of failure, and lack of scalability.
  - Distributed approach: Each node maintains and searches its own local WFG, which represents the dependencies among processes and resources within the node and its neighboring nodes. Each node periodically exchanges information with its neighbors about their local WFGs and updates its own WFG accordingly. Then, each node searches its local WFG for cycles, which indicate deadlocks. The resolution of the detected deadlocks is done by the nodes themselves, without involving a coordinator. The advantages of this approach are fault tolerance, scalability, and reduced communication overhead, but the disadvantages are complexity and possibility of false or phantom deadlocks, which are cycles that do not correspond to actual deadlocks in the system.
  - Hierarchical approach: The nodes are organized into a hierarchy of clusters, where each cluster has a designated node, called the cluster head, that acts as the coordinator for the cluster. The cluster heads maintain and search the cluster WFGs, which represent the dependencies among processes and resources within the cluster and its neighboring clusters. The cluster heads periodically exchange information with each other about their cluster WFGs and update them accordingly. Then, each cluster head searches its cluster WFG for cycles, which indicate deadlocks. The resolution of the detected deadlocks is done by the cluster heads, or by the nodes themselves, depending on the level of the deadlock. The advantages of this approach are a balance between the centralized and distributed approaches, but the disadvantages are increased complexity and possibility of false or phantom deadlocks.
- The resolution of distributed deadlocks involves breaking the existing wait-for dependencies in the system WFG. It can be done by aborting or rolling back some of the deadlocked processes and releasing their resources or messages to the blocked processes in the deadlock, so that they can resume execution. The criteria for selecting which processes to abort or roll back include the following: the number of processes involved, the amount of work done, the priority of the processes, the cost of recovery, and the likelihood of repeated deadlocks. The resolution of distributed deadlocks can be initiated by the coordinator, the cluster heads, or the nodes themselves, depending on the approach used for detection. The resolution of distributed deadlocks can also be adaptive, meaning that it can adjust to the changing conditions of the system, such as the workload, the network topology, and the resource availability.



### Centralized Deadlock Detection

- This is a technique used in distributed systems to handle deadlock detection.
- According to this technique, the system maintains one **global wait-for graph** in a single chosen site, which is named as **deadlock-detection coordinator**.
- The global wait-for graph is a directed graph that represents the waiting relationships among processes and resources in the system.
- Each site in the system periodically sends its local wait-for graph to the coordinator, which then merges them to form the global wait-for graph .
- The coordinator periodically runs a **cycle detection algorithm** on the global wait-for graph to check for the existence of deadlocks .
- If a deadlock is detected, the coordinator selects one or more processes to abort and sends a message to the corresponding sites to terminate them .
- The advantages of this technique are:
  - It is simple and easy to implement.
  - It reduces the communication overhead and the frequency of deadlock detection as compared to the distributed approach.
- The disadvantages of this technique are:
  - It introduces a single point of failure and a performance bottleneck in the coordinator.
  - It may not reflect the current state of the system accurately due to the delays in sending and receiving the local wait-for graphs.
  - It may detect false or phantom deadlocks due to the inconsistency of the global wait-for graph.



### Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set.
- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems.
- Deadlock detection in distributed systems entails addressing two basic issues: detection of existing deadlocks and resolution of detected deadlocks.
- Deadlock detection requires examination of the status of process-resource interactions for presence of cyclic wait.
- There are three main approaches to detect deadlocks in distributed systems:
  - Centralized approach: A single site is designated as the deadlock detector and collects the local wait-for graphs from all the sites to construct a global wait-for graph. The deadlock detector periodically runs a cycle detection algorithm on the global wait-for graph and initiates the resolution of any detected deadlock.
  - Hierarchical approach: The sites are organized into a hierarchy of clusters, each with a local deadlock detector. The local deadlock detectors send their local wait-for graphs to their parent clusters, which construct a cluster wait-for graph. The cycle detection algorithm is run on the cluster wait-for graphs and the global wait-for graph at the root cluster. The resolution of any detected deadlock is delegated to the appropriate cluster or site.
  - Distributed approach: There is no central or hierarchical deadlock detector. Each site maintains its own local wait-for graph and participates in a distributed cycle detection algorithm. The distributed cycle detection algorithm can be based on edge chasing, diffusing computation, or probe propagation. The resolution of any detected deadlock is done by the site that initiated the cycle detection algorithm.



### Path Pushing Algorithms for Distributed Deadlock Detection

- Path pushing algorithms detect distributed deadlocks by maintaining an explicit global wait-for graph (WFG) at each site of the distributed system  .
- The global WFG is a directed graph that represents the dependencies among the processes in the system. A node in the graph is a process and an edge from node P to node Q means that P is waiting for a resource held by Q  .
- The basic idea is to build and update the global WFG at each site whenever a process requests, releases, or blocks on a resource. The global WFG is also exchanged among the neighboring sites periodically or on demand  .
- A site can initiate a deadlock detection by traversing its local copy of the global WFG and checking for cycles. A cycle in the global WFG indicates a deadlock among the processes involved in the cycle  .
- The advantages of path pushing algorithms are that they can detect deadlocks quickly and accurately, and they do not require any additional messages for deadlock detection  .
- The disadvantages of path pushing algorithms are that they require a lot of storage space and communication bandwidth to maintain and exchange the global WFG, and they may incur high overhead for updating the global WFG frequently  .



### Edge Chasing Algorithms for Distributed Deadlock Detection

- Edge chasing algorithms are a class of distributed deadlock detection algorithms that use special messages called probes to trace the dependency graph of processes and resources in a distributed system.
- A probe is a triplet (i, j, k) that denotes that the deadlock detection is initiated by process P_i and the message is being sent by the home site of process P_j to the home site of process P_k.
- The probe message follows the edges of the dependency graph from the waiting processes to the blocking processes until either a cycle is detected or all the edges are traversed.
- A cycle is detected when a probe message returns to the initiator process or when a process receives a probe message with its own identifier in the triplet.
- The most common edge chasing algorithm is the Chandy-Misra-Haas algorithm, which works for the AND request model, where a process can request multiple resources simultaneously and wait for all of them to be granted.
- The Chandy-Misra-Haas algorithm works as follows:

  - Each process maintains a wait-for graph that contains the processes and resources that it is waiting for and the processes and resources that are waiting for it.
  - When a process P_i initiates a deadlock detection, it sends a probe message (i, i, j) to the home site of each process P_j that it is waiting for.
  - When a process P_j receives a probe message (i, k, j), it checks if it is involved in a deadlock with P_i. If yes, it sends a reply message to P_i indicating the deadlock. If no, it forwards the probe message (i, j, l) to the home site of each process P_l that it is waiting for.
  - When a process P_i receives a reply message from P_j, it knows that there is a deadlock involving P_i and P_j and possibly other processes. It can then take appropriate actions to resolve the deadlock, such as aborting or preempting some processes or resources.

- The advantages of edge chasing algorithms are:

  - They are simple and efficient, as they only require sending and receiving probe messages along the dependency graph edges.
  - They are decentralized and distributed, as each process and site can initiate and participate in the deadlock detection independently and concurrently.
  - They are scalable and adaptable, as they can handle dynamic changes in the system topology and resource allocation.

- The disadvantages of edge chasing algorithms are:

  - They may generate false positives, as they may detect cycles that are not deadlocks, such as when some processes or resources are released before the probe message reaches them.
  - They may generate false negatives, as they may miss some deadlocks, such as when some processes or resources are acquired after the probe message passes them.
  - They may generate redundant messages, as they may send multiple probe messages along the same edge or cycle, increasing the network traffic and overhead.



## Unit 4 - Agreement Protocols

- Agreement protocols are a class of distributed algorithms that allow a set of processes to reach a common decision, despite the possibility of failures or malicious behavior.
- Agreement protocols are useful for implementing fault-tolerant services, such as distributed consensus, atomic broadcast, leader election, and distributed transactions.
- Agreement protocols can be classified into different types, depending on the assumptions they make about the system model, the communication model, the failure model, and the adversary model.
- Some common types of agreement protocols are:
  - **Crash fault-tolerant protocols**: These protocols assume that processes may fail by crashing, but do not behave maliciously. They typically use reliable, synchronous, or partially synchronous communication channels, and require a majority of processes to be correct.
  - **Byzantine fault-tolerant protocols**: These protocols assume that processes may fail by behaving arbitrarily, or even colluding with other faulty processes. They typically use authenticated, asynchronous, or partially synchronous communication channels, and require at least two-thirds of processes to be correct.
  - **Randomized protocols**: These protocols use randomization techniques, such as coin tossing or sampling, to break symmetry and achieve agreement with high probability, even in the presence of failures or adversaries. They typically use unreliable, asynchronous, or partially synchronous communication channels, and have weaker correctness guarantees than deterministic protocols.
  - **Cryptographic protocols**: These protocols use cryptographic primitives, such as digital signatures, hash functions, or encryption, to ensure the integrity, authenticity, or confidentiality of messages, and to prevent or detect malicious behavior. They typically use unreliable, asynchronous, or partially synchronous communication channels, and have stronger security guarantees than non-cryptographic protocols.



### Introduction for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by passing messages.
- Agreement protocols are algorithms that enable the processes in a distributed system to reach a common decision or a consistent state, despite the presence of failures or uncertainties.
- Agreement protocols are essential for ensuring the correctness, consistency, reliability, and availability of distributed systems.
- Some examples of agreement problems are:
  - Consensus: All processes agree on a single value from a set of proposed values.
  - Atomic commit: All processes agree on whether to commit or abort a distributed transaction.
  - Byzantine agreement: All processes agree on a single value from a set of proposed values, even if some processes are faulty and may behave arbitrarily.
  - Leader election: All processes agree on a unique process that acts as the leader or coordinator of the system.
  - Mutual exclusion: All processes agree on which process has the exclusive access to a shared resource at any given time.
- Agreement protocols are challenging to design and implement in distributed systems, because of the following issues:
  - Asynchrony: The processes and the communication channels may have unpredictable delays, making it hard to synchronize and order events.
  - Partial failure: Some processes or communication channels may fail or become unreachable, while others continue to operate normally.
  - Non-determinism: The processes and the communication channels may behave in unexpected or random ways, such as losing, duplicating, or reordering messages.
  - Adversarial behavior: Some processes may be malicious or corrupted, and may try to disrupt the agreement or mislead other processes.
- Agreement protocols must satisfy some desirable properties, such as:
  - Validity: The agreed value must be one of the proposed values.
  - Agreement: All correct processes must agree on the same value.
  - Termination: All correct processes must eventually decide on a value.
  - Fault-tolerance: The protocol must work correctly even if some processes or communication channels fail or behave maliciously.
  - Efficiency: The protocol must use a reasonable amount of time, space, and communication resources.



### System models for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

A system model is a description of the properties and assumptions of a distributed system that are relevant for its design and analysis. System models can help us understand the behavior and limitations of a distributed system, as well as compare different algorithms and protocols for solving common problems.

There are three main types of system models for distributed systems:

- **Network models**: These models capture the characteristics and behavior of the network links that connect the nodes of a distributed system. For example, network models can describe the reliability, latency, bandwidth, and topology of the network.
- **Node models**: These models capture the characteristics and behavior of the nodes that run the processes of a distributed system. For example, node models can describe the availability, performance, and failure modes of the nodes.
- **Timing models**: These models capture the assumptions and guarantees about the timing of events and messages in a distributed system. For example, timing models can describe the synchrony, asynchrony, or partial synchrony of the system.

Some examples of system models for distributed systems are:

- **Client-server model**: This is an architectural model that describes a system where clients request services from servers, and servers provide responses to clients. The clients and servers can be distributed across different nodes and communicate through the network. This model is widely used for web applications, databases, and remote procedure calls.
- **Peer-to-peer model**: This is an architectural model that describes a system where nodes act as both clients and servers, and cooperate to provide and consume services. The nodes can be distributed across different locations and communicate through the network. This model is widely used for file sharing, content distribution, and distributed hash tables.
- **Crash-stop model**: This is a fault model that describes a system where nodes can fail by crashing, and do not recover from failures. The nodes that do not fail are called correct, and the nodes that fail are called faulty. This model is often used to simplify the analysis of distributed algorithms and protocols, but it is not realistic in practice.
- **Crash-recovery model**: This is a fault model that describes a system where nodes can fail by crashing, but can also recover from failures and resume their execution. The nodes that do not fail or recover are called correct, and the nodes that fail or recover are called faulty. This model is more realistic than the crash-stop model, but it also introduces more complexity and challenges for distributed algorithms and protocols.
- **Synchronous model**: This is a timing model that describes a system where there are known bounds on the execution time of processes, the transmission time of messages, and the drift rate of clocks. The system can be divided into discrete rounds, where each round consists of sending, receiving, and processing messages. This model is often used to simplify the design and analysis of distributed algorithms and protocols, but it is not realistic in practice.
- **Asynchronous model**: This is a timing model that describes a system where there are no bounds on the execution time of processes, the transmission time of messages, and the drift rate of clocks. The system cannot be divided into discrete rounds, and the order and timing of events and messages are unpredictable. This model is more realistic than the synchronous model, but it also introduces more uncertainty and impossibility results for distributed algorithms and protocols.
- **Partially synchronous model**: This is a timing model that describes a system where there are bounds on the execution time of processes, the transmission time of messages, and the drift rate of clocks, but these bounds are unknown or may change over time. The system can be divided into discrete rounds, but the length and synchrony of the rounds may vary. This model is a compromise between the synchronous and asynchronous models, and it captures the behavior of many real-world distributed systems.



### Classification of Agreement Problem

An agreement problem is a problem where a set of processes in a distributed system have to agree on a common value or decision, despite the possibility of failures or malicious behavior. Agreement problems are fundamental to achieving fault tolerance and consistency in distributed systems. There are different types of agreement problems, depending on the assumptions and requirements of the system. Some of the well-known agreement problems are:

- **Byzantine agreement problem**: A single value, which is to be agreed on, is initialized by an arbitrary process and all non-faulty processes have to agree on that value. The processes may be subject to Byzantine failures, which means they can behave arbitrarily or maliciously, and send conflicting or incorrect messages to other processes. The goal is to ensure that all non-faulty processes agree on the same value, and that value is the initial value of some non-faulty process.   
- **Consensus problem**: A generalization of the Byzantine agreement problem, where each process can propose a value and all non-faulty processes have to agree on a common value. The value agreed on must be one of the proposed values. The processes may be subject to crash failures, which means they can stop executing at any point, but cannot send incorrect messages. The goal is to ensure that all non-faulty processes agree on the same value, and that value is one of the proposed values.   
- **Interactive consistency problem**: A variation of the Byzantine agreement problem, where each process has an initial value and all non-faulty processes have to agree on a vector of values, one for each process. The vector agreed on must satisfy two properties: (1) the value for each non-faulty process is its initial value, and (2) the value for each faulty process is the same for all non-faulty processes. The processes may be subject to Byzantine failures, as in the Byzantine agreement problem. The goal is to ensure that all non-faulty processes agree on the same vector of values, and that vector satisfies the two properties.  

These agreement problems are related to each other and have different applications in distributed systems. For example, the Byzantine agreement problem can be used to implement reliable broadcast, where a message sent by a process is received by all non-faulty processes, even if the sender is faulty. The consensus problem can be used to implement atomic commit, where a set of processes have to decide whether to commit or abort a transaction, even if some processes crash. The interactive consistency problem can be used to implement group membership, where a set of processes have to agree on a consistent view of the system, even if some processes are faulty.



### Byzantine agreement problem

- The Byzantine agreement problem is a fundamental problem in fault tolerant distributed computing that requires a set of parties in a distributed environment to agree on a value even if some of the parties are corrupted.
- The problem was first defined by Lamport who also gave a solution under the situation of processor failure.
- The problem is also known as the Byzantine generals problem, interactive consistency, source congruency, error avalanche, and Byzantine failure.
- The problem can be illustrated by the following scenario:

    - Several divisions of the Byzantine army are camped outside an enemy city, each division commanded by its own general.
    - The generals can communicate with one another only by messenger.
    - After observing the enemy, they must decide upon a common plan of action, either to attack or to retreat.
    - Some of the generals may be traitors who try to prevent the loyal generals from reaching agreement.
    - The loyal generals must have an algorithm to guarantee that they all agree on the same plan, and that the plan is not influenced by the traitors.

- The problem is challenging because of the following reasons:

    - The generals do not know who are the traitors and who are the loyal ones.
    - The messages sent by the generals may be tampered with by the traitors or lost in transit.
    - The generals may have different views of the enemy situation and the optimal plan of action.

- The problem has many applications in distributed systems, such as consensus protocols, fault tolerance, cryptography, and blockchain .
- The problem has been studied extensively and various solutions have been proposed, depending on the assumptions made about the number of traitors, the communication model, the synchrony of the system, and the type of faults .
- Some of the well-known solutions are:

    - The oral messages algorithm, which requires a majority of loyal generals and reliable communication channels.
    - The signed messages algorithm, which allows for any number of traitors but requires authenticated digital signatures.
    - The practical Byzantine fault tolerance (PBFT) algorithm, which tolerates up to one-third of traitors and uses a leader-based approach with message broadcasts and voting.
    - The Bitcoin protocol, which uses a proof-of-work mechanism to achieve probabilistic consensus among anonymous and untrusted parties.



### Consensus problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- The consensus problem is the problem of getting a set of nodes in a distributed system to agree on something - it might be a value, a course of action or a decision.
- Achieving consensus allows a distributed system to act as a single entity, with every individual node aware of and in agreement with the actions of the whole of the network.
- Consensus is a general agreement on a decision made by the majority of those involved.
- Consensus is needed in a distributed system to ensure overall system reliability on top of unreliable system components.
- Consensus is also needed to coordinate distributed transactions, replicate data, elect leaders, and implement fault tolerance mechanisms.
- Consensus is hard to achieve in a distributed system due to the possibility of node failures, network partitions, message delays, and malicious attacks .
- There are many ways in which processes in a distributed system can reach a consensus, but there is usually a trade-off between security and performance.
- Some of the common consensus protocols are:
  - Two-phase commit: A simple and centralized protocol that requires a coordinator to collect votes from all participants and then broadcast the final decision.
  - Three-phase commit: An extension of two-phase commit that adds a pre-commit phase to avoid blocking in case of coordinator failure.
  - Paxos: A family of decentralized protocols that use a quorum of acceptors to agree on a value proposed by a leader.
  - Raft: A simplified version of Paxos that uses a leader election mechanism and a replicated log to ensure consistency among the nodes.
  - Byzantine fault tolerance: A class of protocols that can tolerate arbitrary failures or malicious behaviors of up to one-third of the nodes.
- The consensus problem is proven to be impossible to solve in an asynchronous distributed system with even one faulty node, according to the FLP impossibility result.
- However, practical consensus protocols can achieve probabilistic or eventual consensus by making some assumptions about the system model, such as synchrony, partial synchrony, or randomization.



### Interactive Consistency Problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- Interactive consistency is the problem in which n distinct nodes, each having its own private value, where up to t may be Byzantine, run an algorithm that allows all non-faulty nodes to infer the values of each other node  .
- Byzantine nodes are those that can behave arbitrarily, such as sending incorrect or conflicting messages, or remaining silent .
- Interactive consistency is a generalization of distributed consensus, where the goal is to reach the agreement in a distributed system in the presence of faults.
- Interactive consistency is relevant to critical applications that rely on the combination of the opinions of multiple peers to provide a service, such as fault-tolerant distributed systems, blockchain systems, or voting systems .
- Interactive consistency can be solved by using different algorithms, such as broadcast, randomized, or cryptographic algorithms, depending on the assumptions and requirements of the system .
- Interactive consistency has some limitations and challenges, such as the impossibility of achieving it in asynchronous systems with more than one-third of Byzantine nodes, the trade-off between performance and security, and the need for a single synchronization barrier  .



### Solution to Byzantine Agreement problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- The Byzantine agreement problem is a fundamental problem in fault tolerant distributed computing, where a set of parties in a distributed environment need to agree on a value even if some of the parties are corrupted.
- The problem was first defined by Lamport  and inspired by a hypothetical scenario of several divisions of the Byzantine army camped outside an enemy city, each division commanded by its own general. The generals can communicate with one another only by messenger. After observing the enemy, they must decide upon a common plan of action.
- A solution to the Byzantine agreement problem requires that the following conditions are met:
  - **Agreement**: All honest parties agree on the same value.
  - **Validity**: If all honest parties propose the same value, then they must agree on that value.
  - **Termination**: All honest parties eventually decide on a value.
- A number of solutions to the Byzantine agreement problem exist, depending on the assumptions made about the communication model, the number of corrupted parties, and the type of corruption.
- One of the most well-known solutions is the **Oral Messages Algorithm** by Lamport, Shostak, and Pease. This algorithm assumes that the communication is synchronous, meaning that there is a known upper bound on the message delivery time, and that the messages are authenticated, meaning that the sender and the content of the message cannot be forged. The algorithm also assumes that less than one-third of the parties are corrupted, and that the corruption is arbitrary, meaning that the corrupted parties can behave in any way to disrupt the agreement .
- The Oral Messages Algorithm works as follows  :
  - Each party has an initial value, which is either 0 or 1, and a round number, which starts from 0.
  - In round 0, the source party (the commander in the army scenario) sends its value to all other parties (the lieutenants).
  - In round k > 0, each party that has received a value from the source party in round k-1 sends that value to all other parties.
  - After round k, each party that has received k+1 values from the source party (either directly or indirectly) decides on the majority value among those values.
  - The algorithm terminates after n-1 rounds, where n is the total number of parties.
- The Oral Messages Algorithm guarantees that the agreement, validity, and termination conditions are met, as long as less than one-third of the parties are corrupted  .
- The Oral Messages Algorithm has a high communication complexity, as it requires O(n^2) messages per round, and O(n^3) messages in total  .
- Other solutions to the Byzantine agreement problem include the **Signed Messages Algorithm**, which reduces the communication complexity by using digital signatures, the **Randomized Algorithm**, which relaxes the agreement condition by allowing a small probability of disagreement, and the **Asynchronous Algorithm**, which does not assume a synchronous communication model .



### Application of Agreement problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- Agreement problem is a fundamental problem in distributed computing and multi-agent systems that requires coordinating processes to reach consensus, or agree on some data value that is needed during computation .
- Agreement problem is essential for achieving overall system reliability in the presence of a number of faulty processes .
- Agreement problem has many variants, such as consensus, atomic commitment, atomic broadcast, and group membership .
- Consensus is the problem of getting all processes to agree on a single value, such as the result of a computation or the state of a replicated object  .
- Atomic commitment is the problem of getting all processes to agree on whether to commit or abort a transaction, such as a database update or a payment .
- Atomic broadcast is the problem of getting all processes to deliver the same set of messages in the same order, such as a log of events or a sequence of commands .
- Group membership is the problem of getting all processes to agree on the set of processes that are currently active and reachable in the system, such as a cluster of servers or a network of peers .
- Agreement problem is challenging to solve in distributed systems because of the possibility of communication failures, process crashes, network partitions, and malicious behavior   .
- Agreement problem is often impossible to solve in asynchronous systems, where there is no bound on message delays or process speeds, unless some additional assumptions are made, such as the use of failure detectors, randomization, or cryptography  .
- Agreement problem is often solvable in synchronous systems, where there is a known bound on message delays and process speeds, but the solution may depend on the number and type of faults that can occur, such as crash faults, omission faults, or Byzantine faults   .
- Agreement problem is an active area of research in distributed systems, with many applications in fault-tolerant computing, distributed databases, distributed ledger technologies, distributed consensus algorithms, and distributed coordination services     .



### Atomic Commit in Distributed Database System

- An atomic commit is an operation that applies a set of distinct changes as a single operation. If the changes are applied, then the atomic commit is said to have succeeded. If the changes are not applied, then the atomic commit is said to have failed or aborted.
- In distributed database systems, the primary need for commit protocols is to maintain the atomicity of distributed transactions. A distributed transaction is a transaction that accesses data from multiple sites in a distributed system .
- Atomicity means that either all the changes made by a distributed transaction are committed (made permanent) or none of them are. Atomicity ensures the consistency and integrity of the distributed database.
- Atomic commit protocols are algorithms that coordinate the commit or abort decisions of the sites participating in a distributed transaction. They ensure that all the sites agree on the same outcome, either commit or abort, even in the presence of failures.
- There are two main types of atomic commit protocols: blocking and non-blocking. Blocking protocols require some sites to wait for the recovery of other failed sites before they can decide on the outcome of a transaction. Non-blocking protocols allow some sites to decide on the outcome of a transaction without waiting for the recovery of other failed sites .
- Examples of blocking protocols are the two-phase commit protocol (2PC) and the three-phase commit protocol (3PC). Examples of non-blocking protocols are the Paxos commit protocol and the FLAC protocol .



## Unit 5 - Distributed Resource Management

- Distributed resource management (DRM) is an evolving discipline that aims to enable distributed enterprise systems to operate effectively in production.
- DRM involves a set of software, hardware, network tools, procedures and policies for managing various types of resources in a distributed system, such as computing, storage, communication, energy, and data  .
- DRM can provide various benefits for distributed systems, such as:
  - Enhancing system resiliency and reliability by leveraging distributed and renewable energy sources, such as solar panels, batteries, and combined heat and power (CHP) systems  .
  - Improving system performance and efficiency by optimizing resource allocation and utilization, such as load balancing, scheduling, and demand response  .
  - Reducing system costs and environmental impacts by shifting load away from high price periods, improving load factor, and minimizing carbon emissions  .
- DRM can be implemented in a centralized or decentralized manner, depending on the system architecture, requirements, and constraints .
  - Centralized DRM relies on a single authority or coordinator that has global knowledge and control over the resources and their states .
  - Decentralized DRM distributes the decision-making and control among multiple agents or nodes that have local or partial knowledge and control over the resources and their states .
- DRM faces various challenges and issues, such as:
  - Scalability and complexity of managing large-scale and heterogeneous distributed systems with dynamic and uncertain resource availability and demand .
  - Interoperability and compatibility of different DRM tools and standards across different platforms, vendors, and domains  .
  - Security and privacy of the resource data and transactions, especially in the context of cyber-physical systems and the Internet of Things (IoT)  .
  - Quality of service and user satisfaction of the resource consumers and providers, especially in the context of service-level agreements (SLAs) and market mechanisms  .



### Issues in distributed file systems

A distributed file system (DFS) is a system that allows multiple clients to access and manipulate files stored on one or more servers over a network. DFSs aim to provide high performance, reliability, scalability, and transparency to the users and applications. However, there are several issues and challenges in designing and implementing a DFS, such as:

- **Naming and name resolution**: A DFS needs to provide a consistent and uniform way of naming and locating files across different servers and clients. This involves choosing a suitable namespace, such as hierarchical, flat, or attribute-based, and a name resolution mechanism, such as centralized, distributed, or hybrid, that can map names to physical locations efficiently and reliably .
- **Replication and consistency**: A DFS may replicate files or parts of files across multiple servers to improve availability, fault tolerance, and load balancing. However, this also introduces the problem of maintaining consistency among the replicas, especially when concurrent updates occur. A DFS needs to adopt a suitable replication strategy, such as eager or lazy, and a consistency model, such as strict, causal, or eventual, that can balance the trade-offs between performance and correctness .
- **Caching and cache coherence**: A DFS may cache files or parts of files on the client side to reduce the network traffic and latency. However, this also raises the issue of keeping the cached data coherent with the server data, especially when multiple clients access the same file. A DFS needs to implement a cache coherence protocol, such as write-through, write-back, or write-once, that can ensure the validity and freshness of the cached data .
- **Security and access control**: A DFS needs to protect the files and the system from unauthorized or malicious access and modification. This involves implementing mechanisms for authentication, authorization, encryption, and auditing, that can ensure the confidentiality, integrity, and accountability of the data and the users .
- **Failure handling and recovery**: A DFS needs to cope with various types of failures, such as node crashes, network partitions, or disk errors, that may affect the availability and correctness of the system. This involves implementing techniques for fault detection, fault tolerance, fault masking, and fault recovery, that can ensure the continuity and consistency of the system  .
- **Performance and scalability**: A DFS needs to provide high performance and scalability to the users and applications, especially when the system grows in size and complexity. This involves optimizing the system design and implementation, such as choosing appropriate data structures, algorithms, and protocols, that can reduce the overhead and improve the efficiency of the system  .



### Mechanism for building distributed file systems

A distributed file system (DFS) is a file system that enables clients to access file storage from multiple hosts through a computer network as if the user was accessing local storage. Files are spread across multiple storage servers and in multiple locations, which enables users to share data and storage resources.

Some of the benefits of using a DFS are:

- Improved availability and reliability: A DFS can tolerate failures of individual servers or network links by replicating or caching data on multiple servers. A DFS can also provide load balancing and fault tolerance by distributing requests among multiple servers.
- Improved performance and scalability: A DFS can improve the access speed and throughput of file operations by distributing the workload among multiple servers and locations. A DFS can also support large-scale file systems by allowing dynamic addition and removal of servers and storage devices.
- Simplified administration and management: A DFS can provide a logical view of shared folders that hides the physical location and structure of the files from the users. A DFS can also simplify the administration and management of file permissions, backups, and restores by using a centralized or distributed approach.

Some of the challenges of building a DFS are:

- Consistency and coherence: A DFS must ensure that the files are consistent and coherent across multiple servers and locations, especially when concurrent updates or failures occur. A DFS must also deal with issues such as file locking, version control, and cache coherence.
- Security and privacy: A DFS must protect the files from unauthorized access, modification, or deletion by malicious users or attackers. A DFS must also ensure the confidentiality, integrity, and availability of the files by using encryption, authentication, and authorization mechanisms.
- Complexity and overhead: A DFS must cope with the complexity and overhead of managing multiple servers, locations, and network connections. A DFS must also handle the trade-offs between performance, availability, reliability, and consistency by using appropriate algorithms and protocols.



### Design issues in Distributed Shared Memory

Distributed Shared Memory (DSM) is a mechanism that allows multiple processes on different nodes to share a common logical address space and access data transparently. DSM can simplify the programming of distributed applications and improve the performance and scalability of parallel systems. However, DSM also introduces several design issues that need to be addressed, such as:

- **Granularity**: Granularity refers to the size of the unit of data that is shared and transferred among the nodes. A fine-grained DSM system uses small units, such as words or cache lines, while a coarse-grained DSM system uses large units, such as pages or segments. The choice of granularity affects the communication overhead, the memory overhead, the false sharing, and the coherence protocol complexity of the DSM system  .
- **Structure**: Structure refers to the organization and layout of the shared data in the memory. The structure can be flat, hierarchical, or segmented, depending on how the shared address space is divided and mapped to the physical memory of the nodes. The choice of structure affects the naming, allocation, and location of the shared data, as well as the fault tolerance and heterogeneity of the DSM system  .
- **Coherence semantics**: Coherence semantics refers to the consistency model that defines the order and visibility of the updates to the shared data. The coherence semantics can be strict, relaxed, or weak, depending on how much the DSM system allows the local copies of the shared data to diverge from each other. The choice of coherence semantics affects the correctness, performance, and programmability of the DSM system  .
- **Coherence protocol**: Coherence protocol refers to the mechanism that implements the coherence semantics and maintains the consistency of the shared data. The coherence protocol can be centralized, distributed, or hybrid, depending on how the control and responsibility of the coherence operations are distributed among the nodes. The coherence protocol can also be based on invalidation, update, or replication, depending on how the DSM system handles the modifications to the shared data  .
- **Scalability**: Scalability refers to the ability of the DSM system to handle the increase in the number of nodes, the size of the shared data, and the frequency of the accesses to the shared data. The scalability of the DSM system depends on the design choices of the granularity, structure, coherence semantics, and coherence protocol, as well as the characteristics of the underlying network and hardware. The DSM system should aim to minimize the communication latency, bandwidth, and contention, as well as the memory and processing overhead, to achieve high scalability  .
- **Heterogeneity**: Heterogeneity refers to the diversity of the nodes, the network, and the applications in the DSM system. The heterogeneity of the nodes can be in terms of the architecture, the operating system, the memory size, and the processing speed. The heterogeneity of the network can be in terms of the topology, the protocol, the bandwidth, and the latency. The heterogeneity of the applications can be in terms of the data structure, the access pattern, and the synchronization requirement. The DSM system should be able to adapt to the heterogeneity and provide a uniform and efficient abstraction of the shared memory  .



### Algorithm for Implementation of Distributed Shared Memory

Distributed Shared Memory (DSM) is a technique that allows multiple processes on different nodes of a distributed system to access a common virtual address space as if they were running on a single machine. DSM provides a high-level abstraction for interprocess communication and synchronization, and can simplify the design and implementation of distributed applications.

There are different algorithms for implementing DSM, each with its own advantages and disadvantages. Some of the basic algorithms are:

- **Central Server Algorithm**: In this algorithm, a central server maintains all the shared data and services read and write requests from other nodes. The server can use a page-based or an object-based granularity for the shared data. The advantage of this algorithm is its simplicity and consistency, but the disadvantage is its poor scalability and performance, as the server can become a bottleneck and a single point of failure.

- **Migration Algorithm**: In this algorithm, the shared data is not fixed at a single location, but can migrate from one node to another depending on the access patterns. The migration algorithm can reduce the communication overhead by moving the data closer to the nodes that need it, but it can also incur additional overhead for transferring and updating the data. The migration algorithm can use a directory-based or a broadcast-based scheme for locating the data.

- **Replication Algorithm**: In this algorithm, the shared data is replicated on multiple nodes, so that each node can access a local copy of the data. The replication algorithm can improve the availability and fault-tolerance of the data, but it can also introduce consistency issues, as the copies need to be synchronized periodically. The replication algorithm can use a write-invalidate or a write-update protocol for maintaining the coherence of the data.

- **Hybrid Algorithm**: In this algorithm, a combination of the previous algorithms is used, depending on the characteristics of the shared data and the application. For example, some data can be centralized, some can be migrated, and some can be replicated, depending on the frequency and locality of the accesses. The hybrid algorithm can achieve a better trade-off between performance and consistency, but it can also increase the complexity and overhead of the implementation.



## Unit 6 - Failure Recovery in Distributed Systems

- Failure recovery is the process of restoring the correct state of a distributed system after a failure occurs.
- Failure recovery is essential for fault tolerance, which is the ability of a system to continue functioning despite failures.
- Failures in distributed systems can be classified into different types, such as:
  - Process failures: when a process stops executing or behaves incorrectly.
  - Communication failures: when a message is lost, delayed, duplicated, or corrupted during transmission.
  - Network failures: when a network partition occurs, isolating some processes from others.
  - Media failures: when a secondary storage device fails or becomes inaccessible.
  - Byzantine failures: when a process or a message behaves maliciously or arbitrarily.
- Failure recovery techniques can be broadly divided into two categories, based on the timing of recovery actions:
  - Reactive recovery: when the recovery actions are triggered after a failure is detected.
  - Proactive recovery: when the recovery actions are performed periodically or preemptively, before a failure is detected.
- Reactive recovery techniques include:
  - Checkpointing: when a process periodically saves its state to a stable storage, which can be used to resume execution after a failure.
  - Logging: when a process records its actions and messages to a stable storage, which can be used to replay or undo the effects of a failure.
  - Replication: when a process has one or more backup copies, which can take over its role after a failure.
  - Voting: when a process consults with other processes to reach a consensus on the correct state or action after a failure.
- Proactive recovery techniques include:
  - Garbage collection: when a process periodically removes unused or obsolete data from its memory or storage, which can prevent memory leaks or data corruption.
  - Heartbeat: when a process periodically sends a message to another process to indicate its aliveness, which can detect failures or network partitions.
  - Renewal: when a process periodically restarts itself or creates a new copy of itself, which can eliminate accumulated errors or malicious behavior.
  - Diversity: when a process uses different algorithms, hardware, or software components, which can reduce the probability of common failures or attacks.



### Concepts in Backward and Forward Recovery

- Backward recovery and forward recovery are two techniques to restore the system state after a failure in a distributed system.
- Backward recovery involves rolling back the system state to a previous error-free state by using checkpoints or logs. Forward recovery involves correcting the errors in the current state and continuing the execution from there.
- Backward recovery is more general and independent of the nature of faults, but it may require more overhead and coordination among processes. Forward recovery is more efficient and avoids repeating the computation, but it may require more knowledge and prediction of the faults and their effects.
- Some of the concepts related to backward and forward recovery are:

  - Checkpoint: A checkpoint is a snapshot of the system state at a certain point in time. Checkpoints can be taken periodically or triggered by some events. Checkpoints can be local (for each process) or global (for the whole system). Checkpoints can be used to roll back the system state in case of a failure.
  - Log: A log is a record of the actions or events that have occurred in the system. Logs can be used to undo or redo the actions or events in case of a failure. Logs can be physical (recording the actual changes in the data) or logical (recording the operations or transactions that caused the changes).
  - Recovery line: A recovery line is a set of consistent checkpoints that define a global state of the system. A recovery line can be used to restore the system state after a failure. A recovery line can be consistent (no causal dependency violation) or optimal (the latest possible consistent state).
  - Dependency graph: A dependency graph is a representation of the causal dependencies among the processes or events in the system. A dependency graph can be used to determine the consistent checkpoints or the effects of faults in the system. A dependency graph can be static (based on the program structure) or dynamic (based on the actual execution).
  - Error detection: Error detection is the process of identifying and locating the faults or errors in the system. Error detection can be done by using techniques such as timeouts, acknowledgments, heartbeats, voting, checksums, etc.
  - Error correction: Error correction is the process of removing or repairing the faults or errors in the system. Error correction can be done by using techniques such as retrying, masking, compensation, etc.



### Recovery in Concurrent Systems

Recovery in concurrent systems is the process of restoring the system to a consistent state after a failure, while preserving the effects of the committed transactions and discarding the effects of the aborted transactions. Recovery in concurrent systems is more complex than in sequential systems, because the transactions may interleave their operations and share resources. Therefore, the recovery mechanism must coordinate with the concurrency control mechanism to ensure atomicity, consistency, isolation, and durability (ACID) properties of the transactions.

There are different techniques for recovery in concurrent systems, such as:

- **Interaction with concurrency control**: In this technique, the recovery scheme depends on the concurrency control scheme that is used. For example, if the concurrency control scheme is based on locking, then the recovery scheme must release the locks held by the aborted transactions and restore the values of the data items that were modified by them. If the concurrency control scheme is based on timestamps, then the recovery scheme must invalidate the versions of the data items that were created by the aborted transactions and use the previous versions instead. 

- **Transaction rollback**: In this technique, the recovery scheme uses the log records of the transactions to undo their effects. The log records contain information about the operations performed by the transactions, such as the data items read and written, the old and new values of the data items, and the commit and abort events. The recovery scheme scans the log records in reverse order and applies the undo operation for each log record until it reaches the start of the transaction. The undo operation restores the old value of the data item that was modified by the transaction. 

- **Checkpoints**: In this technique, the recovery scheme periodically records the state of the system and the transactions in a special log record called a checkpoint. A checkpoint contains information about the active transactions, the committed transactions, the data items in the buffer, and the locks held by the transactions. The recovery scheme uses the checkpoint to reduce the amount of work that needs to be done after a failure. The recovery scheme scans the log records from the most recent checkpoint and applies the redo operation for the committed transactions and the undo operation for the active transactions. The redo operation restores the new value of the data item that was modified by the transaction. 

- **Restart recovery**: In this technique, the recovery scheme uses the log records and the checkpoints to restore the system to a consistent state after a failure. The recovery scheme performs two phases: analysis and redo/undo. In the analysis phase, the recovery scheme scans the log records from the most recent checkpoint and identifies the transactions that need to be redone or undone. In the redo/undo phase, the recovery scheme scans the log records from the beginning of the log and applies the redo or undo operation for each log record depending on the analysis phase. 

- **Concurrent recovery**: In this technique, the recovery scheme allows multiple recovery sessions to run concurrently and recover different media sets. A media set is a collection of backup objects that are stored on one or more media devices. Concurrent recovery can improve the performance and efficiency of the recovery process by using parallel device resources. Concurrent recovery requires coordination and synchronization among the recovery sessions to avoid conflicts and ensure consistency.



### Obtaining consistent Checkpoints for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Failure recovery in distributed systems is the process of restoring the system to a consistent and correct state after a failure occurs.
- A failure in a distributed system can be caused by various factors, such as hardware faults, software bugs, network errors, malicious attacks, power outages, etc.
- A failure can affect one or more components of the system, such as processes, messages, links, or nodes.
- A failure can have different consequences, such as data loss, data corruption, performance degradation, service unavailability, or inconsistency.
- To recover from a failure, the system needs to detect the failure, identify the cause and location of the failure, and restore the system to a consistent and correct state.
- One of the common techniques for failure recovery in distributed systems is checkpointing .
- Checkpointing is the process of periodically saving the state of the system or its components to a stable storage, such as a disk or a cloud service.
- Checkpointing can be done at different levels, such as process level, node level, or system level.
- Checkpointing can be done in different ways, such as synchronous, asynchronous, coordinated, or uncoordinated.
- Checkpointing can help the system to recover from a failure by restoring the system or its components to the last saved state, and then replaying the messages or events that occurred after the checkpoint.
- However, checkpointing also has some challenges, such as how to ensure the consistency of the checkpoints, how to minimize the overhead of checkpointing, how to coordinate the checkpointing among different components, and how to handle concurrent or cascading failures .
- To ensure the consistency of the checkpoints, the system needs to ensure that the checkpoints reflect a global state of the system that is reachable and valid.
- A global state of the system is a collection of the local states of all the components and the messages in transit among them.
- A global state is reachable if it can be obtained by executing the system from some initial state.
- A global state is valid if it does not violate any invariant or constraint of the system.
- To ensure the consistency of the checkpoints, the system can use different algorithms, such as the Chandy-Lamport algorithm, the Lai-Yang algorithm, or the Manetho algorithm.
- These algorithms use different mechanisms, such as message logging, message piggybacking, message ordering, or message vector clocks, to capture the global state of the system.
- To minimize the overhead of checkpointing, the system can use different strategies, such as incremental checkpointing, selective checkpointing, or adaptive checkpointing .
- Incremental checkpointing is the process of saving only the changes in the state since the last checkpoint, rather than the entire state.
- Selective checkpointing is the process of saving only the state of some components, rather than all the components, based on some criteria, such as the frequency of failure, the importance of the component, or the dependency among the components.
- Adaptive checkpointing is the process of adjusting the frequency or the granularity of the checkpointing based on some factors, such as the workload, the network condition, or the failure rate.
- To coordinate the checkpointing among different components, the system can use different protocols, such as centralized, decentralized, or hierarchical protocols.
- Centralized protocols use a single coordinator to initiate and control the checkpointing process among all the components.
- Decentralized protocols use a distributed agreement or a leader election algorithm to coordinate the checkpointing process among all the components.
- Hierarchical protocols use a tree structure or a cluster structure to divide the components into groups and coordinate the checkpointing process among the groups.
- To handle concurrent or cascading failures, the system can use different techniques, such as fault masking, fault tolerance, or fault isolation .
- Fault masking is the technique of hiding the failure from the users or the other components by providing an alternative service or a backup component.
- Fault tolerance is the technique of continuing the service despite the failure by using redundancy or replication[^5^



### Recovery in Distributed Database Systems

- Recovery in distributed database systems is the process of restoring the database to a consistent and correct state after a failure or an error .
- Recovery in distributed database systems aims to maintain the atomicity and durability of distributed transactions, which are transactions that span multiple sites or nodes in a distributed system.
- Recovery in distributed database systems is more complicated than in centralized database systems because failures can occur at the communication links or a remote site, and the system may not have a global view of the transaction status or the database state.
- Recovery in distributed database systems can be classified into two types: local recovery and global recovery .
  - Local recovery is the recovery of a single site or node after a failure, such as a disk crash or a power outage. Local recovery involves restoring a past copy of the database from a backup, and applying the undo and redo operations of the transactions that were affected by the failure.
  - Global recovery is the recovery of the entire distributed system after a failure, such as a network partition or a site crash. Global recovery involves coordinating the commit or abort decisions of the distributed transactions that were in progress at the time of the failure, and ensuring that all the sites agree on the final outcome of each transaction.
- Recovery in distributed database systems can use different techniques, such as:
  - Two-phase commit protocol (2PC), which is a protocol that ensures that all the sites involved in a distributed transaction either commit or abort the transaction as a unit. 2PC consists of two phases: a prepare phase, where the coordinator site asks the participant sites to vote on whether to commit or abort the transaction, and a commit phase, where the coordinator site decides the final outcome based on the votes and informs the participant sites .
  - Three-phase commit protocol (3PC), which is a protocol that improves the availability and fault-tolerance of 2PC by adding a pre-commit phase, where the coordinator site asks the participant sites to acknowledge the final outcome before committing or aborting the transaction. 3PC avoids the blocking problem of 2PC, where the participant sites may have to wait indefinitely for the coordinator site to recover from a failure.
  - Presumed abort protocol (PA), which is a protocol that optimizes the performance of 2PC by reducing the number of messages and disk writes required for commit or abort decisions. PA assumes that a transaction is aborted unless it is explicitly committed, and uses a log to record only the commit decisions. PA avoids the need to write a prepare record for each transaction, and to send an abort message for each aborted transaction.
  - Presumed commit protocol (PC), which is a protocol that optimizes the performance of 2PC by reducing the number of messages and disk writes required for commit or abort decisions. PC assumes that a transaction is committed unless it is explicitly aborted, and uses a log to record only the abort decisions. PC avoids the need to write a commit record for each transaction, and to send a commit message for each committed transaction.
  - Sagas, which are a technique that allows long-running distributed transactions to be executed as a sequence of smaller subtransactions, each of which can be committed or aborted independently. Sagas ensure the atomicity of the distributed transaction by providing a compensating action for each subtransaction, which is a reverse operation that can undo the effects of the subtransaction. Sagas avoid the blocking problem of 2PC and 3PC, and allow partial execution of the distributed transaction.



## Unit 7 - Fault Tolerance

- Fault tolerance is the property that enables a system to continue operating properly in the event of the failure of one or more faults within some of its components.
- The objective of creating a fault-tolerant system is to prevent disruptions arising from a single point of failure, ensuring the high availability and business continuity of the system.
- Fault tolerance can be achieved by using various techniques, such as redundancy, replication, backup, recovery, error detection and correction, etc.
- Fault tolerance can be classified into different levels, such as:
  - Active fault tolerance: The system detects and corrects faults without interrupting the normal operation.
  - Passive fault tolerance: The system switches to a backup or standby mode when a fault occurs, and resumes the normal operation after the fault is repaired or isolated.
  - Graceful degradation: The system reduces its functionality or performance in the presence of faults, but maintains the essential services.
  - Fail-safe: The system shuts down or enters a safe state when a fault occurs, to prevent further damage or harm.
- Fault tolerance can be applied to different aspects of a system, such as:
  - Hardware fault tolerance: The system uses redundant or resilient hardware components, such as processors, memory, disks, power supplies, etc., to tolerate hardware failures.
  - Software fault tolerance: The system uses redundant or resilient software components, such as processes, threads, modules, etc., to tolerate software failures.
  - Data fault tolerance: The system uses redundant or resilient data structures, such as databases, files, caches, etc., to tolerate data corruption or loss.
  - Network fault tolerance: The system uses redundant or resilient network components, such as routers, switches, links, etc., to tolerate network failures.
  - Human fault tolerance: The system uses redundant or resilient human operators, such as administrators, users, etc., to tolerate human errors or malicious actions.



### Issues in Fault Tolerance for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Fault tolerance is the ability of a system to continue functioning correctly in the presence of failures.
- Fault tolerance is important for distributed systems because they consist of multiple components that may be subject to different types of failures, such as hardware failures, software failures, network failures, malicious attacks, etc .
- Fault tolerance can be achieved by using various techniques, such as redundancy, replication, checkpointing, recovery, consensus, etc .
- Fault tolerance can be classified into different levels, such as detection, masking, tolerance, recovery, and prevention.
- Fault tolerance can also be categorized into different models, such as fail-stop, fail-silent, fail-safe, fail-recover, Byzantine, etc .
- Fault tolerance can be evaluated by using different metrics, such as reliability, availability, dependability, safety, etc .
- Fault tolerance can be implemented by using different algorithms, such as Paxos, Raft, Two-Phase Commit, Three-Phase Commit, etc .
- Fault tolerance can be challenged by various issues, such as scalability, consistency, latency, complexity, security, etc  .

: Fault Tolerance in Distributed Systems: A Survey - IEEE Xplore
: What is fault tolerance in distributed system - IT Release
: Fault Tolerance Mechanisms in Distributed Systems
: 13 - Fault Tolerance in Distributed Systems - Cambridge Core



### Commit Protocols

- Commit protocols are used to ensure the atomicity and durability of transactions in distributed systems.
- A transaction is a sequence of operations that must be executed as a unit, either completely or not at all.
- A commit protocol coordinates the actions of multiple processes that participate in a transaction, and decides whether to commit or abort the transaction.
- A commit protocol typically involves two phases: a prepare phase and a commit phase.
- In the prepare phase, each participant process votes to either commit or abort the transaction, based on its local state and the outcome of its operations.
- In the commit phase, a coordinator process collects the votes from the participants and decides the final outcome of the transaction, either commit or abort.
- The coordinator then informs the participants of the final outcome, and the participants either make their changes permanent or undo them, depending on the outcome.
- A commit protocol must satisfy the following properties:
  - Agreement: All participants agree on the same outcome of the transaction.
  - Validity: The outcome of the transaction is commit only if all participants voted to commit.
  - Termination: All participants eventually decide the outcome of the transaction.
  - Integrity: A transaction is executed at most once.
- There are different types of commit protocols, such as two-phase commit (2PC), three-phase commit (3PC), and consensus-based commit (CBC).
- Two-phase commit (2PC) is the simplest and most widely used commit protocol. It involves two phases: a prepare phase and a commit phase.
  - In the prepare phase, the coordinator sends a prepare message to all participants, asking them to vote on the transaction.
  - Each participant replies with a yes or no vote, depending on its local state and the outcome of its operations.
  - If the coordinator receives a yes vote from all participants, it decides to commit the transaction and sends a commit message to all participants.
  - If the coordinator receives a no vote from any participant, or does not receive a reply from some participant within a timeout, it decides to abort the transaction and sends an abort message to all participants.
  - In the commit phase, each participant receives the final outcome from the coordinator and either commits or aborts the transaction accordingly.
  - If a participant does not receive the final outcome from the coordinator within a timeout, it enters a blocked state and waits for the outcome from another participant or the coordinator.
- Two-phase commit (2PC) guarantees the agreement, validity, termination, and integrity properties, but it has some drawbacks, such as:
  - Blocking: If the coordinator or some participant fails or becomes unreachable, the protocol may block and prevent the completion of the transaction.
  - Single point of failure: The coordinator is a single point of failure, as it has the final authority to decide the outcome of the transaction.
  - High latency: The protocol requires two rounds of message exchange between the coordinator and the participants, which increases the latency of the transaction.
  - High overhead: The protocol requires the coordinator and the participants to maintain persistent logs of their states and actions, which increases the overhead of the transaction.
- Three-phase commit (3PC) is an extension of two-phase commit (2PC) that aims to overcome the blocking problem. It involves three phases: a prepare phase, a pre-commit phase, and a commit phase.
  - In the prepare phase, the coordinator sends a prepare message to all participants, asking them to vote on the transaction.
  - Each participant replies with a yes or no vote, depending on its local state and the outcome of its operations.
  - If the coordinator receives a yes vote from all participants, it decides to pre-commit the transaction and sends a pre-commit message to all participants.
  - If the coordinator receives a no vote from any participant, or does not receive a reply from some participant within a timeout, it decides to abort the transaction and sends an abort message to all participants.
  - In the pre-commit phase, each participant receives the pre-commit or abort outcome from the coordinator and either prepares to commit or aborts the transaction accordingly.
  - If a participant receives a pre-commit outcome, it sends an acknowledgement message to the coordinator and waits for the final commit outcome.
  - If a participant does not receive the pre-commit or abort outcome from the coordinator within a timeout, it enters a blocked state and waits for the outcome from another participant or the coordinator.
  - In the commit phase, the coordinator receives the acknowledgement messages from all participants and decides to commit the transaction and sends a commit message to all participants.
  - Each participant receives the final commit outcome from the coordinator and commits the transaction accordingly.
- Three-phase commit (3PC) guarantees the agreement, validity, termination, and integrity properties, but it has some drawbacks, such as:



### Voting protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Voting protocols are a type of consensus protocols that allow a set of distributed nodes to agree on a common value or decision, despite the presence of faults or attacks in the system  .
- Voting protocols are based on the idea of collecting votes from a majority or a quorum of nodes, and choosing the value that has the most votes as the consensus value .
- Voting protocols can be classified into two categories: exact voting and inexact voting  .
  - Exact voting requires that all nodes vote for the same value, and that the value is correct and consistent with the system state. Exact voting is typically used for atomic commit or distributed transactions, where the nodes need to agree on whether to commit or abort a transaction  .
  - Inexact voting allows for some nodes to vote for different values, and that the value may not be correct or consistent with the system state. Inexact voting is typically used for fault detection or fault masking, where the nodes need to agree on a value that can tolerate some errors or discrepancies  .
- Voting protocols can also be classified into two types: majority voting and weighted voting .
  - Majority voting assumes that all nodes have equal weight or reputation, and that the consensus value is the one that has more than half of the votes. Majority voting is simple and robust, but it requires a large number of nodes and a high degree of connectivity to achieve consensus .
  - Weighted voting assigns different weights or reputations to different nodes, and that the consensus value is the one that has the highest sum of weights. Weighted voting is more flexible and efficient, but it requires a fair and secure way of assigning and updating the weights of the nodes .
- Voting protocols face several challenges and trade-offs in distributed systems, such as  :
  - Fault tolerance: the ability to cope with node failures, network partitions, message losses, or message delays, and still reach consensus.
  - Security: the ability to resist malicious attacks, such as node impersonation, vote tampering, vote suppression, or vote fabrication, and still reach consensus.
  - Performance: the ability to reach consensus quickly, with low communication and computation overhead, and low latency and bandwidth consumption.
  - Scalability: the ability to reach consensus among a large number of nodes, with high diversity and dynamism, and low coordination and synchronization costs.
  - Fairness: the ability to ensure that all nodes have equal or proportional chances of influencing the consensus value, and that no node is unfairly favored or discriminated.



### Dynamic voting protocols

- Dynamic voting protocols are a technique for maintaining consistency and availability of replicated data in distributed systems  .
- The basic idea is to assign a weight or a number of votes to each replica of a data item, and to require a majority of votes to access or update the data item .
- The weight or the number of votes of each replica can be dynamically adjusted based on the availability, reliability, or performance of the replica or the network   .
- Dynamic voting protocols can improve the fault tolerance and the efficiency of distributed systems by allowing more flexible and adaptive access to replicated data   .
- Some examples of dynamic voting protocols are:
  - The dynamic weighted voting scheme proposed by Davcev  , which adjusts the weight of each replica based on the number of failures and the network partitioning.
  - The protocols for dynamic vote reassignment proposed by Gifford, which reassign votes to the surviving replicas upon node or link failure.
  - The topological dynamic voting algorithm proposed by Agrawal and Abbadi, which assigns votes to replicas based on their location in the network topology and their connectivity to other replicas.



## Unit 8 - Transactions and Concurrency Control

- A **transaction** is a logical unit of work that consists of a sequence of database operations, such as queries, updates, inserts, or deletes.
- A transaction has the following properties: **atomicity**, **consistency**, **isolation**, and **durability** (ACID).
- **Atomicity** means that either all the operations of a transaction are executed or none of them are. A transaction is treated as a single unit and cannot be divided into parts.
- **Consistency** means that a transaction preserves the integrity constraints of the database. A transaction cannot leave the database in an inconsistent state.
- **Isolation** means that a transaction is executed as if it is the only one running on the database. A transaction cannot see the intermediate results of other concurrent transactions.
- **Durability** means that the effects of a transaction are permanent and will not be lost in case of a system failure. A transaction is recorded in a persistent storage device before it is committed.
- A **concurrency control** mechanism is a set of rules and techniques that ensure the correct execution of concurrent transactions on a shared database. Concurrency control prevents data inconsistency and ensures serializability, recoverability, and deadlock-freedom of transactions.
- **Serializability** is the property that the concurrent execution of a set of transactions is equivalent to some serial execution of the same transactions. A serial execution is one in which transactions are executed one after another, without any overlap.
- **Recoverability** is the property that a transaction can be undone in case of a failure or an abort. A transaction is recoverable if it does not commit before all the transactions it depends on have committed.
- **Deadlock-freedom** is the property that a set of transactions will not enter a state in which they are waiting for each other to release some resources. A deadlock is a situation in which two or more transactions are blocked and cannot proceed because they are holding some resources that the other transactions need.
- There are different concurrency control methods, such as **locking**, **timestamping**, **validation**, and **multiversion**. Each method has its own advantages and disadvantages in terms of performance, complexity, and overhead.
- **Locking** is a method that uses locks to control the access of transactions to data items. A lock is a variable that indicates the status of a data item with respect to possible operations that can be applied to it. There are two types of locks: **shared** and **exclusive**. A shared lock allows a transaction to read a data item, but not to modify it. An exclusive lock allows a transaction to both read and write a data item, but not to share it with other transactions. A lock manager is a component that grants, denies, and releases locks according to a locking protocol, such as **two-phase locking** or **tree-protocol**.
- **Timestamping** is a method that assigns a unique timestamp to each transaction and uses these timestamps to order the transactions and determine their conflicts. A timestamp is a logical or physical value that indicates when a transaction started. There are two types of timestamping methods: **basic** and **conservative**. A basic timestamping method uses timestamps to validate the read and write operations of transactions and aborts any transaction that causes a conflict. A conservative timestamping method uses timestamps to assign a serial order to transactions and schedules them accordingly.
- **Validation** is a method that divides the execution of a transaction into three phases: **read**, **validate**, and **write**. In the read phase, a transaction reads the data items from the database and stores them in a private workspace. In the validate phase, a transaction checks whether it can commit without violating the serializability property. In the write phase, a transaction writes the updated data items from its workspace to the database. A validation method uses a validation test, such as **Thomas' write rule** or **backward-oriented** test, to determine the conflicts among transactions.
- **Multiversion** is a method that maintains multiple versions of each data item and allows transactions to access the appropriate version according to their timestamps. A multiversion method uses a version manager to create and store the versions of data items and a concurrency control manager to enforce the serializability property. A multiversion method can use different techniques, such as **multiversion timestamp ordering** or **multiversion two-phase locking**, to implement the concurrency control.



### Transactions
- A transaction is a logical unit of work that accesses and possibly modifies the data in a distributed system.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the operations of a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints of the data, such as uniqueness, referential integrity, etc.
- Isolation means that a transaction executes as if it were the only one in the system, without interference from other concurrent transactions.
- Durability means that the effects of a committed transaction are permanent and survive failures.
- A transaction can be in one of the following states: active, partially committed, committed, failed, or aborted.
- A transaction begins in the active state, where it executes its operations.
- A transaction enters the partially committed state when it issues a commit request, indicating that it has completed its operations successfully.
- A transaction enters the committed state when it receives a confirmation that its commit request has been processed and its effects are durable.
- A transaction enters the failed state when it encounters an error or a failure that prevents it from completing its operations.
- A transaction enters the aborted state when it is rolled back, undoing its effects and releasing any resources it acquired.
- A transaction can only transition from one state to another according to the following state diagram:

Transaction state diagram

- A transaction manager is a component of a distributed system that is responsible for coordinating the execution of transactions across multiple nodes.
- A transaction manager typically performs the following tasks:
  - Assigning unique identifiers to transactions and keeping track of their states.
  - Communicating with other transaction managers to ensure global atomicity and consistency of transactions.
  - Managing the concurrency control and recovery mechanisms for transactions.
  - Handling failures and aborts of transactions and ensuring their durability.



### Nested transactions for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A transaction is a unit of work that accesses and possibly modifies data in a database or a system.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- A distributed transaction is a transaction that accesses data from multiple servers or systems that are connected by a network.
- A nested transaction is a transaction that contains other transactions as subtransactions.
- A nested transaction can be used to improve the performance, modularity, and fault tolerance of distributed transactions.
- A nested transaction has the following characteristics :
  - It has a parent transaction and zero or more child transactions.
  - It can commit or abort independently of its parent or child transactions.
  - It can pass data to or receive data from its parent or child transactions.
  - It can be serialized with respect to other transactions using conflict serializability or other criteria.
  - It can be recovered using a two-phase commit protocol or other methods.
- A nested transaction can be classified into two types:
  - Closed nested transaction: A nested transaction that does not share any data with other transactions outside its nesting hierarchy.
  - Open nested transaction: A nested transaction that can share data with other transactions outside its nesting hierarchy.
- A nested transaction can be implemented using different models, such as:
  - Flat model: A nested transaction is treated as a single transaction by the servers or systems involved.
  - Hierarchical model: A nested transaction is treated as a hierarchy of transactions by the servers or systems involved, and each level of the hierarchy has its own coordinator and participants.
  - Multilevel model: A nested transaction is treated as a multilevel transaction by the servers or systems involved, and each level of the hierarchy can have multiple coordinators and participants.



### Locks for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- Locks are mechanisms that prevent concurrent transactions from accessing the same data item in a way that violates the ACID properties of transactions.
- Locks can be applied on different levels of granularity, such as records, pages, tables, or databases.
- Locks can be of different modes, such as shared (S), exclusive (X), or update (U). The lock compatibility matrix defines which lock modes can coexist on the same data item.
- Locks can be acquired and released by transactions according to different protocols, such as two-phase locking (2PL), timestamp ordering (TO), or optimistic concurrency control (OCC).
- Locks can be managed by a centralized or distributed lock manager, depending on the architecture of the distributed system.
- Locks can cause problems such as deadlocks, livelocks, starvation, or cascading aborts, which need to be detected and resolved by the concurrency control mechanism.



### Optimistic Concurrency Control for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- Optimistic concurrency control (OCC) is a concurrency control method applied to transactional systems such as relational database management systems and software transactional memory.
- OCC assumes that multiple transactions can frequently complete without interfering with each other, and avoids locking of data items that can reduce the performance of the system.
- OCC consists of three phases: read, validation and write.
  - In the read phase, the transaction reads the data items from the database and performs the necessary computations, but does not update the database.
  - In the validation phase, the transaction checks if any of the data items it has read have been modified by other transactions that committed after it started. If there is no conflict, the transaction can proceed to the write phase. Otherwise, the transaction is aborted and restarted.
  - In the write phase, the transaction updates the database with the new values of the data items it has modified.
- OCC has several advantages over locking-based concurrency control techniques:
  - It allows more concurrency, as transactions do not block each other by holding locks on data items.
  - It avoids deadlock, as transactions do not wait for locks to be released by other transactions.
  - It reduces the overhead of lock management, as transactions do not need to acquire and release locks on data items.
- OCC also has some disadvantages and challenges:
  - It may cause more aborts and restarts, as transactions may conflict with each other at the validation phase.
  - It may increase the complexity of the system, as transactions need to keep track of the data items they have read and modified, and the system needs to implement a validation mechanism.
  - It may not be suitable for applications that have high contention or low data availability, as transactions may have a low probability of passing the validation phase.
- OCC can be implemented in different ways, depending on how the validation phase is performed and how the data items are versioned:
  - Centralized OCC: The validation phase is performed by a central validator that maintains a global order of transactions and checks for conflicts among them.
  - Distributed OCC: The validation phase is performed by the transactions themselves, by contacting the sites that store the data items they have read or modified and checking for conflicts with other transactions.
  - Timestamp-based OCC: The data items are versioned by timestamps that indicate when they were last updated, and the transactions are assigned timestamps that indicate when they started. The validation phase is performed by comparing the timestamps of the data items and the transactions, and ensuring that the transactions have read the latest versions of the data items.



### Timestamp ordering for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- Timestamp ordering is a class of **optimistic** concurrency control protocols that assume that transaction conflicts are rare .
- Timestamp ordering does not require transactions to acquire locks before they are allowed to read or write to a database object .
- Timestamp ordering assigns a unique timestamp to each transaction based on the system clock or a logical counter .
- Timestamp ordering uses the timestamps to determine the serializability order of transactions, that is, the order in which the transactions appear to execute in a serial schedule  .
- Timestamp ordering ensures that if a transaction T1 has an earlier timestamp than another transaction T2, then T1 will appear before T2 in the serializability order.
- Timestamp ordering can be implemented using two methods: basic timestamp ordering and Thomas' write rule.
- Basic timestamp ordering ensures that any conflicting read or write operations are executed in timestamp order. If a transaction tries to read or write a data item that has a later timestamp, it is aborted and restarted with a new timestamp.
- Thomas' write rule allows a transaction to overwrite a data item with an earlier timestamp, as long as the overwritten value has not been read by any other transaction. This avoids unnecessary aborts and improves concurrency.
- Timestamp ordering can be applied in a distributed system, where each site has its own local clock or logical counter. However, the local timestamps are not globally unique and may cause conflicts or inconsistencies .
- To solve this problem, distributed timestamp ordering protocols use either global timestamps or local timestamps with additional information to ensure serializability and correctness .
- Global timestamps are generated by a centralized or distributed algorithm that synchronizes the clocks or counters of all the sites. Global timestamps are unique and consistent across the system, but they may incur communication and coordination overhead .
- Local timestamps are generated by each site independently, but they are accompanied by either a site identifier or a vector of timestamps from all the sites. Local timestamps are efficient and scalable, but they may require more storage and comparison operations .



### Comparison of methods for concurrency control

Concurrency control is the process of managing the concurrent access and modification of shared data in a distributed system, such as a distributed database. Concurrency control ensures that the data remains consistent and correct, and that the transactions that operate on the data preserve the ACID properties (atomicity, consistency, isolation, and durability).

There are various methods for concurrency control, each with its own advantages and disadvantages. Some of the common methods are:

- **Two-phase locking (2PL)**: This method uses locks to prevent conflicting operations on the same data item. A lock can be either shared (for read-only access) or exclusive (for read-write access). A transaction must acquire all the locks it needs before it can start executing, and release all the locks when it finishes. This ensures that no two transactions can access the same data item at the same time. However, this method can cause deadlock, where two or more transactions are waiting for each other to release locks, and thus cannot proceed. To avoid deadlock, a transaction can use a timeout mechanism, or a deadlock detection and resolution algorithm. 2PL can also cause blocking, where a transaction has to wait for a lock to be released by another transaction, and thus reduces concurrency. To improve concurrency, a transaction can use a lock escalation technique, where it acquires a lock on a larger granularity (such as a table or a page) instead of a smaller one (such as a record or a field).

- **Timestamp ordering (TO)**: This method assigns a unique timestamp to each transaction, and uses the timestamp to order the transactions. A transaction can only access a data item if its timestamp is greater than the timestamp of the last transaction that accessed the same data item. This ensures that the transactions are executed in a serializable order, which is equivalent to a sequential execution. However, this method can cause aborts, where a transaction has to be rolled back and restarted because it violates the timestamp ordering. To avoid aborts, a transaction can use a wait-die or a wound-wait technique, where it either waits for the conflicting transaction to finish, or aborts the conflicting transaction, depending on the relative timestamps.

- **Multi-version concurrency control (MVCC)**: This method maintains multiple versions of each data item, and assigns a timestamp to each version. A transaction can read the latest version of a data item that is older than its timestamp, and write a new version of a data item with its timestamp. This ensures that the transactions do not block each other, and can read consistent snapshots of the data. However, this method can cause write skew, where two transactions update different data items based on the same read data, and thus create an inconsistent state. To avoid write skew, a transaction can use a snapshot isolation technique, where it checks if the data items it read have been modified by other transactions before committing.

- **Validation concurrency control (VCC)**: This method divides the execution of a transaction into two phases: a read phase and a validation phase. In the read phase, a transaction reads the data items it needs, and records them in a private workspace. In the validation phase, a transaction checks if the data items it read have been modified by other transactions that committed in the meantime. If not, the transaction can commit and write its updates to the database. If yes, the transaction has to be aborted and restarted. This ensures that the transactions are executed in a serializable order, without using locks or timestamps. However, this method can cause high abort rates, where many transactions have to be restarted because they fail the validation. To reduce abort rates, a transaction can use a certification technique, where it sends its read set and write set to a central coordinator, and the coordinator decides if the transaction can commit or not.



## Unit 9 - Distributed Transactions

- A distributed transaction is a type of transaction that involves two or more network hosts, usually providing transactional resources, such as databases, message queues, file systems, etc.   
- A distributed transaction is coordinated by a transaction manager, which is responsible for creating and managing a global transaction that encompasses all the operations against the transactional resources.  
- A distributed transaction requires the following properties to ensure data consistency and reliability: atomicity, consistency, isolation, and durability (ACID). 
- Atomicity means that either all the operations in a distributed transaction are executed successfully, or none of them are. If any operation fails, the transaction manager should roll back the changes made by the previous operations. 
- Consistency means that a distributed transaction should preserve the integrity constraints and business rules of the data. The transaction manager should ensure that the data is in a valid state before and after the transaction. 
- Isolation means that a distributed transaction should not interfere with other concurrent transactions. The transaction manager should prevent the data from being accessed or modified by other transactions until the current transaction is committed or aborted. 
- Durability means that the effects of a committed distributed transaction should be permanent and resilient to failures. The transaction manager should ensure that the data is safely stored and replicated on the transactional resources. 
- A distributed transaction can be implemented using different protocols, such as two-phase commit (2PC), three-phase commit (3PC), or consensus algorithms (e.g., Paxos, Raft). These protocols aim to achieve agreement among the transactional resources and the transaction manager on the outcome of the transaction.  
- A distributed transaction faces various challenges, such as network latency, network partition, node failure, concurrency control, deadlock detection, and recovery. These challenges affect the performance, scalability, and availability of the distributed system.  
- A distributed transaction is a trade-off between consistency and availability. In some scenarios, such as online banking, e-commerce, or airline reservation, consistency is more important than availability, and a distributed transaction is necessary to ensure data integrity and reliability. In other scenarios, such as social media, online gaming, or streaming, availability is more important than consistency, and a distributed transaction may be too costly or impractical to implement.



### Flat and Nested Distributed Transactions

- A **flat or nested transaction** that accesses objects handled by different servers is referred to as a **distributed transaction** .
- When a distributed transaction reaches its end, in order to maintain the **atomicity** property of the transaction, it is mandatory that all of the servers involved in the transaction either **commit** the transaction or **abort** it .
- Distributed transactions can be structured in two different ways: **flat transactions** and **nested transactions** .
- A **flat transaction** has a single initiating point (**Begin**) and a single end point (**Commit** or **Abort**). They are usually very simple and are generally used for short activities rather than larger ones .
- A **nested transaction** is a transaction that consists of a number of **subtransactions**, each of which can be committed or aborted independently. A nested transaction has a **root transaction** and several **branch transactions**. The root transaction can only commit if all of its branch transactions have committed. Nested transactions are useful for complex and long-running activities that require partial results to be saved .
- The **distributed transaction** takes a **bottom-up** approach while the **nested transaction** takes a **top-down** approach to decompose a complex transaction into subtransactions. Distributed transactions provided global integrity constraints over multiple resources. These resources soon started to be heterogeneous as well.



### Atomic Commit Protocols for Distributed Transactions

- A distributed transaction is a transaction that involves multiple servers or nodes in a distributed system. A distributed transaction must satisfy the ACID properties, especially the atomicity property, which means that either all the operations of the transaction are executed or none of them are .
- An atomic commit protocol is a protocol that ensures the atomicity property of a distributed transaction, even if the system or some of the nodes fail or crash. An atomic commit protocol typically involves a coordinator node and multiple participant nodes that execute the operations of the transaction .
- The most common atomic commit protocol is the two-phase commit (2PC) protocol, which consists of two phases: the prepare phase and the commit phase. In the prepare phase, the coordinator asks the participants to vote on whether they are ready to commit or abort the transaction. In the commit phase, the coordinator decides on the final outcome of the transaction based on the votes and informs the participants to either commit or abort accordingly .
- The 2PC protocol has some drawbacks, such as blocking, high latency, and vulnerability to failures. Blocking means that if the coordinator or some of the participants fail or crash, the other nodes may have to wait indefinitely for the outcome of the transaction. High latency means that the 2PC protocol requires at least two rounds of communication between the coordinator and the participants, which can be costly in a distributed system. Vulnerability to failures means that the 2PC protocol may not be able to handle some failure scenarios, such as network partitions or concurrent failures .
- To overcome these drawbacks, some alternative atomic commit protocols have been proposed, such as the three-phase commit (3PC) protocol, the parallel commit protocol, and the failure-aware atomic commit (FLAC) protocol. The 3PC protocol adds a pre-commit phase between the prepare and the commit phases, which reduces the blocking problem but increases the latency and complexity. The parallel commit protocol eliminates the prepare phase and allows the participants to commit in parallel, which reduces the latency but requires stronger assumptions about the system. The FLAC protocol leverages the failure information of the nodes to optimize the commit decision, which reduces the blocking and latency problems but requires additional mechanisms to collect and disseminate the failure information .
- The choice of the atomic commit protocol depends on the trade-offs between the performance, reliability, and complexity of the distributed system. There is no single protocol that can achieve the optimal solution for all scenarios. Therefore, it is important to understand the advantages and disadvantages of each protocol and select the most suitable one for the specific application and environment .



### Concurrency control in distributed transactions

- Concurrency control is the process of ensuring that concurrent operations on a shared data do not violate the consistency and isolation properties of transactions.
- Distributed transactions are transactions that span multiple data servers that are connected by a network.
- Distributed concurrency control provides a mechanism to synchronize distributed transactions in such a way that the ACID properties are not violated by their interleaved execution .
- There are different types of distributed concurrency control algorithms, such as:
  - Locking-based algorithms, which use locks to prevent conflicting operations on the same data item.
  - Timestamp-based algorithms, which use timestamps to order the operations of different transactions and abort transactions that violate the order.
  - Optimistic algorithms, which assume that conflicts are rare and validate transactions at commit time.
  - Consensus-based algorithms, which use a voting protocol to coordinate the commit or abort of distributed transactions.
- The challenges of distributed concurrency control include:
  - Dealing with network delays, failures, and partitions, which may affect the communication and coordination of transactions.
  - Balancing the trade-offs between consistency, availability, and performance, which may depend on the application requirements and the characteristics of the data.
  - Handling the heterogeneity and scalability of the distributed system, which may involve different data models, protocols, and architectures.



### Distributed Deadlocks

- A distributed deadlock is a situation where a set of processes in a distributed system are waiting for each other to release resources or messages, and none of them can proceed  .
- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems .
- Distributed deadlocks are harder to detect, avoid, and prevent than deadlocks in centralized systems, because there is no single authority that can oversee resource allocation and monitor the state of the system.
- There are three main approaches to handle distributed deadlocks :
  - Prevention: This approach tries to prevent deadlocks from occurring by imposing some constraints on resource allocation, such as ordering the resources, granting requests only if they do not create cycles, or using timeouts.
  - Avoidance: This approach tries to avoid deadlocks by making dynamic decisions based on the current state of the system, such as using the banker's algorithm or the wait-die and wound-wait schemes.
  - Detection and resolution: This approach tries to detect deadlocks after they occur and then resolve them by aborting or restarting some of the processes involved in the deadlock.
- There are two main techniques for deadlock detection in distributed systems:
  - Global wait-for graph: This technique involves constructing a global wait-for graph (WFG) from local wait-for graphs at a deadlock detector, and then checking for cycles in the WFG. A WFG is a directed graph that represents the waiting relationships among processes and resources. A cycle in the WFG indicates a deadlock  .
  - Edge chasing: This technique involves sending probe messages along the edges of the local wait-for graphs, and then detecting cycles in the probe messages. A probe message contains the identity of the sender and the receiver, and the path of the message. A cycle in the probe messages indicates a deadlock .
- There are different types of distributed deadlocks, depending on the nature of the resources and the communication model:
  - Communication deadlocks: These are deadlocks that occur due to message passing among processes, where a process is waiting for a message from another process that is also waiting for a message from the first process or from a third process that is part of the cycle.
  - Resource deadlocks: These are deadlocks that occur due to shared resources among processes, where a process is waiting for a resource that is held by another process that is also waiting for a resource from the first process or from a third process that is part of the cycle.
  - Hybrid deadlocks: These are deadlocks that involve both communication and resource dependencies among processes.



### Transaction recovery for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database. A transaction must maintain the ACID properties: atomicity, consistency, isolation, and durability.
- A distributed transaction is a transaction that spans multiple sites or nodes in a distributed system. A distributed transaction may involve multiple subtransactions that execute at different sites and coordinate their results to commit or abort the transaction.
- Transaction recovery is the process of restoring the database to a consistent state after a failure. Transaction recovery ensures the atomicity and durability of transactions, by undoing the effects of incomplete or aborted transactions, and redoing the effects of committed transactions that may have been lost due to failure.
- Transaction recovery in a distributed system is more challenging than in a centralized system, because of the possibility of partial failures, network partitions, and communication delays. Some of the issues that need to be addressed are:
  - How to detect and handle failures of sites, subtransactions, or communication links.
  - How to coordinate the commit or abort decision among all the sites involved in a transaction.
  - How to maintain a consistent and durable log of the transaction history across multiple sites.
  - How to recover the database state at each site after a failure, and ensure the global consistency of the database.
- There are different techniques and protocols for transaction recovery in a distributed system, such as:
  - Two-phase commit (2PC): A protocol that ensures the atomicity of a distributed transaction by using a coordinator site and participant sites. The coordinator initiates the commit process by sending a prepare message to all the participants, and waits for their votes. If all the participants vote yes, the coordinator sends a commit message to all of them, and the transaction commits. If any participant votes no, or fails to respond, the coordinator sends an abort message to all of them, and the transaction aborts. The coordinator and the participants use a log to record their actions and decisions, and use the log to recover in case of failure.
  - Three-phase commit (3PC): A protocol that improves the availability and fault-tolerance of 2PC by adding a pre-commit phase. The coordinator initiates the commit process by sending a can-commit message to all the participants, and waits for their responses. If all the participants respond yes, the coordinator sends a pre-commit message to all of them, and waits for their acknowledgments. If all the participants acknowledge, the coordinator sends a do-commit message to all of them, and the transaction commits. If any participant responds no, fails to respond, or fails to acknowledge, the coordinator sends an abort message to all of them, and the transaction aborts. The coordinator and the participants use a log to record their actions and decisions, and use the log to recover in case of failure.
  - Presumed abort (PA): An optimization of 2PC that reduces the logging overhead by assuming that a transaction aborts unless it is explicitly committed. The coordinator initiates the commit process by sending a prepare message to all the participants, and waits for their votes. If all the participants vote yes, the coordinator sends a commit message to all of them, and logs the commit decision. The transaction commits, and the participants delete their logs. If any participant votes no, or fails to respond, the coordinator does not log anything, and the transaction aborts. The coordinator and the participants use the log to recover in case of failure.
  - Presumed commit (PC): An optimization of 2PC that reduces the logging overhead by assuming that a transaction commits unless it is explicitly aborted. The coordinator initiates the commit process by sending a prepare message to all the participants, and logs the prepare decision. The coordinator waits for the votes of the participants. If all the participants vote yes, the coordinator deletes its log, and sends a commit message to all of them. The transaction commits, and the participants delete their logs. If any participant votes no, or fails to respond, the coordinator sends an abort message to all of them, and logs the abort decision. The transaction aborts. The coordinator and the participants use the log to recover in case of failure.



## Unit 10 - Replication

- Replication is a biological process of duplicating or producing an exact copy, such as a polynucleotide strand (DNA) .
- DNA replication is one of the most vital biological processes in all living things. It is a molecular process taking place in dividing cells by which the DNA creates a copy of itself .
- Replication is also a term used to describe the duplication of a laboratory or experimental procedure, which is essential for research statistics .
- Replication can be classified into two types: biological replicates and technical replicates .
  - Biological replicates are parallel measurements of biologically distinct samples that capture random biological variation, which can be a subject of study or a source of noise itself .
  - Biological replicates are important because they address how widely your experimental results can be generalized .
  - Technical replicates are repeated measurements of the same sample that capture random technical variation, such as measurement error or instrument noise .
  - Technical replicates are important because they assess the precision and reliability of your experimental method .
- The molecular mechanism of DNA replication involves several steps and enzymes .
  - Helicase opens up the DNA at the replication fork .
  - Single-strand binding proteins coat the DNA around the replication fork to prevent rewinding of the DNA .
  - Topoisomerase works at the region ahead of the replication fork to prevent supercoiling .
  - Primase synthesizes a short RNA primer that provides a 3' end for DNA polymerase to start from .
  - DNA polymerase adds nucleotides to the 3' end of the primer, following the template strand .
  - DNA polymerase can only work in the 5' to 3' direction, so it replicates the leading strand continuously and the lagging strand discontinuously .
  - The lagging strand is synthesized in short fragments called Okazaki fragments, each with its own primer .
  - DNA ligase joins the Okazaki fragments together to form a continuous strand .
  - The RNA primers are removed by another DNA polymerase and replaced with DNA nucleotides .
  - The result is two identical DNA molecules, each with one original strand and one new strand . This is called semi-conservative replication .



### System model and group communication for replication in distributed systems

- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by exchanging messages.
- Replication is a technique to create and maintain multiple copies of the same data or service on different processes, for the purposes of fault tolerance, availability, performance, or scalability.
- A system model is a set of assumptions and properties that describe the behavior and characteristics of a distributed system, such as the communication model, the failure model, the timing model, and the consistency model.
- Group communication is a form of communication between multiple processes in a distributed system, where a group is a logical collection of processes that share some common interest or goal .
- Group communication can be classified into two types: broadcast communication and multicast communication.
  - Broadcast communication is when a source process sends a message to all the processes in the system, regardless of their group membership.
  - Multicast communication is when a source process sends a message to a subset of processes that belong to a specific group .
- Group communication can also be characterized by the reliability and ordering guarantees that it provides, such as best-effort, reliable, causal, total, or atomic.
  - Best-effort delivery means that the system tries to deliver the message to the destination processes, but there is no guarantee that it will succeed.
  - Reliable delivery means that the system guarantees that every message sent by a correct process will be eventually delivered to every correct process in the group.
  - Causal delivery means that the system guarantees that every message that causally depends on another message will be delivered after that message.
  - Total delivery means that the system guarantees that every message will be delivered to all the processes in the same order.
  - Atomic delivery means that the system guarantees that every message will be delivered to all the processes or none of them.
- Group communication is useful for implementing replication in distributed systems, as it allows the processes to coordinate their actions and maintain consistency among their replicas .
  - For example, a database cluster can use multicast to replicate the data among the nodes, and use a consensus protocol to agree on the order of the transactions.
  - Another example is a distributed file system that can use broadcast to propagate the updates to the files among the servers, and use a version vector to detect and resolve conflicts.



### Fault-tolerant services for the notes of the Unit 10 - Replication in the subject of DISTRIBUTED SYSTEM

- Fault-tolerant services are services that can continue to function correctly even in the presence of failures, such as server crashes, network partitions, or malicious attacks.
- Replication is a technique for implementing fault-tolerant services by creating and maintaining multiple copies of the same service (or object) on different servers in a distributed system.
- Replication can improve availability, performance, and reliability of services, but also introduces challenges such as consistency, concurrency, and communication overhead.
- The correctness criterion for replicated services is linearizability, which means that every operation on the service appears to take effect atomically at some point between its invocation and response, and that the order of operations is consistent with the real-time order of invocations.
- There are two main classes of replication techniques: primary-backup replication and active replication.
  - Primary-backup replication assigns one server as the primary and the others as backups. The primary executes the operations and sends updates to the backups. The backups apply the updates in the same order as the primary. If the primary fails, one of the backups takes over as the new primary.
  - Active replication assigns all servers as active replicas. The clients send requests to all replicas, and the replicas execute the operations and send responses to the clients. The replicas use a consensus protocol to agree on the order of operations. If some replicas fail, the others can still provide the service.
- There are trade-offs between primary-backup replication and active replication in terms of performance, communication, and fault-tolerance. Primary-backup replication requires less communication and can tolerate more failures, but has lower performance and higher latency. Active replication requires more communication and can tolerate fewer failures, but has higher performance and lower latency.



### Highly Available Services for the Notes of the Unit 10 - Replication in the Subject of Distributed System

- One of the potential benefits of distributed systems is their use in providing **highly-available services** that are likely to be usable when needed.
- **Availability** is the probability that a service is operational at a given time.
- **Replication** is the technique of maintaining multiple copies of data or services on different nodes in a distributed system, to increase availability, reliability, and performance.
- Replication can be classified into two types: **eager replication** and **lazy replication**.
  - **Eager replication** ensures that all replicas are updated synchronously, as soon as an update occurs. This guarantees **strong consistency** among replicas, but it is expensive and may introduce delays or failures.
  - **Lazy replication** allows replicas to be updated asynchronously, after an update occurs. This improves **availability** and **performance**, but it may lead to **inconsistency** among replicas, which needs to be resolved later.
- There are different methods to implement replication in distributed systems, such as **primary copy**, **quorum-based**, **gossip-based**, and **operational transformation**     .
  - **Primary copy** assigns a single replica as the primary, which receives all update requests and propagates them to other replicas. This ensures **consistency**, but it introduces a **single point of failure** and a **performance bottleneck** .
  - **Quorum-based** requires a minimum number of replicas to agree on an update before it is committed. This allows **fault tolerance** and **load balancing**, but it may increase **communication overhead** and **latency**.
  - **Gossip-based** disseminates updates randomly among replicas, using a probabilistic protocol. This achieves **scalability** and **robustness**, but it may result in **eventual consistency** and **redundant messages**.
  - **Operational transformation** applies updates as operations that can be transformed to maintain **consistency** and **convergence** among replicas, even if they are applied in different orders. This enables **collaboration** and **conflict resolution**, but it may require **complex algorithms** and **metadata** .



### Transactions with replicated data

- Transactions are a sequence of operations that are executed atomically, consistently, isolatedly, and durably (ACID properties) on a database system.
- Replication is a technique to distribute data from a source server to other servers while keeping the data updated and synced with the source.
- Transactions with replicated data are transactions that involve data items that are stored on multiple servers and need to be coordinated to ensure consistency and correctness.
- Transactions with replicated data can improve availability, performance, and fault-tolerance of distributed systems, but also introduce challenges such as concurrency control, recovery, and commit protocols.
- Some of the issues and solutions for transactions with replicated data are:

  - Concurrency control: how to ensure serializability and isolation of transactions that access replicated data items on different servers?
    - One solution is to use a primary copy approach, where one server is designated as the primary server for each data item and is responsible for locking and validating transactions that access that item.
    - Another solution is to use a majority consensus approach, where each server maintains a version number for each data item and transactions need to obtain a majority of votes from the servers to commit.
  - Recovery: how to ensure durability and atomicity of transactions that update replicated data items on different servers?
    - One solution is to use a two-phase commit protocol, where a coordinator server initiates the commit process and collects the votes from the participating servers, and then sends a final decision (commit or abort) to all the servers.
    - Another solution is to use a three-phase commit protocol, where a coordinator server adds a pre-commit phase before the final decision to avoid blocking in case of failures.
  - Commit protocols: how to ensure consistency and correctness of transactions that span across multiple servers or databases?
    - One solution is to use a distributed transaction manager, which coordinates the commit process among the servers or databases using a two-phase commit protocol or a variant of it.
    - Another solution is to use an elastic database transaction, which is a feature of Azure SQL Database that allows transactions to span across multiple databases in the same region using a two-phase commit protocol.

