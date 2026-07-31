

## Unit 1 - Characterization of Distributed Systems

A distributed system is a collection of independent computers that appear to the users as a single coherent system. Some examples of distributed systems are the Internet, the World Wide Web, cloud computing, peer-to-peer networks, and distributed databases.

Some of the main characteristics of distributed systems are:

- **Concurrency**: Multiple components can execute simultaneously and independently, without interfering with each other.
- **Lack of a global clock**: There is no common notion of time among the components, and the ordering of events is not always clear.
- **Independent failures**: Each component can fail or recover independently, without affecting the rest of the system. The system has to cope with partial failures and inconsistencies.
- **Heterogeneity**: The components can have different hardware, software, network, and data formats, and the system has to provide interoperability and transparency.
- **Scalability**: The system has to be able to handle an increasing number of components, users, and resources, without degrading its performance or functionality.
- **Security**: The system has to protect the confidentiality, integrity, and availability of its data and services, against malicious attacks or unauthorized access.

Some of the main challenges of designing and implementing distributed systems are:

- **Coordination**: The components have to coordinate their actions and share information, despite the lack of a global clock and the possibility of failures and delays.
- **Consistency**: The system has to provide a consistent view of its data and services, despite the concurrency and replication of components and the possibility of failures and inconsistencies.
- **Fault tolerance**: The system has to be able to detect, mask, and recover from failures, and provide reliable and available services, despite the independent failures of components.
- **Transparency**: The system has to hide the complexity and heterogeneity of its components, and provide a simple and uniform interface to the users, despite the distribution and diversity of components.
- **Performance**: The system has to optimize the use of its resources, and provide efficient and responsive services, despite the scalability and variability of components and the possibility of congestion and contention.



### Introduction for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- The main characteristics of distributed systems are:
  - Concurrency: Multiple components can execute simultaneously and interact with each other.
  - No global clock: There is no shared physical clock among the components, and the clocks may drift apart over time.
  - Independent failures: Each component can fail independently without affecting the whole system, and the system can tolerate some degree of failures.
  - Heterogeneity: The components can have different hardware, software, network, and data formats, and the system can accommodate the diversity.
- The main challenges of distributed systems are:
  - Transparency: The system should hide the complexity and heterogeneity of the components from the users and provide a consistent and uniform interface.
  - Scalability: The system should be able to grow in size and performance without degrading the quality of service or requiring major changes in the design and implementation.
  - Reliability: The system should be able to cope with failures and errors of the components and ensure the correctness and consistency of the data and operations.
  - Security: The system should protect the data and resources from unauthorized access and malicious attacks, and ensure the confidentiality, integrity, and availability of the system.
- The main benefits of distributed systems are:
  - Resource sharing: The system can enable the access and utilization of distributed resources, such as files, printers, databases, and services, across the network.
  - Performance: The system can improve the speed and efficiency of the computation and communication by exploiting the parallelism and locality of the components.
  - Fault tolerance: The system can enhance the availability and reliability of the system by replicating and recovering the data and components in case of failures.
  - Flexibility: The system can adapt to the changing requirements and environments by adding, removing, or modifying the components without affecting the whole system.



### Examples of distributed systems

A distributed system is a collection of independent computers that communicate and coordinate their actions by passing messages. The computers in a distributed system may be physically close or geographically dispersed, and they may be connected by a network or a bus. Distributed systems can provide higher performance, reliability, scalability, and availability than centralized systems.

Some examples of distributed systems are:

- **Telecommunication networks**: Telephone networks are an early example of a peer-to-peer network. Cellular and telephone networks are forms and examples of distributed networks. They allow users to communicate with each other over long distances, and they use routing algorithms to find the best path for each call. Telecommunication networks also include the Internet, which is a global network of networks that connects millions of computers and devices .
- **Real-time systems**: Many industries use real-time systems distributed in various areas, locally and globally. Real-time systems have strict timing constraints and must respond to events within a specified deadline. For example, air traffic control systems, industrial control systems, and online gaming systems are real-time systems that use distributed computing to coordinate and synchronize their actions .
- **Distributed database systems**: A distributed database has locations across multiple servers, physical locations, or both. A distributed database can improve the performance, availability, and scalability of data access and processing. For example, online shopping systems, social media platforms, and cloud computing services use distributed databases to store and manage large amounts of data .
- **Distributed file systems**: A distributed file system allows users to access and manipulate files stored on remote servers as if they were local files. A distributed file system can provide faster access, fault tolerance, and load balancing for file operations. For example, Google File System, Hadoop Distributed File System, and Network File System are distributed file systems that support large-scale data-intensive applications.



### Resource sharing for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Resource sharing means that the existing resources in a distributed system can be accessed or remotely accessed across multiple computers in the system.
- Resources can be hardware (such as disks and printers), software (such as files, windows and data objects) or data (such as databases and web pages) .
- Resource sharing can be achieved in different ways, such as:
  - Data migration: the process of transferring data from one location to another in the system.
  - Computation migration: the process of transferring a computation (such as a program or a service) from one location to another in the system.
  - Process migration: the process of transferring a process (such as a thread or a task) from one location to another in the system.
- Resource sharing can have several benefits, such as:
  - Improving performance: by distributing the workload among multiple computers, the system can achieve higher throughput and lower latency.
  - Increasing reliability: by replicating the resources among multiple computers, the system can tolerate failures and maintain availability.
  - Enhancing scalability: by adding or removing computers, the system can adjust to the changing demand and resource availability.
  - Supporting heterogeneity: by abstracting the differences among the computers, the system can provide a uniform interface to the resources.
- Resource sharing can also have some challenges, such as:
  - Managing concurrency: the system must ensure that concurrent access to the shared resources does not result in inconsistency or deadlock.
  - Handling failures: the system must detect and recover from the failures of the computers or the communication links.
  - Providing security: the system must protect the shared resources from unauthorized or malicious access.
  - Dealing with transparency: the system must hide the complexity and diversity of the distributed system from the users and applications.
- Resource sharing can be influenced by the web, which is a global distributed system that provides access to information and services over the internet .
  - The web enables resource sharing by using standard protocols (such as HTTP and HTTPS), formats (such as HTML and XML) and languages (such as JavaScript and PHP).
  - The web challenges resource sharing by introducing issues such as scalability, security, consistency, caching, replication and load balancing.



### The Web Challenges for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- The web is an example of a distributed system that allows resource sharing and communication among different devices across the internet.
- However, the web also poses several challenges for the design and implementation of distributed systems, such as  :
  - Scalability: The ability to handle increasing load and demand without degrading the performance or functionality of the system. Scalability can be achieved by adding more resources, such as servers, storage, or bandwidth, or by improving the efficiency of the system, such as using caching, load balancing, or compression techniques .
  - Heterogeneity: The diversity of the devices, platforms, languages, protocols, and formats that are involved in the web. Heterogeneity requires the system to be adaptable and interoperable, meaning that it can communicate and exchange data with different types of components without losing information or functionality. Heterogeneity can be addressed by using common standards, such as HTTP, HTML, XML, JSON, or REST, or by using middleware, such as web services, SOAP, or CORBA, that provide a uniform interface for communication .
  - Security: The protection of the system and its data from unauthorized access, modification, or damage. Security involves three aspects: privacy, authentication, and availability. Privacy means that the data is not exposed or leaked to unintended parties. Authentication means that the identity and credentials of the users and the components are verified and trusted. Availability means that the system is resilient and reliable, and can recover from failures or attacks. Security can be achieved by using encryption, digital signatures, certificates, firewalls, backups, or replication techniques .
  - Fault tolerance: The ability to cope with errors, failures, or disruptions that may occur in the system or its components. Fault tolerance involves detecting, isolating, and correcting the faults, and ensuring that the system can continue to provide its services despite the faults. Fault tolerance can be achieved by using redundancy, replication, checkpointing, or recovery techniques .
  - Consistency: The property that the system and its data are in a coherent and valid state, and that the users and the components see the same view of the system and its data. Consistency can be violated by concurrent or conflicting operations, such as updates, deletions, or migrations, that may cause inconsistency or divergence among the replicas or copies of the data. Consistency can be ensured by using synchronization, coordination, or consensus protocols, such as locks, transactions, or Paxos, that guarantee that the operations are atomic, isolated, and ordered .



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




### Fundamental Models

Fundamental models are descriptions of properties that are present in all distributed architectures. They help us understand the characteristics and limitations of distributed systems, and provide a basis for designing and evaluating them. There are three main types of fundamental models:

- **Architectural models**: These models define the structure and organization of the components of a distributed system, such as processes, nodes, communication channels, and middleware. They also describe the patterns of interaction and distribution among the components, such as client-server, peer-to-peer, publish-subscribe, and service-oriented architectures.
- **Performance models**: These models quantify the behavior and efficiency of a distributed system, such as the latency, throughput, scalability, and availability of the system. They also identify the factors that affect the performance, such as the network bandwidth, the processing power, the workload, and the concurrency level of the system.
- **Consistency models**: These models specify the degree of agreement or coherence among the components of a distributed system, such as the data, the state, the events, and the operations of the system. They also define the trade-offs and guarantees that the system can offer, such as the consistency, availability, and partition tolerance (CAP) theorem.

Some examples of fundamental models are:

- **Layered model**: This architectural model divides the functionality of a distributed system into a hierarchy of layers, such as the application, presentation, session, transport, network, data link, and physical layers. Each layer provides a set of services to the layer above it, and uses the services of the layer below it. This model simplifies the design, implementation, and maintenance of a distributed system, by separating the concerns and hiding the details of each layer.
- **Queueing model**: This performance model represents the components of a distributed system as queues and servers, where the queues store the requests or messages that arrive from the network, and the servers process them according to some service discipline, such as first-in first-out (FIFO), shortest job first (SJF), or round-robin (RR). This model can be used to analyze the response time, utilization, and throughput of a distributed system, by applying the queueing theory and the Little's law.
- **Eventual consistency model**: This consistency model allows the components of a distributed system to have temporary inconsistencies or divergences, as long as they eventually converge to the same value or state, when no more updates or changes occur. This model relaxes the strict requirements of the sequential consistency or the linearizability models, and enables the system to achieve higher availability and scalability, at the cost of lower consistency and predictability.



### Theoretical Foundation for Distributed System

A distributed system is a collection of independent processes that communicate with each other by exchanging messages over a network. The processes may be located on different machines, have different speeds, and operate under different failure modes. The main challenges of designing and implementing distributed systems are:

- How to coordinate the actions of the processes without a global clock or a shared memory.
- How to handle the uncertainty and unpredictability of message delays and process failures.
- How to achieve consistency, reliability, and fault-tolerance in the presence of concurrency and partial failures.

Some of the theoretical foundations for distributed systems are:

- **Logical clocks**: A logical clock is a mechanism to assign timestamps to events that occur in a distributed system, such that the timestamps reflect the causal order of the events. Logical clocks can be used to implement synchronization, ordering, and agreement protocols in distributed systems. There are different types of logical clocks, such as Lamport's scalar clocks and vector clocks .
- **Message passing systems**: A message passing system is a model of communication in a distributed system, where processes send and receive messages over channels. A message passing system can be characterized by various properties, such as reliability, ordering, and atomicity of message delivery. Message passing systems can be used to implement distributed algorithms, such as leader election, consensus, and broadcast .
- **Distributed algorithms**: A distributed algorithm is a set of rules that specify the behavior of each process in a distributed system, in order to solve a common problem or achieve a common goal. Distributed algorithms can be classified by various criteria, such as the type of problem, the type of network, the type of communication, the type of coordination, and the type of correctness .
- **Distributed complexity**: Distributed complexity is a branch of computational complexity that studies the inherent difficulty of solving problems in a distributed system, in terms of the amount of resources (such as time, space, communication, or randomness) required by the best possible distributed algorithm. Distributed complexity can be used to establish lower bounds, impossibility results, and trade-offs for distributed problems and algorithms .



### Limitation of Distributed system

A distributed system is a system that consists of multiple independent components that communicate and coordinate with each other over a network. Distributed systems have many advantages, such as scalability, fault-tolerance, availability, and performance. However, they also face some limitations that make them challenging to design and implement. Some of the main limitations of distributed systems are:

- **Absence of a global state**: In a distributed system, there is no single point of control or coordination that can maintain a consistent view of the system state. Each component has its own local state, which may be different from the state of other components. This makes it difficult to reason about the behavior and correctness of the system, especially in the presence of concurrency, failures, and network delays. To cope with this limitation, distributed systems need to use synchronization and coordination mechanisms, such as consensus algorithms, distributed transactions, and replication protocols, to ensure that the system state is consistent or eventually consistent across all components.

- **Absence of a global clock**: In a distributed system, there is no common physical clock that can provide a global notion of time. Each component has its own local clock, which may be inaccurate or unsynchronized with other clocks. This makes it hard to order events and measure durations in the system, especially when the network latency is variable or unpredictable. To cope with this limitation, distributed systems need to use logical clocks, such as Lamport timestamps, vector clocks, or causal clocks, to establish a partial or total order of events based on their causal relationships.

- **Network issues**: In a distributed system, the network is an essential medium for communication and coordination among components. However, the network is also a source of uncertainty and unpredictability, as it may experience failures, delays, congestion, or partitioning. These network issues can affect the availability, reliability, and performance of the system, and may cause inconsistencies, conflicts, or data loss. To cope with this limitation, distributed systems need to use fault-tolerant and resilient techniques, such as timeouts, retries, acknowledgments, heartbeats, and quorums, to detect and handle network failures and recover from them .

- **Security and privacy risks**: In a distributed system, the components and the data are distributed across multiple machines, which may belong to different organizations or domains. This exposes the system to various security and privacy risks, such as unauthorized access, tampering, interception, or leakage of data. To cope with this limitation, distributed systems need to use encryption, authentication, authorization, and auditing mechanisms, to protect the confidentiality, integrity, and availability of the system and the data.



### Absence of Global Clock

- A global clock is a system-wide clock that is equally accessible to all processes in a distributed system and provides a common notion of time.
- A global clock is useful for determining the order of events and the state of the system across different processes.
- However, a global clock is hard to realize in distributed systems due to two inherent limitations: lack of shared memory and unpredictable message delays.
- Lack of shared memory means that processes in a distributed system do not have access to a common storage that can store and update the global clock value.
- Unpredictable message delays mean that the communication channel between processes is unreliable and the transmission time of messages is variable and unknown.
- Therefore, the absence of a global clock implies that:
  - Different processes may have different local clocks that are not synchronized and may drift apart over time.
  - It is not always possible to determine the exact order of events that occur on different processes, especially if they are concurrent or causally unrelated.
  - It is not possible for an individual process to obtain an up-to-date and consistent state of the entire system, as the state may change during the transmission of messages.
  - It is difficult to obtain a meaningful state of the system, in which the states of different processes are consistent with each other and reflect a common point in time.



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
  - It supports dynamic load balancing and fault tolerance by allowing the migration and replication of the shared data across the nodes.
- DSM also has some challenges, such as:
  - It requires a high-performance and reliable network to support the frequent data transfers and updates.
  - It introduces the overhead of maintaining the coherence and consistency of the shared data, which may affect the performance and scalability of the system.
  - It may cause false sharing or thrashing, which are situations where multiple processes access or modify the same memory block or page, causing unnecessary data transfers or invalidations.
  - It may suffer from coherence granularity and coherence protocol issues, which are related to the size and the mechanism of the memory units that are shared and synchronized.



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

- Lamport's logical clocks are a way of ordering events in a distributed system based on the causal relationships between them.
- Lamport's logical clocks are based on the idea that if event a causes event b, then a should happen before b in any consistent ordering of events.
- Lamport's logical clocks use numerical software counter values maintained in each process to assign timestamps to events.
- The rules for Lamport's logical clocks are:

  - Each process increments its counter value by one before each event in that process.
  - Each process attaches its counter value to every message it sends.
  - Each process updates its counter value to the maximum of its own value and the received value, before processing the message.

- Lamport's logical clocks ensure that if a -> b, then C(a) < C(b), where C(a) and C(b) are the timestamps of events a and b, respectively.
- Lamport's logical clocks do not ensure that if C(a) < C(b), then a -> b, because events in different processes may be concurrent and have no causal relationship.
- Lamport's logical clocks are also known as scalar clocks or Lamport timestamps.



### Concepts in Message Passing Systems

- Message passing is a technique for invoking behavior (i.e., running a program) on a computer.
- In message-passing systems, processors communicate with one another by sending and receiving messages over a communication channel.
- The pattern of the connection provided by the channel is described by some topology systems.
- The collection of the channels are called a network.
- A distributed system consists of multiple components, possibly across geographical boundaries, that communicate and coordinate their actions through message passing.
- A message-passing system gives a collection of message-based IPC protocols while sheltering programmers from the complexities of sophisticated network protocols and many heterogeneous platforms.
- A message-passing mechanism can be used in a distributed system for the following two forms of inter-process communication:
  - Local communication, where the communicating processes are located on the same node.
  - Distant communication, in which the communication activities are distributed among multiple nodes.
- The formal model for distributed message passing has two timing models:
  - Synchronous, where the sender and receiver processes are synchronized by the message passing, and the message delivery time is bounded and known.
  - Asynchronous, where the sender and receiver processes are independent of each other, and the message delivery time is unbounded and unknown.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on causal order for the Unit 1 - Characterization of Distributed Systems.

### Causal order

- Causal order is a way of ordering events in a distributed system based on their causal relationships, rather than their physical timestamps or their global order.
- Causal order is important for ensuring consistency and correctness of distributed applications that rely on message passing and shared state.
- Causal order is defined by the **happened-before** relation, denoted by `->`, which captures the notion of potential causality between events.
- The happened-before relation has the following properties :
  - If `a` and `b` are events in the same process, and `a` occurred before `b`, then `a -> b`.
  - If `a` is the event of sending a message by one process and `b` is the event of receiving that message by another process, then `a -> b`.
  - If `a -> b` and `b -> c`, then `a -> c` (transitivity).
  - Two events `a` and `b` are **concurrent**, denoted by `a || b`, if neither `a -> b` nor `b -> a`.
- Causal order implies that if a process observes some event `a`, then it must also observe all events that happened before `a`.
- Causal order can be implemented by using **vector clocks**, which are arrays of logical clocks that track the causal dependencies among processes .
- Vector clocks have the following properties :
  - Each process maintains a vector clock `VC[p]` of size `n`, where `n` is the number of processes in the system, and `VC[p][p]` is the logical clock of process `p`.
  - Initially, all entries of `VC[p]` are zero.
  - Whenever a process `p` executes an internal event, it increments `VC[p][p]` by one.
  - Whenever a process `p` sends a message `m`, it piggybacks `VC[p]` on `m` and increments `VC[p][p]` by one.
  - Whenever a process `q` receives a message `m` with a vector clock `VC[m]`, it updates its own vector clock `VC[q]` by taking the element-wise maximum of `VC[q]` and `VC[m]`, and then increments `VC[q][q]` by one.
- Vector clocks can be used to determine the causal order of events by comparing their vector clocks :
  - If `VC[a] < VC[b]`, meaning that `VC[a][i] <= VC[b][i]` for all `i` and `VC[a][j] < VC[b][j]` for some `j`, then `a -> b`.
  - If `VC[a] > VC[b]`, meaning that `VC[a][i] >= VC[b][i]` for all `i` and `VC[a][j] > VC[b][j]` for some `j`, then `b -> a`.
  - If `VC[a]` and `VC[b]` are incomparable, meaning that neither `VC[a] < VC[b]` nor `VC[a] > VC[b]`, then `a || b`.
- Causal order can be used to implement different consistency models for distributed systems, such as **causal consistency** and **total-causal order**  .
  - Causal consistency is a consistency model that guarantees that all processes see causally related updates in the same order, but concurrent updates may be seen in different orders.
  - Total-causal order is a consistency model that guarantees that all processes see all updates in the same order, which is consistent with the causal order.



### Total Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent entities that communicate by message passing and coordinate their actions to achieve a common goal.
- Events are the occurrences of actions or state changes in a distributed system, such as sending or receiving a message, executing a computation, or accessing a resource.
- A partial order is a binary relation that is reflexive, antisymmetric, and transitive, meaning that for any events x, y, and z in a distributed system:
  - x is related to x (reflexivity)
  - if x is related to y and y is related to x, then x and y are the same event (antisymmetry)
  - if x is related to y and y is related to z, then x is related to z (transitivity)
- A total order is a partial order that is also complete, meaning that for any two distinct events x and y in a distributed system, either x is related to y or y is related to x (completeness).
- A distributed system is said to have partial order if we can have a partial order relationship among the events in the system, such as the causal order or the logical order.
- A distributed system is said to have total order if we can have a total order relationship among the events in the system, such as the physical order or the global order.
- The causal order is a partial order that captures the potential causality between events in a distributed system, meaning that if an event x could have influenced or caused another event y, then x is related to y in the causal order. For example, if a process p sends a message m to another process q, and q receives m and then sends another message n to a process r, then the send event of m is causally related to the receive event of n, and the causal order is respected if m is delivered to q before n is delivered to r.
- The logical order is a partial order that captures the temporal order of events in a distributed system, meaning that if an event x happens before another event y in the local clock of a process, then x is related to y in the logical order. For example, if a process p executes a computation c and then sends a message m to another process q, then the execution event of c is logically related to the send event of m, and the logical order is respected if c is completed before m is sent.
- The physical order is a total order that captures the real-time order of events in a distributed system, meaning that if an event x happens before another event y in the global clock of the system, then x is related to y in the physical order. For example, if a process p sends a message m to another process q, and q receives m and then sends another message n to a process r, then the send event of m is physically related to the receive event of n, and the physical order is respected if m is sent before n is received in the global clock.
- The global order is a total order that captures the arbitrary order of events in a distributed system, meaning that if an event x is assigned a lower identifier than another event y by some mechanism, then x is related to y in the global order. For example, if a process p sends a message m to another process q, and q receives m and then sends another message n to a process r, then the send event of m is globally related to the receive event of n, and the global order is respected if m is assigned a lower identifier than n by some mechanism, such as a Lamport timestamp or a process ID.
- A total order is useful for distributed systems because it can help ensure consistency, agreement, and coordination among the entities in the system. For example, a total order can help implement atomic broadcast, which is a communication primitive that guarantees that all processes in the system receive the same messages in the same order. Atomic broadcast can be used to implement distributed consensus, which is a problem of reaching a common decision among the processes in the system. Distributed consensus can be used to implement distributed transactions, which are operations that involve multiple processes and resources in the system and need to be executed atomically, consistently, and reliably.



### Total Causal Order

- Total causal order is a property of message delivery in distributed systems that ensures that all messages are delivered in a consistent and logical order across all processes .
- Total causal order implies that if a message m1 causally precedes a message m2, then m1 is delivered before m2 by all processes. Moreover, if m1 and m2 are concurrent, meaning that they are not causally related, then they are delivered in the same order by all processes  .
- Total causal order is the strictest form of ordering in distributed systems, as it establishes a single linearization of all events that occur in the system, even those that are concurrent. This means that the execution of the system is considered as synchronous, and there is no ambiguity or inconsistency in the global state of the system .
- Total causal order can be implemented by using a logical clock, such as a vector clock, to assign timestamps to each message that reflect the causal dependencies among them. Then, a message delivery protocol, such as a sequencer or a consensus algorithm, can be used to ensure that all processes agree on the order of messages based on their timestamps .
- Total causal order is useful for applications that require strong consistency and coordination among distributed processes, such as distributed databases, replicated state machines, or distributed transactions . However, it also introduces a high overhead and latency in message delivery, as it requires global synchronization and agreement among all processes .



### Techniques for Message Ordering in Distributed Systems

Message ordering is the problem of ensuring that messages sent by different processes in a distributed system are received and processed in a consistent and predictable way. Message ordering is important for achieving correctness, consistency, and coordination in distributed systems.

There are different types of message ordering techniques, depending on the desired properties and guarantees of the communication. Some of the common techniques are:

- **Unordered**: This is the simplest and most basic technique, where messages are delivered in any order, without any guarantee of preserving the order of sending or causality. This technique is suitable for applications that do not depend on the order of messages, such as broadcasting or gossiping.
- **FIFO**: This technique ensures that messages sent by the same process are delivered in the order of sending, but messages from different processes may be delivered in any order. This technique is useful for applications that need to preserve the order of events within a process, such as logging or auditing.
- **Causal**: This technique ensures that messages that are causally related are delivered in the order of causality, but messages that are not causally related may be delivered in any order. Causality is defined by the happens-before relation, which captures the logical order of events in a distributed system. This technique is useful for applications that need to preserve the order of events that affect each other, such as data replication or distributed transactions.
- **Total**: This technique ensures that messages are delivered in the same order to all processes, regardless of the order of sending or causality. This technique is useful for applications that need to achieve global agreement or synchronization, such as consensus or leader election.
- **Synchronous**: This technique ensures that messages are delivered in the same order to all processes, and that order is also consistent with the order of sending and causality. This technique is useful for applications that need to achieve strong consistency and atomicity, such as distributed databases or atomic broadcast.

Each of these techniques has different trade-offs in terms of complexity, overhead, and performance. Some of the protocols that implement these techniques are:

- **Unordered**: No protocol is needed, as messages are simply sent and received without any ordering mechanism.
- **FIFO**: A simple protocol that uses sequence numbers to order messages from the same sender. Each sender maintains a counter that is incremented for each message sent, and each receiver maintains a buffer that stores the messages from each sender in order of sequence numbers. A message is delivered only when it has the next expected sequence number from its sender.
- **Causal**: A protocol that uses vector clocks to order messages according to causality. Each process maintains a vector clock that records the logical time of each process in the system. A message is sent with the vector clock of the sender, and a message is delivered only when its vector clock is less than or equal to the vector clock of the receiver. This ensures that a message is delivered only after all the messages that causally precede it have been delivered.
- **Total**: A protocol that uses a sequencer or a coordinator to order messages globally. Each sender sends a message to the sequencer, which assigns a global sequence number to the message and broadcasts it to all the receivers. Each receiver maintains a buffer that stores the messages in order of global sequence numbers. A message is delivered only when it has the next expected global sequence number.
- **Synchronous**: A protocol that combines the FIFO and causal protocols to order messages synchronously. Each sender sends a message with its sequence number and vector clock, and each receiver maintains a buffer that stores the messages in order of sequence numbers and vector clocks. A message is delivered only when it has the next expected sequence number from its sender, and its vector clock is less than or equal to the vector clock of the receiver. This ensures that a message is delivered only after all the messages that causally precede it and are from the same sender have been delivered.



### Causal ordering of messages

- Causal ordering of messages is a partial ordering of messages in a distributed computing environment .
- It places a restriction on communication between processes by requiring that if the transmission of message mi to process pk necessarily preceded the transmission of message mj to the same process, then the delivery of these messages to that process must be ordered such that mi is delivered before mj .
- Causal ordering of messages is one of the four semantics of multicast communication, namely unordered, totally ordered, causal, and sync-ordered communication.
- Multicast communication methods vary according to the message’s reliability guarantee and ordering guarantee.
- Causal ordering of messages is based on the notion of potential causality, which captures the idea that if an event A can possibly have caused another event B, then A must happen before B.
- Potential causality is defined by two rules:
  - If A and B are events in the same process, and A comes before B, then A -> B (A potentially causes B).
  - If A is the event of sending a message by one process and B is the event of receiving that message by another process, then A -> B.
- Potential causality is transitive, meaning that if A -> B and B -> C, then A -> C.
- Causal ordering of messages ensures that the messages are delivered in a way that is consistent with the potential causality relation.
- Causal ordering of messages can be implemented by various algorithms, such as vector clocks, logical clocks, or piggybacking  .
- Causal ordering of messages has some advantages and disadvantages:
  - Advantages:
    - It preserves the logical dependencies between messages and events.
    - It avoids the need for global synchronization or agreement among processes.
    - It allows for concurrent and independent execution of processes.
  - Disadvantages:
    - It may delay the delivery of some messages that are not causally related to others.
    - It may incur some overhead in terms of message size or computation.
    - It may not be sufficient for some applications that require stronger ordering guarantees.



### Global State

- The global state of a distributed system is the **union** of the states of the individual processes and the channels .
- A process that wishes to construct a global state must infer the remote components of that state through message exchanges.
- A global state is **consistent** if it reflects a possible execution of the system, i.e., no causal violations occur .
- A global state is **correct** if it is computed along a consistent cut, i.e., a set of local states that are mutually consistent.
- A global state is **useful** for applications such as debugging, checkpointing, termination detection, garbage collection, etc .
- A global state can be recorded by using **distributed snapshot algorithms**, which are protocols that allow processes to cooperate in capturing a consistent global state without blocking or synchronizing.



### Termination Detection

Termination detection is a fundamental problem in distributed systems, where a set of processes cooperate to perform a computation. The goal is to determine when all the processes have finished their work and there are no more messages in transit between them.

Termination detection is non-trivial because:

- No process has complete knowledge of the global state of the system.
- Processes may become idle and active at different times, depending on the arrival of messages.
- There is no global clock or synchronization among processes.

One of the algorithms for termination detection is Huang's algorithm, proposed by Shing-Tsaan Huang in 1989. The main idea of Huang's algorithm is to use a control message, called a token, to collect information about the local states of the processes and the messages in transit. The token circulates among the processes in a logical ring, and when it returns to the initiator process, it contains the global state of the system. The initiator can then decide whether the computation has terminated or not.

The algorithm works as follows:

- Each process maintains a local counter, called diff, that records the difference between the number of messages sent and received by the process. The diff value is initialized to zero and updated whenever a message is sent or received.
- Each process also maintains a boolean variable, called idle, that indicates whether the process is idle or active. The idle value is initialized to false and updated whenever the process becomes idle or active.
- The initiator process creates a token, which is a data structure that contains two fields: count and idle. The count field records the sum of the diff values of all the processes that have seen the token. The idle field records the logical AND of the idle values of all the processes that have seen the token. The token is initialized with count = 0 and idle = false.
- The initiator process sends the token to its successor in the logical ring. The successor is the next process in the ring that is not crashed or disconnected.
- When a process receives the token, it performs the following steps:
  - It adds its diff value to the token's count field and resets its diff value to zero.
  - It updates the token's idle field with the logical AND of its idle value and the token's idle field.
  - It sends the token to its successor in the logical ring.
- When the initiator process receives the token back, it performs the following steps:
  - It adds its diff value to the token's count field and resets its diff value to zero.
  - It updates the token's idle field with the logical AND of its idle value and the token's idle field.
  - It checks the token's count and idle fields. If count = 0 and idle = true, then the computation has terminated. Otherwise, the computation has not terminated and the initiator sends the token to its successor again.

The algorithm terminates when the initiator detects that the computation has terminated. The algorithm is correct because:

- The token's count field represents the total number of messages in transit in the system. When count = 0, there are no more messages in transit.
- The token's idle field represents the global idle state of the system. When idle = true, all the processes are idle.
- The token circulates in a logical ring, so it visits all the processes in the system. The token collects the local states of the processes and aggregates them into the global state.

The algorithm is efficient because:

- The token size is constant and independent of the number of processes in the system.
- The token circulates in a logical ring, so it avoids unnecessary communication overhead and congestion.
- The token is only created and sent by the initiator process, so it avoids duplication and contention.



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
  - Synchronization delay: The time elapsed between the instant a process requests to enter the critical section and the instant it is allowed to do so.
  - System throughput: The number of times the critical section is executed per unit time.
  - Fault tolerance: The ability of the algorithm to handle failures of processes or communication links.



### Classification of distributed mutual exclusion

Distributed mutual exclusion is a problem of ensuring that only one process can access a shared resource or data at a time in a distributed system. It is a fundamental requirement for achieving consistency, reliability, and fault-tolerance in distributed computing.

There are three basic approaches for implementing distributed mutual exclusion algorithms:

- **Token-based approach**: A unique token is shared among the processes. A process can enter its critical section only if it possesses the token. Mutual exclusion is ensured because the token is unique. Examples of token-based algorithms are Suzuki-Kasami's algorithm, Raymond's algorithm, and Maekawa's algorithm  .
- **Non-token-based approach**: Processes communicate with each other to coordinate their access to the critical section. A process can enter its critical section only if it receives permission from all or some of the other processes. Mutual exclusion is ensured by the agreement of the processes. Examples of non-token-based algorithms are Lamport's algorithm, Ricart-Agrawala's algorithm, and Singhal's algorithm   .
- **Quorum-based approach**: Processes communicate with a subset of processes, called a quorum, to obtain permission to enter the critical section. A process can enter its critical section only if it receives permission from a majority of the quorum members. Mutual exclusion is ensured by the intersection of the quorums. Examples of quorum-based algorithms are Maekawa's algorithm, Naimi-Trehel's algorithm, and Agrawal-El Abbadi's algorithm  .

The classification of distributed mutual exclusion algorithms can be summarized in the following diagram:

```
+----------------------------------------+
| Distributed mutual exclusion algorithms |
+----------------------------------------+
|                                        |
+----------------+ +---------------------+ +----------------+
| Token-based    | | Non-token-based    | | Quorum-based   |
+----------------+ +---------------------+ +----------------+
|                | |                     | |                |
| - Suzuki-Kasami| | - Lamport           | | - Maekawa      |
| - Raymond      | | - Ricart-Agrawala  | | - Naimi-Trehel |
| - Maekawa      | | - Singhal          | | - Agrawal-El   |
|                | |                     | |   Abbadi       |
+----------------+ +---------------------+ +----------------+
```



### Requirement of mutual exclusion theorem for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM

- Mutual exclusion is a concurrency control property which is introduced to prevent race conditions.
- It is the requirement that a process can not enter its critical section while another concurrent process is currently present or executing in its critical section i.e only one process is allowed to execute the critical section at any given time .
- A critical section is a segment of code that accesses a shared resource or data.
- Mutual exclusion in a distributed system states that only one process is allowed to execute the critical section at any given time .
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion .
- Message passing is the sole means for implementing distributed mutual exclusion .
- There are three basic approaches for implementing distributed mutual exclusion:
  - Token-based algorithms: A process can enter the critical section only if it possesses a unique token. The token is passed among the processes in a predefined order or by request.
  - Permission-based algorithms: A process can enter the critical section only if it obtains permission from all or a subset of other processes in the system. The process sends request messages and waits for reply messages before entering the critical section.
  - Quorum-based algorithms: A process can enter the critical section only if it obtains permission from a majority or a quorum of processes in the system. The process sends request messages and waits for reply messages from a quorum before entering the critical section.
- The mutual exclusion theorem states that any algorithm that solves the mutual exclusion problem in a distributed system must satisfy the following four properties:
  - Safety: At most one process can execute in the critical section at any time.
  - Liveness: If a process requests to enter the critical section, it will eventually be granted permission.
  - Fairness: No process is indefinitely postponed or starved from entering the critical section.
  - Fault-tolerance: The algorithm can tolerate a bounded number of process or message failures and still guarantee mutual exclusion.



### Token based and non token based algorithms for distributed mutual exclusion

Distributed mutual exclusion (DME) is the problem of ensuring that only one process at a time can access a shared resource in a distributed system. There are two main types of algorithms for DME: token based and non token based.

- Token based algorithms
  - In token based algorithms, a unique token is shared among all the processes in the system. The token represents the permission to enter the critical section. Only the process that holds the token can access the shared resource.
  - A process that wants to enter the critical section must request the token from the current holder. The token is passed from one process to another in a predefined order or based on some criteria. The process that receives the token can enter the critical section and release the token when it is done.
  - Token based algorithms are simple and efficient, but they have some drawbacks. For example, if the token is lost or corrupted, the system may deadlock. Also, the token may cause unnecessary delays if it is far away from the requesting process.
  - Examples of token based algorithms are:
    - Suzuki-Kasami algorithm: This is a modification of Ricart-Agrawala algorithm, a permission based algorithm that uses REQUEST and REPLY messages to ensure mutual exclusion. In Suzuki-Kasami algorithm, the token contains a vector of sequence numbers that indicates the order of requests. The token is sent to the process with the highest sequence number in the vector. This algorithm reduces the number of messages and improves the response time.
    - Raymond's algorithm: This is a tree-based algorithm that organizes the processes into a logical tree. The token is initially held by the root of the tree. A process that wants to enter the critical section sends a REQUEST message to its parent in the tree. The parent forwards the request to the root if it does not have the token. The token is passed along the path from the root to the requesting process. The process that receives the token can enter the critical section and release the token to its parent when it is done. This algorithm minimizes the number of messages and the path length of the token.

- Non token based algorithms
  - In non token based algorithms, there is no token in the system. Instead, the processes use timestamps to order the requests for the critical section and to resolve conflicts between simultaneous requests. A process that wants to enter the critical section must communicate with a set of other processes to determine who should execute the critical section next.
  - Non token based algorithms are more robust and fault-tolerant, but they have some drawbacks. For example, they require more messages and synchronization among the processes. Also, they may cause starvation if some processes are always delayed or ignored.
  - Examples of non token based algorithms are:
    - Lamport's algorithm: This is a basic algorithm that uses logical clocks to assign timestamps to the requests. A process that wants to enter the critical section sends a REQUEST message with its timestamp to all other processes. It waits for a REPLY message from all other processes. The process with the smallest timestamp has the highest priority to enter the critical section. If two processes have the same timestamp, the process with the smaller identifier has the higher priority. This algorithm ensures mutual exclusion and fairness, but it requires a lot of messages and acknowledgments.
    - Ricart-Agrawala algorithm: This is an optimization of Lamport's algorithm that reduces the number of messages. A process that wants to enter the critical section sends a REQUEST message with its timestamp to all other processes. It waits for a REPLY message from all other processes that have a lower priority than itself. A process that receives a REQUEST message can either reply immediately or defer the reply until it leaves the critical section. This algorithm ensures mutual exclusion and fairness, but it still requires a lot of messages and synchronization.



### Performance Metrics for Distributed Mutual Exclusion Algorithms

Distributed mutual exclusion algorithms are algorithms that ensure that only one process at a time can access a shared resource in a distributed system. The performance of these algorithms can be evaluated by using the following metrics :

- **Message complexity**: It is the number of messages that are required per critical section (CS) execution by a process. It indicates the communication overhead of the algorithm. A lower message complexity is desirable.
- **Synchronization delay**: It is the time elapsed between the moment when a process leaves the CS and the moment when the next process enters the CS. It indicates the degree of concurrency of the algorithm. A lower synchronization delay is desirable.
- **Response time**: It is the time elapsed between the moment when a process requests to enter the CS and the moment when it actually enters the CS. It indicates the waiting time of the process. A lower response time is desirable.
- **Throughput**: It is the number of CS executions per unit time in the system. It indicates the efficiency of the algorithm. A higher throughput is desirable.

The performance of different distributed mutual exclusion algorithms may vary depending on the system parameters, such as the number of processes, the network topology, the network delay, the CS execution time, and the inter-request time. Therefore, it is important to compare the algorithms under different scenarios and use appropriate statistical methods to analyze the results .

Some examples of distributed mutual exclusion algorithms are:

- **Central server algorithm**: In this algorithm, one process acts as the coordinator and grants access to the CS to other processes based on a FIFO queue. The message complexity is 3 messages per CS execution, the synchronization delay is one message transmission time, and the response time depends on the position of the requesting process in the queue.
- **Ricart-Agrawala algorithm**: In this algorithm, each process broadcasts its request to enter the CS to all other processes and waits for their replies. The process with the lowest timestamp has the highest priority to enter the CS. The message complexity is 2N messages per CS execution, where N is the number of processes, the synchronization delay is zero, and the response time depends on the network delay and the number of competing processes.
- **Lamport's algorithm**: In this algorithm, each process maintains a logical clock and a request queue. When a process wants to enter the CS, it sends its request with its clock value to all other processes and puts it in its own queue. The process with the lowest clock value has the highest priority to enter the CS. The message complexity is 3N-1 messages per CS execution, the synchronization delay is one message transmission time, and the response time depends on the network delay and the number of competing processes.



## Unit 3 - Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set.
- A distributed deadlock is a deadlock that involves processes and resources located on different nodes of a distributed system.
- Deadlock detection in distributed systems is the approach of identifying and resolving existing deadlocks in the system.
- Deadlock detection in distributed systems entails addressing two basic issues:
  - Detection of existing deadlocks: This requires examining the status of process-resource interactions for the presence of cyclic wait.
  - Resolution of detected deadlocks: This requires aborting one or more deadlocked processes to break the cycle and release the resources.
- There are three main approaches to detect deadlocks in distributed systems:
  - Centralized approach: This involves designating a single node as the deadlock detector, which collects information from all other nodes and constructs a global wait-for graph (WFG) to detect cycles.
  - Hierarchical approach: This involves organizing the nodes into a hierarchy of clusters, where each cluster has a local deadlock detector and a coordinator. The coordinators communicate with each other and construct a global WFG to detect cycles.
  - Distributed approach: This involves using a distributed algorithm, such as edge chasing or probe-based, to detect cycles in the WFG without constructing it explicitly.



### System Model for Distributed Deadlock Detection

- A distributed system consists of a set of nodes that communicate by message passing.
- Each node has a set of resources that can be requested by processes running on the same or different nodes.
- A process can request, hold, and release resources according to some protocol.
- A process is blocked if it is waiting for a resource that is held by another process.
- A deadlock is a situation where a set of processes are blocked and none of them can proceed.
- A wait-for graph (WFG) is a directed graph that represents the blocking relationships among processes. A node in the WFG is a process and an edge from P to Q means that P is waiting for a resource held by Q.
- A cycle in the WFG indicates a deadlock.
- Distributed deadlock detection is the problem of finding cycles in the WFG of a distributed system.
- There are three main approaches to distributed deadlock detection: centralized, hierarchical, and distributed.
- In the centralized approach, there is a designated node (called the coordinator) that collects the local WFGs from all the nodes and constructs the global WFG. The coordinator then runs a cycle detection algorithm on the global WFG and informs the nodes about the deadlocks.
- In the hierarchical approach, the nodes are organized into clusters and each cluster has a leader that acts as a coordinator for the cluster. The leaders communicate with each other to construct a global WFG and detect cycles.
- In the distributed approach, there is no coordinator and each node participates in the deadlock detection process. The nodes exchange messages (called probes) that contain information about the WFG. A cycle is detected when a probe returns to its originator.



### Resource vs Communication Deadlocks

- A deadlock is a condition where a process cannot proceed because it needs to obtain a resource held by another process, and it itself is holding a resource that the other process needs .
- There are two types of deadlocks in distributed systems: resource deadlocks and communication deadlocks.
- Resource deadlocks occur when processes access resources, such as data objects in database systems and buffers in store and forward communication networks. A process acquires a resource before accessing it and releasing it after using it.
- Communication deadlocks occur when processes exchange messages, such as in remote procedure calls and distributed transactions. A process sends a message to another process and waits for a reply before continuing.
- The main difference between resource and communication deadlocks is that in resource deadlocks, processes hold resources while waiting for other resources, whereas in communication deadlocks, processes do not hold any resources while waiting for messages .
- Another difference is that resource deadlocks can be detected by analyzing the resource allocation graph, whereas communication deadlocks require analyzing the wait-for graph .
- A resource allocation graph is a directed graph where nodes represent processes and resources, and edges represent requests and allocations . A cycle in the graph indicates a resource deadlock .
- A wait-for graph is a directed graph where nodes represent processes, and edges represent waiting relationships . A cycle in the graph indicates a communication deadlock .
- An example of a resource deadlock is shown below:

Resource deadlock

- An example of a communication deadlock is shown below:

Communication deadlock



### Deadlock Prevention for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process. In a distributed system, deadlocks are more difficult to detect and resolve than in a centralized system, because there is no global information or control.

Deadlock prevention is a technique that aims to ensure that at least one of the four necessary conditions for deadlock (mutual exclusion, hold and wait, no preemption, and circular wait) does not hold. There are two main methods of deadlock prevention in a distributed system:

- Ordered request: This method assigns a unique level to each resource type and requires that a process requests resources in increasing order of levels. This prevents circular wait, as there is a global ordering of resources.
- Collective request: This method requires that a process requests all the resources it needs at once, before starting its execution. This prevents hold and wait, as a process does not hold any resources while waiting for others.

Both methods have some drawbacks, such as reduced concurrency, increased overhead, and wasted resources. Therefore, deadlock prevention is not always feasible or desirable in a distributed system. Alternatively, deadlock detection and recovery can be used to deal with deadlocks after they occur.



### Avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- Deadlock avoidance is a technique that prevents the occurrence of deadlocks by ensuring that the system is always in a safe state.
- A safe state is a state where there exists a safe sequence of processes that can finish their execution without causing a deadlock.
- In a distributed system, deadlock avoidance is impractical due to several problems, such as:
  - The lack of global information about the resource allocation and requests of all processes.
  - The dynamic and unpredictable nature of the system, where processes and resources may join or leave at any time.
  - The high communication and synchronization overhead involved in maintaining a global safe state.
- Therefore, deadlock detection is preferred over deadlock avoidance in distributed systems, as it allows more concurrency and flexibility in resource allocation.
- Deadlock detection is a technique that identifies the existence of a deadlock after it has occurred, and then takes some recovery actions to resolve it.
- Deadlock detection in distributed systems can be classified into four classes, based on the type of information and algorithm used:
  - Path-pushing: This class of algorithms propagates the information about the wait-for relations along the paths of the wait-for graph, until a cycle is detected or the information reaches a designated coordinator.
  - Edge-chasing: This class of algorithms sends probe messages along the edges of the wait-for graph, until a cycle is detected or the probe returns to the sender.
  - Diffusion computation: This class of algorithms initiates a distributed computation at each node of the wait-for graph, where each node exchanges information with its neighbors and decides whether it is part of a deadlock or not.
  - Global state detection: This class of algorithms collects the global state of the system using techniques such as snapshot algorithms or vector clocks, and then analyzes the global state for the presence of a deadlock.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of distributed deadlock detection and resolution.

### Distributed Deadlock Detection and Resolution

- A deadlock is a situation where a set of processes are blocked, waiting for resources held by other processes in the set.
- A distributed deadlock is a deadlock that involves processes and resources located on different nodes of a distributed system.
- A distributed deadlock can be detected by constructing a wait-for graph (WFG) that represents the dependencies among processes and resources in the system.
- A WFG is a directed graph where nodes are processes or resources, and edges are requests or assignments. An edge from process P to resource R means P is requesting R. An edge from resource R to process P means R is assigned to P.
- A cycle in the WFG indicates a deadlock. A knot is a strongly connected component of the WFG that contains at least one cycle.
- There are three main approaches to construct and search the WFG for cycles or knots: centralized, distributed, and hierarchical.
- In the centralized approach, a single node (coordinator) collects information from all other nodes and builds a global WFG. The coordinator periodically searches the WFG for cycles and notifies the involved nodes if a deadlock is detected.
- In the distributed approach, each node maintains a local WFG that reflects its own state and the state of its neighbors. Each node periodically initiates a probe message that traverses the WFG and detects cycles. A probe message contains a list of visited nodes and a timestamp. If a node receives a probe message that contains its own identifier, it means a cycle is detected.
- In the hierarchical approach, the nodes are organized into a tree structure, where each node has a parent and zero or more children. Each node maintains a local WFG that reflects its own state and the state of its children. Each node periodically sends its local WFG to its parent, who merges it with its own WFG and sends it to its parent, and so on. The root node has the global WFG and searches it for cycles. If a deadlock is detected, the root node notifies the involved nodes through the tree structure.
- The resolution of a distributed deadlock involves breaking the existing wait-for dependencies in the system WFG. It includes rolling back some or all of the deadlocked processes and releasing their resources to the blocked processes in the deadlock so that they may resume execution.
- There are two main strategies for deadlock resolution: prevention and avoidance.
- Prevention is a proactive strategy that ensures that a deadlock can never occur in the system. It involves imposing some constraints on the processes and resources, such as ordering, preemption, or timeout.
- Avoidance is a reactive strategy that ensures that a deadlock can be avoided if it is possible. It involves making dynamic decisions based on the current state of the system, such as granting or denying requests, or aborting or delaying processes.



### Centralized Deadlock Detection

- This is a technique used in distributed systems to handle deadlock detection.
- According to this approach, the system maintains one global wait-for graph in a single chosen site, which is named as deadlock-detection coordinator.
- The coordinator collects information about the local wait-for graphs of all the sites and constructs the global wait-for graph.
- The coordinator periodically runs a deadlock detection algorithm on the global wait-for graph to find cycles.
- If a cycle is found, the coordinator selects one or more processes to abort and sends a message to the corresponding sites.
- The advantages of this approach are simplicity and low communication overhead.
- The disadvantages of this approach are the single point of failure and the bottleneck of the coordinator.

: Centralized deadlock detection approach in distributed database, https://www.exploredatabase.com/2014/06/centralized-deadlock-detection-approach-in-distributed-database.html
: Deadlock Detection in Distributed Systems - javatpoint, https://www.javatpoint.com/deadlock-detection-in-distributed-systems
: Distributed Transactions - Rutgers University, https://people.cs.rutgers.edu/~pxk/417/notes/deadlock.html
: Deadlock detection in Distributed systems - GeeksforGeeks, https://www.geeksforgeeks.org/deadlock-detection-in-distributed-systems/
: Deadlock Detection in Distributed Systems - GeeksforGeeks, https://www.geeksforgeeks.org/deadlock-detection-in-distributed-systems-2/



### Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set, and none of the processes can proceed or release the resources.
- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems.
- Deadlock detection in distributed systems entails addressing two basic issues: detection of existing deadlocks and resolution of detected deadlocks.
- Deadlock detection requires examination of the status of process-resource interactions for presence of cyclic wait.
- There are three main approaches to detect deadlocks in distributed systems:
  - Centralized approach: A single site is designated as the deadlock detector and collects the local wait-for graphs from all the sites to construct a global wait-for graph. The deadlock detector periodically runs an algorithm to check for cycles in the global wait-for graph and initiates the resolution process if a deadlock is found.
  - Hierarchical approach: The sites are organized into a hierarchy of clusters, and each cluster has a coordinator that acts as the deadlock detector for that cluster. The coordinators communicate with each other to construct a global wait-for graph and detect deadlocks.
  - Distributed approach: There is no central or hierarchical authority, and each site participates in the deadlock detection process. The sites exchange messages to probe for cycles in the wait-for graph and report the results to a designated initiator site. The initiator site decides whether a deadlock exists and initiates the resolution process if needed.
- The resolution process involves aborting one or more deadlocked processes to break the cycle and release the resources. The choice of which process to abort depends on several factors, such as the priority, the execution time, the number of resources held, and the cost of rollback.
- Deadlock detection in distributed systems has some advantages and disadvantages compared to deadlock prevention and avoidance:
  - Advantages: It allows more concurrency and flexibility in resource allocation, and it does not require a priori knowledge of the resource requests and availability.
  - Disadvantages: It incurs more overhead in terms of message passing and computation, and it may cause more wastage of resources and time due to rollback and restart of aborted processes.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on path pushing algorithms for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM.

### Path Pushing Algorithms

- Path pushing algorithms detect distributed deadlocks by maintaining an explicit global wait-for graph (WFG) at each site of the distributed system .
- The WFG is a directed graph that represents the dependencies among the processes that are waiting for resources. A cycle in the WFG indicates a deadlock.
- The basic idea is to build a global WFG for each site by sending the local WFG to all the neighboring sites whenever a deadlock computation is performed .
- The neighboring sites are the sites that have processes that are either waiting for or holding resources from the local site.
- The global WFG is updated whenever a process requests, releases, or is granted a resource, or when a local WFG is received from another site.
- The advantages of path pushing algorithms are that they can detect deadlocks quickly and accurately, and they do not require probe messages or diffusing computations .
- The disadvantages of path pushing algorithms are that they require a lot of communication and storage overhead, and they may generate false cycles due to the inconsistency of the global WFG .



### Edge Chasing Algorithms for Distributed Deadlock Detection

- Edge chasing algorithms are a class of distributed deadlock detection algorithms that use special messages called probes to trace the dependency graph of processes and resources in a distributed system.
- A probe is a triplet (i, j, k) that denotes that the deadlock detection is initiated by process P_i and the message is being sent by the home site of process P_j to the home site of process P_k.
- The probe message follows the edges of the dependency graph from the waiting processes to the blocking processes until either a cycle is detected or all the edges are traversed.
- A cycle is detected when a probe message returns to the initiator process or when a process receives a probe message with its own identifier in the triplet.
- The most well-known edge chasing algorithm is the Chandy-Misra-Haas algorithm, which works for the AND request model, where a process can request multiple resources simultaneously and wait for all of them to be granted.
- The Chandy-Misra-Haas algorithm works as follows:

  - Each process maintains a wait-for graph that contains the processes that it is waiting for and the processes that are waiting for it.
  - When a process P_i initiates a deadlock detection, it sends a probe message (i, i, j) to the home site of each process P_j that it is waiting for.
  - When a process P_j receives a probe message (i, k, j), it checks if it is involved in a deadlock with P_i. If yes, it sends a reply message to P_i indicating the deadlock. If no, it forwards the probe message (i, j, l) to the home site of each process P_l that it is waiting for.
  - When a process P_i receives a reply message from P_j, it knows that there is a deadlock involving P_i and P_j, and possibly other processes. It can then take appropriate actions to resolve the deadlock, such as aborting or preempting some processes.

- The advantages of edge chasing algorithms are that they are simple, efficient, and scalable. They do not require global knowledge of the system state or a central coordinator. They only involve the processes that are potentially deadlocked and the messages are small and bounded in number.
- The disadvantages of edge chasing algorithms are that they may generate false positives, meaning that they may detect a deadlock that does not exist, due to the asynchronous nature of the system. They may also incur high communication overhead and latency, especially in large and dynamic systems.



## Unit 4 - Agreement Protocols

- Agreement protocols are a class of distributed algorithms that allow a set of processes to reach a common decision or consensus in the presence of failures or uncertainties.
- Agreement protocols are useful for solving problems such as leader election, atomic commit, distributed mutual exclusion, and fault tolerance.
- Agreement protocols can be classified into two types: **synchronous** and **asynchronous**.
- Synchronous agreement protocols assume that there are known bounds on the message delays and the process speeds, and use timeouts or clocks to coordinate the actions of the processes.
- Asynchronous agreement protocols do not make any assumptions about the message delays and the process speeds, and rely on message ordering or logical clocks to coordinate the actions of the processes.
- Synchronous agreement protocols can tolerate crash failures, where a process stops executing, and Byzantine failures, where a process behaves arbitrarily or maliciously.
- Asynchronous agreement protocols can only tolerate crash failures, and not Byzantine failures, unless additional assumptions are made, such as the existence of a trusted third party or a majority of correct processes.
- Some examples of synchronous agreement protocols are:
  - **Paxos**, which is a protocol for reaching consensus on a single value among a set of processes, using a leader-based approach and a majority voting scheme.
  - **Raft**, which is a protocol for maintaining a replicated state machine among a set of processes, using a leader-based approach and a log replication scheme.
  - **Two-phase commit (2PC)**, which is a protocol for ensuring atomicity of a distributed transaction among a set of processes, using a coordinator process and a prepare-commit scheme.
- Some examples of asynchronous agreement protocols are:
  - **Chandra-Toueg consensus**, which is a protocol for reaching consensus on a single value among a set of processes, using a failure detector and a round-based scheme.
  - **Viewstamped replication (VSR)**, which is a protocol for maintaining a replicated state machine among a set of processes, using a primary-backup approach and a view change scheme.
  - **Three-phase commit (3PC)**, which is a protocol for ensuring atomicity of a distributed transaction among a set of processes, using a coordinator process and a pre-commit-commit scheme.



### Introduction

- Agreement protocols are a class of distributed algorithms that allow a set of processes to reach a common decision based on their individual inputs and preferences.
- Agreement protocols are essential for ensuring consistency, reliability, fault-tolerance, and security in distributed systems.
- Some examples of agreement problems are:
  - Consensus: All processes agree on a single value from a set of proposed values.
  - Atomic commit: All processes agree on whether to commit or abort a distributed transaction.
  - Byzantine agreement: All processes agree on a single value from a set of proposed values, even if some processes are faulty or malicious.
  - Leader election: All processes agree on a unique process to act as the coordinator or leader of the system.
  - Mutual exclusion: All processes agree on which process can access a shared resource at a given time.
- Agreement protocols are challenging to design and implement because of the inherent uncertainty and asynchrony in distributed systems. Processes may fail, messages may be lost or delayed, and clocks may be unsynchronized.
- Agreement protocols must satisfy some desirable properties, such as:
  - Validity: The agreed value must be one of the proposed values.
  - Agreement: All correct processes must agree on the same value.
  - Termination: All correct processes must eventually decide on a value.
  - Fault-tolerance: The protocol must work correctly even if some processes fail or behave arbitrarily.
  - Efficiency: The protocol must use a reasonable amount of time, space, and communication resources.
- Agreement protocols can be classified into different categories based on the assumptions they make about the system model, such as:
  - Synchronous vs. asynchronous: Whether the protocol assumes bounded or unbounded delays in message delivery and process execution.
  - Crash vs. Byzantine: Whether the protocol assumes processes can only fail by crashing or can also behave arbitrarily or maliciously.
  - Deterministic vs. randomized: Whether the protocol always produces the same output for the same input or can use randomization to break ties or increase the probability of success.
  - Message-passing vs. shared-memory: Whether the protocol uses direct communication between processes or indirect communication via a shared data structure.



### System models for distributed systems

System models are abstract descriptions of the properties and behavior of a distributed system. They help to understand, design, and implement distributed systems by providing a common vocabulary and framework for analysis. System models can be classified into three types:

- Architectural models: describe the structure and organization of a distributed system in terms of components and their interactions. They also define the roles and responsibilities of each component and the distribution of resources and tasks among them. Some common architectural models are:

  - Client-server model: a system where clients request services from servers, which provide them. Servers can be centralized or distributed, and clients can be thin or thick (depending on the amount of processing they do).
  - Peer-to-peer model: a system where each component acts as both a client and a server, and can communicate with any other component. Peers can be homogeneous or heterogeneous, and can form structured or unstructured overlays (depending on the topology of the network).
  - Publish-subscribe model: a system where components publish events or messages to a broker or a topic, and other components subscribe to receive them. Publishers and subscribers are decoupled and can be anonymous, and the broker or the topic can implement different types of filtering and routing mechanisms.

- Interaction models: describe the communication and coordination mechanisms used by the components of a distributed system. They also define the properties and guarantees of the messages exchanged, such as ordering, reliability, and atomicity. Some common interaction models are:

  - Message passing model: a system where components communicate by sending and receiving messages through a network. Messages can be synchronous or asynchronous, and can use different protocols and formats, such as TCP, UDP, HTTP, or JSON.
  - Remote procedure call model: a system where components communicate by invoking procedures or methods on remote objects or services. RPCs can be synchronous or asynchronous, and can use different middleware platforms, such as CORBA, RMI, or SOAP.
  - Shared memory model: a system where components communicate by accessing and modifying a shared data structure or a shared variable. Shared memory can be physical or logical, and can use different consistency and synchronization models, such as sequential, causal, or eventual consistency.

- Fault models: describe the types and causes of failures that can occur in a distributed system, and the assumptions and techniques to deal with them. They also define the availability and reliability of the components and the system as a whole. Some common fault models are:

  - Crash fault model: a system where components can fail by stopping their execution and not resuming it. Crash faults can be detected by timeouts or heartbeats, and can be tolerated by replication or redundancy.
  - Byzantine fault model: a system where components can fail by behaving arbitrarily or maliciously. Byzantine faults can be detected by cryptographic techniques or voting schemes, and can be tolerated by using a quorum or a consensus protocol.
  - Network fault model: a system where the network can fail by losing, delaying, duplicating, or reordering messages. Network faults can be detected by sequence numbers or checksums, and can be tolerated by using reliable or atomic broadcast protocols.



### Classification of Agreement Problem

An agreement problem is a problem where a set of processes in a distributed system need to reach a common decision based on their local inputs and messages exchanged with each other. Agreement problems are important for ensuring consistency, reliability, and fault-tolerance in distributed systems. There are different types of agreement problems, depending on the system model, the failure model, and the problem specification. Some of the common agreement problems are:

- **Byzantine agreement problem**: In this problem, each process has an initial value, and the processes need to agree on a common value, despite the presence of some faulty processes that may behave arbitrarily (Byzantine faults). The solution must satisfy the following properties :
  - **Validity**: If all the processes have the same initial value, then the agreed value must be equal to that value.
  - **Agreement**: All the non-faulty processes must agree on the same value.
  - **Termination**: All the non-faulty processes must eventually decide on a value.
- **Consensus problem**: In this problem, each process has an initial value, and the processes need to agree on a common value, despite the presence of some faulty processes that may crash (fail-stop faults). The solution must satisfy the following properties :
  - **Validity**: The agreed value must be one of the initial values of the non-faulty processes.
  - **Agreement**: All the non-faulty processes must agree on the same value.
  - **Termination**: All the non-faulty processes must eventually decide on a value.
- **Interactive consistency problem**: In this problem, each process has an initial value, and the processes need to agree on a vector of values, one for each process, despite the presence of some faulty processes that may behave arbitrarily (Byzantine faults). The solution must satisfy the following properties :
  - **Validity**: The value of the i-th component of the agreed vector must be equal to the initial value of the i-th process, if the i-th process is non-faulty.
  - **Agreement**: All the non-faulty processes must agree on the same vector.
  - **Termination**: All the non-faulty processes must eventually decide on a vector.
- **Atomic commitment problem**: In this problem, each process has an initial value, either commit or abort, and the processes need to agree on a common value, either commit or abort, despite the presence of some faulty processes that may crash (fail-stop faults). The solution must satisfy the following properties :
  - **Validity**: The agreed value must be commit if and only if all the non-faulty processes have the initial value commit.
  - **Agreement**: All the non-faulty processes must agree on the same value.
  - **Termination**: All the non-faulty processes must eventually decide on a value.
  - **Irrevocability**: If a process decides commit, it cannot change its decision later.



### Byzantine agreement problem

- The Byzantine agreement problem is a fundamental problem in fault tolerant distributed computing that requires a set of parties in a distributed environment to agree on a value even if some of the parties are corrupted.
- The problem was first defined by Lamport and was inspired by a hypothetical scenario where several divisions of the Byzantine army are camped outside an enemy city, each division commanded by its own general. The generals can communicate with one another only by messenger. After observing the enemy, they must decide upon a common plan of action  .
- The problem is challenging because some of the generals may be traitors who try to prevent the loyal generals from reaching agreement. The traitors may send conflicting messages to different generals, or may not send any messages at all. The loyal generals need a secure way to come to agreement on a plan (known as consensus) and carry out their chosen plan (known as coordination).
- A solution to the Byzantine agreement problem must satisfy the following properties :
  - **Termination**: Every loyal general eventually decides on a value.
  - **Agreement**: All loyal generals decide on the same value.
  - **Validity**: If all loyal generals start with the same value, then they all decide on that value.
- A number of solutions to the Byzantine agreement problem exist, but they have different assumptions and trade-offs. Some of the factors that affect the feasibility and efficiency of the solutions are :
  - The number of parties involved and the fraction of them that are corrupted.
  - The type of communication channels used (synchronous or asynchronous, reliable or unreliable, authenticated or unauthenticated, etc.).
  - The type of cryptographic primitives available (digital signatures, hash functions, encryption schemes, etc.).
  - The type of values to be agreed upon (binary, multivalued, or arbitrary).
  - The type of adversary model (static or adaptive, passive or active, etc.).
- Some examples of Byzantine agreement protocols are:
  - **Lamport's oral messages algorithm**: This is the original solution proposed by Lamport, which assumes synchronous and reliable communication channels, and requires 3f+1 parties to tolerate f corrupted parties. The algorithm involves f+1 rounds of message exchange, where each party sends its value to all other parties, and then applies a majority rule to decide on a value.
  - **Lamport's signed messages algorithm**: This is an improvement of the oral messages algorithm, which assumes authenticated communication channels, and requires 2f+1 parties to tolerate f corrupted parties. The algorithm involves f+1 rounds of message exchange, where each party signs its value and sends it to all other parties, and then applies a majority rule to decide on a value.
  - **King algorithm**: This is an optimization of the signed messages algorithm, which assumes authenticated communication channels, and requires 2f+1 parties to tolerate f corrupted parties. The algorithm involves only one round of message exchange, where one party is designated as the king and sends its value to all other parties, and then each party decides on the value received from the king, unless it is inconsistent with the values received from other parties.
  - **Practical Byzantine Fault Tolerance (PBFT) algorithm**: This is a practical solution for Byzantine agreement in asynchronous and unreliable communication channels, which requires 3f+1 parties to tolerate f corrupted parties. The algorithm involves three phases of message exchange, where one party is designated as the primary and proposes a value, and then the other parties exchange messages to verify and commit the value. The algorithm also uses checkpoints and view changes to ensure liveness and safety.



### Consensus problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- The consensus problem is the problem of getting a set of nodes in a distributed system to agree on something - it might be a value, a course of action or a decision.
- Achieving consensus allows a distributed system to act as a single entity, with every individual node aware of and in agreement with the actions of the whole of the network.
- Consensus is a general agreement on a decision made by the majority of those involved.
- Consensus is needed in a distributed system to ensure overall system reliability on top of unreliable system components.
- Consensus is also needed to coordinate the actions of different nodes, such as committing transactions, electing leaders, replicating data, etc.
- Consensus is hard to achieve in a distributed system due to the possibility of failures, such as node crashes, network partitions, message losses, etc.
- Consensus algorithms are protocols that enable nodes to reach consensus in a distributed system despite failures.
- Consensus algorithms can vary in terms of security and performance, depending on the assumptions and guarantees they make.
- Some examples of consensus algorithms are Two-Phase Commit, Three-Phase Commit, Paxos, Raft, etc.
- Consensus algorithms can be classified into two categories: crash-fault tolerant (CFT) and Byzantine-fault tolerant (BFT).
- CFT algorithms assume that nodes can only fail by crashing, and they can tolerate up to half of the nodes failing.
- BFT algorithms assume that nodes can fail in arbitrary ways, such as sending incorrect or malicious messages, and they can tolerate up to one-third of the nodes failing.
- BFT algorithms are more secure but less performant than CFT algorithms.



### Interactive Consistency Problem

- Interactive consistency is the problem in which n distinct nodes, each having its own private value, where up to t may be Byzantine, run an algorithm that allows all non-faulty nodes to infer the values of each other node   .
- Byzantine nodes are nodes that can behave arbitrarily, such as sending incorrect or conflicting messages, or remaining silent.
- Interactive consistency is a generalization of distributed consensus, which is the problem of reaching agreement on a single value among n nodes, where up to t may be Byzantine .
- Interactive consistency is also known as Byzantine Generals Problem, which is a metaphor for the situation where a group of generals must coordinate an attack or retreat, but some of them may be traitors who try to sabotage the plan.
- Interactive consistency is relevant to critical applications that rely on the combination of the opinions of multiple peers to provide a service, such as fault-tolerant distributed systems, blockchain systems, or voting systems .
- Interactive consistency is a challenging problem because it requires both reliability and security in the presence of faults and adversaries .
- Interactive consistency has some fundamental limitations and impossibility results, such as:
  - It is impossible to achieve interactive consistency in a purely asynchronous system, where there is no bound on message delays or node speeds, with any number of Byzantine nodes.
  - It is impossible to achieve interactive consistency in a synchronous system, where there is a known bound on message delays and node speeds, with more than n/3 Byzantine nodes.
  - It is possible to achieve interactive consistency in a synchronous system, where there is a known bound on message delays and node speeds, with up to n/3 Byzantine nodes, using a deterministic algorithm that requires n rounds of communication.
  - It is possible to achieve interactive consistency in a partially synchronous system, where there is an unknown bound on message delays and node speeds, with up to n/3 Byzantine nodes, using a randomized algorithm that requires expected constant rounds of communication .
- Interactive consistency can be solved by using various techniques, such as:
  - Broadcast algorithms, which allow a node to send a message to all other nodes, such that all non-faulty nodes receive the same message, even if the sender is Byzantine.
  - Byzantine consensus algorithms, which allow the nodes to agree on a single value, even if some of them are Byzantine.
  - Cryptographic primitives, such as digital signatures, hash functions, or public-key encryption, which can provide authentication, integrity, or confidentiality of messages .
  - Fault detection and recovery mechanisms, which can identify and isolate faulty nodes, or replace them with new nodes .



### Solution to Byzantine Agreement problem

- The Byzantine agreement problem is a fundamental problem in fault tolerant distributed computing, where a set of parties need to agree on a value even if some of them are corrupted or faulty.
- The problem is also known as the Byzantine generals problem, which is a metaphor for a situation where several divisions of the Byzantine army are camped outside an enemy city, and they need to decide whether to attack or retreat .
- The generals can only communicate by sending messages to each other, but some of them may be traitors who send false or conflicting messages to confuse the others .
- The goal is to design a protocol that allows the loyal generals to reach a consensus on a common plan of action, despite the presence of traitors .
- A solution to the Byzantine agreement problem must satisfy the following properties :
  - **Agreement**: All loyal parties must agree on the same value.
  - **Validity**: If all parties start with the same value, then they must agree on that value.
  - **Termination**: The protocol must eventually terminate.
- A solution to the Byzantine agreement problem also depends on the following parameters :
  - **n**: The total number of parties involved in the protocol.
  - **t**: The maximum number of faulty or traitorous parties.
  - **f**: The actual number of faulty or traitorous parties.
  - **m**: The number of rounds of message exchange in the protocol.
- A solution to the Byzantine agreement problem is said to be **resilient** if it can tolerate up to **t** faulty parties, and **optimal** if it can tolerate the maximum possible number of faulty parties, which is **n/3** for synchronous systems and **n/2** for asynchronous systems .
- There are several solutions to the Byzantine agreement problem, depending on the assumptions and the model of communication. Some of the most well-known solutions are:
  - **Lamport's oral messages algorithm**: This is a solution for synchronous systems, where parties have synchronized clocks and messages are delivered within a known bounded time . The algorithm uses **m** rounds of message exchange, where each party sends its initial value to all other parties, and then applies a majority rule to decide on the final value . The algorithm is resilient if **t < m**, and optimal if **m = t + 1** .
  - **Lamport's signed messages algorithm**: This is a solution for asynchronous systems, where parties do not have synchronized clocks and messages may be delayed arbitrarily . The algorithm uses digital signatures to authenticate the messages, and requires each party to send a signed message containing its initial value and the signatures of all previous messages it received . The algorithm is resilient if **t < n/3**, and optimal if **n > 3t** .
  - **Practical Byzantine Fault Tolerance (PBFT)**: This is a solution for asynchronous systems, where parties use a leader-based protocol to propose and agree on a value . The algorithm uses three phases: pre-prepare, prepare, and commit, where each party sends and receives messages from the leader and other parties, and decides on the final value based on a quorum of messages . The algorithm is resilient if **t < n/3**, and optimal if **n > 3t** .



### Application of Agreement problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- Agreement problem is a fundamental problem in distributed computing and multi-agent systems that requires coordinating processes to reach consensus, or agree on some data value that is needed during computation .
- Agreement problem is essential for achieving overall system reliability in the presence of a number of faulty processes .
- Agreement problem has many forms and variations, such as consensus, atomic commitment, atomic broadcast, group membership, etc .
- Consensus is the problem of getting all processes to agree on a single value, such as a leader, a timestamp, a transaction, etc  .
- Atomic commitment is the problem of getting all processes to agree on whether to commit or abort a transaction, such as a database update, a file transfer, etc .
- Atomic broadcast is the problem of getting all processes to deliver the same set of messages in the same order, such as a chat application, a replicated state machine, etc .
- Group membership is the problem of getting all processes to agree on the current set of active processes in the system, such as a fault-tolerant service, a distributed lock, etc .
- Agreement problem is challenging to solve in distributed systems because of the possibility of communication failures, process failures, network partitions, message delays, etc  .
- Agreement problem is impossible to solve in asynchronous systems, where there is no bound on message delivery time or process execution speed, under the assumption of even one faulty process .
- Agreement problem can be solved in synchronous systems, where there is a known bound on message delivery time and process execution speed, under the assumption of a bounded number of faulty processes  .
- Agreement problem can be solved in partially synchronous systems, where there is a bound on message delivery time and process execution speed that is eventually known or satisfied, under the assumption of a bounded number of faulty processes .
- Agreement problem can be solved using various algorithms and protocols, such as Paxos, Raft, Two-Phase Commit, Three-Phase Commit, Byzantine Agreement, etc   .
- Agreement problem can be solved using different models and assumptions, such as crash failures, Byzantine failures, authenticated messages, broadcast channels, etc   .
- Agreement problem can be solved using different techniques and strategies, such as quorums, majority voting, leader election, timeouts, retries, etc   .
- Agreement problem can be applied to various domains and applications, such as distributed databases, distributed file systems, distributed ledger technologies, distributed consensus platforms, etc   .



### Atomic Commit in Distributed Database System

- A distributed database system consists of multiple database sites that are connected by a communication network.
- A distributed transaction is a transaction that accesses data from multiple sites and updates them atomically.
- Atomicity means that either all the updates are committed or none of them are committed, leaving the database in a consistent state.
- Atomic commit is the process of coordinating the decision to commit or abort a distributed transaction among all the participating sites.
- Atomic commit protocols are algorithms that ensure the atomicity of distributed transactions in the presence of failures, such as site crashes, network partitions, or message losses.
- Atomic commit protocols can be classified into two categories: blocking and non-blocking.
  - Blocking protocols require some sites to wait for the recovery of other sites before making a final decision. Examples of blocking protocols are the two-phase commit (2PC) protocol and the three-phase commit (3PC) protocol.
  - Non-blocking protocols allow some sites to make a final decision without waiting for the recovery of other sites. Examples of non-blocking protocols are the Paxos commit protocol and the FLAC protocol.
- The performance and reliability of atomic commit protocols depend on various factors, such as the number of sites, the number of messages, the failure rate, the recovery time, and the network latency.



## Unit 5 - Distributed Resource Management

- Distributed resource management is the process of allocating and managing resources in a distributed system, such as processors, memory, disk space, network bandwidth, etc.
- The main objectives of distributed resource management are to improve the performance, reliability, availability, and scalability of the system, as well as to balance the load and reduce the cost and energy consumption.
- The main challenges of distributed resource management are to deal with the heterogeneity, dynamism, uncertainty, and complexity of the system, as well as to cope with the trade-offs and conflicts among different objectives and constraints.
- Some of the key concepts and techniques of distributed resource management are:

  - Resource discovery: the process of finding and identifying the available resources in the system, such as using directory services, multicast protocols, or peer-to-peer networks.
  - Resource description: the process of specifying the attributes and capabilities of the resources, such as using XML, RDF, or ontologies.
  - Resource selection: the process of choosing the best or most suitable resources for a given task, such as using matchmaking, ranking, or bidding algorithms.
  - Resource allocation: the process of assigning and distributing the resources to the tasks, such as using scheduling, reservation, or negotiation algorithms.
  - Resource monitoring: the process of observing and measuring the status and performance of the resources, such as using probes, agents, or sensors.
  - Resource adaptation: the process of adjusting and optimizing the resource usage and configuration, such as using feedback, control, or learning algorithms.

- Some of the applications and examples of distributed resource management are:

  - Grid computing: a form of distributed computing that involves the sharing and coordination of large-scale heterogeneous and geographically distributed resources, such as supercomputers, clusters, or data centers, for solving complex scientific or engineering problems.
  - Cloud computing: a form of distributed computing that involves the provision and consumption of on-demand and scalable resources, such as servers, storage, or applications, over the Internet, for supporting various business or personal needs.
  - Edge computing: a form of distributed computing that involves the processing and storage of data at the edge of the network, such as mobile devices, sensors, or gateways, for improving the latency, bandwidth, or privacy of the applications.
  - Internet of Things (IoT): a form of distributed computing that involves the interconnection and communication of various physical objects and devices, such as smart homes, cars, or wearables, for enabling various services and functionalities.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of issues in distributed file systems for the unit 5 of distributed resource management in the subject of distributed system.

### Issues in distributed file systems

- A distributed file system (DFS) is a system that allows multiple clients to access and manipulate files stored on one or more servers over a network .
- A DFS should provide the following features:
  - Transparency: The users and applications should not be aware of the physical locations and the network details of the files.
  - Consistency: The users and applications should see a consistent view of the files, regardless of concurrent updates or failures.
  - Fault tolerance: The DFS should be able to continue in case of any partial failures like a link failure, a node failure, or a storage drive crash.
  - Scalability: The DFS should be able to handle a large number of files, clients, and servers without degrading the performance or the reliability.
  - Security: The DFS should provide mechanisms to protect the files from unauthorized access, modification, or deletion.
- Some of the challenges and issues in designing and implementing a DFS are    :
  - Naming: How to assign unique and meaningful names to the files and directories, and how to resolve them to the physical locations.
  - Replication: How to create and maintain multiple copies of the files on different servers to improve availability, reliability, and performance.
  - Caching: How to store frequently accessed files or parts of files on the local disks or memory of the clients to reduce the network traffic and the server load.
  - Consistency: How to ensure that the replicas and the caches are synchronized with the original files, and how to handle concurrent updates and conflicts.
  - Synchronization: How to coordinate the access and the modification of the files among multiple clients and servers, and how to use locking or versioning mechanisms to prevent data inconsistency or corruption.
  - Distributed transactions: How to support atomic and durable operations on multiple files that span across different servers, and how to use commit or rollback protocols to ensure data integrity.
  - Recovery: How to restore the files and the system state in case of failures, and how to use backup, checkpoint, or logging techniques to prevent data loss or corruption.
  - Security: How to authenticate the clients and the servers, and how to use encryption, access control, or auditing techniques to protect the data and the system from malicious attacks or unauthorized access.
  - Performance: How to optimize the system design and the algorithms to achieve high throughput, low latency, and good scalability, and how to use load balancing, prefetching, or compression techniques to improve the system efficiency and the user experience.
  - Heterogeneity: How to support different types of files, clients, servers, and networks, and how to use standard protocols, interfaces, or middleware to ensure interoperability and compatibility.



### Mechanism for building distributed file systems

A distributed file system (DFS) is a file system that is distributed on multiple file servers or multiple locations. It allows programs to access or store isolated files as they do with the local ones, allowing programmers to access files from any network or computer.

The mechanism for building distributed file systems involves the following aspects:

- Use of file models: The DFS uses different conceptual models of a file. The following are the two basic criteria for file modeling, which include file structure and modifiability. The files can be unstructured or structured based on the applications used in file systems. The files can also be immutable or mutable depending on whether they can be modified after creation or not.
- Use of file accessing models: A distributed file system may use one of the following models to service a client’s file requests: upload/download, remote access, or remote service. The upload/download model involves transferring the entire file between the client and the server. The remote access model involves transferring only the requested portions of the file. The remote service model involves executing the file operations on the server and returning the results to the client.
- Use of file replication: File replication is the primary mechanism for improving file availability in a distributed systems environment. A replicated file is a file that has multiple copies with each copy located on a separate file server. The challenges of file replication include maintaining consistency among the replicas, balancing the load among the servers, and handling failures and recovery .
- Use of file caching: File caching is the secondary mechanism for improving file performance in a distributed systems environment. A file cache is a temporary storage area that holds a copy of a file or a portion of a file that is frequently accessed by the client. The benefits of file caching include reducing the network traffic, improving the response time, and saving the bandwidth. The challenges of file caching include maintaining coherence among the caches, managing the cache size and replacement, and handling failures and recovery.
- Use of file naming: File naming is the mechanism for identifying and locating files in a distributed file system. A file name consists of two parts: a file identifier and a file path. A file identifier is a unique and persistent name that is assigned to a file when it is created. A file path is a sequence of directory names that leads to the file. A file name can be either absolute or relative. An absolute file name specifies the complete path from the root directory to the file. A relative file name specifies the path from the current directory to the file.
- Use of file security: File security is the mechanism for protecting files from unauthorized access and modification in a distributed file system. File security involves two aspects: authentication and authorization. Authentication is the process of verifying the identity of the user or the process that requests access to a file. Authorization is the process of granting or denying access rights to a file based on the user’s identity and the file’s permissions. File permissions specify the operations that can be performed on a file by different categories of users, such as the owner, the group, or the others.
- Use of file migration: File migration is the mechanism for moving files from one location to another in a distributed file system. File migration can be either static or dynamic. Static file migration involves relocating files based on a predefined policy or a manual intervention. Dynamic file migration involves relocating files based on the current system state, such as the load, the availability, or the demand. The objectives of file migration include improving the file access performance, balancing the load among the servers, and optimizing the resource utilization.
- Use of cloud services: Cloud services are the mechanism for extending a distributed file system to the cloud. Cloud services expose file and object storage using either standard protocols such as NFS and SMB or published APIs such as Amazon S3 and Google Cloud Storage. The advantages of cloud services include scalability, elasticity, reliability, and cost-effectiveness. The challenges of cloud services include security, privacy, interoperability, and performance.



### Design issues in Distributed Shared Memory

Distributed Shared Memory (DSM) is a mechanism that allows multiple processes on different nodes to share a common logical address space and access data transparently. DSM can simplify the programming of distributed systems by hiding the details of inter-process communication. However, DSM also introduces several design issues that affect its performance, scalability, and correctness. Some of the main design issues in DSM are:

- **Granularity**: Granularity refers to the size of the unit of sharing and the unit of coherence in DSM. A smaller granularity (such as a byte or a word) can reduce the amount of false sharing and improve the locality of access, but it can also increase the overhead of coherence maintenance and communication. A larger granularity (such as a page or a segment) can reduce the overhead of coherence and communication, but it can also increase the amount of false sharing and waste bandwidth and memory. Therefore, choosing an appropriate granularity is a trade-off between these factors.

- **Structure**: Structure refers to the organization of the shared data in the logical address space and the mapping of the shared data to the physical memory of the nodes. The structure of DSM can be flat, hierarchical, or object-based. A flat structure treats the shared data as a single linear array of bytes or words, and uses a fixed or dynamic mapping to distribute the data among the nodes. A hierarchical structure divides the shared data into multiple regions or segments, and allows each region or segment to have a different mapping and coherence policy. An object-based structure treats the shared data as a collection of objects, and allows each object to have a different location, size, type, and coherence policy.

- **Coherence semantics**: Coherence semantics define the consistency model of DSM, which specifies the order and visibility of the updates to the shared data. Coherence semantics can be strict or relaxed. A strict coherence semantics (such as sequential consistency or processor consistency) guarantees that all processes see the same order of updates to the shared data, and that the updates are visible as soon as they are performed. A relaxed coherence semantics (such as release consistency or entry consistency) allows different processes to see different orders of updates to the shared data, and delays the visibility of the updates until certain synchronization events occur. A strict coherence semantics can simplify the programming of DSM, but it can also limit the concurrency and performance of the system. A relaxed coherence semantics can improve the concurrency and performance of the system, but it can also complicate the programming and debugging of DSM.

- **Coherence protocol**: Coherence protocol defines the mechanism of maintaining the coherence of the shared data in DSM. Coherence protocol can be centralized or distributed. A centralized coherence protocol uses a single node or a small set of nodes as the manager or the directory of the shared data, and relies on the manager or the directory to coordinate the access and update of the shared data among the nodes. A distributed coherence protocol uses a distributed algorithm or a distributed data structure to coordinate the access and update of the shared data among the nodes, without relying on a central manager or directory. A centralized coherence protocol can simplify the design and implementation of DSM, but it can also introduce a single point of failure and a bottleneck of communication and computation. A distributed coherence protocol can improve the fault tolerance and scalability of DSM, but it can also increase the complexity and overhead of the system.

- **Scalability**: Scalability refers to the ability of DSM to handle a large number of nodes and a large amount of shared data. Scalability depends on several factors, such as the granularity, the structure, the coherence semantics, and the coherence protocol of DSM. A scalable DSM should minimize the communication and computation overhead of coherence maintenance, the memory and bandwidth consumption of data replication, and the contention and latency of data access and update. A scalable DSM should also adapt to the changes in the system size, the workload, and the network topology.

- **Heterogeneity**: Heterogeneity refers to the diversity of the nodes and the network in DSM. Heterogeneity can be in terms of the hardware architecture, the operating system, the programming language, the communication protocol, and the performance characteristics of the nodes and the network. Heterogeneity can pose several challenges for DSM, such as the compatibility, the interoperability, the portability, and the performance optimization of the system. A heterogeneous DSM should provide a uniform and transparent interface for the shared data access and update, and should also exploit the specific features and capabilities of the different nodes and the network.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is a summary of the algorithm for implementation of distributed shared memory for the notes of the Unit 5 - Distributed Resource Management in the subject of DISTRIBUTED SYSTEM.

### Algorithm for Implementation of Distributed Shared Memory

Distributed shared memory (DSM) is a technique that allows multiple processes on different nodes of a distributed system to access a common virtual address space as if they were running on a single machine. DSM can simplify the programming of distributed applications by providing a shared memory abstraction. However, DSM also introduces challenges such as maintaining consistency, coherence, and performance of the shared data.

There are different algorithms for implementing DSM, each with its own advantages and disadvantages. Some of the basic algorithms are:

- **Central Server Algorithm**: In this algorithm, a central server maintains all the shared data and services read and write requests from other nodes. The central server can use a page-based or an object-based approach to manage the shared data. The advantage of this algorithm is that it is simple and ensures consistency and coherence of the shared data. The disadvantage is that it introduces a single point of failure and a bottleneck for communication and computation.
- **Migration Algorithm**: In this algorithm, the shared data is distributed among the nodes and can migrate from one node to another based on the access patterns. Each node has a local copy of the shared data that it accesses, and when a node requests a data item that is not present locally, it is transferred from the node that currently owns it. The advantage of this algorithm is that it reduces the communication overhead and improves the locality of the shared data. The disadvantage is that it may cause frequent data transfers and inconsistency issues.
- **Replication Algorithm**: In this algorithm, the shared data is replicated on multiple nodes and each node can access its local copy. The replication can be done eagerly or lazily, depending on whether the updates are propagated to all the replicas immediately or on demand. The advantage of this algorithm is that it enhances the availability and fault-tolerance of the shared data and reduces the communication latency. The disadvantage is that it may consume more memory and network bandwidth and create coherence problems.
- **Invalidation Algorithm**: In this algorithm, the shared data is distributed among the nodes and each node has a local cache of the data items that it accesses. The cache can be invalidated by the owner node or by a central coordinator when the data is updated. The invalidation can be done eagerly or lazily, depending on whether the invalidation messages are sent to all the cache holders immediately or on demand. The advantage of this algorithm is that it reduces the communication overhead and improves the performance of read operations. The disadvantage is that it may increase the cache miss rate and the complexity of the cache management.



## Unit 6 - Failure Recovery in Distributed Systems

- Failure recovery is the process of restoring the correct state and operation of a distributed system after a failure occurs.
- Failure recovery is essential for fault tolerance, which is the ability of a system to continue functioning despite faults or errors.
- Failure recovery can be classified into two types: reactive and proactive.
  - Reactive failure recovery involves detecting and correcting failures after they happen, using techniques such as checkpointing, logging, replication, and rollback.
  - Proactive failure recovery involves preventing or avoiding failures before they happen, using techniques such as fault detection, fault diagnosis, fault isolation, and fault masking.
- Failure recovery can also be classified into two levels: system level and application level.
  - System level failure recovery aims to restore the availability and consistency of the system resources, such as nodes, links, and data.
  - Application level failure recovery aims to restore the correctness and progress of the application logic, such as transactions, workflows, and computations.
- Failure recovery can be challenging in distributed systems due to the following issues:
  - Partial failures: some components of the system may fail while others remain operational, making it difficult to detect and isolate failures.
  - Network failures: communication links may fail or become unreliable, causing message loss, duplication, or delay, which can affect the coordination and synchronization of the system.
  - Concurrency: multiple processes may access or update the same data or resources concurrently, leading to inconsistency or conflicts, which can affect the correctness and integrity of the system.
  - Transparency: the system may hide the details of its distribution and replication from the users and applications, making it difficult to identify and recover from failures.
- Failure recovery can be achieved by using various techniques and mechanisms, such as:
  - Checkpointing: periodically saving the state of the system or the application to a stable storage, which can be used to resume the execution from a consistent point in case of a failure.
  - Logging: recording the events or actions of the system or the application to a stable storage, which can be used to replay or undo the execution in case of a failure.
  - Replication: maintaining multiple copies of the system or the application on different nodes, which can provide redundancy and fault tolerance in case of a failure.
  - Rollback: restoring the state of the system or the application to a previous consistent point in case of a failure, which can undo the effects of the failure.
  - Fault detection: monitoring the system or the application for signs of faults or errors, such as timeouts, exceptions, or anomalies, which can trigger the failure recovery process.
  - Fault diagnosis: identifying the cause and location of the faults or errors, such as node crashes, link failures, or data corruption, which can help in isolating and correcting the faults.
  - Fault isolation: separating the faulty components from the rest of the system, such as disconnecting the links, blocking the messages, or removing the nodes, which can prevent the propagation of the faults.
  - Fault masking: hiding the effects of the faults from the users and applications, such as providing alternative paths, substituting values, or retrying operations, which can maintain the functionality and performance of the system.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on the concepts of backward and forward recovery in distributed systems.

### Concepts in Backward and Forward Recovery

- **Backward recovery** is a technique that restores the system state to a previous error-free state after a failure occurs. It involves three steps:
  - **Checkpointing**: periodically saving the system state to a stable storage.
  - **Logging**: recording the actions performed by the system in a log file.
  - **Rollback**: undoing the effects of the actions that occurred after the last checkpoint.
- **Forward recovery** is a technique that corrects the errors in the system state and allows the system to continue its normal execution. It involves two steps:
  - **Error detection**: identifying the errors in the system state using techniques such as redundancy, checksums, or timeouts.
  - **Error correction**: applying corrective actions to the system state using techniques such as retry, compensation, or masking.
- The main difference between backward and forward recovery is that backward recovery requires the system to restart from a previous state, while forward recovery does not. Backward recovery is more general and independent of the nature of faults, but it may incur more overhead and latency. Forward recovery is more efficient and responsive, but it may require more knowledge and complexity of the system.
- In distributed systems, recovery techniques need to ensure the **consistency** and **availability** of the system. Consistency means that the system state is coherent and agreed upon by all the components. Availability means that the system can provide its services despite failures. Some of the challenges and solutions for recovery in distributed systems are :
  - **Synchronization**: ensuring that the system components take checkpoints and rollbacks at the same time or in a coordinated manner. This can be achieved by using algorithms such as **synchronous checkpointing**, **asynchronous checkpointing**, or **communication-induced checkpointing**.
  - **Dependency**: ensuring that the system components do not depend on the actions or states of other components that have rolled back. This can be achieved by using algorithms such as **domino effect avoidance**, **orphan message prevention**, or **independent recovery**.
  - **Communication**: ensuring that the system components can communicate with each other and exchange information about their states and actions. This can be achieved by using protocols such as **two-phase commit**, **three-phase commit**, or **distributed logging**.



### Recovery in Concurrent Systems

- Recovery in concurrent systems is the process of restoring the system to a consistent state after a failure, while preserving the effects of concurrent transactions that did not cause the failure.
- Recovery in concurrent systems is challenging because of the interleaving of operations from different transactions, which may affect the same data items or resources.
- Recovery in concurrent systems requires coordination between the concurrency control and the recovery mechanisms, to ensure that the system maintains the ACID properties of transactions (atomicity, consistency, isolation, and durability).
- Recovery in concurrent systems can be classified into two main categories: backward recovery and forward recovery.

#### Backward Recovery

- Backward recovery is the technique of undoing the effects of erroneous or incomplete transactions, and restoring the system to a previous consistent state.
- Backward recovery relies on logging the operations and data values of transactions, so that they can be reversed in case of a failure.
- Backward recovery can be done in different ways, depending on the concurrency control scheme used, such as:
  - Interaction with concurrency control: The recovery scheme depends on the concurrency control scheme, such as locking, timestamp ordering, or optimistic concurrency control, to determine which transactions need to be undone and in what order.
  - Transaction rollback: The recovery scheme aborts and undoes the transactions that are affected by the failure, either partially or completely, and restarts them later.
  - Checkpoints: The recovery scheme periodically saves the state of the system and the transactions, so that in case of a failure, it can undo the transactions that occurred after the last checkpoint, and resume from there.
  - Restart recovery: The recovery scheme restarts the system after a failure, and uses the log to undo the transactions that were not committed before the failure, and redo the transactions that were committed but not reflected in the database.

#### Forward Recovery

- Forward recovery is the technique of correcting the effects of erroneous or incomplete transactions, and advancing the system to a new consistent state.
- Forward recovery relies on detecting and resolving the errors or inconsistencies in the system, without undoing the transactions that caused them.
- Forward recovery can be done in different ways, such as:
  - Compensation: The recovery scheme applies compensating operations to reverse the effects of erroneous transactions, without aborting them.
  - Majority consensus: The recovery scheme uses a voting protocol to determine the correct value of a data item or a resource, based on the majority of the replicas or participants in the system.
  - Error masking: The recovery scheme uses redundancy or fault tolerance techniques to mask the errors or inconsistencies in the system, and continue the normal operation.



### Obtaining consistent Checkpoints for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Failure recovery in distributed systems is the process of restoring the system to a consistent and correct state after a failure occurs.
- A failure in a distributed system can be caused by various factors, such as node crashes, network partitions, message losses, malicious attacks, etc.
- A consistent checkpoint is a snapshot of the global state of the system that satisfies the following properties:
  - No orphan message: A message is orphan if it is sent by a process before taking its checkpoint, but received by another process after taking its checkpoint.
  - No domino effect: The domino effect occurs when a failure forces the system to roll back to an earlier checkpoint, which in turn causes another failure, and so on, until the system reaches the initial state.
- Obtaining consistent checkpoints is important for efficient and correct failure recovery, as it allows the system to resume the computation from a known and valid state, without losing or repeating any work.
- There are different techniques for obtaining consistent checkpoints, such as coordinated checkpointing, uncoordinated checkpointing, and communication-induced checkpointing.
  - Coordinated checkpointing: All the processes in the system agree on when to take a checkpoint, and synchronize their actions to ensure a consistent global state. This technique is simple and avoids the orphan message problem, but it incurs a high overhead and requires a reliable broadcast mechanism.
  - Uncoordinated checkpointing: Each process takes a checkpoint independently, without any coordination with other processes. This technique is flexible and scalable, but it may result in inconsistent global states and requires a complex recovery algorithm to deal with orphan messages and domino effect.
  - Communication-induced checkpointing: Each process takes a checkpoint based on the information piggybacked on the messages it receives from other processes. This technique is adaptive and reduces the number of checkpoints, but it requires a consistent cut detection algorithm and a dependency tracking mechanism.
- The choice of the checkpointing technique depends on the characteristics of the system, such as the failure rate, the communication pattern, the checkpoint size, the recovery time, etc.



### Recovery in Distributed Database Systems

- Recovery in distributed database systems is the process of restoring the database to a consistent and correct state after a failure or a transaction abort.
- Recovery in distributed database systems is more complex than in centralized database systems because of the following reasons:
  - Failures can occur at multiple sites or communication links, affecting different parts of a distributed transaction.
  - A distributed transaction may involve multiple sites with different recovery protocols and failure modes.
  - A distributed transaction may have partial or inconsistent information about the status of other sites or subtransactions.
  - A distributed transaction may have to coordinate with other concurrent transactions that span multiple sites.
- Recovery in distributed database systems aims to maintain the atomicity and durability of distributed transactions, which means that either all or none of the subtransactions of a distributed transaction are committed, and the effects of committed transactions are permanent.
- Recovery in distributed database systems can be classified into two types: local recovery and global recovery.
  - Local recovery is the process of recovering from a failure or a transaction abort at a single site. It involves applying the undo and redo operations on the local log records to restore the local database to a consistent state. Local recovery is similar to recovery in centralized database systems, except that it may have to deal with the dependencies and dependencies of subtransactions on other sites.
  - Global recovery is the process of recovering from a failure or a transaction abort that affects multiple sites or the entire distributed system. It involves coordinating the commit or abort decisions of all the subtransactions of a distributed transaction, and ensuring that all the sites agree on the same outcome. Global recovery may require communication and synchronization among the sites, and may have to handle network partitions, site failures, and message losses. Global recovery can be further divided into two subtypes: backward recovery and forward recovery.
    - Backward recovery is the process of aborting a distributed transaction and undoing its effects on all the sites. It is also known as rollback or compensation. Backward recovery is used when a subtransaction fails or aborts, or when a distributed transaction cannot commit due to concurrency control or deadlock resolution. Backward recovery may require the use of a distributed commit protocol, such as the two-phase commit protocol, to ensure that all the sites agree on the abort decision and execute the undo operations in a consistent order.
    - Forward recovery is the process of committing a distributed transaction and redoing its effects on all the sites. It is also known as retry or re-execution. Forward recovery is used when a site or a communication link fails, and the distributed transaction has already committed at some sites but not at others. Forward recovery may require the use of a distributed commit protocol, such as the three-phase commit protocol, to ensure that all the sites agree on the commit decision and execute the redo operations in a consistent order.



## Unit 7 - Fault Tolerance

- Fault tolerance is the property that enables a system to continue operating properly in the event of the failure of one or more faults within some of its components.
- The objective of creating a fault-tolerant system is to prevent disruptions arising from a single point of failure, ensuring the high availability and business continuity of the system.
- Fault tolerance can be achieved by using various techniques, such as redundancy, replication, backup, failover, recovery, error detection and correction, etc.
- Fault tolerance can be applied at different levels of a system, such as hardware, software, network, data, etc.
- Fault tolerance can be classified into different types, such as active, passive, hybrid, adaptive, etc., depending on the degree of redundancy, the mode of operation, and the response to faults.
- Fault tolerance can be measured by various metrics, such as reliability, availability, maintainability, safety, etc., depending on the system requirements and the fault scenarios.



### Issues in Fault Tolerance for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Fault tolerance is the ability of a system to continue functioning correctly in the presence of failures.
- Fault tolerance is important for distributed systems because they consist of multiple components that may be subject to different types of failures, such as hardware, software, network, or human errors .
- Fault tolerance mechanisms in distributed systems aim to detect, mask, tolerate, or recover from failures, and to maintain the consistency, availability, and reliability of the system .
- Some of the issues and challenges in fault tolerance for distributed systems are:
  - How to classify and model different types of faults and failures .
  - How to design and implement fault-tolerant algorithms and protocols that can cope with various failure scenarios .
  - How to measure and evaluate the performance and dependability of fault-tolerant systems .
  - How to balance the trade-offs between fault tolerance and other system properties, such as complexity, scalability, efficiency, and security .
  - How to adapt to dynamic and heterogeneous environments, where the system configuration, workload, and failure patterns may change over time .



### Commit Protocols

- Commit protocols are algorithms that ensure the atomicity of distributed transactions, i.e., all the sites involved in a transaction either commit or abort it unanimously, even in the presence of failures  .
- Commit protocols involve a coordinator site that initiates the transaction and communicates with the participant sites that execute the transaction on behalf of the coordinator .
- There are different types of commit protocols, such as one-phase commit, two-phase commit, and three-phase commit, that vary in the number of phases and messages exchanged between the coordinator and the participants   .

#### One-Phase Commit Protocol

- A one-phase commit protocol involves only one phase, in which the coordinator sends a commit request to all the participants and waits for their replies.
- If all the participants reply with an OK message, the coordinator commits the transaction and sends a commit message to all the participants.
- If any participant replies with an abort message, the coordinator aborts the transaction and sends an abort message to all the participants.
- The advantages of this protocol are simplicity and low message overhead.
- The disadvantages of this protocol are lack of fault tolerance and concurrency control. If the coordinator or any participant fails, the transaction may be left in an inconsistent state. Also, the participants have to lock the resources until they receive the commit or abort message from the coordinator, which may cause blocking and deadlock.

#### Two-Phase Commit Protocol

- A two-phase commit protocol involves two phases: a voting phase and a commit phase  .
- In the voting phase, the coordinator sends a prepare message to all the participants, asking them to vote on whether to commit or abort the transaction  .
- Each participant replies with a yes or no vote, after executing the transaction and writing a prepare log record  .
- In the commit phase, the coordinator decides whether to commit or abort the transaction based on the votes received from the participants  .
- If all the votes are yes, the coordinator commits the transaction and sends a commit message to all the participants  .
- If any vote is no, the coordinator aborts the transaction and sends an abort message to all the participants  .
- Each participant commits or aborts the transaction according to the message received from the coordinator, and writes a commit or abort log record  .
- The advantages of this protocol are fault tolerance and concurrency control  . If the coordinator or any participant fails, the transaction can be recovered from the log records. Also, the participants can release the locks after the voting phase, which reduces the blocking and deadlock  .
- The disadvantage of this protocol is blocking  . If the coordinator fails after the voting phase, the participants have to wait indefinitely for the commit or abort message, which may cause the system to stall  .

#### Three-Phase Commit Protocol

- A three-phase commit protocol involves three phases: a prepare phase, a pre-commit phase, and a commit phase .
- The prepare phase is the same as in the two-phase commit protocol .
- In the pre-commit phase, the coordinator sends an enter prepared state message to all the participants, if all the votes are yes .
- The participants reply with an OK message, after entering a prepared state and writing a pre-commit log record .
- In the commit phase, the coordinator sends a commit message to all the participants, if all the OK messages are received .
- The participants commit the transaction and write a commit log record .
- If any vote is no or any OK message is not received, the coordinator sends an abort message to all the participants[^1^



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on voting protocols for fault tolerance in distributed systems:

### Voting protocols for fault tolerance in distributed systems

- Voting protocols are a type of consensus protocols that allow a set of nodes in a distributed system to agree on a common value or decision, despite the presence of faults or attacks.
- Voting protocols are based on the idea of collecting votes from a subset of nodes, called a quorum, and applying a voting function to determine the final outcome.
- Voting protocols can be classified into two categories: exact voting and inexact voting.
  - Exact voting requires that all nodes in the quorum agree on the same value or decision, and that the voting function is a simple majority or unanimity. Exact voting can tolerate up to half of the quorum nodes being faulty or malicious, but it may suffer from low availability or high latency.
  - Inexact voting allows some nodes in the quorum to disagree on the value or decision, and that the voting function is a weighted majority or a threshold function. Inexact voting can tolerate more than half of the quorum nodes being faulty or malicious, but it may suffer from low accuracy or consistency.
- Voting protocols can also be classified into two types: static voting and dynamic voting.
  - Static voting assumes that the quorum size and composition are fixed and predetermined, and that the voting function is known and agreed upon by all nodes. Static voting can simplify the protocol design and implementation, but it may not adapt well to changes in the system or the environment.
  - Dynamic voting allows the quorum size and composition to vary depending on the context and the state of the system, and that the voting function can be negotiated or learned by the nodes. Dynamic voting can improve the protocol performance and robustness, but it may introduce more complexity and overhead.
- Voting protocols can be used for various purposes in distributed systems, such as data replication, transaction commit, leader election, group membership, or configuration management. Voting protocols can also be combined with other techniques, such as cryptography, trust, or reputation, to enhance their security and fault-tolerance.



### Dynamic voting protocols

- Dynamic voting protocols are techniques for consistency and recovery control of replicated files in distributed systems  .
- The purpose of a replicated file is to improve the availability of a logical file in the presence of site failures and network partitions  .
- A dynamic voting protocol assigns a number of votes to each replica of a file, and requires a majority of votes to access or update the file   .
- The number of votes assigned to each replica can change dynamically depending on the system state, such as the number of active replicas, the network connectivity, or the access pattern   .
- A dynamic voting protocol can achieve the following objectives   :
  - Maintain the consistency of replicated files by ensuring that only one group of replicas can access or update the file at a time.
  - Maximize the availability of replicated files by allowing access or update even when some replicas or links are faulty or disconnected.
  - Minimize the communication overhead by reducing the number of messages and votes required for each access or update operation.
  - Adapt to the changing system state by reassigning votes to balance the load and improve the performance.
- A dynamic voting protocol consists of the following components   :
  - A voting algorithm that determines how many votes are assigned to each replica and how many votes are required for each access or update operation.
  - A vote reassignment algorithm that decides when and how to change the vote assignment of each replica based on the system state.
  - A recovery algorithm that restores the consistency and availability of replicated files after a failure or a partition.
- Examples of dynamic voting protocols are     :
  - Majority consensus voting, which assigns one vote to each replica and requires a majority of votes for each access or update operation.
  - Weighted voting, which assigns different weights to each replica and requires a weighted majority of votes for each access or update operation.
  - Quorum-based voting, which assigns a read quorum and a write quorum to each replica and requires a read quorum for read operations and a write quorum for write operations.
  - Topological voting, which assigns votes to each replica based on the network topology and the location of the requester.
  - Dynamic weighted voting, which adjusts the weights of each replica based on the access frequency and the network distance.
  - Dynamic quorum-based voting, which adjusts the read and write quorums of each replica based on the availability and the load of the system.



## Unit 8 - Transactions and Concurrency Control

- A **transaction** is a logical unit of work that consists of a sequence of database operations, such as queries, updates, inserts, or deletes.
- A transaction has the following properties: **atomicity**, **consistency**, **isolation**, and **durability** (ACID).
- **Atomicity** means that either all the operations of a transaction are executed or none of them are. A transaction is treated as a single unit and cannot be divided into parts.
- **Consistency** means that a transaction preserves the integrity constraints of the database. A transaction cannot leave the database in an inconsistent state.
- **Isolation** means that a transaction is executed as if it is the only one running in the system. A transaction cannot see the intermediate results of other transactions.
- **Durability** means that the effects of a transaction are permanent and will not be lost in case of a system failure. A transaction is recorded in a persistent storage device before it is committed.
- A **concurrency control** mechanism is a set of rules and techniques that ensure the correct execution of concurrent transactions in a database system. Concurrency control prevents data inconsistency and ensures serializability, recoverability, and deadlock-freedom of transactions.
- **Serializability** is the property that the concurrent execution of a set of transactions is equivalent to some serial execution of the same transactions. A serial execution is one in which transactions are executed one after another, without any overlap.
- **Recoverability** is the property that a transaction can be undone in case of a failure or an abort. A transaction is recoverable if it does not commit before all the transactions that it depends on have committed.
- **Deadlock-freedom** is the property that a set of transactions will not enter a state in which they are waiting for each other to release some resources. A deadlock is a situation in which two or more transactions are blocked indefinitely, each holding a resource that the other needs.
- Some common concurrency control techniques are: **locking**, **timestamping**, **validation**, and **multiversion**.
- **Locking** is a technique that uses locks to control the access of transactions to data items. A lock is a variable that indicates the status of a data item with respect to possible operations that can be applied to it. There are two types of locks: **shared** and **exclusive**. A shared lock allows a transaction to read a data item, but not to modify it. An exclusive lock allows a transaction to both read and write a data item. A lock manager is a component of the database system that grants, denies, and releases locks according to a locking protocol.
- **Timestamping** is a technique that uses timestamps to order the transactions and to determine their precedence. A timestamp is a unique identifier that indicates the logical time at which a transaction is started. A timestamp manager is a component of the database system that assigns timestamps to transactions and data items. A timestamping protocol is a set of rules that determines how transactions are executed based on their timestamps.
- **Validation** is a technique that uses a validation test to check whether the concurrent execution of a set of transactions is serializable. A validation test is a procedure that compares the read and write sets of transactions to determine if they conflict with each other. A read set is the set of data items that a transaction has read, and a write set is the set of data items that a transaction has written. A validation manager is a component of the database system that performs the validation test and decides whether to commit or abort a transaction.
- **Multiversion** is a technique that uses multiple versions of data items to allow concurrent transactions to access different versions of the same data item. A version is a copy of a data item that reflects its state at a certain point in time. A multiversion manager is a component of the database system that maintains and manages the versions of data items and assigns them to transactions. A multiversion protocol is a set of rules that determines how transactions are executed based on the versions of data items they access.



### Transactions

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the operations in a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction is not affected by the concurrent execution of other transactions.
- Durability means that the effects of a transaction are permanent even in the case of failures.

### Distributed Transactions

- A distributed transaction is a transaction that spans multiple data servers in a distributed database system.
- A distributed transaction consists of a set of subtransactions, each of which is executed by one data server.
- A distributed transaction coordinator is a component that manages the execution of distributed transactions across the data servers.
- A distributed transaction has the same ACID properties as a local transaction, but it also requires coordination and communication among the data servers.

### Distributed Concurrency Control

- Distributed concurrency control is the concurrency control of a system distributed over a computer network.
- Distributed concurrency control provides a mechanism to synchronize distributed transactions in such a way that the ACID properties are not violated by their interleaved execution.
- Distributed concurrency control makes sure that all subtransactions of a set of distributed transactions are serialized identically in all data servers involved.
- Distributed concurrency control can be classified into two categories: centralized and decentralized.
- Centralized concurrency control relies on a single coordinator to manage the locks and timestamps of the data items accessed by the distributed transactions.
- Decentralized concurrency control allows each data server to manage its own locks and timestamps, and uses a distributed algorithm to ensure global consistency.



### Nested transactions

- A nested transaction is a transaction that is composed of subtransactions, each of which may have its own commit or abort point.
- A nested transaction can be used to implement partial rollback, modular programming, and concurrency control in distributed systems.
- A nested transaction has a hierarchical structure, where the top-level transaction is the parent of all subtransactions, and each subtransaction may have its own children.
- A nested transaction can be classified into two types: closed nested transactions and open nested transactions.
  - A closed nested transaction is a transaction that is fully contained within its parent transaction, and its commit or abort depends on the outcome of the parent transaction.
  - An open nested transaction is a transaction that can commit or abort independently of its parent transaction, and may have visible effects on other transactions or the database state.
- A nested transaction can be implemented using different models, such as the following:
  - The flat model, where all subtransactions are treated as a single transaction, and the commit or abort of the top-level transaction determines the fate of all subtransactions.
  - The strict model, where subtransactions can commit or abort only when their parent transaction commits or aborts, and the effects of subtransactions are not visible to other transactions until the top-level transaction commits.
  - The relaxed model, where subtransactions can commit or abort independently of their parent transaction, and the effects of subtransactions are visible to other transactions as soon as they commit.
  - The sagas model, where subtransactions can commit or abort independently of their parent transaction, and the effects of subtransactions are compensated by inverse operations in case of abort.
- A nested transaction can provide the following benefits in distributed systems:
  - It can reduce the communication overhead and the blocking time of distributed transactions, by allowing subtransactions to commit or abort locally without waiting for the global decision of the top-level transaction.
  - It can increase the concurrency and the availability of distributed transactions, by allowing subtransactions to access different data items or servers without conflicting with each other or with other transactions.
  - It can enhance the modularity and the reusability of distributed transactions, by allowing subtransactions to be defined as independent units of work that can be nested within different transactions or executed in parallel.
  - It can support the partial rollback and the recovery of distributed transactions, by allowing subtransactions to undo their effects in case of failure or abort, without affecting the rest of the transaction or the database state.



### Locks for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A lock is a mechanism that allows only one of the innumerable nodes (or processes) to access and modify a resource or data that is being shared commonly to prevent execution of same task twice and also maintain data integrity.
- Locks are designed to enforce a mutual exclusion concurrency control policy, which means that only one node can hold a lock on a resource at a time, and other nodes have to wait until the lock is released before they can access the resource.
- Locks can be classified into different types based on the following criteria  :
  - The granularity of the resource: locks can be applied to a whole database, a table, a page, a record, or a field.
  - The mode of the lock: locks can be either shared or exclusive. A shared lock allows multiple nodes to read the same resource, but prevents any node from writing to it. An exclusive lock allows only one node to read and write the resource, and blocks any other node from accessing it.
  - The duration of the lock: locks can be either long-lived or short-lived. A long-lived lock is held by a node for the entire duration of a transaction, and is released only when the transaction commits or aborts. A short-lived lock is held by a node only for the time it needs to access the resource, and is released as soon as possible.
  - The scope of the lock: locks can be either local or global. A local lock is managed by a single node, and is only valid within that node. A global lock is managed by a distributed lock manager (DLM), and is valid across the whole distributed system.
- Locks can be implemented using different strategies and algorithms, such as   :
  - A wait-and-see strategy: a node that requests a lock waits for a while before retrying, hoping that the lock will be released by then. This strategy is simple, but may cause deadlock, starvation, or livelock.
  - A timeout strategy: a node that requests a lock waits for a specified amount of time before giving up and aborting the transaction. This strategy avoids deadlock, but may cause aborts, retries, or wasted resources.
  - A deadlock detection and resolution strategy: a node that requests a lock sends a message to the DLM, which maintains a wait-for graph of all the nodes and locks in the system. The DLM periodically checks the graph for cycles, which indicate deadlock, and breaks them by aborting one of the transactions involved. This strategy avoids starvation and livelock, but may cause aborts, retries, or overhead.
  - A deadlock prevention strategy: a node that requests a lock follows a predefined protocol that ensures that deadlock cannot occur. For example, a node can use a timestamp-based protocol, where each transaction is assigned a unique timestamp, and a lock request is granted only if the timestamp of the requesting transaction is smaller than the timestamp of any other transaction that holds or waits for the lock. This strategy avoids deadlock, but may cause blocking, aborts, or wasted resources.
  - A quorum-based strategy: a node that requests a lock contacts a subset of nodes (called a quorum) that have a copy of the resource, and obtains a lock from them. A quorum is chosen such that any two quorums have at least one node in common, which ensures consistency. For example, a node can use a majority quorum, where it contacts more than half of the nodes that have a copy of the resource, and obtains a lock from them. This strategy avoids deadlock and blocking, but may cause overhead, latency, or unavailability.



### Optimistic Concurrency Control

- Optimistic concurrency control (OCC) is a concurrency control method applied to transactional systems such as relational database management systems and software transactional memory.
- OCC assumes that multiple transactions can frequently complete without interfering with each other, and avoids locking of data items that can reduce the performance of the system.
- OCC consists of three phases: read, validation and write.
- In the read phase, the transaction reads the data items from the database and performs the necessary computations, but does not update the database.
- In the validation phase, the transaction checks if any of the data items it has read have been modified by other transactions that committed after it started. If so, the transaction is aborted and restarted, otherwise it proceeds to the write phase.
- In the write phase, the transaction updates the database with the new values of the data items it has modified.
- OCC has the advantage of allowing a high degree of concurrency and avoiding deadlocks, but it may incur a high cost of aborting and restarting transactions if conflicts are frequent.
- OCC can be implemented in a centralized or distributed manner, depending on the architecture of the system.
- In a centralized system, there is a single validation server that maintains the versions of the data items and validates the transactions before they commit.
- In a distributed system, there are multiple validation servers that communicate with each other to ensure the consistency of the data items and the correctness of the transactions.
- A distributed OCC protocol may use different strategies to reduce the number of restarts, such as acquiring locks, using timestamps, or applying voting mechanisms.



### Timestamp ordering

- Timestamp ordering is a technique for ensuring serializability of transactions in a distributed system.
- A transaction is a sequence of operations that must be executed atomically, i.e., either all or none of them are performed.
- Serializability means that the concurrent execution of transactions produces the same result as some sequential execution of them.
- Timestamp ordering assigns a unique timestamp to each transaction when it starts, and uses these timestamps to order the operations of different transactions.
- The timestamp of a transaction reflects its logical start time, not the physical time on the node where it executes.
- Timestamp ordering can be implemented using logical clocks, such as Lamport timestamps, or physical clocks, such as synchronized clocks.
- Logical clocks are based on the causal ordering of events in the system, i.e., if event A happens before event B, then the timestamp of A is less than the timestamp of B.
- Physical clocks are based on the real time of the nodes, and require some synchronization mechanism to ensure that they do not drift too much.
- Timestamp ordering can be applied to different granularities of data, such as records, pages, or objects.
- Timestamp ordering can be enforced by different protocols, such as basic timestamp ordering, optimistic timestamp ordering, or multiversion timestamp ordering.
- Basic timestamp ordering checks the timestamps of transactions before reading or writing data, and aborts any transaction that violates the order.
- Optimistic timestamp ordering allows transactions to execute without checking timestamps, but validates them at the end and aborts any transaction that conflicts with the order.
- Multiversion timestamp ordering maintains multiple versions of data, and assigns timestamps to each version. Transactions can read the latest version that is compatible with their timestamp, and write new versions with their timestamp.



### Comparison of methods for concurrency control

Concurrency control is the process of managing the concurrent access and modification of shared data in a distributed system, such that the consistency and correctness of the data and the system are preserved. Concurrency control methods can be classified into two main categories: pessimistic and optimistic.

- Pessimistic methods prevent conflicts from occurring by using locks, timestamps, or other mechanisms to coordinate the access and modification of data by concurrent transactions. Pessimistic methods ensure serializability, which means that the outcome of concurrent transactions is equivalent to some serial execution of them. However, pessimistic methods may incur high overhead, blocking, deadlock, and reduced concurrency.

- Optimistic methods allow conflicts to occur and then detect and resolve them by using validation, versioning, or other mechanisms to verify the correctness of concurrent transactions. Optimistic methods do not ensure serializability, but rather weaker consistency criteria, such as snapshot isolation or causal consistency. However, optimistic methods may reduce overhead, blocking, deadlock, and increase concurrency.

Some examples of concurrency control methods are:

- Two-phase locking (2PL): A pessimistic method that uses locks to grant exclusive or shared access to data items by transactions. A transaction must acquire all the locks it needs before releasing any lock, and it must release all the locks after committing or aborting. 2PL ensures serializability and strictness, but it may cause blocking and deadlock.

- Timestamp ordering (TO): A pessimistic method that uses timestamps to order the execution of transactions. A transaction is assigned a unique timestamp when it starts, and it must access and modify data items in timestamp order. TO ensures serializability and strictness, but it may cause aborts and restarts.

- Multi-version concurrency control (MVCC): An optimistic method that uses versions to maintain multiple copies of data items, each with a timestamp. A transaction reads the latest committed version of a data item that is older than its timestamp, and it writes a new version of a data item with its timestamp. MVCC ensures snapshot isolation, which means that a transaction sees a consistent snapshot of the database at its start time, and it does not overwrite the changes of other concurrent transactions. However, MVCC may cause write skew, which is a form of inconsistency that occurs when two transactions update different data items based on a common predicate.

- Validation concurrency control (VCC): An optimistic method that uses validation to check the correctness of transactions before committing them. A transaction executes without any coordination with other transactions, and then it validates its read and write sets against the database state. VCC ensures serializability, but it may cause aborts and restarts.



## Unit 9 - Distributed Transactions

- A distributed transaction is a type of transaction that involves two or more network hosts, usually providing transactional resources, such as databases, message queues, file systems, etc.   
- A distributed transaction is coordinated by a transaction manager, which is responsible for creating and managing a global transaction that encompasses all the operations against the transactional resources.   
- A distributed transaction requires the following properties to ensure data consistency and reliability: atomicity, consistency, isolation, and durability (ACID).  
- Atomicity means that either all the operations in a distributed transaction are executed successfully, or none of them are. If any operation fails, the transaction manager should roll back the changes made by the other operations.  
- Consistency means that the distributed transaction should preserve the integrity constraints and business rules of the data. The transaction manager should ensure that the data is in a valid state before and after the transaction.  
- Isolation means that the distributed transaction should not interfere with other concurrent transactions. The transaction manager should prevent the data from being accessed or modified by other transactions until the current transaction is committed or aborted.  
- Durability means that the effects of a committed distributed transaction should be permanent and survive any system failures. The transaction manager should ensure that the data is written to persistent storage and can be recovered if needed.  
- A distributed transaction can be implemented using different protocols, such as two-phase commit (2PC), three-phase commit (3PC), or the saga pattern. Each protocol has its own advantages and disadvantages in terms of performance, availability, and fault tolerance.  
- A distributed transaction can also be classified into different models, such as flat, nested, or multidatabase. Each model has its own characteristics and challenges in terms of concurrency control, deadlock detection, and recovery.  
- A distributed transaction is a complex and costly process that introduces additional overhead and risks to the system. Therefore, it should be used only when necessary and when the benefits outweigh the drawbacks.



### Flat and nested distributed transactions

- A distributed transaction is a transaction that accesses objects managed by multiple servers.
- A distributed transaction must maintain the atomicity property, which means that either all of the servers commit the transaction or all of them abort the transaction.
- There are two ways to structure a distributed transaction: flat or nested.

#### Flat transactions

- A flat transaction has a single begin point and a single end point (commit or abort).
- A flat transaction is usually simple and short-lived, and does not involve any subtransactions.
- A flat transaction can be coordinated by a single server or by a distributed commit protocol, such as the two-phase commit protocol.

#### Nested transactions

- A nested transaction is a transaction that contains other transactions as subtransactions.
- A nested transaction has a hierarchical structure, where the top-level transaction is the parent of all the subtransactions, and the subtransactions can have their own subtransactions as children.
- A nested transaction can be committed or aborted independently of its parent or children, but the final outcome of the top-level transaction depends on the outcomes of all the subtransactions.
- A nested transaction can provide more concurrency, fault tolerance, and modularity than a flat transaction, but it also requires more complex coordination and recovery mechanisms.



### Atomic Commit Protocols for Distributed Transactions

- A distributed transaction is a transaction that involves multiple servers or nodes in a distributed system.
- An atomic commit protocol is a protocol that guarantees the atomicity property of a transaction, which means that either all the operations of the transaction are executed or none of them are.
- Atomicity is important for maintaining the consistency and integrity of the data in a distributed system, especially in the presence of failures or concurrency.
- There are different types of atomic commit protocols, such as two-phase commit (2PC), three-phase commit (3PC), parallel commit, and failure-aware commit.
- Two-phase commit (2PC) is the most widely used atomic commit protocol. It consists of two phases: a prepare phase and a commit phase.
  - In the prepare phase, the coordinator (the node that initiates the transaction) sends a prepare message to all the participants (the nodes that execute the operations of the transaction) and waits for their votes (yes or no).
  - In the commit phase, if the coordinator receives a yes vote from all the participants, it sends a commit message to all of them and commits the transaction. If the coordinator receives a no vote from any participant, or a timeout occurs, it sends an abort message to all the participants and aborts the transaction.
- Two-phase commit (2PC) has some drawbacks, such as blocking, vulnerability to network partitions, and high latency.
  - Blocking means that if the coordinator or any participant fails or becomes unreachable, the other nodes may have to wait indefinitely for its recovery or message, and cannot proceed with other transactions.
  - Vulnerability to network partitions means that if the network is split into two or more disconnected components, the nodes in different components may have inconsistent views of the transaction outcome, and may commit or abort the transaction independently, violating the atomicity property.
  - High latency means that the transaction has to wait for two round-trips of messages between the coordinator and the participants, which may be costly in a large-scale or geographically distributed system.
- Three-phase commit (3PC) is an extension of two-phase commit (2PC) that aims to overcome the blocking problem. It consists of three phases: a prepare phase, a pre-commit phase, and a commit phase.
  - In the prepare phase, the coordinator sends a prepare message to all the participants and waits for their votes (yes or no).
  - In the pre-commit phase, if the coordinator receives a yes vote from all the participants, it sends a pre-commit message to all of them and waits for their acknowledgments. If the coordinator receives a no vote from any participant, or a timeout occurs, it sends an abort message to all the participants and aborts the transaction.
  - In the commit phase, if the coordinator receives an acknowledgment from all the participants, it sends a commit message to all of them and commits the transaction. If the coordinator does not receive an acknowledgment from any participant, or a timeout occurs, it aborts the transaction.
- Three-phase commit (3PC) has some advantages over two-phase commit (2PC), such as non-blocking, resilience to network partitions, and fault tolerance.
  - Non-blocking means that if the coordinator or any participant fails or becomes unreachable, the other nodes can decide the transaction outcome based on their local state and the messages they have received, and can proceed with other transactions.
  - Resilience to network partitions means that if the network is split into two or more disconnected components, the nodes in different components can agree on the same transaction outcome, and can commit or abort the transaction consistently, preserving the atomicity property.
  - Fault tolerance means that the transaction can tolerate up to n/2 failures, where n is the number of nodes involved in the transaction, and still reach a correct and consistent outcome.
- Three-phase commit (3PC) has some drawbacks, such as increased latency, increased message complexity, and increased state complexity.
  - Increased latency means that the transaction has to wait for three round-trips of messages between the coordinator and the participants, which may be more costly than two round-trips in two-phase commit (2PC).
  - Increased message complexity means that the transaction has to exchange more messages between the coordinator and the participants, which may consume more network bandwidth and resources.
  - Increased state complexity means that the transaction has to maintain more states for each node, such as prepared, pre-committed, committed, and aborted, which may increase the memory and storage requirements.
- Parallel commit is a new atomic commit protocol that aims to reduce the latency of transactions to only a single round-trip of distributed consensus.



### Concurrency control in distributed transactions

- Concurrency control is the process of ensuring that multiple transactions can access and modify shared data in a consistent and correct manner, without violating the ACID properties of transactions.
- Distributed transactions are transactions that span multiple data servers that are connected by a network, and may involve data replication, fragmentation, or partitioning .
- Distributed concurrency control provides a mechanism to synchronize distributed transactions in such a way that the ACID properties are not violated by their interleaved execution .
- There are different types of distributed concurrency control algorithms, such as locking-based, timestamp-based, and optimistic algorithms.
- Locking-based algorithms use locks to prevent concurrent transactions from accessing or modifying the same data item. Locks can be exclusive (write lock) or shared (read lock), and can be granted or denied by a lock manager. Locking-based algorithms can be centralized, decentralized, or hierarchical, depending on the location and structure of the lock manager.
- Timestamp-based algorithms use timestamps to order transactions and determine their precedence. Timestamps can be assigned by a global clock, a logical clock, or a hybrid clock. Timestamp-based algorithms can be basic, Thomas' write rule, or multiversion, depending on how they handle read and write operations.
- Optimistic algorithms assume that conflicts among transactions are rare, and allow transactions to execute without any synchronization. However, before committing, transactions have to validate their read and write sets to ensure that they do not conflict with other transactions. If a conflict is detected, the transaction has to abort and restart. Optimistic algorithms can be centralized, decentralized, or distributed, depending on the location and structure of the validation process.
- Some of the challenges and trade-offs of distributed concurrency control are:
  - Maintaining global serializability, which is the property that the concurrent execution of distributed transactions is equivalent to some serial execution of the same transactions .
  - Dealing with network delays, failures, and partitions, which can affect the performance, availability, and consistency of distributed transactions .
  - Balancing between the degree of concurrency, which is the number of transactions that can execute simultaneously, and the degree of synchronization, which is the amount of coordination and communication among transactions .
  - Choosing between pessimistic and optimistic approaches, which have different advantages and disadvantages in terms of blocking, aborting, and validating transactions.



### Distributed Deadlocks

- A distributed deadlock is a situation where a set of processes in a distributed system are waiting for each other to release resources or messages, and none of them can proceed .
- Distributed deadlocks are similar to deadlocks in centralized systems, but they are harder to detect, avoid, and prevent, because there is no single authority that can oversee resource allocation and monitor the state of the system.
- There are different types of distributed deadlocks, depending on the nature of the resources or messages involved:
  - Communication deadlocks: occur when processes are waiting for messages from each other that will never arrive.
  - Resource deadlocks: occur when processes are holding local resources and requesting remote resources that are held by other processes.
  - Hybrid deadlocks: occur when both communication and resource deadlocks are present in the system.
- There are different approaches to handle distributed deadlocks, such as :
  - Prevention: use a global ordering of resources or messages and ensure that processes request them in that order, avoiding circular waits.
  - Avoidance: use a global state information of the system and ensure that processes only request resources or messages that will not lead to unsafe states.
  - Detection: use a global or distributed algorithm to detect cycles in the wait-for graph of the system and resolve them by aborting or restarting some processes.
  - Ignorance: do not attempt to handle distributed deadlocks and rely on timeouts or user intervention to recover from them.



### Transaction recovery for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A distributed transaction is a transaction that spans multiple nodes in a distributed system, such as multiple databases or microservices.
- A distributed transaction must satisfy the ACID properties: atomicity, consistency, isolation, and durability.
- Atomicity means that either all the operations in a transaction are executed or none of them are.
- Consistency means that the transaction preserves the integrity constraints of the database.
- Isolation means that the transaction does not interfere with other concurrent transactions.
- Durability means that the effects of the transaction are permanent and survive failures.
- Transaction recovery is the process of restoring the database to a consistent state after a failure, such as a system crash, a network partition, or a transaction abort.
- Transaction recovery is based on two techniques: logging and checkpointing.
- Logging is the process of recording the changes made by a transaction to the database in a persistent log file.
- Checkpointing is the process of periodically writing the modified pages of the database to the disk, and recording the checkpoint location in the log file.
- There are two types of logging: undo logging and redo logging.
- Undo logging records the old values of the data items before they are modified by a transaction. Undo logging allows to rollback a transaction by restoring the old values from the log.
- Redo logging records the new values of the data items after they are modified by a transaction. Redo logging allows to reapply the changes of a committed transaction from the log in case of a failure.
- There are two types of recovery algorithms: undo/redo recovery and shadow versioning.
- Undo/redo recovery is based on both undo and redo logging. It uses the log file and the checkpoint to determine which transactions need to be undone or redone after a failure.
- Shadow versioning is based on creating a copy of the database before modifying it by a transaction. It uses the copy as a backup in case of a failure, and switches to the modified version only after the transaction commits.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for Unit 10 - Replication.

## Unit 10 - Replication

- Replication is the process of creating and maintaining multiple copies of the same data on different database servers.
- Replication can improve the availability, performance, and scalability of a database system.
- Replication can also provide data redundancy and backup, as well as facilitate data distribution and synchronization across different locations.
- Replication can be classified into different types based on the following criteria:

  - The direction of data flow: unidirectional, bidirectional, or multidirectional.
  - The timing of data transfer: synchronous, asynchronous, or semi-synchronous.
  - The granularity of data transfer: statement-based, row-based, or mixed.
  - The topology of replication: master-slave, master-master, peer-to-peer, or hierarchical.

- Replication can also be categorized into different modes based on the consistency level of the replicated data:

  - Snapshot replication: the data is copied from the source to the target at a specific point in time, and then remains unchanged until the next snapshot is taken.
  - Transactional replication: the data is copied from the source to the target as transactions are committed, and then applied in the same order and with the same atomicity and isolation properties as the source.
  - Merge replication: the data is copied from the source to the target initially, and then changes are tracked and merged periodically or on demand, allowing for updates to occur at both the source and the target.
  - Conflict detection and resolution: replication can encounter conflicts when the same data is updated by different sources or targets, or when the data is corrupted or lost due to network or system failures. Replication can use different methods to detect and resolve conflicts, such as timestamps, version numbers, primary keys, or user-defined rules.



### System model and group communication for replication in distributed systems

- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by passing messages.
- Replication is a technique to improve the availability, reliability, and performance of a distributed system by creating and maintaining multiple copies of data or services across different processes or nodes.
- A system model is a set of assumptions and properties that describe the behavior and characteristics of a distributed system, such as the communication model, the failure model, the timing model, and the security model.
- Group communication is a form of communication between multiple processes in a distributed system that share some common interest or goal, such as replicating data or coordinating actions.
- Group communication can be classified into two types: broadcast communication and multicast communication.
  - Broadcast communication is when a source process sends a message to all other processes in the system, regardless of their interest or membership in a group. Broadcast communication can be used to disseminate information widely and efficiently, such as code or a file.
  - Multicast communication is when a source process sends a message to a subset of processes in the system that belong to a specific group. Multicast communication can be used to implement replication and consistency protocols, such as data updates or consensus.
- Group communication can also be characterized by the reliability and ordering guarantees it provides, such as reliable, atomic, causal, or total order delivery of messages.
  - Reliable delivery means that every message sent by a process is eventually received by all intended recipients, unless the sender or the receiver fails.
  - Atomic delivery means that every message sent by a process is either received by all or none of the intended recipients, and that the sender is notified of the outcome.
  - Causal delivery means that every message sent by a process is received by all intended recipients in the same causal order as they were sent, where causal order is defined by the happens-before relation between events in the system.
  - Total order delivery means that every message sent by a process is received by all intended recipients in the same order, regardless of the causal order or the sender identity.
- Group communication can be implemented using various protocols and algorithms, such as flooding, gossiping, spanning trees, logical clocks, vector clocks, or consensus algorithms. The choice of the protocol depends on the system model, the group size, the network topology, the communication cost, and the desired reliability and ordering guarantees.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of fault-tolerant services for the unit 10 - replication in the subject of distributed system.

### Fault-tolerant services

- A fault-tolerant service is a service that can continue to function correctly even in the presence of faults, such as server crashes, network partitions, or malicious attacks.
- Fault-tolerance is an important property for distributed systems, as they are prone to various kinds of failures and uncertainties.
- Fault-tolerance can be achieved by replicating the service across multiple servers, and coordinating the client interactions with the server replicas.
- Replication can improve the availability, performance, and reliability of the service, but also introduces challenges such as consistency, synchronization, and recovery.

### Replication techniques

- There are two main classes of replication techniques: primary-backup replication and active replication.
- Primary-backup replication: One server acts as the primary, and the others act as backups. The primary executes the client requests and sends updates to the backups. The backups apply the updates in the same order as the primary. If the primary fails, one of the backups takes over as the new primary.
- Active replication: All servers execute the same client requests in the same order, and send replies to the clients. The clients use a majority voting scheme to determine the correct reply. If a server fails, the others can continue to execute the requests.
- Both techniques require a consensus protocol to ensure that the servers agree on the order of the requests and the state of the service.

### Replication challenges

- Consistency: The replicas should provide a consistent view of the service to the clients, regardless of the faults and delays in the system. A common correctness criterion for replicated services is linearizability, which requires that the service appears as a single copy that processes the requests atomically and in real time.
- Synchronization: The replicas should synchronize their state periodically or on demand, to ensure that they are up to date and consistent. Synchronization can be done by state transfer, where one replica sends its entire state to another, or by log exchange, where the replicas exchange the history of the requests they executed.
- Recovery: The replicas should be able to recover from faults and resume normal operation. Recovery can be done by restarting the failed replica and synchronizing it with the others, or by replacing it with a new replica and initializing it with the current state of the service.

### Replication trade-offs

- Replication can improve the availability and performance of the service, but also incurs costs in terms of storage, communication, and computation.
- Replication can also affect the latency and throughput of the service, depending on the replication technique and the network conditions.
- Replication can also introduce complexity and overhead in the design and implementation of the service, as it requires additional mechanisms for coordination, consistency, synchronization, and recovery.
- Replication can also introduce security risks, as it exposes more attack surfaces and requires trust among the replicas.
- Therefore, replication should be used carefully and appropriately, considering the requirements and constraints of the service and the system.



### Highly Available Services

- A highly available service is a service that can provide continuous and reliable operation despite failures or faults in the system.
- Replication is a technique for achieving high availability by creating and maintaining multiple copies of the same data or service on different nodes in a distributed system.
- Replication can improve availability by allowing the system to tolerate node failures, network partitions, or data corruption, as long as a sufficient number of replicas remain accessible and consistent.
- Replication can also improve performance by reducing the load on a single node, increasing the concurrency of operations, and reducing the latency of accessing data or service.
- Replication can be classified into two types: eager replication and lazy replication.
  - Eager replication ensures that all replicas are updated synchronously or atomically whenever a write operation occurs, thus providing strong consistency guarantees.
  - Lazy replication allows replicas to be updated asynchronously or periodically, thus providing weaker consistency guarantees but higher availability and scalability.
- Replication can be implemented at different levels of abstraction, such as data replication, process replication, or service replication.
  - Data replication involves replicating the state or content of a data object, such as a file, a record, or a table, across multiple nodes.
  - Process replication involves replicating the execution or behavior of a process, such as a server, a client, or a component, across multiple nodes.
  - Service replication involves replicating the functionality or interface of a service, such as a web service, a database service, or a messaging service, across multiple nodes.
- Replication can be managed by different protocols or algorithms, such as primary-backup, quorum-based, or consensus-based protocols.
  - Primary-backup protocols assign a primary replica to handle all write operations and propagate them to backup replicas, which handle read operations and take over the primary role in case of failure.
  - Quorum-based protocols require a minimum number of replicas, called a quorum, to agree on each write or read operation, thus ensuring consistency and availability.
  - Consensus-based protocols require all replicas to reach a common agreement on each write operation, thus ensuring strong consistency and fault tolerance.
- Replication can be challenged by various issues, such as replica consistency, replica synchronization, replica placement, replica selection, or replica recovery.
  - Replica consistency refers to the degree of agreement or divergence among replicas regarding the state or content of the data or service.
  - Replica synchronization refers to the process of updating or reconciling replicas to ensure consistency or convergence.
  - Replica placement refers to the decision of where to locate replicas in the network to optimize availability, performance, or cost.
  - Replica selection refers to the decision of which replica to access or update for a given operation to optimize availability, performance, or consistency.
  - Replica recovery refers to the process of restoring or repairing replicas after a failure or a fault to ensure availability and consistency.

: https://hevodata.com/learn/data-replication-in-distributed-system/
: https://techcommunity.microsoft.com/t5/sql-server-blog/replication-enhancement-8211-distribution-database-in/ba-p/385882
: https://raima.com/rdme-high-availability-database/
: https://link.springer.com/chapter/10.1007/978-3-7091-9198-9_4
: https://link.springer.com/article/10.1007/BF01762124
: https://dl.acm.org/doi/10.1145/138873.138877
: https://www.cs.cornell.edu/courses/cs5412/2012sp/lectures/lec25.pdf
: https://www.cs.cmu.edu/~dga/15-440/F10/lectures/15-replication.pdf



### Transactions with replicated data

- Transactions are a sequence of operations that are executed atomically, consistently, isolatedly, and durably (ACID properties) on a database system.
- Replication is the process of copying and maintaining data in multiple locations to improve availability, performance, and fault tolerance of a distributed system.
- Transactions with replicated data involve executing operations on multiple copies of the same data item, while ensuring that the copies remain consistent and synchronized with each other.
- Some of the challenges and trade-offs of transactions with replicated data are:
  - How to propagate updates to all the replicas without causing conflicts or inconsistencies?
  - How to ensure serializability and isolation of concurrent transactions on different replicas?
  - How to handle failures and recoveries of replicas without losing or corrupting data?
  - How to balance the benefits of replication (such as availability, scalability, and locality) with the costs of replication (such as communication, synchronization, and storage overhead)?
- Some of the techniques and protocols for transactions with replicated data are:
  - Primary-copy replication: One replica is designated as the primary copy, which receives all the updates and propagates them to the other replicas (called secondary copies). The primary copy ensures serializability and isolation of transactions, while the secondary copies provide read-only access to the data. This approach simplifies the update propagation and consistency maintenance, but introduces a single point of failure and a bottleneck for write operations.
  - Quorum-based replication: Each replica has a vote on the validity of an update, and a quorum (a majority or a subset) of replicas must agree on the update before it is committed. This approach allows for fault tolerance and load balancing, but requires more communication and coordination among replicas, and may result in lower availability or consistency depending on the quorum size and composition.
  - Optimistic replication: Each replica can update its local copy independently, without waiting for the other replicas to agree. The updates are then reconciled periodically or on demand, using conflict detection and resolution mechanisms. This approach enables high availability and performance, but may incur more storage and computation overhead, and may lead to data divergence or loss if conflicts are not resolved correctly.

