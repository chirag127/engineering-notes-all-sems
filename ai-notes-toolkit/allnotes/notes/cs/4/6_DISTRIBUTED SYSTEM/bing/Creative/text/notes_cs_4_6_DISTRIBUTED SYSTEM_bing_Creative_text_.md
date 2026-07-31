

## Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- The main characteristics of distributed systems are:
  - Concurrency: Multiple components can execute simultaneously and interact with each other.
  - No global clock: There is no shared physical clock among the components, so synchronization and coordination are challenging.
  - Independent failures: Each component can fail independently, without affecting the rest of the system.
  - Heterogeneity: The components can have different hardware, software, network, and data formats.
- The main advantages of distributed systems are:
  - Scalability: The system can grow in size and performance by adding more components.
  - Availability: The system can tolerate failures and provide continuous service.
  - Fault tolerance: The system can recover from errors and resume normal operation.
  - Transparency: The system can hide its complexity and heterogeneity from the users and provide a consistent interface.
- The main challenges of distributed systems are:
  - Communication: The system has to deal with network delays, failures, and bandwidth limitations.
  - Consistency: The system has to ensure that the data and state of the components are coherent and up-to-date.
  - Replication: The system has to manage multiple copies of data and components for performance and availability.
  - Security: The system has to protect the data and components from unauthorized access and malicious attacks.
  - Naming: The system has to provide a way to identify and locate the components and resources in the system.



Hello, I am Sydney, your AI assistant. I can help you with writing content in markdown format. Here is the content I have generated for the topic of ### Introduction for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM:

### Introduction

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- The main challenges of designing and implementing a distributed system are:
  - Heterogeneity: The system should be able to cope with different hardware, software, network, and data formats.
  - Scalability: The system should be able to perform well as the number of users, resources, or geographic locations increases.
  - Fault tolerance: The system should be able to continue functioning despite failures of components or communication links.
  - Security: The system should be able to protect the data and resources from unauthorized access, modification, or disclosure.
  - Transparency: The system should hide the complexity and diversity of its components and interactions from the users and applications.
- The main benefits of using a distributed system are:
  - Resource sharing: The system can enable the access and utilization of remote resources, such as files, printers, sensors, or services.
  - Performance: The system can improve the speed and efficiency of computation by exploiting parallelism and load balancing.
  - Reliability: The system can increase the availability and durability of data and services by replicating them across multiple nodes.
  - Flexibility: The system can adapt to changing requirements and environments by adding, removing, or reconfiguring components.
- The main examples of distributed systems are:
  - The Internet: A global network of interconnected networks that provides various services, such as web, email, or DNS.
  - The World Wide Web: A distributed hypermedia system that allows users to access and link information across the Internet using browsers and servers.
  - Cloud computing: A model of providing on-demand access to a shared pool of computing resources, such as servers, storage, or applications, over the Internet.
  - Peer-to-peer systems: A class of systems that rely on the direct communication and collaboration of peers, rather than centralized servers, to provide services, such as file sharing, streaming, or social networking.
  - Distributed databases: A collection of databases that are physically distributed across multiple sites, but logically appear as a single database to the users and applications.
  - Distributed operating systems: A layer of software that provides the abstraction of a single system image to the users and applications of a distributed system.



### Examples of Distributed Systems

A distributed system is a collection of independent computers that communicate and coordinate their actions by passing messages. The computers in a distributed system may be physically close or geographically dispersed, and they may be connected by a network or a bus. The main advantages of distributed systems are scalability, fault tolerance, resource sharing, and performance.

Some examples of distributed systems are:

- **Telecommunication networks**: Telephone networks are an early example of a peer-to-peer network, where each node can initiate or receive calls. Cellular and telephone networks are forms and examples of distributed networks. They use protocols such as TCP/IP, HTTP, and SMTP to exchange data and messages.  
- **Real-time systems**: Many industries use real-time systems distributed in various areas, locally and globally. For example, air traffic control systems, power grid systems, industrial control systems, and online gaming systems are all examples of real-time distributed systems. They require high reliability, availability, and responsiveness. They use protocols such as RTP, RTCP, and MQTT to ensure timely and accurate delivery of data and commands.  
- **Distributed database systems**: A distributed database has locations across multiple servers, physical locations, or both. The data is replicated or partitioned to improve availability, performance, and scalability. For example, Google's Bigtable, Amazon's DynamoDB, and MongoDB are all examples of distributed database systems. They use protocols such as Paxos, Raft, and Gossip to ensure consistency and fault tolerance.  
- **Distributed computing platforms**: A distributed computing platform is a system that allows multiple computers to work together on a common task or problem. For example, MapReduce, Spark, and Hadoop are examples of distributed computing platforms that enable large-scale data processing and analysis. They use protocols such as RPC, RMI, and REST to invoke remote procedures and services.  
- **Content delivery networks**: A content delivery network (CDN) is a system that distributes web content to users based on their geographic location, network conditions, and content type. For example, Akamai, Cloudflare, and Netflix are examples of CDNs that provide fast and reliable delivery of web pages, videos, and images. They use protocols such as DNS, HTTP, and HTTPS to route and cache content.



### Resource sharing for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Resource sharing is one of the main goals and benefits of distributed systems, which are systems that consist of multiple independent computers that communicate and coordinate their actions by passing messages.
- Resource sharing can be classified into two types: sharing of hardware resources and sharing of software resources.
- Hardware resources are physical devices or components that can be accessed or used by multiple computers, such as printers, scanners, disks, sensors, etc.
- Software resources are logical entities or data that can be accessed or used by multiple computers, such as files, databases, web pages, services, etc.
- Resource sharing can be achieved by different methods, such as:
  - Remote access: a computer requests access to a resource that is located on another computer, and the request is forwarded to the resource owner, who grants or denies the access. For example, a computer can access a file on a remote server using a protocol such as FTP or HTTP.
  - Replication: a resource is copied or duplicated on multiple computers, and each copy can be accessed or used independently. For example, a web page can be replicated on multiple servers using a protocol such as DNS or CDN.
  - Migration: a resource is moved or transferred from one computer to another, and the original location is no longer available. For example, a process can migrate from one node to another in a cluster using a protocol such as MPI or RMI.
  - Distribution: a resource is split or divided into multiple parts or chunks, and each part is located on a different computer. For example, a file can be distributed on multiple disks using a protocol such as RAID or HDFS.



### The Web Challenges for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- The web is an example of a distributed system that allows resource sharing and communication among different devices across the internet.
- However, the web also poses several challenges for the design and implementation of distributed systems, such as    :
  - Scalability: The ability to handle increasing load and demand without degrading the performance or functionality of the system. This requires efficient algorithms, protocols, and architectures that can cope with large numbers of users, requests, and data.
  - Heterogeneity: The diversity of devices, platforms, languages, and formats that are involved in the web. This requires interoperability, compatibility, and standardization among different components and interfaces of the system.
  - Security: The protection of the system and its users from unauthorized access, modification, or damage. This requires authentication, authorization, encryption, and integrity mechanisms that can prevent or detect attacks and ensure privacy and availability.
  - Fault tolerance: The ability to recover from failures and errors that may occur in the system or its components. This requires redundancy, replication, and consensus protocols that can ensure reliability and consistency of the system.
  - Transparency: The hiding of the complexity and diversity of the system from the users and applications. This requires abstraction, encapsulation, and naming services that can provide a simple and uniform view of the system.



### Architectural models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Architectural models are a type of system model that describe the organization of components across the network and their interrelationship .
- Architectural models can help to design, implement, and evaluate distributed systems by providing a high-level view of the system structure and behavior.
- Architectural models can also help to identify the challenges and trade-offs involved in distributed computing, such as scalability, reliability, performance, security, and consistency.
- Some common architectural models for distributed systems are  :
  - **Client-server architecture**: A model where one or more servers provide services to multiple clients that request and consume them. The servers and clients can be distributed across different machines and communicate over a network. The servers can be specialized for different types of services, such as web servers, database servers, or file servers. The clients can be thin (relying mostly on the server) or thick (having more processing power and functionality). This model is widely used for web applications, email systems, and online banking.
  - **Multi-tier architecture**: A model where the client-server architecture is extended to have multiple layers or tiers of servers that perform different functions. For example, a three-tier architecture can have a presentation tier (for user interface), a business logic tier (for application logic), and a data tier (for data storage and access). The tiers can be distributed across different machines and communicate over a network. This model can improve scalability, modularity, and security of the system by separating the concerns and responsibilities of each tier.
  - **Broker architecture**: A model where a broker component acts as an intermediary between clients and servers, facilitating the communication and coordination among them. The broker can provide services such as naming, location, discovery, routing, load balancing, and security. The broker can be centralized or distributed, and can be implemented using standards such as CORBA, Jini, or RMI. This model can simplify the development and deployment of distributed systems by hiding the complexity and heterogeneity of the network and the components.
  - **Service-oriented architecture (SOA)**: A model where the system is composed of loosely coupled and interoperable services that provide functionality and data to other services or clients. The services can be distributed across different machines and communicate over a network using standard protocols such as SOAP, REST, or XML-RPC. The services can be discovered and composed dynamically using registries such as UDDI or WSDL. This model can increase the reusability, flexibility, and adaptability of the system by enabling the integration and orchestration of different services.
  - **Peer-to-peer architecture**: A model where the system is composed of autonomous and equal peers that cooperate and share resources without relying on a central authority or server. The peers can be distributed across different machines and communicate over a network using protocols such as Gnutella, BitTorrent, or Chord. The peers can provide services such as file sharing, content distribution, distributed computing, or social networking. This model can enhance the scalability, reliability, and fault tolerance of the system by exploiting the redundancy and diversity of the peers.



### Fundamental Models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Fundamental models are descriptions of properties that are present in all distributed architectures  .
- They help us to understand the characteristics, challenges and trade-offs of designing and implementing distributed systems.
- There are three main types of fundamental models: interaction models, failure models and security models  .

#### Interaction Models
- Interaction models deal with the issues of communication and coordination among processes in a distributed system  .
- They include aspects such as performance, timing, ordering, consistency and synchronization of events  .
- Some examples of interaction models are:
  - Synchronous vs. asynchronous communication: whether the sender and receiver of a message have to wait for each other or not  .
  - Remote procedure call (RPC): a method of invoking a procedure or function on a remote machine as if it were local  .
  - Message passing interface (MPI): a standard for parallel programming that supports point-to-point and collective communication among processes  .
  - Publish/subscribe: a pattern of communication where publishers send messages to a broker or a topic, and subscribers receive messages that match their interests  .

#### Failure Models
- Failure models specify the types of faults that can occur in a distributed system and how they affect the processes and communication channels  .
- They help us to design fault-tolerant and resilient distributed systems that can cope with failures and recover from them  .
- Some examples of failure models are:
  - Crash failure: a process stops executing and does not resume  .
  - Omission failure: a process fails to send or receive a message  .
  - Timing failure: a process does not meet the timing constraints of the system  .
  - Byzantine failure: a process behaves arbitrarily or maliciously, sending incorrect or conflicting messages  .

#### Security Models
- Security models describe the threats and attacks that can compromise the confidentiality, integrity and availability of a distributed system and the countermeasures that can be applied to prevent or mitigate them  .
- They include aspects such as authentication, authorization, encryption, digital signatures, firewalls and intrusion detection  .
- Some examples of security models are:
  - Kerberos: a protocol for authenticating users and services in a distributed system using tickets and keys  .
  - Public key infrastructure (PKI): a system for managing public keys and certificates for encryption and digital signatures  .
  - Secure sockets layer (SSL) / transport layer security (TLS): a protocol for securing the communication between a client and a server using encryption and certificates  .
  - Blockchain: a distributed ledger that records transactions in a secure and verifiable way using cryptography and consensus  .



### Theoretical Foundation for Distributed System

- A distributed system is a collection of processes that are spatially separated and do not share a common memory and communicate with one another by exchanging messages with arbitrary delays .
- Theoretical foundation for distributed system aims to understand the inherent limitations, challenges and possibilities of such systems, and to design efficient and reliable algorithms and protocols for solving various problems in distributed settings  .
- Some of the key concepts and topics in the theoretical foundation for distributed system are  :
  - Limitation of distributed system: due to the lack of global clock, shared memory, and reliable communication, distributed systems face issues such as uncertainty, inconsistency, concurrency, and fault-tolerance.
  - Logical clocks: a mechanism to order events and messages in a distributed system without relying on physical clocks, proposed by Lamport. A logical clock is a function that assigns a logical timestamp to each event, such that if event A causally precedes event B, then the timestamp of A is smaller than the timestamp of B.
  - Vector clocks: an extension of logical clocks that can capture the partial order of events in a distributed system, proposed by Fidge and Mattern. A vector clock is a vector of logical clocks, one for each process, that is updated and piggybacked on each message. A vector clock can determine the causal relationship between any two events by comparing their vector timestamps.
  - Message passing system: a model of distributed computation where processes communicate by sending and receiving messages through channels. A message passing system can be characterized by various properties, such as synchrony, reliability, ordering, and topology.



### Limitation of Distributed system

A distributed system is a system that consists of multiple independent components that communicate with each other over a network. Distributed systems have many advantages, such as scalability, fault-tolerance, availability, and performance. However, they also face some limitations that make them challenging to design and implement. Some of the main limitations of distributed systems are:

- **Absence of a global state**: In a distributed system, there is no single point of control or coordination for the entire system. Each component has its own local state and view of the system, which may differ from the views of other components. This makes it difficult to reason about the behavior and correctness of the system, and to synchronize the actions and data of different components. For example, it is hard to ensure consistency and atomicity of transactions that span multiple components, or to detect and resolve conflicts and failures that may occur in the system.

- **Absence of a global clock**: In a distributed system, there is no common notion of time or ordering of events for the entire system. Each component has its own local clock, which may drift or be inaccurate. This makes it hard to measure and compare the timestamps and durations of events that happen in different components, and to establish causal relationships and dependencies among them. For example, it is hard to implement concurrency control and deadlock detection mechanisms that rely on timestamps or logical clocks, or to ensure that messages are delivered and processed in the same order as they were sent.

- **Network latency and unreliability**: In a distributed system, the communication between components is subject to delays and failures that are caused by the network. The network may be slow, congested, partitioned, or disrupted by external factors. This makes it hard to guarantee the timeliness and reliability of the communication, and to handle the errors and exceptions that may arise. For example, it is hard to implement synchronous and blocking communication protocols that require acknowledgments and timeouts, or to ensure that messages are delivered exactly once and not duplicated or lost.

- **Security and privacy issues**: In a distributed system, the components and the network may be exposed to malicious attacks and unauthorized access by external or internal adversaries. The adversaries may try to compromise the confidentiality, integrity, or availability of the system, or to disrupt its normal operation. This makes it hard to protect the system and its data from unauthorized modification, disclosure, or deletion, and to detect and prevent the attacks and intrusions that may occur. For example, it is hard to implement authentication and authorization mechanisms that verify the identity and permissions of the components and the users, or to encrypt and decrypt the messages and data that are exchanged in the system.



### Absence of Global Clock

- A global clock is a system-wide clock that is equally accessible to all processes in a distributed system and provides a common notion of time.
- A global clock is useful for determining the order of events, synchronizing processes, and obtaining a consistent state of the system.
- However, a global clock is hard to realize in distributed systems due to two inherent limitations: lack of shared memory and unpredictable message delays.
- Lack of shared memory means that processes in a distributed system do not have access to a common storage that can store and update the global clock value.
- Unpredictable message delays mean that the communication channel between processes is unreliable and may introduce variable and unknown delays in message transmission.
- As a result, processes in a distributed system may have different and inaccurate views of the global clock value, and the notion of common time does not exist.
- Therefore, distributed systems have to rely on other mechanisms, such as logical clocks, vector clocks, or Lamport timestamps, to order events and capture causality.



### Shared Memory

Shared memory is a programming model for distributed systems that allows multiple processes to access a common logical address space, as if they were running on a single machine. Shared memory can simplify the communication and synchronization among processes, and enable the implementation of parallel algorithms and data structures.

There are two types of shared memory models: physical and virtual.

- Physical shared memory: The processes share the same physical memory, such as in a multiprocessor system. The hardware ensures the coherence and consistency of the shared data, by using mechanisms such as cache coherence protocols and memory barriers. Physical shared memory is fast and transparent, but it is limited by the scalability and availability of the hardware.

- Virtual shared memory: The processes do not share the same physical memory, but they have a common view of a virtual memory, which is mapped to their local memories. This is also known as distributed shared memory (DSM). The software ensures the coherence and consistency of the shared data, by using mechanisms such as page-based, object-based, or tuple-based approaches. Virtual shared memory is more scalable and fault-tolerant, but it is slower and less transparent than physical shared memory.

Some advantages of shared memory are:

- It provides a simple and familiar abstraction for programmers, who do not need to deal with low-level details of message passing or remote procedure calls.
- It allows the reuse of existing sequential or parallel code, libraries, and tools that are designed for the shared memory model.
- It can exploit the locality and parallelism of the processes, by allowing them to access the shared data without network delays or serialization overheads.

Some disadvantages of shared memory are:

- It can introduce performance and scalability issues, due to the overhead of maintaining the coherence and consistency of the shared data, especially in a distributed system.
- It can introduce correctness and security issues, due to the possibility of data races, deadlocks, or unauthorized access to the shared data, especially in a concurrent or distributed system.
- It can introduce portability and compatibility issues, due to the diversity of the hardware and software platforms that support different types of shared memory models and mechanisms.



### Logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A logical clock is a mechanism for capturing chronological and causal relationships in a distributed system  .
- A distributed system may have no physically synchronous global clock, so a logical clock allows global ordering on events from different processes in such systems .
- A logical clock is not a physical device, but a software counter that is incremented according to some rules .
- Logical clocks are useful in computation analysis, distributed algorithm design, individual event tracking, and exploring computational progress.
- Some noteworthy logical clock algorithms are:
  - Lamport timestamps, which are monotonically increasing software counters that are updated based on the send and receive events of messages .
  - Vector clocks, which are arrays of software counters that are updated based on the send, receive, and local events of processes .
  - Matrix clocks, which are matrices of software counters that are updated based on the send, receive, and local events of processes and also capture the concurrency of events.
- Logical clocks can provide a partial or total ordering of events in a distributed system, depending on the algorithm used .
- Logical clocks can also be used to implement other distributed system concepts, such as mutual exclusion, deadlock detection, snapshot, and causal broadcast .



### Lamport's logical clocks

- Lamport's logical clocks are a way of ordering events in a distributed system without relying on physical clocks.
- Lamport's logical clocks are based on the idea of a **happens-before** relation, denoted by `->`, which captures the causal order of events.
- If `a` and `b` are events on the same process, then `a -> b` if `a` occurs before `b` based on the local clock.
- If `a` is the event of sending a message by one process and `b` is the event of receiving that message by another process, then `a -> b`.
- The happens-before relation is transitive, meaning that if `a -> b` and `b -> c`, then `a -> c`.
- Lamport's logical clocks assign a numerical value, called a **timestamp**, to each event that reflects its position in the happens-before order.
- A timestamp is a software counter that is maintained by each process and incremented before each event.
- When a process sends a message, it attaches its current timestamp to the message.
- When a process receives a message, it updates its timestamp to be the maximum of its own timestamp and the timestamp of the message, and then increments it by one.
- Lamport's logical clocks ensure that if `a -> b`, then the timestamp of `a` is less than the timestamp of `b`.
- However, the converse is not true, meaning that if the timestamp of `a` is less than the timestamp of `b`, it does not imply that `a -> b`.
- Therefore, Lamport's logical clocks can only partially order events, and they cannot distinguish between concurrent events, i.e., events that are not causally related.
- Lamport's logical clocks are simple and easy to implement, but they have some limitations, such as:
  - They do not reflect the real time of events, only their logical order.
  - They do not provide a total order of events, only a partial order.
  - They do not capture the causal dependencies between events on different processes, only between events on the same process or between send and receive events.
  - They may assign different timestamps to events that are logically equivalent, such as two processes sending messages to each other at the same time.



### Concepts in Message Passing Systems

- Message passing is a technique for invoking behavior (i.e., running a program) on a computer.
- In message-passing systems, processors communicate with one another by sending and receiving messages over a communication channel.
- The pattern of the connection provided by the channel is described by some topology systems.
- The collection of the channels are called a network.
- A message-passing system gives a collection of message-based IPC protocols while sheltering programmers from the complexities of sophisticated network protocols and many heterogeneous platforms.
- A message-passing mechanism can be used in a distributed system for the following two forms of inter-process communication:
  - Local communication, where the communicating processes are located on the same node.
  - Distant communication, in which the communication activities are distributed among multiple nodes.
- A distributed system consists of multiple components, possibly across geographical boundaries, that communicate and coordinate their actions through message passing.
- To an actor outside this system, it appears as if a single coherent system.
- The formal model for distributed message passing has two timing models:
  - Synchronous, where there are known bounds on the message transmission delays and the relative speeds of the processors.
  - Asynchronous, where there are no such bounds and the processors may operate at arbitrary speeds.



### Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems in the Subject of Distributed System

- Causal order is a way of ordering events in a distributed system based on their causal relationships, rather than their physical timestamps or locations.
- Causal order captures the intuitive notion of "happened before" or "influenced by" among events in a distributed system, where events can be messages, actions, or state changes.
- Causal order is important for ensuring consistency, correctness, and coordination in distributed systems, especially when dealing with concurrency, replication, and fault tolerance.
- Causal order can be defined formally using Lamport's logical clocks, which assign logical timestamps to events such that if event A causally precedes event B, then the timestamp of A is less than the timestamp of B.
- Causal order can also be implemented using vector clocks, which are arrays of logical clocks that track the causal dependencies among processes in a distributed system.
- Causal order can be enforced using various protocols, such as causal broadcast, causal multicast, or causal delivery, which ensure that messages are delivered to processes in a way that respects their causal order.
- Causal order is a weaker form of ordering than total order, which imposes a single linear order on all events in a distributed system, regardless of their causal relationships. Total order is more strict and synchronous, but also more expensive and less scalable than causal order.
- Causal order is a stronger form of ordering than unordered or FIFO order, which do not guarantee any relationship among events in a distributed system, except for their arrival order at a process. Unordered or FIFO order are more simple and efficient, but also more prone to inconsistency and ambiguity than causal order.



### Total Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent entities that communicate by message passing and coordinate their actions to achieve a common goal.
- A distributed system is said to have partial order if we can have a partial order relationship among the events in the system. An event is something that happens at a single point in time and space, such as sending or receiving a message, or changing a local state.
- A partial order relationship is defined by the "happened before" relation, denoted by ->, which captures the causal dependencies between events. For example, if a process sends a message and another process receives it, then the send event happened before the receive event.
- A distributed system is said to have total order if 'totality', i.e., causal relationship among all events in the system, can be established, then the system is said to have total order. This means that for any two events in the system, either one happened before the other, or they are concurrent.
- Total order is useful for ensuring consistency and agreement among the entities in a distributed system, especially when dealing with shared resources, replicated data, or fault tolerance  .
- Total order can be implemented by using logical clocks, such as Lamport timestamps or vector clocks, which assign a unique and monotonically increasing value to each event in the system . These values can be used to compare and order events according to their causal relationships .
- Total order can also be implemented by using atomic broadcast, which is a communication primitive that guarantees that all entities in a distributed system receive the same messages in the same order. Atomic broadcast can be achieved by using consensus algorithms, such as Paxos or Raft, which ensure that all entities agree on a single value or sequence of values.



### Total Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems in the Subject of Distributed System

- A distributed system is a collection of independent processes that communicate by exchanging messages over a network.
- Events are actions or occurrences that happen in a process, such as sending or receiving a message, executing a statement, or changing a state variable.
- The order of events in a distributed system is important for ensuring the correctness and consistency of the system's behavior and state.
- A partial order is a relation that defines a precedence among some events, but not all. For example, if event A happens before event B in the same process, then A is partially ordered before B. However, if event C happens in a different process, then there is no partial order between A and C or B and C.
- A causal order is a relation that defines a precedence among events that are causally related, meaning that one event influences or depends on another. For example, if event A causes event B, then A is causally ordered before B. Causality can be inferred from the message passing between processes. If process P sends a message m to process Q, and Q receives m before sending another message n to process R, then m is causally ordered before n.
- A total order is a relation that defines a precedence among all events in the system, regardless of their causal relationship. For example, if event A happens before event B in the global clock of the system, then A is totally ordered before B. A total order is a linearization of the partial order, meaning that it preserves the precedence of the partially ordered events and assigns an order to the concurrent events.
- A total causal order is a relation that defines a precedence among all events in the system, consistent with the causal order. For example, if event A causes event B, and event C is concurrent with both A and B, then a total causal order can be either A-B-C or C-A-B, but not A-C-B or B-A-C. A total causal order is a linearization of the causal order, meaning that it preserves the precedence of the causally ordered events and assigns an order to the concurrent events.
- A total causal order is the strictest ordering in distributed systems, as it establishes only one linearization among all the events that occur in the system. For that reason, the execution of the system is considered as synchronous, meaning that all processes agree on the order of events .
- A total causal order can be implemented by using a logical clock, such as a vector clock, that assigns a timestamp to each event, reflecting its causal dependencies. A vector clock is an array of integers, one for each process, that is incremented by one when a process executes an event, and updated with the maximum of its own and the sender's values when a process receives a message. A vector clock can capture the causal order of events, as well as their concurrency. Two events are causally ordered if their vector clocks are ordered lexicographically, meaning that one vector clock has smaller or equal values in all positions and a smaller value in at least one position than the other vector clock. Two events are concurrent if their vector clocks are incomparable, meaning that neither vector clock is lexicographically smaller than the other. A total causal order can be achieved by breaking the ties among concurrent events using some deterministic rule, such as the process identifier .



### Techniques for Message Ordering for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Message ordering is the order of delivering the messages to the intended recipients in a distributed system .
- Message ordering is important for ensuring the consistency and correctness of the actions and outcomes in a distributed system.
- Message ordering can be affected by various factors, such as transmission delay, network congestion, system failure, and message routing.
- There are different types of message ordering techniques, depending on the desired properties and guarantees of the communication paradigm  . Some of the common techniques are:

  - **First in First out (FIFO)**: This technique ensures that the messages sent by a process are delivered in the same order as they were sent . For example, if process A sends messages m1, m2, and m3 to process B, then B will receive them in the order m1, m2, and m3. This technique can be implemented by using sequence numbers for each message and buffering the out-of-order messages until the previous ones are delivered.
  - **Non-FIFO**: This technique does not guarantee any specific order of message delivery. The messages can be delivered in any order, depending on the network conditions and the message routing algorithm . For example, if process A sends messages m1, m2, and m3 to process B, then B can receive them in any order, such as m2, m1, m3 or m3, m2, m1. This technique is the simplest and the most efficient, but it may not be suitable for some applications that require a certain order of message delivery.
  - **Causal order**: This technique ensures that the messages that are causally related are delivered in the same order as they were sent  . Two messages are causally related if one message depends on the occurrence or the content of the other message. For example, if process A sends message m1 to process B, and then B sends message m2 to process C, then m1 and m2 are causally related. Causal order guarantees that if process A sends another message m3 to process C, then C will receive m2 before m3, because m2 is causally related to m1, which was sent before m3. This technique can be implemented by using vector clocks or logical clocks to capture the causal dependencies among the messages and to compare their timestamps.
  - **Synchronous order**: This technique ensures that the messages sent to a group of processes are delivered in the same order to all the processes in the group  . This technique is also known as total order or atomic order. For example, if process A sends messages m1, m2, and m3 to a group of processes B, C, and D, then synchronous order guarantees that all the processes in the group will receive the messages in the same order, such as m1, m2, m3 or m3, m2, m1. This technique can be implemented by using a sequencer process or a consensus algorithm to assign a global sequence number to each message and to coordinate the delivery order among the processes in the group.

- Message ordering techniques can be combined to provide different levels of ordering guarantees for different scenarios and applications. For example, FIFO and causal order can be combined to provide FIFO-causal order, which ensures that the messages sent by a process are delivered in FIFO order and the messages that are causally related are delivered in causal order. Similarly, causal and synchronous order can be combined to provide causal-synchronous order, which ensures that the messages sent to a group of processes are delivered in causal order and in the same order to all the processes in the group.



### Causal ordering of messages

- Causal ordering of messages is a partial ordering of messages in a distributed computing environment .
- It places a restriction on communication between processes by requiring that if the transmission of message mi to process pk necessarily preceded the transmission of message mj to the same process, then the delivery of these messages to that process must be ordered such that mi is delivered before mj .
- Causal ordering of messages is one of the four semantics of multicast communication, namely unordered, totally ordered, causal, and sync-ordered communication.
- Multicast communication methods vary according to the message’s reliability guarantee and ordering guarantee.
- Causal ordering of messages is based on the concept of potential causality, which is defined by the Lamport's happened-before relation .
- The Lamport's happened-before relation states that if event A happens before event B in the same process, or if event A is the sending of a message and event B is the receipt of that message, then A -> B.
- Causal ordering of messages ensures that if A -> B, then A cannot possibly have caused B, and therefore A and B can be executed concurrently.
- Causal ordering of messages can be implemented by using vector clocks, which are arrays of logical clocks that keep track of the causal dependencies among events in a distributed system .
- Vector clocks can be used to label each message with a vector timestamp that reflects the causal history of the message .
- A process can deliver a message only if its vector timestamp is less than or equal to the current vector clock of the process .
- Causal ordering of messages can be useful for applications that require consistency and concurrency control, such as collaborative editing, distributed databases, and replicated state machines .



### Global State for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent processes that communicate through message passing.
- The global state of a distributed system is the union of the local states of the individual processes and the channels.
- A local state of a process is the values of its variables, registers, program counter, etc. at a given point in time.
- A channel state is the set of messages that have been sent but not yet received by the processes.
- The global state of a distributed system may change due to the occurrence of events, such as local computation, message sending, or message receiving.
- A global state is consistent if it reflects a possible execution of the system, i.e., it does not contain any causal anomaly.
- A causal anomaly is a violation of the causal order of events, such as a message being received before it is sent, or a process observing the effect of an event before the cause.
- A consistent global state can be computed along a consistent cut, which is a partition of the set of events into past and future such that no message is received in the past from the future.
- A consistent cut can be determined by using distributed snapshot algorithms, which are protocols that allow the processes to record their local states and the channel states in a coordinated way.
- Distributed snapshot algorithms can be classified into two categories: uncoordinated and coordinated.
- Uncoordinated algorithms do not require any synchronization among the processes, but they may record inconsistent global states. An example of an uncoordinated algorithm is the Chandy-Lamport algorithm.
- Coordinated algorithms ensure that the recorded global state is consistent, but they may incur more overhead and delay. An example of a coordinated algorithm is the Lai-Yang algorithm.
- The global state of a distributed system can be used for various purposes, such as debugging, checkpointing, recovery, termination detection, deadlock detection, etc.



### Termination Detection

Termination detection is a fundamental problem in distributed systems, where a set of processes cooperate to perform a computation. The goal is to determine if the computation has finished, i.e., if all the processes are idle and there are no messages in transit. Termination detection is useful for many applications, such as garbage collection, deadlock detection, load balancing, etc.

One of the most well-known algorithms for termination detection is Huang's algorithm, proposed by Shing-Tsaan Huang in 1989. The algorithm is based on the concept of a distributed snapshot, which captures a consistent global state of the system. The algorithm works as follows:

- Each process maintains a local counter that records the number of messages it has sent and received. The difference between these two numbers is called the **weight** of the process. A positive weight means that the process has sent more messages than it has received, and vice versa. The sum of the weights of all the processes is called the **global weight** of the system, which is invariant throughout the execution.
- The algorithm uses a special process called the **controller**, which initiates and coordinates the termination detection. The controller can be any process in the system, or a separate process that communicates with the others. The controller also maintains a local counter that records the number of messages it has sent and received.
- The algorithm consists of two phases: the **snapshot phase** and the **diffusion phase**. In the snapshot phase, the controller initiates a distributed snapshot to collect the weights of all the processes. In the diffusion phase, the controller propagates the result of the snapshot to all the processes, and each process adjusts its weight accordingly.
- The snapshot phase works as follows:
  - The controller sends a **marker** message to itself and to all its neighbors. The marker message contains the weight of the controller at the time of sending. The controller also records its own weight as the **local snapshot**.
  - When a process receives a marker message for the first time, it records its own weight as the local snapshot, and sends a marker message with its weight to all its neighbors. It also starts recording the weights of the messages it receives from each neighbor, until it receives a marker message from that neighbor. The sum of these weights is called the **channel snapshot** for that neighbor.
  - When a process receives a marker message from a neighbor, it subtracts the weight of the message from the channel snapshot for that neighbor. If the process has received a marker message from all its neighbors, it computes the **partial snapshot** as the sum of its local snapshot and all its channel snapshots. It then sends the partial snapshot to the controller and enters the diffusion phase.
- The diffusion phase works as follows:
  - When the controller receives the partial snapshots from all the processes, it computes the global snapshot as the sum of all the partial snapshots and its own local snapshot. The global snapshot is equal to the global weight of the system at the time of the snapshot initiation. The controller then sends a **result** message to all the processes, containing the global snapshot and a **termination flag** that indicates whether the global snapshot is zero or not. A zero global snapshot means that the computation has terminated, and a non-zero global snapshot means that the computation is still ongoing.
  - When a process receives a result message, it adjusts its weight by subtracting the global snapshot from its local snapshot. It then sets its termination flag to the same value as the result message. If the termination flag is true, the process declares termination and stops participating in the computation. If the termination flag is false, the process continues the computation and waits for the next snapshot initiation.

The algorithm guarantees that if the computation has terminated, the global snapshot will eventually be zero, and all the processes will declare termination. The algorithm also preserves the global weight of the system, and does not interfere with the computation. The algorithm requires O(n) messages per snapshot, where n is the number of processes in the system. The algorithm can be initiated by the controller at any time, or periodically, or based on some condition. The algorithm can also be modified to handle failures and dynamic topology changes.



## Unit 2 - Distributed Mutual Exclusion

- Distributed mutual exclusion is a fundamental problem in distributed computing systems  .
- It ensures that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner  .
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion. Message passing is the sole means for implementing distributed mutual exclusion .
- There are three basic approaches for implementing distributed mutual exclusion:
  - Token-based algorithms: A process can enter the critical section only if it possesses a unique token. The token is passed among the processes in a predefined order or by request.
  - Permission-based algorithms: A process can enter the critical section only if it obtains permission from all or a subset of other processes in the system. The process sends a request message to other processes and waits for their replies.
  - Quorum-based algorithms: A process can enter the critical section only if it obtains permission from a majority or a quorum of processes in the system. The process sends a request message to a subset of processes and waits for their replies.
- The performance of distributed mutual exclusion algorithms can be measured by the following metrics :
  - Message complexity: The number of messages exchanged per critical section entry.
  - Synchronization delay: The time elapsed between the instant a process becomes the head of the queue and the instant it enters the critical section.
  - System throughput: The number of times the critical section is executed per unit time.
  - Fault tolerance: The ability of the algorithm to handle failures of processes or communication links.



### Classification of distributed mutual exclusion

- Distributed mutual exclusion is a problem of ensuring that only one process can access a shared resource or data at a time in a distributed system.
- Distributed mutual exclusion algorithms are solutions that use message passing to coordinate the access of processes to the shared resource or data.
- Distributed mutual exclusion algorithms can be classified into three basic approaches: token-based, non-token-based, and quorum-based.

#### Token-based approach

- In this approach, a unique token is shared among the sites or processes in the system.
- A site or process can enter its critical section (CS) only if it possesses the token.
- Mutual exclusion is ensured because the token is unique and only one site or process can have it at a time.
- The token is passed from one site or process to another according to some protocol or rule.
- Examples of token-based algorithms are: Suzuki-Kasami algorithm, Raymond's algorithm, and Maekawa's algorithm.

#### Non-token-based approach

- In this approach, a site or process does not need a token to enter its CS.
- Instead, a site or process requests permission from other sites or processes in the system before entering its CS.
- Mutual exclusion is ensured by the agreement of the other sites or processes on granting or denying the permission.
- The request and permission messages are exchanged according to some protocol or rule.
- Examples of non-token-based algorithms are: Ricart-Agrawala algorithm, Lamport's algorithm, and Singhal's algorithm.

#### Quorum-based approach

- In this approach, a site or process does not need a token or permission from all the other sites or processes in the system to enter its CS.
- Instead, a site or process requests permission from a subset of sites or processes in the system, called a quorum, before entering its CS.
- Mutual exclusion is ensured by the intersection of the quorums, that is, any two quorums have at least one common site or process.
- The request and permission messages are exchanged according to some protocol or rule.
- Examples of quorum-based algorithms are: Majority voting algorithm, Tree-based algorithm, and Grid-based algorithm.



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
- The mutual exclusion theorem states that any algorithm that solves the mutual exclusion problem in a distributed system must satisfy the following four properties:
  - Safety: At most one process can execute in the critical section at any time.
  - Liveness: If a process requests to enter the critical section, it will eventually be granted permission.
  - Fairness: No process is indefinitely postponed or starved from entering the critical section.
  - Fault-tolerance: The algorithm can tolerate failures of some processes or messages without violating the safety property.



### Token based and non token based algorithms for distributed mutual exclusion

Distributed mutual exclusion (DME) is the problem of ensuring that only one process at a time can access a shared resource in a distributed system. There are two main types of algorithms for DME: token based and non token based.

- Token based algorithms
  - In token based algorithms, a unique token is shared among all the processes in the system. The token represents the permission to enter the critical section. Only the process that holds the token can access the shared resource. The token is passed from one process to another according to some protocol.
  - Token based algorithms have the advantage of being simple and efficient, as they do not require any communication among processes except for passing the token. They also avoid the problem of deadlock, as there is always a unique token in the system. However, they have some drawbacks, such as the possibility of losing the token due to failures, the overhead of token passing, and the lack of fairness, as some processes may have to wait for a long time to get the token.
  - Examples of token based algorithms are the Raymond's algorithm, the Suzuki-Kasami algorithm, and the Maekawa's algorithm.
- Non token based algorithms
  - In non token based algorithms, there is no token in the system. Instead, the processes communicate with each other using messages to request and grant permission to enter the critical section. The processes use some criteria, such as timestamps or logical clocks, to order the requests and resolve conflicts.
  - Non token based algorithms have the advantage of being more robust to failures, as they do not depend on a single token. They also allow for more flexibility and fairness, as the processes can choose whom to grant permission based on some policy. However, they have some drawbacks, such as the complexity and overhead of message exchange, the possibility of deadlock, and the need for synchronization among processes.
  - Examples of non token based algorithms are the Ricart-Agrawala algorithm, the Lamport's algorithm, and the Singhal's algorithm.



### Performance metric for distributed mutual exclusion algorithms

Distributed mutual exclusion algorithms are protocols that allow processes in a distributed system to access a shared resource or a critical section without violating the mutual exclusion property, i.e., at most one process can be in the critical section at any time.

The performance of distributed mutual exclusion algorithms can be evaluated by the following four metrics :

- **Message complexity**: It is the number of messages that are required per critical section execution by a process. It measures the communication overhead and the network bandwidth consumption of the algorithm. A lower message complexity is desirable for better performance.
- **Synchronization delay**: It is the time elapsed between the departure of a process from the critical section and the entry of the next process into the critical section. It measures the degree of concurrency and fairness of the algorithm. A lower synchronization delay is desirable for better performance.
- **Response time**: It is the time elapsed between the request of a process to enter the critical section and the actual entry of the process into the critical section. It measures the waiting time and the latency of the algorithm. A lower response time is desirable for better performance.
- **Throughput**: It is the number of critical section executions per unit time in the system. It measures the efficiency and the utilization of the shared resource or the critical section. A higher throughput is desirable for better performance.

Different types of distributed mutual exclusion algorithms, such as centralized, decentralized, token-based, or quorum-based, can have different values of these metrics depending on the system size, the network topology, the request rate, and the critical section duration. A simulation-based approach can be used to compare the performance of different algorithms under various scenarios and parameters .



## Unit 3 - Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set.
- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems.
- Deadlock detection in distributed systems entails addressing two basic issues: detection of existing deadlocks and resolution of detected deadlocks.
- Deadlock detection requires examination of the status of process-resource interactions for presence of cyclic wait.
- There are three approaches to detect deadlocks in distributed systems: global wait-for graph, edge chasing, and probe-based.
- Global wait-for graph: A deadlock detector collects local wait-for graphs from all sites and constructs a global wait-for graph. A cycle in the global wait-for graph indicates a deadlock.
- Edge chasing: A deadlock detector initiates a probe message along the edges of the local wait-for graph. A probe message that returns to the initiator indicates a deadlock.
- Probe-based: A deadlock detector periodically sends a probe message to each process. A process that receives a probe message replies with its status and forwards the message to its successor. A deadlock is detected if a process does not reply or if a probe message is lost.
- To resolve a deadlock, one or more deadlocked processes have to be aborted. The selection of processes to abort can be based on criteria such as priority, cost, or rollback distance.



### System Model for Distributed Deadlock Detection

- A distributed system consists of a set of nodes that communicate by message passing.
- Each node has a set of resources that can be requested by processes running on the node or on other nodes.
- A process can request a resource by sending a message to the node that owns the resource.
- A node can grant a resource to a process by sending a message to the process or by placing the resource in a shared buffer.
- A process can release a resource by sending a message to the node that owns the resource or by removing the resource from a shared buffer.
- A process can hold multiple resources at a time and can request additional resources while holding some resources.
- A process can wait for a resource if the resource is not available or if the node that owns the resource is busy or unreachable.
- A deadlock occurs when a set of processes are waiting for resources that are held by other processes in the set, and none of the processes can proceed or release any resources.
- A distributed deadlock detection algorithm is a method to detect and resolve deadlocks in a distributed system.
- A distributed deadlock detection algorithm can be classified into three categories: centralized, hierarchical, and distributed.
- A centralized deadlock detection algorithm assigns a single node as the deadlock detector, which collects information from all other nodes and constructs a global wait-for graph to detect cycles.
- A hierarchical deadlock detection algorithm divides the nodes into clusters, and assigns a node in each cluster as the cluster controller, which collects information from the nodes in the cluster and constructs a local wait-for graph. The cluster controllers communicate with each other to construct a global wait-for graph and detect cycles.
- A distributed deadlock detection algorithm does not assign any node as the deadlock detector, but instead relies on the cooperation of all nodes to exchange information and detect cycles. A distributed deadlock detection algorithm can use either edge chasing or probe-based techniques.
- Edge chasing is a technique where a node initiates a deadlock detection by sending a probe message along the edges of the wait-for graph, and the probe message returns to the initiator if a cycle is detected.
- Probe-based is a technique where a node periodically sends a probe message to all its neighbors, and the probe message collects information about the resources and processes along the way, and returns to the initiator with the information. The initiator then analyzes the information to detect cycles.



### Resource Vs Communication Deadlocks

- A deadlock is a condition where a process cannot proceed because it needs to obtain a resource held by another process, and it itself is holding a resource that the other process needs.
- There are two types of deadlocks in distributed systems: resource deadlocks and communication deadlocks.
- Resource deadlocks occur when processes access resources, such as data objects in database systems and buffers in store and forward communication networks . A process acquires a resource before accessing it and releases it after using it. A resource deadlock can happen if four conditions are met: mutual exclusion, hold and wait, no preemption, and circular wait.
- Communication deadlocks occur when processes exchange messages, such as in message passing systems and distributed algorithms . A process sends a message to another process and waits for a reply. A communication deadlock can happen if there is a cycle of processes waiting for messages from each other.
- The main difference between resource deadlocks and communication deadlocks is that resource deadlocks involve contention for resources, while communication deadlocks involve loss or corruption of messages . Resource deadlocks can be prevented by avoiding one of the four conditions, while communication deadlocks can be prevented by using timeouts, acknowledgments, or retries .



### Deadlock Prevention for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

- A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
- Deadlock prevention is a technique to ensure that at least one of the necessary conditions for deadlock does not hold in a system.
- In a distributed system, deadlock prevention is more challenging than in a centralized system, because the processes and resources may be located in different nodes and there is no global information or control.
- There are two main approaches to deadlock prevention in a distributed system: ordered request and collective request.

#### Ordered Request
- In this approach, each resource type is assigned a unique level, and a process can request resources only in increasing order of levels.
- This ensures that no circular wait can occur, as a process that has a resource of level i cannot request a resource of level j < i.
- For example, if there are three resource types A, B, and C with levels 1, 2, and 3 respectively, a process can request A, then B, then C, but not C, then A, then B.
- This approach requires a global agreement on the levels of the resource types, and may impose unnecessary restrictions on the processes.

#### Collective Request
- In this approach, a process must request all the resources it needs at the same time, before starting its execution.
- This ensures that no hold and wait can occur, as a process that has some resources cannot request more resources later.
- For example, if a process needs resources A, B, and C, it must request them all together, and not request A, then B, then C.
- This approach requires a global knowledge of the resource requirements of the processes, and may cause underutilization of the resources.



### Avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- Deadlock avoidance is a technique that tries to prevent a deadlock from occurring by ensuring that the system is always in a safe state, where there is at least one possible sequence of resource allocation that does not lead to a deadlock .
- However, deadlock avoidance is impractical in distributed systems due to several problems, such as :
  - The lack of global information about the current state of the system and the future requests of the processes.
  - The high communication and synchronization overhead involved in maintaining and updating the global state.
  - The possibility of inconsistent and outdated information due to network delays and failures.
  - The difficulty of predicting the future behavior of the processes and the resources.
- Therefore, deadlock detection is preferred over deadlock avoidance in distributed systems, as it allows more concurrency and flexibility in resource allocation .
- Deadlock detection involves examining the status of the process-resource interactions for the presence of a cyclic wait, which indicates a deadlock .
- Deadlock detection algorithms in distributed systems can be classified into four categories :
  - Path-pushing algorithms, which propagate the information about the dependency paths along the wait-for graph.
  - Edge-chasing algorithms, which send probe messages along the dependency cycles in the wait-for graph.
  - Diffusion computation algorithms, which initiate a distributed computation at each node to detect a deadlock.
  - Global state detection algorithms, which collect the global state of the system and check for a deadlock using a centralized or distributed algorithm.



### Detection and Resolution of Distributed Deadlocks

- A distributed deadlock is a situation where a set of processes in a distributed system are waiting for each other to release resources or messages, and none of them can proceed.
- Detection and resolution of distributed deadlocks involve two steps: first, identifying the existence of deadlocks in the system, and second, breaking the cycles of dependency among the deadlocked processes.
- Detection of distributed deadlocks can be done by maintaining and searching a global wait-for graph (WFG), which is a directed graph that represents the dependency relationships among the processes and resources in the system.
- There are three main approaches to maintain and search the WFG: centralized, distributed, and hierarchical.
  - Centralized approach: One designated node, called the coordinator, is responsible for collecting the local WFG information from all the nodes, constructing the global WFG, and searching it for cycles. This approach is simple and efficient, but it has a single point of failure and a high communication overhead.
  - Distributed approach: Each node maintains its own local WFG and periodically exchanges it with its neighbors. Each node also runs a cycle detection algorithm on its local WFG and initiates a probe message to check the status of other nodes in the cycle. This approach is fault-tolerant and scalable, but it may detect false or phantom deadlocks due to inconsistent or outdated information.
  - Hierarchical approach: The nodes are organized into a tree structure, where each node maintains a local WFG for its subtree and sends it to its parent node. The root node constructs and searches the global WFG and notifies the nodes involved in a deadlock. This approach is a compromise between the centralized and distributed approaches, but it may suffer from high latency and load imbalance.
- Resolution of distributed deadlocks can be done by aborting or preempting some of the deadlocked processes and releasing their resources or messages to the blocked processes. There are various criteria to select which processes to abort or preempt, such as priority, age, number of resources, number of messages, etc. The goal is to minimize the cost of resolution and maximize the system performance.



### Centralized Deadlock Detection

- This is a technique used in distributed systems to handle deadlock detection.
- According to this technique, the system maintains one global wait-for graph in a single chosen site, which is named as deadlock-detection coordinator.
- The coordinator collects information about the local wait-for graphs of all the sites and constructs the global wait-for graph.
- The coordinator periodically runs a deadlock detection algorithm on the global wait-for graph to identify any cycles.
- If a cycle is detected, the coordinator selects one or more processes to abort and sends a message to the corresponding sites to terminate them.
- The advantages of this technique are simplicity and low communication overhead.
- The disadvantages of this technique are single point of failure, scalability issues, and lack of autonomy.

: https://www.exploredatabase.com/2014/06/centralized-deadlock-detection-approach-in-distributed-database.html
: https://www.javatpoint.com/deadlock-detection-in-distributed-systems
: https://people.cs.rutgers.edu/~pxk/417/notes/deadlock.html
: https://www.geeksforgeeks.org/deadlock-detection-in-distributed-systems/



### Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set.
- Deadlocks can occur in distributed systems when distributed transactions or concurrency control are used.
- Deadlock detection is the approach of identifying and resolving existing deadlocks in the system.
- Deadlock detection in distributed systems entails two basic issues:
  - Detection of existing deadlocks
  - Resolution of detected deadlocks
- Deadlock detection requires examination of the status of process-resource interactions for presence of cyclic wait.
- Deadlock detection in distributed systems can be done using three approaches:
  - Centralized approach: A single node is designated as the deadlock detector and collects information from all other nodes to construct a global wait-for graph (WFG) and detect cycles.
  - Hierarchical approach: The nodes are organized into a hierarchy of clusters and each cluster has a coordinator that collects information from its members and communicates with other coordinators to construct a partial WFG and detect cycles.
  - Distributed approach: Each node maintains its own local WFG and exchanges information with other nodes using messages to detect cycles in a distributed manner.
- Some examples of distributed deadlock detection algorithms are:
  - Chandy-Misra-Haas algorithm: A distributed edge-chasing algorithm that uses probe messages to trace the dependency paths in the WFG.
  - Ho-Ramamoorthy algorithm: A distributed algorithm that uses a diffusing computation to initiate and terminate the deadlock detection process.
  - Menasce-Muntz algorithm: A hierarchical algorithm that uses a tree structure to organize the nodes and coordinators and uses a combination of edge-chasing and WFG construction to detect cycles.



### Path Pushing Algorithms for Distributed Deadlock Detection

- Path pushing algorithms detect distributed deadlocks by maintaining an explicit global wait-for graph (WFG) for each site of the distributed system  .
- The global WFG is a directed graph that represents the dependencies among the processes in the system. A node in the graph is a process and an edge from node P to node Q means that P is waiting for a resource held by Q  .
- The basic idea is to build and update the global WFG at each site whenever a deadlock computation is performed. A site initiates a deadlock computation when it detects a local deadlock or receives a deadlock computation request from another site  .
- When a site performs a deadlock computation, it sends its local WFG to all neighboring sites, where a neighboring site is a site that shares an edge with the sender in the global WFG  .
- Each site then merges the received local WFGs with its own local WFG to form a new global WFG. The site then checks for cycles in the new global WFG, which indicate the presence of a distributed deadlock  .
- If a cycle is detected, the site initiates a deadlock resolution procedure, which may involve aborting or preempting some processes in the cycle  .
- The advantages of path pushing algorithms are that they can detect deadlocks quickly and accurately, and they do not require any additional messages for deadlock detection  .
- The disadvantages of path pushing algorithms are that they require a lot of storage space and communication bandwidth to maintain and exchange the global WFGs, and they may generate false cycles due to the inconsistency of the global WFGs  .



### Edge Chasing Algorithms for Distributed Deadlock Detection

- Edge chasing algorithms are a class of distributed deadlock detection algorithms that use special messages called probes to trace the dependency graph of processes and resources in a distributed system.
- A probe is a triplet (i, j, k) that denotes that the deadlock detection is initiated by process P_i and the message is being sent by the home site of process P_j to the home site of process P_k.
- The probe message follows the edges of the dependency graph from the waiting processes to the blocking processes until either a cycle is detected or the probe reaches a process that is not waiting for any resource.
- A cycle in the dependency graph indicates a deadlock, and the processes involved in the cycle are notified by the probe message.
- Edge chasing algorithms can be applied to different request models, such as AND model, OR model, or AND-OR model, depending on the type of requests that processes can make for resources.
- One of the most well-known edge chasing algorithms is the Chandy-Misra-Haas algorithm for the AND model, which is based on the following rules:

  - Rule 1: A process P_i initiates a deadlock detection by sending a probe (i, i, j) to the home site of process P_j, where P_j is the process that P_i is waiting for.
  - Rule 2: A process P_j receives a probe (i, k, j) from the home site of process P_k. If P_j is not waiting for any resource, it discards the probe. Otherwise, it sends the probe (i, j, l) to the home site of process P_l, where P_l is the process that P_j is waiting for.
  - Rule 3: A process P_i receives a probe (i, k, i) from the home site of process P_k. This means that a cycle has been detected and P_i is involved in a deadlock. P_i informs all the processes in the cycle about the deadlock and terminates the deadlock detection.

- Edge chasing algorithms have the advantages of being simple, efficient, and scalable, as they do not require global information or synchronization among the sites. However, they also have some drawbacks, such as:

  - They may generate false positives, i.e., detect deadlocks that do not exist, due to the presence of concurrent requests and releases of resources.
  - They may generate multiple probes for the same deadlock, resulting in redundant messages and computations.
  - They may not terminate if there are orphan messages, i.e., messages that are lost or delayed in the network.



## Unit 4 - Agreement Protocols

- Agreement protocols are a class of distributed algorithms that allow a set of processes to reach a common decision or consensus, despite the possibility of failures or faults.
- Agreement protocols are useful for implementing reliable and consistent services in distributed systems, such as leader election, atomic broadcast, distributed transactions, replication, and fault tolerance.
- Agreement protocols can be classified into different types based on the assumptions they make about the system model, such as the number and type of failures, the communication model, the synchrony assumptions, and the validity and termination properties.
- Some of the common types of agreement protocols are:
  - **Consensus**: Each process proposes a value and must agree on a single value that is one of the proposed values.
  - **Atomic commit**: Each process decides to commit or abort a transaction and must agree on a single outcome that is either commit or abort.
  - **Byzantine agreement**: Each process proposes a value and must agree on a single value that is one of the proposed values, even if some processes are faulty and may behave arbitrarily (Byzantine faults).
  - **Interactive consistency**: Each process has a private value and must agree on a vector of values that contains the private values of all correct processes.
  - **k-set agreement**: Each process proposes a value and must agree on a single value that is one of the proposed values, but up to k different values are allowed.
- Agreement protocols are often impossible or difficult to achieve in certain system models, due to the presence of failures, asynchrony, or uncertainty. For example, the FLP impossibility result shows that consensus is impossible to solve in an asynchronous system with even one crash failure. The CAP theorem shows that atomic consistency, availability, and partition tolerance are impossible to achieve simultaneously in a distributed system. The Byzantine generals problem shows that Byzantine agreement requires at least 3f+1 processes to tolerate f Byzantine faults.
- Agreement protocols often rely on techniques such as message passing, timeouts, failure detectors, quorums, voting, randomization, cryptography, or trusted components to overcome the challenges and limitations of the system model and achieve the desired properties. Some of the well-known agreement protocols are:
  - **Paxos**: A family of consensus protocols that use a leader-based approach and quorum intersection to ensure safety and liveness in asynchronous systems with crash failures.
  - **Raft**: A consensus protocol that simplifies Paxos by using a stronger leader and a more intuitive state machine to ensure safety and liveness in asynchronous systems with crash failures.
  - **Two-phase commit**: An atomic commit protocol that uses a coordinator and two phases (prepare and commit) to ensure agreement on a transaction outcome in synchronous systems with crash failures.
  - **Three-phase commit**: An atomic commit protocol that uses a coordinator and three phases (prepare, pre-commit, and commit) to ensure agreement on a transaction outcome in asynchronous systems with crash failures.
  - **Practical Byzantine Fault Tolerance (PBFT)**: A Byzantine agreement protocol that uses a primary and a three-phase protocol (pre-prepare, prepare, and commit) to ensure agreement on a value in asynchronous systems with Byzantine faults.
  - **Zyzzyva**: A Byzantine agreement protocol that uses a primary and a two-phase protocol (request and commit) to ensure agreement on a value in asynchronous systems with Byzantine faults, and optimizes the performance by using speculative execution and MAC authentication.



### Introduction for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by passing messages.
- Agreement protocols are algorithms that enable the processes in a distributed system to reach a common decision or consensus on some value or action, despite the presence of failures or uncertainties.
- Agreement protocols are essential for ensuring the consistency, reliability, and availability of distributed systems, especially in applications such as fault-tolerant services, distributed transactions, distributed databases, distributed ledgers, and distributed consensus.
- Some of the challenges and issues that agreement protocols need to address are:
  - How to deal with partial failures, such as process crashes, network partitions, or message losses?
  - How to cope with malicious failures, such as Byzantine faults, where some processes may behave arbitrarily or dishonestly?
  - How to handle asynchrony, where there is no bound on the message delays or the relative speeds of the processes?
  - How to achieve efficiency, scalability, and fault-tolerance, while minimizing the communication and computation overheads?
- Some of the types and variants of agreement protocols are:
  - Atomic commit protocols, which ensure that a set of processes either all commit or all abort a transaction.
  - Consensus protocols, which ensure that a set of processes agree on a single value proposed by one or more of them.
  - Byzantine agreement protocols, which are consensus protocols that can tolerate Byzantine faults.
  - Paxos and Raft protocols, which are consensus protocols that are widely used in practical distributed systems.
  - Multi-Paxos and Viewstamped Replication protocols, which are extensions of Paxos and Raft that enable state machine replication.
  - Leader election protocols, which ensure that a set of processes elect a unique leader among them.
  - Mutual exclusion protocols, which ensure that a set of processes can access a shared resource in a mutually exclusive manner.



### System models for distributed systems

System models are abstract descriptions of the properties and behaviors of distributed systems. They help to understand, design, and implement distributed systems by providing common concepts and terminology. System models can be classified into three types:

- **Architectural models**: describe the structure and organization of the components of a distributed system and their interactions. Architectural models can be further divided into subtypes based on the roles and responsibilities of the components, such as client-server, peer-to-peer, publish-subscribe, etc.
- **Interaction models**: describe the communication and coordination mechanisms among the components of a distributed system. Interaction models can be further divided into subtypes based on the timing, ordering, and reliability of the messages, such as synchronous, asynchronous, causal, atomic, etc.
- **Fault models**: describe the types and effects of failures that can occur in a distributed system and the assumptions and guarantees that can be made about them. Fault models can be further divided into subtypes based on the nature and severity of the failures, such as crash, omission, timing, byzantine, etc.

System models are useful for the study of agreement protocols in distributed systems, which are algorithms that allow the components to reach a consistent state or decision despite the presence of faults and uncertainties. Agreement protocols can be classified into three types:

- **Consensus protocols**: require the components to agree on a single value from a set of proposed values. Consensus protocols are essential for achieving fault tolerance and consistency in distributed systems, such as distributed databases, blockchain, and leader election.
- **Atomic broadcast protocols**: require the components to deliver the same set of messages in the same order. Atomic broadcast protocols are useful for implementing replicated state machines and distributed transactions in distributed systems, such as distributed commit, Paxos, and Raft.
- **Mutual exclusion protocols**: require the components to access a shared resource in a mutually exclusive manner. Mutual exclusion protocols are important for ensuring correctness and fairness in distributed systems, such as distributed locks, tokens, and quorums.



### Classification of Agreement Problem in Distributed System

An agreement problem is a problem where a set of processes in a distributed system need to reach a common decision based on their local inputs and messages exchanged with each other. Agreement problems are fundamental for achieving coordination, consistency, and fault tolerance in distributed systems. There are different types of agreement problems, depending on the system model, the failure assumptions, and the desired properties of the decision. Some of the common agreement problems are:

- **Byzantine agreement problem**: In this problem, each process has an initial value and needs to decide on a final value, such that all correct processes decide on the same value, and the value is equal to the initial value of some correct process. The system may contain faulty processes that can behave arbitrarily, called Byzantine faults. A solution to this problem requires a communication protocol that can tolerate a certain number of Byzantine faults and ensure agreement among the correct processes .
- **Consensus problem**: In this problem, each process has an initial value and needs to decide on a final value, such that all correct processes decide on the same value, and the value is equal to the initial value of some process. The system may contain faulty processes that can crash, called crash faults. A solution to this problem requires a communication protocol that can tolerate a certain number of crash faults and ensure agreement among the correct processes .
- **Interactive consistency problem**: In this problem, each process has an initial value and needs to decide on a vector of values, such that the vector contains the initial values of all processes, and all correct processes decide on the same vector. The system may contain faulty processes that can behave arbitrarily, called Byzantine faults. A solution to this problem requires a communication protocol that can tolerate a certain number of Byzantine faults and ensure agreement among the correct processes .
- **Atomic commitment problem**: In this problem, each process has an initial value that indicates whether it is willing to commit or abort a transaction, and needs to decide on a final value that indicates whether the transaction is committed or aborted, such that all correct processes decide on the same value, and the value is commit only if all processes are willing to commit. The system may contain faulty processes that can crash, called crash faults. A solution to this problem requires a communication protocol that can tolerate a certain number of crash faults and ensure agreement among the correct processes .
- **Atomic broadcast problem**: In this problem, each process can send a message to a group of processes, and needs to deliver the messages, such that all correct processes deliver the same set of messages, and the messages are delivered in the same order. The system may contain faulty processes that can crash, called crash faults. A solution to this problem requires a communication protocol that can tolerate a certain number of crash faults and ensure agreement among the correct processes .
- **Group membership problem**: In this problem, each process needs to decide on a set of processes that are currently active in the system, such that all correct processes decide on the same set, and the set reflects the actual status of the processes. The system may contain faulty processes that can crash, join, or leave, called dynamic faults. A solution to this problem requires a communication protocol that can tolerate a certain number of dynamic faults and ensure agreement among the correct processes .



### Byzantine agreement problem

- The Byzantine agreement problem is a fundamental problem in fault tolerant distributed computing that requires a set of parties in a distributed environment to agree on a value even if some of the parties are corrupted.
- The problem was first defined by Lamport and inspired by a hypothetical scenario of several divisions of the Byzantine army camped outside an enemy city, each division commanded by its own general. The generals can communicate with one another only by messenger. After observing the enemy, they must decide upon a common plan of action.
- The problem is that some of the generals may be traitors and try to prevent the loyal generals from reaching agreement. The traitors may send conflicting messages to different generals, or send no messages at all. The loyal generals need a secure way to come to agreement on a plan (known as consensus) and carry out their chosen plan (known as coordination).
- A solution to the Byzantine agreement problem is a protocol that ensures the following properties:
  - **Validity**: If all the parties start with the same value, then they all decide on that value.
  - **Agreement**: All the parties decide on the same value.
  - **Termination**: All the parties eventually decide on a value.
- A number of solutions to the Byzantine agreement problem exist, depending on the assumptions made about the communication model, the number of corrupted parties, the synchrony of the system, and the cryptographic primitives available. Some examples of Byzantine agreement protocols are:
  - **Oral messages**: This protocol assumes that the communication is reliable and authenticated, but the messages may be altered by the corrupted parties. It requires that the number of corrupted parties is less than one third of the total number of parties.
  - **Signed messages**: This protocol assumes that the communication is reliable and the messages are digitally signed by the sender, but the signatures may be forged by the corrupted parties. It requires that the number of corrupted parties is less than half of the total number of parties.
  - **Randomized messages**: This protocol assumes that the communication is reliable and the messages are randomly generated by the sender, but the randomness may be biased by the corrupted parties. It requires that the number of corrupted parties is less than half of the total number of parties, and that the parties have access to a common source of randomness.
  - **Cryptographic messages**: This protocol assumes that the communication is reliable and the messages are encrypted by the sender, but the encryption may be broken by the corrupted parties. It requires that the number of corrupted parties is less than half of the total number of parties, and that the parties have access to a secure cryptographic scheme.



### Consensus problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- The consensus problem is the problem of getting a set of nodes in a distributed system to agree on something - it might be a value, a course of action or a decision.
- Achieving consensus allows a distributed system to act as a single entity, with every individual node aware of and in agreement with the actions of the whole of the network.
- Consensus is a general agreement on a decision made by the majority of those involved.
- Consensus is essential for ensuring reliability, consistency, fault-tolerance, and availability in distributed systems .
- Consensus is challenging to achieve in distributed systems because of the possibility of failures, such as network partitions, message losses, node crashes, or malicious attacks  .
- There are many ways in which processes in a distributed system can reach a consensus, but there is usually a trade-off between security and performance.
- Some of the common consensus protocols are:
  - Two-phase commit: A simple and centralized protocol that requires a coordinator node to initiate and finalize the decision based on the votes of the other nodes.
  - Three-phase commit: An extension of the two-phase commit that adds a pre-commit phase to avoid blocking in case of coordinator failure.
  - Paxos: A family of decentralized protocols that use a quorum of nodes to propose and accept values, and ensure that only one value is chosen.
  - Raft: A simplified version of Paxos that divides the consensus problem into leader election, log replication, and safety.
  - Byzantine fault tolerance: A class of protocols that can tolerate arbitrary failures, including malicious behavior, by requiring a supermajority of nodes to agree.



### Interactive Consistency Problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- Interactive consistency is the problem in which n distinct nodes, each having its own private value, where up to t may be Byzantine, run an algorithm that allows all non-faulty nodes to infer the values of each other node  .
- Byzantine nodes are nodes that can behave arbitrarily, such as sending incorrect or conflicting messages, or remaining silent.
- The goal of interactive consistency is to reach agreement in a distributed system in the presence of faults.
- Interactive consistency is also known as Byzantine Generals Problem, which is a metaphor for a situation where a group of generals must coordinate an attack or retreat, but some of them may be traitors who try to sabotage the plan.
- Interactive consistency is a fundamental problem in computer science, as it is relevant to critical applications that rely on the combination of the opinions of multiple peers to provide a service, such as distributed databases, fault-tolerant systems, blockchain, and voting systems .
- Interactive consistency is a hard problem to solve, as it requires a high degree of synchronization and communication among the nodes, and it has some impossibility results that limit the feasibility and efficiency of the algorithms  .
- Some of the impossibility results are:
  - There is no deterministic algorithm that can solve interactive consistency in an asynchronous system with one or more Byzantine nodes.
  - There is no deterministic algorithm that can solve interactive consistency in a synchronous system with more than n/3 Byzantine nodes.
  - There is no randomized algorithm that can solve interactive consistency in a synchronous system with more than n/2 Byzantine nodes.
- Some of the algorithms that can solve interactive consistency in different settings are:
  - The Oral Messages Algorithm, which can solve interactive consistency in a synchronous system with up to n/3 Byzantine nodes, using O(n^2) messages and O(n) rounds.
  - The Signed Messages Algorithm, which can solve interactive consistency in a synchronous system with up to n/2 Byzantine nodes, using O(n^2) messages and O(n) rounds, but requiring digital signatures.
  - The Randomized Consensus Algorithm, which can solve interactive consistency in a synchronous system with up to n/2 Byzantine nodes, using O(n^2) messages and O(n) rounds, but requiring random bits and having a probability of failure that decreases exponentially with the number of rounds.
  - The Broadcast Algorithm, which can solve interactive consistency in a mostly-asynchronous system with up to n/3 Byzantine nodes, using O(n^2) messages and O(1) rounds, but requiring a single synchronization barrier .
- Interactive consistency is an important and challenging problem in distributed systems, and it has many applications and variations that require different assumptions and solutions.



### Solution to Byzantine Agreement problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- The Byzantine agreement problem is a fundamental problem in fault tolerant distributed computing, where a set of parties in a distributed environment need to agree on a value even if some of the parties are corrupted.
- The problem was first defined by Lamport  and inspired by a hypothetical scenario of several divisions of the Byzantine army camped outside an enemy city, each division commanded by its own general. The generals can communicate with one another only by messenger. After observing the enemy, they must decide upon a common plan of action, such as attack or retreat .
- The problem is that some of the generals may be traitors, who try to prevent the loyal generals from reaching agreement. The traitors may send conflicting messages to different generals, or send no messages at all. The loyal generals need a protocol that allows them to reach a consensus, despite the presence of traitors .
- A solution to the Byzantine agreement problem must satisfy the following properties :
  - **Termination**: Every loyal general eventually decides on a value.
  - **Agreement**: All loyal generals decide on the same value.
  - **Validity**: If all loyal generals start with the same value, then they all decide on that value.
- A number of solutions to the Byzantine agreement problem exist, depending on the assumptions made about the communication model, the number of parties, the number of traitors, and the type of values. Some of the common solutions are :
  - **Oral messages**: This solution assumes that the communication is synchronous, meaning that messages are delivered within a known bounded time, and that the messages are signed, meaning that the sender and the content of the message can be verified. The solution also assumes that there are n parties, of which at most t are traitors, and that n > 3t. The solution involves a series of rounds, where each party sends its value to all other parties, and then computes a majority value based on the received messages. The number of rounds depends on the number of traitors, and the final value is the majority value after the last round.
  - **Signed messages**: This solution assumes that the communication is asynchronous, meaning that messages may be delayed arbitrarily, and that the messages are signed. The solution also assumes that there are n parties, of which at most t are traitors, and that n > 3t. The solution involves a series of rounds, where each party sends its value and a proof of its value to all other parties, and then computes a majority value based on the received messages and proofs. The proof consists of a vector of signatures from other parties, and the number of rounds depends on the number of traitors. The final value is the majority value after the last round.
  - **Randomized messages**: This solution assumes that the communication is asynchronous and that the messages are not signed. The solution also assumes that there are n parties, of which at most t are traitors, and that n > 3t. The solution involves a series of rounds, where each party sends its value and a random coin flip to all other parties, and then computes a majority value based on the received messages and coin flips. The coin flip is used to break ties in case of a split majority. The number of rounds depends on the probability of error, and the final value is the majority value after the last round.



### Application of Agreement problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- Agreement problem is a fundamental problem in distributed computing and multi-agent systems that requires coordinating processes to reach consensus, or agree on some data value that is needed during computation .
- Agreement problem can be classified into two types: consensus and atomic commitment.
  - Consensus: participants need to agree on a value, but they are willing and capable to accept any value.
  - Atomic commitment: participants need to agree on a value, but they have specific constraints on whether they can accept any particular value.
- Agreement problem is essential for a wide range of applications in distributed systems, such as fault tolerance, replication, distributed transactions, distributed databases, group communication, leader election, etc .
- Agreement problem is challenging to solve in the presence of failures, such as process crashes, network partitions, message losses, or malicious behavior   .
- Agreement problem can be solved by using various agreement protocols, such as Paxos, Raft, Two-phase commit, Three-phase commit, Byzantine agreement, etc    .
- Agreement protocols have different properties, such as correctness, termination, validity, agreement, fault tolerance, performance, etc   .
- Agreement protocols can be analyzed and compared using different models and assumptions, such as synchronous or asynchronous systems, deterministic or randomized algorithms, failure detectors, message complexity, etc   .



### Atomic Commit in Distributed Database System

- A distributed database system consists of multiple database sites that are connected by a communication network.
- A distributed transaction is a transaction that accesses data from multiple sites and updates them atomically.
- Atomicity means that either all the updates are committed or none of them are, leaving the database in a consistent state.
- Atomic commit is the process of ensuring that all the sites involved in a distributed transaction agree on the final outcome of the transaction, whether it is commit or abort.
- Atomic commit is essential for maintaining the ACID properties of transactions in a distributed database system, especially in the presence of failures or network partitions.
- Atomic commit protocols are the algorithms that coordinate the decision making among the sites and handle the possible failures or conflicts.
- Atomic commit protocols can be classified into two categories: blocking and non-blocking.
- Blocking protocols are those that require some sites to wait for the response of other sites before committing or aborting their local updates. These protocols may block indefinitely if some sites fail or become unreachable.
- Non-blocking protocols are those that do not require any site to wait for the response of other sites. These protocols can guarantee the termination of the atomic commit process even if some sites fail or become unreachable.
- Examples of blocking protocols are the two-phase commit protocol (2PC) and the three-phase commit protocol (3PC).
- Examples of non-blocking protocols are the Paxos commit protocol and the FLAC protocol.



## Unit 5 - Distributed Resource Management

- Distributed resource management (DRM) is an evolving discipline that aims to optimize the performance and efficiency of distributed enterprise systems by using a set of software, hardware, network tools, procedures and policies.
- DRM can be applied to various types of distributed systems, such as cloud computing, grid computing, peer-to-peer networks, distributed databases, and distributed energy resources.
- DRM involves two main tasks: resource discovery and resource scheduling.
  - Resource discovery is the process of finding and identifying the available resources in a distributed system, such as processors, memory, storage, bandwidth, and energy sources.
  - Resource scheduling is the process of allocating and managing the resources among the competing tasks or applications in a distributed system, such as load balancing, fault tolerance, quality of service, and security.
- DRM faces several challenges, such as heterogeneity, scalability, dynamism, uncertainty, and coordination of the distributed resources and tasks.
- DRM can benefit from various techniques, such as distributed algorithms, machine learning, optimization, game theory, and blockchain, to address the challenges and improve the outcomes.
- DRM can provide various benefits to the distributed systems and their users, such as:
  - Enhancing system resiliency and reliability by using multiple and diverse resources .
  - Reducing operational costs and environmental impacts by using renewable and efficient resources .
  - Improving user satisfaction and experience by providing customized and flexible services .



### Issues in Distributed File Systems

A distributed file system (DFS) is a system that allows multiple clients to access and manipulate files stored on one or more servers over a network. DFS aims to provide high performance, reliability, scalability, and transparency to the users. However, there are several issues and challenges in designing and implementing a DFS, such as:

- **Naming and name resolution**: A DFS needs to provide a consistent and uniform way of naming and locating files across different servers and clients. This involves choosing a suitable namespace, a naming scheme, and a name resolution mechanism. For example, a DFS may use a hierarchical namespace that maps file names to server addresses, or a flat namespace that uses unique identifiers for files. A name resolution mechanism may involve a centralized or distributed directory service, a caching scheme, or a hashing function .

- **Replication and consistency**: A DFS may replicate files or parts of files across multiple servers to improve availability, fault tolerance, and load balancing. However, this introduces the problem of maintaining consistency among the replicas, especially when concurrent updates occur. A DFS needs to define a consistency model that specifies the guarantees and expectations for the users and the system. For example, a DFS may use a strict consistency model that ensures all replicas are always identical, or a relaxed consistency model that allows temporary divergence and eventual convergence of replicas. A DFS also needs to implement a consistency protocol that enforces the consistency model, such as a locking mechanism, a versioning scheme, or a quorum-based approach .

- **Caching and performance**: A DFS may cache files or parts of files on the client side or the server side to reduce network traffic and improve response time. However, this also introduces the problem of cache coherence, which is related to the consistency issue. A DFS needs to ensure that the cached data is valid and up-to-date, and that any changes made to the cached data are propagated to the servers and other clients. A DFS may use a cache coherence protocol that invalidates or updates the cached data when a write operation occurs, such as a write-through or a write-back policy. A DFS may also use a prefetching technique that anticipates the future access patterns and fetches the data in advance .

- **Security and access control**: A DFS needs to provide a secure and reliable way of authenticating and authorizing the users and the servers, and protecting the data from unauthorized or malicious access. This involves choosing a suitable security model, a cryptographic scheme, and a access control mechanism. For example, a DFS may use a centralized or distributed security model that relies on a trusted authority or a peer-to-peer network. A cryptographic scheme may involve encryption, decryption, hashing, or digital signatures. An access control mechanism may involve a discretionary or a mandatory policy, a capability-based or an access control list-based approach .

- **Fault tolerance and recovery**: A DFS needs to cope with various types of failures that may occur in the network, the servers, or the clients, and ensure that the system can continue to operate correctly and efficiently. This involves choosing a suitable fault model, a fault detection scheme, and a fault recovery mechanism. For example, a DFS may assume a fail-stop or a Byzantine fault model that characterizes the behavior and the impact of the faulty components. A fault detection scheme may involve timeouts, heartbeats, or acknowledgments. A fault recovery mechanism may involve replication, checkpointing, logging, or rollback .



### Mechanism for building distributed file systems

A distributed file system (DFS) is a file system that enables clients to access file storage from multiple hosts through a computer network as if the user was accessing local storage. Files are spread across multiple storage servers and in multiple locations, which enables users to share data and storage resources.

The mechanism for building distributed file systems involves the following components and steps:

- **File servers**: These are the hosts that store the files and provide access to them over the network. File servers can be dedicated machines or general-purpose computers that run a file server software.
- **Clients**: These are the hosts that request and use the files stored on the file servers. Clients can be any device that can connect to the network and run a file system client software.
- **Network**: This is the medium that connects the file servers and the clients. The network can be wired or wireless, local or wide area, and use different protocols and topologies.
- **Naming**: This is the process of assigning unique and meaningful identifiers to the files and directories in the distributed file system. Naming can be done by using a flat or hierarchical namespace, a global or local naming scheme, and a static or dynamic mapping.
- **Location**: This is the process of finding the physical location of a file or directory given its name. Location can be done by using a centralized or distributed directory service, a caching or replication mechanism, and a consistent hashing or load balancing technique.
- **Access**: This is the process of reading and writing data to and from the files and directories in the distributed file system. Access can be done by using a stateful or stateless protocol, a remote or local access method, and a locking or concurrency control mechanism.
- **Consistency**: This is the process of ensuring that the data in the distributed file system is correct and up-to-date across all the file servers and clients. Consistency can be done by using a strict or relaxed consistency model, a push or pull update strategy, and a synchronous or asynchronous update mode.
- **Fault tolerance**: This is the process of handling failures and errors in the distributed file system. Fault tolerance can be done by using a replication or erasure coding scheme, a backup or recovery method, and a detection or correction technique.
- **Security**: This is the process of protecting the data and the users in the distributed file system from unauthorized access and malicious attacks. Security can be done by using a authentication or authorization mechanism, a encryption or decryption method, and a auditing or logging technique.

Some examples of distributed file systems are NFS, HDFS, Ceph, GlusterFS, and DFS .



### Design issues in Distributed Shared Memory

Distributed Shared Memory (DSM) is a mechanism that allows multiple processes on different nodes to share a common logical address space and access data transparently. DSM can simplify the programming of distributed systems by hiding the details of inter-process communication. However, DSM also introduces several design issues that affect its performance, scalability, and correctness. Some of the main design issues in DSM are:

- **Granularity**: Granularity refers to the size of the unit of sharing and the unit of coherence in DSM. A smaller granularity, such as a byte or a word, can reduce the amount of false sharing and improve the locality of access, but it can also increase the overhead of coherence maintenance and communication. A larger granularity, such as a page or a segment, can reduce the overhead of coherence and communication, but it can also increase the amount of false sharing and waste bandwidth and memory. Therefore, choosing an appropriate granularity is a trade-off between these factors.

- **Structure**: Structure refers to the organization of the shared data in the logical address space and the mapping of the shared data to the physical memory of the nodes. The structure of DSM can be flat, hierarchical, or object-based. A flat structure treats the shared data as a single linear array and maps it to the nodes using a static or dynamic hashing function. A hierarchical structure divides the shared data into multiple regions and maps each region to a node using a directory or a home-based scheme. An object-based structure treats the shared data as a collection of objects and maps each object to a node using a name server or a location service. The structure of DSM affects the ease of programming, the locality of access, and the scalability of the system.

- **Coherence semantics**: Coherence semantics define the consistency model of DSM, which specifies the order and visibility of the updates to the shared data. Coherence semantics can be strict, relaxed, or weak. A strict coherence semantics, such as sequential consistency or processor consistency, guarantees that all processes see the same order of updates and that the updates are propagated immediately. A relaxed coherence semantics, such as release consistency or entry consistency, allows some reordering and delay of updates, but requires the programmer to use synchronization primitives to ensure correctness. A weak coherence semantics, such as eventual consistency or causal consistency, does not guarantee any order or visibility of updates, but relies on the application logic to tolerate inconsistency. The coherence semantics of DSM affects the performance, scalability, and correctness of the system.

- **Coherence protocol**: Coherence protocol defines the mechanism of maintaining the coherence of the shared data among the nodes. Coherence protocol can be centralized, distributed, or hybrid. A centralized coherence protocol uses a single node or a group of nodes as the authority for the coherence of the shared data and relies on messages or interrupts to communicate with the other nodes. A distributed coherence protocol uses a distributed algorithm, such as a token ring or a quorum, to coordinate the coherence of the shared data and relies on messages or multicast to communicate with the other nodes. A hybrid coherence protocol combines the features of both centralized and distributed protocols and adapts to the workload and the network conditions. The coherence protocol of DSM affects the performance, scalability, and fault tolerance of the system.

- **Scalability**: Scalability refers to the ability of DSM to handle the increase in the number of nodes, the size of the shared data, and the frequency of the access. Scalability depends on the design choices of the granularity, the structure, the coherence semantics, and the coherence protocol of DSM. A scalable DSM should minimize the overhead of coherence and communication, balance the load and the memory among the nodes, and adapt to the changes in the workload and the network conditions.

- **Heterogeneity**: Heterogeneity refers to the diversity of the nodes in terms of the hardware architecture, the operating system, the network interface, and the communication protocol. Heterogeneity poses several challenges for DSM, such as the compatibility of the data formats, the interoperability of the communication mechanisms, and the portability of the software. A heterogeneous DSM should provide a common abstraction of the shared data and the communication interface, and use appropriate techniques, such as data conversion, protocol translation, and code migration, to handle the differences among the nodes.



### Algorithm for Implementation of Distributed Shared Memory

Distributed Shared Memory (DSM) is a technique that allows multiple processes on different nodes of a distributed system to share a common virtual address space and access the same data objects. DSM can simplify the programming of distributed applications by providing a uniform view of memory and hiding the details of data distribution and communication.

There are different algorithms for implementing DSM, each with its own advantages and disadvantages. Some of the basic algorithms are:

- **Central Server Algorithm**: In this algorithm, a central server maintains all the shared data and services the read and write requests from other nodes. The server can use a page-based or an object-based approach to store the shared data. The advantage of this algorithm is that it is simple and ensures consistency of the shared data. The disadvantage is that it introduces a single point of failure and a performance bottleneck, as all the requests have to go through the server.   

- **Migration Algorithm**: In this algorithm, the shared data is initially stored at the server, but it can migrate to other nodes upon request. The node that requests a data item gets the exclusive access to it and becomes the new owner of the item. The server keeps track of the current location of each data item. The advantage of this algorithm is that it reduces the network traffic and the server load, as the data can be accessed locally by the owner. The disadvantage is that it may cause frequent data migration and inconsistency, as the data can be modified by the owner without notifying the server or other nodes.   

- **Replication Algorithm**: In this algorithm, the shared data is replicated on multiple nodes, so that each node can access the data locally. The server is responsible for creating and deleting the replicas, and for ensuring the consistency of the data. The server can use different consistency models, such as sequential consistency, causal consistency, or weak consistency, depending on the application requirements. The advantage of this algorithm is that it improves the availability and fault tolerance of the data, as the data can be accessed even if some nodes or the server fail. The disadvantage is that it increases the storage and communication overhead, as the data has to be replicated and updated on multiple nodes.   

- **Invalidation Algorithm**: In this algorithm, the shared data is initially stored at the server, but it can be cached on other nodes upon request. The server maintains a list of nodes that have cached a data item, and sends invalidation messages to them when the data item is modified by another node. The node that requests a data item gets a read-only copy of it, unless it requests a write access. The advantage of this algorithm is that it reduces the network traffic and the server load, as the data can be read from the cache. The disadvantage is that it may cause cache misses and inconsistency, as the data can be invalidated by the server or other nodes.   

These algorithms are not mutually exclusive, and can be combined or modified to suit different scenarios and applications. For example, a hybrid algorithm can use both replication and invalidation, or a hierarchical algorithm can use multiple servers to distribute the load and improve the scalability.



## Unit 6 - Failure Recovery in Distributed Systems

- Failure recovery is the process of restoring the correct state and functionality of a distributed system after a failure occurs.
- A failure is an event that causes a deviation from the expected behavior of a system or a component.
- Failures can be classified into different types, such as:
  - Crash failure: A component stops functioning and does not resume.
  - Omission failure: A component fails to send or receive a message.
  - Timing failure: A component violates the timing constraints of the system.
  - Response failure: A component produces an incorrect output or performs an incorrect action.
  - Byzantine failure: A component behaves arbitrarily and maliciously, possibly colluding with other faulty components.
- Failure recovery can be achieved by different techniques, such as:
  - Checkpointing: A component periodically saves its state to a stable storage, which can be used to restore the state in case of a failure.
  - Logging: A component records its actions and messages to a stable storage, which can be used to replay the actions and messages in case of a failure.
  - Replication: A component is replicated by one or more backup components, which can take over the role of the primary component in case of a failure.
  - Voting: A component receives multiple results from different sources and chooses the correct one based on a majority or a consensus rule.
  - Rollback-recovery: A component reverts its state to a previous consistent state after a failure, and resumes the computation from that point.
  - Forward-recovery: A component detects and corrects the errors in its state after a failure, and continues the computation from the current point.



### Concepts in Backward and Forward Recovery

- Backward recovery and forward recovery are two techniques for restoring the system to a consistent state after a failure in a distributed system.
- Backward recovery involves rolling back the system to a previous error-free state by using checkpoints and logs. Forward recovery involves correcting the errors and continuing the execution from the current state.
- Backward recovery has the advantage of being independent of the nature of faults, but it may require undoing the effects of many transactions and coordinating with other processes. Forward recovery has the advantage of avoiding unnecessary rollbacks, but it may require accurate diagnosis of errors and complex recovery actions.
- Some of the concepts related to backward and forward recovery are:

  - Checkpoint: A checkpoint is a snapshot of the system state that is periodically taken and stored in a stable storage. Checkpoints can be local (for each process) or global (for the whole system). Checkpoints are used to reduce the amount of work that needs to be redone or undone in case of a failure.
  - Log: A log is a record of the actions performed by the system that may affect the system state. Logs can be undo logs (that store the old values of the modified data) or redo logs (that store the new values of the modified data). Logs are used to restore the system state to a consistent checkpoint by applying or reversing the logged actions.
  - Recovery line: A recovery line is a set of checkpoints that defines a consistent state of the system. A recovery line can be consistent (if all the checkpoints are consistent with each other) or inconsistent (if some checkpoints are inconsistent with each other). A recovery line is used to determine the starting point for recovery.
  - Recovery point: A recovery point is a point in the execution history of the system that corresponds to a consistent state of the system. A recovery point can be a checkpoint or a log record. A recovery point is used to determine the ending point for recovery.
  - Dependency graph: A dependency graph is a graph that represents the causal dependencies among the processes and the actions in the system. A dependency graph is used to determine the global state of the system and the effects of failures and rollbacks.



### Recovery in Concurrent Systems

- Recovery in concurrent systems is the process of restoring the system to a consistent state after a failure, while preserving the effects of the transactions that committed before the failure.
- Recovery in concurrent systems is challenging because multiple transactions may interleave their operations and share data, which may result in inconsistent or incomplete recovery actions.
- Recovery in concurrent systems can be classified into two main categories: backward recovery and forward recovery.
- Backward recovery is the technique of undoing the effects of the transactions that were affected by the failure, and restoring the system to a previous consistent state. Backward recovery requires the system to maintain logs or checkpoints of the system state and the transaction history, and to use them to roll back the changes made by the transactions.
- Forward recovery is the technique of redoing the effects of the transactions that were committed before the failure, and applying them to the current state of the system. Forward recovery requires the system to maintain logs or checkpoints of the committed transactions and their outputs, and to use them to replay the changes made by the transactions.
- Recovery in concurrent systems can also be influenced by the concurrency control mechanism used by the system, such as locking, timestamping, or optimistic methods. Concurrency control can affect the order and the atomicity of the transactions, and thus the recovery actions needed to preserve them.
- Recovery in concurrent systems can also be performed in parallel or concurrently, by using multiple recovery sessions or threads to recover different parts of the system or different media sets. Concurrent recovery can improve the performance and the availability of the system, but it may also introduce additional complexity and synchronization issues.



### Obtaining consistent Checkpoints for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Checkpointing is a technique to save the state of a distributed system periodically, so that it can be recovered from failures.
- A checkpoint is a snapshot of the local state of a process, such as its memory, registers, and open files.
- A consistent checkpoint is a set of checkpoints from different processes that reflects a global state that could have occurred during the execution of the system.
- A consistent checkpoint should not contain any orphan messages, which are messages that are received by a process after its checkpoint, but sent by another process before its checkpoint.
- There are two main approaches to obtain consistent checkpoints: coordinated checkpointing and communication-induced checkpointing.
- Coordinated checkpointing requires all processes to coordinate with each other to take checkpoints at the same time, or to flush all messages in transit before taking checkpoints. This ensures that no orphan messages are created, but it incurs a high overhead and may block the normal execution of the system.
- Communication-induced checkpointing allows each process to take checkpoints independently, but requires them to piggyback some information on the messages they send or receive, such as the sequence number or the dependency vector. This information is used to detect and discard inconsistent checkpoints, or to force some processes to take additional checkpoints to eliminate orphan messages. This approach reduces the overhead and blocking, but it may create more checkpoints than necessary.



### Recovery in Distributed Database Systems

- Recovery in distributed database systems is the process of restoring the database to a consistent state after a failure, such as a site crash, a communication link failure, or a transaction abort .
- Recovery in distributed database systems is more complicated than in centralized database systems, because failures can affect multiple sites and transactions, and the system has to coordinate the recovery actions across the network.
- Recovery in distributed database systems aims to maintain the atomicity and durability of distributed transactions, which means that either all or none of the subtransactions at different sites are committed, and the committed changes are permanent.
- Recovery in distributed database systems can be classified into two types: local recovery and global recovery.
  - Local recovery is the recovery of a single site from a failure, such as a disk crash or a power outage. Local recovery involves restoring a backup copy of the database, and applying the undo and redo operations from the log to bring the database to a consistent state.
  - Global recovery is the recovery of the whole system from a failure, such as a network partition or a coordinator crash. Global recovery involves resolving the uncertain status of distributed transactions, and ensuring that all sites agree on the final outcome of each transaction.
- Recovery in distributed database systems can use different techniques, such as:
  - Two-phase commit protocol, which is a distributed commit protocol that ensures atomicity of distributed transactions by using a coordinator site and participant sites, and two phases of voting and decision .
  - Three-phase commit protocol, which is an extension of the two-phase commit protocol that ensures atomicity and avoids blocking in case of a coordinator failure, by using a third phase of pre-commit and a timeout mechanism .
  - Shadow paging, which is a technique that maintains two copies of the database pages, one as the current version and one as the shadow version, and updates only the current version until the transaction commits, and then switches the roles of the two versions .
  - Checkpointing, which is a technique that periodically records the state of the system, such as the committed transactions, the active transactions, and the log records, to a stable storage, and reduces the amount of work needed for recovery .
  - Logging, which is a technique that records the changes made by the transactions to the database, such as the before and after values of the updated data items, the transaction identifiers, and the commit and abort records, to a log file, and uses them for undo and redo operations during recovery .
  - Replication, which is a technique that maintains multiple copies of the database at different sites, and increases the availability and reliability of the system, but also introduces the challenges of maintaining consistency and concurrency among the replicas .

: https://www.tutorialspoint.com/distributed_dbms/distributed_dbms_database_recovery.htm
: https://www.oreilly.com/library/view/database-systems-concepts/9788177585674/9788177585674_ch18lev1sec7.html
: https://link.springer.com/referenceworkentry/10.1007/978-0-387-39940-9_712



## Unit 7 - Fault Tolerance

- Fault tolerance is the ability of a system to continue functioning correctly in the presence of failures.
- Fault tolerance can be achieved by using techniques such as redundancy, replication, recovery, and reconfiguration.
- Redundancy is the provision of extra components or resources that can take over the function of a failed component or resource.
- Replication is the creation of multiple copies of data or services that can be accessed in case of a failure.
- Recovery is the process of restoring a system to a consistent and correct state after a failure.
- Reconfiguration is the process of changing the structure or parameters of a system to adapt to a failure or a changing environment.
- Fault tolerance can be classified into two types: passive and active.
- Passive fault tolerance relies on redundancy to mask failures without requiring any intervention or detection.
- Active fault tolerance relies on detection and recovery to handle failures by switching to a backup component or resource.
- Fault tolerance can be applied at different levels of a system, such as hardware, software, network, and application.
- Fault tolerance can improve the reliability, availability, and performance of a system, but it also introduces complexity, cost, and overhead.



### Issues in Fault Tolerance for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Fault tolerance is the ability of a system to continue functioning correctly in the presence of failures.
- Fault tolerance is important for distributed systems because they consist of multiple components that may be subject to different types of failures, such as hardware failures, software failures, network failures, malicious attacks, etc .
- Fault tolerance can be achieved by using various techniques, such as redundancy, replication, checkpointing, recovery, consensus, etc .
- Fault tolerance can be classified into different levels, such as detection, masking, tolerance, and recovery.
- Fault tolerance can also be categorized into different models, such as fail-stop, fail-silent, fail-noisy, Byzantine, etc .
- Fault tolerance can be evaluated by using different metrics, such as reliability, availability, safety, maintainability, etc .
- Fault tolerance can be implemented by using different algorithms, such as Paxos, Raft, Two-Phase Commit, Three-Phase Commit, etc .
- Fault tolerance can be enhanced by using different approaches, such as self-stabilization, self-healing, self-organization, etc .



### Commit Protocols

- Commit protocols are used to ensure the atomicity and durability of transactions in distributed systems.
- A transaction is a sequence of operations that must be executed as a unit, either completely or not at all.
- A commit protocol coordinates the actions of multiple processes that participate in a transaction, and decides whether to commit or abort the transaction.
- A commit protocol typically involves two phases: a voting phase and a decision phase.
- In the voting phase, each participant process sends a vote to a coordinator process, indicating whether it is ready to commit or not.
- In the decision phase, the coordinator process collects the votes and decides whether to commit or abort the transaction, and informs the participants of the decision.
- A commit protocol must satisfy the following properties:
  - Agreement: All participants agree on the same outcome of the transaction, either commit or abort.
  - Validity: The transaction is committed only if all participants voted to commit.
  - Termination: All participants eventually reach a decision, either commit or abort.
  - Non-blocking: If the coordinator or some participants fail, the remaining participants can still reach a decision.
- There are different types of commit protocols, such as two-phase commit (2PC), three-phase commit (3PC), and consensus-based commit (CBC).
- Two-phase commit (2PC) is the simplest and most widely used commit protocol. It consists of two phases: a prepare phase and a commit phase.
  - In the prepare phase, the coordinator sends a prepare message to all participants, asking them to vote. Each participant replies with a yes or no vote, indicating whether it is ready to commit or not. If a participant fails or does not reply, the coordinator assumes a no vote.
  - In the commit phase, the coordinator decides whether to commit or abort the transaction, based on the votes. If all votes are yes, the coordinator commits the transaction and sends a commit message to all participants. If any vote is no, the coordinator aborts the transaction and sends an abort message to all participants. Each participant follows the coordinator's decision and commits or aborts the transaction accordingly.
  - 2PC guarantees agreement, validity, and termination, but not non-blocking. If the coordinator fails after sending some commit messages and some abort messages, the participants may be in an inconsistent state and cannot reach a decision without the coordinator's recovery.
- Three-phase commit (3PC) is an extension of 2PC that adds a pre-commit phase to avoid blocking in case of coordinator failure. It consists of three phases: a prepare phase, a pre-commit phase, and a commit phase.
  - In the prepare phase, the coordinator sends a prepare message to all participants, asking them to vote. Each participant replies with a yes or no vote, indicating whether it is ready to commit or not. If a participant fails or does not reply, the coordinator assumes a no vote.
  - In the pre-commit phase, the coordinator decides whether to commit or abort the transaction, based on the votes. If all votes are yes, the coordinator sends a pre-commit message to all participants, indicating that it intends to commit the transaction. If any vote is no, the coordinator aborts the transaction and sends an abort message to all participants. Each participant follows the coordinator's decision and pre-commits or aborts the transaction accordingly. A pre-committed participant waits for a commit message from the coordinator to finalize the transaction.
  - In the commit phase, the coordinator sends a commit message to all pre-committed participants, confirming the transaction. Each participant follows the coordinator's decision and commits the transaction. If the coordinator fails or does not send a commit message, the pre-committed participants can communicate with each other and decide to commit the transaction without the coordinator.
  - 3PC guarantees agreement, validity, termination, and non-blocking, but it requires more messages and time than 2PC. It also assumes that there are no network partitions, otherwise the participants may reach different decisions.
- Consensus-based commit (CBC) is a generalization of commit protocols that uses a consensus algorithm to reach a decision. A consensus algorithm is a distributed algorithm that allows a set of processes to agree on a common value, even if some processes fail or behave maliciously.
  - In CBC, the coordinator proposes a value to commit or abort the transaction, and sends it to all participants. Each participant votes on the proposed value, and sends its vote to all other participants. The participants use a consensus algorithm to agree on a final value, and commit or abort the transaction accordingly.
  - CBC guarantees agreement, validity, termination, and non-blocking, but it requires more messages and time than 2PC and 3PC. It also requires a majority of correct and honest participants to reach a decision.



### Voting protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Voting protocols are a type of consensus protocols that allow a set of distributed nodes to agree on a common value or decision, despite the presence of faults or attacks.
- Voting protocols are useful for achieving fault tolerance in distributed systems, such as replicated databases, distributed file systems, or blockchain networks.
- Voting protocols can be classified into two categories: exact voting and inexact voting.
  - Exact voting requires that all nodes agree on the same value or decision, and that the value or decision is correct according to some predefined criteria. Examples of exact voting protocols are two-phase commit, three-phase commit, and Paxos.
  - Inexact voting allows some degree of disagreement or error among the nodes, as long as the value or decision is acceptable according to some predefined criteria. Examples of inexact voting protocols are majority voting, weighted voting, and probabilistic voting.
- Voting protocols can also be classified into two categories based on the security properties they provide: secure voting and non-secure voting.
  - Secure voting ensures that the value or decision is not influenced by malicious nodes or external attackers, and that the voting process is confidential and verifiable. Examples of secure voting protocols are Byzantine fault-tolerant protocols, such as PBFT, Zyzzyva, and Tendermint.
  - Non-secure voting does not provide any security guarantees, and assumes that the nodes are honest and the network is reliable. Examples of non-secure voting protocols are the traditional two-phase commit and three-phase commit protocols.
- Voting protocols can also be classified into two categories based on the fairness properties they provide: fair voting and unfair voting.
  - Fair voting ensures that the value or decision is not biased towards any node or group of nodes, and that the voting process is equitable and representative. Examples of fair voting protocols are proportional voting, approval voting, and ranked voting.
  - Unfair voting allows some degree of bias or preference among the nodes, as long as the value or decision is acceptable according to some predefined criteria. Examples of unfair voting protocols are plurality voting, veto voting, and dictatorship voting.



### Dynamic voting protocols

- Dynamic voting protocols are techniques for consistency and recovery control of replicated files in distributed systems  .
- The purpose of a replicated file is to improve the availability of a logical file in the presence of site failures and network partitions  .
- A dynamic voting protocol assigns a number of votes to each replica of a file, and requires a majority of votes to access or update the file   .
- The number of votes assigned to each replica can change dynamically depending on the system state, such as the number of active replicas, the network connectivity, and the access pattern   .
- Dynamic voting protocols can achieve higher availability and lower communication cost than static voting protocols, which assign a fixed number of votes to each replica    .
- Dynamic voting protocols can also be combined with quorum-based voting, which requires a minimum number of votes to access or update the file, rather than a majority .
- Quorum-based voting can reduce the number of messages and the response time of the system, but may increase the risk of inconsistency .
- Some examples of dynamic voting protocols are:
  - Topological dynamic voting, which assigns votes based on the network topology and the location of replicas.
  - Adaptive dynamic voting, which assigns votes based on the access frequency and the failure probability of replicas.
  - Dynamic weighted voting, which assigns votes based on the weight of replicas, which reflects their reliability and availability  .



## Unit 8 - Transactions and Concurrency Control

- A **transaction** is a logical unit of work that consists of a sequence of operations on a database, such as reading, writing, inserting, deleting, or updating data.
- A transaction has four main properties, known as **ACID**:
  - **Atomicity**: A transaction is either executed completely or not at all. If a transaction fails in the middle, the database is restored to its original state before the transaction started.
  - **Consistency**: A transaction preserves the integrity constraints and business rules of the database. After a transaction completes, the database is in a consistent and valid state.
  - **Isolation**: A transaction is executed independently of other transactions. The intermediate results of a transaction are not visible to other transactions, and vice versa.
  - **Durability**: The effects of a transaction are permanent and persist even in the event of system failures or power outages.
- A **concurrency control** mechanism is a set of rules and techniques that ensures the correct and consistent execution of multiple transactions on a shared database.
- Concurrency control is necessary to prevent **conflicts** or **anomalies** that may arise when multiple transactions access or modify the same data concurrently, such as:
  - **Lost update**: A transaction overwrites the changes made by another transaction that has not yet committed.
  - **Dirty read**: A transaction reads the uncommitted changes made by another transaction.
  - **Non-repeatable read**: A transaction reads the same data twice, but gets different results because another transaction has modified the data in between.
  - **Phantom read**: A transaction reads a set of data that satisfies some condition, but gets different results because another transaction has inserted or deleted some data that satisfies the same condition in between.
- There are different types of concurrency control mechanisms, such as:
  - **Locking**: A transaction acquires locks on the data items it needs to access or modify, and releases them when it is done. Locks can be exclusive (for writing) or shared (for reading). Locks prevent other transactions from accessing or modifying the same data items concurrently, thus ensuring isolation and preventing lost updates. However, locking may cause **deadlocks**, where two or more transactions are waiting for each other to release locks, or **starvation**, where a transaction is repeatedly denied access to a data item due to other transactions holding locks for a long time.
  - **Timestamping**: A transaction is assigned a unique timestamp when it starts, and uses it to order its operations on the data items. Timestamps can be either logical (based on a counter) or physical (based on the system clock). Timestamps ensure that older transactions have precedence over newer transactions, thus ensuring consistency and preventing lost updates and dirty reads. However, timestamping may cause **aborts**, where a transaction is rolled back and restarted due to conflicts with other transactions, or **cascading aborts**, where a transaction is rolled back and causes other transactions that depend on its results to be rolled back as well.
  - **Optimistic**: A transaction executes without any concurrency control until it is ready to commit, and then checks if there are any conflicts with other transactions. If there are no conflicts, the transaction commits; otherwise, it aborts and restarts. Optimistic concurrency control assumes that conflicts are rare, and avoids the overhead of locking or timestamping. However, optimistic concurrency control may cause a high rate of aborts if conflicts are frequent, or if transactions are long and access many data items.



### Transactions

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the operations of a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction executes as if it is the only one in the system, without interference from other transactions.
- Durability means that the effects of a committed transaction are permanent and survive any system failures.

### Concurrency Control

- Concurrency control is the process of managing simultaneous execution of transactions in a shared database, to ensure the serializability and correctness of the transactions.
- Concurrency control is needed to prevent conflicts and anomalies that may arise when multiple transactions access and update the same data concurrently.
- Concurrency control techniques can be broadly classified into two categories: lock-based protocols and timestamp-based protocols.
- Lock-based protocols use locks to control the access of transactions to data items. A lock is a mechanism that grants or denies permission to a transaction to read or write a data item.
- Timestamp-based protocols use timestamps to order the transactions and determine their precedence. A timestamp is a unique identifier that indicates the time at which a transaction is started.

### Distributed Transactions and Distributed Concurrency Control

- A distributed transaction is a transaction that accesses and updates data stored in multiple data servers that are connected by a computer network.
- A distributed transaction consists of a set of subtransactions, each of which is executed by one data server.
- A distributed transaction has the same ACID properties as a local transaction, but it also requires two additional properties: atomic commitment and global serializability.
- Atomic commitment means that either all the subtransactions of a distributed transaction are committed or none of them are.
- Global serializability means that the execution of a set of distributed transactions is equivalent to some serial execution of the same transactions.
- Distributed concurrency control is the process of synchronizing distributed transactions in such a way that the ACID properties are not violated by their interleaved execution.
- Distributed concurrency control makes sure that all subtransactions of a set of distributed transactions are serialized identically in all data servers involved.
- Distributed concurrency control techniques can be based on locks, timestamps, or other methods, such as optimistic concurrency control, voting protocols, or quorum consensus.



### Nested transactions for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A transaction is a unit of work that accesses and possibly modifies data in a database or a distributed system.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that a transaction either completes all its operations or none of them.
- Consistency means that a transaction preserves the integrity constraints of the data.
- Isolation means that a transaction does not interfere with other concurrent transactions.
- Durability means that the effects of a committed transaction are permanent and survive failures.

- A nested transaction is a transaction that contains other transactions as subtransactions.
- A nested transaction can be used to divide a complex transaction into smaller and more manageable units.
- A nested transaction can also be used to support partial rollback and recovery, as well as concurrency control and deadlock prevention.
- A nested transaction has a parent transaction and zero or more child transactions.
- A child transaction can also have its own child transactions, forming a hierarchy of transactions.
- A nested transaction can be in one of the following states: active, committed, aborted, or prepared.

- A nested transaction is active when it is executing its operations.
- A nested transaction is committed when it completes all its operations successfully and notifies its parent transaction.
- A nested transaction is aborted when it encounters an error or is aborted by its parent transaction.
- A nested transaction is prepared when it is ready to commit or abort, but waits for the decision of its parent transaction.

- A nested transaction can commit or abort independently of its parent transaction, but its final outcome depends on the outcome of its parent transaction.
- A nested transaction can use one of the following commit protocols: flat, closed, open, or sagas.

- A flat commit protocol treats a nested transaction as a single flat transaction, ignoring the subtransaction boundaries.
- A flat commit protocol is simple and efficient, but does not support partial rollback and recovery, nor concurrency control and deadlock prevention at the subtransaction level.
- A flat commit protocol requires a two-phase commit protocol (2PC) to coordinate the commit or abort of all the servers involved in a distributed transaction.

- A closed commit protocol preserves the subtransaction boundaries and allows a nested transaction to commit or abort its subtransactions independently.
- A closed commit protocol supports partial rollback and recovery, as well as concurrency control and deadlock prevention at the subtransaction level.
- A closed commit protocol requires a nested two-phase commit protocol (N2PC) to coordinate the commit or abort of all the subtransactions and servers involved in a distributed transaction.

- An open commit protocol allows a nested transaction to commit or abort its subtransactions independently, but also allows other transactions to access the data modified by the subtransactions before the parent transaction commits or aborts.
- An open commit protocol supports partial rollback and recovery, as well as concurrency control and deadlock prevention at the subtransaction level, but also improves the performance and availability of the system by reducing the locking time and the blocking of other transactions.
- An open commit protocol requires a multilevel two-phase commit protocol (M2PC) to coordinate the commit or abort of all the subtransactions and servers involved in a distributed transaction, as well as to handle the conflicts and dependencies among the subtransactions and other transactions.

- A sagas commit protocol allows a nested transaction to commit or abort its subtransactions independently, but also allows other transactions to access the data modified by the subtransactions before the parent transaction commits or aborts, and provides a compensation mechanism to undo the effects of the subtransactions in case of abort.
- A sagas commit protocol supports partial rollback and recovery, as well as concurrency control and deadlock prevention at the subtransaction level, but also improves the performance and availability of the system by reducing the locking time and the blocking of other transactions, and by avoiding the need for a global coordinator and a two-phase commit protocol.
- A sagas commit protocol requires each subtransaction to have a compensating transaction that can undo its effects, and a saga manager that can execute the compensating transactions in reverse order in case of abort.

- References:
  -  Nested Transactions in Distributed Systems | IEEE Journals & Magazine
  -  Flat & Nested Distributed Transactions - GeeksforGeeks
  -  Nested Transactions in Distributed Systems | Semantic Scholar



### Locks for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- Locks are mechanisms that prevent concurrent transactions from accessing or modifying the same data item in an inconsistent way .
- Locks can be applied on different levels of granularity, such as records, pages, tables, or databases .
- Locks can be of different types, such as shared locks, exclusive locks, or update locks .
- Shared locks allow multiple transactions to read the same data item, but not to modify it .
- Exclusive locks allow only one transaction to read or modify the same data item, and block other transactions from accessing it .
- Update locks are a combination of shared and exclusive locks, that allow a transaction to read a data item and later upgrade to an exclusive lock if it wants to modify it .
- Locks are usually acquired and released by following some locking protocol, such as two-phase locking, timestamp ordering, or optimistic concurrency control  .
- Two-phase locking requires that a transaction acquires all the locks it needs before releasing any lock, and releases all the locks after it has acquired all the locks .
- Timestamp ordering assigns a unique timestamp to each transaction, and uses the timestamp to determine the order of conflicting operations on the same data item .
- Optimistic concurrency control assumes that conflicts are rare, and allows transactions to execute without locking, but validates them before committing to ensure serializability .
- Locks can be managed by a centralized or a distributed lock manager, depending on the architecture of the distributed system  .
- A centralized lock manager maintains a global lock table and handles all the lock requests from the transactions .
- A distributed lock manager partitions the lock table and distributes it among the nodes of the system, and uses a communication protocol to coordinate the lock requests from the transactions  .
- Locks can improve the consistency and isolation of transactions, but they can also cause problems such as deadlocks, livelocks, starvation, or reduced concurrency  .
- Deadlocks occur when two or more transactions are waiting for each other to release the locks they hold  .
- Livelocks occur when two or more transactions repeatedly yield to each other and make no progress  .
- Starvation occurs when a transaction is repeatedly denied access to a data item due to the presence of other transactions with higher priority or longer duration  .
- Reduced concurrency occurs when locks are held too long or too frequently, and limit the parallelism of transactions  .
- Locks can be optimized by using techniques such as lock escalation, lock conversion, lock caching, or lock timeout  .
- Lock escalation is the process of replacing multiple fine-grained locks with a single coarse-grained lock, to reduce the overhead of lock management  .
- Lock conversion is the process of changing the type of a lock, such as from shared to exclusive, or vice versa, to adapt to the needs of a transaction  .
- Lock caching is the process of keeping the locks in memory, rather than in disk, to improve the performance of lock operations  .
- Lock timeout is the process of setting a limit on how long a transaction can wait for a lock, to avoid blocking or starvation  .



### Optimistic Concurrency Control

- Optimistic concurrency control (OCC) is a concurrency control method applied to transactional systems such as relational database management systems and software transactional memory.
- OCC assumes that multiple transactions can frequently complete without interfering with each other, and does not use locking or timestamping techniques to prevent conflicts .
- Instead, a transaction is executed without restrictions until it is committed, and then it is validated to check if any conflicts occurred with other concurrent transactions.
- If a conflict is detected, the transaction is aborted and restarted, otherwise it is committed.
- OCC has three phases: read, validation and write.
  - In the read phase, the transaction reads the data from the database and performs its operations, without acquiring any locks or updating the database.
  - In the validation phase, the transaction checks if any other transaction has modified the data that it has read or written, using some validation rules.
  - In the write phase, if the validation succeeds, the transaction writes its updates to the database, otherwise it aborts and restarts.
- OCC is suitable for distributed systems, where locking or timestamping may incur high communication overhead or introduce delays.
- OCC can improve the performance and scalability of distributed transaction systems, by allowing more concurrency and reducing blocking and waiting .
- However, OCC may also incur high costs of aborting and restarting transactions, especially if the conflict rate is high or the transactions are long and complex .
- Therefore, OCC should be used carefully, depending on the characteristics of the workload and the system .



### Timestamp ordering for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- Timestamp ordering is a class of **optimistic** concurrency control protocols that assume that transaction conflicts are rare .
- Timestamp ordering does not require transactions to acquire locks before they are allowed to read or write to a database object. Instead, it uses **timestamps** to determine the serializability order of transactions .
- A timestamp is a monotonically increasing number that is often based on the system clock. It is assigned to each transaction when it starts .
- A schedule is serializable if it is equivalent to some serial schedule, where transactions are executed one after another without interleaving.
- Timestamp ordering ensures that the transactions are executed in a serializable order by enforcing two rules: the **read-write rule** and the **write-write rule**.
- The read-write rule states that a transaction T can read an object X only if the timestamp of T is greater than or equal to the timestamp of the last transaction that wrote X. If this condition is not satisfied, T is aborted and restarted with a new timestamp.
- The write-write rule states that a transaction T can write an object X only if the timestamp of T is greater than the timestamp of the last transaction that wrote X. If this condition is not satisfied, T is aborted and restarted with a new timestamp.
- Timestamp ordering can be implemented in a centralized or distributed system. In a centralized system, a single timestamp generator can assign timestamps to transactions. In a distributed system, each site can have its own timestamp generator, but they must ensure that the timestamps are globally unique and consistent.
- Timestamp ordering has some advantages and disadvantages. Some advantages are: it avoids deadlock, it reduces locking overhead, and it allows read-only transactions to execute without any concurrency control . Some disadvantages are: it may abort and restart transactions unnecessarily, it may cause starvation of some transactions, and it may not preserve the original order of transactions .



### Comparison of methods for concurrency control

Concurrency control is the process of managing the simultaneous execution of transactions in a distributed system, such that the ACID properties are preserved and the system remains consistent and correct. There are various methods for concurrency control, each with its own advantages and disadvantages. Some of the common methods are:

- **Two-phase locking protocol (2PL)**: This method uses locks to grant exclusive access to data items for transactions. A transaction must acquire a lock on a data item before reading or writing it, and release the lock after finishing its operation. There are two phases in this protocol: the growing phase, where a transaction acquires locks and does not release any; and the shrinking phase, where a transaction releases locks and does not acquire any. This protocol ensures serializability, which means that the concurrent execution of transactions is equivalent to some serial execution. However, it may cause deadlock, where two or more transactions are waiting for each other to release locks, and thus cannot proceed. It may also cause starvation, where some transactions are repeatedly blocked by others and never get a chance to execute. Moreover, it may reduce concurrency, as transactions have to wait for locks to be released by others .

- **Timestamp ordering protocol (TO)**: This method assigns a unique timestamp to each transaction, which reflects its start time or priority. A transaction must follow the timestamp order when accessing data items, meaning that it can only read or write a data item if its timestamp is smaller than the timestamp of any other transaction that has accessed the same data item. This protocol ensures serializability and avoids deadlock, as transactions do not wait for each other. However, it may cause abortion, where a transaction is aborted and restarted if it violates the timestamp order. It may also cause starvation, where some transactions are repeatedly aborted and never get a chance to execute. Moreover, it may reduce concurrency, as transactions have to abort and restart if they encounter a newer data item .

- **Multi-version concurrency control (MVCC)**: This method maintains multiple versions of each data item, each with a timestamp that indicates when it was created or modified. A transaction can read the version of a data item that is consistent with its timestamp, and write a new version of a data item with its own timestamp. This protocol ensures serializability and avoids deadlock and abortion, as transactions do not wait for each other or abort due to conflicts. However, it may cause storage overhead, as multiple versions of data items have to be stored and managed. It may also cause consistency issues, as transactions may read stale or outdated versions of data items .

- **Validation concurrency control (VCC)**: This method divides the execution of a transaction into three phases: the read phase, where a transaction reads data items from the database; the validation phase, where a transaction checks if it has violated any concurrency control rules; and the write phase, where a transaction writes data items to the database. This protocol ensures serializability and avoids deadlock, as transactions do not wait for each other or hold locks. However, it may cause abortion, where a transaction is aborted and restarted if it fails the validation phase. It may also cause concurrency, as transactions have to delay their write operations until the validation phase .

These methods can be compared based on the following criteria:

- **Performance**: The performance of a concurrency control method depends on the workload characteristics, such as the number of transactions, the number of data items, the read-write ratio, the conflict probability, and the network latency. Generally, 2PL has the lowest performance, as it causes a lot of locking and waiting overhead. TO and VCC have moderate performance, as they cause some abortion and restarting overhead. MVCC has the highest performance, as it causes the least overhead and allows the most concurrency .

- **Complexity**: The complexity of a concurrency control method depends on the implementation and management of the concurrency control rules, such as the locking, timestamping, versioning, and validation mechanisms. Generally, 2PL and TO have the lowest complexity, as they are relatively simple and straightforward to implement and manage. MVCC and VCC have moderate complexity, as they require more sophisticated and elaborate mechanisms to handle multiple versions and validation phases. However, the complexity of any method may increase in a distributed system, as it has to deal with network communication, synchronization, and failure recovery .

- **Scalability**: The scalability of a concurrency control method



## Unit 9 - Distributed Transactions

- A distributed transaction is a type of transaction that involves two or more network hosts, usually providing transactional resources, such as databases, message queues, file systems, etc.   
- A distributed transaction is coordinated by a transaction manager, which is responsible for creating and managing a global transaction that encompasses all the operations against the transactional resources.   
- A distributed transaction has the same ACID properties as a local transaction, which are atomicity, consistency, isolation, and durability. However, achieving these properties in a distributed environment is more challenging and requires additional mechanisms, such as two-phase commit, distributed locking, concurrency control, etc.  
- A distributed transaction can improve the performance, availability, and scalability of an application, by allowing it to access and update data across multiple hosts. However, it also introduces more complexity, overhead, and risks, such as network failures, partial commits, deadlocks, etc.  
- A distributed transaction can be classified into different types, such as flat, nested, multidatabase, sagas, etc., depending on the structure, scope, and isolation level of the transaction.



### Flat and Nested Distributed Transactions

- A **flat or nested transaction** that accesses objects handled by different servers is referred to as a **distributed transaction** .
- When a distributed transaction reaches its end, in order to maintain the **atomicity property** of the transaction, it is mandatory that all of the servers involved in the transaction either **commit** the transaction or **abort** it .
- Distributed transactions can be structured in two different ways: **flat transactions** and **nested transactions** .
- A **flat transaction** has a single initiating point (**Begin**) and a single end point (**Commit** or **Abort**). They are usually very simple and are generally used for short activities rather than larger ones .
- A **nested transaction** is a transaction that consists of a number of **subtransactions**, each of which can be committed or aborted independently. A nested transaction has a **root transaction** and several **subordinate transactions**. The root transaction can only commit if all of its subordinates have committed, and it must abort if any of its subordinates have aborted  .
- Nested transactions provide a way to **decompose** a complex transaction into smaller units that can be executed **concurrently** and **recovered** independently. They also allow for **partial rollback** of a transaction without affecting the whole transaction.
- The **distributed transaction** takes a **bottom-up** approach while the **nested transaction** takes a **top-down** approach to decompose a complex transaction into subtransactions.
- Distributed transactions provide **global integrity constraints** over multiple resources. These resources soon started to be **heterogeneous** as well.



### Atomic Commit Protocols for Distributed Transactions

- A distributed transaction is a transaction that involves multiple servers or nodes in a distributed system.
- An atomic commit protocol is a protocol that ensures that a distributed transaction is either committed or rolled back in its entirety, even if the system fails or some of the nodes fail or crash.
- Ensuring atomic commit is important for maintaining the consistency and integrity of the data in the distributed system.
- There are different types of atomic commit protocols, such as two-phase commit, three-phase commit, parallel commit, and failure-aware commit.
- Two-phase commit (2PC) is the most widely used atomic commit protocol. It consists of two phases: a prepare phase and a commit phase. In the prepare phase, a coordinator node asks all the participant nodes to vote on whether they are ready to commit or not. In the commit phase, the coordinator node decides whether to commit or abort the transaction based on the votes, and informs all the participant nodes of the decision.
- Three-phase commit (3PC) is an extension of 2PC that adds a pre-commit phase between the prepare and commit phases. In the pre-commit phase, the coordinator node informs all the participant nodes that they have agreed to commit, and waits for their acknowledgments. In the commit phase, the coordinator node sends the final commit message to all the participant nodes. 3PC can tolerate more failures than 2PC, but it also introduces more latency and message overhead.
- Parallel commit is a new atomic commit protocol that reduces the latency of transactions down to only a single round-trip of distributed consensus. It does not use a coordinator node, but instead relies on the participant nodes to reach consensus on the transaction status. Each participant node writes its transaction record to a distributed log, and waits for the log to reach a quorum of replicas. Once the quorum is reached, the participant node can commit the transaction locally, without waiting for other nodes. Parallel commit can achieve high performance and availability, but it requires a reliable and fast distributed log service.
- Failure-aware commit (FLAC) is another new atomic commit protocol that aims to improve the performance and availability of distributed transactions in the presence of failures. It uses a coordinator node, but it also allows the participant nodes to commit independently if they detect that the coordinator node has failed. FLAC uses a two-phase transaction processing framework, where the first phase performs the transaction logic, and the second phase performs the atomic commit. FLAC can adapt to different failure scenarios and optimize the commit latency and message overhead accordingly.



### Concurrency control in distributed transactions

- Concurrency control is the process of managing the concurrent execution of transactions in a distributed database system, such that the ACID properties are preserved.
- Concurrency control aims to ensure the correctness, consistency, and isolation of transactions, while also maximizing the degree of concurrency and minimizing the overhead of synchronization.
- Concurrency control can be classified into two main categories: pessimistic and optimistic.
  - Pessimistic concurrency control assumes that conflicts are likely to occur and uses locking mechanisms to prevent them. Locking-based protocols require transactions to acquire locks on the data items they access, and release them when they are done. Locks can be shared or exclusive, depending on the operation (read or write) performed by the transaction. Locking-based protocols can be centralized, decentralized, or distributed .
  - Optimistic concurrency control assumes that conflicts are rare and allows transactions to execute without locking. However, before committing, transactions have to validate their read and write sets against other concurrent transactions. If a conflict is detected, the transaction is aborted and restarted. Optimistic concurrency control can be based on timestamps, validation numbers, or versions .
- Concurrency control in distributed transactions faces several challenges, such as:
  - Network latency and communication costs, which can affect the performance and scalability of the protocols.
  - Network failures and partitions, which can cause inconsistency and unavailability of the data.
  - Data replication and consistency, which require additional mechanisms to ensure that copies of the same data item are synchronized across different servers.
  - Deadlocks and livelocks, which can occur when transactions wait for each other to release locks or validate their operations .
- Concurrency control in distributed transactions can be improved by using various techniques, such as:
  - Adaptive concurrency control, which adjusts the level of concurrency and the type of protocol based on the workload characteristics and the system state.
  - Semantic concurrency control, which exploits the application semantics and the data dependencies to allow more concurrency and reduce conflicts.
  - Distributed commit protocols, which coordinate the final outcome of a distributed transaction across multiple servers. The most common protocol is the two-phase commit (2PC), which consists of a prepare phase and a commit phase. However, 2PC is blocking, meaning that if a server fails, the transaction cannot proceed. Therefore, variants of 2PC have been proposed, such as 3PC, 2PC*, and Paxos commit .
  - Compensation and sagas, which allow transactions to undo their effects in case of failures or conflicts, by executing compensating actions or reversing the sequence of operations.



### Distributed Deadlocks

- A **distributed deadlock** is a situation where a set of processes in a distributed system are waiting for each other to release resources or messages, and none of them can proceed  .
- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems .
- Distributed deadlocks are harder to detect, avoid, and prevent than deadlocks in centralized systems, because there is no single authority that can oversee resource allocation and monitor the state of the system.
- There are three main approaches to handle distributed deadlocks :
  - **Prevention**: This approach tries to ensure that deadlocks never occur by imposing some constraints on resource allocation, such as ordering the resources, granting requests only if they do not create cycles, or limiting the number of resources that a process can hold at a time. This approach may be costly and inefficient, as it may require a lot of communication and synchronization among the nodes, and it may reduce the concurrency and utilization of the system.
  - **Avoidance**: This approach tries to avoid deadlocks by making careful decisions on resource allocation, based on the current and future requests of the processes. This approach requires the knowledge of the resource requirements and dependencies of each process, which may not be available or accurate in a distributed system. This approach may also be expensive and complex, as it may involve a lot of computation and coordination among the nodes, and it may impose some restrictions on the system behavior.
  - **Detection and recovery**: This approach tries to detect deadlocks after they occur, and then recover from them by aborting or restarting some of the processes involved in the deadlock, or by preempting or releasing some of the resources held by them. This approach does not prevent or avoid deadlocks, but rather deals with them when they happen. This approach may be simpler and more flexible than the previous ones, as it does not require a lot of information or control over the system, and it allows more concurrency and freedom in the system. However, this approach may also be costly and risky, as it may involve a lot of overhead and delay in detecting and resolving deadlocks, and it may cause some loss of work or inconsistency in the system.

- There are two main techniques to detect distributed deadlocks :
  - **Global wait-for graph**: This technique involves constructing a global graph that represents the waiting relationships among the processes and resources in the system, and then checking for cycles in the graph. A cycle in the graph indicates a deadlock. The global graph can be constructed from local graphs at each node, by sending and merging the information to a central node or to all the nodes. This technique may be simple and accurate, but it may also be expensive and slow, as it requires a lot of communication and computation, and it may not reflect the current state of the system due to message delays or failures.
  - **Distributed algorithm**: This technique involves running a distributed algorithm among the nodes, such as edge chasing or probe-based algorithms, that can detect cycles in the waiting relationships without constructing a global graph. These algorithms typically use special messages, such as probes or queries, that are sent along the waiting paths and returned to the sender if a cycle is found. This technique may be faster and more scalable, but it may also be more complex and less reliable, as it depends on the correctness and timeliness of the messages, and it may generate false or phantom deadlocks due to concurrency or inconsistency in the system.



### Transaction recovery for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

- Transaction recovery is the process of restoring the consistency and integrity of a distributed database after a failure or an abort of a transaction.
- A failure in a distributed system can be caused by various reasons, such as network partition, site crash, communication link failure, disk failure, or software error.
- A transaction in a distributed system may involve multiple sites, each executing a subtransaction on a local database. If any of the subtransactions fails or aborts, the whole transaction must be rolled back to ensure atomicity and isolation.
- Transaction recovery in a distributed system is more complex than in a centralized system, because it involves coordination and communication among multiple sites, and it must deal with the possibility of partial or inconsistent information.
- There are two main approaches for transaction recovery in a distributed system: logging and shadow versions.
  - Logging is a technique that records the changes made by a transaction in a persistent log file, before applying them to the database. The log file can be used to undo or redo the changes in case of a failure or an abort. Logging can be classified into two types: undo logging and redo logging.
    - Undo logging records the old values of the data items before they are modified by a transaction. If a transaction aborts, the log file can be used to restore the data items to their original values. Undo logging requires that the log file is written before the database is updated, which is called write-ahead logging (WAL).
    - Redo logging records the new values of the data items after they are modified by a transaction. If a transaction commits, the log file can be used to reapply the changes in case of a failure. Redo logging requires that the log file is written before the transaction commits, which is called force logging.
  - Shadow versions is a technique that creates a copy of the database before a transaction starts, and modifies the copy instead of the original database. The copy is called a shadow version, and the original database is called a current version. If a transaction commits, the shadow version becomes the new current version. If a transaction aborts, the shadow version is discarded and the current version remains unchanged. Shadow versions can avoid the overhead of logging, but they require more storage space and may incur more disk accesses.



## Unit 10 - Replication

- Replication is a biological process of duplicating or producing an exact copy, such as a polynucleotide strand (DNA) .
- DNA replication is one of the most vital biological processes in all living things. It is a molecular process taking place in dividing cells by which the DNA creates a copy of itself .
- Replication is essential for the transmission of genetic information from one generation to the next, the maintenance of genetic stability, and the repair of DNA damage .
- Replication is also important for research statistics, as it refers to the duplication of a laboratory or experimental procedure, which can help to reduce errors and increase reliability .
- Replication can be classified into two types: biological replicates and technical replicates .
  - Biological replicates are parallel measurements of biologically distinct samples that capture random biological variation, which can be a subject of study or a source of noise itself .
  - Technical replicates are repeated measurements of the same sample under identical conditions, which can help to assess the precision and reproducibility of the experimental method .
- Replication can also be categorized into three modes: semiconservative, conservative, and dispersive .
  - Semiconservative replication is the most common mode of DNA replication, in which each strand of the original DNA molecule serves as a template for the synthesis of a new complementary strand, resulting in two identical DNA molecules, each consisting of one old and one new strand .
  - Conservative replication is a hypothetical mode of DNA replication, in which the original DNA molecule remains intact and a new copy is synthesized from entirely new nucleotides, resulting in one old and one new DNA molecule .
  - Dispersive replication is another hypothetical mode of DNA replication, in which the original DNA molecule is randomly broken into fragments and each fragment serves as a template for the synthesis of a new strand, resulting in two mixed DNA molecules, each consisting of old and new segments .
- Replication can also be distinguished by the direction of synthesis: leading strand and lagging strand .
  - Leading strand is the strand of DNA that is synthesized continuously in the same direction as the movement of the replication fork, which is the point where the DNA helix is unwound and separated into two single strands .
  - Lagging strand is the strand of DNA that is synthesized discontinuously in the opposite direction of the replication fork, in short segments called Okazaki fragments, which are later joined by an enzyme called DNA ligase .
- Replication involves several enzymes and proteins that work together to ensure the accuracy and efficiency of the process .
  - Helicase is the enzyme that opens up the DNA at the replication fork by breaking the hydrogen bonds between the complementary bases .
  - Single-strand binding proteins are the proteins that coat the DNA around the replication fork to prevent rewinding of the DNA and protect it from degradation .
  - Topoisomerase is the enzyme that works at the region ahead of the replication fork to prevent supercoiling, which is the twisting of the DNA due to the unwinding .
  - Primase is the enzyme that synthesizes a short RNA primer, which is a sequence of nucleotides that provides a starting point for DNA polymerase, the enzyme that adds new nucleotides to the growing DNA strand .
  - DNA polymerase is the enzyme that catalyzes the formation of phosphodiester bonds between the nucleotides, following the base-pairing rules of A with T and G with C .
  - DNA ligase is the enzyme that joins the Okazaki fragments on the lagging strand by forming phosphodiester bonds between them .



### System model and group communication for replication in distributed systems

- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by exchanging messages.
- Replication is a technique to improve the availability, reliability, performance, and fault tolerance of a distributed system by creating and maintaining multiple copies of the same data or service on different processes or nodes.
- A system model is a set of assumptions and properties that describe the behavior and characteristics of a distributed system, such as the communication model, the failure model, the timing model, and the security model.
- A group is a subset of processes in a distributed system that share some common interest or functionality, such as a replicated service, a multicast group, or a cluster.
- Group communication is a mechanism to send and receive messages among the members of a group in a distributed system, such as broadcast, multicast, or anycast.
- Group communication can be classified into two types: reliable and unreliable.
  - Reliable group communication ensures that all the members of a group receive the same messages in the same order, regardless of failures or network delays.
  - Unreliable group communication does not guarantee any delivery or ordering properties, and may result in message losses, duplications, or reorderings.
- Group communication can also be classified into two modes: atomic and non-atomic.
  - Atomic group communication ensures that a message is delivered to all the members of a group or none of them, and that all the members agree on the delivery status of a message.
  - Non-atomic group communication does not guarantee any atomicity property, and may result in partial or inconsistent deliveries of a message.
- Group communication can be implemented using various protocols and algorithms, such as IP multicast, gossip, reliable broadcast, reliable multicast, atomic broadcast, atomic multicast, consensus, and virtual synchrony.
- Group communication is essential for replication in distributed systems, as it enables the coordination and synchronization of the replicas, the dissemination and propagation of updates, the detection and resolution of conflicts, and the maintenance of consistency and coherence among the replicas.



### Fault-Tolerant Services by Replication in Distributed Systems

- Fault-tolerance is the ability of a system to continue providing correct service despite the occurrence of failures, such as server crashes, network partitions, or malicious attacks.
- Replication is a technique that creates and maintains multiple copies of the same entity (such as data, service, or object) in a distributed system, so that the system can tolerate some degree of failures without losing availability or consistency.
- Replication can be classified into two main categories: passive replication and active replication.
  - Passive replication (or primary-backup replication) is a technique that assigns a single replica (the primary) to handle all the requests from the clients, while the other replicas (the backups) only update their state based on the messages from the primary. If the primary fails, one of the backups takes over as the new primary.
  - Active replication (or state machine replication) is a technique that assigns all the replicas to handle the requests from the clients in the same order, using a consensus protocol to agree on the order. All the replicas execute the same operations and produce the same results, so that any replica can respond to the clients.
- The correctness criterion for replicated services is linearizability, which means that the service should behave as if there is a single copy of the entity and every operation appears to take effect atomically at some point between its invocation and response.
- The challenges of implementing fault-tolerant replication in distributed systems include:
  - How to ensure that the replicas are consistent with each other, despite the possibility of failures or network delays.
  - How to handle concurrent and conflicting requests from different clients, and ensure that the replicas agree on a total order of the requests.
  - How to balance the trade-offs between availability, consistency, and performance, and cope with the limitations of the CAP theorem, which states that it is impossible for a distributed system to simultaneously provide all three of the following guarantees: consistency, availability, and partition tolerance.
  - How to deal with Byzantine faults, which are arbitrary or malicious behaviors of some replicas or clients, such as sending incorrect or conflicting messages, or colluding with each other to compromise the system.



### Highly Available Services for the Notes of the Unit 10 - Replication in the Subject of Distributed System

- A highly available service is a service that can provide continuous and reliable operation despite the presence of failures in the system.
- Replication is a technique for increasing the availability of a service by creating and maintaining multiple copies of the service's data or state across different nodes in a distributed system.
- Replication can also improve the performance, scalability, and fault tolerance of a service by reducing the load on a single node, allowing parallel processing of requests, and masking failures of some nodes.
- Replication can be classified into two types: eager replication and lazy replication.
  - Eager replication ensures that all replicas are updated synchronously whenever a write operation occurs, thus providing strong consistency and fault tolerance, but at the cost of higher latency and lower availability.
  - Lazy replication allows replicas to be updated asynchronously after a write operation, thus providing higher availability and lower latency, but at the cost of weaker consistency and possible conflicts.
- Replication can be implemented using various protocols, such as primary-backup, quorum-based, state machine, and epidemic protocols.
  - Primary-backup protocols assign a primary replica to handle all write operations and propagate them to backup replicas, thus ensuring consistency and fault tolerance, but introducing a single point of failure and performance bottleneck.
  - Quorum-based protocols require a minimum number of replicas (a quorum) to agree on each read and write operation, thus allowing trade-offs between consistency, availability, and performance, but increasing the complexity and overhead of coordination.
  - State machine protocols model the service as a deterministic state machine and use a consensus algorithm to ensure that all replicas execute the same sequence of commands, thus providing strong consistency and fault tolerance, but requiring reliable and ordered communication.
  - Epidemic protocols disseminate updates among replicas using a probabilistic gossip mechanism, thus providing high availability and scalability, but allowing temporary inconsistencies and conflicts.
- Replication can be applied to various types of services, such as databases, file systems, web servers, and distributed applications.
  - Databases can use replication to improve the availability and performance of data access, as well as to support disaster recovery and load balancing.
  - File systems can use replication to ensure the durability and reliability of file storage, as well as to support caching and offline access.
  - Web servers can use replication to handle the increasing demand and traffic of web applications, as well as to provide faster and more reliable service to users.
  - Distributed applications can use replication to enhance the functionality and quality of service of their components, such as messaging, coordination, and computation.



### Transactions with replicated data

- Transactions are a sequence of operations that are executed as a single logical unit of work.
- Transactions have the properties of atomicity, consistency, isolation, and durability (ACID) to ensure data integrity and reliability.
- Replication is the process of maintaining copies of data at multiple sites to improve availability, performance, and fault tolerance .
- Replication can be classified into two types: eager replication and lazy replication.
  - Eager replication ensures that all copies of data are updated as soon as a transaction commits, using a two-phase commit protocol .
  - Lazy replication allows some copies of data to be updated later, using a log-based or timestamp-based reconciliation mechanism .
- Transactions with replicated data pose some challenges, such as :
  - How to ensure serializability and consistency of transactions across multiple sites?
  - How to handle conflicts and concurrency control among transactions accessing the same data items?
  - How to recover from failures and maintain data availability and durability?
- Some possible solutions to these challenges are  :
  - Using a primary copy or a quorum-based approach to designate a subset of replicas as the authoritative source of data for transactions.
  - Using a locking or a timestamp-based protocol to coordinate transactions and prevent conflicts and anomalies.
  - Using a distributed commit protocol or a compensation mechanism to ensure atomicity and durability of transactions.
  - Using a replication manager or a middleware component to abstract the details of replication from the application layer.

