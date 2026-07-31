

# Distributed System

A distributed system is a system whose components are located on different networked computers, which communicate and coordinate their actions by passing messages to one another. A distributed system can also be defined as a number of independent computers linked by a network, or a computing environment in which various components are spread across multiple computers (or other computing devices) on a network.

Some of the advantages of distributed systems are:

- They can share different resources and capabilities, to provide users with a single and integrated coherent network.
- They can achieve higher performance, scalability, reliability, and availability than centralized systems.
- They can tolerate failures and faults of some components without affecting the whole system.

Some of the challenges of distributed systems are:

- They have to deal with concurrency, consistency, synchronization, and replication issues.
- They have to handle partial failures, network delays, and security threats.
- They have to cope with heterogeneity, diversity, and dynamism of the components and the network.

Some of the examples of distributed systems are:

- The Internet, which is a global network of interconnected computers and devices that communicate using various protocols.
- Cloud computing, which is a model of providing on-demand access to shared computing resources and services over the Internet.
- Peer-to-peer networks, which are networks of equal nodes that cooperate to share resources and information without a central authority.
- Distributed databases, which are databases that store data across multiple servers or locations, and provide a unified view of the data to the users.
- Distributed file systems, which are file systems that allow access to files stored on multiple hosts or devices, and provide a consistent and transparent view of the files to the users.



## Unit 1 - Characterization of Distributed Systems

A distributed system is a collection of independent computers that appear to the users as a single coherent system. 

Some of the characteristics of distributed systems are:

- Concurrency: The computers in a distributed system can execute multiple processes simultaneously, without interfering with each other.
- Scalability: The distributed system can accommodate more computers, users, or resources without degrading the performance or functionality of the system.
- Fault tolerance: The distributed system can continue to operate correctly even if some of the computers fail or become unavailable.
- Transparency: The distributed system can hide the details of its internal structure, location, and communication from the users, so that they can interact with the system as if it were a single entity.
- Heterogeneity: The distributed system can support different types of computers, operating systems, networks, and protocols, and provide a uniform interface to the users.

Some of the challenges of distributed systems are:

- Coordination: The distributed system must ensure that the computers cooperate and synchronize their actions to achieve a common goal, while avoiding conflicts and inconsistencies.
- Communication: The distributed system must provide reliable, efficient, and secure communication among the computers, and handle the issues of latency, bandwidth, and congestion.
- Consistency: The distributed system must maintain a consistent view of the data and the state of the system across the computers, and cope with the problems of replication, concurrency, and caching.
- Security: The distributed system must protect the data and the resources from unauthorized access, modification, or disclosure, and deal with the threats of malicious attacks, eavesdropping, and impersonation.
- Performance: The distributed system must optimize the use of the resources and the network, and balance the load and the workload among the computers, and minimize the overhead and the response time.



### Introduction for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- A distributed system has the following characteristics:
  - Concurrency: The components of a distributed system can execute concurrently, without interfering with each other.
  - No global clock: There is no global notion of time in a distributed system. Each component has its own local clock, which may not be synchronized with others.
  - Independent failures: The components of a distributed system can fail independently, without affecting the whole system. The system should be able to tolerate and recover from failures.
  - Heterogeneity: The components of a distributed system can have different hardware, software, network, and data formats. The system should be able to hide the heterogeneity from the users and provide a uniform interface.
- A distributed system has the following advantages:
  - Scalability: A distributed system can grow in size and performance by adding more components, without affecting the existing ones.
  - Availability: A distributed system can provide continuous service, even in the presence of failures, by replicating and distributing the data and computation across multiple components.
  - Fault tolerance: A distributed system can cope with failures, by detecting, masking, and recovering from them, without compromising the correctness and consistency of the system.
  - Transparency: A distributed system can hide the complexity and diversity of its components from the users, and provide a simple and consistent view of the system.
  - Resource sharing: A distributed system can allow the users to access and share the resources (such as data, files, devices, services, etc.) that are distributed across the system.



### Examples of distributed systems

A distributed system is a collection of independent computers that communicate and coordinate their actions by passing messages. The computers in a distributed system may be physically close or geographically dispersed, and they may be connected by a network or a bus. Distributed systems can provide higher performance, reliability, scalability, and availability than centralized systems.

Some examples of distributed systems are:

- **Telecommunication networks**: Telephone networks are an early example of a peer-to-peer network, where each node can initiate or receive calls. Cellular and telephone networks are forms and examples of distributed networks. They use protocols such as TCP/IP, HTTP, and SMTP to exchange data and messages.  
- **Real-time systems**: Many industries use real-time systems distributed in various areas, locally and globally. For example, air traffic control systems, power grid systems, industrial control systems, and online gaming systems are all examples of real-time distributed systems. They require fast and accurate communication, synchronization, and fault tolerance.  
- **Distributed database systems**: A distributed database has locations across multiple servers, physical locations, or both. The data can be replicated or partitioned to improve performance, availability, and consistency. Examples of distributed database systems are Google's Bigtable, Amazon's Dynamo, and MongoDB.  
- **Distributed computing platforms**: A distributed computing platform is a system that allows multiple computers to work together on a common task, such as scientific computing, data analysis, or web crawling. Examples of distributed computing platforms are Apache Hadoop, Apache Spark, and Google's MapReduce.  
- **Content delivery networks**: A content delivery network (CDN) is a system that distributes web content to users based on their geographic location, network conditions, and content type. A CDN consists of a network of servers that cache and deliver web content, such as images, videos, and web pages. Examples of CDNs are Akamai, Cloudflare, and Amazon CloudFront.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of resource sharing and the web challenges in distributed systems:

### Resource sharing and the web challenges in distributed systems

- A distributed system is a collection of independent computers that appears to its users as a single coherent system .
- Resource sharing is one of the main motivations for building distributed systems. Resources can be hardware, software, or data that are available in the system .
- Resource sharing can be achieved in different ways, such as:
  - Data migration: transferring data from one location to another in the system.
  - Computation migration: transferring computation from one location to another in the system.
  - Service migration: transferring services from one location to another in the system.
  - Remote invocation: invoking a service or a function on a remote location in the system.
- The web is an example of a large-scale distributed system that enables resource sharing among millions of users and devices.
- The web faces several challenges in distributed systems, such as:
  - Scalability: the ability to handle increasing load and demand without degrading the performance or functionality of the system .
  - Heterogeneity: the ability to communicate and interoperate with different devices, platforms, languages, and protocols in the system .
  - Fault tolerance: the ability to recover from failures and errors in the system without affecting the availability or correctness of the system.
  - Security: the ability to protect the system and its resources from unauthorized access, modification, or damage.
  - Transparency: the ability to hide the complexity and diversity of the system from the users and the application programmers, so that the system appears as a whole, rather than as a collection of independent components .



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of architectural models for distributed systems.

### Architectural models for distributed systems

- Architectural models are a type of system model that describe the organization and interrelationship of components across the network in a distributed system .
- Architectural models can be classified into different styles based on the placement, communication, and coordination of components.
- Some common architectural styles are:
  - **Client-server architecture**: A style where components are divided into clients and servers. Clients request services from servers, and servers provide services to clients. Servers can be centralized or distributed.
  - **Broker architecture**: A style where components are connected by a broker that acts as an intermediary. The broker locates and invokes services on behalf of clients, and hides the details of service implementation and location from clients. An example of broker architecture is CORBA.
  - **Service-oriented architecture (SOA)**: A style where components are exposed as services that can be discovered and invoked by other components. Services are loosely coupled and can be composed to form complex applications. An example of SOA is web services.
  - **Peer-to-peer architecture**: A style where components are equal peers that can act as both clients and servers. Peers can communicate and share resources directly with each other, without relying on a central authority. An example of peer-to-peer architecture is BitTorrent.
  - **Layered architecture**: A style where components are organized in layers. Each layer communicates with its adjacent layer by sending requests and getting responses. Layers can be hierarchical or horizontal. An example of layered architecture is the OSI model.
- Architectural models can have different properties and trade-offs, such as scalability, performance, reliability, security, and modularity.
- Architectural models can be influenced by the underlying fundamental models and interaction models of the distributed system.



Hello, I am Sydney, your AI assistant. I can help you with your topic of fundamental models for distributed systems. Here is a summary of the main points:

### Fundamental Models for Distributed Systems

- Fundamental models describe the properties that are common to all distributed systems, such as concurrency, scalability, heterogeneity, and transparency  .
- Interaction models deal with the issues related to the communication and coordination of processes in a distributed system, such as performance, timing, ordering, and consistency of events  .
- Failure models specify the types of faults that can occur in a distributed system, such as crash, omission, timing, response, and Byzantine faults, and how they affect the processes and the communication channels  .
- Security models address the challenges of ensuring the confidentiality, integrity, availability, and authenticity of the data and the processes in a distributed system, such as encryption, authentication, authorization, and auditing  .

Here is a diagram that illustrates the fundamental models for distributed systems:

Diagram of fundamental models for distributed systems




Hello, I am Sydney, your AI assistant. I can help you with your query. Here is the content I have generated for you based on the topic you have given me.

### Theoretical Foundation for Distributed System

- A distributed system is a collection of processes that are spatially separated and do not share a common memory and communicate with one another by exchanging messages with arbitrary delays .
- Theoretical foundations of distributed systems aim to understand the inherent limitations, capabilities, and trade-offs of such systems and to design efficient and correct algorithms for solving various problems in them.
- Some of the fundamental concepts and challenges in distributed systems are :
  - **Limitation of distributed systems**: Due to the lack of global clock, shared memory, and reliable communication, distributed systems cannot achieve perfect synchronization, consensus, or atomicity in general. These limitations impose constraints on the feasibility and complexity of distributed algorithms.
  - **Logical clocks**: Logical clocks are a way of ordering events in a distributed system based on their causal relationships, rather than their physical timestamps. Logical clocks can be implemented using various schemes, such as Lamport's scalar clocks or vector clocks, which assign logical timestamps to events and messages that preserve the partial order of causality.
  - **Message passing systems**: Message passing systems are a model of distributed computation where processes communicate by sending and receiving messages over a network. Message passing systems can be classified based on various properties, such as the network topology, the message delivery guarantees, the failure model, or the synchrony assumptions.



### Limitation of Distributed system

A distributed system is a system that consists of multiple independent components that communicate with each other over a network. Distributed systems have many advantages, such as scalability, fault-tolerance, availability, and performance. However, they also face some limitations that make them challenging to design and implement. Some of the main limitations of distributed systems are:

- **Absence of a global state**: In a distributed system, there is no single point of control or coordination for the entire system. Each component has its own local state and view of the system, which may differ from the views of other components. This makes it difficult to reason about the behavior and correctness of the system, especially in the presence of failures, concurrency, and inconsistency. For example, it is hard to determine if a message has been delivered to all recipients, or if a transaction has been committed by all participants, or if a data item has the same value on all replicas. To cope with this limitation, distributed systems often use techniques such as consensus algorithms, logical clocks, vector clocks, or distributed snapshots to establish some form of global state or ordering among the components.

- **Absence of shared memory**: In a distributed system, there is no common memory space that can be accessed by all components. Each component has its own local memory and can only communicate with other components by sending and receiving messages over the network. This makes it difficult to share data and synchronize operations among the components, especially when the network is unreliable, slow, or congested. For example, it is hard to implement mutual exclusion, atomicity, or consistency guarantees for distributed data structures or algorithms. To cope with this limitation, distributed systems often use techniques such as distributed locking, distributed transactions, or distributed consensus to coordinate access and updates to shared data.

- **Network issues**: In a distributed system, the network is a critical and unpredictable factor that affects the performance and reliability of the system. The network can introduce delays, losses, duplications, reordering, or partitioning of messages, which can cause communication failures, timeouts, or inconsistencies among the components. For example, it is hard to detect if a component has crashed or is just slow, or if a message has been lost or delayed, or if a network partition has occurred. To cope with this limitation, distributed systems often use techniques such as heartbeat messages, failure detectors, timeouts, retries, or quorums to handle network failures and recover from them.

- **Security issues**: In a distributed system, the network is also a potential source of attacks and threats to the system. The network can be compromised by malicious actors who can intercept, modify, or inject messages, or launch denial-of-service attacks, which can compromise the confidentiality, integrity, or availability of the system. For example, it is hard to prevent or detect if a message has been tampered with, or if a component has been impersonated, or if a component has been corrupted by a malicious code. To cope with this limitation, distributed systems often use techniques such as encryption, authentication, authorization, or digital signatures to secure the communication and the components.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of absence of global clock for the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM.

### Absence of global clock

- A global clock is a system-wide clock that is equally accessible to all processes in a distributed system.
- A global clock would allow processes to synchronize their actions, measure the elapsed time between events, and determine the order of events across the system.
- However, a global clock is hard to realize in distributed systems due to the following reasons:
  - The physical clocks of different processes may have different rates of drift, accuracy, and precision, making them unsuitable for global synchronization.
  - The communication channels between processes may have unpredictable and variable transmission delays, making it impossible to exchange accurate clock values or timestamps.
  - The distributed system may span multiple time zones, making it difficult to agree on a common time reference.
- Therefore, distributed systems are inherently asynchronous, meaning that there is no common notion of time or global state among the processes.
- This has two important implications for distributed systems:
  - It is not always possible to determine the order of events on different processes, since there is no global time to compare their timestamps. This affects the consistency and causality of the system.
  - It is not possible for an individual process to obtain an up-to-date state of the entire system, since there is no global clock to capture a consistent snapshot of the system. This affects the observability and debugging of the system.



### Shared Memory

- Shared memory is a programming model that allows multiple processes to access and modify the same data in a shared address space.
- Shared memory can be implemented in two ways: physically shared memory and distributed shared memory.
- Physically shared memory is when multiple processors or cores share the same physical memory, such as in a multiprocessor system or a multicore system.
- Distributed shared memory (DSM) is when multiple nodes or computers in a distributed system share a virtual address space, but not a physical memory. The DSM system manages the memory across all the nodes and provides the illusion of a shared memory.
- DSM can be achieved via software or hardware. Software DSM relies on the operating system or the middleware to handle the memory consistency, coherence, and synchronization. Hardware DSM relies on special hardware components, such as cache coherence circuits and network interface controllers, to handle the memory operations.
- DSM has some advantages over other programming models, such as message passing or remote procedure calls, in distributed systems. Some of these advantages are:
  - It simplifies the programming by hiding the details of data distribution and communication.
  - It allows the programmers to use familiar shared memory constructs, such as locks, semaphores, and monitors, to synchronize the processes.
  - It enables the use of existing shared memory applications and libraries in distributed systems without much modification.
  - It can improve the performance by exploiting the locality of data access and reducing the communication overhead.
- DSM also has some challenges and limitations, such as:
  - It requires a large amount of network bandwidth and memory to maintain the consistency and coherence of the shared data.
  - It may incur high latency and overhead for accessing remote data or resolving conflicts.
  - It may suffer from false sharing, which is when multiple processes access different parts of the same memory page or cache line, causing unnecessary invalidations and updates.
  - It may not be suitable for some applications that require fine-grained data access or strong consistency guarantees.



### Logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A logical clock is a mechanism for capturing chronological and causal relationships in a distributed system  .
- A distributed system may have no physically synchronous global clock, so a logical clock allows global ordering on events from different processes in such systems .
- A logical clock is not a physical device, but a software counter that is incremented according to some rules .
- A logical clock can be used for computation analysis, distributed algorithm design, individual event tracking, and exploring computational progress.
- Some examples of logical clock algorithms are:
  - Lamport timestamps, which are monotonically increasing software counters that are updated based on the send and receive events of messages .
  - Vector clocks, which are arrays of software counters that are updated based on the send, receive, and local events of processes .
  - Matrix clocks, which are matrices of software counters that are updated based on the send, receive, and local events of processes and also capture the concurrency of events.
- The main properties of logical clocks are:
  - Consistency: If event A causally precedes event B, then the logical clock value of A is less than the logical clock value of B .
  - Accuracy: The logical clock values reflect the real-time order of events as closely as possible.
  - Efficiency: The logical clock algorithm should minimize the overhead of updating and transmitting the clock values.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is some information on Lamport's logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM.

### Lamport's logical clocks

- Lamport's logical clocks are a way of ordering events in a distributed system without relying on physical clocks.
- Lamport's logical clocks are based on the concept of **happens-before** relation, denoted by `->`, which means that one event causally affects another event.
- Lamport's logical clocks assign a numerical value, called a **timestamp**, to each event in a process. The timestamp reflects the logical order of events, not the actual physical time.
- Lamport's logical clocks follow two rules:
  - Rule 1: If `a` and `b` are events in the same process, and `a` occurs before `b`, then `L(a) < L(b)`, where `L(x)` is the timestamp of event `x`.
  - Rule 2: If `a` is the event of sending a message by one process and `b` is the event of receiving that message by another process, then `L(a) < L(b)`.
- Lamport's logical clocks ensure that if `a -> b`, then `L(a) < L(b)`, but the converse is not necessarily true. That is, two events with different timestamps may be concurrent and have no causal relation.
- Lamport's logical clocks can be implemented by following these steps:
  - Each process maintains a counter, initialized to zero, that is incremented before each event in that process.
  - Each message sent by a process contains the counter value of the sender as its timestamp.
  - When a process receives a message, it updates its counter to be the maximum of its own counter and the timestamp of the message, plus one.
- Lamport's logical clocks are simple and efficient, but they do not capture the full causal history of events. For example, two events that are causally related by a chain of messages may have the same timestamp. This can lead to inconsistencies and anomalies in distributed systems.
- To overcome the limitations of Lamport's logical clocks, **vector clocks** are used, which are an extension of Lamport's logical clocks that keep track of the timestamps of all processes in the system.



### Concepts in Message Passing Systems for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Message passing is a technique for invoking behavior on a computer by sending messages from one process to another.
- Message passing systems are subsystems of distributed operating systems that provide a set of message-based interprocess communication (IPC) protocols.
- Message passing systems can be classified into two types: synchronous and asynchronous.
  - Synchronous message passing systems require the sender and the receiver to be ready at the same time for communication. The sender blocks until the receiver acknowledges the message, and the receiver blocks until a message arrives.
  - Asynchronous message passing systems do not require the sender and the receiver to be ready at the same time for communication. The sender does not block after sending a message, and the receiver does not block if no message is available.
- Message passing systems can also be classified into two types: direct and indirect.
  - Direct message passing systems require the sender and the receiver to know each other's identities. The sender specifies the destination process and the receiver specifies the source process in the message.
  - Indirect message passing systems do not require the sender and the receiver to know each other's identities. The sender and the receiver communicate through a shared data structure, such as a queue, a mailbox, or a topic.
- Message passing systems can have different features, such as reliability, ordering, multicasting, and security.
  - Reliability refers to the ability of the message passing system to deliver messages without loss, duplication, or corruption.
  - Ordering refers to the ability of the message passing system to preserve the temporal or causal relationships among messages.
  - Multicasting refers to the ability of the message passing system to send a message to multiple destinations at once.
  - Security refers to the ability of the message passing system to protect messages from unauthorized access, modification, or disclosure.
- Message passing systems can face different challenges, such as network failures, message fragmentation, message buffering, and message routing.
  - Network failures refer to the possibility of the communication link between the sender and the receiver being disrupted or unavailable.
  - Message fragmentation refers to the possibility of the message being too large to fit in a single network packet and having to be split into smaller pieces.
  - Message buffering refers to the possibility of the message being stored temporarily in the sender, the receiver, or an intermediate node until it can be delivered or processed.
  - Message routing refers to the possibility of the message having to traverse multiple nodes or paths to reach its destination.



### Causal order for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Causal order is a way of ordering events in a distributed system based on their causal relationships, rather than their physical timestamps or global clocks.
- Causal order ensures that if an event e1 causally precedes another event e2, then e1 is observed before e2 by all processes in the system.
- Causal order is important for maintaining consistency and correctness in distributed systems, especially for applications that rely on causal dependencies, such as collaborative editing, social media, or online gaming.
- Causal order can be defined formally using the concept of Lamport's happened-before relation, denoted by ->, which is a partial order on the set of events in a distributed system.
- The happened-before relation -> satisfies the following properties:
  - If e1 and e2 are events in the same process, and e1 occurs before e2, then e1 -> e2.
  - If e1 is the sending of a message by one process and e2 is the receipt of the same message by another process, then e1 -> e2.
  - If e1 -> e2 and e2 -> e3, then e1 -> e3 (transitivity).
- Two events e1 and e2 are said to be concurrent, denoted by e1 || e2, if neither e1 -> e2 nor e2 -> e1 holds.
- Causal order can be implemented in distributed systems using various algorithms, such as vector clocks, causal broadcast, or causal delivery.
- Vector clocks are an extension of Lamport's logical clocks, which assign a scalar timestamp to each event in a distributed system. Vector clocks assign a vector of timestamps to each event, where each element of the vector represents the logical clock of a process in the system.
- Vector clocks can be used to determine the causal order of events by comparing their vectors element-wise. If the vector of e1 is less than or equal to the vector of e2 in every element, then e1 -> e2. If the vectors are incomparable, then e1 || e2.
- Causal broadcast is a communication primitive that guarantees that messages are delivered to all processes in the system in causal order. Causal broadcast can be implemented using vector clocks, by piggybacking the vector clock of the sender with each message, and buffering the messages at the receiver until their causal dependencies are satisfied.
- Causal delivery is a weaker property than causal broadcast, which only guarantees that messages are delivered to each process in causal order, but not necessarily to all processes. Causal delivery can be implemented using vector clocks, by piggybacking the vector clock of the sender with each message, and delivering the messages at the receiver in the order of their vector clocks.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is some information on the topic of total order for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM.

### Total order

- A distributed system is said to have **partial order** if we can have a partial order relationship among the events in the system .
- A partial order relationship means that some events are **comparable** (i.e., one event happens before another) and some events are **incomparable** (i.e., there is no causal relationship between them).
- If **totality**, i.e., causal relationship among all events in the system, can be established, then the system is said to have **total order** .
- A total order relationship means that all events are **comparable** and there is a unique way to order them chronologically.
- Total order is very useful for distributed system implementation, especially for **consensus**, **replication**, **fault tolerance**, and **coordination**.
- Total order can be achieved by using some **logical clocks** that assign timestamps to events and allow processes to compare them.
- One example of a logical clock is the **Lamport timestamp**, which assigns a counter value to each event and increments it whenever a process sends or receives a message .
- Lamport timestamps can be used to create a total order of events in a distributed system by using some arbitrary mechanism to break ties (e.g., the ID of the process).
- Another example of a logical clock is the **vector clock**, which assigns a vector of counter values to each event and updates it based on the causal dependencies among events.
- Vector clocks can be used to create a partial order of events in a distributed system, but not a total order, as they may not be able to break ties among concurrent events.

Here is a diagram that illustrates the difference between partial order and total order in a distributed system with three processes:

```markdown
P1: a -> b -> c
P2: d -> e -> f
P3: g -> h -> i

Partial order: a -> b -> c, d -> e -> f, g -> h -> i, b -> e, c -> f, d -> g, e -> h, f -> i
Total order: a -> b -> c -> d -> e -> f -> g -> h -> i
```

The arrows indicate the causal relationship between events. For example, b -> e means that event b happens before event e. In the partial order, there are some events that are incomparable, such as a and d, or c and g. In the total order, all events are comparable and there is a unique way to order them.




### Total Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems in the Subject of Distributed System

- A distributed system is a collection of independent processes that communicate by exchanging messages over a network.
- Events are occurrences that happen at a specific point in time and space in a distributed system, such as sending or receiving a message, or executing a local operation.
- The order of events is important for understanding the behavior and correctness of a distributed system, especially in the presence of concurrency and failures.
- A partial order is a binary relation that satisfies three properties: reflexivity, antisymmetry, and transitivity. A partial order can be represented by a directed acyclic graph (DAG), where nodes are events and edges are ordering relations.
- A causal order is a partial order that captures the notion of potential causality between events. An event e1 is causally related to an event e2, denoted by e1 -> e2, if one of the following conditions holds:
  - e1 and e2 are events in the same process, and e1 happened before e2.
  - e1 is the sending of a message m, and e2 is the receipt of the same message m.
  - There exists an event e3 such that e1 -> e3 and e3 -> e2.
- A total order is a partial order that satisfies an additional property: comparability. A total order can be represented by a linear sequence, where every pair of events is ordered. A total order is also called a linearization of a partial order.
- A total causal order is a total order that is consistent with the causal order, meaning that if e1 -> e2, then e1 is ordered before e2 in the total order. A total causal order is the strictest ordering in distributed systems; it establishes only one linearization, consistent with the causal order, among all the events that occur in the system, even those that occur concurrently. For that reason, the execution of the system is considered as synchronous .
- A total causal order can be implemented by using a logical clock, such as a vector clock, that assigns a timestamp to each event, such that the timestamp reflects the causal order. A vector clock is an array of integers, one for each process, that is incremented by one when a local event occurs, and updated with the maximum of the local and received values when a message is sent or received. A vector clock can be used to compare the order of events by using the following rules:
  - If VC(e1) < VC(e2), then e1 is ordered before e2.
  - If VC(e1) > VC(e2), then e2 is ordered before e1.
  - If VC(e1) || VC(e2), then e1 and e2 are concurrent and can be ordered arbitrarily.
- A total causal order can also be implemented by using a total order broadcast, which is a communication primitive that delivers messages to all processes in the same total order, consistent with the causal order. A total order broadcast can be achieved by using a sequencer, which is a special process that assigns a sequence number to each message and broadcasts it to all processes. The processes then deliver the messages in the order of the sequence numbers. A sequencer can be elected by using a leader election algorithm, or can be replicated for fault tolerance. A total order broadcast can be used to implement distributed algorithms, such as distributed snapshots, consensus, and atomic broadcast   .



### Techniques for Message Ordering in Distributed Systems

- Message ordering is the problem of ensuring that messages are processed in a consistent and predictable order in a distributed system.
- Message ordering is important because it affects the correctness and consistency of the system's state and behavior.
- There are different types of message ordering techniques, depending on the desired level of ordering guarantee and the trade-off between performance and complexity.
- Some of the common message ordering techniques are:

  - **Unordered**: Messages are delivered in any order, without any guarantee of ordering. This is the simplest and fastest technique, but it may lead to inconsistent or incorrect results. For example, if two processes send messages to update a shared variable, the final value may depend on the order of delivery, which is arbitrary.
  - **FIFO**: Messages are delivered in the same order as they are sent by each sender. This technique ensures that messages from the same sender are ordered, but it does not guarantee any ordering among messages from different senders. For example, if two processes send messages to increment a shared counter, the final value may depend on the order of delivery of messages from different senders, which is not FIFO.
  - **Causal**: Messages are delivered in a way that respects the causal dependencies among them. A message m1 is causally dependent on another message m2 if m1 is sent after m2 is received, or if there is a chain of messages that connects m1 and m2. This technique ensures that messages that are causally related are ordered, but it does not guarantee any ordering among messages that are causally unrelated. For example, if two processes send messages to update a shared variable based on the value of another shared variable, the final value may depend on the order of delivery of messages that are causally unrelated, which is not causal.
  - **Total**: Messages are delivered in the same order to all receivers. This technique ensures that messages are globally ordered, regardless of their sender or causal dependencies. This is the strongest and most desirable technique, but it is also the most complex and costly. For example, if two processes send messages to update a shared variable, the final value will be the same for all receivers, regardless of the order of sending, which is total.

- Different message ordering techniques can be implemented using different protocols, such as logical clocks, vector clocks, timestamps, sequence numbers, etc. These protocols use various mechanisms, such as piggybacking, buffering, acknowledgement, etc. to achieve the desired ordering guarantee.



### Causal ordering of messages

- Causal ordering of messages is a partial ordering of messages in a distributed computing environment .
- It places a restriction on communication between processes by requiring that if the transmission of message mi to process pk necessarily preceded the transmission of message mj to the same process, then the delivery of these messages to that process must be ordered such that mi is delivered before mj  .
- Causal ordering of messages is one of the four semantics of multicast communication, namely unordered, totally ordered, causal, and sync-ordered communication.
- Multicast communication methods vary according to the message’s reliability guarantee and ordering guarantee.
- Causal ordering of messages is useful for applications that need to preserve the logical dependencies between events in a distributed system .
- Causal ordering of messages is not automatically guaranteed in distributed systems, because of transmission delays, network congestion, or clock synchronization issues .
- Causal ordering of messages can be implemented by various algorithms, such as vector clocks, logical clocks, or piggybacking techniques  .
- Causal ordering of messages has some advantages and disadvantages, such as:
  - Advantages: 
    - It allows for reasoning about causality in a distributed system without a global time.
    - It reduces the complexity of message ordering compared to total ordering.
    - It preserves the consistency of replicated data and avoids concurrency anomalies.
  - Disadvantages:
    - It may incur additional overhead in terms of message size, memory, or computation .
    - It may not reflect the actual physical order of events or the user's expectations.
    - It may not be sufficient for some applications that need stronger guarantees of message ordering.



Hello, I am Sydney, your AI assistant. I can help you with your notes on global state for the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM. Here is some information that I found from the web:

### Global State in Distributed Systems

- A **global state** of a distributed system is a collection of the **local states** of the processes and the channels that communicate among them .
- A local state of a process is the values of its variables, registers, program counter, etc. at a given point in time.
- A local state of a channel is the set of messages that have been sent but not yet received by the destination process.
- A global state can be used to determine properties of the distributed system, such as deadlock, termination, consistency, etc  .
- However, capturing a global state of a distributed system is not trivial, because the processes are concurrent and asynchronous, and there is no global clock or shared memory .
- Therefore, a global state must be **consistent**, meaning that it reflects a possible execution of the distributed system, and does not contain any causal anomalies .
- A causal anomaly is a situation where a process observes an effect before its cause, such as receiving a message before it is sent .
- A global state is consistent if it satisfies the **happened-before** relation, which defines a partial order among the events in the distributed system .
- The happened-before relation, denoted by ->, is defined as follows :
  - If a and b are events in the same process, and a occurs before b, then a -> b.
  - If a is the event of sending a message m by a process, and b is the event of receiving m by another process, then a -> b.
  - If a -> b and b -> c, then a -> c (transitivity).
- A **cut** of a distributed system is a subset of events that partitions the system into past and future .
- A cut is consistent if it contains no causal anomalies, i.e., if a -> b and b is in the cut, then a is also in the cut .
- A **snapshot** of a distributed system is a global state that is computed along a consistent cut .
- A snapshot can be taken by each process recording its local state and the state of its incoming channels, and exchanging messages with other processes to coordinate the cut .
- There are different algorithms for taking snapshots, such as the **Chandy-Lamport algorithm**, the **Lai-Yang algorithm**, the **Mattern's algorithm**, etc  .
- The main challenges of snapshot algorithms are to ensure consistency, completeness, accuracy, and efficiency  .



### Termination Detection

Termination detection is a fundamental problem in distributed systems, where a set of processes cooperate to perform a computation. The goal is to determine when all the processes have finished their work and there are no more messages in transit between them. This is non-trivial because no process has complete knowledge of the global state, and global time does not exist.

There are different algorithms for termination detection, depending on the assumptions and properties of the distributed system. One of the most well-known algorithms is Huang's algorithm, proposed by Shing-Tsaan Huang in 1989. Huang's algorithm is based on the following concepts:

- A process is either in an active state or in an idle state. An active process may become idle at any time, but an idle process may only become active again upon receiving a computational message (a message that affects the local state of the process).
- A process maintains a counter of the number of messages it has sent and received. This counter is called the **control state** of the process.
- A process periodically sends its control state to a designated process, called the **controller**. The controller collects the control states of all the processes and computes the **global control state**, which is the sum of all the control states.
- The controller initiates a **snapshot** of the system, which is a consistent global state that reflects the local states of the processes and the messages in transit at some point in time. The controller uses a special message, called the **marker**, to initiate and propagate the snapshot.
- The controller detects termination when the global control state is zero and all the processes are idle. This means that there are no more messages in transit and no more work to be done.

The algorithm works as follows:

- The controller initiates a snapshot by sending a marker to itself and to all the other processes. The controller also records its local state and control state.
- When a process receives a marker for the first time, it records its local state and control state, and sends a marker to all the other processes. It also starts recording the messages it receives from each process until it receives a marker from that process.
- When a process receives a marker from a process that it has already received a marker from, it stops recording the messages from that process and sends its recorded messages to the controller. The controller adds the number of recorded messages to the global control state.
- When the controller receives the recorded messages from all the processes, it computes the global control state and checks if it is zero and all the processes are idle. If so, it declares termination. Otherwise, it waits for the next snapshot.

The algorithm guarantees that termination is detected eventually, and that no false positives are possible. The algorithm also preserves the execution of the underlying computation, and does not require additional communication channels between processes. However, the algorithm has some drawbacks, such as:

- The algorithm requires a reliable and FIFO communication network, which may not be realistic in some distributed systems.
- The algorithm relies on a single controller, which may become a bottleneck or a single point of failure.
- The algorithm generates a lot of messages for each snapshot, which may consume a lot of bandwidth and delay the underlying computation.

There are other algorithms for termination detection that overcome some of these drawbacks, such as the Dijkstra-Scholten algorithm, the credit recovery algorithm, the wave algorithm, and the distributed garbage collection algorithm. These algorithms use different techniques, such as parent-child relationships, tokens, waves, and reference counting, to detect termination in different types of distributed systems.



## Unit 2 - Distributed Mutual Exclusion

- Distributed mutual exclusion is the problem of ensuring that at most one process in a distributed system can access a shared resource at a time.
- Distributed mutual exclusion algorithms can be classified into two categories: permission-based and token-based.
- Permission-based algorithms require a process to obtain permission from other processes before entering the critical section. Examples of permission-based algorithms are Ricart-Agrawala algorithm, Lamport's algorithm, and Maekawa's algorithm.
- Token-based algorithms use a special message, called a token, that grants the right to enter the critical section. A process can enter the critical section only if it has the token. Examples of token-based algorithms are Suzuki-Kasami algorithm, Raymond's algorithm, and Singhal's algorithm.
- The performance of distributed mutual exclusion algorithms can be measured by the following metrics: message complexity, synchronization delay, and fairness.
- Message complexity is the number of messages exchanged per critical section access.
- Synchronization delay is the time elapsed between a process requesting the critical section and entering it.
- Fairness is the degree to which the algorithm ensures that every process gets a fair chance to enter the critical section.



### Classification of distributed mutual exclusion

Distributed mutual exclusion is a problem of ensuring that only one process in a distributed system can access a shared resource or data at a time. It is a fundamental requirement for achieving consistency, coordination and synchronization among the processes.

There are three basic approaches for implementing distributed mutual exclusion algorithms:

- **Token-based approach**: A unique token is shared among the sites. A site is allowed to enter its critical section if it possesses the token. Mutual exclusion is ensured because the token is unique. Examples of token-based algorithms are Ricart-Agrawala algorithm, Suzuki-Kasami algorithm, Raymond's tree-based algorithm, etc.
- **Non-token-based approach**: There is no token in this approach. Instead, a site requests permission from other sites before entering its critical section. A site is allowed to enter its critical section if it receives permission from all or a majority of other sites. Examples of non-token-based algorithms are Lamport's algorithm, Ricart-Agrawala algorithm with optimization, Maekawa's algorithm, etc.
- **Quorum-based approach**: This is a generalization of the non-token-based approach. A site requests permission from a subset of sites, called a quorum, before entering its critical section. A site is allowed to enter its critical section if it receives permission from all the sites in its quorum. Examples of quorum-based algorithms are Maekawa's algorithm, Sankararaman's algorithm, Agrawala-El Abbadi algorithm, etc.

The main performance metrics for evaluating distributed mutual exclusion algorithms are:

- **Message complexity**: The number of messages exchanged per critical section execution.
- **Synchronization delay**: The time elapsed between a site's request and its entry to the critical section.
- **System throughput**: The number of critical section executions per unit time in the system.



### Requirement of mutual exclusion theorem for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM

- Mutual exclusion is a concurrency control property which is introduced to prevent race conditions.
- It is the requirement that a process can not enter its critical section while another concurrent process is currently present or executing in its critical section i.e only one process is allowed to execute the critical section at any given time.
- A critical section is a section of code that accesses a shared resource or data that must not be accessed by more than one process at a time.
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion. Message passing is the sole means for implementing distributed mutual exclusion .
- Mutual exclusion in a distributed system states that only one process is allowed to execute the critical section (CS) at any given time  .
- The mutual exclusion theorem states that any algorithm that solves the mutual exclusion problem in a distributed system must satisfy the following four properties :
  - Safety: No two processes can be in the critical section at the same time.
  - Liveness: Every request to enter the critical section is eventually granted.
  - Fairness: No process is indefinitely postponed or starved while waiting to enter the critical section.
  - Fault-tolerance: The algorithm can tolerate a bounded number of process or message failures without violating the safety property.
- There are three basic approaches for implementing distributed mutual exclusion:
  - Token-based algorithms: A unique token is circulated among the processes in a logical ring. A process can enter the critical section only if it possesses the token.
  - Permission-based algorithms: A process requests permission from a set of processes before entering the critical section. A process can enter the critical section only if it receives permission from all the processes in the set.
  - Quorum-based algorithms: A process requests permission from a subset of processes (called a quorum) before entering the critical section. A process can enter the critical section only if it receives permission from a majority of the processes in the quorum.



### Token based and non token based algorithms for distributed mutual exclusion

Distributed mutual exclusion (DME) is the problem of ensuring that only one process at a time can access a shared resource in a distributed system. There are two main types of algorithms for DME: token based and non token based.

- Token based algorithms
  - In token based algorithms, a unique token is shared among all the processes in the system. The token represents the permission to enter the critical section. A process can enter the critical section only if it has the token. After exiting the critical section, the process passes the token to another process that is waiting for it.
  - Token based algorithms guarantee mutual exclusion and fairness, since the token is passed in a predefined order or based on requests. However, they have some drawbacks, such as the possibility of losing the token due to failures, the overhead of passing the token, and the delay of waiting for the token.
  - Examples of token based algorithms are the Suzuki-Kasami algorithm, the Raymond's tree algorithm, and the Maekawa's algorithm.

- Non token based algorithms
  - In non token based algorithms, a process communicates with a set of other processes to determine who should enter the critical section next. The communication is done by sending and receiving messages, such as requests, replies, and releases. A process can enter the critical section only if it receives a positive reply from all the processes in its set.
  - Non token based algorithms do not require a token, so they avoid the problems of token loss, token passing, and token waiting. However, they have other drawbacks, such as the possibility of deadlock, the overhead of message exchanges, and the dependency on the reliability of the communication channels.
  - Examples of non token based algorithms are the Ricart-Agrawala algorithm, the Lamport's timestamp algorithm, and the Singhal's dynamic information structure algorithm.



Hello, I am Sydney, your AI assistant. I can help you with your query.

### Performance metric for distributed mutual exclusion algorithms

Distributed mutual exclusion algorithms are algorithms that ensure that only one process can access a shared resource or execute a critical section at a time in a distributed system. The performance of these algorithms can be evaluated by the following metrics:

- **Message complexity**: It is the number of messages that are required per critical section execution by a process. It measures the communication overhead of the algorithm. The lower the message complexity, the better the performance.
- **Synchronization delay**: It is the time elapsed between the moment a process leaves the critical section and the moment the next process enters the critical section. It measures the responsiveness of the algorithm. The lower the synchronization delay, the better the performance.
- **Response time**: It is the time elapsed between the moment a process requests to enter the critical section and the moment it actually enters the critical section. It measures the waiting time of the process. The lower the response time, the better the performance.
- **Throughput**: It is the number of critical section executions per unit time in the system. It measures the efficiency of the algorithm. The higher the throughput, the better the performance.

Different algorithms may have different trade-offs among these metrics. For example, a token-based algorithm may have low message complexity but high synchronization delay, while a non-token-based algorithm may have high message complexity but low synchronization delay. A quorum-based algorithm may have low response time but low throughput, while a centralized algorithm may have high response time but high throughput. Therefore, the choice of the algorithm depends on the application requirements and the system characteristics.



## Unit 3 - Distributed Deadlock Detection

- A **deadlock** is a condition where a set of processes request resources that are held by other processes in the set, and none of the processes can proceed until they obtain the requested resources.
- A **distributed deadlock** is a deadlock that involves processes and resources located on different machines in a distributed system.
- **Deadlock detection** is a strategy to deal with deadlocks by examining the status of the process-resource interactions for the presence of cyclic wait.
- **Deadlock detection** in distributed systems requires addressing two basic issues: 
  - **Detection** of existing deadlocks by using a distributed technique or by constructing a global wait-for graph from local wait-for graphs at a deadlock detector.
  - **Resolution** of detected deadlocks by aborting one or more deadlocked processes or preempting some resources from them.
- There are three main approaches to **deadlock detection** in distributed systems:
  - **Centralized approach**: A single node is designated as the deadlock detector and collects the local wait-for graphs from all the nodes periodically. It then constructs the global wait-for graph and checks for cycles. This approach is simple but suffers from a single point of failure and a high communication overhead.
  - **Hierarchical approach**: The nodes are organized into a hierarchy of clusters, and each cluster has a coordinator node that acts as the deadlock detector for that cluster. The coordinator nodes communicate with each other to construct the global wait-for graph and check for cycles. This approach reduces the communication overhead but increases the complexity and the delay in detection.
  - **Distributed approach**: Each node maintains its own local wait-for graph and initiates a distributed algorithm to detect cycles in the global wait-for graph. There are two main algorithms for this approach: the **path-pushing algorithm** and the **edge-chasing algorithm**. The path-pushing algorithm propagates the paths of waiting processes along the edges of the local wait-for graphs, and detects a cycle when a process receives its own path. The edge-chasing algorithm sends probe messages along the edges of the local wait-for graphs, and detects a cycle when a probe message returns to its originator. Both algorithms are decentralized and fault-tolerant, but they differ in the amount and the frequency of message exchange.



### System Model for Distributed Deadlock Detection

- A distributed system consists of a set of nodes that communicate by message passing.
- Each node has a set of resources that can be requested by processes running on the same or different nodes.
- A process can request, hold, and release resources according to some protocol.
- A process is blocked if it is waiting for a resource that is held by another process.
- A deadlock is a situation where a set of processes are blocked and none of them can proceed.
- A wait-for graph (WFG) is a directed graph that represents the blocking relationships among processes. A node in the WFG is a process and an edge from P to Q means that P is waiting for a resource held by Q.
- A cycle in the WFG indicates a deadlock.
- A global WFG is a WFG that contains all the processes and resources in the system. A local WFG is a WFG that contains only the processes and resources on a single node.
- A system model for distributed deadlock detection defines how the global WFG is constructed and analyzed to detect deadlocks.
- There are three main approaches to distributed deadlock detection: centralized, hierarchical, and distributed.    

  - Centralized approach: One node is designated as the deadlock detector (DD) and collects the local WFGs from all the other nodes. The DD constructs the global WFG and checks for cycles periodically or on demand.
  - Hierarchical approach: The nodes are organized into a tree structure, where each node is responsible for a subset of nodes. The root node is the DD and collects the local WFGs from its children. The children nodes may also collect the local WFGs from their descendants and send them to the root. The DD constructs the global WFG and checks for cycles periodically or on demand.
  - Distributed approach: Each node maintains a partial view of the global WFG based on the messages it sends and receives. The nodes cooperate to detect cycles using algorithms such as edge chasing, diffusing computation, or probe-based. The cycle detection can be initiated by any node or by a special node.



### Resource vs Communication Deadlocks

- A deadlock occurs when a set of processes requests resources that are already occupied by other processes in the group. Because each process possesses a resource and waits for another resource held by another process, the execution of two or more processes is blocked.
- Resource deadlocks and communication deadlocks are two types of deadlock that can occur in distributed systems.
- In resource deadlocks, processes access resources, such as data objects in database systems and buffers in store and forward communication networks. A process acquires a resource before accessing it and releasing it after using it.
- In communication deadlocks, processes communicate with each other by sending and receiving messages. A process waits for a message from another process before proceeding with its execution.
- The main difference between resource deadlocks and communication deadlocks is that in resource deadlocks, processes contend for resources, while in communication deadlocks, processes wait for messages.
- Resource deadlocks can be detected by using techniques such as wait-for graphs, timestamps, and timeouts. Communication deadlocks can be detected by using techniques such as message sequence charts, message dependency graphs, and message passing protocols .
- Resource deadlocks can be prevented by using techniques such as resource ordering, resource preallocation, and resource revocation. Communication deadlocks can be prevented by using techniques such as message buffering, message acknowledgment, and message retransmission .
- Resource deadlocks can be resolved by using techniques such as resource release, resource rollback, and resource recovery. Communication deadlocks can be resolved by using techniques such as message cancellation, message reordering, and message rerouting .



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on deadlock prevention for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM.

### Deadlock Prevention

- A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
- Deadlock prevention is a technique to avoid the occurrence of deadlocks by ensuring that at least one of the four necessary conditions for deadlock (mutual exclusion, hold and wait, no preemption, and circular wait) is never satisfied.
- In distributed systems, deadlock prevention is more challenging and costly than in centralized systems, because of the lack of global information and synchronization among the processes and resources.
- There are two main approaches to deadlock prevention in distributed systems: ordered request and collective request.

#### Ordered Request

- In this approach, each resource type is assigned a unique level, and each process must request resources in increasing order of levels.
- This ensures that no circular wait can occur, as a process that has a resource of level i cannot request a resource of level j < i.
- For example, if there are three resource types A, B, and C, with levels 1, 2, and 3 respectively, then a process can request A, then B, then C, but not C, then A, then B.
- The advantage of this approach is that it is simple and easy to implement.
- The disadvantage is that it may cause resource underutilization and starvation, as a process may have to wait for a long time to acquire a resource of a higher level, even if the resource of a lower level is available.

#### Collective Request

- In this approach, each process must request all the resources it needs at once, before starting its execution.
- This ensures that no hold and wait can occur, as a process either gets all the resources it needs or none at all.
- For example, if a process needs resources A, B, and C, it must request them together, and not one by one.
- The advantage of this approach is that it avoids resource underutilization and starvation, as a process can start its execution as soon as it gets all the resources it needs.
- The disadvantage is that it may cause resource wastage and deadlock, as a process may hold some resources that it does not need immediately, and prevent other processes from using them. Also, if the resources requested by a process are not available, the process may have to wait indefinitely, and cause a deadlock.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM.

### Avoidance for the notes of the Unit 3 - Distributed Deadlock Detection

- Avoidance is a technique that prevents deadlocks from occurring in a distributed system by ensuring that the system is always in a safe state.
- A safe state is a state where there is a sequence of resource allocations that can satisfy the requests of all processes without causing a deadlock.
- A system is in an unsafe state if there is no such sequence of resource allocations.
- Avoidance requires the system to have some knowledge of the current and future resource requests of the processes, which may not be feasible or accurate in a distributed system.
- Avoidance also requires the system to make decisions about granting or denying resource requests based on the global state of the system, which may be difficult or costly to obtain in a distributed system.
- Therefore, avoidance is impractical in distributed systems, and deadlock detection is preferred as a technique to handle deadlocks in distributed systems.
- Some examples of avoidance algorithms are Banker's algorithm and Resource ordering algorithm.



### Detection and Resolution of Distributed Deadlocks

- A distributed deadlock is a situation where a set of processes in a distributed system are waiting for resources held by other processes in the same set, and none of them can proceed.
- Distributed deadlock detection is the process of identifying the existence of a distributed deadlock in the system.
- Distributed deadlock resolution is the process of breaking the deadlock by aborting one or more processes involved in the deadlock.
- There are different techniques for distributed deadlock detection and resolution, based on various strategies such as:
  - Centralized approach: A single designated node (coordinator) is responsible for maintaining the global wait-for graph (WFG) and detecting cycles in it. The coordinator can also initiate the resolution by choosing a victim process to abort. This approach is simple and efficient, but it has a single point of failure and a high communication overhead.
  - Distributed approach: Each node maintains a local WFG and exchanges messages with other nodes to detect cycles. There are different algorithms for this approach, such as:
    - Path-pushing algorithm: Each node periodically sends its local WFG to its neighbors, and each node merges the received WFGs with its own. A cycle is detected when a node receives a WFG that contains a path from itself to itself.
    - Edge-chasing algorithm: Each node periodically initiates a probe message that traverses the WFG along the edges. A cycle is detected when a node receives a probe message that originated from itself.
    - Diffusing computation algorithm: Each node initiates a diffusing computation when it requests a resource and waits for it. A diffusing computation consists of a set of nodes that are involved in the request and a set of messages that are exchanged among them. A cycle is detected when a node receives a message that indicates that all its children in the diffusing computation are blocked.
  - Hierarchical approach: The nodes are organized into a hierarchy of clusters, and each cluster has a coordinator that maintains a local WFG and detects cycles within the cluster. The coordinators also communicate with each other to detect cycles across clusters. This approach reduces the communication overhead and the single point of failure, but it increases the complexity and the detection latency.
- The resolution of distributed deadlocks can be based on various criteria, such as:
  - Process priority: The process with the lowest priority is aborted.
  - Resource utilization: The process that holds the most resources is aborted.
  - Process age: The process that has been running for the longest time is aborted.
  - Process progress: The process that has made the least progress is aborted.
  - Process dependency: The process that has the most dependents is aborted.



### Centralized Deadlock Detection

- This is a technique used in distributed systems to handle deadlock detection.
- According to this technique, the system maintains one global wait-for graph in a single chosen site, which is named as deadlock-detection coordinator.
- The coordinator collects information about the local wait-for graphs of each site and constructs the global wait-for graph.
- The coordinator periodically runs a deadlock detection algorithm on the global wait-for graph and identifies any cycles that indicate deadlocks.
- The coordinator then informs the involved sites to abort one or more processes to resolve the deadlock.
- The advantages of this technique are simplicity and low communication overhead.
- The disadvantages of this technique are the dependency on a single coordinator, which may become a bottleneck or a single point of failure, and the possibility of false deadlocks due to stale information .

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
  - Centralized approach: A single site is designated as the deadlock detector and collects global wait-for graph (WFG) from local WFGs at other sites. The deadlock detector periodically checks the global WFG for cycles and initiates recovery actions if needed.
  - Hierarchical approach: The sites are organized into a hierarchy of clusters. Each cluster has a coordinator that collects local WFGs from its members and constructs a cluster WFG. The coordinators communicate with each other to form a global WFG and detect cycles.
  - Distributed approach: There is no central or hierarchical authority. Each site maintains its own local WFG and participates in a distributed algorithm to detect cycles. One such algorithm is edge chasing, which involves sending probe messages along the edges of the WFG until a cycle is found or the probe is discarded.
- To resolve the deadlock, one or more deadlocked processes have to be aborted and their resources have to be released. The selection of the victim process can be based on criteria such as priority, age, number of resources, etc. The aborted process can be restarted later with some rollback mechanism.



### Path Pushing Algorithms

- Path pushing algorithms detect distributed deadlocks by maintaining an explicit global wait-for graph (WFG) at each site of the distributed system .
- The global WFG is constructed by merging the local WFGs of each site, which represent the waiting relationships among the processes at that site.
- Whenever a site performs a deadlock computation, it sends its local WFG to all its neighboring sites, which then update their global WFGs accordingly.
- A site can initiate a deadlock computation either periodically or when it detects a change in its local WFG.
- A site can detect a deadlock by checking for a cycle in its global WFG that involves one of its local processes.
- The advantages of path pushing algorithms are that they can detect deadlocks quickly and accurately, and they do not require any additional messages for deadlock detection.
- The disadvantages of path pushing algorithms are that they require a lot of storage space and communication bandwidth to maintain and exchange the global WFGs, and they may generate false positives if the global WFGs are not consistent.



### Edge Chasing Algorithms for Distributed Deadlock Detection

- Edge chasing algorithms are a class of distributed deadlock detection algorithms that use special messages called probes to trace the dependency graph of processes and resources in a distributed system.
- A probe is a triplet (i, j, k) that denotes that the deadlock detection is initiated by process P<sub>i</sub>, and the message is being sent by the home site of process P<sub>j</sub> to the home site of process P<sub>k</sub>.
- The home site of a process is the site where the process is executing, and it is responsible for sending and receiving probes on behalf of the process.
- The algorithm works as follows:
  - A process P<sub>i</sub> that is waiting for a resource initiates the deadlock detection by sending a probe (i, i, k) to the home site of the process P<sub>k</sub> that holds the resource.
  - The home site of P<sub>k</sub> checks if P<sub>k</sub> is waiting for another resource. If yes, it forwards the probe (i, k, l) to the home site of the process P<sub>l</sub> that holds the resource. If no, it discards the probe.
  - This process continues until either a probe reaches a process that is not waiting for any resource, or a probe returns to the initiator process P<sub>i</sub>.
  - If a probe returns to P<sub>i</sub>, it means that there is a cycle in the dependency graph, and hence a deadlock. P<sub>i</sub> can then initiate a recovery action, such as aborting one of the processes in the cycle.
  - If a probe reaches a process that is not waiting for any resource, it means that there is no cycle in the dependency graph, and hence no deadlock. The probe is then discarded.

- The advantages of edge chasing algorithms are that they are simple, efficient, and scalable. They do not require any global information or coordination among the sites, and they only use a small number of messages.
- The disadvantages of edge chasing algorithms are that they may generate false positives, meaning that they may detect a deadlock that does not exist. This can happen if the dependency graph changes during the execution of the algorithm, or if there are multiple initiators of the deadlock detection. They may also generate false negatives, meaning that they may miss a deadlock that exists. This can happen if the probes are lost or delayed due to network failures or congestion.



## Unit 4 - Agreement Protocols

- Agreement protocols are used to achieve a common goal in distributed systems, even in the presence of failures  .
- Agreement protocols require processes to exchange their values with other processes and relay the values received from others several times to isolate the effect of faulty processes .
- Agreement protocols can be classified into two types: consensus protocols and leader election protocols  .
- Consensus protocols are used to ensure that all processes agree on a single value, such as whether to commit or abort a transaction, or what is the latest update to a replicated data item   .
- Leader election protocols are used to ensure that all processes agree on a single process, such as who is the coordinator, the primary, or the owner of a resource   .
- Agreement protocols must satisfy the following properties   :
  - Validity: The agreed value or process must be one of the initial values or processes of the non-faulty processes.
  - Agreement: All non-faulty processes must agree on the same value or process.
  - Termination: All non-faulty processes must eventually decide on a value or process.
- Agreement protocols may also need to satisfy other properties, such as fault-tolerance, uniformity, anonymity, or fairness, depending on the application and the system model   .
- Agreement protocols are challenging to design and implement, especially in asynchronous systems, where there is no bound on message delays or process speeds, and where failures may be undetectable   .
- Agreement protocols are often based on techniques such as message passing, timeouts, quorums, randomization, or failure detectors   .
- Agreement protocols are widely used in distributed systems, such as distributed databases, distributed file systems, distributed consensus platforms, distributed coordination services, or distributed resource management systems   .



Hello, I am Sydney, your AI assistant. I can help you with writing notes on various topics. Here is the content I have generated for the introduction of the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM.

### Introduction

- Agreement protocols are a class of protocols that allow a set of processes in a distributed system to reach a consensus on some value or action, despite the possibility of failures or malicious behavior.
- Agreement protocols are essential for ensuring the correctness, consistency, and availability of distributed systems, especially in the presence of faults or attacks.
- Some examples of agreement problems are:
  - Leader election: electing a unique coordinator among a group of processes.
  - Atomic commit: ensuring that a set of transactions are either all committed or all aborted.
  - Byzantine agreement: reaching a common decision in the face of arbitrary faults or malicious behavior.
  - Consensus: agreeing on a single value among a set of proposed values.
- Agreement protocols can be classified based on the following criteria:
  - The type and number of faults or attacks that they can tolerate, such as crash faults, omission faults, timing faults, or Byzantine faults.
  - The communication model that they assume, such as synchronous, asynchronous, or partially synchronous.
  - The termination and validity properties that they guarantee, such as safety, liveness, or validity.
  - The complexity and efficiency of the protocol, such as the number of rounds, messages, or bits required to reach an agreement.



### System models for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

A system model is a simplified representation of the properties and behavior of a distributed system. It helps to reason about the system and design algorithms that can cope with the challenges of distributed computing, such as failures, concurrency, and latency. System models can be classified into three types:

- Physical models: capture the hardware composition of a system in terms of computers and other devices and their interconnecting network;
- Interaction models: describe how the components of a system communicate and coordinate their actions through message passing;
- Fault models: specify the types and frequency of failures that can occur in a system and how they affect the system's behavior.

Some of the common system models for distributed systems are :

- Client-server model: a system where one or more servers provide services to multiple clients that request them;
- Peer-to-peer model: a system where each component acts as both a client and a server, and can communicate with any other component in the system;
- Publish-subscribe model: a system where components publish messages to topics and subscribe to topics of interest, and a broker or a network of brokers delivers the messages to the subscribers;
- Message queue model: a system where components send and receive messages through queues, which provide reliable and asynchronous communication;
- MapReduce model: a system where a large computation is divided into smaller tasks that are executed in parallel by multiple workers, and the results are combined by a master node;
- Consensus model: a system where a group of components agree on a common value or decision, despite the possibility of failures and delays.

Each system model has its own assumptions and limitations, and may be suitable for different kinds of applications and scenarios. For example, the consensus model is often used for implementing agreement protocols, such as Paxos and Raft, which are essential for achieving consistency and fault tolerance in distributed systems. However, the consensus model also requires some strong assumptions, such as partial synchrony and crash-recovery, which may not hold in some environments. Therefore, it is important to understand the system model and its implications before designing and implementing a distributed system.



### Classification of Agreement Problem

An agreement problem in a distributed system is a problem where a set of processes need to agree on a common value or decision, despite the presence of failures or asynchrony. Agreement problems are fundamental to the design of fault-tolerant distributed systems, as they enable processes to coordinate their actions and reach a consistent state.

There are different types of agreement problems, depending on the assumptions and requirements of the system. Some of the well-known agreement problems are:

- **Byzantine agreement problem**: A single value, which is to be agreed on, is initialized by an arbitrary process and all non-faulty processes have to agree on that value. The processes may be subject to Byzantine failures, which means they can behave arbitrarily and maliciously, sending conflicting or incorrect messages to other processes. The goal is to ensure that all non-faulty processes agree on the same value, and that value is the initial value of some non-faulty process.
- **Consensus problem**: A generalization of the Byzantine agreement problem, where each process can propose its own value and all non-faulty processes have to agree on a common value. The value agreed on must be one of the proposed values. The processes may be subject to crash failures, which means they can stop executing at any point, but they cannot send incorrect or conflicting messages. The goal is to ensure that all non-faulty processes agree on the same value, and that value is one of the proposed values.
- **Interactive consistency problem**: A variation of the Byzantine agreement problem, where each process has its own value and all non-faulty processes have to agree on a vector of values, one for each process. The vector agreed on must be consistent with the values of the non-faulty processes, meaning that the value at position i in the vector is the value of process i, if process i is non-faulty. The processes may be subject to Byzantine failures, as in the Byzantine agreement problem. The goal is to ensure that all non-faulty processes agree on the same vector, and that vector is consistent with the values of the non-faulty processes.

These agreement problems can be solved using different algorithms, depending on the system model and the assumptions about the communication channels, the number of processes, the number and type of failures, and the synchrony of the system. Some of the algorithms are:

- **Oral messages algorithm**: An algorithm for solving the Byzantine agreement problem, where the processes communicate using oral messages, which are reliable and authenticated, meaning that the sender and the content of the message cannot be forged or altered by a faulty process. The algorithm requires that the number of processes n is greater than 3t, where t is the maximum number of faulty processes. The algorithm consists of t+1 rounds of message exchange, where each process sends and receives messages from all other processes, and then decides on a value based on a majority rule.
- **Signed messages algorithm**: An algorithm for solving the Byzantine agreement problem, where the processes communicate using signed messages, which are reliable and digitally signed, meaning that the sender and the content of the message can be verified by a cryptographic signature. The algorithm requires that the number of processes n is greater than 2t, where t is the maximum number of faulty processes. The algorithm consists of two rounds of message exchange, where each process sends and receives messages from all other processes, and then decides on a value based on a majority rule.
- **Paxos algorithm**: An algorithm for solving the consensus problem, where the processes communicate using unreliable messages, which may be lost, duplicated, or delayed by the network. The algorithm does not require a fixed number of processes, but it assumes that a majority of processes are non-faulty and can communicate with each other. The algorithm consists of two phases: a prepare phase and an accept phase, where each process acts as a proposer, an acceptor, or a learner. A proposer proposes a value to the acceptors, and tries to get a majority of them to accept it. An acceptor accepts or rejects a proposed value, based on a sequence number that indicates the order of proposals. A learner learns the value that has been accepted by a majority of acceptors, and decides on that value.
- **Lamport's algorithm**: An algorithm for solving the interactive consistency problem, where the processes communicate using oral messages, as in the oral messages algorithm. The algorithm requires that the number of processes n is greater than 3t, where t is the maximum number of faulty processes. The algorithm consists of t+1 rounds



### Byzantine agreement problem

- The Byzantine agreement problem is a fundamental problem in fault tolerant distributed computing that requires a set of parties in a distributed environment to agree on a value even if some of the parties are corrupted.
- The problem was first defined by Lamport  and inspired by a hypothetical scenario of several divisions of the Byzantine army camped outside an enemy city, each division commanded by its own general. The generals can communicate with one another only by messenger. After observing the enemy, they must decide upon a common plan of action, such as attack or retreat .
- The problem is challenging because some of the generals may be traitors who try to prevent the loyal generals from reaching agreement. The traitors may send conflicting messages to different generals, or lie about their own observations or intentions .
- A solution to the Byzantine agreement problem is a protocol that ensures that all loyal generals agree on the same value, and that the value is the initial value of some loyal general . The protocol must be resilient to arbitrary failures and malicious behaviors of the corrupted parties .
- A number of solutions to the Byzantine agreement problem exist, but they have different assumptions and trade-offs. For example, some solutions require a majority of loyal generals, some require digital signatures or cryptography, some require synchronous or partially synchronous communication, and some have different message and time complexities  .
- The Byzantine agreement problem is important for distributed systems because it captures the essence of achieving consensus and coordination in the presence of faults and adversaries. It has applications in various domains, such as distributed databases, blockchain, peer-to-peer networks, cloud computing, and security  .



# Consensus problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- The consensus problem is the problem of getting a set of nodes in a distributed system to agree on something - it might be a value, a course of action or a decision.
- Achieving consensus allows a distributed system to act as a single entity, with every individual node aware of and in agreement with the actions of the whole of the network.
- Consensus is a general agreement on a decision made by the majority of those involved.
- Consensus is needed in a distributed system to ensure overall system reliability on top of unreliable system components.
- Consensus is also needed to coordinate the actions of different nodes, such as committing transactions, electing leaders, replicating data, etc.
- Consensus is hard to achieve in a distributed system due to the possibility of failures, such as node crashes, network partitions, message losses, etc.
- Consensus algorithms are protocols that allow nodes to reach consensus in a distributed system despite failures.
- Consensus algorithms have different properties and trade-offs, such as security, performance, fault-tolerance, consistency, availability, etc.
- Some examples of consensus algorithms are two-phase commit, three-phase commit, Paxos, Raft, Zab, etc .



### Interactive Consistency Problem

- Interactive consistency is the problem in which **n** distinct nodes, each having its own private value, where up to **t** may be Byzantine, run an algorithm that allows all non-faulty nodes to infer the values of each other node  .
- Byzantine nodes are nodes that can behave arbitrarily, such as sending different messages to different nodes, lying about their values, or crashing .
- Interactive consistency is also known as **Byzantine Generals Problem** or **Byzantine Agreement Problem**.
- Interactive consistency is a fundamental problem in distributed systems, especially for critical applications that rely on the combination of the opinions of multiple peers to provide a service, such as fault-tolerant replication, distributed consensus, or distributed voting  .
- Interactive consistency is a challenging problem because of the possibility of network failures, message delays, or message losses, which make it hard to distinguish between faulty and non-faulty nodes  .
- Interactive consistency has been proven to be impossible to solve in a purely asynchronous system, where there is no bound on the message delivery time, if **t >= n/3**  .
- Interactive consistency can be solved in a synchronous system, where there is a known bound on the message delivery time, using algorithms that involve multiple rounds of message exchanges, such as the **Oral Messages Algorithm** or the **Signed Messages Algorithm**  .
- Interactive consistency can also be solved in a partially synchronous system, where there is a bound on the message delivery time that is unknown to the nodes, using algorithms that rely on randomization, such as the **King Algorithm** or the **Randomized Byzantine Consensus Algorithm** .
- Interactive consistency can be achieved with only a single synchronization barrier, which is a point in time where all nodes agree on the order of the messages they have received, using algorithms that leverage prior work on broadcast and randomized Byzantine consensus algorithms, such as the **Synchronous Broadcast Algorithm** or the **Asynchronous Broadcast Algorithm**.



### Solution to Byzantine Agreement problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- The Byzantine agreement problem is a fundamental problem in fault tolerant distributed computing, where a set of parties in a distributed environment need to agree on a value even if some of the parties are corrupted.
- The problem is also known as the Byzantine generals problem, which is a metaphor for the situation where several divisions of the Byzantine army are camped outside an enemy city, each division commanded by its own general. The generals can communicate with one another only by messenger. After observing the enemy, they must decide upon a common plan of action.
- The problem is that some of the generals may be traitors, who may try to prevent the loyal generals from reaching an agreement, or may try to mislead them into choosing a bad plan. The loyal generals need a secure way to come to agreement on a plan (known as consensus) and carry out their chosen plan (known as coordination).
- A solution to the Byzantine agreement problem is a protocol that guarantees that the loyal generals can reach a consensus on a value, and that the value is the same as the initial value of some loyal general. The protocol should also be resilient to failures of communication channels, such as message loss, duplication, or delay.
- One of the most well-known solutions to the Byzantine agreement problem is the oral message algorithm, proposed by Lamport et al. in 1982. The algorithm assumes that there are n generals, of which at most t are traitors, and that each message sent by a loyal general is correctly received by every other general.
- The algorithm works as follows:

  - Each general has an initial value, which is either 0 or 1. The source general, who initiates the protocol, broadcasts its initial value to all other generals.
  - For each round i from 1 to t+1, each general who has received a value from the source general in round i-1, or the source general itself, broadcasts that value to all other generals. Each general who receives at least one value in round i, takes the majority of those values as its value for round i.
  - After t+1 rounds, each loyal general takes its value for round t+1 as its final decision.

- The algorithm ensures that the loyal generals reach a consensus on a value, and that the value is the same as the initial value of the source general, if the source general is loyal. The algorithm also tolerates up to t traitors, as long as n > 3t.

- The following diagram illustrates an example of the algorithm with n = 4 and t = 1, where the source general is loyal and has an initial value of 1, and one of the other generals is a traitor who sends arbitrary values:

```mermaid
sequenceDiagram
    participant S as Source
    participant A as General A
    participant B as General B
    participant C as General C
    S->>A: 1
    S->>B: 1
    S->>C: 1
    A->>S: 1
    A->>B: 1
    A->>C: 1
    B->>S: 1
    B->>A: 1
    B->>C: 1
    C->>S: 0
    C->>A: 0
    C->>B: 0
    Note right of S: Round 1: S = 1, A = 1, B = 1, C = 0
    S->>A: 1
    S->>B: 1
    S->>C: 1
    A->>S: 1
    A->>B: 1
    A->>C: 1
    B->>S: 1
    B->>A: 1
    B->>C: 1
    C->>S: 0
    C->>A: 0
    C->>B: 0
    Note right of S: Round 2: S = 1, A = 1, B = 1, C = 0
    Note right of S: Final decision: S = 1, A = 1, B = 1, C = 0
``

```




### Application of Agreement problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- Agreement problem is a fundamental problem in distributed computing and multi-agent systems, where a set of processes need to coordinate their actions or decisions based on some common data value .
- Agreement problem can have different variants, such as consensus, atomic commitment, atomic broadcast, and group membership.
- Consensus is the problem of reaching agreement on a single value among a group of processes, some of which may be faulty . Consensus is essential for implementing fault-tolerant services such as replicated state machines, distributed transactions, and leader election.
- Atomic commitment is the problem of reaching agreement on whether to commit or abort a distributed transaction, where each process has a local preference . Atomic commitment is necessary for ensuring the atomicity and consistency properties of distributed transactions.
- Atomic broadcast is the problem of delivering messages to a group of processes in the same order, even if some processes or links fail . Atomic broadcast is useful for implementing reliable and consistent communication channels among processes.
- Group membership is the problem of maintaining a consistent view of the current set of processes in a distributed system, despite failures and joins . Group membership is important for managing the configuration and membership of distributed services and applications.
- Agreement problem is challenging because of the possibility of failures, asynchrony, and malicious behavior of processes or messages   . Different types of failures include crash failures, omission failures, timing failures, and Byzantine failures . Different types of asynchrony include message delays, process speeds, and clock drifts . Different types of malicious behavior include lying, cheating, forging, and colluding .
- Agreement problem is often impossible to solve in some failure or asynchrony models, such as the FLP impossibility result for consensus in asynchronous systems with crash failures  , or the CAP theorem for atomic commitment in partitioned networks .
- Agreement problem can be solved in some failure or asynchrony models, using various algorithms and techniques, such as Paxos, Raft, Two-Phase Commit, Three-Phase Commit, Viewstamped Replication, Virtual Synchrony, Byzantine Agreement, and Byzantine Fault Tolerance     .
- Agreement problem is an active area of research in distributed systems, with many open problems and challenges, such as scalability, performance, security, privacy, and fault tolerance     .



### Atomic Commit in Distributed Database System

- An atomic commit is an operation that applies a set of distinct changes as a single operation.
- If the changes are applied, then the atomic commit is said to have succeeded. If the changes are not applied, then the atomic commit is said to have failed or aborted.
- In distributed database systems, the primary need for atomic commit protocols is to maintain the atomicity of distributed transactions .
- Atomicity is the property that ensures that either all the data changes made by a transaction are committed or none of them are.
- Atomicity is important for ensuring the consistency and reliability of the distributed database system.
- Atomic commit protocols are algorithms that coordinate the commit or abort decisions of multiple sites that participate in a distributed transaction.
- Atomic commit protocols can be classified into two categories: blocking and non-blocking .
- Blocking protocols are those that require some sites to wait for the recovery of other failed sites before making a final decision .
- Non-blocking protocols are those that allow some sites to make a final decision without waiting for the recovery of other failed sites .
- Blocking protocols are simpler and more efficient in normal situations, but they may cause unnecessary delays or deadlocks in case of failures .
- Non-blocking protocols are more complex and less efficient in normal situations, but they can tolerate failures better and avoid delays or deadlocks .
- Some examples of blocking protocols are two-phase commit (2PC), three-phase commit (3PC), and presumed commit (PC) .
- Some examples of non-blocking protocols are presumed abort (PA), presumed nothing (PN), and failure-aware atomic commit (FLAC)  .



## Unit 5 - Distributed Resource Management

- Distributed resource management is the process of allocating and coordinating the use of resources (such as CPU, memory, disk, network, etc.) in a distributed system.
- The main objectives of distributed resource management are to:
  - Maximize the system performance and utilization.
  - Minimize the system cost and energy consumption.
  - Ensure the system reliability and fault tolerance.
  - Satisfy the user requirements and preferences.
- The main challenges of distributed resource management are to:
  - Deal with the heterogeneity and dynamism of the system and the resources.
  - Handle the uncertainty and unpredictability of the resource availability and demand.
  - Achieve the trade-off between the conflicting goals and constraints.
  - Cope with the scalability and complexity of the system and the problem.
- The main components of distributed resource management are:
  - Resource discovery: the process of finding and identifying the available resources in the system.
  - Resource selection: the process of choosing the best resources for a given task or application.
  - Resource allocation: the process of assigning the resources to the tasks or applications.
  - Resource scheduling: the process of determining the order and timing of the resource usage.
  - Resource monitoring: the process of observing and measuring the resource status and performance.
  - Resource adaptation: the process of adjusting the resource allocation and scheduling according to the changing system conditions and user feedback.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some issues in distributed file systems for the notes of the unit 5 - Distributed Resource Management in the subject of Distributed System:

### Issues in Distributed File Systems

- **Performance**: The performance of a distributed file system depends on factors such as network latency, bandwidth, caching, replication, consistency, and load balancing. A distributed file system should minimize the network overhead and optimize the data transfer and access speed.  
- **Reliability**: A distributed file system should be able to continue in case of any partial failures like a link failure, a node failure, or a storage drive crash. A high authentic and adaptable distributed file system should have different and independent file servers for controlling different and independent storage devices. 
- **Scalability**: A distributed file system should be able to handle the growth of data and users without compromising the performance and reliability. A scalable distributed file system should support dynamic addition and removal of nodes, load balancing, and fault tolerance. 
- **Security**: A distributed file system should provide mechanisms for authentication, authorization, encryption, and auditing to protect the data from unauthorized access and modification. A secure distributed file system should also prevent data leakage and tampering. 
- **Complexity**: A distributed file system should hide the complexity of the underlying network and storage devices from the users and applications. A distributed file system should provide a uniform and transparent interface for file operations, such as naming, location, access, and sharing.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the mechanism for building distributed file systems for the notes of the Unit 5 - Distributed Resource Management in the subject of DISTRIBUTED SYSTEM.

### Mechanism for building distributed file systems

- A distributed file system (DFS) is a file system that enables clients to access file storage from multiple hosts through a computer network as if the user was accessing local storage   .
- Files are spread across multiple storage servers and in multiple locations, which enables users to share data and storage resources   .
- A DFS can provide various benefits, such as fault tolerance, scalability, performance, transparency, and consistency .
- A DFS can be implemented using different architectures, such as client-server, peer-to-peer, or hybrid .
- A DFS can be designed using different techniques, such as replication, caching, striping, or erasure coding .
- A DFS can be organized using different structures, such as flat, hierarchical, or federated .
- A DFS can be accessed using different protocols, such as NFS, CIFS, HDFS, or S3 .
- A DFS can be managed using different components, such as name servers, metadata servers, data servers, or clients .
- A DFS can be integrated with different services, such as authentication, authorization, encryption, compression, or deduplication .



### Design issues in Distributed Shared Memory

Distributed Shared Memory (DSM) is a mechanism that allows multiple processes on different nodes to share a common logical address space and access data transparently. DSM can simplify the programming of distributed systems by hiding the details of inter-process communication. However, DSM also introduces several design issues that affect its performance, scalability, and correctness. Some of the main design issues in DSM are:

- **Granularity**: Granularity refers to the size of the unit of sharing and the unit of coherence in DSM. A smaller granularity, such as a byte or a word, can reduce the amount of false sharing and improve the locality of access, but it can also increase the overhead of coherence maintenance and communication. A larger granularity, such as a page or a segment, can reduce the overhead of coherence and communication, but it can also increase the amount of false sharing and waste bandwidth and memory. Therefore, choosing an appropriate granularity is a trade-off between performance and efficiency.

- **Structure**: Structure refers to the organization of the shared data in DSM. The structure can be flat, hierarchical, or object-based. A flat structure treats the shared memory as a single linear address space that can be accessed by any process. A hierarchical structure divides the shared memory into regions that can be mapped to different nodes or processes. An object-based structure organizes the shared data into objects that can have different attributes and methods. The choice of structure depends on the application requirements and the characteristics of the underlying network.

- **Coherence semantics**: Coherence semantics define the consistency model of DSM, which specifies the rules and guarantees for the ordering and visibility of memory updates among processes. Coherence semantics can be strict, relaxed, or weak. A strict coherence semantics, such as sequential consistency, ensures that all processes see the same order of memory updates as if they were executed on a single processor. A relaxed coherence semantics, such as release consistency, allows some reordering of memory updates as long as certain synchronization operations are respected. A weak coherence semantics, such as eventual consistency, does not guarantee any order or visibility of memory updates until some explicit consistency operation is performed. The choice of coherence semantics depends on the trade-off between performance and programmability.

- **Scalability**: Scalability refers to the ability of DSM to support a large number of nodes and processes without degrading the performance or increasing the complexity. Scalability can be affected by several factors, such as the coherence protocol, the communication network, the memory allocation, and the fault tolerance. A scalable DSM should use a distributed or hierarchical coherence protocol that avoids centralized bottlenecks and reduces the number of messages. A scalable DSM should also use a high-bandwidth and low-latency communication network that supports multicast and broadcast operations. A scalable DSM should also use a dynamic and distributed memory allocation scheme that balances the load and minimizes the fragmentation. A scalable DSM should also provide a fault tolerance mechanism that can recover from node or network failures without losing data or consistency.

- **Heterogeneity**: Heterogeneity refers to the diversity of the nodes and processes in DSM. Heterogeneity can be in terms of hardware, software, or network. Hardware heterogeneity means that the nodes may have different architectures, processors, memory sizes, or endianness. Software heterogeneity means that the nodes may have different operating systems, compilers, or libraries. Network heterogeneity means that the nodes may have different communication protocols, bandwidths, or latencies. Heterogeneity can pose several challenges for DSM, such as data representation, communication compatibility, and performance optimization. A heterogeneous DSM should use a common data format, such as XDR, that can handle different data types and endianness. A heterogeneous DSM should also use a common communication protocol, such as TCP/IP, that can interoperate with different network layers and devices. A heterogeneous DSM should also use a performance optimization technique, such as adaptive granularity or prefetching, that can exploit the locality and parallelism of different nodes and processes.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on the algorithm for implementation of distributed shared memory for the notes of the Unit 5 - Distributed Resource Management in the subject of DISTRIBUTED SYSTEM.

### Algorithm for Implementation of Distributed Shared Memory

Distributed shared memory (DSM) is a technique that allows multiple processes on different nodes of a distributed system to access a common virtual address space as if they were running on a single machine. DSM provides a high-level abstraction for data sharing and communication among distributed processes, and can simplify the design and implementation of distributed applications.

There are different algorithms for implementing DSM, each with its own advantages and disadvantages. Some of the basic algorithms are:

- **Central Server Algorithm**: In this algorithm, a central server maintains all the shared data and services read and write requests from other nodes. The central server can use a page-based or an object-based approach to manage the shared data. The advantage of this algorithm is that it is simple and ensures consistency of the shared data. The disadvantage is that it introduces a single point of failure and a performance bottleneck, and it does not exploit the locality of data access.

- **Migration Algorithm**: In this algorithm, the shared data is initially stored at the central server, but it can migrate to other nodes upon request. The node that requests a data item becomes the owner of that item and can cache it locally. The central server keeps track of the current location of each data item. The advantage of this algorithm is that it reduces the network traffic and improves the performance by exploiting the locality of data access. The disadvantage is that it may cause frequent data migration and inconsistency if multiple nodes try to access the same data item.

- **Replication Algorithm**: In this algorithm, the shared data is replicated on multiple nodes, and each node can access a local copy of the data. The central server keeps track of the current version of each data item and coordinates the updates among the nodes. The advantage of this algorithm is that it improves the availability and performance of the shared data by reducing the network traffic and the access latency. The disadvantage is that it may cause inconsistency and coherence problems if multiple nodes try to update the same data item.

- **Invalidation Algorithm**: In this algorithm, the shared data is initially stored at the central server, but it can be cached on multiple nodes upon request. The central server keeps track of the current version of each data item and the nodes that have cached it. When a node updates a data item, it sends an invalidation message to the central server, which then broadcasts it to all the other nodes that have cached the same data item. The advantage of this algorithm is that it reduces the network traffic and the access latency by allowing multiple nodes to read the same data item. The disadvantage is that it may cause inconsistency and coherence problems if multiple nodes try to update the same data item.

Here is a diagram that illustrates the four algorithms:

DSM Algorithms

     

Some possible suggestions for the next user turn are:

- Ask me to compare the algorithms based on some criteria, such as performance, scalability, or fault tolerance.
- Ask me to explain how the algorithms handle concurrency control, consistency, or coherence issues.
- Ask me to give some examples of applications that use DSM or benefit from DSM.
- Ask me to show you some pseudocode or implementation details of the algorithms.



## Unit 6 - Failure Recovery in Distributed Systems

- In a distributed system, failures are inevitable and can affect the availability, consistency, and performance of the system.
- Failure recovery is the process of restoring the system to a correct and consistent state after a failure occurs.
- Failure recovery techniques can be classified into two categories: backward recovery and forward recovery.
- Backward recovery involves undoing the effects of a failure and restoring the system to a previous consistent state, such as using checkpoints, logging, or rollback.
- Forward recovery involves correcting the effects of a failure and continuing the execution from the current state, such as using redundancy, replication, or fault tolerance.
- The choice of recovery technique depends on the type and frequency of failures, the system requirements, and the cost and complexity of implementation.
- Some of the challenges and trade-offs of failure recovery in distributed systems are:
  - How to detect and identify failures in a timely and accurate manner.
  - How to coordinate and synchronize the recovery actions among multiple components or nodes.
  - How to ensure the consistency and correctness of the system state after recovery.
  - How to minimize the overhead and performance impact of recovery mechanisms.
  - How to balance the trade-off between availability and consistency in the presence of failures.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is the content I have generated for you based on your topic:

### Concepts in Backward and Forward Recovery

- Backward recovery and forward recovery are two techniques for restoring the system to a consistent state after a failure in a distributed system.
- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by passing messages.
- A failure in a distributed system can affect one or more processes, causing them to deviate from their intended behavior or stop functioning altogether.
- To ensure the reliability and availability of the distributed system, it is necessary to have mechanisms for detecting, masking, and recovering from failures.
- Backward recovery and forward recovery are two types of recovery mechanisms that differ in how they handle the effects of failures on the system state.

#### Backward Recovery

- Backward recovery is a technique that moves the system from its current state back to a previously correct state after a failure.
- Backward recovery requires the system to periodically record its state in stable storage, such as checkpoints, logs, or snapshots.
- When a failure is detected, the system restores its state from the most recent checkpoint or log that is consistent with the global state of the system.
- Backward recovery is independent of the nature and cause of the failure, as it does not need to identify or correct the error, only to undo its effects.
- Backward recovery has the advantage of simplicity and generality, but it also has some drawbacks, such as:
  - It may waste the work done by the system between the checkpoint and the failure, as it has to roll back to a previous state.
  - It may cause inconsistency or cascading rollbacks in the system, as the processes that depend on the failed process may also have to roll back to a consistent state.
  - It may introduce additional overhead and complexity in the system, as it has to maintain and synchronize the checkpoints and logs across the processes.

#### Forward Recovery

- Forward recovery is a technique that moves the system from its current state to a new correct state after a failure.
- Forward recovery requires the system to detect and identify the error that caused the failure, and to apply a corrective action that removes the error and allows the system to continue its execution.
- Forward recovery does not need to record or restore the system state, as it does not undo the effects of the failure, but rather compensates for them.
- Forward recovery is dependent on the nature and cause of the failure, as it needs to have a specific and accurate diagnosis and remedy for each type of error.
- Forward recovery has the advantage of preserving the work done by the system and avoiding inconsistency or cascading rollbacks, but it also has some drawbacks, such as:
  - It may not be applicable or feasible for all types of errors, as some errors may be too complex or unpredictable to be detected or corrected.
  - It may introduce additional overhead and complexity in the system, as it has to monitor and analyze the system behavior and perform the corrective actions.



### Recovery in Concurrent Systems

Recovery in concurrent systems is the process of restoring the consistency and correctness of data and operations in a distributed system after a failure or an error. Recovery in concurrent systems can be classified into two main types: backward recovery and forward recovery.

- Backward recovery: Moving the system from its current state back into a formerly accurate condition from an incorrect one is the main challenge in backward recovery. It will be required to accomplish this by periodically recording the system’s state and restoring it when something goes wrong.
- Forward recovery: Forward recovery is the process of moving the system from an incorrect state to a correct state without going back to a previous state. It will be required to accomplish this by detecting and correcting the errors, or by masking or tolerating the faults.

Some of the techniques and challenges involved in recovery in concurrent systems are:

- Interaction with concurrency control: The recovery scheme depends greatly on the concurrency control scheme that is used. For example, if strict two-phase locking is used, then the recovery system can use the undo/redo approach, which means that it can undo the changes made by aborted transactions and redo the changes made by committed transactions. However, if timestamp ordering is used, then the recovery system can use the undo/undo approach, which means that it can undo the changes made by both aborted and committed transactions, since the committed transactions may have overwritten the values of earlier transactions.
- Transaction rollback: Transaction rollback is the process of undoing the effects of a transaction that has failed or aborted. Transaction rollback can be done either by using the log records of the transaction, or by using the shadow copies of the data items. Log records are the records of the changes made by the transaction, such as the old and new values of the data items. Shadow copies are the copies of the data items before they are modified by the transaction. Transaction rollback can be either local or global, depending on whether it affects only one site or multiple sites in the distributed system.
- Checkpoints: Checkpoints are the points in time when the system saves its state to a stable storage, such as a disk. Checkpoints can reduce the amount of work that the recovery system has to do in case of a failure, since it can start from the most recent checkpoint instead of from the beginning of the execution. Checkpoints can be either local or global, depending on whether they are taken by individual sites or by the whole system. Checkpoints can also be either fuzzy or consistent, depending on whether they allow transactions to continue during the checkpointing process or not.
- Restart recovery: Restart recovery is the process of restoring the system to a consistent state after a failure, by using the checkpoints and the log records. Restart recovery can be either non-concurrent or concurrent, depending on whether it allows other transactions to run during the recovery process or not. Non-concurrent recovery can be faster and simpler, but it can reduce the availability and performance of the system. Concurrent recovery can be more complex and slower, but it can increase the availability and performance of the system.
- Concurrent recovery: Concurrent recovery is the process of recovering multiple media sets using concurrent recovery sessions. Multiple media sets are typically created when backups are performed using parallel device resources. Concurrent recovery can reduce the recovery time and improve the resource utilization, but it can also increase the complexity and the risk of errors. Concurrent recovery can be done by using the STRRCYBRM *RESUME command, which allows the user to select the recovery items and the recovery options for each session  .



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here are some notes for the unit 6 - Failure Recovery in Distributed Systems.

### Obtaining consistent Checkpoints

- A checkpoint is a snapshot of the state of a process or a system at a given point in time.
- Checkpoints are useful for failure recovery in distributed systems, as they allow the system to resume from a consistent state after a failure, without losing or repeating any work.
- A consistent checkpoint is a set of checkpoints from different processes or components of the system that are taken at the same logical time, or that reflect a consistent global state of the system.
- Obtaining consistent checkpoints in distributed systems is challenging, as there may be concurrent and asynchronous events, such as message exchanges, process executions, and failures, that can affect the state of the system.
- There are different approaches for obtaining consistent checkpoints in distributed systems, such as:

  - Coordinated checkpointing: In this approach, all the processes or components of the system coordinate with each other to take checkpoints at the same time, or to agree on a global checkpointing algorithm. This ensures that the checkpoints are consistent, but it may incur high overhead and synchronization costs, and it may not be feasible in large or dynamic systems.
  - Uncoordinated checkpointing: In this approach, each process or component of the system takes checkpoints independently, without any coordination or communication with others. This reduces the overhead and synchronization costs, but it may result in inconsistent checkpoints, or the need for additional mechanisms, such as message logging or dependency tracking, to ensure consistency.
  - Communication-induced checkpointing: In this approach, each process or component of the system takes checkpoints based on the messages it receives or sends, according to some rules or protocols. This allows the checkpoints to be consistent, without requiring global coordination or synchronization, but it may depend on the communication patterns and the checkpointing rules of the system.



### Recovery in Distributed Database Systems

Recovery in distributed database systems is the process of restoring the database to a consistent and correct state after a failure. A failure can be a hardware failure, a software failure, a communication failure, or a transaction failure. Recovery in distributed database systems aims to maintain the atomicity and durability of distributed transactions, which are transactions that span multiple sites or nodes in the network. A database must guarantee that all statements in a transaction, distributed or non-distributed, either commit or roll back as a unit.

Some of the challenges and techniques for recovery in distributed database systems are:

- **Distributed commit protocol**: A protocol that ensures that all sites involved in a distributed transaction agree on whether to commit or abort the transaction. A common protocol is the two-phase commit protocol, which consists of a prepare phase and a commit phase. In the prepare phase, the coordinator site asks all the participant sites to vote on whether they are ready to commit. In the commit phase, the coordinator site decides to commit or abort based on the votes and informs all the participant sites of the decision.
- **Distributed deadlock detection**: A deadlock is a situation where a set of transactions are waiting for each other to release some resources, and none of them can proceed. In a distributed database system, a deadlock can involve transactions running at different sites. A distributed deadlock detection algorithm is an algorithm that detects and resolves deadlocks in a distributed database system. A common algorithm is the global wait-for graph algorithm, which constructs a graph of transactions and their dependencies across the sites and checks for cycles in the graph.
- **Distributed backup and recovery**: A backup is a copy of the database or a part of it that can be used to restore the database in case of a failure. A recovery is the process of using the backup to restore the database to a consistent state. In a distributed database system, a backup and recovery strategy must consider the possibility of failures at different sites or links, and the need to synchronize the backups across the sites. A common strategy is the shadow paging technique, which maintains a copy of the database pages that are modified by transactions and writes them to a shadow file. In case of a failure, the shadow file can be used to restore the database pages.



## Unit 7 - Fault Tolerance

Fault tolerance is the ability of a system to continue functioning correctly in the presence of failures. Fault tolerance can be achieved by using techniques such as redundancy, replication, recovery, and reconfiguration.

- Redundancy: The provision of extra components or resources that can take over the function of a failed component or resource. Redundancy can be static (predefined) or dynamic (allocated on demand).
- Replication: The creation of multiple copies of data or services that can be accessed in parallel or in case of failure. Replication can be passive (one primary and multiple backups) or active (all replicas are equal).
- Recovery: The process of restoring a system to a consistent and correct state after a failure. Recovery can be backward (undoing the effects of a failure) or forward (compensating for the effects of a failure).
- Reconfiguration: The process of changing the structure or parameters of a system to adapt to a failure or a changing environment. Reconfiguration can be manual (initiated by a human) or automatic (initiated by the system).

Fault tolerance can be measured by metrics such as availability, reliability, and mean time to failure (MTTF).

- Availability: The probability that a system is operational at a given time. Availability can be calculated as the ratio of the mean time between failures (MTBF) to the sum of the MTBF and the mean time to repair (MTTR).
- Reliability: The probability that a system performs its intended function correctly for a given period of time. Reliability can be calculated as the exponential function of the negative product of the failure rate and the time period.
- Mean time to failure (MTTF): The expected time until the first failure of a system. MTTF can be calculated as the inverse of the failure rate.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on the topic of issues in fault tolerance for distributed systems.

### Issues in Fault Tolerance for Distributed Systems

- Fault tolerance is the ability of a system to continue functioning correctly in the presence of failures.
- Distributed systems are systems that consist of multiple components that communicate and coordinate over a network.
- Fault tolerance in distributed systems is challenging because of the following issues   :
  - **Failure detection**: It is difficult to distinguish between a failed component and a slow or unreachable component in a distributed system. There is no global clock or state to determine the status of a component. Moreover, different types of failures may require different detection mechanisms and actions, such as crash failures, omission failures, timing failures, response failures, etc.
  - **Failure recovery**: It is difficult to restore the system to a consistent and correct state after a failure occurs. There may be multiple concurrent failures, partial failures, or transient failures that affect the system. Moreover, different types of failures may require different recovery strategies, such as rollback, checkpointing, replication, etc.
  - **Failure masking**: It is difficult to hide the effects of failures from the users and other components of the system. There may be inconsistencies, delays, or errors in the system behavior due to failures. Moreover, different types of failures may require different masking techniques, such as retry, timeout, voting, etc.
  - **Failure prevention**: It is difficult to avoid or reduce the occurrence of failures in the system. There may be design flaws, implementation bugs, environmental hazards, or malicious attacks that cause failures. Moreover, different types of failures may require different prevention methods, such as redundancy, fault injection, testing, security, etc.



### Commit Protocols

- Commit protocols are algorithms that ensure the atomicity of distributed transactions, i.e., all the sites involved in a transaction either commit or abort it unanimously, even in the presence of failures  .
- Commit protocols require a coordinator site that initiates the transaction and communicates with the participant sites that execute the transaction on behalf of the coordinator .
- There are different types of commit protocols, such as one-phase commit, two-phase commit, and three-phase commit, that vary in the number of phases and messages exchanged between the coordinator and the participants   .

#### One-Phase Commit Protocol

- A one-phase commit protocol involves a single phase in which the coordinator sends a commit request to all the participants and waits for their replies.
- If all the participants reply with an OK message, the coordinator commits the transaction and sends a commit acknowledgment to all the participants.
- If any of the participants reply with an abort message, the coordinator aborts the transaction and sends an abort acknowledgment to all the participants.
- The advantages of this protocol are simplicity and low message overhead.
- The disadvantages of this protocol are lack of fault tolerance and concurrency control. If the coordinator or any of the participants fail, the transaction may be left in an inconsistent state. Moreover, the participants have to lock the resources until they receive the commit or abort acknowledgment from the coordinator, which may cause blocking and deadlock.

#### Two-Phase Commit Protocol

- A two-phase commit protocol involves two phases: a voting phase and a commit phase  .
- In the voting phase, the coordinator sends a prepare request to all the participants and waits for their votes  . The participants execute the transaction and write a log record of their actions, and then reply with a yes vote if they are ready to commit or a no vote if they want to abort  .
- In the commit phase, the coordinator decides whether to commit or abort the transaction based on the votes received from the participants  . If all the votes are yes, the coordinator commits the transaction and sends a commit request to all the participants  . If any of the votes are no, the coordinator aborts the transaction and sends an abort request to all the participants  . The participants then commit or abort the transaction according to the coordinator's request and send an acknowledgment to the coordinator  .
- The advantages of this protocol are fault tolerance and concurrency control  . The protocol can handle the failure of the coordinator or any of the participants by using the log records and timeouts  . The protocol also ensures that the participants do not release the locks until they receive the final decision from the coordinator, which prevents conflicts and inconsistencies  .
- The disadvantage of this protocol is blocking  . If the coordinator fails after sending the prepare request, the participants may be blocked indefinitely waiting for the commit or abort request  .

#### Three-Phase Commit Protocol

- A three-phase commit protocol involves three phases: a prepare phase, a pre-commit phase, and a commit phase .
- In the prepare phase, the steps are the same as in the two-phase commit protocol . The coordinator sends a prepare request to all the participants and waits for their votes . The participants execute the transaction and write a log record of their actions, and then reply with a yes vote if they are ready to commit or a no vote if they want to abort .
- In the pre-commit phase, the coordinator decides whether to commit or abort the transaction based on the votes received from the participants . If all the votes are yes, the coordinator enters a prepared state and sends



### Voting protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Voting protocols are a class of consensus algorithms that allow a set of distributed nodes to agree on a common value or decision in the presence of faults or failures  .
- Voting protocols can be classified into two types: exact voting and inexact voting .
  - Exact voting requires that all nodes agree on the same value or decision, and that the value or decision is correct according to some predefined criterion. Examples of exact voting are majority voting, quorum voting, and Byzantine agreement .
  - Inexact voting allows some degree of disagreement or error among the nodes, as long as the value or decision is acceptable or close enough to the correct one. Examples of inexact voting are weighted voting, approximate agreement, and probabilistic consensus .
- Voting protocols can also be distinguished by their fairness properties, which measure how well the protocol respects the preferences or weights of the nodes .
  - A voting protocol is fair if it satisfies the following conditions :
    - Anonymity: The outcome of the protocol does not depend on the identities of the nodes.
    - Neutrality: The outcome of the protocol does not favor any particular value or decision over others.
    - Monotonicity: The outcome of the protocol does not change if a node changes its preference or weight in favor of the current outcome.
    - Pareto efficiency: The outcome of the protocol is not dominated by another possible outcome, i.e., there is no other outcome that is preferred by all nodes or by a subset of nodes with higher total weight.
  - A voting protocol is unfair if it violates any of the above conditions .
- Voting protocols can be implemented using different techniques, such as message passing, shared memory, or blockchain    .
  - Message passing is a technique where nodes communicate by sending and receiving messages over a network. Message passing can be synchronous or asynchronous, reliable or unreliable, authenticated or unauthenticated, depending on the assumptions and requirements of the protocol  .
  - Shared memory is a technique where nodes access a common data structure, such as a register or a queue, that can store and retrieve values or decisions. Shared memory can be atomic or non-atomic, single-writer or multi-writer, depending on the assumptions and requirements of the protocol .
  - Blockchain is a technique where nodes maintain a distributed ledger that records the history of transactions or events, such as votes or proposals. Blockchain can be permissioned or permissionless, public or private, depending on the assumptions and requirements of the protocol .



### Dynamic voting protocols

- Dynamic voting protocols are techniques for consistency and recovery control of replicated files in distributed systems  .
- The purpose of a replicated file is to improve the availability of a logical file in the presence of site failures and network partitions  .
- A dynamic voting protocol assigns a number of votes to each replica of a file, and requires a majority of votes to access or update the file    .
- The number of votes assigned to each replica can change dynamically depending on the system state, such as the number of active replicas, the network connectivity, or the access pattern    .
- The advantages of dynamic voting protocols are:
  - They can adapt to changing system conditions and optimize the availability and performance of replicated files    .
  - They can tolerate a higher degree of failures and partitions than static voting protocols, which assign a fixed number of votes to each replica    .
  - They can reduce the communication and synchronization overhead of accessing or updating replicated files, by minimizing the number of replicas involved in each operation    .
- The challenges of dynamic voting protocols are:
  - They need to maintain a consistent view of the vote assignments among the replicas, which may require additional messages or coordination    .
  - They need to ensure that the vote assignments do not violate the majority requirement, which may impose some constraints on the vote reassignment algorithm    .
  - They need to handle concurrent or conflicting operations on the same file, which may require some conflict resolution or rollback mechanism    .



## Unit 8 - Transactions and Concurrency Control

- A **transaction** is a logical unit of work that consists of a sequence of database operations, such as queries, updates, inserts, or deletes.
- A transaction has the following properties:
  - **Atomicity**: A transaction is either executed in its entirety or not at all. If a transaction fails, the database is restored to the state before the transaction started.
  - **Consistency**: A transaction preserves the integrity constraints of the database. If the database is consistent before the transaction, it is also consistent after the transaction.
  - **Isolation**: A transaction is executed as if it is the only one running on the database. The intermediate results of a transaction are not visible to other transactions.
  - **Durability**: The effects of a transaction are permanent and survive any system failures.
- **Concurrency control** is the technique of managing the simultaneous execution of transactions on a shared database, such that the consistency and isolation properties are maintained.
- Concurrency control can be implemented using various methods, such as:
  - **Locking**: A transaction acquires locks on the data items it accesses, and releases them when it is done. A lock can be either shared (for read-only access) or exclusive (for read-write access). A transaction can only access a data item if it has the appropriate lock on it, and no other transaction has a conflicting lock on it.
  - **Timestamping**: A transaction is assigned a unique timestamp when it starts, and the timestamp is used to order the transactions. A transaction can only access a data item if its timestamp is greater than the timestamp of the last transaction that wrote to the data item, and less than the timestamp of the last transaction that read the data item.
  - **Optimistic**: A transaction executes without acquiring any locks, and checks for conflicts at the end. If a conflict is detected, the transaction is aborted and restarted with a new timestamp.
  - **Multiversion**: A transaction accesses a version of the data item that corresponds to its timestamp, and creates a new version of the data item if it modifies it. A transaction can only access a version of the data item if its timestamp is greater than or equal to the timestamp of the version, and less than the timestamp of the next version.



Hello, I am Sydney, your AI assistant. I will help you with your query. Here are some notes on the topic of transactions and concurrency control in distributed systems.

### Transactions
- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the operations in a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction does not interfere with other concurrent transactions.
- Durability means that the effects of a committed transaction are permanent and survive failures.

### Distributed Transactions
- A distributed transaction is a transaction that spans multiple data servers in a distributed database system.
- A distributed transaction consists of a set of subtransactions, each of which is executed by one data server.
- A distributed transaction coordinator is a component that manages the execution and coordination of distributed transactions.
- A distributed transaction has two phases: prepare and commit.
- In the prepare phase, each data server executes its subtransaction and votes to either commit or abort the distributed transaction.
- In the commit phase, the coordinator decides the final outcome of the distributed transaction based on the votes and informs the data servers to either commit or abort their subtransactions.

### Concurrency Control
- Concurrency control is the process of managing the concurrent execution of transactions in a database system.
- Concurrency control ensures that the transactions are serialized, meaning that they are executed as if they were executed one after another in some order.
- Concurrency control prevents conflicts and anomalies that may arise from the interleaved execution of transactions, such as lost updates, dirty reads, unrepeatable reads, and phantom reads.
- Concurrency control can be implemented using various techniques, such as locking, timestamping, validation, and multiversioning.

### Distributed Concurrency Control
- Distributed concurrency control is the concurrency control of a distributed database system, where relevant data is hosted by a group of linked data servers.
- Distributed concurrency control makes sure that all subtransactions of a set of distributed transactions are serialized identically in all data servers involved.
- Distributed concurrency control takes into account not only local dependencies, but also global dependencies involving multiple data servers.
- Distributed concurrency control can be classified into two categories: centralized and decentralized.
- In centralized distributed concurrency control, a single coordinator is responsible for managing the concurrency control of all data servers.
- In decentralized distributed concurrency control, each data server is responsible for managing its own concurrency control and communicating with other data servers as needed.



### Nested transactions for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A transaction is a unit of work that accesses and possibly modifies data in a database or a system.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- A distributed transaction is a transaction that accesses data from multiple servers or systems that are connected by a network.
- A nested transaction is a transaction that contains other transactions as subtransactions.
- Nested transactions can be used to improve the modularity, concurrency, and fault tolerance of distributed systems.
- Nested transactions have the following characteristics:
  - A nested transaction can commit or abort independently of its parent transaction.
  - A nested transaction can see the effects of its parent and sibling transactions, but not of its children transactions.
  - A nested transaction can be partially committed, meaning that its effects are visible to its parent transaction, but not to other transactions.
  - A nested transaction can be flattened, meaning that its effects are merged with its parent transaction and treated as a single transaction.
- Nested transactions can be classified into two types: closed nested transactions and open nested transactions.
  - A closed nested transaction is a nested transaction that follows the strict two-phase locking protocol, meaning that it acquires all the locks before releasing any of them.
  - A closed nested transaction guarantees serializability, but may suffer from high locking overhead and deadlock.
  - A closed nested transaction can be implemented using the two-phase commit protocol, which ensures atomicity and durability of distributed transactions.
  - A open nested transaction is a nested transaction that relaxes the strict two-phase locking protocol, meaning that it can release some locks before acquiring others.
  - A open nested transaction may improve concurrency and performance, but may violate serializability and consistency.
  - A open nested transaction can be implemented using the compensating transactions technique, which uses undo and redo operations to restore consistency in case of failure or abort.



### Locks

- Locks are a mechanism to control the concurrent access of data items by transactions in a distributed system.
- A lock is a variable associated with a data item that determines whether read/write operations can be performed on that data item by a transaction .
- A lock can have different modes, such as shared (S), exclusive (X), or update (U), depending on the type of operation that the transaction intends to perform on the data item .
- A lock compatibility matrix is used to specify which lock modes are compatible or incompatible with each other, i.e., whether two transactions can hold locks of different modes on the same data item at the same time .
- A lock manager is a component of the distributed system that is responsible for granting, releasing, and enforcing locks on data items .
- A lock manager can be centralized, distributed, or hierarchical, depending on the architecture of the distributed system and the granularity of the data items .
- Locks are used to ensure the serializability and isolation of transactions, i.e., to prevent conflicts and anomalies that may arise due to concurrent execution of transactions  .
- Locks can also affect the performance and availability of the distributed system, as they may cause blocking, deadlock, or reduced concurrency  .
- Locking-based concurrency control protocols are algorithms that specify the rules and procedures for acquiring and releasing locks on data items by transactions .
- Locking-based concurrency control protocols can be classified into two-phase locking (2PL), strict two-phase locking (S2PL), rigorous two-phase locking (R2PL), timestamp ordering (TO), and optimistic concurrency control (OCC), among others  .
- Locking-based concurrency control protocols have different properties and trade-offs in terms of serializability, recoverability, deadlock prevention, deadlock detection, deadlock resolution, concurrency level, and overhead  .



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of optimistic concurrency control for the unit 8 - transactions and concurrency control in the subject of distributed system.

### Optimistic Concurrency Control

- Optimistic concurrency control (OCC) is a concurrency control method applied to transactional systems such as relational database management systems and software transactional memory.
- OCC assumes that multiple transactions can frequently complete without interfering with each other, and does not use locking or timestamping techniques to prevent conflicts .
- Instead, a transaction is executed without restrictions until it is committed, and then it is validated to check if any conflicts occurred with other concurrent transactions.
- If a conflict is detected, the transaction is aborted and restarted, otherwise it is committed.
- OCC has three phases: read, validation and write.
  - In the read phase, the transaction reads the data from the database and performs its operations, without acquiring any locks or updating the database.
  - In the validation phase, the transaction checks if any other transaction has modified the data that it has read or written, using some validation rules.
  - In the write phase, if the validation succeeds, the transaction writes its updates to the database, otherwise it aborts and restarts.
- OCC has some advantages and disadvantages over other concurrency control methods  .
  - Advantages:
    - OCC allows a high degree of concurrency, as transactions do not block each other during the read phase .
    - OCC avoids the problems of deadlock and starvation, as transactions do not hold any locks .
    - OCC is suitable for distributed systems, as it reduces the communication and synchronization overhead among the nodes .
  - Disadvantages:
    - OCC may incur a high cost of aborting and restarting transactions, especially if the conflict rate is high or the transactions are long .
    - OCC may cause inconsistency or lost updates, if the validation phase is not done correctly or the write phase is not atomic .
    - OCC may not be applicable for some applications that require strict serializability or real-time constraints .




Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of timestamp ordering for transactions and concurrency control in distributed systems:

### Timestamp ordering

- Timestamp ordering is a class of optimistic concurrency control protocols that assume that transaction conflicts are rare.
- Instead of requiring transactions to acquire locks before they are allowed to read or write to a database object, the DBMS uses timestamps to determine the serializability order of transactions.
- A timestamp is a monotonically increasing number, often based on the system clock, that is assigned to each transaction when it starts.
- The DBMS maintains two timestamps for each database object: the read timestamp (RTS) and the write timestamp (WTS), which record the latest timestamps of transactions that have read or written to the object.
- The DBMS uses the timestamps to enforce two rules: the basic timestamp ordering (BTO) rule and the Thomas' write rule.

#### Basic timestamp ordering (BTO) rule

- The BTO rule states that a transaction can only read or write an object if its timestamp is greater than or equal to the object's RTS and WTS, respectively.
- If a transaction tries to read an object with a higher WTS, it means that a later transaction has already updated the object, and the read is rejected as a violation of serializability.
- If a transaction tries to write an object with a higher RTS or WTS, it means that a later transaction has already read or updated the object, and the write is rejected as a violation of serializability.
- In either case, the transaction is aborted and restarted with a new timestamp.

#### Thomas' write rule

- The Thomas' write rule is a modification of the BTO rule that allows some write operations to be ignored without affecting serializability.
- The rule states that a transaction can write an object if its timestamp is greater than or equal to the object's WTS, regardless of the object's RTS.
- If a transaction tries to write an object with a lower WTS, it means that a later transaction has already updated the object, and the write is ignored as a no-op.
- The rationale behind this rule is that the write operation does not affect the final state of the object, and can be safely skipped without violating serializability.

### Distributed timestamp ordering

- In a distributed system, the timestamps of transactions cannot be based on the local clocks of the sites, since they are not globally unique or synchronized.
- One solution is to use a global logical clock, such as Lamport's clock or vector clock, to generate timestamps that are consistent across the sites.
- Another solution is to use a centralized timestamp server, which assigns timestamps to transactions based on a single physical or logical clock.
- The DBMS then applies the timestamp ordering rules as in the centralized case, but with some additional challenges, such as network delays, message ordering, and site failures.



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is a summary of some methods for concurrency control in distributed systems:

### Comparison of methods for concurrency control

Concurrency control is the process of managing the concurrent access and modification of shared data in a distributed system, such that the consistency and correctness of the data and the system are preserved. Concurrency control techniques can be classified into two main categories: pessimistic and optimistic.

Pessimistic concurrency control techniques prevent conflicts from occurring by acquiring locks on the data items before accessing or modifying them. Locks can be exclusive (for write operations) or shared (for read operations). Pessimistic techniques ensure serializability, which means that the concurrent execution of transactions is equivalent to some serial execution of the same transactions. However, pessimistic techniques can also cause problems such as deadlock, blocking, and reduced concurrency.

Some examples of pessimistic concurrency control techniques are:

- Two-phase locking (2PL): A transaction acquires all the locks it needs before releasing any lock. This ensures that no two conflicting transactions can hold locks on the same data item at the same time. However, 2PL can cause deadlock, which occurs when two or more transactions are waiting for each other to release locks. 2PL can also cause blocking, which occurs when a transaction has to wait for another transaction to release a lock before proceeding.
- Timestamp ordering (TO): A transaction is assigned a unique timestamp when it starts, and the timestamp determines the order of execution of the transactions. A transaction can access or modify a data item only if its timestamp is greater than the timestamp of the last transaction that accessed or modified the same data item. This ensures that the transactions are executed in a chronological order. However, TO can cause aborts, which occur when a transaction is rejected because its timestamp is smaller than the timestamp of another transaction that accessed or modified the same data item. TO can also cause reduced concurrency, which occurs when a transaction has to wait for another transaction to finish before accessing or modifying a data item.

Optimistic concurrency control techniques allow conflicts to occur, but detect and resolve them before committing the transactions. Optimistic techniques do not use locks, but rely on validation or versioning mechanisms to ensure the correctness of the transactions. Optimistic techniques can improve the performance and concurrency of the system, but they can also cause more aborts and overhead.

Some examples of optimistic concurrency control techniques are:

- Validation (or certification) concurrency control: A transaction executes without any locking or checking, but before committing, it validates its read and write sets against the read and write sets of the other concurrent transactions. If there is no conflict, the transaction commits; otherwise, it aborts and restarts. This ensures that the transactions are executed in a conflict-serializable order. However, validation concurrency control can cause more aborts, which occur when a transaction fails the validation test. It can also cause more overhead, which occurs due to the validation process and the maintenance of the read and write sets.
- Multiversion concurrency control (MVCC): A transaction accesses or modifies a version of a data item, rather than the current version. Each version of a data item has a timestamp that indicates when it was created or modified. A transaction can access or modify a version of a data item only if its timestamp is compatible with the timestamp of the version. This ensures that the transactions are executed in a snapshot isolation order, which means that each transaction sees a consistent snapshot of the database as of its start time. However, MVCC can cause more storage space, which occurs due to the creation and maintenance of multiple versions of the data items. It can also cause more complexity, which occurs due to the management and garbage collection of the versions.



## Unit 9 - Distributed Transactions

- A distributed transaction is a type of transaction that involves two or more network hosts, usually providing transactional resources, such as databases, message queues, file systems, etc.   
- A distributed transaction is coordinated by a transaction manager, which is responsible for creating and managing a global transaction that encompasses all the operations against the transactional resources.  
- A distributed transaction requires the following properties to ensure consistency and reliability of the data: atomicity, consistency, isolation, and durability (ACID).  
- Atomicity means that either all the operations in a distributed transaction are executed successfully, or none of them are. If any operation fails, the transaction manager should roll back the changes made by the other operations.  
- Consistency means that the distributed transaction preserves the integrity constraints and business rules of the data. The transaction manager should ensure that the data is in a valid state before and after the transaction.  
- Isolation means that the distributed transaction is executed as if it was the only one running in the system. The transaction manager should prevent any interference or conflicts between concurrent transactions.  
- Durability means that the effects of a distributed transaction are permanent and persistent, even in the case of failures or crashes. The transaction manager should ensure that the data is safely stored and replicated on the transactional resources.  
- A distributed transaction can be implemented using different protocols, such as two-phase commit (2PC), three-phase commit (3PC), or the saga pattern. Each protocol has its own advantages and disadvantages in terms of performance, availability, and fault tolerance.  
- Two-phase commit (2PC) is a protocol that involves two phases: prepare and commit. In the prepare phase, the transaction manager asks each transactional resource to vote on whether they are ready to commit or abort the transaction. In the commit phase, the transaction manager decides to commit or abort the transaction based on the votes, and informs each transactional resource of the decision.  
- Three-phase commit (3PC) is a protocol that involves three phases: prepare, pre-commit, and commit. In the prepare phase, the transaction manager asks each transactional resource to vote on whether they are ready to commit or abort the transaction. In the pre-commit phase, the transaction manager decides to commit or abort the transaction based on the votes, and informs each transactional resource of the decision. In the commit phase, the transaction manager asks each transactional resource to acknowledge the decision.  
- The saga pattern is a protocol that involves a sequence of compensating actions. Each action is a local transaction that can be executed independently and can be undone by another action. The transaction manager coordinates the execution of the actions and triggers the compensating actions in case of failures.



### Flat and nested distributed transactions

- A **distributed transaction** is a transaction that accesses objects managed by multiple servers .
- A distributed transaction must maintain the **ACID** properties of atomicity, consistency, isolation, and durability across all the servers involved .
- A distributed transaction can be structured in two different ways: **flat** or **nested** .

#### Flat transactions

- A **flat transaction** has a single initiating point (**Begin**) and a single end point (**Commit** or **Abort**) .
- A flat transaction is usually simple and short-lived, and does not allow any subtransactions .
- A flat transaction uses a **two-phase commit protocol** (2PC) to coordinate the commit or abort decision among all the servers .
- A flat transaction has the following drawbacks :
  - It may cause long blocking times and high resource consumption on the servers.
  - It may suffer from failures and inconsistencies due to network or server crashes.
  - It may not support complex or long-running activities that require multiple steps or interactions.

#### Nested transactions

- A **nested transaction** is a transaction that can be decomposed into smaller subtransactions  .
- A nested transaction has a single initiating point (**Begin**) and a single end point (**Commit** or **Abort**), but also allows intermediate points (**Partial Commit** or **Partial Abort**) for the subtransactions  .
- A nested transaction is usually complex and long-lived, and supports hierarchical and modular decomposition of a transaction  .
- A nested transaction uses a **saga protocol** or a **compensation protocol** to coordinate the commit or abort decision among all the servers  .
- A nested transaction has the following advantages  :
  - It reduces the blocking times and resource consumption on the servers by committing or aborting subtransactions independently.
  - It tolerates failures and inconsistencies by using compensating actions or undo logs to restore the previous state of the servers.
  - It supports complex or long-running activities that require multiple steps or interactions by allowing partial results and flexible control.



### Atomic Commit Protocols for Distributed Transactions

- A distributed transaction is a transaction that involves multiple servers or nodes in a distributed system.
- An atomic commit protocol is a protocol that ensures that a distributed transaction is either committed or rolled back in its entirety, even if the system fails or some of the nodes fail or crash.
- Ensuring atomic commit is important for maintaining the consistency and integrity of the data in a distributed system.
- There are different types of atomic commit protocols, such as two-phase commit, three-phase commit, parallel commit, and failure-aware commit.
- Two-phase commit (2PC) is the most widely used atomic commit protocol. It consists of two phases: a prepare phase and a commit phase. In the prepare phase, a coordinator node asks all the participant nodes to vote on whether they are ready to commit or abort the transaction. In the commit phase, the coordinator node decides on the final outcome based on the votes and informs all the participant nodes to either commit or abort the transaction accordingly.
- Three-phase commit (3PC) is an extension of 2PC that adds a pre-commit phase between the prepare and commit phases. In the pre-commit phase, the coordinator node informs all the participant nodes of its decision and waits for their acknowledgments. This phase ensures that the coordinator and the participants agree on the same outcome before committing or aborting the transaction.
- Parallel commit is a new atomic commit protocol that reduces the latency of transactions down to only a single round-trip of distributed consensus. It does not use a coordinator node, but instead relies on the participants to agree on a commit timestamp for the transaction. The participants then write their intents to commit the transaction with the agreed timestamp to a distributed key-value store. The transaction is considered committed if and only if all the intents are written before the commit timestamp. Otherwise, the transaction is rolled back.
- Failure-aware commit (FLAC) is another new atomic commit protocol that improves the performance and availability of distributed transactions in the presence of failures. It uses a two-phase transaction processing framework, where the first phase executes the transaction logic and the second phase commits the transaction using a distributed consensus protocol. FLAC optimizes the second phase by using a failure-aware consensus protocol that adapts to different failure scenarios and minimizes the number of messages and rounds required to reach a consensus.



### Concurrency control in distributed transactions

- Concurrency control is the process of ensuring that multiple transactions can access and modify shared data in a consistent and correct manner, without violating the ACID properties of the transactions.
- Distributed transactions are transactions that span multiple data servers that are connected by a network, and may involve data replication, fragmentation, or partitioning .
- Distributed concurrency control provides a mechanism to synchronize distributed transactions in such a way that the ACID properties are not violated by their interleaved execution .
- There are different types of distributed concurrency control algorithms, such as locking-based, timestamp-based, and optimistic algorithms.
- Locking-based algorithms use locks to prevent concurrent transactions from accessing or modifying the same data item. Locks can be shared or exclusive, and can be granted or denied by a central or distributed lock manager .
- Timestamp-based algorithms assign a unique timestamp to each transaction, and use the timestamp order to determine the precedence and validity of transactions. Transactions with older timestamps have higher priority than transactions with newer timestamps .
- Optimistic algorithms assume that conflicts among transactions are rare, and allow transactions to execute without any synchronization until the commit phase. At the commit phase, transactions are validated and aborted if they violate the serializability property .
- Some of the challenges and issues in distributed concurrency control are:
  - Deadlocks: A deadlock occurs when two or more transactions are waiting for each other to release locks on data items that they need to access or modify. Deadlocks can be prevented, detected, or resolved by using different techniques, such as timeouts, deadlock detection algorithms, or deadlock resolution protocols .
  - Distributed commit: A distributed commit is the process of ensuring that either all or none of the data servers involved in a distributed transaction commit the transaction. Distributed commit protocols, such as the two-phase commit (2PC) or the three-phase commit (3PC), are used to coordinate the commit decision among the data servers and handle failures or network partitions  .
  - Data consistency: Data consistency refers to the correctness and integrity of the data in a distributed database system. Data consistency can be affected by factors such as data replication, data fragmentation, data partitioning, network delays, or communication failures. Data consistency can be ensured by using different levels of isolation, such as serializable, snapshot, or read committed, or by using consistency models, such as linearizability, sequential consistency, or eventual consistency .



### Distributed Deadlocks

- A distributed deadlock is a situation where a set of processes in a distributed system are waiting for each other to release resources or messages, and none of them can proceed .
- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems .
- Distributed deadlocks are harder to detect, avoid, and prevent than deadlocks in centralized systems, because there is no single authority that can oversee resource allocation and monitor the state of the system.
- There are three main approaches to handle distributed deadlocks :
  - Prevention: This approach tries to ensure that deadlocks never occur by imposing some constraints on resource allocation, such as ordering the resources, granting requests only if they do not create cycles, or limiting the number of resources that a process can hold at a time. This approach may be costly and inefficient, as it may require a lot of communication and synchronization among the nodes, and it may reduce the concurrency and utilization of the system.
  - Avoidance: This approach tries to avoid deadlocks by making careful decisions on resource allocation, based on the current and future requests of the processes. This approach requires the knowledge of the resource requirements and the dependencies of the processes, which may not be available or accurate in a distributed system. This approach may also be expensive and complex, as it may involve a lot of computation and coordination among the nodes, and it may impose some restrictions on the system behavior.
  - Detection and recovery: This approach tries to detect deadlocks after they occur and then recover from them by aborting or restarting some of the processes involved in the deadlock. This approach does not prevent or avoid deadlocks, but rather tolerates them and deals with them when they happen. This approach may be simpler and more flexible than the previous ones, as it does not require any prior knowledge or assumptions about the processes and the resources, and it does not impose any constraints on the system operation. However, this approach may also be costly and risky, as it may require a lot of overhead to detect deadlocks and a lot of damage to recover from them.

- There are two main techniques to detect distributed deadlocks :
  - Global wait-for graph: This technique involves constructing a global wait-for graph (WFG) from local wait-for graphs at a deadlock detector or a coordinator node. A WFG is a directed graph that represents the dependencies among the processes and the resources in the system. A node in the WFG is either a process or a resource, and an edge from a process to a resource indicates that the process is requesting or holding the resource, while an edge from a resource to a process indicates that the resource is allocated or promised to the process. A deadlock exists in the system if and only if the WFG contains a cycle. This technique requires the nodes to periodically send their local wait-for graphs to the deadlock detector or the coordinator, which then merges them into a global wait-for graph and checks for cycles. This technique may be simple and accurate, but it may also be expensive and slow, as it requires a lot of communication and computation, and it may not reflect the current state of the system due to delays and inconsistencies.
  - Distributed algorithm: This technique involves running a distributed algorithm among the nodes to detect cycles in the WFG without constructing it explicitly. One such algorithm is edge chasing, which works as follows: Each node maintains a set of probes, which are messages that contain the identifiers of the processes and the resources involved in a dependency chain. When a node receives a probe, it checks if it contains its own identifier, which means that a cycle has been detected. If not, it appends its identifier to the probe and forwards it to the next node in the chain, if any. This technique requires the nodes to exchange probes with each other until a cycle is detected or all probes are terminated. This technique may be fast and scalable, but it may also be complex and unreliable, as it may generate a lot of probes and false positives, and it may depend on the network reliability and the node cooperation.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on transaction recovery for the unit 9 - distributed transactions in the subject of distributed system.

### Transaction recovery

- Transaction recovery is the process of restoring the consistency and integrity of a distributed database after a failure or an abort of a transaction .
- A failure can be caused by various reasons, such as network partition, site crash, communication error, disk failure, or concurrency conflict.
- A transaction can be aborted by the user, the system, or the coordinator.
- Transaction recovery involves two main steps: detection and resolution.
- Detection is the process of identifying the transactions that are affected by the failure and their status (committed, aborted, or in doubt).
- Resolution is the process of deciding the final outcome of the transactions and applying the appropriate actions (commit or abort) to ensure atomicity and durability.
- There are different techniques for transaction recovery, such as logging, shadow versions, and two-phase commit  .
- Logging is the technique of recording the changes made by the transactions in a persistent log file, which can be used to undo or redo the operations in case of a failure .
- Shadow versions is the technique of creating a copy of the data before modifying it, which can be used to restore the original state in case of an abort .
- Two-phase commit is the protocol of coordinating the commit or abort decision among the sites involved in a distributed transaction, which consists of a prepare phase and a commit phase .



## Unit 10 - Replication

Replication is the process of copying data from one database server to another, either for backup, high availability, load balancing, or distributed computing purposes. Replication can be classified into different types based on the direction, timing, and granularity of the data transfer.

- **Direction**: Replication can be unidirectional, bidirectional, or multidirectional. Unidirectional replication transfers data from a source server to a target server in one direction only. Bidirectional replication allows data to be transferred in both directions between two servers, and resolves any conflicts that may arise. Multidirectional replication involves more than two servers and allows data to be transferred in any direction among them.
- **Timing**: Replication can be synchronous, asynchronous, or semi-synchronous. Synchronous replication ensures that data is transferred to the target server before the source server commits the transaction. This guarantees data consistency, but adds latency and reduces performance. Asynchronous replication transfers data to the target server after the source server commits the transaction. This improves performance, but may result in data loss or inconsistency in case of a failure. Semi-synchronous replication combines the features of both synchronous and asynchronous replication, and transfers data to the target server before the source server commits the transaction, but does not wait for an acknowledgement from the target server.
- **Granularity**: Replication can be snapshot, transactional, or merge. Snapshot replication copies the entire data set from the source server to the target server at a specified interval. This is suitable for static or slowly changing data, but may consume a lot of network bandwidth and storage space. Transactional replication copies only the changes made to the data from the source server to the target server as they occur. This is suitable for dynamic or frequently changing data, but may require more processing and monitoring. Merge replication allows the source and target servers to update the data independently, and merges the changes periodically. This is suitable for distributed or disconnected environments, but may introduce conflicts and complexity.



### System model and group communication for replication in distributed systems

- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by passing messages .
- Replication is a technique to improve the availability, performance, and fault tolerance of a distributed system by creating and maintaining multiple copies of data or services .
- A system model is a set of assumptions and properties that describe the behavior and characteristics of a distributed system, such as the communication model, the failure model, the timing model, and the security model .
- Group communication is a form of communication between multiple processes in a distributed system that share some common interest or goal, such as achieving consistency, ordering, or reliability   .
- Group communication can be classified into two types: broadcast communication and multicast communication .
  - Broadcast communication is when a source process sends a message to all the processes in the system, regardless of their group membership or interest .
  - Multicast communication is when a source process sends a message to a subset of processes in the system that belong to a specific group .
- Group communication can also be characterized by different levels of reliability, such as best-effort, reliable, or atomic .
  - Best-effort group communication is when a source process sends a message to a group and does not expect any acknowledgment or guarantee of delivery .
  - Reliable group communication is when a source process sends a message to a group and expects that all the processes in the group will eventually receive the message, unless they fail .
  - Atomic group communication is when a source process sends a message to a group and expects that either all or none of the processes in the group will receive the message, and that they will receive it in the same order .
- Group communication can be implemented by various protocols and algorithms, such as IP multicast, gossip protocols, reliable broadcast, reliable multicast, atomic broadcast, and atomic multicast .
- Group communication can be used for replication in distributed systems by enabling the processes to exchange information, coordinate actions, and maintain consistency among the replicas  .
- Replication can be achieved by different strategies, such as primary-backup, active replication, passive replication, or quorum-based replication  .
  - Primary-backup replication is when one process acts as the primary and handles all the requests, while the other processes act as backups and receive updates from the primary .
  - Active replication is when all the processes execute the same requests in the same order and produce the same results .
  - Passive replication is when one process acts as the leader and executes the requests, while the other processes act as followers and receive the results from the leader .
  - Quorum-based replication is when each process maintains a local copy of the data and updates it according to a voting scheme that ensures a minimum number of processes agree on the value .
- Replication can also be classified by different consistency models, such as strong consistency, weak consistency, eventual consistency, or causal consistency  .
  - Strong consistency is when all the processes see the same value of the data at all times .
  - Weak consistency is when the processes may see different values of the data at different times, but the data will eventually converge to a consistent state .
  - Eventual consistency is when the processes may see different values of the data at different times, but the data will eventually converge to a consistent state if no more updates occur .
  - Causal consistency is when the processes see the same value of the data for causally related updates, but may see different values for concurrent updates .



### Fault-Tolerant Services for the Notes of the Unit 10 - Replication in the Subject of Distributed System

- Fault-tolerance is the ability of a system to continue providing correct service despite the occurrence of faults, such as server crashes, network partitions, or malicious attacks.
- Replication is a technique for achieving fault-tolerance by creating and maintaining multiple copies of the same service or data on different servers or locations.
- Replication can improve the availability, performance, and reliability of a distributed system, but also introduces challenges such as consistency, coordination, and recovery.
- There are two main classes of replication techniques: primary-backup replication and active replication.
  - Primary-backup replication: One server acts as the primary and handles all the requests from the clients, while the others act as backups and receive updates from the primary. The primary is responsible for ensuring the consistency and order of the updates. If the primary fails, one of the backups takes over as the new primary.
  - Active replication: All servers are active and execute the same requests from the clients in the same order. The servers use a consensus protocol to agree on the order of the requests. The clients receive responses from all the servers and ignore the faulty ones.
- The correctness criterion for replicated services is linearizability, which means that every operation appears to take effect instantaneously at some point between its invocation and response, and that the operations respect their real-time order.
- The replicated state machine approach is a general method for implementing a fault-tolerant service by replicating servers and coordinating client interactions with server replicas. This approach can use either primary-backup replication or active replication, depending on the type and number of faults to be tolerated.
- An alternative method for fault-tolerance is fused state machines, which combines ideas from replication and coding theory to achieve efficiency and savings in storage and messages during normal operations, at the cost of higher overhead during recovery from faults. This method uses a combination of erasure coding and secret sharing to encode the state of the service and distribute it among the servers.



### Highly Available Services

- A highly available service is a service that can provide continuous and reliable operation despite failures or faults in the system.
- Replication is a technique for achieving high availability by creating and maintaining multiple copies of the same data or service on different nodes in a distributed system .
- Replication can improve availability by allowing the system to tolerate node failures, network partitions, or data corruption, as long as there are enough replicas that can serve the requests.
- Replication can also improve performance by reducing the load on a single node, increasing the throughput of the system, and reducing the latency for the clients.
- Replication can be classified into two types: eager replication and lazy replication .
  - Eager replication ensures that all replicas are updated as soon as a change occurs, using synchronous or atomic multicast protocols. This provides strong consistency and fault tolerance, but at the cost of higher communication overhead and lower availability in the presence of network failures.
  - Lazy replication allows some replicas to be updated later than others, using asynchronous or epidemic protocols. This provides higher availability and lower communication overhead, but at the cost of weaker consistency and possible conflicts or divergence.
- Replication can also be classified into two modes: primary-backup and active replication.
  - Primary-backup replication assigns a single replica as the primary, which is responsible for processing all the requests and updating the backups. This simplifies the implementation and avoids conflicts, but introduces a single point of failure and a performance bottleneck.
  - Active replication executes the same request on all replicas in the same order, using a consensus or a total order protocol. This eliminates the single point of failure and the performance bottleneck, but increases the complexity and the communication overhead.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of transactions with replicated data for the unit 10 - replication in the subject of distributed system.

### Transactions with replicated data

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database. A transaction must satisfy the ACID properties: atomicity, consistency, isolation, and durability.
- Data replication is the process of copying and maintaining data from a source server to other servers in a distributed system. Data replication can improve availability, performance, and fault-tolerance of the system .
- Transactions with replicated data involve coordinating the execution and commit of transactions across multiple servers that hold copies of the same data. This can introduce challenges such as concurrency control, consistency, and recovery.
- There are different approaches to handle transactions with replicated data, such as:
  - Primary copy: One server is designated as the primary copy holder for each data item, and all transactions that access that data item must go through the primary server. The primary server is responsible for propagating the updates to the secondary servers. This approach simplifies concurrency control and recovery, but introduces a single point of failure and a bottleneck for each data item.
  - Voting: Each server that holds a copy of a data item has a vote on whether to commit or abort a transaction that accesses that data item. A transaction can commit only if it receives a majority of votes from the servers involved. This approach can tolerate failures and improve availability, but requires more communication and coordination among servers.
  - Two-phase commit: A transaction that accesses replicated data is divided into two phases: prepare and commit. In the prepare phase, the transaction coordinator asks each server involved to vote on whether to commit or abort the transaction. In the commit phase, the coordinator decides based on the votes and informs each server to either commit or abort the transaction. This approach ensures atomicity and consistency, but introduces blocking and recovery problems if the coordinator or some servers fail .

