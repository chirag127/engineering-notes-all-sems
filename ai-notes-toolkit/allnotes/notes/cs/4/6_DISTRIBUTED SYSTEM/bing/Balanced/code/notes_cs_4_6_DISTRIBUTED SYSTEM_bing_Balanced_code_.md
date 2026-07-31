

## Unit 1 - Characterization of Distributed Systems

A distributed system is a system in which components located at networked computers communicate and coordinate their actions only by passing messages . The components of a distributed system may be hardware devices, software processes, or a combination of both. The end-users of a distributed system perceive it as a single coherent system that provides a set of services.

Some of the main characteristics of distributed systems are:

- **Resource sharing**: The components of a distributed system can share resources such as hardware, software, or data with other components, regardless of their physical location or access mode . Resource sharing enables efficient utilization of resources, improved performance, and increased availability.
- **Openness**: The components of a distributed system can be easily extended and improved by adding new hardware or software, without affecting the existing functionality or performance of the system . Openness also implies that the system conforms to well-defined standards and interfaces, and that the software is developed and shared in a transparent and collaborative manner.
- **Concurrency**: The components of a distributed system can execute concurrently, without interfering with each other, and can coordinate their actions through message passing . Concurrency enables parallelism, scalability, and fault tolerance in distributed systems.
- **Scalability**: The components of a distributed system can be added or removed dynamically, without affecting the overall behavior or performance of the system . Scalability allows the system to handle increasing or decreasing workloads, and to adapt to changing environmental conditions.
- **Transparency**: The components of a distributed system can hide their internal details and complexities from the end-users and other components, and present a uniform and consistent view of the system . Transparency enables abstraction, modularity, and simplicity in distributed systems.
- **Reliability**: The components of a distributed system can cope with failures of other components, and can recover from errors and faults, without compromising the correctness or availability of the system . Reliability ensures that the system can deliver its services despite the presence of failures.
- **Security**: The components of a distributed system can protect their resources and data from unauthorized access, modification, or disclosure, and can ensure the authenticity, integrity, and confidentiality of the messages exchanged with other components . Security prevents malicious attacks and preserves the trust and privacy of the system.

Some of the main challenges of distributed systems are:

- **Communication**: The components of a distributed system need to communicate with each other through a network, which may introduce delays, errors, or losses of messages, and may vary in bandwidth, latency, or reliability . Communication also requires protocols and mechanisms for addressing, routing, synchronizing, and ordering the messages.
- **Coordination**: The components of a distributed system need to coordinate their actions and decisions, which may depend on the state and behavior of other components, and may involve conflicts or inconsistencies . Coordination also requires algorithms and techniques for consensus, agreement, mutual exclusion, and distributed transactions.
- **Replication**: The components of a distributed system may replicate their resources or data across multiple locations, which may improve availability, performance, or fault tolerance, but may also introduce overhead, complexity, or inconsistency . Replication also requires methods and policies for consistency, coherence, and reconciliation of the replicas.
- **Fault tolerance**: The components of a distributed system may encounter various types of failures, such as crash, omission, timing, or Byzantine failures, which may affect the functionality or performance of the system . Fault tolerance also requires strategies and mechanisms for detection, diagnosis, recovery, and prevention of failures.
- **Security**: The components of a distributed system may face various types of threats, such as eavesdropping, tampering, spoofing, or denial of service, which may compromise the security of the system . Security also requires methods and tools for encryption, authentication, authorization, and auditing of the system.



### Introduction for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- A distributed system has the following characteristics:
  - Concurrency: The components of the system can execute simultaneously and independently.
  - No global clock: The components of the system do not share a common notion of time or a global clock.
  - Independent failures: The components of the system can fail independently and recover from failures without affecting the rest of the system.
- A distributed system has the following advantages:
  - Resource sharing: The system can share resources such as data, files, devices, services, etc. among the components and the users.
  - Scalability: The system can grow or shrink in size and performance by adding or removing components without affecting the overall functionality.
  - Fault tolerance: The system can tolerate and mask failures of some components and continue to provide services to the users.
  - Transparency: The system can hide the details of its internal structure and operation from the users and provide a uniform interface and behavior.
- A distributed system has the following challenges:
  - Heterogeneity: The system has to deal with the diversity of hardware, software, network, data, and user interfaces among the components.
  - Security: The system has to protect the confidentiality, integrity, and availability of the resources and the communication among the components and the users.
  - Coordination: The system has to coordinate the actions and interactions of the components to achieve a common goal or provide a consistent service.
  - Consistency: The system has to maintain a consistent view of the state and the behavior of the components and the resources among the users and the components.
  - Performance: The system has to optimize the utilization of the resources and the communication among the components and the users to achieve high efficiency and quality of service.



### Examples of distributed systems

A distributed system is a collection of independent computers that communicate and coordinate their actions by passing messages. The computers in a distributed system may be physically close or geographically dispersed, and they may be connected by a network or a bus. Distributed systems can provide higher performance, reliability, scalability, and availability than centralized systems.

Some examples of distributed systems are:

- **Telecommunication networks**: Telephone networks are an early example of a peer-to-peer network, where each node can initiate or receive calls. Cellular and telephone networks are forms and examples of distributed networks. They use protocols such as TCP/IP, HTTP, and SMTP to exchange data and messages.  
- **Real-time systems**: Many industries use real-time systems distributed in various areas, locally and globally. For example, air traffic control systems, power grid systems, industrial control systems, and online gaming systems are all examples of real-time distributed systems. They require fast and accurate communication and synchronization among the components.  
- **Distributed database systems**: A distributed database has locations across multiple servers, physical locations, or both. The data can be replicated or partitioned to improve performance, availability, and fault tolerance. Examples of distributed database systems are Google's Bigtable, Amazon's Dynamo, and MongoDB.  
- **Distributed computing systems**: A distributed computing system is a system that uses the idle resources of many computers to perform a large-scale computation or task. Examples of distributed computing systems are the SETI@home project, which searches for extraterrestrial intelligence, and the Folding@home project, which simulates protein folding.  
- **Content delivery networks**: A content delivery network (CDN) is a system that distributes web content to users based on their geographic location, network conditions, and content origin. A CDN consists of a network of servers that cache and deliver web pages, images, videos, and other content to users. Examples of CDNs are Akamai, Cloudflare, and Amazon CloudFront.



```
# Resource sharing for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Resource sharing is one of the main goals and benefits of distributed systems.
- Resource sharing means that the users and applications can access and use the resources (such as data, files, devices, services, etc.) that are available in the distributed system, regardless of their physical location and ownership.
- Resource sharing can improve the performance, reliability, scalability, and availability of the distributed system, as well as reduce the cost and complexity of managing the resources.
- Resource sharing can be achieved by different methods, such as:
  - File sharing: the users and applications can access and manipulate the files that are stored on remote file servers, using a common file system interface and protocol (such as NFS, CIFS, etc.).
  - Data sharing: the users and applications can access and query the data that are stored on remote databases, using a common data model and language (such as SQL, NoSQL, etc.).
  - Device sharing: the users and applications can access and use the devices (such as printers, scanners, cameras, etc.) that are connected to the distributed system, using a common device driver and protocol (such as USB, Bluetooth, etc.).
  - Service sharing: the users and applications can access and invoke the services (such as web services, cloud services, etc.) that are provided by remote servers, using a common service interface and protocol (such as SOAP, REST, etc.).
- Resource sharing can also be classified into two types, depending on the degree of transparency and coordination among the resource providers and consumers:
  - Unstructured resource sharing: the resource providers and consumers are loosely coupled and do not have a global view or control of the distributed system. The resource discovery and allocation are based on local information and decisions. Examples of unstructured resource sharing are peer-to-peer systems, ad hoc networks, etc.
  - Structured resource sharing: the resource providers and consumers are tightly coupled and have a global view or control of the distributed system. The resource discovery and allocation are based on global information and decisions. Examples of structured resource sharing are grid systems, cloud systems, etc.
```



### The Web Challenges for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- The web is an example of a distributed system that allows resource sharing and communication among different devices across the internet.
- However, developing and maintaining a distributed system poses many challenges, such as  :
  - Scalability: The ability to handle increasing load and demand without degrading the performance or functionality of the system.
  - Heterogeneity: The ability to communicate and interoperate with different devices, platforms, languages, and protocols.
  - Security: The ability to protect the system and its data from unauthorized access, modification, or denial of service.
  - Fault tolerance: The ability to cope with failures of components or links without compromising the correctness or availability of the system.
  - Consistency: The ability to ensure that all the components of the system have a coherent and up-to-date view of the system state and data.
  - Transparency: The ability to hide the complexity and diversity of the system from the users and applications.
- These challenges require careful design and implementation of distributed algorithms, protocols, and architectures that can balance the trade-offs and requirements of different scenarios and applications  .



### Architectural models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Architectural models are system models that describe the organization of components across the network and their interrelationship.
- Architectural models can help to understand the trade-offs and challenges of distributed systems, such as scalability, performance, reliability, security, and consistency.
- Some common architectural models for distributed systems are:

  - Client-server architecture: A model where one or more servers provide services to multiple clients that request and consume them. The servers and clients can be distributed across different machines and communicate over a network. This model forms the base for multi-tier architectures, where different layers of servers provide different functionalities, such as presentation, application, and data.
  - Broker architecture: A model where a broker component acts as an intermediary between clients and servers, hiding the details of communication and location from both parties. The broker can provide services such as naming, routing, load balancing, security, and fault tolerance. An example of a broker architecture is the Common Object Request Broker Architecture (CORBA), which allows objects written in different languages and running on different platforms to interact.
  - Service-oriented architecture (SOA): A model where services are loosely coupled and can be composed and reused to create complex applications. Services are self-contained, self-describing, and platform-independent units of functionality that communicate using standard protocols, such as SOAP or REST. An example of a service-oriented architecture is the web, where web services can be accessed through URLs and exchanged using XML or JSON.
  - Peer-to-peer architecture: A model where nodes in the network act as both clients and servers, sharing resources and collaborating without a central authority. Peer-to-peer architectures can be classified into structured and unstructured, depending on how the nodes are organized and how they locate each other. An example of a peer-to-peer architecture is BitTorrent, which allows users to download and upload files in a distributed manner.
  - Distributed ledger architecture: A model where a shared and synchronized database is maintained by a network of nodes that follow a consensus protocol to validate transactions and prevent double-spending. Distributed ledgers can be public or private, depending on who can access and participate in the network. An example of a distributed ledger architecture is blockchain, which underlies cryptocurrencies such as Bitcoin and Ethereum.

: https://www.thecode11.com/2022/06/architectural-model-in-distributed-system.html
: https://www.se.rit.edu/~se442/slides/class/02-SystemModels-Architecture.pdf
: https://www.tutorialspoint.com/software_architecture_design/distributed_architecture.htm
: https://www.techtarget.com/searchnetworking/tip/A-guide-to-distributed-network-architectures



### Fundamental Models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Fundamental models are descriptions of properties that are present in all distributed architectures  .
- They help us understand the characteristics, challenges and trade-offs of designing and implementing distributed systems.
- There are three main types of fundamental models: interaction models, failure models and security models  .

#### Interaction Models
- Interaction models deal with the issues of communication and coordination among processes in a distributed system  .
- They include aspects such as performance, timing, ordering, synchronization and consistency of events and data  .
- Some examples of interaction models are:
  - Synchronous vs. asynchronous communication: whether the sender and receiver of a message have to wait for each other or not  .
  - Remote procedure call (RPC) vs. message passing: whether the communication is based on invoking a procedure on a remote machine or sending a message to a destination  .
  - Client-server vs. peer-to-peer: whether the communication is based on a centralized or decentralized architecture  .
  - Publish-subscribe vs. message queue: whether the communication is based on a topic or a queue  .

#### Failure Models
- Failure models specify the types of faults that can occur in a distributed system and how they can be detected and handled  .
- They include aspects such as availability, reliability, fault tolerance and recovery  .
- Some examples of failure models are:
  - Crash vs. omission vs. arbitrary failures: whether a process stops working, misses some messages or behaves unpredictably  .
  - Fail-stop vs. fail-silent vs. fail-noisy: whether a process can notify others of its failure, remains silent or sends incorrect messages  .
  - Byzantine vs. non-Byzantine failures: whether a process can lie or cheat or not  .
  - Transient vs. intermittent vs. permanent failures: whether a failure is temporary, recurring or lasting  .

#### Security Models
- Security models specify the types of threats that can compromise the confidentiality, integrity and availability of a distributed system and how they can be prevented and mitigated  .
- They include aspects such as authentication, authorization, encryption, digital signatures and firewalls  .
- Some examples of security models are:
  - Symmetric vs. asymmetric cryptography: whether the same or different keys are used for encryption and decryption  .
  - Kerberos vs. public key infrastructure (PKI): whether the authentication is based on a trusted third party or a network of certificates  .
  - Access control list (ACL) vs. role-based access control (RBAC): whether the authorization is based on individual or group permissions  .
  - Intrusion detection system (IDS) vs. intrusion prevention system (IPS): whether the system can only detect or also prevent attacks  .



### Theoretical Foundation for Distributed System

A distributed system is a collection of processes that are spatially separated and do not share a common memory and communicate with one another by exchanging messages with arbitrary delays . Some of the theoretical foundations for distributed systems are:

- **Limitations of distributed systems**: Due to the lack of a global clock, shared memory, and reliable communication, distributed systems face some inherent challenges such as synchronization, coordination, consistency, fault-tolerance, and scalability .
- **Logical clocks**: Logical clocks are a way of ordering events in a distributed system based on their causal relationships, rather than their physical timestamps. Logical clocks can be implemented using different algorithms, such as Lamport's logical clocks and vector clocks .
- **Concepts in message passing systems**: Message passing systems are a model of communication in distributed systems, where processes send and receive messages to each other. Some of the concepts in message passing systems are: message types, message ordering, message delivery, message buffering, message acknowledgement, and message passing primitives .
- **Distributed algorithms**: Distributed algorithms are algorithms that run on multiple processes in a distributed system and coordinate their actions to achieve a common goal. Some examples of distributed algorithms are: leader election, mutual exclusion, consensus, broadcast, multicast, and distributed snapshots .
- **Distributed information systems**: Distributed information systems are systems that store, process, and disseminate information across multiple nodes in a distributed system. Some of the challenges and opportunities of distributed information systems are: data replication, data consistency, data partitioning, data querying, data mining, and data privacy.



### Limitation of Distributed system

A distributed system is a system that consists of multiple independent components that communicate with each other over a network. Distributed systems have many advantages, such as scalability, fault-tolerance, availability, and performance. However, they also face some limitations that make them challenging to design and implement. Some of the main limitations of distributed systems are:

- **Absence of a global state**: In a distributed system, there is no single point of control or coordination for the entire system. Each component has its own local state and view of the system, which may differ from the views of other components. This makes it difficult to reason about the behavior and correctness of the system, especially in the presence of concurrency, failures, and network delays. To cope with this limitation, distributed systems often use techniques such as consensus algorithms, distributed transactions, and replication protocols to achieve some form of consistency and agreement among the components.

- **Absence of a global clock**: In a distributed system, there is no common notion of time or ordering of events across the components. Each component has its own local clock, which may not be synchronized with the clocks of other components. This makes it hard to measure and compare the timestamps and durations of events that occur in different parts of the system. To cope with this limitation, distributed systems often use techniques such as logical clocks, vector clocks, and Lamport timestamps to establish a partial or causal order of events.

- **Absence of shared memory**: In a distributed system, there is no shared memory or storage that can be accessed by all the components. Each component has its own local memory or storage, which may not be consistent or coherent with the memory or storage of other components. This makes it challenging to share and update data among the components, especially in the presence of concurrency, failures, and network partitions. To cope with this limitation, distributed systems often use techniques such as message passing, distributed hash tables, and eventual consistency to exchange and synchronize data.

- **Network issues**: In a distributed system, the network is a critical and unreliable component that connects the components. The network may experience various issues, such as latency, bandwidth, congestion, packet loss, duplication, reordering, and partitioning. These issues can affect the performance, availability, and correctness of the system, especially in the presence of failures and concurrency. To cope with this limitation, distributed systems often use techniques such as timeouts, retries, acknowledgments, and fault-tolerance protocols to handle and recover from network failures.



### Absence of Global Clock

- A global clock is a system-wide clock that is equally accessible to all processes in a distributed system and provides a common notion of time.
- A global clock is useful for determining the order of events and the state of the system across different processes.
- However, a global clock is hard to realize in distributed systems due to two inherent limitations: lack of shared memory and unpredictable message delays.
- Lack of shared memory means that processes in a distributed system do not have access to a common storage that can store and update the global clock value.
- Unpredictable message delays mean that the communication channel between processes is unreliable and the transmission time of messages is variable and unknown.
- Therefore, the absence of a global clock implies that:
  - Different processes may have different local clocks that are not synchronized and may drift apart over time.
  - It is not always possible to determine the exact order of events that occur on different processes, especially if they are concurrent or causally unrelated.
  - It is not possible for an individual process to obtain an up-to-date and consistent state of the entire system, since the state information may be outdated or inconsistent due to message delays.
  - Obtaining a meaningful state of the system, in which the states of different processes are consistent with each other, is difficult and requires special algorithms and protocols.



### Shared Memory

Shared memory is a memory architecture where physically separated memories can be addressed as a single shared address space. It allows multiple processes to access and modify the same data without explicit message passing.

Shared memory can be implemented in two ways:

- **Physical shared memory**: The memory is physically shared among multiple processors or nodes. This requires hardware support such as cache coherence circuits and network interface controllers. Examples of physical shared memory systems are symmetric multiprocessors (SMPs) and non-uniform memory access (NUMA) machines.
- **Distributed shared memory (DSM)**: The memory is physically distributed among multiple processors or nodes, but it is logically shared by using software techniques. The DSM system manages the memory across all the nodes and provides a virtual address space that is shared by all the nodes. The data moves between the main memories of different nodes as needed. Examples of DSM systems are Ivy, Munin, and TreadMarks.

The advantages of shared memory are:

- It simplifies the programming model by providing a single address space and a familiar memory abstraction.
- It allows the programmers to handle synchronizations in the familiar shared memory model using locks, semaphores, or monitors.
- It can improve the performance by reducing the communication overhead and exploiting the locality of data access.

The disadvantages of shared memory are:

- It can introduce consistency and coherence issues due to concurrent access and modification of the same data by multiple processes.
- It can increase the complexity of the system by requiring hardware or software mechanisms to maintain the consistency and coherence of the shared memory.
- It can limit the scalability of the system by imposing a fixed size of the shared memory or increasing the communication cost as the number of nodes increases.



### Logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A logical clock is a mechanism for capturing chronological and causal relationships in a distributed system  .
- A distributed system may have no physically synchronous global clock, so a logical clock allows global ordering on events from different processes in such systems .
- A logical clock is not a physical device, but a software counter that is incremented according to some rules .
- A logical clock can be used for computation analysis, distributed algorithm design, individual event tracking, and exploring computational progress.
- There are different types of logical clocks, such as Lamport timestamps, vector clocks, matrix clocks, etc., each with different properties and applications  .
- A logical clock must satisfy the following property: if event A causally precedes event B, then the logical clock value of A must be less than the logical clock value of B .
- A logical clock does not necessarily reflect the real time or the physical order of events, but only the logical order and causality  .



### Lamport's logical clocks

- Lamport's logical clocks are a way of ordering events in a distributed system without relying on physical clocks.
- They are based on the idea of a "happens-before" relation, denoted by `->`, which means that one event causally affects another.
- For example, if a process sends a message to another process, then the send event happens before the receive event.
- Lamport's logical clocks assign a numerical value, called a timestamp, to each event in a process.
- The timestamp reflects the order of events within a process and across processes that communicate with each other.
- The rules for assigning timestamps are:

  - Each process maintains a counter, initialized to zero, that is incremented before each event in the process.
  - The timestamp of an event is the value of the counter when the event occurs.
  - When a process sends a message, it attaches its current timestamp to the message.
  - When a process receives a message, it updates its counter to be the maximum of its own counter and the timestamp in the message, plus one.

- The timestamps can be used to compare the order of events in a distributed system.
- If `a` and `b` are events in the same process, then `a -> b` if and only if the timestamp of `a` is less than the timestamp of `b`.
- If `a` is the send event of a message and `b` is the receive event of the same message, then `a -> b`.
- If `a -> b` and `b -> c`, then `a -> c`.
- If `a` and `b` are events in different processes that do not communicate with each other, then they are concurrent, denoted by `a || b`, and their timestamps cannot be compared.



### Concepts in Message Passing Systems

- Message passing is a technique for invoking behavior on a computer by sending and receiving messages over a communication channel.
- Message passing systems provide a collection of message-based inter-process communication (IPC) protocols that hide the complexities of network protocols and heterogeneous platforms.
- Message passing can be used for two forms of IPC in distributed systems: local communication and distant communication.
- Local communication occurs when the communicating processes are located on the same node, and distant communication occurs when the processes are distributed among multiple nodes.
- Message passing can be synchronous or asynchronous, depending on the timing model of the system.
- Synchronous message passing assumes that there is a known bound on the message transmission time and the process execution time, and that the processes are synchronized by a global clock.
- Asynchronous message passing does not make any assumptions about the message transmission time and the process execution time, and that the processes are not synchronized by a global clock.
- Message passing can be unicast, multicast, or broadcast, depending on the number of recipients of the message.
- Unicast message passing sends a message to a single destination, multicast message passing sends a message to a subset of destinations, and broadcast message passing sends a message to all destinations.
- Message passing can be reliable or unreliable, depending on the guarantees of the message delivery.
- Reliable message passing ensures that every message sent by a process is eventually received by the intended recipient, and that the messages are received in the same order as they were sent.
- Unreliable message passing does not provide any guarantees of the message delivery, and that the messages may be lost, duplicated, or reordered.
- Message passing can be blocking or non-blocking, depending on the behavior of the sender and the receiver.
- Blocking message passing requires the sender to wait until the message is received by the destination, and the receiver to wait until a message is available from the source.
- Non-blocking message passing allows the sender to continue without waiting for the message delivery, and the receiver to check for the availability of a message without waiting.
- Message passing can be implemented using various methods, such as sockets, message queues, remote procedure calls, remote method invocation, publish-subscribe systems, etc  .



### Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- Causal order is a way of defining the logical precedence of events in a distributed system, based on the potential causal influence between them.
- Causal order is important for ensuring the consistency and correctness of distributed applications, such as collaborative editing, chat systems, distributed databases, etc.
- Causal order is weaker than total order, which imposes a single linear sequence of all events in the system, even those that are concurrent. Causal order allows more concurrency and scalability, but also more complexity and ambiguity.
- Causal order can be defined formally using Lamport's happened-before relation: an event a happens before an event b (denoted as a -> b) if one of the following conditions holds :
  - a and b are events in the same process, and a occurs before b in the local clock order.
  - a is the sending of a message by one process, and b is the receipt of the same message by another process.
  - there exists some event c such that a -> c and c -> b (transitivity).
- Causal order can be implemented using various algorithms, such as vector clocks, causal broadcast, causal memory, etc . These algorithms typically require some form of metadata or communication overhead to track the causal dependencies among events.



### Total order for the notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent entities that communicate by message passing and coordinate their actions to achieve a common goal.
- Events are occurrences that happen at a specific point in time and space in a distributed system, such as sending or receiving a message, or executing a local operation.
- The order of events is important for understanding the behavior and correctness of a distributed system, especially when there are concurrent or conflicting events.
- A partial order is a binary relation that satisfies three properties: reflexivity, antisymmetry, and transitivity. A partial order can be represented by a directed acyclic graph (DAG), where nodes are events and edges are order relations.
- A total order is a partial order that additionally satisfies the property of totality, which means that any two events are comparable, i.e., either one happens before the other, or they are the same event. A total order can be represented by a linear sequence of events.
- A distributed system is said to have partial order if we can have a partial order relationship among the events in the system. If totality, i.e., causal relationship among all events in the system, can be established, then the system is said to have total order .
- Total order is useful for ensuring consistency, agreement, and fault tolerance in distributed systems, as it allows all processes to observe the same events in the same order.
- Total order can be achieved by using various algorithms or protocols, such as Lamport timestamps, vector clocks, logical clocks, or atomic broadcast  .
- Lamport timestamps are scalar values that are assigned to each event by the process that generates it, based on the local clock and the messages received from other processes. Lamport timestamps can be used to create a total order of events in a distributed system by using some arbitrary mechanism to break ties (e.g. the ID of the process).
- Vector clocks are arrays of values that are assigned to each event by the process that generates it, based on the local clock and the vector clocks received from other processes. Vector clocks can capture the causal order of events in a distributed system, but not the total order, as they may not be comparable for concurrent events.
- Logical clocks are abstract mechanisms that assign logical time values to events, such that the order of events is consistent with the causal order. Logical clocks can be implemented using Lamport timestamps, vector clocks, or other methods.
- Atomic broadcast is a communication primitive that guarantees that all processes in a distributed system receive the same set of messages in the same order, even in the presence of failures. Atomic broadcast can be used to implement a total order of events in a distributed system, as it ensures that all processes observe the same events in the same order.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is some information on the topic of total causal order for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM.

### Total Causal Order

- A distributed system is a collection of independent processes that communicate by exchanging messages over a network.
- A distributed system is said to have partial order if we can have a partial order relationship among the events in the system. An event is something that happens at a single point in time and space, such as sending or receiving a message, or performing a local computation. A partial order relationship is a binary relation that is reflexive, antisymmetric, and transitive. For example, if event A happens before event B, and event B happens before event C, then event A happens before event C. This is denoted as A -> B -> C.
- A partial order relationship among events can be established by using logical clocks, which are counters that are incremented by each process whenever an event occurs, and are attached to each message sent. A logical clock can capture the causal dependency between events, such that if A -> B, then the logical clock of A is less than the logical clock of B. This is called the happened-before relation, or causal order.
- If ‘totality’, i.e., causal relationship among all events in the system, can be established, then the system is said to have total order. This means that there is a single linearization, consistent with the causal order, among all the events that occur in the system, even those that occur concurrently. For example, if A and B are concurrent events, i.e., neither A -> B nor B -> A, then we can arbitrarily assign A < B or B < A, as long as all processes agree on the same order. This is called the total order relation, or total causal order.
- Total causal order is the strictest ordering in distributed systems; it establishes a global view of the system state and the order of events, regardless of the physical time or the network delays. For that reason, the execution of the system is considered as synchronous.
- Total causal order can be implemented by using a total order broadcast, which is a communication primitive that guarantees that all processes deliver the same set of messages in the same order. A total order broadcast can be achieved by using a sequencer, which is a special process that assigns a sequence number to each message and broadcasts it to all processes. The processes then deliver the messages according to the sequence numbers. Alternatively, a total order broadcast can be achieved by using a consensus algorithm, which is a distributed protocol that allows all processes to agree on a common value, such as the order of messages. A consensus algorithm can be based on rounds of voting, or on a leader election, or on a quorum system.



### Techniques for Message Ordering in Distributed Systems

Message ordering is the problem of ensuring that messages sent by different processes in a distributed system are received and processed in a consistent and predictable way. Message ordering is important for achieving correctness, consistency, and coordination in distributed systems.

There are different types of message ordering techniques, depending on the desired properties and guarantees of the communication. Some of the common techniques are:

- **Unordered**: This is the simplest and most basic technique, where messages are delivered in any order, without any guarantee of preserving the order of sending or causality. This technique is suitable for applications that do not depend on the order of messages, such as broadcasting information or notifications.

- **FIFO**: This technique ensures that messages sent by the same process are delivered in the same order as they were sent, but messages from different processes may be delivered in any order. This technique is useful for applications that require sequential consistency, such as implementing a queue or a stack.

- **Causal**: This technique ensures that messages that are causally related are delivered in the same order as they were sent, but messages that are not causally related may be delivered in any order. Causality is defined by the happens-before relation, which captures the logical order of events in a distributed system. This technique is useful for applications that require causal consistency, such as implementing a shared memory or a bulletin board.

- **Total**: This technique ensures that messages are delivered in the same order to all processes, regardless of the order of sending or causality. This technique is useful for applications that require strong consistency, such as implementing a distributed database or a consensus protocol.

- **Synchronous**: This technique ensures that messages are delivered in the same order to all processes, and that the order is agreed upon by all processes before delivering any message. This technique is useful for applications that require atomicity, such as implementing a distributed transaction or a distributed lock.

Each of these techniques has different trade-offs in terms of complexity, overhead, and performance. Some of the common protocols that implement these techniques are:

- **Unicast**: This is a protocol that sends a message from one process to another, without any ordering guarantee. This protocol is simple and efficient, but does not provide any consistency or coordination.

- **Broadcast**: This is a protocol that sends a message from one process to all other processes, without any ordering guarantee. This protocol is useful for disseminating information or notifications, but does not provide any consistency or coordination.

- **Multicast**: This is a protocol that sends a message from one process to a subset of processes, without any ordering guarantee. This protocol is useful for communicating with a group of processes, but does not provide any consistency or coordination.

- **Reliable broadcast**: This is a protocol that sends a message from one process to all other processes, with the guarantee that the message is delivered to all processes or none. This protocol is useful for ensuring reliability, but does not provide any ordering guarantee.

- **FIFO broadcast**: This is a protocol that sends a message from one process to all other processes, with the guarantee that messages from the same process are delivered in FIFO order. This protocol is useful for ensuring sequential consistency, but does not provide any causal or total ordering guarantee.

- **Causal broadcast**: This is a protocol that sends a message from one process to all other processes, with the guarantee that messages that are causally related are delivered in causal order. This protocol is useful for ensuring causal consistency, but does not provide any total or synchronous ordering guarantee.

- **Total order broadcast**: This is a protocol that sends a message from one process to all other processes, with the guarantee that messages are delivered in the same order to all processes. This protocol is useful for ensuring strong consistency, but does not provide any synchronous ordering guarantee.

- **Synchronous order broadcast**: This is a protocol that sends a message from one process to all other processes, with the guarantee that messages are delivered in the same order to all processes, and that the order is agreed upon by all processes before delivering any message. This protocol is useful for ensuring atomicity, but is complex and costly to implement.



### Causal ordering of messages

- Causal ordering of messages is a partial ordering of messages in a distributed computing environment .
- It places a restriction on communication between processes by requiring that if the transmission of message mi to process pk necessarily preceded the transmission of message mj to the same process, then the delivery of these messages to that process must be ordered such that mi is delivered before mj.
- Causal ordering of messages is one of the four semantics of multicast communication, namely unordered, totally ordered, causal, and sync-ordered communication.
- Multicast communication methods vary according to the message’s reliability guarantee and ordering guarantee.
- Causal ordering of messages is useful for applications that need to preserve the logical dependencies between events in a distributed system.
- Causal ordering of messages can be implemented by using vector clocks, which are arrays of logical clocks that keep track of the causal relationships between processes .
- Vector clocks are updated and piggybacked on every message sent and received by a process .
- A process can deliver a message only if its vector clock is not ahead of the vector clock of the message in any component .
- Causal ordering of messages ensures that the messages are delivered in a consistent and meaningful order, but it does not guarantee global synchronization or agreement among processes .



### Global State

- A global state of a distributed system is a collection of the local states of the processes and the channels involved in the system   .
- A local state of a process is the values of its variables and its program counter at a given point in time.
- A local state of a channel is the sequence of messages that have been sent but not yet received along that channel.
- A global state can be represented by a cut, which is a set of events, one per process, such that no event in the cut is causally dependent on an event outside the cut.
- A cut is consistent if it contains no message that is received but not sent. A consistent cut represents a possible global state that could have occurred during the execution of the system.
- A global state is correct if it is computed along a consistent cut.
- Determining the global state of a distributed system is useful for debugging, monitoring, checkpointing, rollback-recovery, and termination detection.
- There are different algorithms for recording the global state of a distributed system, such as the Chandy-Lamport algorithm, the Lai-Yang algorithm, and the Mattern algorithm. These algorithms are based on sending and receiving special messages called markers to capture the local states and the channel states.
- The challenges of determining the global state of a distributed system are the lack of a global clock, the asynchrony of the communication, and the possibility of failures .



### Termination Detection

Termination detection is a fundamental problem in distributed systems, where a set of processes cooperate to perform a computation. The goal is to determine when all the processes have finished their work and there are no more messages in transit between them.

Termination detection is non-trivial because:

- No process has complete knowledge of the global state of the system.
- Processes may become idle and active at different times, depending on the arrival of messages.
- There is no global clock or synchronization among processes.

There are different algorithms for termination detection, depending on the assumptions and properties of the system. One of them is Huang's algorithm, which is based on the following ideas:

- Each process maintains a local counter of the number of messages it has sent and received.
- Each process periodically sends its counter value to a designated control process, which collects and aggregates the counter values from all processes.
- The control process can detect termination when the sum of all counter values is zero, meaning that there are no more messages in transit.

Huang's algorithm has the following advantages:

- It is efficient, as it only requires one control message per process per round.
- It is scalable, as it does not depend on the number of processes or messages in the system.
- It is robust, as it can tolerate process failures and message losses.

Huang's algorithm has the following disadvantages:

- It requires a reliable control process, which may become a bottleneck or a single point of failure.
- It requires periodic communication, which may incur unnecessary overhead or delay.
- It may not detect termination in some cases, such as when there are cycles of messages or when messages are reordered by the network.



## Unit 2 - Distributed Mutual Exclusion

- Distributed mutual exclusion is a fundamental problem in distributed computing systems  .
- It ensures that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner  .
- It states that only one process is allowed to execute the critical section (CS) at any given time  .
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion . Message passing is the sole means for implementing distributed mutual exclusion.
- There are three basic approaches for implementing distributed mutual exclusion:
  - Token-based algorithms: A process can enter the CS only if it possesses a unique token. The token is passed among the processes in a predefined order or by request. Examples are Suzuki-Kasami's algorithm and Raymond's algorithm.
  - Permission-based algorithms: A process can enter the CS only if it receives permission from all or a subset of other processes. The process sends a request message to other processes and waits for their reply messages. Examples are Lamport's algorithm and Ricart-Agrawala's algorithm.
  - Quorum-based algorithms: A process can enter the CS only if it receives permission from a majority or a quorum of other processes. The process sends a request message to a subset of processes and waits for their reply messages. Examples are Maekawa's algorithm and Sopena's algorithm.
- The performance of distributed mutual exclusion algorithms can be measured by the following criteria :
  - Message complexity: The number of messages exchanged per CS execution.
  - Synchronization delay: The time elapsed between a process requesting the CS and being granted the CS, assuming no other process is in the CS or requesting the CS.
  - Response time: The time elapsed between a process requesting the CS and being granted the CS, assuming some other processes may be in the CS or requesting the CS.
  - System throughput: The number of times the CS can be executed per unit time in the system.



### Classification of distributed mutual exclusion

Distributed mutual exclusion is a problem of ensuring that only one process in a distributed system can access a shared resource or data at a time. It is a fundamental requirement for achieving consistency, coordination and synchronization among the processes in a distributed system.   

There are three basic approaches for implementing distributed mutual exclusion algorithms:  

- Token-based approach: A unique token is shared among the sites or processes. A site is allowed to enter its critical section if it possesses the token. Mutual exclusion is ensured because the token is unique. Examples of token-based algorithms are Suzuki-Kasami's algorithm, Raymond's algorithm and Maekawa's algorithm.  
- Non-token-based approach: A site requests permission from other sites before entering its critical section. A site is allowed to enter its critical section if it receives permission from all or a majority of other sites. Mutual exclusion is ensured by a voting mechanism. Examples of non-token-based algorithms are Ricart-Agrawala's algorithm, Lamport's algorithm and Singhal's algorithm.  
- Quorum-based approach: A site requests permission from a subset of sites, called a quorum, before entering its critical section. A site is allowed to enter its critical section if it receives permission from all the sites in the quorum. Mutual exclusion is ensured by the intersection property of quorums. Examples of quorum-based algorithms are Naimi-Trehel's algorithm, Agrawal-El Abbadi's algorithm and Thomas's algorithm.  

The performance of distributed mutual exclusion algorithms can be evaluated based on the following metrics:   

- Message complexity: The number of messages exchanged per critical section execution.
- Synchronization delay: The time elapsed between a site's request and its entry to the critical section.
- System throughput: The number of critical section executions per unit time in the system.
- Fault tolerance: The ability of the algorithm to handle failures of sites or communication links.



### Requirement of mutual exclusion theorem for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM

- Mutual exclusion is a concurrency control property which is introduced to prevent race conditions.
- It is the requirement that a process can not enter its critical section while another concurrent process is currently present or executing in its critical section.
- A critical section is a segment of code that accesses a shared resource or data.
- Mutual exclusion ensures that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner .
- Mutual exclusion in a distributed system states that only one process is allowed to execute the critical section at any given time .
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion .
- Message passing is the sole means for implementing distributed mutual exclusion .
- There are three basic approaches for implementing distributed mutual exclusion:
  - Token-based algorithms: A process can enter the critical section only if it possesses a unique token. The token is passed among the processes in a predefined order or by request.
  - Permission-based algorithms: A process can enter the critical section only if it receives permission from all or a subset of other processes in the system. The process sends request messages and waits for reply messages before entering the critical section.
  - Quorum-based algorithms: A process can enter the critical section only if it receives permission from a majority or a quorum of processes in the system. The process sends request messages to a subset of processes and waits for reply messages from a quorum before entering the critical section.
- The mutual exclusion theorem states that any algorithm for implementing mutual exclusion in a distributed system must satisfy the following properties:
  - Safety: At most one process can execute in the critical section at any time.
  - Liveness: If a process requests to enter the critical section, it will eventually be granted permission.
  - Fairness: No process is indefinitely postponed or starved from entering the critical section.



### Token based and non token based algorithms for distributed mutual exclusion

Distributed mutual exclusion (DME) is the problem of ensuring that only one process at a time can access a shared resource in a distributed system. There are two main approaches to solve this problem: token based and non token based algorithms.

- Token based algorithms
  - In token based algorithms, a unique token is shared among all the processes in the system. The process that holds the token has the exclusive right to enter the critical section. The token is passed from one process to another according to some protocol.
  - Token based algorithms are simple and efficient, as they do not require any message exchange between processes to request or grant permission to enter the critical section. However, they have some drawbacks, such as the possibility of token loss, duplication, or starvation.
  - Some examples of token based algorithms are:
    - Centralized token algorithm: The token is initially assigned to a designated coordinator process, which grants the token to the first process that requests it. The process that receives the token must return it to the coordinator after exiting the critical section. The coordinator maintains a queue of pending requests and grants the token to the next process in the queue when it is available.
    - Ring token algorithm: The processes are arranged in a logical ring, and the token circulates in the ring. A process that wants to enter the critical section must wait for the token to arrive. After exiting the critical section, the process passes the token to the next process in the ring.
    - Suzuki-Kasami algorithm: The token contains a vector of sequence numbers, one for each process, that indicates the latest request from each process. A process that wants to enter the critical section broadcasts a request message with its sequence number to all other processes. The process that holds the token sends it to the process with the highest sequence number in the token vector. The process that receives the token updates the token vector with its own sequence number and enters the critical section.

- Non token based algorithms
  - In non token based algorithms, a process that wants to enter the critical section communicates with a set of other processes to request and obtain permission. The processes use timestamps or logical clocks to order and resolve the requests. Non token based algorithms require more message exchange than token based algorithms, but they are more robust and flexible, as they do not depend on a single token.
  - Some examples of non token based algorithms are:
    - Lamport's algorithm: A process that wants to enter the critical section sends a request message with its logical clock value to all other processes. The process waits for a reply message from all other processes, indicating that they have received the request and they are not in the critical section or have a lower priority. The process enters the critical section when it receives all the replies. After exiting the critical section, the process sends a release message to all other processes, indicating that it has finished using the resource.
    - Ricart-Agrawala algorithm: A process that wants to enter the critical section sends a request message with its logical clock value to all other processes. The process waits for a reply message from all other processes, indicating that they have received the request and they are not in the critical section or have a lower priority. The process enters the critical section when it receives all the replies. After exiting the critical section, the process sends a reply message to all the processes that have sent a request message to it while it was in the critical section.
    - Maekawa's algorithm: A process that wants to enter the critical section sends a request message to a subset of processes, called a voting set, that contains at least one process in common with every other voting set. The process waits for a reply message from all the processes in its voting set, indicating that they have granted the permission. The process enters the critical section when it receives all the replies. After exiting the critical section, the process sends a release message to all the processes in its voting set, indicating that it has released the resource. A process can grant permission to only one process at a time, and it must queue the requests from other processes.



### Performance Metric for Distributed Mutual Exclusion Algorithms

Distributed mutual exclusion algorithms are algorithms that ensure that only one process at a time can access a shared resource in a distributed system. The performance of these algorithms can be evaluated by the following metrics :

- **Message complexity**: It is the number of messages that are required per critical section (CS) execution by a process. It reflects the communication overhead and network congestion caused by the algorithm. A lower message complexity is desirable.
- **Synchronization delay**: It is the time elapsed between the departure of a process from the CS and the entry of the next process into the CS. It reflects the degree of concurrency and fairness achieved by the algorithm. A lower synchronization delay is desirable.
- **Response time**: It is the time interval between the request of a process to enter the CS and the end of its CS execution. It reflects the waiting time and the service time experienced by the process. A lower response time is desirable.
- **Throughput**: It is the number of CS executions per unit time in the system. It reflects the efficiency and utilization of the shared resource by the processes. A higher throughput is desirable.

Different algorithms may have different trade-offs among these metrics, depending on the assumptions and design choices they make. For example, some algorithms may use a central coordinator to grant access to the CS, while others may use a distributed token or a quorum of processes . Some algorithms may use a FIFO queue to order the requests, while others may use a priority queue or a random order. Some algorithms may require the processes to know the global state of the system, while others may allow the processes to have partial or outdated information. These factors may affect the performance of the algorithms in different scenarios and workloads. Therefore, it is important to compare and analyze the algorithms using the performance metrics mentioned above.



## Unit 3 - Distributed Deadlock Detection

- A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
- Deadlock detection is the process of finding out whether a deadlock has occurred or not in a system.
- Distributed deadlock detection is the process of detecting deadlocks in a distributed system, where processes and resources may be located on different nodes connected by a network.
- Distributed deadlock detection can be classified into two categories: centralized and distributed.
- Centralized deadlock detection involves a designated node, called the coordinator, that collects global information about the system and runs a deadlock detection algorithm.
- Distributed deadlock detection involves each node running a local deadlock detection algorithm and exchanging messages with other nodes to detect global deadlocks.
- There are different types of distributed deadlock detection algorithms, such as:
  - Path-pushing algorithms, where each node maintains a wait-for graph and sends it to other nodes along a potential deadlock cycle.
  - Edge-chasing algorithms, where each node sends a probe message to the node it is waiting for, and the probe message is forwarded along the wait-for chain until it either reaches the initiator node (deadlock detected) or a node that is not waiting for anyone (deadlock not detected).
  - Diffusion computation algorithms, where each node initiates a computation to detect a deadlock involving itself, and the computation is propagated to other nodes through messages. The computation terminates when either a deadlock is detected or all nodes have been visited.



### System Model for Distributed Deadlock Detection

- A distributed system consists of a set of nodes that communicate by message passing.
- Each node has a set of resources that can be requested by processes running on the node or on other nodes.
- A process can request, use, and release resources according to some protocol.
- A process may hold some resources while waiting for others, resulting in a wait-for graph (WFG) that represents the dependencies among processes and resources.
- A deadlock occurs when there is a cycle in the WFG, meaning that some processes are waiting for resources that are held by other processes in the cycle, and no progress can be made.
- Deadlock detection is the problem of finding cycles in the WFG and resolving them by aborting some processes or preempting some resources.
- There are three main approaches to deadlock detection in distributed systems: centralized, hierarchical, and distributed.
- In the centralized approach, there is a designated node, called the deadlock detector (DD), that collects information about the WFG from all other nodes and performs cycle detection on the global WFG.
- In the hierarchical approach, the nodes are organized into clusters, and each cluster has a local DD that collects information from the nodes in the cluster and performs cycle detection on the local WFG. The local DDs communicate with a global DD that performs cycle detection on the global WFG, which is constructed from the local WFGs.
- In the distributed approach, there is no central or hierarchical authority, and each node participates in the cycle detection algorithm by sending and receiving messages along the edges of the WFG. There are different algorithms for distributed cycle detection, such as edge chasing, diffusing computation, and probe-based.



### Resource vs Communication Deadlocks

- A deadlock is a condition where a process cannot proceed because it needs to obtain a resource held by another process, and it itself is holding a resource that the other process needs.
- There are two types of deadlocks in distributed systems: resource deadlocks and communication deadlocks.
- Resource deadlocks occur when processes access resources, such as data objects in database systems and buffers in store and forward communication networks . A process acquires a resource before accessing it and releasing it after using it. A resource deadlock happens when a cycle of processes is formed, each holding a resource and waiting for another resource in the cycle.
- Communication deadlocks occur when processes communicate by sending and receiving messages, such as in message passing systems and distributed shared memory systems . A process sends a message to another process and waits for a reply. A communication deadlock happens when a cycle of processes is formed, each sending a message and waiting for a reply from another process in the cycle.
- The main difference between resource deadlocks and communication deadlocks is that resource deadlocks involve the contention for resources, while communication deadlocks involve the loss or corruption of signals.
- Another difference is that resource deadlocks can be detected by using techniques such as wait-for graphs, timestamps, and timeouts, while communication deadlocks are harder to detect and resolve because they depend on the reliability and ordering of messages .
- Resource deadlocks can be prevented by using protocols such as deadlock prevention, deadlock avoidance, and deadlock recovery, while communication deadlocks can be prevented by using protocols such as reliable and ordered message delivery, message acknowledgments, and message retransmission .



### Deadlock Prevention for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process. In a distributed system, deadlocks are more difficult to detect and resolve because the processes and resources may be physically dispersed across different nodes.

Deadlock prevention is a technique to avoid the occurrence of deadlocks by ensuring that at least one of the four necessary conditions for deadlock (mutual exclusion, hold and wait, no preemption, and circular wait) is never satisfied.

There are two main methods of deadlock prevention in a distributed system:

- Ordered request: This method assigns a unique level to each resource type and requires that a process requests resources in an increasing order of levels. This prevents circular wait condition, as there is a total ordering of resources.
- Collective request: This method requires that a process requests all the resources it needs at the same time, before starting its execution. This prevents hold and wait condition, as a process does not hold any resource while waiting for others.

Some advantages of deadlock prevention are:

- It is simple and easy to implement.
- It does not incur any overhead of deadlock detection and recovery.

Some disadvantages of deadlock prevention are:

- It may impose unnecessary restrictions on resource utilization and process execution.
- It may not be applicable or feasible for some types of resources or processes.



### Avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- Deadlock avoidance is a technique that prevents the occurrence of deadlocks by ensuring that the system is always in a safe state.
- A safe state is one in which there exists a sequence of resource allocations that does not lead to a deadlock.
- Deadlock avoidance requires the system to have some knowledge of the current and future resource requests and releases of each process.
- However, deadlock avoidance is impractical in distributed systems due to several problems, such as:
  - The lack of global information and synchronization among the nodes.
  - The uncertainty and unpredictability of resource requests and releases.
  - The possibility of communication failures and process crashes.
  - The high overhead and complexity of maintaining and checking the safe state.
- Therefore, deadlock detection is preferred over deadlock avoidance in distributed systems.
- Deadlock detection is a technique that identifies the existence of deadlocks after they have occurred and takes some actions to resolve them.
- Deadlock detection requires the system to collect and analyze the information about the process-resource interactions and look for cycles in the wait-for graph.
- Deadlock detection algorithms in distributed systems can be classified into four categories, based on the way they collect and propagate the information:
  - Path-pushing algorithms: Each node maintains a set of paths that represent the dependencies among the processes and resources. The paths are periodically exchanged among the nodes to detect cycles.
  - Edge-chasing algorithms: Each node sends a probe message along the edges of the wait-for graph to trace a cycle. If a probe returns to the sender, a deadlock is detected.
  - Diffusion computation algorithms: Each node initiates a computation to determine the local wait-for graph and propagates it to its neighbors. The computation terminates when the global wait-for graph is obtained and checked for cycles.
  - Global state detection algorithms: Each node periodically records its local state and sends it to a coordinator node. The coordinator node constructs a global state from the local states and checks it for consistency and cycles.



### Detection and Resolution of Distributed Deadlocks

- A distributed deadlock is a situation where a set of processes in a distributed system are waiting for each other to release resources or send messages, and none of them can proceed.
- A distributed deadlock can be detected by constructing a wait-for graph (WFG) that represents the dependencies among the processes and resources in the system.
- A cycle in the WFG indicates the presence of a deadlock. A knot is a strongly connected component of the WFG that contains all the processes involved in a deadlock.
- There are two main issues in deadlock detection: how to maintain the WFG and how to search the WFG for cycles or knots.
- There are three approaches to maintain the WFG: centralized, distributed, and hierarchical.
  - In the centralized approach, a single coordinator process collects information from all the other processes and constructs the global WFG. The coordinator periodically searches the WFG for cycles and initiates deadlock resolution. This approach is simple but suffers from a single point of failure and a high communication overhead.
  - In the distributed approach, each process maintains a local WFG that reflects its dependencies with other processes. The processes exchange messages to construct a global WFG on demand. The global WFG can be searched for cycles or knots using a distributed algorithm. This approach avoids a single point of failure and reduces the communication overhead, but it requires more complex algorithms and synchronization.
  - In the hierarchical approach, the processes are organized into a tree structure, where each node is a group of processes. Each node maintains a local WFG that reflects the dependencies within the group and with other groups. The nodes exchange messages to construct a global WFG on demand. The global WFG can be searched for cycles or knots using a hierarchical algorithm. This approach combines the advantages of the centralized and distributed approaches, but it requires a stable and balanced tree structure.
- There are two main methods to search the WFG for cycles or knots: edge-chasing and probe-based.
  - In the edge-chasing method, each process sends a probe message along the outgoing edges of its local WFG. The probe message contains the identity of the sender and the path it has traversed. If a process receives a probe message that contains its own identity, it detects a cycle and initiates deadlock resolution. This method is simple but generates a lot of messages and may detect false cycles due to concurrency.
  - In the probe-based method, each process sends a probe message to a subset of its outgoing neighbors in its local WFG. The probe message contains the identity of the sender and a timestamp. If a process receives a probe message that has a smaller timestamp than its own, it forwards the message to a subset of its outgoing neighbors. If a process receives a probe message that has a larger timestamp than its own, it discards the message. If a process receives a probe message that contains its own identity, it detects a knot and initiates deadlock resolution. This method reduces the number of messages and avoids false cycles, but it requires a global clock or a logical clock to generate timestamps.
- There are various resolutions of deadlock detection in the distributed system, such as:
  - Abort one or more processes involved in the deadlock and release their resources or messages. The choice of which process to abort can be based on some criteria, such as priority, cost, or age.
  - Preempt one or more resources or messages from the processes involved in the deadlock and allocate them to other processes. The choice of which resource or message to preempt can be based on some criteria, such as usage, availability, or demand.
  - Rollback one or more processes involved in the deadlock to a previous state and release their resources or messages. The choice of which process to rollback and how far to rollback can be based on some criteria, such as checkpoint frequency, recovery time, or consistency.
  - Migrate one or more processes involved in the deadlock to another location and release their resources or messages. The choice of which process to migrate and where to migrate can be based on some criteria, such as load balancing, network latency, or fault tolerance.



# Centralized Deadlock Detection

- This is a technique used in distributed systems to handle deadlock detection.
- According to this approach, the system maintains one global wait-for graph in a single chosen site, which is named as deadlock-detection coordinator.
- The coordinator collects information about the local wait-for graphs of each site and constructs the global wait-for graph.
- The coordinator periodically runs a deadlock detection algorithm on the global wait-for graph to find cycles, which indicate deadlocks.
- If a deadlock is detected, the coordinator selects a victim process and sends an abort message to the site where the process is located.
- The advantages of this approach are simplicity and low communication overhead.
- The disadvantages of this approach are single point of failure, scalability issues, and lack of autonomy.

: https://www.exploredatabase.com/2014/06/centralized-deadlock-detection-approach-in-distributed-database.html
: https://www.javatpoint.com/deadlock-detection-in-distributed-systems
: https://people.cs.rutgers.edu/~pxk/417/notes/deadlock.html
: https://www.geeksforgeeks.org/deadlock-detection-in-distributed-systems/



### Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set, and none of the processes can proceed or release the resources.
- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems.
- Deadlock detection in distributed systems entails addressing two basic issues: first, detection of existing deadlocks and second, resolution of detected deadlocks.
- Deadlock detection in distributed systems requires examination of the status of process-resource interactions for presence of cyclic wait.
- There are three approaches to detect deadlocks in distributed systems: centralized, hierarchical, and distributed.
  - Centralized approach: A single node is designated as the deadlock detector and collects information from all other nodes about their resource allocation and requests. The deadlock detector constructs a global wait-for graph (WFG) and checks for cycles in the graph. If a cycle is found, a deadlock is detected and resolved by aborting one or more processes in the cycle.
  - Hierarchical approach: The nodes are organized into a hierarchy of clusters, and each cluster has a local deadlock detector. The local deadlock detectors periodically send information to their parent cluster, and the parent cluster constructs a global WFG for the sub-tree. The parent cluster checks for cycles in the global WFG and notifies the local deadlock detectors if a deadlock is detected. The local deadlock detectors then resolve the deadlock by aborting one or more processes in the cycle.
  - Distributed approach: There is no central or hierarchical authority for deadlock detection. Each node maintains a local WFG and exchanges information with other nodes using messages. There are two main techniques for distributed deadlock detection: edge chasing and probe-based.
    - Edge chasing: Each node initiates a probe message when it requests a resource that is held by another node. The probe message contains the identity of the initiator and the path of the message. The probe message is forwarded along the wait-for edges until it either reaches the initiator (a cycle is detected) or a node that is not waiting for any resource (a cycle is not detected). The initiator aborts itself or another process in the cycle to resolve the deadlock.
    - Probe-based: Each node periodically initiates a probe message that contains a timestamp and a hop count. The probe message is broadcast to all other nodes, and each node updates its local WFG based on the information in the probe message. Each node also maintains a counter that indicates the number of probe messages it has received. When the counter reaches a certain threshold, the node checks its local WFG for cycles. If a cycle is found, the node sends a resolution message to the process with the smallest timestamp in the cycle, and the process aborts itself or another process in the cycle to resolve the deadlock.



### Path Pushing Algorithms

- Path pushing algorithms detect distributed deadlocks by maintaining an explicit global wait-for graph (WFG) at each site of the distributed system .
- The global WFG is constructed by sending the local WFG of each site to all its neighboring sites whenever a deadlock computation is performed .
- The neighboring sites then merge the received WFG with their own local WFG to update their global WFG .
- The global WFG contains all the dependency edges among the processes in the distributed system, and can be used to detect cycles that indicate deadlocks .
- Path pushing algorithms have the advantage of reducing the number of messages needed for deadlock detection, as the global WFG is only updated when a deadlock computation is initiated .
- However, path pushing algorithms also have some drawbacks, such as:
  - The global WFG may be inconsistent or outdated, as it does not reflect the current state of the distributed system .
  - The global WFG may be large and complex, as it contains all the dependency edges in the distributed system, which may increase the storage and computation overhead .
  - The global WFG may contain false dependencies, as some edges may be obsolete or irrelevant for deadlock detection, which may lead to false positives or false negatives .



### Edge Chasing Algorithms for Distributed Deadlock Detection

- Edge chasing algorithms are a class of distributed deadlock detection algorithms that use special messages called probes to trace the dependency graph of processes and resources in a distributed system.
- A probe is a triplet (i, j, k) that denotes that the deadlock detection is initiated by process P_i and the message is being sent by the home site of process P_j to the home site of process P_k.
- The probe message follows the edges of the dependency graph from the waiting processes to the blocking processes until either a cycle is detected or all the edges are traversed.
- A cycle is detected when a probe message returns to the initiator process or when a process receives a probe message with its own identifier in the triplet.
- Edge chasing algorithms can be applied to different request models, such as AND model, OR model, or general model, depending on the type of requests that processes can make for resources.
- One of the most well-known edge chasing algorithms is the Chandy-Misra-Haas algorithm for the AND model, which assumes that a process can request multiple resources simultaneously and must acquire all of them to proceed.
- The Chandy-Misra-Haas algorithm works as follows:

  - Each process maintains a wait-for graph that records its dependency on other processes.
  - When a process P_i initiates a deadlock detection, it sends a probe message (i, i, j) to the home site of each process P_j that it is waiting for.
  - When a process P_j receives a probe message (i, k, j), it checks if it is dependent on any other process. If not, it discards the message. If yes, it does the following:
    - If j = i, then a cycle is detected and P_j informs P_i of the deadlock.
    - If j != i and P_j has not participated in the deadlock detection initiated by P_i before, then P_j records i in its local state and sends a probe message (i, j, l) to the home site of each process P_l that it is waiting for.
    - If j != i and P_j has participated in the deadlock detection initiated by P_i before, then P_j discards the message.
  - When a process P_i receives a deadlock notification from another process, it informs all the processes that are dependent on it to abort and releases all the resources that it holds.

- The advantages of edge chasing algorithms are that they are simple, efficient, and scalable. They do not require global information or synchronization among processes or sites. They only generate probe messages when a deadlock is suspected and they terminate the detection when a cycle is found or when all the edges are traversed.
- The disadvantages of edge chasing algorithms are that they may generate false positives, meaning that they may detect a cycle that does not correspond to a real deadlock. This can happen when the dependency graph changes dynamically due to resource releases or process terminations. They may also generate duplicate probe messages if multiple processes initiate the deadlock detection concurrently.



## Unit 4 - Agreement Protocols

- Agreement protocols are a class of distributed algorithms that allow a set of processes to reach a common decision, despite the possibility of failures or malicious behavior.
- Agreement protocols are useful for implementing fault-tolerant services, such as distributed consensus, atomic broadcast, leader election, and distributed transactions.
- Agreement protocols can be classified into different types, depending on the assumptions they make about the system model, the communication model, the failure model, and the adversary model.
- Some common types of agreement protocols are:
  - **Crash fault-tolerant protocols**: These protocols assume that processes may fail by crashing, but do not behave maliciously. They also assume that the communication is reliable and synchronous, meaning that messages are delivered within a known bounded time. Examples of crash fault-tolerant protocols are Paxos, Raft, and Two-Phase Commit.
  - **Byzantine fault-tolerant protocols**: These protocols assume that processes may fail by behaving arbitrarily, or even colluding with other faulty processes. They also assume that the communication is unreliable and asynchronous, meaning that messages may be lost, delayed, duplicated, or reordered. Examples of Byzantine fault-tolerant protocols are PBFT, Zyzzyva, and Tendermint.
  - **Randomized protocols**: These protocols use randomization techniques, such as coin tossing or sampling, to achieve agreement with high probability, even in the presence of failures or adversaries. They also relax the synchrony assumption, and allow for partial or eventual synchrony, meaning that messages are delivered within some unknown or variable time. Examples of randomized protocols are Ben-Or, Rabin, and HoneyBadgerBFT.
- Agreement protocols typically have the following properties or guarantees:
  - **Validity**: The decision value must be valid, meaning that it must be proposed by some correct process, or satisfy some predefined condition.
  - **Agreement**: All correct processes must agree on the same decision value.
  - **Termination**: All correct processes must eventually decide on some value.
  - **Integrity**: A process can decide at most once, and only on a single value.
- Agreement protocols may also have additional properties or optimizations, such as:
  - **Uniformity**: The agreement property holds even for faulty processes, meaning that they cannot decide on a different value from the correct processes.
  - **Early stopping**: The protocol can terminate in fewer rounds than the worst-case scenario, depending on the actual system behavior or the input values.
  - **Leaderlessness**: The protocol does not rely on a designated leader or coordinator, which may become a bottleneck or a single point of failure.
  - **Adaptivity**: The protocol can adapt to the changing system conditions or parameters, such as the number of failures, the network latency, or the adversary power.



### Introduction for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- Agreement protocols are a class of algorithms that allow a set of distributed processes to reach a common decision or consensus on some value or action, despite the presence of failures or uncertainties.
- Agreement protocols are essential for ensuring the correctness and consistency of distributed systems, especially in the context of fault tolerance, replication, distributed transactions, distributed consensus, and distributed commit.
- Agreement protocols can be classified into different types based on the following criteria:
  - The type of failures that the protocol can tolerate, such as crash failures, omission failures, timing failures, or Byzantine failures.
  - The type of communication model that the protocol assumes, such as synchronous, asynchronous, or partially synchronous.
  - The type of agreement that the protocol guarantees, such as uniform agreement, non-uniform agreement, or interactive consistency.
  - The type of value that the protocol agrees on, such as binary, multivalued, or vector.
- Some of the most well-known agreement protocols are:
  - Paxos, which is a family of protocols that achieve consensus in a network of unreliable processes.
  - Raft, which is a protocol that simplifies the design and implementation of Paxos by dividing the consensus problem into three subproblems: leader election, log replication, and safety.
  - Two-phase commit (2PC), which is a protocol that allows a coordinator to atomically commit or abort a distributed transaction involving multiple participants.
  - Three-phase commit (3PC), which is a protocol that improves the availability of 2PC by introducing a third phase to avoid blocking in case of failures.
  - Byzantine agreement (BA), which is a protocol that allows a set of processes to agree on a value even if some of them are faulty or malicious.
  - Byzantine fault tolerance (BFT), which is a general technique that enables a system to tolerate Byzantine failures by using replication, cryptography, and voting.



### System models for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

A system model is a description of the properties and assumptions of a distributed system that are relevant for its design and analysis. System models can help us understand the behavior and limitations of a system, as well as compare different systems and algorithms.

There are three main types of system models:

- **Network models**: These models capture the characteristics and behavior of the communication network that connects the components of a distributed system. For example, network models can describe the reliability, latency, bandwidth, and topology of the network.
- **Node models**: These models capture the characteristics and behavior of the individual components of a distributed system, such as processes, servers, or devices. For example, node models can describe the availability, performance, and failure modes of the nodes.
- **Timing models**: These models capture the assumptions and guarantees about the timing and synchronization of events and actions in a distributed system. For example, timing models can describe the clock accuracy, message delivery order, and global time of the system.

Different system models can have different levels of abstraction and complexity, depending on the goals and requirements of the system. Some common system models are:

- **Synchronous system model**: This model assumes that there are known bounds on the network delay, node processing speed, and clock drift of the system. This model simplifies the design and analysis of distributed algorithms, but it is often unrealistic and impractical for real systems.
- **Asynchronous system model**: This model assumes that there are no bounds on the network delay, node processing speed, and clock drift of the system. This model is more realistic and general for real systems, but it makes the design and analysis of distributed algorithms more challenging and complex.
- **Partially synchronous system model**: This model assumes that there are bounds on the network delay, node processing speed, and clock drift of the system, but they are unknown or may change over time. This model is a compromise between the synchronous and asynchronous models, and it tries to capture the realistic behavior of real systems while still allowing some tractable analysis of distributed algorithms.
- **Crash-stop system model**: This model assumes that nodes can fail by crashing, which means that they stop executing and do not recover. This model simplifies the analysis of fault tolerance, but it does not account for other types of failures, such as network partitions, message losses, or Byzantine behavior.
- **Crash-recovery system model**: This model assumes that nodes can fail by crashing, but they can also recover and resume execution after some time. This model is more realistic and general for real systems, but it requires more complex mechanisms for state recovery and consistency.
- **Byzantine system model**: This model assumes that nodes can fail in arbitrary ways, which means that they can behave maliciously, dishonestly, or inconsistently. This model is the most pessimistic and challenging for fault tolerance, but it can capture the worst-case scenarios of real systems.

System models are essential for the design and analysis of agreement protocols in distributed systems. Agreement protocols are algorithms that allow a set of nodes to reach a common decision or value, despite the presence of failures and uncertainties in the system. Some examples of agreement protocols are:

- **Consensus protocol**: This protocol allows a set of nodes to agree on a single value, such as a leader, a transaction, or a configuration. Consensus is one of the most fundamental and difficult problems in distributed systems, and it has many applications and variations.
- **Atomic broadcast protocol**: This protocol allows a set of nodes to deliver a stream of messages in the same order, such that the order is consistent with the causal dependencies of the messages. Atomic broadcast is a useful abstraction for implementing replicated state machines and consistent databases.
- **Group membership protocol**: This protocol allows a set of nodes to maintain a consistent view of the current members of the system, and to detect and handle node failures and joins. Group membership is a basic service for building reliable and scalable distributed systems.

Different system models have different implications and limitations for the feasibility and performance of agreement protocols. For example, the famous FLP impossibility result shows that consensus is impossible to solve in an asynchronous system model with even one crash failure. On the other hand, consensus can be solved in a synchronous system model with up to half of the nodes crashing. However, synchronous system models are often too restrictive and unrealistic for real systems, so many practical consensus protocols use partially synchronous system models or additional assumptions, such as failure detectors, randomization, or trusted components.

System models are not fixed or universal, but rather they depend on the context



### Classification of Agreement Problem

An agreement problem is a problem where a set of processes in a distributed system have to agree on some value or decision, despite the possibility of failures or malicious behavior. Agreement problems are fundamental to achieving fault tolerance and consistency in distributed systems.

There are different types of agreement problems, depending on the assumptions and requirements of the system. Some of the well-known agreement problems are:

- **Byzantine agreement problem**: A single value, which is to be agreed on, is initialized by an arbitrary process and all non-faulty processes have to agree on that value. The processes may be subject to Byzantine failures, which means they can behave arbitrarily or maliciously, sending conflicting or incorrect messages to other processes. The goal is to ensure that all non-faulty processes agree on the same value, and that value is the initial value of some non-faulty process.   

- **Consensus problem**: A generalization of the Byzantine agreement problem, where each process can propose a value and all non-faulty processes have to agree on a common value. The value agreed on must be one of the proposed values. The processes may be subject to crash failures, which means they can stop executing at any point, but they cannot send incorrect or conflicting messages. The goal is to ensure that all non-faulty processes agree on the same value, and that value is one of the proposed values.   

- **Interactive consistency problem**: A generalization of the consensus problem, where each process can propose a value and all non-faulty processes have to agree on a vector of values, one for each process. The value agreed on for each process must be the proposed value of that process, if it is non-faulty, or any value otherwise. The processes may be subject to Byzantine failures, as in the Byzantine agreement problem. The goal is to ensure that all non-faulty processes agree on the same vector of values, and that vector satisfies the validity condition.   

These are some of the main classification of agreement problems in distributed systems. There are other variations and extensions of these problems, such as atomic broadcast, atomic commitment, group membership, etc.   These problems are important for designing reliable and consistent distributed algorithms and protocols. However, they are also challenging to solve, especially in asynchronous systems or systems with Byzantine failures. There are various impossibility results and lower bounds that limit the feasibility and efficiency of solving these problems.   Therefore, researchers have proposed various techniques and trade-offs to cope with these limitations, such as using randomization, cryptography, trusted components, partial synchrony, etc.



### Byzantine agreement problem

- The Byzantine agreement problem is a fundamental problem in fault tolerant distributed computing, where a set of parties in a distributed environment need to agree on a value even if some of the parties are corrupted.
- The problem was first defined by Lamport and inspired by a hypothetical scenario of several divisions of the Byzantine army camped outside an enemy city, each division commanded by its own general. The generals can communicate with one another only by messenger. After observing the enemy, they must decide upon a common plan of action.
- The problem is that some of the generals may be traitors, who try to prevent the loyal generals from reaching agreement. The traitors may send conflicting messages, lie about their own values, or collude with other traitors. The loyal generals need a secure way to come to agreement on a plan (known as consensus) and carry out their chosen plan (known as coordination).
- A solution to the Byzantine agreement problem requires that the following conditions are met:
  - **Termination**: Every loyal party eventually decides on a value.
  - **Agreement**: All loyal parties decide on the same value.
  - **Validity**: If all loyal parties start with the same value, then they all decide on that value.
- A number of solutions to the Byzantine agreement problem exist, depending on the assumptions made about the communication model, the number of parties, the number of traitors, the synchrony of the system, and the cryptographic primitives available. Some examples of solutions are:
  - **Oral messages**: This is the original solution by Lamport, which assumes that messages are authenticated but not encrypted, and that the system is synchronous. The solution requires that the number of traitors is less than one third of the total number of parties, and that the parties exchange messages in rounds, where each round involves sending and receiving messages from all other parties. The solution is based on a recursive algorithm that uses majority voting to eliminate conflicting messages.
  - **Signed messages**: This is a variation of the oral messages solution, which assumes that messages are digitally signed and verifiable, but not encrypted, and that the system is synchronous. The solution requires that the number of traitors is less than half of the total number of parties, and that the parties exchange messages in rounds, where each round involves sending and receiving messages from all other parties. The solution is based on a recursive algorithm that uses majority voting to eliminate conflicting messages, and uses digital signatures to prevent forgery.
  - **Randomized algorithms**: These are solutions that use randomization to achieve probabilistic guarantees of consensus, rather than deterministic guarantees. They assume that the parties have access to some source of randomness, such as coin tossing or hash functions, and that the system is asynchronous. The solutions require that the number of traitors is less than half of the total number of parties, and that the parties exchange messages in rounds, where each round involves sending and receiving messages from a random subset of other parties. The solutions are based on algorithms that use random sampling to estimate the values of other parties, and use voting or coin tossing to decide on a value.



# Consensus problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- The consensus problem is the problem of getting a set of nodes in a distributed system to agree on something - it might be a value, a course of action or a decision.
- Achieving consensus allows a distributed system to act as a single entity, with every individual node aware of and in agreement with the actions of the whole of the network.
- Consensus is a general agreement on a decision made by the majority of those involved.
- Consensus is essential for ensuring reliability, consistency, fault-tolerance and availability in distributed systems  .
- Consensus is challenging to achieve in distributed systems due to the possibility of failures, such as network partitions, message losses, node crashes, or malicious attacks  .
- There are many ways in which processes in a distributed system can reach a consensus, but there is usually a trade-off between security and performance.
- The more we want our algorithm to be secure against ways in which failure can happen, the less performant it tends to become.
- Some of the common consensus algorithms in distributed systems are:
  - Two-phase commit (2PC): A simple and widely used protocol that involves a coordinator and a set of participants. The coordinator initiates the protocol by sending a prepare message to all participants, asking them to vote on a proposed value. The participants reply with either a yes or a no vote. If the coordinator receives a yes vote from all participants, it sends a commit message to all participants, asking them to commit the value. If the coordinator receives a no vote from any participant, or does not receive a reply from any participant within a timeout, it sends an abort message to all participants, asking them to abort the value.
  - Three-phase commit (3PC): An extension of 2PC that adds a pre-commit phase to avoid blocking in case of a coordinator failure. The coordinator initiates the protocol by sending a prepare message to all participants, asking them to vote on a proposed value. The participants reply with either a yes or a no vote. If the coordinator receives a yes vote from all participants, it sends a pre-commit message to all participants, asking them to prepare to commit the value. The participants reply with an ack message. If the coordinator receives an ack message from all participants, it sends a commit message to all participants, asking them to commit the value. If the coordinator receives a no vote from any participant, or does not receive a reply from any participant within a timeout, it sends an abort message to all participants, asking them to abort the value.
  - Paxos: A family of protocols that use a quorum-based approach to achieve consensus in the presence of failures. The protocol involves a set of proposers, acceptors and learners. A proposer initiates the protocol by sending a prepare message with a proposal number to a quorum of acceptors, asking them to promise not to accept any proposal with a lower number. The acceptors reply with either a promise message, indicating the highest-numbered proposal they have accepted so far, or a reject message, indicating a higher-numbered proposal they have promised to another proposer. If the proposer receives a promise message from a quorum of acceptors, it sends an accept message with a proposal number and a value to the same quorum of acceptors, asking them to accept the value. The acceptors reply with either an accepted message, indicating they have accepted the value, or a reject message, indicating a higher-numbered proposal they have promised to another proposer. If the proposer receives an accepted message from a quorum of acceptors, it sends a learn message with the proposal number and the value to all learners, asking them to learn the value. The learners learn the value when they receive a learn message from a quorum of acceptors.
  - Raft: A protocol that simplifies Paxos by dividing the consensus problem into two subproblems: leader election and log replication. The protocol involves a set of servers, one of which is elected as the leader and the rest are followers. The leader is responsible for accepting client requests, appending them to a log, and replicating the log to all followers. The followers are responsible for receiving log entries from the leader, appending them to their logs, and sending acknowledgements to the leader. The leader and the followers communicate through heartbeat messages



### Interactive Consistency Problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- Interactive consistency is the problem in which n distinct nodes, each having its own private value, where up to t may be Byzantine, run an algorithm that allows all non-faulty nodes to infer the values of each other node  .
- Byzantine nodes are nodes that can behave arbitrarily, such as sending incorrect or conflicting messages, or remaining silent .
- Interactive consistency is a generalization of the consensus problem, where the goal is to reach agreement on a single value among all non-faulty nodes .
- Interactive consistency is also known as the generals problem, where each node represents a general in an army, and the private value represents the decision to attack or retreat .
- Interactive consistency is relevant to critical applications that rely on the combination of the opinions of multiple peers to provide a service, such as fault-tolerant distributed systems, blockchain systems, or voting systems  .
- Interactive consistency is a hard problem to solve, especially in asynchronous or partially synchronous systems, where there is no global clock or bounded message delays  .
- Interactive consistency requires at least n > 3t nodes to be solvable, where t is the maximum number of Byzantine nodes  .
- Interactive consistency can be solved using various algorithms, such as the oral messages algorithm, the signed messages algorithm, the echo broadcast algorithm, or the randomized Byzantine consensus algorithm   .
- Interactive consistency algorithms typically involve multiple rounds of message exchange, where each node broadcasts its value or a function of its value to all other nodes, and then collects and processes the received messages to infer the values of other nodes   .
- Interactive consistency algorithms may have different properties, such as termination, validity, agreement, and resilience, depending on the assumptions and guarantees they provide   .



### Solution to Byzantine Agreement problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- The Byzantine agreement problem is a fundamental problem in fault tolerant distributed computing, where a set of parties in a distributed environment need to agree on a value even if some of the parties are corrupted.
- The problem was first defined by Lamport and inspired by a hypothetical scenario of several divisions of the Byzantine army camped outside an enemy city, each division commanded by its own general. The generals can communicate with one another only by messenger. After observing the enemy, they must decide upon a common plan of action.
- A solution to the Byzantine agreement problem requires that the following conditions are met:
  - **Agreement**: All honest parties agree on the same value.
  - **Validity**: If all honest parties propose the same value, then they must agree on that value.
  - **Termination**: All honest parties eventually decide on a value.
- A number of solutions to the Byzantine agreement problem exist, depending on the assumptions made about the communication model, the number of corrupted parties, and the type of corruption.
- One of the most well-known solutions is the **oral messages algorithm** proposed by Lamport, Shostak, and Pease. This algorithm assumes that the communication is synchronous, meaning that there is a known upper bound on the message delivery time, and that the messages are authenticated, meaning that the sender and the content of the message cannot be forged. The algorithm also assumes that less than one-third of the parties are corrupted, and that the corruption is arbitrary, meaning that the corrupted parties can behave in any way to disrupt the agreement.
- The oral messages algorithm works as follows:
  - Each party proposes a value and sends it to all other parties.
  - For each round `r`, each party acts as a commander and sends an order to all other parties, based on the majority of the values received in the previous round. If there is no majority, the party sends a default value.
  - Each party acts as a lieutenant and follows the order of the commander, unless the order is different from the majority of the orders received from other parties. In that case, the party follows the majority or the default value if there is no majority.
  - After `r` rounds, each party decides on the value that it received in the last round.
- The oral messages algorithm can tolerate up to `f` corrupted parties, where `f` satisfies `3f < n`, where `n` is the total number of parties. The algorithm requires `O(n^2)` messages and `O(n)` rounds of communication.
- The oral messages algorithm can be improved by using **signed messages**, which allow the parties to prove the authenticity of the messages they receive and send. This reduces the number of rounds of communication to `O(f)` and the number of messages to `O(nf)`.
- Another solution to the Byzantine agreement problem is the **randomized algorithm** proposed by Rabin. This algorithm assumes that the communication is asynchronous, meaning that there is no upper bound on the message delivery time, and that the messages are authenticated. The algorithm also assumes that less than one-half of the parties are corrupted, and that the corruption is arbitrary.
- The randomized algorithm works as follows:
  - Each party proposes a value and sends it to all other parties.
  - Each party flips a coin and sends the result to all other parties.
  - Each party decides on the value that is proposed by the majority of the parties that have the same coin result as itself. If there is no such majority, the party decides on a default value.
- The randomized algorithm can tolerate up to `f` corrupted parties, where `f` satisfies `2f < n`, where `n` is the total number of parties. The algorithm requires `O(n^2)` messages and `O(1)` rounds of communication. The algorithm has a probability of error that decreases exponentially with the number of parties.



### Application of Agreement Problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- Agreement problem is a fundamental problem in distributed systems, where a set of processes need to reach a common decision based on their individual inputs and messages exchanged with each other .
- Agreement problem has many variants, such as consensus, atomic broadcast, atomic commitment, group membership, etc., depending on the type and number of values to be agreed upon, the assumptions about the system model, and the requirements for the agreement .
- Agreement problem is essential for many applications in distributed systems, such as fault tolerance, replication, coordination, distributed transactions, distributed databases, etc .
- Some examples of applications that use agreement problem are:
  - Atomic snapshot: A data structure that allows processes to atomically read and write multiple shared variables in a distributed system. Atomic snapshot can be implemented using a variant of agreement problem called lattice agreement, where processes need to agree on a value from a partially ordered set.
  - Replicated state machine: A technique that replicates the same deterministic state machine on multiple servers, and ensures that they execute the same sequence of commands in the same order. Replicated state machine can be implemented using consensus or atomic broadcast, where processes need to agree on a single value or a total order of values.
  - Distributed commit: A protocol that ensures that a distributed transaction either commits on all the participating sites, or aborts on all of them. Distributed commit can be implemented using atomic commitment, where processes need to agree on a binary value (commit or abort).
  - Group membership: A service that maintains the membership information of a group of processes in a distributed system, and notifies them of any changes (such as join, leave, or failure) in the group. Group membership can be implemented using a variant of agreement problem where processes need to agree on a set of values (the group members).



### Atomic Commit in Distributed Database System

- A distributed database system consists of multiple database sites that are connected by a communication network.
- A distributed transaction is a transaction that accesses data from multiple sites and updates them in a consistent manner.
- Atomicity is one of the ACID properties of transactions, which means that either all the changes made by a transaction are committed (made permanent) or none of them are.
- Atomic commit is the process of ensuring that all the sites involved in a distributed transaction agree on the final outcome (commit or abort) of the transaction.
- Atomic commit is necessary to maintain the consistency and integrity of the distributed database, and to avoid partial or inconsistent updates.
- Atomic commit is challenging in distributed systems because of the possibility of site failures, network failures, or communication delays, which may prevent some sites from receiving or sending messages to other sites.
- Atomic commit protocols are algorithms that coordinate the decision making of the sites involved in a distributed transaction, and handle the possible failures and uncertainties in the system.
- Atomic commit protocols can be classified into two categories: blocking and non-blocking.
  - Blocking protocols are protocols that may block (wait indefinitely) some sites from making progress if some other sites fail or become unreachable. An example of a blocking protocol is the two-phase commit (2PC) protocol, which consists of two phases: a prepare phase and a commit phase. In the prepare phase, a coordinator site asks all the participant sites to vote on whether they are ready to commit or not. In the commit phase, the coordinator site decides on the final outcome based on the votes, and informs all the participant sites to either commit or abort. If the coordinator site or some participant sites fail or become unreachable during the protocol, some sites may be blocked from making a decision or completing the transaction.
  - Non-blocking protocols are protocols that guarantee that no site will be blocked from making progress, even if some other sites fail or become unreachable. An example of a non-blocking protocol is the one-phase commit (1PC) protocol, which consists of only one phase: a commit phase. In the commit phase, a coordinator site decides on the final outcome and informs all the participant sites to either commit or abort. If the coordinator site or some participant sites fail or become unreachable during the protocol, the other sites can use a backup coordinator or a majority voting scheme to determine the final outcome and complete the transaction.

- Atomic commit protocols have different trade-offs in terms of performance, reliability, and complexity. Blocking protocols are simpler and faster than non-blocking protocols, but they may incur more blocking and aborts in the presence of failures. Non-blocking protocols are more robust and resilient to failures, but they may require more messages and coordination overhead than blocking protocols.



## Unit 5 - Distributed Resource Management

- Distributed resource management (DRM) is an evolving discipline that aims to enable distributed enterprise systems to operate effectively in production.
- DRM involves the coordination and optimization of various resources, such as computing, storage, network, energy, and human, across multiple locations and domains  .
- DRM can provide benefits such as improved performance, scalability, reliability, availability, security, and cost-efficiency for distributed systems  .
- DRM can also support the integration and management of distributed energy resources (DERs), such as solar panels, batteries, and demand response, which can enhance the resiliency and sustainability of the power grid .
- DRM can be implemented using various software, hardware, and network tools, as well as procedures and policies, depending on the specific requirements and objectives of the distributed system   .
- DRM can face challenges such as heterogeneity, dynamism, uncertainty, complexity, and scalability of the distributed system and its environment .
- DRM can adopt different approaches and techniques, such as centralized, decentralized, hierarchical, or hybrid, to address these challenges and achieve the desired level of control and coordination  .



# Issues in Distributed File Systems

A distributed file system (DFS) is a system that allows multiple clients to access and manipulate files stored on one or more servers over a network. A DFS provides the abstraction of a single, shared namespace for files and directories, hiding the details of their physical locations and distribution.

Some of the issues and challenges in designing and using a DFS are:

- **Naming and transparency**: A DFS should provide a consistent and uniform way of naming files and directories, regardless of their physical locations and distribution. A DFS should also support different levels of transparency, such as location transparency, access transparency, replication transparency, failure transparency, and migration transparency, to hide the complexity and heterogeneity of the underlying system from the users and applications.
- **Scalability**: A DFS should be able to accommodate a large number of clients and servers, and a large amount of data, without degrading the performance or reliability of the system. A DFS should also be able to adapt to the changes in the workload and the network conditions, by dynamically adjusting the allocation and replication of files and directories.
- **Performance**: A DFS should provide efficient and fast access to files and directories, minimizing the network latency and bandwidth consumption. A DFS should also balance the load among the servers, and exploit the locality and caching of data to improve the performance.
- **Consistency and coherence**: A DFS should ensure that the files and directories are consistent and coherent across the servers and the clients, especially when they are replicated or cached. A DFS should also provide mechanisms for concurrency control and conflict resolution, to handle the concurrent and conflicting operations on the same files and directories by different clients.
- **Reliability and availability**: A DFS should be able to tolerate and recover from the partial failures of the servers, the clients, the network, or the storage devices, without losing or corrupting the data. A DFS should also provide mechanisms for fault detection, fault isolation, fault masking, and fault recovery, to ensure the availability and integrity of the files and directories.
- **Security and privacy**: A DFS should provide mechanisms for authentication, authorization, encryption, and auditing, to protect the files and directories from unauthorized or malicious access, modification, or disclosure. A DFS should also respect the privacy and confidentiality of the users and the data, and comply with the relevant laws and regulations.



### Mechanism for building distributed file systems

A distributed file system (DFS) is a file system that is distributed on multiple file servers or multiple locations. It allows programs to access or store isolated files as they do with the local ones, allowing programmers to access files from any network or computer.

The mechanism for building a DFS involves the following aspects:

- Use of file models: The DFS uses different conceptual models of a file. The following are the two basic criteria for file modeling, which include file structure and modifiability. The files can be unstructured or structured based on the applications used in file systems. The files can also be immutable or mutable depending on whether they can be modified or not .
- Use of file accessing models: A DFS may use one of the following models to service a client’s file request: upload/download, remote access, or remote service. The upload/download model involves transferring the entire file between the client and the server. The remote access model involves transferring only the requested parts of the file. The remote service model involves executing the file operations on the server and returning the results to the client .
- Use of file replication: File replication is the primary mechanism for improving file availability in a distributed systems environment. A replicated file is a file that has multiple copies with each copy located on a separate file server. The challenges of file replication include maintaining consistency, coherence, and fault tolerance among the replicas .
- Use of file caching: File caching is the secondary mechanism for improving file performance in a distributed systems environment. A file cache is a temporary storage area that holds a copy of a file or a part of a file that is frequently accessed by the client. The benefits of file caching include reducing network traffic, latency, and server load. The challenges of file caching include maintaining cache consistency, coherence, and fault tolerance .
- Use of file naming: File naming is the mechanism for identifying and locating files in a DFS. A file name consists of two parts: a file identifier and a file path. A file identifier is a unique name that distinguishes a file from other files. A file path is a sequence of names that specifies the location of a file in a hierarchical directory structure. The file naming schemes can be classified into three types: flat, structured, and attribute-based .
- Use of file security: File security is the mechanism for protecting files from unauthorized access, modification, or deletion in a DFS. File security involves two aspects: authentication and authorization. Authentication is the process of verifying the identity of a user or a process that requests access to a file. Authorization is the process of granting or denying access rights to a file based on the identity and the role of the user or the process .
- Use of cloud services: Cloud services are the mechanism for extending a DFS to the cloud. Cloud services expose file and object storage using either standard protocols such as NFS and SMB or published APIs such as Amazon S3 and Google Cloud Storage. The advantages of cloud services include scalability, elasticity, and cost-effectiveness. The challenges of cloud services include security, privacy, and interoperability.



### Design issues in Distributed Shared Memory

Distributed Shared Memory (DSM) is a mechanism that allows multiple processes on different nodes to share a common virtual memory space. DSM can simplify the programming of distributed applications by hiding the details of inter-process communication. However, designing and implementing a DSM system involves several challenges and trade-offs, such as :

- **Granularity**: This refers to the size of the memory blocks that are shared and transferred among the nodes. A finer granularity (e.g., a page or a cache line) can reduce the amount of data transferred, but also increase the overhead of coherence maintenance. A coarser granularity (e.g., an object or a segment) can reduce the coherence overhead, but also increase the amount of false sharing and network traffic.
- **Structure**: This refers to the organization and layout of the shared memory space. The structure can be flat, hierarchical, or segmented, depending on the degree of uniformity and locality of the shared data. A flat structure can simplify the address translation and access control, but also increase the contention and fragmentation of the shared space. A hierarchical or segmented structure can exploit the locality and heterogeneity of the shared data, but also complicate the management and consistency of the shared space.
- **Coherence semantics**: This refers to the rules and guarantees that define the behavior and correctness of the shared memory accesses. The coherence semantics can be strict, relaxed, or weak, depending on the degree of synchronization and ordering of the shared memory operations. A strict semantics (e.g., sequential consistency) can simplify the programming and debugging of the distributed applications, but also limit the performance and scalability of the DSM system. A relaxed or weak semantics (e.g., release consistency or eventual consistency) can improve the performance and scalability of the DSM system, but also increase the complexity and difficulty of the programming and debugging of the distributed applications.
- **Coherence protocols**: This refers to the mechanisms and algorithms that implement the coherence semantics and ensure the consistency and validity of the shared memory data. The coherence protocols can be based on replication, migration, or invalidation, depending on the strategy of distributing and updating the shared memory blocks. A replication-based protocol can improve the availability and fault-tolerance of the shared memory data, but also increase the storage and communication overhead. A migration-based protocol can reduce the storage and communication overhead, but also increase the latency and contention of the shared memory accesses. An invalidation-based protocol can balance the storage and communication overhead, but also require the coordination and synchronization of the nodes.
- **Scalability**: This refers to the ability of the DSM system to handle the increase in the number of nodes, processes, and shared memory data. The scalability of the DSM system depends on the design choices and trade-offs of the above issues, as well as the characteristics and requirements of the distributed applications. A scalable DSM system should be able to adapt to the dynamic and heterogeneous environment of the distributed system, and provide efficient and reliable performance and functionality to the distributed applications.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on the algorithm for implementation of distributed shared memory for the notes of the unit 5 - distributed resource management in the subject of distributed system.

### Algorithm for Implementation of Distributed Shared Memory

Distributed shared memory (DSM) is a technique that allows multiple processes on different nodes of a distributed system to access a common virtual address space as if they were running on a single machine. DSM can simplify the programming of distributed applications by providing a familiar and consistent memory model across the nodes. However, DSM also introduces challenges such as maintaining coherence, consistency, and performance of the shared data.

There are different algorithms for implementing DSM, each with its own advantages and disadvantages. Some of the basic algorithms are:

- **Central server algorithm**: In this algorithm, a central server maintains all the shared data and services the read and write requests from the other nodes. The central server can use a page-based or an object-based approach to manage the shared data. The advantage of this algorithm is that it is simple and ensures coherence and consistency of the shared data. The disadvantage is that it introduces a single point of failure and a bottleneck for communication and computation.

- **Migration algorithm**: In this algorithm, the shared data is initially stored at the central server, but it can migrate to other nodes upon request. The node that requests a data item becomes the owner of that item and can read and write it locally. The central server keeps track of the current location of each data item. The advantage of this algorithm is that it reduces the communication overhead and improves the locality of access. The disadvantage is that it may cause frequent data migration and inconsistency if multiple nodes access the same data item.

- **Replication algorithm**: In this algorithm, the shared data is replicated on multiple nodes, and each node can read the local copy of the data. However, to write a data item, a node must obtain a write permission from the central server, which ensures that only one node can write the data item at a time. The central server also broadcasts the write updates to all the nodes that have a copy of the data item. The advantage of this algorithm is that it allows concurrent reads and reduces the communication latency. The disadvantage is that it consumes more memory and bandwidth and may cause coherence problems if the updates are delayed or lost.

- **Invalidation algorithm**: In this algorithm, the shared data is also replicated on multiple nodes, but each node must validate its local copy before reading or writing the data. The central server maintains a version number for each data item, which is incremented whenever the data item is written. The node that wants to access a data item must compare its local version number with the global version number at the central server. If the local version is outdated, the node must invalidate its local copy and request a fresh copy from the central server or another node. The advantage of this algorithm is that it avoids unnecessary data transfers and allows concurrent reads. The disadvantage is that it may cause frequent invalidations and validations and increase the communication overhead.



## Unit 6 - Failure Recovery in Distributed Systems

- Failure recovery is the process of restoring a distributed system to a consistent and correct state after one or more components fail.
- Failure recovery is important for ensuring the availability, reliability, and correctness of distributed systems.
- Failure recovery can be classified into two types: backward recovery and forward recovery.
- Backward recovery involves undoing the effects of erroneous or incomplete actions and restoring the system to a previous consistent state.
- Forward recovery involves correcting or compensating for the errors and continuing the execution from the current state.
- Backward recovery can be implemented using techniques such as checkpoints, logging, rollback, and replay.
- Checkpoints are snapshots of the system state that are periodically saved on stable storage.
- Logging is the recording of the actions or events that occur in the system on stable storage.
- Rollback is the process of restoring the system state to a previous checkpoint.
- Replay is the process of re-executing the actions or events that occurred after the checkpoint.
- Forward recovery can be implemented using techniques such as redundancy, replication, voting, and exception handling.
- Redundancy is the provision of extra resources or components that can take over the functionality of the failed ones.
- Replication is the creation of multiple copies of the same data or service that can be accessed by different components.
- Voting is the mechanism of reaching a consensus among the replicas or components on the correct value or action.
- Exception handling is the mechanism of detecting, reporting, and handling the errors or failures that occur in the system.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on the concepts of backward and forward recovery in distributed systems.

### Concepts in Backward and Forward Recovery

- **Backward recovery** is a technique that restores the system state to a previous error-free state after a failure occurs. It involves three steps:
  - **Checkpointing**: periodically saving the system state to a stable storage.
  - **Logging**: recording the actions performed by the system to a log file.
  - **Rollback**: undoing the effects of the actions that occurred after the last checkpoint.
- **Forward recovery** is a technique that corrects the errors in the system state and allows the system to continue its normal execution. It involves two steps:
  - **Error detection**: identifying the errors in the system state and their causes.
  - **Error correction**: applying appropriate actions to remove the errors and restore the system state to a consistent condition.
- The main difference between backward and forward recovery is that backward recovery discards the work done after the last checkpoint, while forward recovery preserves the work done and tries to fix the errors.
- The advantages of backward recovery are that it is more general and does not require the knowledge of the nature of faults. The disadvantages are that it may cause more overhead, waste of resources, and loss of useful information.
- The advantages of forward recovery are that it avoids the rollback of the system state and reduces the recovery time. The disadvantages are that it may require more complex error detection and correction mechanisms and may not be applicable to all types of faults.



### Recovery in Concurrent Systems

Recovery in concurrent systems is the process of restoring the consistency and correctness of data and operations in a system that involves multiple transactions executing simultaneously. Recovery is necessary when a failure occurs, such as a system crash, a power outage, a network partition, or a malicious attack, that may cause some transactions to abort or lose data.

There are different techniques for recovery in concurrent systems, depending on the type of failure, the concurrency control mechanism, and the system architecture. Some of the common techniques are:

- **Backward recovery**: This technique involves undoing the effects of aborted or incomplete transactions by restoring the system to a previous consistent state. This can be done by using logs, checkpoints, or backups that record the changes made by transactions. Backward recovery requires the ability to identify and undo the operations of each transaction, and to ensure that the undo operations do not interfere with other transactions. Backward recovery is suitable for centralized or distributed systems that use pessimistic concurrency control, such as locking or timestamp ordering .

- **Forward recovery**: This technique involves redoing the effects of committed or completed transactions by applying the changes to the current state of the system. This can be done by using logs, checkpoints, or backups that record the committed transactions and their outputs. Forward recovery requires the ability to identify and redo the operations of each transaction, and to ensure that the redo operations do not conflict with other transactions. Forward recovery is suitable for centralized or distributed systems that use optimistic concurrency control, such as validation or multiversioning .

- **Concurrent recovery**: This technique involves recovering multiple media sets (such as disks, tapes, or optical devices) using concurrent recovery sessions. Multiple media sets are typically created when performing backups using parallel device resources. Concurrent recovery allows the system to recover faster and more efficiently by using multiple devices and sessions to restore the data. Concurrent recovery requires the ability to coordinate and synchronize the recovery sessions, and to ensure that the recovered data is consistent and correct. Concurrent recovery is suitable for centralized or distributed systems that use parallel backup and recovery tools, such as IBM's Backup, Recovery and Media Services (BRMS) for i .

- **Compensation**: This technique involves applying compensating actions to correct the effects of aborted or incomplete transactions. A compensating action is an operation that reverses or nullifies the logical effect of another operation, without undoing the physical changes. For example, if a transaction debits an account, a compensating action would be to credit the same account. Compensation requires the ability to define and execute the compensating actions for each transaction, and to ensure that the compensation does not violate the system constraints or business rules. Compensation is suitable for distributed systems that use asynchronous or loosely coupled communication, such as message passing or event-driven architectures .



### Obtaining consistent Checkpoints for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Failure recovery in distributed systems is the process of restoring the system to a consistent and correct state after a failure occurs.
- A failure is an event that causes a deviation from the expected behavior of the system.
- Failures can be classified into different types, such as crash failures, omission failures, timing failures, response failures, Byzantine failures, etc .
- A checkpoint is a snapshot of the system state at a certain point in time, which can be used to resume the execution after a failure.
- Obtaining consistent checkpoints is a challenge in distributed systems, because the system consists of multiple processes that may communicate and synchronize with each other.
- A consistent checkpoint is a set of checkpoints from different processes that reflects a global state of the system that could have occurred during the normal execution.
- A consistent checkpoint should satisfy the following properties:
  - No orphan message: A message is orphan if it is sent by a process before its checkpoint, but received by another process after its checkpoint.
  - No lost message: A message is lost if it is sent by a process after its checkpoint, but received by another process before its checkpoint.
- There are different techniques to obtain consistent checkpoints, such as coordinated checkpointing, uncoordinated checkpointing, and communication-induced checkpointing .
- Coordinated checkpointing is a technique where all the processes in the system agree on a global checkpoint and take their local checkpoints simultaneously.
- Coordinated checkpointing has the advantages of simplicity, no orphan messages, and easy recovery, but it has the disadvantages of high overhead, blocking, and domino effect.
- Domino effect is the phenomenon where a failure of one process may cause the rollback of other processes that depend on it, potentially to the initial state.
- Uncoordinated checkpointing is a technique where each process takes its local checkpoint independently, without any coordination with other processes.
- Uncoordinated checkpointing has the advantages of low overhead, non-blocking, and no domino effect, but it has the disadvantages of complexity, orphan messages, and difficult recovery.
- Communication-induced checkpointing is a technique where each process takes its local checkpoint based on the information piggybacked on the messages it sends or receives.
- Communication-induced checkpointing has the advantages of low overhead, non-blocking, and no domino effect, but it has the disadvantages of complexity, dependency tracking, and potential useless checkpoints.
- To obtain consistent checkpoints, the system should also have a stable storage, which is a storage device that can resist major disasters and preserve the checkpoints.

: Failure Recovery in Distributed Systems - 1000 Projects
: Recovery in Distributed Systems - GeeksforGeeks
: 1 Zorro: Zero-Cost Reactive Failure Recovery in ...
: Various Failures in Distributed Systems - tutorialspoint.com
: Handling Failure in Distributed System - GeeksforGeeks



### Recovery in Distributed Database Systems

- Recovery in distributed database systems is the process of restoring the database to a consistent state after a failure or an error .
- Recovery in distributed database systems is more complicated than in centralized database systems because failures can occur at the communication links or a remote site.
- Recovery in distributed database systems aims to maintain the atomicity and durability of distributed transactions, which means that all statements in a transaction, distributed or non-distributed, either commit or roll back as a unit.
- Recovery in distributed database systems can be classified into two types: transaction recovery and system recovery.
- Transaction recovery is done to eliminate the adverse effects of faulty transactions rather than to recover from a failure. Faulty transactions include all transactions that have changed the database into an undesired state and the transactions that have used values written by the faulty transactions.
- Transaction recovery can be achieved by using undo or redo operations, depending on the state of the transaction at the time of failure. Undo operations restore the database to its state before the transaction started, while redo operations restore the database to its state after the transaction committed.
- Transaction recovery can be implemented by using different protocols, such as two-phase commit protocol, three-phase commit protocol, or majority protocol, which coordinate the commit or abort decisions of the subtransactions at different sites .
- System recovery is done to restore the database to a consistent state after a failure that causes extensive damage to the database, such as disk crash or power outage.
- System recovery can be achieved by using backup copies of the database, which are periodically created and stored on archival media, such as tapes or disks.
- System recovery can be implemented by using different techniques, such as shadow paging, checkpointing, or logging, which record the changes made to the database or the state of the database at certain points in time .
- System recovery can be performed by using different strategies, such as deferred update, immediate update, or fuzzy update, which determine when the changes made by the transactions are written to the database or the backup copy .



## Unit 7 - Fault Tolerance

- Fault tolerance is the ability of a system to continue functioning correctly in the presence of failures.
- Fault tolerance can be achieved by using techniques such as redundancy, replication, recovery, and reconfiguration.
- Fault tolerance can be classified into two types: hardware fault tolerance and software fault tolerance.
- Hardware fault tolerance is the ability of a system to tolerate failures of physical components, such as processors, memory, disks, or network devices.
- Hardware fault tolerance can be achieved by using techniques such as:
  - Static redundancy: using multiple identical components that perform the same function in parallel, and selecting the correct output from a majority vote.
  - Dynamic redundancy: using spare components that can replace failed ones on the fly, and transferring the state and workload of the failed component to the spare one.
  - Error detection and correction: using mechanisms such as parity bits, checksums, or error-correcting codes to detect and correct errors in data transmission or storage.
- Software fault tolerance is the ability of a system to tolerate failures of software components, such as modules, processes, or threads.
- Software fault tolerance can be achieved by using techniques such as:
  - Exception handling: using mechanisms such as try-catch blocks, signals, or interrupts to handle errors or exceptions that occur during the execution of a program.
  - Checkpointing and rollback: using mechanisms such as logs, snapshots, or backups to save the state of a program at regular intervals, and restoring the state from the most recent checkpoint in case of a failure.
  - Process replication: using mechanisms such as forks, threads, or distributed systems to create multiple copies of a process that execute the same or similar tasks, and coordinating the results among them.
  - Rejuvenation: using mechanisms such as restarts, reboots, or garbage collection to refresh the state of a program or a system periodically, and prevent the accumulation of errors or resource leaks.



### Issues in Fault Tolerance for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Fault tolerance is the ability of a system to continue functioning correctly in the presence of failures.
- Fault tolerance is important for distributed systems because they consist of multiple components that may be subject to different types of failures, such as hardware failures, software failures, network failures, malicious attacks, etc .
- Fault tolerance can be achieved by using various techniques, such as redundancy, replication, checkpointing, recovery, consensus, etc .
- Fault tolerance can be classified into different levels, such as detection, masking, tolerance, recovery, and prevention.
- Fault tolerance can also be categorized into different models, such as fail-stop, fail-silent, fail-safe, fail-recover, etc.
- Fault tolerance can be evaluated by using different metrics, such as reliability, availability, dependability, etc .
- Fault tolerance can be implemented by using different algorithms, such as Byzantine agreement, Paxos, Raft, etc.
- Fault tolerance can be challenged by various issues, such as scalability, consistency, performance, security, etc .



### Commit Protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Commit protocols are algorithms that ensure the atomicity of distributed transactions, i.e., all the sites involved in a transaction either commit or abort it unanimously, even in the presence of failures  .
- Commit protocols are necessary to maintain the consistency and reliability of distributed systems, as they prevent partial execution or data loss due to network or site failures  .
- There are different types of commit protocols, such as one-phase commit (1PC), two-phase commit (2PC), and three-phase commit (3PC), each with its own advantages and disadvantages    .
- One-phase commit (1PC) is the simplest commit protocol, where the coordinator sends a commit or abort message to all the participants, and they execute it accordingly . However, 1PC is not fault-tolerant, as it does not handle the case where the coordinator or some participants fail or become unreachable .
- Two-phase commit (2PC) is the most widely used commit protocol, where the coordinator initiates a voting phase, where it asks all the participants to prepare and vote to commit or abort, and then a decision phase, where it collects the votes and broadcasts the final decision to all the participants    . 2PC ensures the atomicity and durability of distributed transactions, but it has a blocking problem, where the participants have to wait indefinitely for the coordinator's decision if the coordinator fails or becomes unreachable    .
- Three-phase commit (3PC) is an extension of 2PC, where the coordinator adds a pre-commit phase, where it sends a pre-commit message to all the participants after receiving all the votes, and waits for their acknowledgments before sending the final commit or abort message . 3PC is a non-blocking commit protocol, as it allows the participants to reach a consensus without the coordinator's decision in case of failures, by using a timeout mechanism and a majority rule . However, 3PC requires more messages and rounds of communication, and it cannot handle network partitions .



# Voting protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Voting protocols are a type of consensus protocols that allow a set of distributed nodes to agree on a common value or decision.
- Voting protocols are useful for achieving fault tolerance in distributed systems, as they can tolerate the failure or malicious behavior of some nodes, as long as a majority of nodes are correct and reachable.
- Voting protocols can be classified into two categories: exact voting and inexact voting.
  - Exact voting requires that all nodes agree on the same value or decision, and that the value or decision is correct according to some predefined criterion. Examples of exact voting are the two-phase commit protocol and the Paxos algorithm.
  - Inexact voting allows some degree of disagreement or error among the nodes, as long as the value or decision is acceptable according to some predefined criterion. Examples of inexact voting are the weighted voting protocol and the Byzantine agreement protocol.
- Voting protocols can also be classified into two categories based on the security properties they provide: secure voting and non-secure voting.
  - Secure voting ensures that the value or decision agreed by the nodes is not influenced by malicious nodes or external attackers, and that the voting process is confidential and verifiable. Examples of secure voting are the secret sharing scheme and the digital signature scheme.
  - Non-secure voting does not provide any security guarantees, and relies on the assumption that the nodes are honest and the network is reliable. Examples of non-secure voting are the majority voting protocol and the plurality voting protocol.
- Voting protocols can be evaluated based on several criteria, such as fairness, efficiency, scalability, robustness, and simplicity.
  - Fairness measures how equally the nodes are treated in the voting process, and how their preferences or weights are reflected in the value or decision. Fairness can be formalized using concepts such as anonymity, neutrality, monotonicity, and proportionality.
  - Efficiency measures how fast and how cheap the voting process is, in terms of communication, computation, and storage costs. Efficiency can be formalized using concepts such as latency, throughput, bandwidth, and complexity.
  - Scalability measures how well the voting protocol can handle a large number of nodes or a dynamic network topology. Scalability can be formalized using concepts such as fault tolerance, adaptability, and self-organization.
  - Robustness measures how resilient the voting protocol is to failures or attacks, and how it can recover from them. Robustness can be formalized using concepts such as reliability, availability, consistency, and security.
  - Simplicity measures how easy the voting protocol is to understand, implement, and verify. Simplicity can be formalized using concepts such as elegance, clarity, and correctness.



### Dynamic voting protocols

- Dynamic voting protocols are techniques for consistency and recovery control of replicated files in distributed systems  .
- The purpose of a replicated file is to improve the availability of a logical file in the presence of site failures and network partitions  .
- A dynamic voting protocol assigns a number of votes to each copy of a replicated file, and allows a group of copies to access the file only if they have a majority of votes   .
- The number of votes assigned to each copy can change dynamically depending on the system state, such as the number of copies, the network topology, the failure pattern, etc    .
- Dynamic voting protocols can improve the performance and reliability of distributed systems by reducing the communication overhead, balancing the load, and tolerating failures    .
- Some examples of dynamic voting protocols are:
  - Topological dynamic voting: assigns votes based on the connectivity of the copies and the network partitions.
  - Weighted voting: assigns votes based on the importance or preference of the copies  .
  - Quorum-based voting: assigns votes based on the size of the quorum, which is a subset of copies that must agree on the file access.



## Unit 8 - Transactions and Concurrency Control

A transaction is a logical unit of work that consists of a sequence of database operations, such as queries, updates, inserts, or deletes. A transaction has the following properties:

- Atomicity: A transaction is either executed in its entirety or not at all. If any operation in the transaction fails, the entire transaction is aborted and the database is restored to its previous state.
- Consistency: A transaction preserves the consistency of the database by ensuring that it satisfies all the integrity constraints and business rules before and after its execution.
- Isolation: A transaction executes independently of other concurrent transactions and does not interfere with them. The intermediate results of a transaction are not visible to other transactions until the transaction commits.
- Durability: The effects of a committed transaction are permanent and persist even in the event of system failures or power outages.

Concurrency control is the process of managing the simultaneous execution of multiple transactions in a shared database system. Concurrency control ensures that the transactions do not conflict with each other and maintain the consistency and isolation properties. Concurrency control can be implemented using various techniques, such as:

- Locking: A locking mechanism grants exclusive or shared access to a data item or a set of data items to a transaction. A transaction must acquire a lock before accessing a data item and release the lock after finishing the access. Locking prevents concurrent transactions from modifying the same data item or reading an uncommitted value of a data item.
- Timestamping: A timestamping mechanism assigns a unique timestamp to each transaction and uses the timestamps to order the transactions. A transaction can access a data item only if its timestamp is older than the timestamp of the last transaction that modified the data item. Timestamping avoids the need for locking and prevents deadlock situations.
- Validation: A validation mechanism executes a transaction in three phases: read phase, validation phase, and write phase. In the read phase, the transaction reads the data items from the database but does not modify them. In the validation phase, the transaction checks whether its read set and write set conflict with any other concurrent transaction. If there is no conflict, the transaction proceeds to the write phase and commits its changes to the database. Otherwise, the transaction is aborted and restarted. Validation ensures that the transactions are serializable, meaning that their concurrent execution is equivalent to some sequential execution.



# Transactions

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the operations in a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction does not interfere with other concurrent transactions.
- Durability means that the effects of a transaction are permanent even in the case of failures.

# Concurrency Control

- Concurrency control is the process of managing simultaneous execution of transactions in a shared database, to ensure the consistency and isolation properties of transactions.
- Concurrency control techniques can be broadly classified into two categories: lock-based protocols and timestamp-based protocols.
- Lock-based protocols use locks to prevent conflicting operations from accessing the same data item. A lock is a variable associated with a data item that describes the status of the item with respect to possible operations that can be applied to it.
- Timestamp-based protocols use timestamps to order the transactions and ensure serializability. A timestamp is a unique identifier assigned to each transaction that reflects its start time. Timestamps can be either logical or physical.

# Distributed Transactions and Distributed Concurrency Control

- A distributed transaction is a transaction that accesses data from multiple data servers that are connected by a computer network.
- A distributed transaction consists of a set of subtransactions, each of which is executed by one data server.
- Distributed concurrency control provides a mechanism to synchronize distributed transactions in such a way that the ACID properties are not violated by their interleaved execution.
- Distributed concurrency control makes sure that all subtransactions of a set of distributed transactions are serialized identically in all data servers involved. Therefore, not only local dependencies need to be taken into account, but also dependencies involving multiple data servers.
- Distributed concurrency control techniques can be classified into two categories: centralized and decentralized.
- Centralized techniques use a single coordinator to manage the locks or timestamps of all data servers. The coordinator is responsible for granting or denying requests from transactions, and for detecting and resolving conflicts and deadlocks.
- Decentralized techniques use a distributed algorithm to coordinate the locks or timestamps of all data servers. Each data server communicates with other data servers to exchange information and reach a consensus on the serialization order of transactions.



### Nested transactions for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A transaction is a sequence of operations that satisfies the ACID properties (Atomicity, Consistency, Isolation, Durability).
- A distributed transaction is a transaction that accesses objects handled by different servers in a distributed system.
- A nested transaction is a transaction that contains subtransactions within it, each with its own begin and end points.
- Nested transactions can be used to improve the performance, reliability, and modularity of distributed transactions.
- Nested transactions have the following characteristics:
  - A subtransaction can commit or abort independently of its parent transaction, but its effects are not visible to other transactions until the parent transaction commits.
  - A subtransaction can inherit the locks and resources of its parent transaction, or it can acquire its own locks and resources.
  - A subtransaction can be retried or compensated in case of failure, without affecting the rest of the parent transaction.
  - A subtransaction can be nested within another subtransaction, forming a hierarchy of transactions.
- Nested transactions can be classified into two types: closed nested transactions and open nested transactions.
  - Closed nested transactions are those that follow the strict two-phase locking protocol, which ensures serializability and recoverability of transactions. They are also called flat transactions or subtransactions.
  - Open nested transactions are those that allow subtransactions to release their locks and resources before the parent transaction commits, which improves concurrency and availability of transactions. They are also called sagas or compensating transactions.



### Locks for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A lock is a mechanism that allows only one of the innumerable nodes or processes to access and modify a resource or data that is being shared commonly to prevent execution of same task twice and also maintain data integrity.
- Locks are designed to enforce a mutual exclusion concurrency control policy, which means that only one transaction can hold a lock on a data item at a time.
- Locks can be classified into different types based on the following criteria:
  - The granularity of the data item being locked, such as record-level, page-level, or table-level locks.
  - The mode of the lock, such as shared (read) or exclusive (write) locks.
  - The duration of the lock, such as long (until the transaction commits or aborts) or short (until the operation finishes) locks.
  - The protocol of acquiring and releasing locks, such as two-phase locking (2PL), timestamp ordering, or optimistic concurrency control.
- In distributed systems, locks can be implemented using different strategies, such as:
  - Centralized locking, where a single node acts as a lock manager and grants or denies lock requests from other nodes.
  - Distributed locking, where each node manages its own locks and communicates with other nodes to coordinate lock requests.
  - Hierarchical locking, where the nodes are organized into a tree structure and lock requests are propagated from the leaves to the root or vice versa.
- Distributed locks can also be based on different security levels of the lock resources, such as:
  - Distributed systems based on asynchronous replication, such as MySQL, Tair, and Redis, where the lock resource is replicated on multiple nodes and the lock is granted by the primary node or a quorum of nodes.
  - Paxos-based distributed consensus systems, such as ZooKeeper, etcd, and Consul, where the lock resource is stored on a cluster of nodes that use a consensus algorithm to agree on the lock state.
- Distributed locks are useful for coordinating access to shared resources in a distributed system, but they also have some challenges and limitations, such as:
  - Lock contention, where multiple transactions compete for the same lock and cause delays or deadlocks.
  - Lock availability, where the lock manager or the lock resource may fail or become unreachable and cause lock failures or inconsistencies.
  - Lock performance, where the lock operations may incur network overhead or latency and affect the throughput or responsiveness of the system.
- Distributed locks should be used with caution and only when necessary, as they may introduce more complexity and risk than benefit. Some alternatives or complements to distributed locks are:
  - Idempotent operations, where the same operation can be repeated without changing the outcome or causing side effects.
  - Conflict-free replicated data types (CRDTs), where the data can be replicated and modified on multiple nodes without requiring coordination or synchronization.
  - Event sourcing and command query responsibility segregation (CQRS), where the data is stored as a sequence of events and the queries are separated from the commands.



### Optimistic Concurrency Control

- Optimistic concurrency control (OCC) is a concurrency control method applied to transactional systems such as relational database management systems and software transactional memory.
- OCC assumes that multiple transactions can frequently complete without interfering with each other, and does not require locking or timestamping techniques.
- OCC consists of two or three phases: read, validation and write.
- In the read phase, a transaction reads the data from the database and performs its operations without any restrictions.
- In the validation phase, a transaction checks if it has any conflicts with other transactions that have committed since the read phase.
- A conflict occurs when two transactions access the same data item and at least one of them modifies it.
- If there are no conflicts, the transaction proceeds to the write phase, where it writes its updates to the database and commits.
- If there are conflicts, the transaction aborts and restarts from the beginning or from a checkpoint.
- OCC has the advantage of allowing high concurrency and avoiding deadlocks, as transactions do not hold any locks during their execution.
- OCC also reduces the communication overhead in distributed systems, as transactions do not need to coordinate with each other until the validation phase.
- OCC has the disadvantage of wasting resources and increasing latency, as transactions may have to abort and restart due to conflicts.
- OCC also requires a mechanism to detect and resolve conflicts, which can be challenging in distributed systems with partial failures and network delays.
- OCC is suitable for applications where conflicts are rare and transactions are short-lived, such as online shopping and social networking.
- OCC is not suitable for applications where conflicts are frequent and transactions are long-lived, such as banking and reservation systems.



### Timestamp ordering for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- Timestamp ordering is a class of concurrency control protocols that use timestamps to determine the serializability order of transactions in a distributed system .
- A timestamp is a monotonically increasing number that is often based on the system clock or a logical clock .
- A transaction is assigned a timestamp when it starts, and this timestamp is used to order the transactions and resolve conflicts .
- There are two types of timestamp ordering protocols: basic timestamp ordering and optimistic timestamp ordering .
- Basic timestamp ordering protocol uses two timestamps for each data item: read timestamp (RTS) and write timestamp (WTS). RTS is the largest timestamp of any transaction that has successfully read the data item. WTS is the largest timestamp of any transaction that has successfully written the data item .
- Basic timestamp ordering protocol enforces two rules: read-write rule and write-write rule. Read-write rule states that a transaction T can read a data item X only if T's timestamp is greater than or equal to X's WTS. Write-write rule states that a transaction T can write a data item X only if T's timestamp is greater than both X's RTS and X's WTS .
- If a transaction T violates either of the rules, it is aborted and restarted with a new timestamp .
- Basic timestamp ordering protocol ensures conflict serializability, but it may cause cascading aborts, where aborting one transaction causes other transactions to abort as well .
- Optimistic timestamp ordering protocol avoids cascading aborts by using three phases for each transaction: read phase, validation phase, and write phase .
- In the read phase, a transaction T reads the data items from the database and stores them in a private workspace. T is not allowed to write any data item to the database in this phase .
- In the validation phase, a transaction T checks whether it can commit without violating serializability. T is assigned a validation timestamp (VTS) when it enters this phase. T compares its VTS with the RTS and WTS of the data items it has read or written. T can commit only if it satisfies the following conditions :
  - For each data item X that T has read, T's VTS must be greater than or equal to X's WTS.
  - For each data item X that T has written, T's VTS must be greater than X's RTS and X's WTS.
- If T fails to satisfy either of the conditions, it is aborted and restarted with a new timestamp .
- In the write phase, a transaction T writes the data items from its private workspace to the database. T is assigned a commit timestamp (CTS) when it enters this phase. T updates the RTS and WTS of the data items it has written with its CTS .
- Optimistic timestamp ordering protocol ensures conflict serializability and avoids cascading aborts, but it may cause more aborts than basic timestamp ordering protocol, especially when the system is highly concurrent .



# Comparison of methods for concurrency control

Concurrency control is the process of managing the simultaneous execution of transactions in a distributed system, such that the consistency and correctness of the data are preserved. Concurrency control methods can be classified into two main categories: pessimistic and optimistic.

Pessimistic methods prevent conflicts from occurring by using locks, timestamps, or other mechanisms to coordinate the access to shared data. Optimistic methods allow conflicts to occur, but detect and resolve them before committing the transactions.

Some of the common concurrency control methods are:

- Two-phase locking (2PL): This is a pessimistic method that requires each transaction to acquire locks on the data items it needs to access, and release them after it is done. There are two phases: the growing phase, where the transaction can only acquire locks, and the shrinking phase, where the transaction can only release locks. 2PL ensures serializability, which means that the concurrent execution of transactions is equivalent to some serial execution. However, 2PL may cause deadlocks, where two or more transactions are waiting for each other to release locks, and thus block indefinitely.

- Timestamp ordering (TO): This is another pessimistic method that assigns a unique timestamp to each transaction, and uses it to order the access to shared data. Each data item has two timestamps: the read timestamp (RTS), which records the latest time when the data item was read, and the write timestamp (WTS), which records the latest time when the data item was written. A transaction can read a data item only if its timestamp is greater than or equal to the WTS of the data item, and can write a data item only if its timestamp is greater than both the RTS and the WTS of the data item. Otherwise, the transaction is aborted and restarted with a new timestamp. TO ensures serializability and avoids deadlocks, but may cause more aborts and restarts than 2PL.

- Multi-version concurrency control (MVCC): This is an optimistic method that allows multiple versions of the same data item to coexist, and assigns a timestamp to each version. A transaction can read the latest version of a data item that was committed before the transaction started, and can write a new version of a data item without affecting the existing versions. When a transaction is ready to commit, it validates its read set and write set against the current versions of the data items, and checks if there are any conflicts. If there are no conflicts, the transaction commits and its new versions become visible to other transactions. Otherwise, the transaction aborts and restarts. MVCC ensures serializability and avoids locking and blocking, but requires more storage space and garbage collection for the old versions.

- Validation concurrency control (VCC): This is another optimistic method that divides the execution of a transaction into three phases: the read phase, where the transaction reads the data items it needs, the validation phase, where the transaction checks if there are any conflicts with other transactions, and the write phase, where the transaction writes the data items it modified. The validation phase uses a validation test, such as the serial validation test or the snapshot isolation test, to determine if the transaction can commit or abort. VCC ensures serializability or snapshot isolation, depending on the validation test, and avoids locking and blocking, but requires more computation and communication for the validation phase.

The choice of the concurrency control method depends on the characteristics of the distributed system, such as the network latency, the data distribution, the transaction workload, and the performance requirements. There is no single best method for all scenarios, and each method has its own advantages and disadvantages.



```markdown
## Unit 9 - Distributed Transactions

- A distributed transaction is a transaction that works across several computers or data repositories (especially databases)   .
- A distributed transaction should satisfy the ACID properties (atomicity, consistency, isolation, and durability)  .
- A distributed transaction is typically coordinated by a transaction manager, which is responsible for creating and managing a global transaction that encompasses all operations against the transactional resources  .
- A distributed transaction may use different protocols or methods to achieve coordination and consensus among the participants, such as two-phase commit, three-phase commit, Paxos, or Raft .
- A distributed transaction may face various challenges or issues, such as network failures, concurrency conflicts, data inconsistencies, or security risks  .
- A distributed transaction may have different benefits or drawbacks, depending on the application domain, the system architecture, and the performance requirements  .
```



### Flat and Nested Distributed Transactions

A distributed transaction is a transaction that accesses objects managed by multiple servers. A distributed transaction must maintain the ACID properties of a transaction, which means that it must be atomic, consistent, isolated, and durable. Atomicity means that either all the changes made by the transaction are committed or none of them are. Consistency means that the transaction preserves the integrity constraints of the data. Isolation means that the transaction does not interfere with other concurrent transactions. Durability means that the committed changes are permanent and survive failures.

There are two ways to structure a distributed transaction: flat or nested.

- A flat transaction has a single begin point and a single end point, where it either commits or aborts. A flat transaction is simple and suitable for short activities, but it may have problems with concurrency control, deadlock detection, and recovery. A flat transaction uses a two-phase commit protocol to coordinate the commit or abort decision among all the servers involved in the transaction. The two-phase commit protocol consists of a prepare phase and a commit phase. In the prepare phase, the coordinator asks all the servers to vote on whether they are ready to commit or not. In the commit phase, the coordinator decides to commit or abort based on the votes, and informs all the servers of the decision.

- A nested transaction is a transaction that consists of subtransactions, which may themselves be nested. A nested transaction has a partial commit point for each subtransaction, and a global commit point for the whole transaction. A nested transaction is more flexible and suitable for complex and long-running activities, but it may have problems with consistency and isolation. A nested transaction uses a two-phase commit protocol for each subtransaction, and a multilevel commit protocol for the whole transaction. The multilevel commit protocol consists of a bottom-up phase and a top-down phase. In the bottom-up phase, the subtransactions are committed from the lowest level to the highest level. In the top-down phase, the whole transaction is committed from the highest level to the lowest level.



# Atomic Commit Protocols for Distributed Transactions

- A distributed transaction is a transaction that involves multiple servers or nodes in a distributed system. A distributed transaction must satisfy the ACID properties: atomicity, consistency, isolation, and durability.
- Atomicity means that either all the operations of a transaction are executed or none of them are. Atomicity is important for maintaining the consistency and integrity of the data in the system.
- An atomic commit protocol is a protocol that ensures that a distributed transaction is either committed or rolled back in its entirety, even if the system fails or some of the nodes fail or crash.
- There are different types of atomic commit protocols, such as two-phase commit (2PC), three-phase commit (3PC), parallel commit, and failure-aware atomic commit (FLAC).
- Two-phase commit (2PC) is the most widely used atomic commit protocol. It consists of two phases: a prepare phase and a commit phase. In the prepare phase, a coordinator node sends a prepare message to all the participant nodes and waits for their votes. If all the participants vote yes, the coordinator sends a commit message to all of them and commits the transaction. If any of the participants vote no or timeout, the coordinator sends an abort message to all of them and aborts the transaction.
- Three-phase commit (3PC) is an extension of 2PC that adds a pre-commit phase between the prepare and commit phases. In the pre-commit phase, the coordinator sends a pre-commit message to all the participants after receiving their votes. The participants acknowledge the pre-commit message and wait for the final decision. In the commit phase, the coordinator sends a commit or abort message to all the participants based on the pre-commit acknowledgments. 3PC can tolerate some failures that 2PC cannot, such as network partitions and coordinator crashes, but it has higher latency and complexity.
- Parallel commit is a new atomic commit protocol that reduces the latency of transactions to only a single round-trip of distributed consensus. It does not use a coordinator node or a prepare phase. Instead, it uses a timestamp oracle to assign a commit timestamp to each transaction. The participants write their intents to the storage layer with the commit timestamp and wait for the consensus layer to confirm that the timestamp is safe. If the timestamp is safe, the transaction is committed. If the timestamp is not safe, the transaction is aborted. Parallel commit can achieve high performance and scalability, but it requires a reliable and fast timestamp oracle and consensus layer.
- Failure-aware atomic commit (FLAC) is a practical atomic commit protocol that leverages the failure information of the nodes to optimize the commit decision. It uses a coordinator node and a two-phase transaction processing framework. In the first phase, the coordinator sends a prepare message to all the participants and waits for their votes. If all the participants vote yes, the coordinator sends a commit message to all of them and commits the transaction. If any of the participants vote no or timeout, the coordinator checks the failure information of the nodes. If the coordinator knows that the failed node has not executed any operation of the transaction, it can commit the transaction without waiting for the failed node. If the coordinator does not know the status of the failed node, it aborts the transaction. FLAC can improve the commit rate and latency of transactions, but it requires a failure detection mechanism and a failure-aware storage layer.



### Concurrency control in distributed transactions

- Concurrency control is the process of managing the concurrent execution of transactions in a distributed database system, such that the ACID properties are preserved .
- Concurrency control is necessary to avoid conflicts and inconsistencies that may arise due to the interleaved execution of transactions that access and modify shared data .
- Concurrency control can be achieved by using various techniques, such as locking, timestamping, optimistic methods, or serialization .
- Locking-based concurrency control protocols use the concept of locking data items before accessing or modifying them, to prevent other transactions from interfering with them .
- Timestamp-based concurrency control algorithms use a transaction’s timestamp to order the execution of conflicting operations, such that older transactions have priority over newer ones .
- Optimistic concurrency control methods assume that conflicts are rare and allow transactions to execute without any synchronization, but validate them before committing to ensure serializability .
- Serialization is the property that ensures that the concurrent execution of transactions is equivalent to some serial execution of the same transactions, where no two transactions are interleaved .
- Distributed concurrency control protocols have to deal with additional challenges, such as network delays, communication failures, partial failures, and distributed deadlock detection and resolution .
- Distributed concurrency control protocols can be classified into two categories: centralized and decentralized .
- Centralized concurrency control protocols rely on a single coordinator node to manage the concurrency control of all transactions in the system, which may introduce a single point of failure and a performance bottleneck .
- Decentralized concurrency control protocols distribute the responsibility of concurrency control among multiple nodes, which may increase the scalability and fault-tolerance of the system, but also increase the complexity and overhead of coordination .
- Examples of centralized concurrency control protocols are two-phase locking (2PL), two-phase commit (2PC), and three-phase commit (3PC) .
- Examples of decentralized concurrency control protocols are distributed 2PL, distributed 2PC, distributed optimistic concurrency control, and distributed timestamp ordering  .



### Distributed Deadlocks

- A distributed deadlock is a situation where a set of processes in a distributed system are waiting for each other to release resources or messages, and none of them can proceed .
- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems .
- Distributed deadlocks are harder to detect, avoid, and prevent than deadlocks in centralized systems, because there is no single authority that can oversee resource allocation and monitor the state of the system.
- There are three main approaches to handle distributed deadlocks :
  - Prevention: This approach tries to ensure that deadlocks never occur by imposing some constraints on resource allocation, such as ordering, preemption, or timeouts. However, this approach may reduce system performance and utilization.
  - Avoidance: This approach tries to avoid deadlocks by dynamically analyzing the resource requests and granting them only if they do not lead to a potential deadlock. This approach requires the knowledge of the current and future resource requirements of each process, which may not be feasible or accurate in a distributed system.
  - Detection and recovery: This approach tries to detect deadlocks after they occur and then recover from them by aborting or restarting some processes, or by releasing some resources. This approach requires the cooperation of all the nodes in the system to collect and exchange information about the resource dependencies and the wait-for relations among processes.
- There are two main techniques for deadlock detection in distributed systems :
  - Global wait-for graph: This technique involves constructing a global wait-for graph (WFG) from local wait-for graphs at a deadlock detector or a coordinator node. The WFG is a directed graph that represents the resource dependencies and the wait-for relations among processes in the system. A cycle in the WFG indicates a deadlock. The WFG can be constructed by periodically sending messages from each node to the deadlock detector, or by using a distributed snapshot algorithm. The main challenges of this technique are the communication overhead, the synchronization of the WFG, and the possibility of false or phantom deadlocks due to stale information.
  - Edge chasing: This technique involves sending probe messages along the wait-for edges in the local wait-for graphs to detect cycles. A probe message contains the identifier of the initiator node and the sequence of nodes visited so far. When a node receives a probe message, it checks if it is the initiator or if it has already seen the message. If yes, it means a cycle has been detected and a deadlock exists. If no, it appends its identifier to the message and forwards it to the next node in the wait-for edge. The main challenges of this technique are the message complexity, the termination detection, and the possibility of false or phantom deadlocks due to concurrent resource requests or releases.



### Transaction recovery for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

- A distributed transaction is a transaction that involves multiple sites or nodes in a distributed system, such as a network of databases or microservices.
- A distributed transaction must satisfy the ACID properties: atomicity, consistency, isolation, and durability.
- Atomicity means that either all the subtransactions of a distributed transaction commit or none of them do.
- Consistency means that the distributed transaction preserves the integrity constraints of the data.
- Isolation means that the distributed transaction does not interfere with other concurrent transactions.
- Durability means that the effects of a committed distributed transaction are permanent and survive failures.
- A failure in a distributed system can affect one or more sites or nodes, and can cause partial or complete loss of data, communication, or processing capability.
- A failure can also leave some distributed transactions in an uncertain or in-doubt state, where it is not clear whether they have committed or aborted.
- Transaction recovery is the process of restoring the consistency and durability of the data after a failure, by either committing or aborting the affected distributed transactions.
- Transaction recovery in a distributed system is more complex than in a centralized system, because it involves coordination and communication among multiple sites or nodes, and it must handle different types of failures and their effects.
- There are two main approaches for transaction recovery in a distributed system: logging and shadow versions.
- Logging is a technique that records the changes made by a distributed transaction in a log file, which can be used to undo or redo the changes in case of a failure.
- Shadow versions is a technique that creates a copy of the data before a distributed transaction modifies it, and switches to the new version only after the transaction commits.
- Both logging and shadow versions require a distributed commit protocol, such as the two-phase commit protocol, to ensure atomicity of the distributed transaction.
- The two-phase commit protocol consists of two phases: the prepare phase and the commit phase.
- In the prepare phase, the coordinator of the distributed transaction asks all the participants to vote on whether they are ready to commit or not, and collects their votes.
- In the commit phase, the coordinator decides whether to commit or abort the distributed transaction based on the votes, and informs all the participants of the decision.
- The two-phase commit protocol can handle some types of failures, such as site failures or communication failures, by using timeouts and recovery managers.
- However, the two-phase commit protocol can also block or deadlock if the coordinator or some participants fail permanently or indefinitely, and no one knows the outcome of the distributed transaction.
- To avoid blocking or deadlock, some variations of the two-phase commit protocol have been proposed, such as the three-phase commit protocol, the presumed abort protocol, and the presumed commit protocol.
- The three-phase commit protocol adds a pre-commit phase between the prepare phase and the commit phase, where the coordinator and the participants agree on the decision before committing or aborting.
- The presumed abort protocol optimizes the two-phase commit protocol by assuming that a distributed transaction is aborted unless it is explicitly committed, and thus reducing the amount of logging and communication needed.
- The presumed commit protocol optimizes the two-phase commit protocol by assuming that a distributed transaction is committed unless it is explicitly aborted, and thus reducing the amount of logging and communication needed.



## Unit 10 - Replication

- Replication is the process of creating and maintaining multiple copies of the same data on different database servers.
- Replication provides benefits such as high availability, fault tolerance, load balancing, and scalability.
- Replication can be classified into different types based on the direction, timing, and location of data transfer.
- The main types of replication are:
  - Snapshot replication: A snapshot of the data is taken at a point in time and copied to the subscribers. The data is not synchronized until the next snapshot is taken.
  - Transactional replication: Changes made to the data at the publisher are captured and sent to the subscribers as they occur. The data is synchronized in near real time.
  - Merge replication: Changes made to the data at the publisher and the subscribers are tracked and merged periodically. The data is synchronized based on a predefined schedule or on demand.
  - Peer-to-peer replication: Changes made to the data at any node in a peer-to-peer topology are propagated to all other nodes. The data is synchronized in near real time and all nodes are equal.
- Replication involves the following components:
  - Publisher: The database server that publishes the data to be replicated.
  - Distributor: The database server that stores the replication metadata and distributes the data to the subscribers.
  - Subscriber: The database server that receives the data from the publisher or the distributor.
  - Publication: The set of data that is published by the publisher.
  - Subscription: The request for the data that is made by the subscriber.
  - Article: The smallest unit of data that can be replicated, such as a table, a view, or a stored procedure.
  - Agent: The software component that performs the replication tasks, such as copying, distributing, merging, or monitoring the data.



### System model and group communication for replication in distributed systems

- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by passing messages .
- Replication is a technique to improve the availability, performance, and fault tolerance of a distributed system by creating and maintaining multiple copies of data or services .
- A system model is a set of assumptions and properties that characterize the behavior and limitations of a distributed system, such as the communication model, the failure model, the timing model, and the security model .
- Group communication is a form of communication between multiple processes in a distributed system that share some common interests or goals, such as data replication, fault tolerance, or load balancing  .
- Group communication can be classified into two types: broadcast communication and multicast communication .
  - Broadcast communication is when a source process sends a message to all the processes in the system, regardless of their group membership or interest .
  - Multicast communication is when a source process sends a message to a subset of processes in the system that belong to a specific group or have a specific interest  .
- Group communication can also be classified into two categories: reliable and unreliable .
  - Reliable group communication is when a message sent by a source process is guaranteed to be delivered to all the intended recipients, even in the presence of failures or network partitions .
  - Unreliable group communication is when a message sent by a source process may be lost, duplicated, or delivered out of order, depending on the network conditions and the system model .
- Group communication can be implemented using various protocols and algorithms, such as IP multicast, gossip protocols, reliable multicast protocols, atomic broadcast protocols, and consensus protocols   .
- Group communication can be used for replication in distributed systems in several ways, such as  :
  - Replicating data or services across multiple processes or nodes to increase availability, performance, and fault tolerance.
  - Maintaining consistency and coherence among the replicas by using group communication protocols to order and synchronize the updates or requests.
  - Detecting and recovering from failures or network partitions by using group communication protocols to monitor and coordinate the status and actions of the replicas.
  - Balancing the load and optimizing the resource utilization by using group communication protocols to distribute the work or requests among the replicas.



# Fault-Tolerant Services for the Notes of the Unit 10 - Replication in the Subject of Distributed System

- Fault-tolerant services are services that can continue to function correctly even in the presence of failures, such as server crashes, network partitions, or malicious attacks.
- Replication is a technique for implementing fault-tolerant services by creating and maintaining multiple copies of the same service (or state machine) on different servers (or replicas) in a distributed system.
- Replication can improve the availability, performance, and reliability of the service, but also introduces challenges such as consistency, coordination, and recovery.
- There are two main classes of replication techniques: primary-backup replication and active replication.
  - Primary-backup replication: One replica is designated as the primary, and the others are backups. The primary receives all the requests from the clients, executes them, and sends the results and updates to the backups. The backups apply the updates to their local copies and acknowledge the primary. The primary sends the results back to the clients. If the primary fails, one of the backups takes over as the new primary.
  - Active replication: All replicas receive the same requests from the clients, execute them independently, and send the results back to the clients. The clients use a majority voting scheme to determine the correct result. If a replica fails, it does not affect the service as long as a majority of replicas are correct.
- Replication can tolerate different types of faults, such as crash faults or Byzantine faults.
  - Crash faults: A replica stops functioning or responds slowly. This can be detected by timeouts or heartbeats. Crash faults can be tolerated by using a minimum of n(f+1) replicas to tolerate f crash faults in primary-backup replication, or n(2f+1) replicas to tolerate f crash faults in active replication.
  - Byzantine faults: A replica behaves arbitrarily or maliciously, such as sending incorrect or conflicting messages. This can be detected by cryptographic signatures or message authentication codes. Byzantine faults can be tolerated by using a minimum of n(3f+1) replicas to tolerate f Byzantine faults in primary-backup replication, or n(3f+1) replicas to tolerate f Byzantine faults in active replication.
- Replication can also be classified based on the consistency model that the service provides to the clients, such as linearizability, sequential consistency, causal consistency, or eventual consistency.
  - Linearizability: The service appears as if there is a single copy of the state machine, and each operation appears to take effect atomically at some point between its invocation and response. This is the strongest consistency model and the most intuitive for the clients, but also the most expensive to implement. Linearizability requires that all replicas agree on the total order of all operations.
  - Sequential consistency: The service appears as if there is a single copy of the state machine, and each operation appears to take effect in the order specified by the client. This is a weaker consistency model than linearizability, but still preserves the client's view of the service. Sequential consistency does not require that all replicas agree on the same order of operations, as long as they respect the order issued by each client.
  - Causal consistency: The service guarantees that operations that are causally related are seen by all replicas in the same order, but operations that are concurrent (not causally related) can be seen in different orders by different replicas. This is a weaker consistency model than sequential consistency, but still preserves the causal dependencies among operations. Causal consistency can be implemented by using vector clocks or dependency graphs to track the causal relations among operations.
  - Eventual consistency: The service guarantees that if no new updates are made to the service, eventually all replicas will converge to the same state. This is the weakest consistency model, but also the easiest to implement. Eventual consistency does not impose any ordering constraints on the operations, and allows replicas to diverge temporarily. Eventual consistency can be implemented by using gossip protocols or anti-entropy mechanisms to propagate updates among replicas.



### Highly Available Services for the Notes of the Unit 10 - Replication in the Subject of Distributed System

- Replication is the process of creating and maintaining multiple copies of data or services across different nodes or locations in a distributed system.
- Replication can improve the availability, reliability, performance, and scalability of distributed systems by reducing the impact of failures, network latency, and load imbalance.
- Replication can also enable fault tolerance, disaster recovery, and data consistency in distributed systems.
- Replication can be classified into different types based on the following criteria:
  - The degree of replication: full replication (all nodes have a copy of the data or service) or partial replication (only some nodes have a copy of the data or service).
  - The timing of replication: eager replication (updates are propagated to all replicas as soon as they occur) or lazy replication (updates are propagated to some or all replicas after a delay or on demand).
  - The consistency of replication: strong consistency (all replicas have the same view of the data or service at all times) or weak consistency (replicas may have different views of the data or service at some times).
- Replication can be implemented at different levels of abstraction in distributed systems, such as:
  - Data replication: replicating data items or files across storage nodes or databases.
  - Service replication: replicating application-level processes or components across compute nodes or servers.
  - System replication: replicating entire systems or virtual machines across physical machines or clusters.
- Replication can be coordinated by different protocols or algorithms, such as:
  - Primary-backup protocol: one replica is designated as the primary and the others are backups. The primary receives and executes all requests and sends updates to the backups. The backups take over the primary role in case of failure.
  - Quorum protocol: each replica has a vote and a quorum is a subset of replicas whose votes are needed to perform an operation. A read quorum is needed to read data or service state and a write quorum is needed to update data or service state.
  - State machine protocol: each replica is modeled as a deterministic state machine that executes the same sequence of commands. A leader replica is elected to order and broadcast commands to the other replicas. The leader can be replaced in case of failure.
  - Gossip protocol: each replica periodically exchanges information with a random subset of other replicas. The information can be updates, acknowledgments, or summaries. The protocol converges to a consistent state over time.



### Transactions with replicated data

- Transactions are a sequence of operations that are executed atomically, consistently, isolatedly, and durably (ACID properties) on a database system.
- Replication is the process of copying and maintaining data in multiple locations to improve availability, performance, and fault tolerance of a distributed system.
- Transactions with replicated data involve executing operations on multiple copies of the same data item, while ensuring that the copies remain consistent and synchronized with each other.
- Some of the challenges and techniques for transactions with replicated data are:

  - **Concurrency control**: How to coordinate concurrent transactions on replicated data without violating serializability and consistency?
    - One approach is to use a primary copy scheme, where one copy of each data item is designated as the primary copy, and all transactions must access and update the primary copy first, before propagating the changes to the other copies. This ensures a serial order of transactions on each data item, but introduces a single point of failure and a communication overhead.
    - Another approach is to use a majority consensus scheme, where each transaction must obtain a lock on a majority of the copies of each data item it accesses, and commit only if a majority of the copies agree. This ensures a quorum of transactions on each data item, but requires more locking and voting messages.
  - **Recovery**: How to recover from failures and ensure durability of transactions on replicated data?
    - One approach is to use a two-phase commit protocol, where each transaction coordinator sends a prepare message to all the participants (replica managers) involved in the transaction, and waits for their votes. If all the participants vote yes, the coordinator sends a commit message to all of them, and waits for their acknowledgments. If any participant votes no, or the coordinator does not receive a vote or an acknowledgment within a timeout, the coordinator sends an abort message to all the participants. This ensures atomicity and durability of transactions, but introduces a blocking problem if the coordinator fails.
    - Another approach is to use a three-phase commit protocol, where each transaction coordinator sends a prepare message to all the participants, and waits for their votes. If all the participants vote yes, the coordinator sends a pre-commit message to all of them, and waits for their acknowledgments. If any participant votes no, or the coordinator does not receive a vote or an acknowledgment within a timeout, the coordinator sends an abort message to all the participants. If all the participants acknowledge the pre-commit message, the coordinator sends a commit message to all of them, and waits for their acknowledgments. If the coordinator does not receive an acknowledgment within a timeout, it resends the commit message. This ensures atomicity and durability of transactions, and avoids the blocking problem, but requires more messages and phases.

