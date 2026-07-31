

## Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- The main characteristics of distributed systems are:
  - Concurrency: Multiple components can execute simultaneously and interact with each other.
  - No global clock: There is no shared physical clock among the components, so synchronization and coordination are challenging.
  - Independent failures: Each component can fail independently, without affecting the rest of the system, unless there is a dependency.
  - Heterogeneity: The components can have different hardware, software, network, data, and protocols.
  - Scalability: The system can grow in size and complexity without losing its functionality and performance.
  - Transparency: The system hides its internal details from the users, such as the location, migration, replication, and failure of components.
- The main advantages of distributed systems are:
  - Resource sharing: The system can access and utilize the resources of multiple components, such as files, printers, sensors, etc.
  - Fault tolerance: The system can tolerate and recover from the failure of some components, by using replication, redundancy, or backup mechanisms.
  - Performance: The system can achieve higher throughput and lower latency by distributing the workload among multiple components and using parallelism.
  - Availability: The system can provide continuous service to the users, by using load balancing, caching, or replication techniques.
  - Modularity: The system can be composed of smaller and simpler components, which can be developed, tested, and maintained independently.
- The main challenges of distributed systems are:
  - Coordination: The system needs to coordinate the actions and states of multiple components, by using algorithms, protocols, or middleware.
  - Consistency: The system needs to ensure that the components have a consistent view of the data and the system state, by using synchronization, replication, or consensus mechanisms.
  - Security: The system needs to protect the data and the communication from unauthorized access, modification, or disclosure, by using encryption, authentication, or authorization techniques.
  - Reliability: The system needs to ensure that the components perform correctly and deliver the expected results, by using verification, testing, or debugging techniques.
  - Complexity: The system needs to cope with the complexity and uncertainty of the environment, such as network failures, message delays, or malicious attacks, by using fault tolerance, adaptation, or self-organization techniques.



### Introduction for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- A distributed system has the following characteristics:
  - Concurrency: The components of a distributed system can execute concurrently, without interfering with each other.
  - No global clock: There is no global notion of time in a distributed system. Each component has its own local clock, which may not be synchronized with others.
  - Independent failures: The components of a distributed system can fail independently, without affecting the whole system. The system should be able to tolerate and recover from failures.
  - Heterogeneity: The components of a distributed system can have different hardware, software, network, and data formats. The system should be able to cope with the diversity and complexity of the components.
- A distributed system has the following advantages:
  - Scalability: A distributed system can grow in size and performance by adding more components, without affecting the existing ones.
  - Availability: A distributed system can provide continuous service, even in the presence of failures, by replicating and distributing the components across different locations.
  - Fault tolerance: A distributed system can handle partial failures, by detecting and masking them, or by providing alternative solutions.
  - Transparency: A distributed system can hide the details of the distribution from the users, by providing a uniform and consistent view of the system.
  - Resource sharing: A distributed system can enable the sharing of resources, such as data, files, devices, and services, among the components and the users of the system.



### Examples of Distributed Systems

A distributed system is a collection of independent computers that communicate and coordinate their actions by passing messages. The computers in a distributed system may be physically close or geographically dispersed, and they may be connected by a network or a bus. Distributed systems can provide higher performance, reliability, scalability, and availability than centralized systems.

Some examples of distributed systems are:

- **Telecommunication networks**: Telephone networks are an early example of a peer-to-peer network, where each node can initiate or receive calls. Cellular and telephone networks are forms and examples of distributed networks. They use protocols such as TCP/IP, HTTP, and SMTP to exchange messages and data.  
- **Real-time systems**: Many industries use real-time systems distributed in various areas, locally and globally. For example, air traffic control systems, power grid systems, industrial control systems, and online gaming systems are all examples of real-time distributed systems. They require fast and accurate communication and synchronization among the nodes to ensure safety and quality of service.  
- **Distributed database systems**: A distributed database has locations across multiple servers, physical locations, or both. The data is replicated or partitioned among the nodes, and the nodes communicate and coordinate to maintain consistency and availability. Examples of distributed database systems are Google's Bigtable, Amazon's Dynamo, and MongoDB.  
- **Distributed computing platforms**: A distributed computing platform is a system that allows multiple computers to work together on a common task or problem. The computers may share resources, such as memory, disk space, or processing power, or they may have different roles and responsibilities. Examples of distributed computing platforms are MapReduce, Spark, Hadoop, and BOINC.



### Resource sharing for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Resource sharing is one of the main goals and benefits of distributed systems.
- Resource sharing means that the users and applications can access and use the resources (such as data, files, devices, services, etc.) that are available in the distributed system, regardless of their physical location, ownership, or access policy.
- Resource sharing can improve the performance, reliability, scalability, and availability of the distributed system, as well as reduce the cost and complexity of managing the resources.
- Resource sharing can be achieved by different methods, such as:
  - File sharing: the users and applications can access and manipulate the files that are stored on remote file servers, using a common file system interface and protocol (such as NFS, CIFS, etc.).
  - Data sharing: the users and applications can access and query the data that are stored on distributed databases, using a common data model and language (such as SQL, NoSQL, etc.).
  - Device sharing: the users and applications can access and use the devices (such as printers, scanners, cameras, etc.) that are connected to the distributed system, using a common device driver and protocol (such as USB, Bluetooth, etc.).
  - Service sharing: the users and applications can access and invoke the services (such as web services, cloud services, etc.) that are provided by the distributed system, using a common service interface and protocol (such as SOAP, REST, etc.).
- Resource sharing can also be classified into different types, such as:
  - Sharing by communication: the users and applications can exchange messages and data with each other, using a common communication protocol and middleware (such as TCP/IP, UDP, RPC, RMI, etc.).
  - Sharing by cooperation: the users and applications can coordinate and collaborate with each other, using a common coordination protocol and middleware (such as distributed transactions, consensus, etc.).
  - Sharing by competition: the users and applications can compete for the resources that are limited or scarce in the distributed system, using a common allocation protocol and middleware (such as distributed scheduling, load balancing, etc.).
- Resource sharing can also involve different challenges and issues, such as:
  - Heterogeneity: the resources in the distributed system may have different hardware, software, data, and network characteristics, which require a common abstraction and interoperability layer to enable resource sharing.
  - Transparency: the users and applications should be unaware of the details and complexities of the distributed system, such as the location, replication, migration, and failure of the resources, which require a common hiding and masking layer to enable resource sharing.
  - Security: the resources in the distributed system may be subject to unauthorized access, modification, or deletion, which require a common protection and enforcement layer to enable resource sharing.
  - Scalability: the resources in the distributed system may grow or shrink in number and size, which require a common adaptation and optimization layer to enable resource sharing.



### The Web Challenges for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- The web is an example of a distributed system that allows resource sharing and communication among different devices across the internet.
- However, the web also poses several challenges for the design and implementation of distributed systems, such as    :
  - Scalability: The ability to handle increasing load and demand without degrading the performance or functionality of the system. This requires efficient algorithms, protocols, and architectures that can cope with large numbers of users, requests, and data.
  - Heterogeneity: The diversity of devices, platforms, languages, and formats that are involved in the web. This requires interoperability, standardization, and adaptation mechanisms that can ensure compatibility and usability across different systems.
  - Security: The protection of data and resources from unauthorized access, modification, or destruction. This requires authentication, authorization, encryption, and auditing techniques that can prevent or detect attacks and ensure privacy and availability.
  - Fault tolerance: The ability to cope with failures and errors that may occur in the web. This requires redundancy, replication, recovery, and consensus techniques that can ensure reliability and consistency of the system.
  - Transparency: The hiding of the complexity and diversity of the web from the users and applications. This requires abstraction, location independence, concurrency control, and caching techniques that can provide a simple and uniform view of the system.



### Architectural models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Architectural models are types of system models that deal with the organization of components across the network and their interrelationship.
- Architectural models describe the placement of parts in a distributed system and the relationship between them.
- Architectural models can be classified into different styles, such as:
  - Client-server architecture: A style where one or more servers provide services to multiple clients that request them. The servers and clients can be distributed across the network. This style forms the base for multi-tier architectures.
  - Broker architecture: A style where a broker component acts as an intermediary between clients and servers, hiding the details of communication and location from them. The broker can also provide additional services such as security, load balancing, and fault tolerance. An example of this style is CORBA.
  - Service-oriented architecture: A style where services are loosely coupled and can be discovered, composed, and invoked dynamically. Services are self-contained, platform-independent, and communicate using standard protocols such as SOAP and REST. An example of this style is web services.
  - Peer-to-peer architecture: A style where each node in the network can act as both a client and a server, and can communicate directly with other nodes without a central authority. This style can provide scalability, resilience, and resource sharing. An example of this style is BitTorrent.
  - Distributed object architecture: A style where objects are distributed across the network and can be accessed and manipulated by remote method invocation. Objects can be transparently replicated, migrated, and cached for performance and availability. An example of this style is Java RMI.
  - Distributed component architecture: A style where components are distributed across the network and can be assembled into applications using a component model. Components can be reusable, configurable, and interoperable. An example of this style is EJB.
- Architectural models can also be influenced by other factors, such as:
  - Scalability: The ability of a system to handle increasing workload or number of users without degrading performance or quality of service.
  - Availability: The degree to which a system is operational and accessible to users.
  - Reliability: The probability that a system will perform its intended function without failure.
  - Security: The protection of a system from unauthorized access, modification, or disclosure of information.
  - Transparency: The degree to which a system hides the details of its distribution from users and applications.
  - Heterogeneity: The diversity of hardware, software, and network platforms in a distributed system.
- Architectural models can be evaluated and compared based on various criteria, such as:
  - Complexity: The difficulty of designing, implementing, testing, and maintaining a system.
  - Modularity: The degree to which a system is composed of independent and cohesive units.
  - Reusability: The extent to which a system or its parts can be used in different contexts or applications.
  - Configurability: The ease of adapting a system to different requirements or environments.
  - Interoperability: The ability of a system to communicate and cooperate with other systems.
  - Performance: The measure of how well a system meets its functional and non-functional requirements.
  - Cost: The amount of resources (such as time, money, and effort) required to develop, deploy, and operate a system.



### Fundamental Models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Fundamental models are descriptions of properties that are present in all distributed architectures  .
- They help us understand the characteristics, challenges and trade-offs of designing and implementing distributed systems.
- There are three main types of fundamental models: interaction models, failure models and security models  .

#### Interaction Models
- Interaction models deal with the issues of communication and coordination among processes in a distributed system  .
- They include aspects such as performance, timing, ordering, synchronization and consistency of events and messages  .
- Some examples of interaction models are:
  - Synchronous vs. asynchronous communication: whether the sender and receiver of a message have to wait for each other or not  .
  - Remote procedure call (RPC): a method of invoking a procedure or function on a remote machine as if it were local  .
  - Publish-subscribe: a pattern of communication where publishers send messages to a broker, and subscribers receive messages that match their interests  .
  - Message queue: a data structure that stores messages from senders until they are consumed by receivers  .

#### Failure Models
- Failure models specify the types of faults that can occur in a distributed system and how they affect the processes and communication channels  .
- They help us design fault-tolerant and resilient systems that can cope with failures and recover from them  .
- Some examples of failure models are:
  - Crash failure: a process stops executing and does not resume  .
  - Omission failure: a process fails to send or receive a message  .
  - Timing failure: a process or a message violates the timing assumptions of the system  .
  - Byzantine failure: a process behaves arbitrarily or maliciously, sending incorrect or conflicting messages  .

#### Security Models
- Security models define the goals and threats of a distributed system in terms of confidentiality, integrity and availability of data and services  .
- They help us design secure and trustworthy systems that can prevent, detect and respond to attacks  .
- Some examples of security models are:
  - Cryptography: the use of mathematical techniques to encrypt and decrypt data, as well as to authenticate and verify the identity and integrity of the parties involved  .
  - Access control: the mechanism of granting or denying permissions to access data or services based on the identity and role of the requester  .
  - Distributed firewalls: the use of filters and rules to block or allow network traffic based on the source, destination and content of the packets  .



### Theoretical Foundation for Distributed System

- A distributed system is a collection of processes that are spatially separated and do not share a common memory and communicate with one another by exchanging messages with arbitrary delays .
- Theoretical foundation for distributed system aims to understand the inherent limitations, capabilities and trade-offs of a distributed system and to develop abstract models, algorithms and techniques for solving problems in a distributed environment .
- Some of the topics covered by the theoretical foundation for distributed system are:
  - Limitation of distributed system: such as impossibility of consensus, failure detection, global state, mutual exclusion, etc. in the presence of failures, asynchrony or uncertainty .
  - Absence of global clock: the lack of a common notion of time or ordering of events in a distributed system and the need for synchronization mechanisms  .
  - Shared memory: the abstraction of a global memory that can be accessed by all processes in a distributed system and the challenges of consistency, coherence, replication, etc. in implementing it .
  - Logical clocks: the methods of assigning logical timestamps to events in a distributed system and the properties of causality, concurrency and partial ordering they capture   .
  - Lamport's and vector logical clocks: the two types of logical clocks that are widely used in distributed systems and their advantages and disadvantages   .
  - Concepts in message passing system: the communication model that relies on sending and receiving messages between processes in a distributed system and the issues of reliability, ordering, buffering, routing, etc. in it .



### Limitation of Distributed System

A distributed system is a system that consists of multiple independent components that communicate with each other over a network. Distributed systems have many advantages, such as scalability, fault tolerance, availability, and performance. However, they also face some limitations that make them challenging to design and implement. Some of the main limitations of distributed systems are:

- **Absence of a global state**: In a distributed system, there is no single point of control or coordination for the entire system. Each component has its own local state and view of the system, which may differ from other components. This makes it difficult to reason about the behavior and correctness of the system as a whole, and to ensure consistency and coherence among the components. For example, in a distributed database, different replicas of the same data may have different values due to concurrent updates or network delays. To resolve this issue, distributed systems need to use synchronization and consensus protocols, which can be complex and costly.
- **Absence of a global clock**: In a distributed system, there is no common notion of time or ordering of events among the components. Each component has its own local clock, which may drift or be inaccurate. This makes it hard to measure and compare the timestamps of events that occur in different components, and to synchronize the actions and operations of the components. For example, in a distributed system that processes online transactions, it may be unclear which transaction happened first or which one should be committed or aborted. To address this problem, distributed systems need to use logical clocks or vector clocks, which can be complicated and overhead.
- **Network issues**: In a distributed system, the communication between the components depends on the network, which can be unreliable, unpredictable, or insecure. The network may experience failures, delays, congestion, or attacks, which can affect the availability and performance of the system. For example, in a distributed system that provides a web service, the network may cause the service to be slow, unavailable, or corrupted. To cope with this challenge, distributed systems need to use fault tolerance and security mechanisms, which can be expensive and difficult.



### Absence of Global Clock

- A global clock is a system-wide clock that is equally accessible to all processes in a distributed system and provides a common notion of time.
- A global clock is useful for ordering events, synchronizing processes, and obtaining consistent states of the system.
- However, a global clock is hard to realize in distributed systems due to two inherent limitations: lack of shared memory and unpredictable message delays.
- Lack of shared memory means that processes in a distributed system do not have access to a common storage that can store and update the global clock value.
- Unpredictable message delays mean that processes in a distributed system cannot rely on the communication channel to exchange accurate and timely information about the global clock value.
- As a result, processes in a distributed system may have different and inconsistent notions of time, and it may not be possible to determine the order of events or the state of the system in a meaningful way.



### Shared Memory

- Shared memory is a programming model that allows multiple processes to access and modify the same data in a shared address space.
- Shared memory can be implemented in two ways: physically shared memory and distributed shared memory.
- Physically shared memory is when multiple processors or cores share the same physical memory, such as in a multiprocessor system or a multicore system.
- Distributed shared memory (DSM) is when multiple nodes or computers in a distributed system share a virtual address space, but do not have physical access to the same memory, such as in a cluster or a grid.
- DSM systems can provide the illusion of a shared memory model on a distributed system, which can simplify the programming and increase the performance of parallel and distributed applications.
- DSM systems can be implemented in hardware or software, or a combination of both.
- Hardware DSM systems use special hardware components, such as cache coherence circuits and network interface controllers, to maintain the consistency and coherence of the shared data across the nodes.
- Software DSM systems use software mechanisms, such as page-based, object-based, or tuple-based approaches, to manage the distribution and replication of the shared data across the nodes.
- DSM systems face several challenges, such as scalability, fault tolerance, consistency, coherence, synchronization, and communication overhead. Different DSM systems use different techniques and policies to address these challenges.



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
  - Consistency: If event A causally precedes event B, then the logical clock of A is less than the logical clock of B .
  - Accuracy: The logical clock of an event reflects the real time of the event as closely as possible.
  - Efficiency: The logical clock algorithm should have low overhead in terms of time and space complexity.



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
- Therefore, Lamport's logical clocks can only partially order events, and they cannot distinguish between concurrent events, which are events that are not causally related.
- Lamport's logical clocks are simple and easy to implement, but they have some limitations, such as:
  - They do not reflect the real time of events, only their logical order.
  - They do not provide a total order of events, only a partial order.
  - They do not guarantee that timestamps are unique, only that they are monotonically increasing.
  - They do not account for the communication delays or clock drifts in the system.



### Concepts in Message Passing Systems

- Message passing is a technique for invoking behavior (i.e., running a program) on a computer.
- In message-passing systems, processors communicate with one another by sending and receiving messages over a communication channel.
- The pattern of the connection provided by the channel is described by some topology systems.
- The collection of the channels are called a network.
- A message-passing system gives a collection of message-based IPC protocols while sheltering programmers from the complexities of sophisticated network protocols and many heterogeneous platforms.
- A message-passing mechanism can be used in a distributed system for the following two forms of inter-process communication:
  - Local communication, where the communicating processes are located on the same node.
  - Distant communication, in which the communication activities are distributed among multiple nodes.
- The formal model for distributed message passing has two timing models:
  - Synchronous, where there are known bounds on the message transmission time, the processing time, and the clock drift rate.
  - Asynchronous, where there are no such bounds and the processes may operate at arbitrary speeds.
- Message passing can be classified into two types:
  - Blocking, where the sender and the receiver are blocked until the message is delivered.
  - Non-blocking, where the sender and the receiver can proceed without waiting for the message delivery.
- Message passing can also be classified into two modes:
  - Point-to-point, where the message is sent from one specific process to another specific process.
  - Broadcast, where the message is sent from one process to all other processes in the system.



### Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- Causal order is a way of ordering events in a distributed system based on their causal relationships, rather than their physical timestamps or locations.
- Causal order ensures that if an event e1 causally precedes another event e2, then e1 is observed before e2 by all processes in the system.
- Causal order is important for maintaining consistency and correctness in distributed systems, especially for applications that rely on causal dependencies, such as collaborative editing, social media, or online gaming.
- Causal order can be defined formally using the concept of Lamport's happened-before relation, denoted by ->, which is a partial order on the set of events in a distributed system.
- The happened-before relation -> satisfies the following properties:
  - If e1 and e2 are events in the same process, and e1 occurs before e2, then e1 -> e2.
  - If e1 is the sending of a message by one process and e2 is the receipt of the same message by another process, then e1 -> e2.
  - If e1 -> e2 and e2 -> e3, then e1 -> e3 (transitivity).
- Two events e1 and e2 are said to be concurrent, denoted by e1 || e2, if neither e1 -> e2 nor e2 -> e1 holds. Concurrent events have no causal relationship and can be observed in any order by different processes.
- Causal order can be implemented in distributed systems using various algorithms, such as vector clocks, causal broadcast, or causal memory.
- Vector clocks are a mechanism for assigning logical timestamps to events in a distributed system, such that the timestamps reflect the causal order of the events.
- A vector clock is an array of n integers, where n is the number of processes in the system. Each process maintains its own vector clock and updates it as follows:
  - Initially, all entries are set to zero.
  - Whenever a process performs an internal event, it increments its own entry in the vector clock by one.
  - Whenever a process sends a message, it attaches its current vector clock to the message and increments its own entry by one.
  - Whenever a process receives a message, it updates its vector clock by taking the element-wise maximum of its own vector clock and the vector clock received with the message.
- The vector clocks of two events e1 and e2 can be compared to determine their causal order as follows:
  - If e1 -> e2, then the vector clock of e1 is less than the vector clock of e2, denoted by VC(e1) < VC(e2), meaning that for every i, VC(e1)[i] <= VC(e2)[i], and there exists some j such that VC(e1)[j] < VC(e2)[j].
  - If e1 || e2, then the vector clocks of e1 and e2 are incomparable, denoted by VC(e1) || VC(e2), meaning that there exists some i and some j such that VC(e1)[i] < VC(e2)[i] and VC(e1)[j] > VC(e2)[j].
- Causal broadcast is a communication primitive that guarantees that messages are delivered to all processes in the system in causal order.
- Causal broadcast can be implemented using vector clocks as follows:
  - Whenever a process wants to broadcast a message, it sends the message along with its current vector clock to all other processes.
  - Whenever a process receives a message, it checks if the message is causally ready, meaning that the vector clock of the message is less than or equal to its own vector clock plus one at the sender's entry. If the message is causally ready, it delivers the message and updates its vector clock. Otherwise, it buffers the message until it becomes causally ready.
- Causal memory is a shared memory abstraction that guarantees that read and write operations are performed in causal order.
- Causal memory can be implemented using vector clocks as follows:
  - Each process maintains a local copy of the shared memory and a vector clock that reflects the causal order of its operations.
  - Whenever a process wants to read a value from the shared memory, it returns the value from its local copy.
  - Whenever a process wants to write a value to the shared memory, it updates its local copy and its vector clock, and sends the value and the vector clock to all other processes.
  - Whenever a process receives a value and a vector clock from another process, it



### Total Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent entities that communicate by message passing and coordinate their actions to achieve a common goal.
- Events are occurrences that happen at a specific point in time and space in a distributed system, such as sending or receiving a message, executing a statement, or accessing a shared resource.
- A partial order is a binary relation that satisfies three properties: reflexivity, antisymmetry, and transitivity. A partial order can be used to compare some but not all events in a distributed system, based on their causal relationship.
- A total order is a binary relation that satisfies four properties: reflexivity, antisymmetry, transitivity, and totality. A total order can be used to compare all events in a distributed system, regardless of their causal relationship.
- A total order can be established by using some arbitrary mechanism to break ties among events that are not causally related, such as the ID of the process, the timestamp of the event, or the lexicographic order of the message content.
- A total order can be useful for implementing distributed algorithms that require consistency, agreement, or coordination among the entities, such as mutual exclusion, atomic broadcast, consensus, or distributed transactions.



### Total Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems in the Subject of Distributed System

- A distributed system is a collection of independent processes that communicate by exchanging messages over a network.
- Events are occurrences that happen at a specific point in time and space in a distributed system, such as sending or receiving a message, or executing a local operation.
- The order of events is important for understanding the behavior and correctness of a distributed system, especially in the presence of concurrency and failures.
- A partial order is a binary relation that satisfies three properties: reflexivity, antisymmetry, and transitivity. A partial order can be represented by a directed acyclic graph (DAG), where nodes are events and edges are ordering relations.
- A causal order is a partial order that captures the notion of potential causality between events. An event e1 is causally related to another event e2, denoted by e1 -> e2, if one of the following conditions holds:
  - e1 and e2 are events in the same process, and e1 happened before e2.
  - e1 is the sending of a message, and e2 is the corresponding receiving of that message.
  - There exists some event e3 such that e1 -> e3 and e3 -> e2.
- A total order is a partial order that satisfies an additional property: comparability. This means that for any two events e1 and e2, either e1 -> e2, or e2 -> e1, or both (if e1 and e2 are the same event). A total order can be represented by a linear sequence of events, where each event is ordered before or after every other event.
- A total causal order is a total order that is consistent with the causal order. This means that if e1 -> e2 in the causal order, then e1 -> e2 in the total order as well. A total causal order establishes a unique linearization of all the events in the system, even those that are concurrent (not causally related).
- A total causal order is useful for ensuring consistency and agreement among the processes in a distributed system. For example, a total causal order can be used to implement atomic broadcast, a communication primitive that guarantees that all processes deliver the same set of messages in the same order.



### Techniques for Message Ordering for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Message ordering is the problem of ensuring that messages are processed in a consistent and predictable order in a distributed system .
- Message ordering is important because it affects the final outcome of the actions and the correctness of the algorithms in a distributed system .
- There are different types of message ordering techniques, depending on the desired level of consistency and synchronization among the processes in a distributed system  .
- Some of the common message ordering techniques are:

  - **Unordered**: Messages are delivered in any order, without any guarantee of consistency or synchronization. This is the simplest and fastest technique, but it may lead to incorrect or inconsistent results  .
  - **FIFO**: Messages are delivered in the same order as they are sent by each sender, but not necessarily in the same order as they are received by each receiver. This technique ensures that messages from the same sender are processed in a sequential order, but it does not guarantee any global order among messages from different senders  .
  - **Causal**: Messages are delivered in a way that respects the causal dependencies among them, i.e., if a message m1 causally precedes a message m2, then m1 is delivered before m2 at every receiver. This technique ensures that messages that are related by some logical or temporal relation are processed in a consistent order, but it does not guarantee any total order among all messages  .
  - **Total**: Messages are delivered in the same order at every receiver, i.e., there is a global order among all messages in the system. This technique ensures that messages are processed in a deterministic and uniform order, but it requires a high degree of coordination and synchronization among the processes  .
  - **Synchronous**: Messages are delivered in the same order and at the same time at every receiver, i.e., there is a global order and a global clock among all messages in the system. This technique ensures that messages are processed in a synchronous and atomic manner, but it requires a very high degree of coordination and synchronization among the processes, and it may not be feasible in some scenarios  .

- Each message ordering technique has its own advantages and disadvantages, and it may be suitable for different applications and requirements. For example, unordered message ordering may be sufficient for some simple or unreliable tasks, while total or synchronous message ordering may be necessary for some critical or complex tasks  .
- There are different protocols and algorithms that can implement each message ordering technique, such as vector clocks, logical clocks, Lamport timestamps, sequence numbers, etc. These protocols and algorithms may vary in their complexity, overhead, scalability, and performance  .



### Causal ordering of messages

- Causal ordering of messages is a partial ordering of messages in a distributed computing environment .
- It places a restriction on communication between processes by requiring that if the transmission of message mi to process pk necessarily preceded the transmission of message mj to the same process, then the delivery of these messages to that process must be ordered such that mi is delivered before mj.
- Causal ordering of messages is one of the four semantics of multicast communication, namely unordered, totally ordered, causal, and sync-ordered communication.
- Multicast communication methods vary according to the message’s reliability guarantee and ordering guarantee.
- Causal ordering of messages is useful for ensuring consistency and correctness in distributed systems that involve concurrent and interdependent events.
- Causal ordering of messages can be implemented using various algorithms, such as vector clocks, logical clocks, or piggybacking  .
- Causal ordering of messages can be violated due to transmission delays, network congestion, or clock synchronization errors .



### Global State for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent processes that communicate through message passing.
- The local state of a process is the values of its variables and the contents of its memory at a given point in time.
- The global state of a distributed system is the union of the local states of all the processes and the states of the communication channels.
- A global state is consistent if it reflects a possible execution of the system, i.e., no causal dependencies are violated.
- A global state is useful for detecting global properties of the system, such as deadlock, termination, or invariant violation.
- A global state can be recorded by taking a distributed snapshot, which is a collection of local snapshots taken by each process at some point during the execution.
- A distributed snapshot algorithm must ensure that the recorded global state is consistent and that the normal execution of the system is not disrupted.
- There are different distributed snapshot algorithms for different types of communication channels, such as FIFO, causal, or reliable.



### Termination Detection

- Termination detection is a fundamental problem in distributed systems, where a set of processes cooperate to perform a computation and need to know when the computation is finished.
- A process in a distributed system can be either in an active state or in an idle state at any given point of time  .
- An active process may become idle at any time, but an idle process may only become active again upon receiving a computational message.
- Termination occurs when all of the processes become idle and there are no in-transit computational messages.
- Termination detection is non-trivial because no process has complete knowledge of the global state, and global time does not exist.
- A termination detection algorithm must ensure the following properties:
  - Execution of the algorithm cannot indefinitely delay the underlying computation.
  - The algorithm must not require addition of new communication channels between processes.
- Huang's algorithm is an example of a termination detection algorithm that uses a control message called a token to collect information about the local states of the processes and the messages in transit  .
- The token is circulated among the processes in a logical ring, and each process updates the token with its own state and the number of messages it has sent and received  .
- When the token returns to the initiator process, it can determine if termination has occurred by checking if the token contains all idle states and zero messages in transit  .
- Huang's algorithm is efficient, as it requires only one token and a constant number of bits per process.



## Unit 2 - Distributed Mutual Exclusion

- Distributed mutual exclusion is a fundamental problem in distributed computing systems  .
- It ensures that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner  .
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion. Message passing is the sole means for implementing distributed mutual exclusion .
- There are three basic approaches for implementing distributed mutual exclusion:
  - Token-based algorithms: A unique token is circulated among the processes in the system. A process can enter the critical section only if it possesses the token.
  - Permission-based algorithms: A process requests permission from other processes in the system before entering the critical section. A process can enter the critical section only if it receives permission from all or a majority of the processes.
  - Quorum-based algorithms: A process requests permission from a subset of processes in the system before entering the critical section. A process can enter the critical section only if it receives permission from a quorum of processes.
- The performance of distributed mutual exclusion algorithms can be measured by the following criteria :
  - Message complexity: The number of messages exchanged per critical section entry.
  - Synchronization delay: The delay between the time a process requests to enter the critical section and the time it is granted permission.
  - System throughput: The rate at which processes can execute the critical section.
  - Fault tolerance: The ability of the algorithm to handle failures of processes or communication links.
- Some examples of distributed mutual exclusion algorithms are:
  - Ricart-Agrawala algorithm: A permission-based algorithm that uses a logical clock to order the requests and replies .
  - Suzuki-Kasami algorithm: A token-based algorithm that uses a request vector to keep track of the pending requests and a token that contains a privilege vector to indicate the processes that have executed the critical section .
  - Maekawa's algorithm: A quorum-based algorithm that uses a voting set of processes to grant permission to a requesting process .
  - Lamport's bakery algorithm: A permission-based algorithm that uses a numbering scheme to assign priority to the processes and a shared queue to order the requests .



### Classification of distributed mutual exclusion

Distributed mutual exclusion is a problem of ensuring that only one process in a distributed system can access a shared resource or data at a time. It is a fundamental requirement for achieving consistency, coordination and synchronization among the processes in a distributed system.

There are three basic approaches for implementing distributed mutual exclusion algorithms:

- **Token-based approach**: A unique token is shared among the sites or processes. A site is allowed to enter its critical section if it possesses the token. Mutual exclusion is ensured because the token is unique. Examples of token-based algorithms are Suzuki-Kasami's algorithm, Raymond's algorithm and Maekawa's algorithm.
- **Non-token-based approach**: There is no token in this approach. Instead, a site requests permission from other sites before entering its critical section. The other sites grant or deny the permission based on some rules or conditions. Examples of non-token-based algorithms are Lamport's algorithm, Ricart-Agrawala's algorithm and Singhal's algorithm.
- **Quorum-based approach**: A site needs to obtain permission from a subset of sites, called a quorum, before entering its critical section. A quorum is a set of sites that satisfies some properties, such as intersection, majority or availability. Examples of quorum-based algorithms are Naimi-Trehel's algorithm, Agrawal-El Abbadi's algorithm and Thomas's algorithm.

Each approach has its own advantages and disadvantages in terms of message complexity, synchronization delay, fault tolerance and scalability.



### Requirement of mutual exclusion theorem for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM

- Mutual exclusion is a concurrency control property which is introduced to prevent race conditions.
- Race conditions occur when multiple processes access a shared resource or data simultaneously and the outcome depends on the order of execution.
- Mutual exclusion ensures that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner  .
- Mutual exclusion in a distributed system states that only one process is allowed to execute the critical section (CS) at any given time  .
- A critical section is a piece of code that accesses a shared resource or data.
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion .
- Message passing is the sole means for implementing distributed mutual exclusion .
- There are three basic approaches for implementing distributed mutual exclusion:
  - Token-based algorithms: A process can enter the CS only if it possesses a unique token. The token is passed among the processes in a predefined order or by request.
  - Permission-based algorithms: A process can enter the CS only if it obtains permission from all or a subset of the processes in the system. The process sends request messages and waits for reply messages before entering the CS.
  - Quorum-based algorithms: A process can enter the CS only if it obtains permission from a majority or a quorum of the processes in the system. The process sends request messages and waits for reply messages from a quorum before entering the CS.
- The mutual exclusion theorem states that any algorithm for implementing distributed mutual exclusion must satisfy the following properties:
  - Safety: At most one process can execute the CS at any given time.
  - Liveness: Every request to enter the CS eventually succeeds.
  - Fairness: No process is indefinitely postponed from entering the CS.



### Token based and non token based algorithms for distributed mutual exclusion

- Distributed mutual exclusion (DME) is the problem of ensuring that only one process at a time can access a shared resource in a distributed system.
- There are two main approaches to solve DME: token based and non token based algorithms.
- Token based algorithms use a special message, called a token, that grants the permission to enter the critical section. Only the process that holds the token can access the shared resource. The token is passed among the processes in a predefined order or based on requests.
- Non token based algorithms use timestamps to order the requests for the critical section and to resolve conflicts between simultaneous requests. A process communicates with a set of other processes to determine who should execute the critical section next. The process that has the highest priority according to some criteria can enter the critical section.
- Some examples of token based algorithms are:
  - Suzuki-Kasami algorithm: a modification of Ricart-Agrawala algorithm, which uses REQUEST and REPLY messages to ensure mutual exclusion. In this algorithm, the token is a vector that records the number of requests made by each process. The token is sent to the process that has the highest request number in the vector .
  - Raymond's algorithm: a tree-based algorithm, where the processes are organized in a logical tree. The token is initially held by the root of the tree. A process that wants to enter the critical section sends a REQUEST message to its parent in the tree. The parent forwards the request to the root, if it does not have the token. The root sends the token to the requesting process along the path of the requests. A process that has the token can enter the critical section. When it leaves the critical section, it sends the token to one of its children that has requested it, or to its parent otherwise.
- Some examples of non token based algorithms are:
  - Lamport's algorithm: a logical clock based algorithm, where each process maintains a local clock that is incremented on each event. A process that wants to enter the critical section sends a REQUEST message with its clock value to all other processes. A process that receives a request replies with an ACK message and updates its clock. A process can enter the critical section when it has received ACKs from all other processes and its request has the smallest timestamp among all pending requests.
  - Maekawa's algorithm: a voting based algorithm, where each process belongs to a subset of processes, called a quorum, that can grant permission to enter the critical section. A process that wants to enter the critical section sends a REQUEST message to all processes in its quorum. A process that receives a request replies with a VOTE message if it has not voted for another process, or a FAILED message otherwise. A process can enter the critical section when it has received VOTES from all processes in its quorum. When it leaves the critical section, it sends a RELEASE message to all processes in its quorum to revoke its vote.



### Performance Metric for Distributed Mutual Exclusion Algorithms

- Distributed mutual exclusion algorithms are algorithms that ensure that only one process can access a shared resource or execute a critical section at a time in a distributed system.
- The performance of distributed mutual exclusion algorithms can be evaluated by the following four metrics :
  - **Message complexity**: It is the number of messages that are required per critical section execution by a process. It reflects the communication overhead and network congestion caused by the algorithm. A lower message complexity is desirable.
  - **Synchronization delay**: It is the time elapsed between the departure of a process from the critical section and the entry of the next process into the critical section. It reflects the degree of concurrency and fairness achieved by the algorithm. A lower synchronization delay is desirable.
  - **Response time**: It is the time interval between the request of a process to enter the critical section and the actual entry of the process into the critical section. It reflects the waiting time and the performance perceived by the process. A lower response time is desirable.
  - **Throughput**: It is the number of critical section executions per unit time in the system. It reflects the overall efficiency and utilization of the shared resource by the algorithm. A higher throughput is desirable.
- Different distributed mutual exclusion algorithms may have different trade-offs among these metrics, depending on the underlying assumptions, design choices, and network conditions. For example, a token-based algorithm may have a lower message complexity but a higher synchronization delay than a non-token-based algorithm. A quorum-based algorithm may have a lower response time but a higher message complexity than a centralized algorithm.



## Unit 3 - Distributed Deadlock Detection

- A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
- Deadlock detection is the process of identifying the existence of a deadlock in a system.
- Distributed deadlock detection is the process of detecting deadlocks in a distributed system, where processes and resources are located on different nodes connected by a network.
- Distributed deadlock detection can be classified into two categories: global and local.
  - Global deadlock detection involves collecting information from all nodes and applying a centralized algorithm to detect deadlocks.
  - Local deadlock detection involves applying a distributed algorithm that uses local information and message passing to detect deadlocks.
- Distributed deadlock detection can also be classified into two approaches: edge-chasing and probe-based.
  - Edge-chasing is a technique that uses control messages (called probes) to trace the dependency graph of processes and resources. A deadlock is detected when a probe returns to its originator or when a cycle is formed in the graph.
  - Probe-based is a technique that uses special messages (called probes) to initiate deadlock detection at some nodes. A probe contains information about the sender, the receiver, and the resources requested by the sender. A deadlock is detected when a probe reaches a node that is waiting for a resource held by the sender or when a probe returns to its originator.



### System Model for Distributed Deadlock Detection

- A distributed system consists of a collection of nodes that communicate and cooperate to achieve a common goal.
- A node can be a process, a processor, a computer, or a cluster of computers.
- A node can request, hold, and release resources that are shared among the nodes.
- A resource can be a physical device, a logical entity, or a message.
- A node can be in one of the following states: active, waiting, or blocked.
- An active node is executing its own instructions and does not need any resource.
- A waiting node is waiting for a resource that is currently held by another node.
- A blocked node is waiting for a resource that is not currently available in the system.
- A deadlock is a situation where a set of nodes are blocked and none of them can proceed.
- A deadlock can be detected by examining the wait-for graph (WFG) of the system, which is a directed graph that represents the resource requests and holds among the nodes.
- A node in the WFG corresponds to a node in the system, and an edge from node A to node B means that node A is waiting for a resource held by node B.
- A deadlock exists in the system if and only if the WFG contains a cycle.
- There are three main approaches to deadlock detection in distributed systems: centralized, hierarchical, and distributed.
- In the centralized approach, there is a designated node, called the coordinator, that is responsible for collecting the local WFGs from all the nodes and constructing the global WFG. The coordinator periodically checks the global WFG for cycles and initiates deadlock resolution if needed.
- In the hierarchical approach, the system is divided into clusters of nodes, and each cluster has a local coordinator that collects the local WFGs from the nodes in the cluster and constructs the cluster WFG. The cluster coordinators communicate with a global coordinator that collects the cluster WFGs and constructs the global WFG. The global coordinator periodically checks the global WFG for cycles and initiates deadlock resolution if needed.
- In the distributed approach, there is no coordinator, and each node participates in the deadlock detection algorithm. The nodes exchange messages to construct and check the global WFG in a distributed manner. There are different algorithms for distributed deadlock detection, such as edge chasing, diffusing computation, and probe-based algorithms.



### Resource Vs Communication Deadlocks

- A deadlock is a condition where a process cannot proceed because it needs to obtain a resource held by another process, and it itself is holding a resource that the other process needs.
- There are two types of deadlocks in distributed systems: resource deadlocks and communication deadlocks.
- Resource deadlocks occur when processes access resources, such as data objects in database systems and buffers in store and forward communication networks. A process acquires a resource before accessing it and releasing it after using it.
- Communication deadlocks occur when processes exchange messages, such as in message passing systems and distributed algorithms. A process sends a message to another process and waits for a reply before continuing.
- The main difference between resource deadlocks and communication deadlocks is that in resource deadlocks, the resources are explicitly acquired and released by the processes, while in communication deadlocks, the resources are implicitly allocated and freed by the communication system.
- Another difference is that in resource deadlocks, the processes are blocked by the resources they request, while in communication deadlocks, the processes are blocked by the messages they send or receive.
- Resource deadlocks can be detected by constructing a wait-for graph, where nodes represent processes and edges represent resource requests. A cycle in the graph indicates a deadlock.
- Communication deadlocks can be detected by constructing a dependency graph, where nodes represent processes and edges represent message dependencies. A cycle in the graph indicates a deadlock.



### Deadlock Prevention for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

- A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
- Deadlock prevention is a technique to ensure that at least one of the necessary conditions for deadlock does not hold in a system.
- In a distributed system, deadlock prevention is more challenging than in a centralized system, because the processes and resources are distributed across multiple nodes, and there is no global information or control.
- There are two main approaches to deadlock prevention in a distributed system: ordered request and collective request.

#### Ordered Request
- In this approach, each resource type is assigned a unique level, and a process can request resources only in increasing order of levels.
- This ensures that no circular wait can occur, as a process cannot request a resource that is already held by a lower-level resource.
- For example, if there are three resource types A, B, and C, with levels 1, 2, and 3 respectively, a process can request A, then B, then C, but not C, then A, then B.
- This approach requires a global agreement on the resource levels, and may impose unnecessary restrictions on the resource requests.

#### Collective Request
- In this approach, a process must request all the resources it needs at once, before starting its execution.
- This ensures that no hold and wait can occur, as a process cannot hold a resource while waiting for another resource.
- For example, if a process needs resources A, B, and C, it must request them all together, and not request A, then B, then C.
- This approach requires a global knowledge of the resource needs, and may cause underutilization of resources.



### Avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- Deadlock avoidance is a technique that prevents a system from entering a deadlock state by ensuring that the system is always in a safe state.
- A safe state is a state where there exists a sequence of resource allocations that can satisfy the requests of all processes without causing a deadlock.
- In a distributed system, deadlock avoidance is impractical due to several problems, such as:
  - The lack of global information about the resource allocation and requests of all processes.
  - The dynamic and unpredictable nature of the processes and resources in a distributed system.
  - The high communication and synchronization overhead involved in maintaining a global safe state.
- Therefore, deadlock detection is preferred over deadlock avoidance in distributed systems.
- Deadlock detection is a technique that identifies the existence of a deadlock in a system after it has occurred and takes appropriate actions to recover from it.
- Deadlock detection in distributed systems requires the following steps:
  - Collecting local information about the resource allocation and requests of each process and sending it to a coordinator or a set of coordinators.
  - Constructing a global wait-for graph that represents the dependencies among the processes and resources in the system.
  - Detecting a cycle in the global wait-for graph, which indicates a deadlock.
  - Initiating a recovery procedure to break the cycle and resolve the deadlock.



### Detection and Resolution of Distributed Deadlocks

- A distributed deadlock is a situation where a set of processes in a distributed system are waiting for each other to release resources or send messages, and none of them can proceed.
- Detection and resolution of distributed deadlocks involve two steps: finding the existing deadlocks and breaking them by releasing some resources or aborting some processes.
- Detection of distributed deadlocks requires the maintenance and analysis of a wait-for graph (WFG), which is a directed graph that represents the dependencies among processes and resources in the system.
- There are three main approaches to maintain and search the WFG for cycles, which indicate deadlocks:
  - Centralized approach: A single site is designated as the deadlock detector, which collects the local WFG information from all other sites and constructs a global WFG. The deadlock detector periodically searches the global WFG for cycles and informs the involved sites if a deadlock is detected. This approach is simple and efficient, but it has a single point of failure and may cause communication overhead and delays.
  - Distributed approach: Each site maintains its own local WFG and exchanges it with other sites to construct a global WFG. The sites cooperate to search the global WFG for cycles using a distributed algorithm, such as the Chandy-Misra-Haas algorithm or the Menasce-Muntz algorithm. This approach is fault-tolerant and scalable, but it may cause more communication overhead and complexity.
  - Hierarchical approach: The sites are organized into a hierarchy of clusters, each with a local deadlock detector. The local deadlock detectors collect the local WFG information from their cluster members and construct a cluster WFG. The cluster WFGs are then sent to higher-level deadlock detectors, which construct a higher-level WFG. The deadlock detection is performed at different levels of the hierarchy, starting from the lowest level. This approach is a compromise between the centralized and distributed approaches, but it may cause false or phantom deadlocks due to the aggregation of WFG information.
- Resolution of distributed deadlocks involves breaking the existing wait-for dependencies in the system WFG. There are two main strategies to resolve distributed deadlocks:
  - Preemption: Some processes involved in the deadlock are rolled back and their resources are released to other processes. This strategy preserves the work done by the processes, but it may cause cascading rollbacks and inconsistency of data.
  - Termination: Some processes involved in the deadlock are aborted and their resources are released to other processes. This strategy avoids cascading rollbacks and inconsistency of data, but it may cause lost work and missed deadlines.



### Centralized Deadlock Detection

- This is a technique used in distributed systems to handle deadlock detection.
- According to this approach, the system maintains one **global wait-for graph** in a single chosen site, which is named as **deadlock-detection coordinator**.
- The coordinator collects information about the **local wait-for graphs** of each site and constructs the global wait-for graph.
- The coordinator periodically runs a **cycle detection algorithm** on the global wait-for graph to detect deadlocks.
- If a deadlock is detected, the coordinator selects a victim process and sends an **abort message** to the site where the process is located.
- The advantages of this approach are:
  - It is simple and easy to implement.
  - It reduces the communication overhead and the number of messages exchanged.
- The disadvantages of this approach are:
  - It introduces a single point of failure and a performance bottleneck at the coordinator.
  - It requires the coordinator to have a global view of the system, which may not be feasible or accurate in some cases.
  - It may detect false or phantom deadlocks due to the delay in propagating the information to the coordinator.



### Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set.
- Deadlocks can occur in distributed systems when distributed transactions or concurrency control are used.
- Deadlock detection is the approach of identifying and resolving existing deadlocks in the system.
- Deadlock detection in distributed systems entails two basic issues:
  - Detection of existing deadlocks by examining the status of process-resource interactions for presence of cyclic wait.
  - Resolution of detected deadlocks by aborting one or more deadlocked processes.
- Deadlock detection in distributed systems can be done by using one of the following methods:
  - Centralized approach: A single node is designated as the deadlock detector and collects information from all other nodes about their resource requests and allocations. The deadlock detector constructs a global wait-for graph (WFG) and checks for cycles in it. If a cycle is found, the deadlock detector selects a victim process and sends a message to abort it.
  - Distributed approach: Each node maintains a local wait-for graph (WFG) and periodically sends it to a neighboring node. The neighboring node merges the received WFG with its own and forwards it to another node. This process continues until a node receives its own WFG back. The node then checks for cycles in the merged WFG and if found, selects a victim process and sends a message to abort it.
  - Hierarchical approach: The nodes are organized into a hierarchy of clusters. Each cluster has a coordinator node that collects information from its members and constructs a local WFG. The coordinators periodically exchange their WFGs with their parent or child coordinators and merge them. The root coordinator checks for cycles in the global WFG and if found, selects a victim process and sends a message to abort it.



### Path Pushing Algorithms

- Path pushing algorithms detect distributed deadlocks by maintaining an explicit global wait-for graph (WFG) at each site of the distributed system .
- The global WFG is constructed by merging the local WFGs of each site, which represent the waiting relationships among the processes at that site.
- Whenever a site performs a deadlock computation, it sends its local WFG to all its neighboring sites, which update their global WFGs accordingly.
- A site initiates a deadlock computation when it detects a local deadlock or receives a request from another site.
- A site detects a global deadlock by checking for cycles in its global WFG. If a cycle is found, the site sends a message to the initiator of the deadlock computation, which then selects a victim process to abort.
- The advantages of path pushing algorithms are that they can detect deadlocks quickly and accurately, and they do not require probe messages to traverse the WFG.
- The disadvantages of path pushing algorithms are that they require a lot of communication and storage overhead, and they may generate false cycles due to inconsistent global WFGs.



### Edge Chasing Algorithms for Distributed Deadlock Detection

- Edge chasing algorithms are a class of distributed deadlock detection algorithms that use special messages called probes to trace the dependency graph of processes and resources in a distributed system.
- A probe is a triplet (i, j, k) that denotes that the deadlock detection is initiated by process P_i and the message is being sent by the home site of process P_j to the home site of process P_k.
- The home site of a process is the site where the process is executing.
- A probe message is sent along the edges of the dependency graph, following the wait-for relations between processes.
- If a probe message returns to the initiator process, it means that a cycle exists in the dependency graph and a deadlock has occurred.
- One of the most well-known edge chasing algorithms is the Chandy-Misra-Haas algorithm, which works for the AND request model, where a process can request multiple resources simultaneously and wait for all of them to be granted.
- The Chandy-Misra-Haas algorithm works as follows:

  - Each process maintains a local wait-for graph that contains the processes that it is waiting for and the processes that are waiting for it.
  - When a process P_i initiates a deadlock detection, it sends a probe message (i, i, j) to the home site of each process P_j that it is waiting for.
  - When the home site of a process P_j receives a probe message (i, k, j), it checks if P_j is waiting for any other process. If not, it discards the message. If yes, it forwards the message to the home site of each process P_l that P_j is waiting for, with the probe message (i, j, l).
  - When the home site of the initiator process P_i receives a probe message (i, j, i), it declares a deadlock and initiates a recovery procedure.

- The advantages of edge chasing algorithms are:

  - They are simple and easy to implement.
  - They do not require global knowledge of the system state or a central coordinator.
  - They can detect deadlocks in a finite number of steps.

- The disadvantages of edge chasing algorithms are:

  - They may generate a large number of probe messages, which consume network bandwidth and processing power.
  - They may cause false positives, where a deadlock is detected even though it does not exist, due to the delay or loss of messages in the network.
  - They may not be able to handle dynamic changes in the system, such as process migration or resource relocation.



## Unit 4 - Agreement Protocols

- Agreement protocols are used in distributed systems to ensure that processes or sites can reach a common decision or goal in the presence of failures or uncertainties  .
- Agreement protocols can be classified into different types based on the problem they solve, such as consensus, atomic commit, leader election, group membership, etc  .
- Consensus is the problem of getting all processes to agree on a single value, such as a leader or a transaction outcome  . Consensus is impossible to achieve in asynchronous systems with even one faulty process.
- Atomic commit is the problem of getting all processes to agree on whether to commit or abort a transaction that involves multiple sites . Atomic commit can be solved by using two-phase commit (2PC) or three-phase commit (3PC) protocols .
- Leader election is the problem of getting all processes to agree on a unique process that acts as the coordinator or the master  . Leader election can be solved by using various algorithms, such as the bully algorithm, the ring algorithm, or the randomized algorithm  .
- Group membership is the problem of getting all processes to agree on a set of processes that are currently active or alive in the system . Group membership can be solved by using heartbeat messages, failure detectors, or gossip protocols .
- Agreement protocols must satisfy some properties, such as validity, agreement, termination, and integrity . Validity means that the agreed value must be proposed by some process. Agreement means that all processes must agree on the same value. Termination means that all processes must eventually decide on a value. Integrity means that the agreed value must not be changed once decided .



### Introduction for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by passing messages.
- Agreement protocols are a class of distributed algorithms that aim to achieve a common goal or value among a set of processes, despite the presence of failures or uncertainties.
- Agreement protocols are essential for ensuring the reliability, consistency, and fault-tolerance of distributed systems, especially in applications such as distributed databases, distributed consensus, leader election, group membership, and atomic actions  .
- Some of the challenges and requirements for designing agreement protocols in distributed systems are:
  - Dealing with partial failures, such as process crashes, network partitions, message losses, or Byzantine faults .
  - Achieving termination, validity, and agreement properties, which ensure that all correct processes eventually decide on a value, the decided value is valid according to some criterion, and all correct processes agree on the same value .
  - Balancing the trade-offs between performance, complexity, and resilience, such as minimizing the number of messages, rounds, or assumptions needed to reach agreement, while maximizing the number of faults tolerated .
  - Adapting to dynamic and heterogeneous environments, such as changing network topologies, process behaviors, or system parameters.
- Some of the examples and types of agreement protocols in distributed systems are:
  - Two-phase commit and three-phase commit protocols, which are used to coordinate the commit or abort decision of a distributed transaction among multiple data managers.
  - Paxos and Raft protocols, which are used to implement distributed consensus among a set of replicas, such that they can agree on a sequence of commands or updates.
  - Bully and ring algorithms, which are used to elect a leader among a set of processes, such that the leader has the highest priority or identifier.
  - Viewstamped replication and virtual synchrony protocols, which are used to maintain a consistent view of the group membership among a set of processes, such that they can detect and handle failures or joins.
  - Lamport's and vector clocks, which are used to synchronize the logical clocks of processes, such that they can order the events or messages in a causal or consistent manner.



### System models for distributed systems

- System models for distributed systems illustrate or describe common properties and design choices for distributed systems in a single descriptive model.
- System models can help to understand, analyze, and design distributed systems by abstracting away unnecessary details and focusing on the essential aspects.
- There are three main types of system models for distributed systems: physical models, architectural models, and interaction models .
- Physical models capture the hardware composition of a system in terms of computers and other devices and their interconnecting network.
  - Physical models can describe the topology, latency, bandwidth, reliability, and security of the network.
  - Physical models can also classify distributed systems into different categories, such as local-area networks (LANs), wide-area networks (WANs), mobile networks, wireless networks, and peer-to-peer networks.
- Architectural models describe the responsibilities distributed between system components and how these components are placed.
  - Architectural models can also define the communication patterns, coordination mechanisms, and data distribution among the components.
  - Architectural models can also classify distributed systems into different styles, such as client-server, peer-to-peer, publish-subscribe, broker, and service-oriented architectures .
- Interaction models describe the behavior of the system components and how they interact with each other through message passing.
  - Interaction models can specify the properties, assumptions, and guarantees of the communication channels, such as synchronous or asynchronous, reliable or unreliable, ordered or unordered, and causal or non-causal.
  - Interaction models can also specify the properties, assumptions, and guarantees of the system components, such as deterministic or non-deterministic, stateful or stateless, and fault-tolerant or fault-prone.
  - Interaction models can also define the protocols, algorithms, and strategies for achieving common goals, such as consensus, agreement, coordination, synchronization, replication, and consistency.



### Classification of Agreement Problem

An agreement problem in a distributed system is a problem where a set of processes need to agree on a common value or decision, despite the possibility of failures or malicious behavior of some processes. Agreement problems are fundamental for achieving fault tolerance and consistency in distributed systems.

There are different types of agreement problems, depending on the assumptions and requirements of the system. Some of the well-known agreement problems are:

- **Byzantine agreement problem**: A single value, which is to be agreed on, is initialized by an arbitrary process and all non-faulty processes have to agree on that value. The processes may have different initial values and may behave arbitrarily (including lying or sending conflicting messages). The goal is to reach agreement among the non-faulty processes, despite the presence of faulty or malicious processes. This problem is also known as the **Byzantine generals problem**  .

- **Consensus problem**: A generalization of the Byzantine agreement problem, where each process has its own initial value and proposes it to the other processes. The processes have to agree on a single value that is one of the proposed values. The processes may fail by crashing (but not by behaving arbitrarily). The goal is to reach agreement among the non-crashed processes, despite the possibility of failures. This problem is also known as the **commit problem** or the **atomic broadcast problem** .

- **Interactive consistency problem**: A generalization of the consensus problem, where each process has its own initial value and proposes it to the other processes. The processes have to agree on a vector of values, one for each process, such that the value for a process is either its initial value or the default value (if the process is faulty). The processes may behave arbitrarily (as in the Byzantine agreement problem). The goal is to reach agreement among the non-faulty processes, despite the presence of faulty or malicious processes. This problem is also known as the **Byzantine generals problem with signed messages** or the **generalized Byzantine agreement problem**  .

These problems are related to each other and have different levels of difficulty and feasibility, depending on the system model and the number of faulty processes. For example, the Byzantine agreement problem is a special case of the consensus problem, which is a special case of the interactive consistency problem. The consensus problem is impossible to solve in an asynchronous system with one or more crash failures, while the Byzantine agreement problem is impossible to solve in a synchronous system with more than one-third of faulty processes .

Agreement problems have many applications in distributed systems, such as:

- **Coordination**: Agreement problems can be used to coordinate the actions of multiple processes, such as committing a transaction, updating a replicated state, or electing a leader.
- **Reliable communication**: Agreement problems can be used to ensure reliable and ordered delivery of messages, such as broadcasting a message to all processes or multicasting a message to a subset of processes.
- **Fault detection**: Agreement problems can be used to detect and isolate faulty or malicious processes, such as by using a voting scheme or a challenge-response protocol.
- **Security**: Agreement problems can be used to achieve security properties, such as authentication, integrity, confidentiality, or non-repudiation, by using cryptographic techniques or trust models.



### Byzantine agreement problem

- The Byzantine agreement problem is a fundamental problem in fault tolerant distributed computing that requires a set of parties in a distributed environment to agree on a value even if some of the parties are corrupted.
- The problem was first defined by Lamport and inspired by a hypothetical scenario of several divisions of the Byzantine army camped outside an enemy city, each division commanded by its own general. The generals can communicate with one another only by messenger. After observing the enemy, they must decide upon a common plan of action.
- The problem is challenging because some of the generals may be traitors who try to prevent the loyal generals from reaching agreement. The traitors may send conflicting messages to different generals, or lie about their own observations or preferences. The loyal generals need a secure way to come to agreement on a plan (known as consensus) and carry out their chosen plan (known as coordination).
- A solution to the Byzantine agreement problem must satisfy the following properties:
  - **Termination**: Every loyal general eventually decides on a value.
  - **Agreement**: All loyal generals decide on the same value.
  - **Validity**: If all loyal generals have the same initial value, then they all decide on that value.
- A number of solutions to the Byzantine agreement problem exist, depending on the assumptions made about the communication model, the number of traitors, the synchrony of the system, and the type of the messages. Some of the well-known solutions are:
  - **Oral messages**: This solution assumes that messages are signed and authenticated, but can be forged by traitors. It requires that the number of traitors is less than one third of the total number of generals. It uses a recursive algorithm that involves sending and relaying messages among the generals.
  - **Signed messages**: This solution assumes that messages are signed and authenticated, and cannot be forged by traitors. It requires that the number of traitors is less than half of the total number of generals. It uses a simpler algorithm that involves sending and comparing messages among the generals.
  - **Randomized messages**: This solution assumes that messages are signed and authenticated, but can be forged by traitors. It does not have a bound on the number of traitors, but it only guarantees a probabilistic consensus. It uses a randomized algorithm that involves sending and flipping coins among the generals.
  - **Broadcast messages**: This solution assumes that messages are broadcasted to all generals, and that there is a designated source general who initiates the communication. It requires that the source general is loyal, and that the number of traitors is less than half of the total number of generals. It uses a simple algorithm that involves sending and echoing messages among the generals.



### Consensus problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- The consensus problem is the problem of getting a set of nodes in a distributed system to agree on something - it might be a value, a course of action or a decision.
- Achieving consensus allows a distributed system to act as a single entity, with every individual node aware of and in agreement with the actions of the whole of the network.
- Consensus is a general agreement on a decision made by the majority of those involved.
- Consensus is needed in a distributed system to ensure overall system reliability on top of unreliable system components.
- Consensus is also needed to coordinate distributed transactions, replicate data, elect leaders, and implement fault tolerance mechanisms.
- Consensus is hard to achieve in a distributed system due to the possibility of node failures, network partitions, message delays, and malicious attacks .
- There are many ways in which processes in a distributed system can reach a consensus, but there is usually a trade-off between security and performance.
- Some of the common consensus protocols are:
  - Two-phase commit: A simple and centralized protocol that requires a coordinator node to initiate and finalize the consensus among all participants.
  - Three-phase commit: An extension of two-phase commit that adds a pre-commit phase to avoid blocking in case of coordinator failure.
  - Paxos: A family of decentralized protocols that use a quorum of nodes to propose and accept values, and tolerate up to half of the nodes to fail.
  - Raft: A simplified version of Paxos that uses a leader node to propose values and replicate them to follower nodes, and handles leader election and log consistency.
  - Byzantine fault tolerance: A class of protocols that can tolerate arbitrary failures or malicious behaviors of up to one-third of the nodes, and use cryptographic techniques to ensure agreement.



### Interactive Consistency Problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- Interactive consistency is the problem in which n distinct nodes, each having its own private value, where up to t may be Byzantine, run an algorithm that allows all non-faulty nodes to infer the values of each other node  .
- Byzantine nodes are those that can behave arbitrarily, deviating from the protocol, sending conflicting messages, or crashing .
- Interactive consistency is a generalization of distributed consensus, where the goal is to reach the agreement in a distributed system in the presence of faults.
- Interactive consistency is relevant to critical applications that rely on the combination of the opinions of multiple peers to provide a service, such as fault-tolerant distributed systems, blockchain systems, or voting systems .
- Interactive consistency can be solved by using broadcast and consensus algorithms, such as reliable broadcast, authenticated broadcast, or randomized Byzantine consensus .
- Interactive consistency has different variants, such as oral messages, signed messages, or authenticated messages, depending on the assumptions about the communication channels and the cryptographic primitives .
- Interactive consistency has different lower bounds and impossibility results, depending on the number of nodes, the number of Byzantine nodes, and the synchrony of the system . For example, interactive consistency is impossible to solve in a fully asynchronous system with one-third or more Byzantine nodes.



### Solution to Byzantine Agreement problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- The Byzantine agreement problem is a fundamental problem in fault tolerant distributed computing, where a set of parties in a distributed environment need to agree on a value even if some of the parties are corrupted.
- The problem was first defined by Lamport and inspired by a hypothetical scenario of several divisions of the Byzantine army camped outside an enemy city, each division commanded by its own general. The generals can communicate with one another only by messenger. After observing the enemy, they must decide upon a common plan of action.
- The problem is that some of the generals may be traitors, who try to prevent the loyal generals from reaching agreement. The traitors may send conflicting messages to different generals, or send no messages at all. The loyal generals need a secure way to come to agreement on a plan (known as consensus) and carry out their chosen plan (known as coordination).
- A solution to the Byzantine agreement problem is a protocol that guarantees that all loyal generals agree on the same value, and that the value is the initial value of some loyal general. The protocol should work for any number of traitors, as long as they are less than one third of the total number of generals.
- One possible solution to the Byzantine agreement problem is the following:
  - The source general broadcasts its initial value to all other generals.
  - Each general who receives the message from the source general forwards it to all other generals, except the source general.
  - Each general who receives at least n/3 + 1 identical messages from different generals, including the source general, adopts that value as its decision value. Otherwise, it adopts a default value, such as 0.
  - The protocol terminates after two rounds of message passing.
- This solution ensures that all loyal generals agree on the same value, and that the value is the initial value of the source general, if the source general is loyal. The protocol can tolerate up to n/3 - 1 traitors, where n is the total number of generals. The protocol requires O(n^2) messages and O(1) rounds of communication.



### Application of Agreement Problem for the Notes of the Unit 4 - Agreement Protocols in the Subject of Distributed System

- Agreement problem is a fundamental problem in distributed systems, where a set of processes need to reach a common decision based on their individual inputs and messages exchanged with each other.
- Agreement problem has many variants, such as consensus, atomic broadcast, atomic commitment, group membership, etc. Each variant has different requirements and assumptions about the system model, such as synchrony, failure types, communication channels, etc.
- Agreement problem is essential for many applications in distributed systems, such as fault tolerance, replication, coordination, distributed transactions, distributed databases, etc .
- Some examples of applications of agreement problem are:

  - Atomic snapshot: A distributed data structure that allows processes to atomically read and write multiple shared registers. Atomic snapshot can be implemented using lattice agreement, a variant of agreement problem where processes need to agree on a value from a lattice.
  - Replicated state machine: A technique to implement a fault-tolerant service by replicating the service state and operations across multiple processes. Replicated state machine requires atomic broadcast, a variant of agreement problem where processes need to deliver the same sequence of messages.
  - Distributed transaction: A unit of work that involves multiple resources in a distributed system and needs to be executed atomically. Distributed transaction requires atomic commitment, a variant of agreement problem where processes need to agree on whether to commit or abort the transaction.
  - Group membership: A service that maintains the membership information of a group of processes in a distributed system and notifies the processes of any changes. Group membership requires consensus, a variant of agreement problem where processes need to agree on a single value.

- Solving agreement problem in distributed systems is challenging due to the possibility of failures, asynchrony, and malicious behavior of processes. Different algorithms and protocols have been proposed to solve agreement problem under different system models and assumptions, such as Paxos, Raft, Byzantine agreement, etc .
- Agreement problem is also related to some fundamental limitations and trade-offs in distributed systems, such as the FLP impossibility result, the CAP theorem, and the Byzantine generals problem .



### Atomic Commit in Distributed Database System

- An atomic commit is an operation that applies a set of distinct changes as a single operation. If the changes are applied, then the atomic commit is said to have succeeded. If the changes are not applied, then the atomic commit is said to have failed or aborted.
- In distributed database systems, the primary need for atomic commit protocols is to maintain the atomicity of distributed transactions. Atomicity means that either all the changes made by a transaction are committed or none of them are  .
- Atomic commit protocols are used to coordinate the distinct operations of a transaction across different database sites and then commit/rollback the transaction as needed. An atomic commit protocol guarantees that, in spite of possible failures or communication delays, all the sites agree on the final outcome of the transaction.
- There are two main types of atomic commit protocols: blocking and non-blocking. Blocking protocols require that some sites block or wait until the final outcome of the transaction is known, while non-blocking protocols allow all sites to continue processing other transactions without waiting .
- Blocking protocols are simpler and more efficient in normal situations, but they may cause performance degradation or deadlock in case of failures. Non-blocking protocols are more resilient and fault-tolerant, but they may incur more overhead and complexity .
- Some examples of blocking protocols are two-phase commit (2PC), three-phase commit (3PC), and presumed commit (PC). Some examples of non-blocking protocols are presumed abort (PA), presumed nothing (PN), and failure-aware atomic commit (FLAC)  .



## Unit 5 - Distributed Resource Management

- Distributed resource management (DRM) is an evolving discipline that uses software, hardware, network tools, procedures, and policies to enable distributed enterprise systems to operate effectively in production .
- DRM covers solutions for the daily monitoring, resource planning, system administration, change management, operations, and security of distributed systems.
- Distributed systems are systems that consist of multiple independent components that communicate and coordinate with each other over a network to achieve a common goal.
- Examples of distributed systems are cloud computing, peer-to-peer networks, distributed databases, and distributed energy resources.
- The main challenges of DRM are:
  - Managing the heterogeneity, scalability, and dynamism of distributed systems.
  - Balancing the trade-offs between performance, availability, consistency, and fault tolerance.
  - Ensuring the security, privacy, and trust of distributed systems and their users.
  - Optimizing the utilization and allocation of distributed resources.
- The main benefits of DRM are:
  - Improving the efficiency and reliability of distributed systems.
  - Reducing the operational costs and environmental impacts of distributed systems.
  - Enhancing the flexibility and adaptability of distributed systems.
  - Enabling the innovation and collaboration of distributed systems.



### Issues in Distributed File Systems

A distributed file system (DFS) is a system that allows multiple clients to access and manipulate files stored on one or more servers over a network. DFSs aim to provide high availability, scalability, performance, and transparency to the users. However, there are several issues and challenges in designing and implementing a DFS, such as:

- **Naming and name resolution**: A DFS needs a consistent and efficient way to name and locate files across different servers and clients. A common approach is to use a hierarchical namespace that maps file names to physical locations, such as paths or URLs. However, this approach may introduce problems such as name conflicts, name resolution failures, name caching, and name replication .
- **Consistency and replication**: A DFS may replicate files or parts of files across multiple servers to improve availability, fault tolerance, and load balancing. However, this also raises the issue of maintaining consistency among the replicas, especially when concurrent updates occur. A DFS needs to define a consistency model that specifies the guarantees and expectations for the users and the system. For example, a DFS may use strict consistency, which ensures that all replicas are always identical, or eventual consistency, which allows temporary divergence but guarantees eventual convergence .
- **Caching and performance**: A DFS may cache files or parts of files on the client side to reduce network traffic and improve response time. However, caching also introduces the issue of cache coherence, which is the problem of ensuring that the cached data is up to date with the server data. A DFS needs to implement a cache coherence protocol that defines how and when the cache is invalidated, updated, or refreshed. For example, a DFS may use write-through caching, which propagates updates to the server immediately, or write-back caching, which delays updates until the cache is full or evicted .
- **Security and access control**: A DFS needs to provide mechanisms to protect the files and the system from unauthorized or malicious access. A DFS needs to implement authentication, authorization, encryption, and auditing features to ensure the security and privacy of the data and the users. For example, a DFS may use passwords, tokens, certificates, or biometrics to authenticate users, and use access control lists, capabilities, or roles to authorize users .
- **Failure handling and recovery**: A DFS needs to cope with various types of failures that may occur in the network, the servers, or the clients. A DFS needs to detect, isolate, and recover from failures without compromising the functionality and performance of the system. For example, a DFS may use heartbeat messages, timeouts, or acknowledgments to detect failures, and use backups, checkpoints, or logs to recover from failures .
- **Scalability and heterogeneity**: A DFS needs to support a large number of users, files, and servers, and handle the dynamic changes in the system. A DFS also needs to accommodate the diversity of the hardware, software, and network platforms that may be involved in the system. For example, a DFS may use distributed hash tables, load balancing, or caching to achieve scalability, and use standard protocols, interfaces, or middleware to achieve heterogeneity .



### Mechanism for building distributed file systems

- A distributed file system (DFS) is a file system that is distributed on multiple file servers or locations, allowing programs to access or store isolated files as they do with the local ones.
- A DFS may use different mechanisms to build a reliable, scalable, and efficient file system, such as:
  - Use of file models: The DFS uses different conceptual models of a file, based on the file structure and modifiability. The files can be unstructured or structured, depending on the applications used in file systems. Unstructured files are treated as a sequence of bytes, while structured files have a specific format and organization.
  - Use of file accessing models: A DFS may use one of the following models to service a client's file requests:
    - Upload/download model: The client downloads the entire file from the server, modifies it locally, and uploads it back to the server. This model is suitable for small files that are rarely updated.
    - Remote access model: The client accesses the file on the server by sending read and write operations over the network. This model is suitable for large files that are frequently updated, but it may incur high network overhead.
    - Remote procedure call model: The client invokes remote procedures on the server to perform file operations. This model is more flexible and efficient than the remote access model, but it requires more complex protocols and security mechanisms.
  - Use of file replication: File replication is the primary mechanism for improving file availability and performance in a distributed systems environment. A replicated file is a file that has multiple copies with each copy located on a separate file server. The DFS may use different strategies to manage file replication, such as:
    - Static replication: The number and location of file replicas are fixed and predetermined by the system administrator. This strategy is simple and reliable, but it may not adapt well to dynamic workloads and network conditions.
    - Dynamic replication: The number and location of file replicas are determined by the DFS at runtime, based on the file access patterns and network status. This strategy is more flexible and responsive, but it may incur more overhead and complexity.
  - Use of file caching: File caching is another mechanism for improving file performance and reducing network traffic in a DFS. A file cache is a temporary storage area on the client or the server that holds a copy of a file or a file fragment. The DFS may use different policies to manage file caching, such as:
    - Write-through policy: The file cache is updated whenever the file is modified, and the changes are immediately propagated to the server. This policy ensures data consistency, but it may increase network latency and bandwidth consumption.
    - Write-back policy: The file cache is updated whenever the file is modified, but the changes are delayed until the cache is flushed to the server. This policy reduces network load, but it may compromise data consistency.
  - Use of cloud services: A DFS may use cloud services to extend its functionality and scalability to the cloud. Cloud services expose file and object storage using either standard protocols such as NFS and SMB or published APIs such as Amazon S3 and Google Cloud Storage. A DFS may use cloud services to store, access, or replicate files across different regions and platforms.



### Design issues in Distributed Shared Memory

Distributed Shared Memory (DSM) is a mechanism that allows multiple processes on different nodes to share a common logical address space and access data transparently. DSM can simplify the programming of distributed systems by hiding the details of inter-process communication. However, DSM also introduces several design issues that affect its performance, scalability, and correctness. Some of the main design issues in DSM are:

- **Granularity**: Granularity refers to the size of the unit of sharing and the unit of coherence in DSM. A smaller granularity (such as a byte or a word) can reduce the amount of false sharing and improve the locality of access, but it can also increase the overhead of coherence maintenance and communication. A larger granularity (such as a page or a segment) can reduce the overhead of coherence and communication, but it can also increase the amount of false sharing and waste bandwidth and memory. Therefore, choosing an appropriate granularity is a trade-off between these factors.

- **Structure**: Structure refers to the organization of the shared data in the logical address space and the mapping of the shared data to the physical memory of the nodes. The structure of DSM can be flat, hierarchical, or object-based. A flat structure treats the shared data as a single linear array and maps it to the nodes using a static or dynamic hashing function. A hierarchical structure divides the shared data into multiple regions and maps each region to a node using a directory or a home-based scheme. An object-based structure treats the shared data as a collection of objects and maps each object to a node using a naming or a location service. The structure of DSM affects the ease of programming, the flexibility of allocation, and the efficiency of access.

- **Coherence semantics**: Coherence semantics define the consistency model of DSM, which specifies the rules and guarantees for the ordering and visibility of updates to the shared data. Coherence semantics can be strict, relaxed, or weak. A strict coherence semantics (such as sequential consistency or cache coherence) ensures that all processes see the same order and value of updates to the shared data, but it can also impose a high synchronization and communication cost. A relaxed coherence semantics (such as release consistency or entry consistency) allows some updates to be delayed or reordered, but it can also reduce the synchronization and communication cost and improve the concurrency and scalability of DSM. A weak coherence semantics (such as eventual consistency or lazy consistency) provides no guarantees for the ordering and visibility of updates, but it can also tolerate network failures and partitions and support disconnected operation of DSM.

- **Scalability**: Scalability refers to the ability of DSM to handle a large number of nodes, processes, and data without degrading the performance or increasing the complexity of the system. Scalability depends on several factors, such as the granularity, the structure, the coherence semantics, and the implementation methods of DSM. Some of the techniques that can improve the scalability of DSM are: using a hierarchical or a distributed directory for coherence maintenance, using a multicast or a broadcast network for communication, using a lazy or a diff-based update protocol for data transfer, using a relaxed or a weak coherence semantics for consistency, and using a dynamic or a adaptive load balancing for allocation.

- **Heterogeneity**: Heterogeneity refers to the diversity of the nodes, processes, and data in DSM. Heterogeneity can be in terms of the hardware architecture, the operating system, the network protocol, the data format, or the application domain of the nodes and processes. Heterogeneity can pose several challenges for the design and implementation of DSM, such as: ensuring the portability and interoperability of the DSM software, ensuring the compatibility and correctness of the data access and manipulation, ensuring the fairness and efficiency of the resource allocation and utilization, and ensuring the security and privacy of the data and communication. Some of the techniques that can address the heterogeneity of DSM are: using a standard or a common interface for the DSM software, using a transparent or a explicit conversion for the data format, using a uniform or a customized policy for the resource management, and using a secure or a encrypted protocol for the data and communication.



### Algorithm for Implementation of Distributed Shared Memory

Distributed Shared Memory (DSM) is a technique that allows multiple processes on different nodes of a distributed system to share a common virtual address space and access the same data objects. DSM can simplify the programming of distributed applications by providing a uniform view of memory and hiding the details of data distribution and communication.

There are different algorithms for implementing DSM, each with its own advantages and disadvantages. Some of the basic algorithms are:

- **Central Server Algorithm**: In this algorithm, a central server maintains all the shared data and services the read and write requests from other nodes. The central server can use a page-based or an object-based approach to manage the shared data. The advantage of this algorithm is that it is simple and ensures data consistency. The disadvantage is that it introduces a single point of failure and a performance bottleneck, as all the requests have to go through the central server.

- **Migration Algorithm**: In this algorithm, the shared data is initially stored at the central server, but it can migrate to other nodes upon request. When a node wants to read or write a data item, it requests the central server for the location of that item. If the item is not at the central server, the server forwards the request to the node that has the item. The node that has the item can either send a copy of the item to the requester, or transfer the ownership of the item to the requester. The advantage of this algorithm is that it reduces the network traffic and the load on the central server, as the data can move closer to the nodes that access it frequently. The disadvantage is that it may cause data inconsistency, as multiple copies of the same item may exist in the system.

- **Replication Algorithm**: In this algorithm, the shared data is replicated on multiple nodes, and each node can access the local copy of the data. The replication can be done eagerly or lazily, depending on whether the updates are propagated to all the copies immediately or on demand. The advantage of this algorithm is that it improves the availability and the performance of the system, as the nodes can access the data locally without contacting the central server or other nodes. The disadvantage is that it requires more storage space and more communication overhead to maintain the consistency of the replicas.

- **Invalidation Algorithm**: In this algorithm, the shared data is cached on the nodes that access it, and the central server keeps track of the cache status of each data item. When a node wants to read a data item, it first checks its local cache. If the item is in the cache and it is valid, the node can read it locally. If the item is not in the cache or it is invalid, the node requests the central server for the latest version of the item. When a node wants to write a data item, it first invalidates the copies of the item on other nodes by sending invalidation messages through the central server. Then, it writes the item locally and updates the central server. The advantage of this algorithm is that it reduces the network traffic and the load on the central server, as the nodes can read the data locally most of the time. The disadvantage is that it may cause data inconsistency, as the nodes may read stale data from their caches.



## Unit 6 - Failure Recovery in Distributed Systems

- In distributed systems, failures are inevitable and can affect the availability, consistency, and performance of the system.
- Failure recovery is the process of restoring the system to a correct and consistent state after a failure occurs.
- Failure recovery techniques can be classified into two categories: backward recovery and forward recovery.
- Backward recovery involves undoing the effects of a failure and restoring the system to a previous consistent state, such as using checkpoints, logging, or rollback.
- Forward recovery involves correcting the effects of a failure and continuing the execution from the current state, such as using redundancy, replication, or voting.
- The choice of recovery technique depends on the type and frequency of failures, the system requirements, and the cost and complexity of implementation.
- Some of the challenges and trade-offs of failure recovery in distributed systems are:
  - How to detect and locate failures in a timely and accurate manner.
  - How to coordinate the recovery actions among multiple components or nodes.
  - How to ensure the consistency and correctness of the system state after recovery.
  - How to minimize the overhead and performance impact of recovery mechanisms.
  - How to handle concurrent and cascading failures.



### Concepts in Backward and Forward Recovery

- Backward recovery and forward recovery are two techniques for restoring the system to a consistent state after a failure in a distributed system.
- Backward recovery involves rolling back the system to a previous error-free state by using checkpoints and logs. Forward recovery involves correcting the errors and continuing the execution from the current state.
- The main difference between backward and forward recovery is that backward recovery discards the work done after the error, while forward recovery preserves the work done before and after the error.
- Backward recovery is more general and independent of the nature of faults, but it may incur more overhead and waste of resources. Forward recovery is more efficient and avoids unnecessary rollbacks, but it requires accurate assessment and removal of errors.
- Some examples of backward recovery protocols are checkpointing, message logging, and rollback-dependency tracking. Some examples of forward recovery techniques are error correction codes, redundancy, and replication.



### Recovery in Concurrent Systems

- Recovery in concurrent systems is the process of restoring the system to a consistent state after a failure or an error occurs.
- Recovery in concurrent systems is challenging because multiple transactions may be executing in parallel and may have interdependencies or conflicts with each other.
- Recovery in concurrent systems can be classified into two main categories: backward recovery and forward recovery.
- Backward recovery is the technique of undoing the effects of erroneous or failed transactions and restoring the system to a previous consistent state.
- Forward recovery is the technique of correcting the errors or failures without undoing the effects of previous transactions and advancing the system to a new consistent state.
- Backward recovery can be implemented using techniques such as logging, checkpoints, shadow paging, and transaction rollback.
- Forward recovery can be implemented using techniques such as redundancy, replication, error correction codes, and compensation transactions.
- The choice of recovery technique depends on factors such as the type and frequency of failures, the performance and availability requirements, the concurrency control scheme, and the system architecture.



### Obtaining consistent Checkpoints for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Failure recovery in distributed systems is the process of restoring the system to a consistent and correct state after a failure occurs.
- Failure recovery is essential for fault tolerance, which is the ability of the system to continue functioning despite the presence of errors.
- One of the common mechanisms for failure recovery is checkpoint-based, which involves periodically saving the state of the system or its components to a stable storage .
- Checkpoints are snapshots of the system state that can be used to resume the computation from a known point in case of a failure.
- Obtaining consistent checkpoints is a challenge in distributed systems, because the system consists of multiple components that may be executing concurrently and communicating with each other.
- A consistent checkpoint is one that reflects a global state of the system that could have occurred during the normal execution of the system.
- A consistent checkpoint should satisfy the following properties:
  - No orphan message: A message is orphan if it is received by a process after its checkpoint, but sent by a process before its checkpoint.
  - No domino effect: The domino effect occurs when a failure forces the system to roll back to an earlier checkpoint, which in turn causes another failure that requires another rollback, and so on.
- There are two main approaches for obtaining consistent checkpoints in distributed systems:
  - Coordinated checkpointing: In this approach, all the processes in the system coordinate with each other to take a global checkpoint at the same time. This ensures that no orphan messages or domino effects occur, but it requires a lot of synchronization and communication overhead.
  - Uncoordinated checkpointing: In this approach, each process in the system takes its own checkpoint independently, without any coordination with other processes. This reduces the overhead of synchronization and communication, but it may result in inconsistent checkpoints that contain orphan messages or domino effects. To resolve these inconsistencies, some additional techniques are needed, such as message logging or dependency tracking.



### Recovery in Distributed Database Systems

- Recovery in distributed database systems aims to maintain the **atomicity** and **durability** of distributed transactions.
- A distributed transaction is a transaction that accesses data from multiple sites in a distributed database system.
- Recovery in distributed database systems is more complicated than in centralized database systems because failures can occur at the communication links or a remote site.
- A failure in a distributed database system can affect one or more sites, one or more transactions, or one or more communication links.
- A recovery system should be simple, incur tolerable overhead, maintain system consistency, provide partial operability and avoid global rollback.
- There are two main approaches for recovery in distributed database systems: **centralized recovery** and **decentralized recovery**.
- Centralized recovery relies on a single site to coordinate the commit or abort of distributed transactions. This site is called the **coordinator**.
- Decentralized recovery relies on multiple sites to cooperate in the commit or abort of distributed transactions. Each site is called a **participant**.
- Both approaches use a **two-phase commit protocol** (2PC) to ensure the atomicity of distributed transactions.
- The two-phase commit protocol consists of two phases: the **prepare phase** and the **commit phase**.
- In the prepare phase, the coordinator (or a participant) sends a prepare message to all the participants (or the coordinator) involved in the transaction, asking them to vote on whether to commit or abort the transaction.
- In the commit phase, the coordinator (or a participant) collects the votes from all the participants (or the coordinator) and decides whether to commit or abort the transaction based on the majority rule.
- If the coordinator (or a participant) decides to commit the transaction, it sends a commit message to all the participants (or the coordinator) and writes a commit record in its log.
- If the coordinator (or a participant) decides to abort the transaction, it sends an abort message to all the participants (or the coordinator) and writes an abort record in its log.
- The participants (or the coordinator) follow the decision of the coordinator (or a participant) and write a commit or abort record in their logs accordingly.
- The two-phase commit protocol ensures that all the sites involved in a distributed transaction agree on the same outcome.
- However, the two-phase commit protocol has some drawbacks, such as blocking, deadlock, and vulnerability to failures.
- Blocking occurs when a site waits for a message from another site that has failed or is unreachable.
- Deadlock occurs when two or more sites wait for each other to send a message, forming a cycle.
- Vulnerability to failures occurs when a site fails before or after sending a message, causing inconsistency or loss of information.
- To overcome these drawbacks, some variations of the two-phase commit protocol have been proposed, such as the **three-phase commit protocol** (3PC), the **presumed abort protocol** (PA), and the **presumed commit protocol** (PC).
- The three-phase commit protocol adds a third phase, called the **pre-commit phase**, between the prepare phase and the commit phase.
- In the pre-commit phase, the coordinator (or a participant) sends a pre-commit message to all the participants (or the coordinator) after receiving all the votes, indicating that the transaction will be committed.
- The participants (or the coordinator) acknowledge the pre-commit message and wait for the final commit message.
- The pre-commit phase reduces the blocking problem by allowing the participants (or the coordinator) to decide the outcome of the transaction independently if the coordinator (or a participant) fails after sending the pre-commit message.
- However, the three-phase commit protocol introduces more messages and delays, and does not eliminate the deadlock and vulnerability to failures problems completely.
- The presumed abort protocol and the presumed commit protocol are based on the idea of **presumptions**.
- A presumption is a default outcome of a transaction that is assumed by a site in case of a failure or a timeout.
- The presumed abort protocol assumes that a transaction is aborted unless it receives a commit message from the coordinator (or a participant).
- The presumed commit protocol assumes that a transaction is committed unless it



## Unit 7 - Fault Tolerance

- Fault tolerance is the property that enables a system to continue operating properly in the event of the failure of one or more faults within some of its components.
- The objective of creating a fault-tolerant system is to prevent disruptions arising from a single point of failure, ensuring the high availability and business continuity of the system.
- Fault tolerance can be achieved by using various techniques, such as redundancy, replication, backup, recovery, error detection and correction, etc.
- Fault tolerance can be applied at different levels of a system, such as hardware, software, network, data, etc.
- Fault tolerance can be classified into different types, such as active, passive, hybrid, etc., depending on the degree of redundancy and the mode of operation of the system components.
- Fault tolerance can be measured by various metrics, such as reliability, availability, mean time to failure, mean time to repair, etc.
- Fault tolerance can be evaluated by various methods, such as fault injection, testing, simulation, modeling, etc.



### Issues in Fault Tolerance for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Fault tolerance is the ability of a system to continue functioning correctly in the presence of failures.
- Fault tolerance is important for distributed systems because they consist of multiple components that may be subject to failures, such as hardware faults, software bugs, network errors, malicious attacks, etc.
- Fault tolerance can be achieved by using various techniques, such as redundancy, replication, checkpointing, recovery, consensus, etc.
- Fault tolerance can be classified into different levels, such as detection, masking, tolerance, recovery, and prevention.
- Fault tolerance can also be categorized into different types, such as passive, active, hybrid, adaptive, etc.
- Fault tolerance faces several challenges and issues in distributed systems, such as:
  - How to detect and identify failures in a timely and accurate manner?
  - How to ensure consistency and availability of data and services in the presence of failures?
  - How to balance the trade-offs between performance, cost, and reliability of fault-tolerant techniques?
  - How to cope with different types and models of failures, such as crash, omission, timing, Byzantine, etc?



### Commit Protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Commit protocols are algorithms that ensure the atomicity of distributed transactions, i.e., all the sites involved in a transaction either commit or abort it unanimously, even in the presence of failures  .
- Commit protocols are necessary to maintain the consistency and reliability of distributed systems, as they prevent partial execution or data loss due to network or site failures  .
- There are different types of commit protocols, such as one-phase commit (1PC), two-phase commit (2PC), and three-phase commit (3PC), each with its own advantages and disadvantages    .
- One-phase commit (1PC) is the simplest commit protocol, where a coordinator sends a commit or abort message to all the participating sites, and they execute the transaction accordingly .
  - The advantage of 1PC is that it is fast and simple, as it requires only one round of communication .
  - The disadvantage of 1PC is that it is not fault-tolerant, as a single failure of the coordinator or a site can cause inconsistency or data loss .
- Two-phase commit (2PC) is the most widely used commit protocol, where a coordinator initiates a voting phase and a decision phase to reach a consensus among the participating sites    .
  - In the voting phase, the coordinator sends a prepare message to all the sites, and they reply with a yes or no vote, indicating whether they are ready to commit or abort the transaction    .
  - In the decision phase, the coordinator collects the votes and decides to commit or abort the transaction based on the majority. It then sends a commit or abort message to all the sites, and they execute the transaction accordingly    .
  - The advantage of 2PC is that it is fault-tolerant, as it ensures that all the sites agree on the same outcome, and it uses a log to recover from failures    .
  - The disadvantage of 2PC is that it is blocking, as a failure of the coordinator or a site can cause the other sites to wait indefinitely for a decision    .
- Three-phase commit (3PC) is an extension of 2PC, where a coordinator adds a pre-commit phase between the voting phase and the decision phase to avoid blocking .
  - In the pre-commit phase, the coordinator sends a pre-commit message to all the sites that voted yes in the voting phase, and they reply with an acknowledgment, indicating that they are ready to commit the transaction .
  - In the decision phase, the coordinator sends a commit or abort message to all the sites, and they execute the transaction accordingly .
  - The advantage of 3PC is that it is non-blocking, as it allows the sites to decide on their own in case of a coordinator failure, based on a timeout mechanism .
  - The disadvantage of 3PC is that it is more complex and costly, as it requires an extra round of communication and more log entries .



### Voting protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Voting protocols are a type of consensus protocols that allow a set of distributed nodes to agree on a common value or decision, despite the presence of faults or attacks.
- Voting protocols are useful for achieving fault tolerance in distributed systems, such as replicated databases, distributed file systems, or blockchain networks.
- Voting protocols can be classified into two categories: exact voting and inexact voting.
  - Exact voting requires all nodes to agree on the same value or decision, and is typically implemented using two-phase commit or three-phase commit protocols.
  - Inexact voting allows some nodes to have different values or decisions, as long as a majority or a weighted majority of nodes agree on the same value or decision. Inexact voting is more flexible and resilient to faults or attacks, but may incur more communication overhead or inconsistency.
- Voting protocols can also be distinguished by their fairness properties, which measure how well they balance the interests or preferences of different nodes or groups of nodes.
  - Fairness can be defined in terms of Pareto optimality, envy-freeness, or proportional representation, among other criteria.
  - Fairness is important for ensuring the legitimacy and stability of the consensus outcome, especially in heterogeneous or adversarial networks, where different nodes may have different levels of reputation or weight.
  - Fairness can be achieved by using appropriate voting rules, such as plurality, Borda, or Condorcet, or by using cryptographic techniques, such as secret sharing, zero-knowledge proofs, or homomorphic encryption.



### Dynamic voting protocols

- Dynamic voting protocols are a technique for maintaining consistency and availability of replicated data in distributed systems.
- The idea is to assign a number of votes to each replica of a data item, and to require a majority of votes to access or update the data item.
- The number of votes can be dynamically adjusted based on the availability and reliability of the replicas, the network topology, and the access patterns of the data item.
- Dynamic voting protocols can improve the performance and fault tolerance of distributed systems by reducing the communication and synchronization overhead, and by allowing more concurrency and flexibility in accessing the data item.
- Some examples of dynamic voting protocols are:

  - Dynamic weighted voting: A protocol that assigns different weights to different replicas based on their availability and reliability, and requires a weighted majority of votes to access or update the data item  .
  - Topological dynamic voting: A protocol that assigns votes to replicas based on their network proximity and connectivity, and requires a majority of votes within a non-partitionable group of replicas to access or update the data item .
  - Quorum-based voting: A protocol that defines a set of subsets of replicas, called quorums, such that any two quorums have a non-empty intersection, and requires a quorum of votes to access or update the data item.



## Unit 8 - Transactions and Concurrency Control

- A **transaction** is a logical unit of work that consists of a sequence of operations on a database, such as reading, writing, inserting, deleting, or updating data.
- A transaction has four main properties, known as **ACID**:
  - **Atomicity**: A transaction is either executed completely or not at all. If any operation in the transaction fails, the whole transaction is aborted and the database is restored to its previous state.
  - **Consistency**: A transaction preserves the integrity and validity of the database. It ensures that the database satisfies all the constraints and rules before and after the transaction.
  - **Isolation**: A transaction is executed independently of other concurrent transactions. It does not interfere with or see the intermediate results of other transactions.
  - **Durability**: A transaction's effects are permanent and persistent in the database. They are not lost even in the event of a system failure or power outage.
- **Concurrency control** is the management of simultaneously executing transactions in a shared database. It ensures that correct results for concurrent operations are generated while getting those results as quickly as possible.
- Concurrency control is important because it helps to maintain the **serializability** and **recoverability** of transactions. Serializability means that the outcome of concurrent transactions is equivalent to some serial execution of the same transactions. Recoverability means that the transactions can be undone or redone in case of a failure or abort.
- Concurrency control can be implemented using various techniques, such as:
  - **Lock-based protocols**: These protocols use locks to prevent multiple transactions from accessing the same data item at the same time. A lock can be either shared or exclusive, depending on the operation. A shared lock allows read-only access, while an exclusive lock allows read-write access. A transaction must acquire the appropriate lock before accessing a data item and release it after finishing. Lock-based protocols can prevent **conflicts**, such as **lost updates**, **dirty reads**, and **unrepeatable reads**, but they can also cause **deadlocks**, where two or more transactions are waiting for each other to release locks.
  - **Timestamp-based protocols**: These protocols use timestamps to order the transactions and determine their precedence. A timestamp is a unique identifier that reflects the start time of a transaction. A transaction must have a timestamp before accessing any data item. A timestamp-based protocol compares the timestamps of the transactions and the data items to decide whether to allow or reject an operation. Timestamp-based protocols can prevent conflicts and deadlocks, but they can also cause **aborts**, where a transaction is rolled back due to a timestamp violation.
  - **Optimistic protocols**: These protocols assume that conflicts are rare and allow transactions to execute without any locking or timestamping. However, they validate the transactions before committing them to the database. A transaction is validated by checking whether it has any conflicts with other concurrent transactions. If a conflict is detected, the transaction is aborted and restarted. Optimistic protocols can reduce the overhead of locking and timestamping, but they can also increase the abort rate and the response time of transactions.



### Transactions
- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the operations in a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction does not interfere with other concurrent transactions.
- Durability means that the effects of a transaction are permanent even in the case of failures.

### Distributed Transactions
- A distributed transaction is a transaction that spans multiple data servers in a distributed database system.
- A distributed transaction consists of a set of subtransactions, each of which is executed by one data server.
- A distributed transaction coordinator is a component that manages the execution of distributed transactions across the data servers.
- A distributed transaction has the same ACID properties as a local transaction, but it is more complex and challenging to implement.

### Concurrency Control
- Concurrency control is the technique of ensuring the correct and consistent execution of multiple transactions that access the same data concurrently.
- Concurrency control prevents problems such as lost updates, dirty reads, unrepeatable reads, and phantom reads, which can compromise the integrity and consistency of the database.
- Concurrency control can be implemented using various methods, such as locking, timestamping, validation, and multiversioning.

### Distributed Concurrency Control
- Distributed concurrency control is the concurrency control of a distributed database system, where relevant data is hosted by a group of linked data servers.
- Distributed concurrency control provides a mechanism to synchronize distributed transactions in such a way that the ACID properties are not violated by their interleaved execution.
- Distributed concurrency control makes sure that all subtransactions of a set of distributed transactions are serialized identically in all data servers involved.
- Distributed concurrency control can be classified into two categories: centralized and decentralized.
- Centralized distributed concurrency control relies on a single coordinator to manage the locks and timestamps of the data items across the data servers.
- Decentralized distributed concurrency control relies on a distributed algorithm to coordinate the locks and timestamps of the data items among the data servers.



### Nested transactions for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A transaction is a sequence of operations that satisfies the ACID properties (Atomicity, Consistency, Isolation, Durability).
- A nested transaction is a transaction that is composed of subtransactions, each of which may have its own begin and end points, and may be executed concurrently or sequentially.
- A nested transaction that accesses objects handled by different servers is referred to as a distributed transaction.
- Nested transactions in distributed systems have several advantages, such as:
  - They allow for more concurrency and parallelism, as subtransactions can execute independently and commit or abort without affecting the parent transaction.
  - They provide more flexibility and modularity, as subtransactions can be reused, nested, or aborted without affecting the parent transaction.
  - They facilitate error recovery and fault tolerance, as subtransactions can be retried, compensated, or aborted without affecting the parent transaction.
  - They enable partial results and feedback, as subtransactions can return intermediate results or status to the parent transaction.
- Nested transactions in distributed systems have several challenges, such as:
  - They require more coordination and communication among the servers involved in the transaction, as subtransactions may depend on each other or conflict with each other.
  - They introduce more complexity and overhead in the transaction management, as subtransactions may have different levels of isolation, consistency, and durability.
  - They raise more issues in the transaction commit and abort protocols, as subtransactions may have different outcomes or dependencies.
- Nested transactions in distributed systems can be structured in two different ways: flat transactions and nested transactions.
  - A flat transaction has a single initiating point (Begin) and a single end point (Commit or abort). They are usually very simple and are generally used for short activities rather than larger ones.
  - A nested transaction has multiple initiating points and end points, corresponding to the subtransactions. They are usually more complex and are generally used for long or composite activities that involve multiple servers or objects.
- Nested transactions in distributed systems can be implemented using different protocols, such as:
  - Two-phase commit (2PC): A protocol that ensures atomicity and consistency of a distributed transaction by coordinating the commit or abort decision among all the servers involved in the transaction. It consists of two phases: a prepare phase and a commit phase.
  - Three-phase commit (3PC): A protocol that extends 2PC by adding a pre-commit phase that ensures that all the servers are ready to commit before the final commit phase. It improves the fault tolerance and availability of the distributed transaction, as it avoids blocking in case of failures or network partitions.
  - Presumed abort (PA): A protocol that optimizes 2PC by reducing the number of messages and disk writes required for the commit or abort decision. It assumes that a transaction will abort unless it receives a commit request from the coordinator, and it does not require an acknowledgment from the servers for the abort decision.
  - Presumed commit (PC): A protocol that optimizes 2PC by reducing the number of messages and disk writes required for the commit or abort decision. It assumes that a transaction will commit unless it receives an abort request from the coordinator, and it does not require an acknowledgment from the servers for the commit decision.
  - Nested two-phase commit (N2PC): A protocol that extends 2PC to support nested transactions by allowing subtransactions to commit or abort independently of the parent transaction. It consists of two phases: a local commit phase and a global commit phase.
  - Saga: A protocol that supports nested transactions by allowing subtransactions to commit independently of the parent transaction, and compensating for any subtransaction that aborts by executing a compensating subtransaction that reverses its effects. It ensures eventual consistency and durability of the distributed transaction, but not atomicity or isolation.



### Locks for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A lock is a mechanism that allows only one of the innumerable nodes or processes to access and modify a resource or data that is being shared commonly to prevent execution of same task twice and also maintain data integrity.
- Locks are designed to enforce a mutual exclusion concurrency control policy, which means that only one process can hold a lock on a resource at a time, and any other process that wants to access the same resource has to wait until the lock is released.
- Locks can be classified into different types based on the following criteria  :
  - The granularity of the resource: locks can be applied to a whole database, a table, a page, a row, or a field, depending on the level of concurrency and isolation required.
  - The mode of the lock: locks can be either shared or exclusive, depending on whether the process holding the lock intends to read or write the resource. Shared locks allow multiple processes to read the same resource, but prevent any process from writing it. Exclusive locks allow only one process to write the resource, but prevent any other process from reading or writing it.
  - The duration of the lock: locks can be either long-lived or short-lived, depending on whether the process holding the lock keeps it until the end of the transaction or releases it as soon as possible. Long-lived locks reduce the concurrency and increase the risk of deadlock, but ensure the consistency and durability of the transaction. Short-lived locks increase the concurrency and reduce the risk of deadlock, but may compromise the consistency and durability of the transaction.
  - The security of the lock: locks can be either pessimistic or optimistic, depending on whether the process holding the lock assumes that conflicts are rare or frequent. Pessimistic locks acquire the lock before accessing the resource, and block any other process that tries to access the same resource. Optimistic locks access the resource without acquiring the lock, and check for conflicts at the end of the transaction. If a conflict is detected, the transaction is aborted and restarted.
- Locks can be implemented in different ways in a distributed system, depending on the architecture and the communication model of the system  :
  - Centralized locking: a single node or process acts as the lock manager, and grants or denies lock requests from other nodes or processes. This approach simplifies the lock management, but introduces a single point of failure and a performance bottleneck.
  - Distributed locking: each node or process manages its own locks, and communicates with other nodes or processes to coordinate the lock requests. This approach eliminates the single point of failure and the performance bottleneck, but complicates the lock management and increases the network overhead.
  - Consensus-based locking: each node or process participates in a consensus protocol, such as Paxos or Raft, to agree on the lock requests and the lock state. This approach ensures the consistency and fault tolerance of the lock management, but requires more computation and communication resources.



### Optimistic Concurrency Control

- Optimistic concurrency control (OCC) is a concurrency control method applied to transactional systems such as relational database management systems and software transactional memory.
- OCC assumes that multiple transactions can frequently complete without interfering with each other, and does not use locking or timestamping techniques to prevent conflicts .
- Instead, a transaction is executed without restrictions until it is committed, and then it is validated to check if any conflicts occurred with other concurrent transactions.
- If a conflict is detected, the transaction is aborted and restarted, otherwise it is committed.
- OCC has three phases: read, validation and write.
  - In the read phase, the transaction reads the data from the database and performs its operations, without acquiring any locks or updating the database.
  - In the validation phase, the transaction checks if any other transaction has modified the data that it has read or written, using some validation rules.
  - In the write phase, if the validation succeeds, the transaction writes its updates to the database, otherwise it aborts and restarts.
- OCC is suitable for distributed systems, where locking or timestamping may incur high communication overhead or limit the scalability of the system.
- OCC can improve the performance and throughput of the system, as transactions can execute concurrently without blocking or waiting for each other.
- However, OCC may also increase the abort rate and the response time of the system, as transactions may have to restart multiple times due to conflicts.
- To reduce the number of restarts, some OCC protocols use locking or timestamping techniques to guarantee a successful second execution for a failed transaction.



### Timestamp ordering

- Timestamp ordering is a technique for ensuring serializability of transactions in a distributed system.
- A transaction is a sequence of operations that must be executed atomically, i.e., either all or none of them are performed.
- Serializability means that the concurrent execution of transactions produces the same result as some sequential execution of them.
- Timestamp ordering assigns a unique timestamp to each transaction when it starts, and uses these timestamps to order the operations of different transactions.
- A timestamp can be either a logical clock value or a physical clock value, depending on the implementation.
- The basic idea of timestamp ordering is that a transaction can only read or write an object if its timestamp is greater than the timestamp of the last transaction that accessed the object.
- If a transaction tries to access an object with a lower timestamp, it is aborted and restarted with a new timestamp.
- This ensures that the transactions are executed in a consistent order, and that no transaction can overwrite the changes of a later transaction.
- Timestamp ordering can be implemented in a centralized or decentralized manner, depending on the architecture of the distributed system.
- In a centralized system, there is a single timestamp server that assigns timestamps to transactions and maintains the last access timestamps of all objects.
- In a decentralized system, each node has its own local timestamp generator and maintains the last access timestamps of the objects it owns.
- The nodes communicate with each other to synchronize their timestamps and resolve conflicts.



### Comparison of methods for concurrency control

Concurrency control is the process of managing the simultaneous execution of transactions in a distributed system, such that the consistency and correctness of the data are preserved. There are various methods for concurrency control, each with its own advantages and disadvantages. Some of the common methods are:

- **Two-phase locking (2PL)**: This method requires each transaction to acquire locks on the data items it accesses, and release them after it commits or aborts. There are two phases: the growing phase, where the transaction can only acquire locks, and the shrinking phase, where the transaction can only release locks. 2PL ensures serializability, which means that the concurrent execution of transactions is equivalent to some serial execution. However, 2PL may cause deadlock, where two or more transactions are waiting for each other to release locks, and thus cannot proceed. 2PL also reduces concurrency, as transactions may block each other from accessing data items. 2PL can be implemented in a centralized or distributed manner, depending on where the lock manager is located.

- **Timestamp ordering (TO)**: This method assigns a unique timestamp to each transaction, and uses it to order the transactions. Each data item has two timestamps: the read timestamp (RTS), which records the timestamp of the last transaction that read the item, and the write timestamp (WTS), which records the timestamp of the last transaction that wrote the item. A transaction can read or write a data item only if its timestamp is compatible with the RTS and WTS of the item, otherwise it is aborted and restarted with a new timestamp. TO ensures serializability, as transactions are executed in the order of their timestamps. However, TO may cause cascading aborts, where one aborted transaction causes other transactions to abort, and thus waste resources. TO also requires synchronization of clocks, which may be difficult in a distributed system. TO can be implemented in a centralized or distributed manner, depending on where the timestamp manager is located.

- **Multi-version concurrency control (MVCC)**: This method allows each transaction to access a snapshot of the data, which is a consistent version of the data at some point in time. Each data item has multiple versions, each with a timestamp and a value. A transaction can read the latest version of a data item that is older than or equal to its timestamp, and can write a new version of a data item with its timestamp and value. MVCC ensures serializability, as transactions are executed in the order of their timestamps. MVCC also avoids cascading aborts, as transactions do not overwrite each other's versions. However, MVCC requires more storage space, as multiple versions of data items are maintained. MVCC also requires garbage collection, which is the process of deleting obsolete versions of data items. MVCC can be implemented in a centralized or distributed manner, depending on where the version manager is located.

- **Validation concurrency control (VCC)**: This method divides the execution of a transaction into three phases: the read phase, where the transaction reads the data items it needs, the validation phase, where the transaction checks if it can commit without violating serializability, and the write phase, where the transaction writes the data items it modified. A transaction can validate only if it does not conflict with any other committed or validating transaction, otherwise it is aborted and restarted. VCC ensures serializability, as transactions are validated in the order of their timestamps. VCC also avoids cascading aborts, as transactions do not write until they are validated. However, VCC may cause unnecessary aborts, as transactions may conflict with each other even if they do not access the same data items. VCC also requires more processing time, as transactions have to validate before they can write. VCC can be implemented in a centralized or distributed manner, depending on where the validation manager is located.



## Unit 9 - Distributed Transactions

- A distributed transaction is a type of transaction that involves two or more network hosts, usually providing transactional resources, such as databases, message queues, file systems, etc.
- A distributed transaction is coordinated by a transaction manager, which is responsible for creating and managing a global transaction that encompasses all the operations against the transactional resources.
- A distributed transaction ensures the ACID (Atomicity, Consistency, Isolation, Durability) properties across multiple hosts, meaning that either all the operations succeed or none of them, the data remains consistent, the concurrent transactions do not interfere with each other, and the effects of the transaction are permanent.
- A distributed transaction faces several challenges, such as network failures, host failures, concurrency control, deadlock detection, and recovery mechanisms.
- A distributed transaction can use different protocols to achieve coordination and consensus, such as two-phase commit, three-phase commit, Paxos, Raft, etc.



### Flat and Nested Distributed Transactions

- A **distributed transaction** is a flat or nested transaction that accesses objects managed by multiple servers .
- A **flat transaction** has a single begin point and a single end point (commit or abort). It is usually simple and short-lived .
- A **nested transaction** has a hierarchical structure of subtransactions, each with its own begin and end points. It is usually complex and long-lived .
- A **flat distributed transaction** can be coordinated by a single transaction manager that communicates with all the servers involved in the transaction.
- A **nested distributed transaction** can be coordinated by a hierarchy of transaction managers, each responsible for a subtransaction and its children.
- The advantages of nested distributed transactions over flat distributed transactions are:
  - They allow partial commits, which means that some subtransactions can commit even if others abort, thus reducing the amount of work to be redone.
  - They allow concurrency control and recovery to be done locally, which means that each subtransaction can use its own locking and logging mechanisms, thus reducing the overhead and complexity of global coordination.
  - They allow better fault tolerance, which means that each subtransaction can handle its own failures and restarts, thus reducing the impact of failures on other subtransactions.



### Atomic Commit Protocols for Distributed Transactions

- A distributed transaction is a transaction that involves multiple servers or nodes in a distributed system.
- An atomic commit protocol is a protocol that ensures that a distributed transaction is either committed or rolled back in its entirety, even if the system fails or some of the nodes fail or crash.
- Ensuring atomic commit is important for maintaining the consistency and integrity of the data in a distributed system.
- There are different types of atomic commit protocols, such as two-phase commit (2PC), three-phase commit (3PC), parallel commit, and failure-aware atomic commit (FLAC).
- Two-phase commit (2PC) is the most widely used atomic commit protocol. It consists of two phases: a prepare phase and a commit phase. In the prepare phase, the coordinator node asks all the participant nodes to vote on whether they are ready to commit or not. In the commit phase, the coordinator node decides whether to commit or abort the transaction based on the votes, and informs all the participant nodes of the decision.
- Three-phase commit (3PC) is an extension of 2PC that adds a pre-commit phase between the prepare and commit phases. In the pre-commit phase, the coordinator node informs all the participant nodes that they have agreed to commit, and waits for their acknowledgments. In the commit phase, the coordinator node confirms the commit decision to all the participant nodes. 3PC can avoid blocking in some failure scenarios that 2PC cannot handle, but it introduces more communication overhead and latency.
- Parallel commit is a new atomic commit protocol that reduces the latency of transactions down to only a single round-trip of distributed consensus. It does not use a coordinator node, but instead relies on a distributed consensus protocol (such as Raft or Paxos) to agree on a commit timestamp for each transaction. Each participant node writes its transaction data with the commit timestamp, and then checks whether all the other participant nodes have done the same. If yes, the transaction is committed; otherwise, it is rolled back.
- Failure-aware atomic commit (FLAC) is a practical atomic commit protocol that leverages the failure detection information from the underlying distributed consensus protocol to optimize the commit decision process. It can achieve the same latency as parallel commit in the common case, and gracefully degrade to 2PC or 3PC in the rare case of failures. It can also handle network partitions and heterogeneous failures without blocking or compromising consistency.



### Concurrency control in distributed transactions

- Concurrency control is the process of ensuring that multiple transactions can access and modify shared data in a consistent and correct manner, without violating the ACID properties of the transactions.
- Distributed transactions are transactions that span multiple data servers in a distributed database system, where each server hosts a subset of the data and communicates with other servers via a network.
- Distributed concurrency control provides a mechanism to synchronize distributed transactions in such a way that the ACID properties are not violated by their interleaved execution.
- There are different types of distributed concurrency control algorithms, such as locking-based, timestamp-based, optimistic, and consensus-based algorithms.
- Locking-based algorithms use locks to prevent concurrent transactions from accessing the same data item at the same time. A transaction must acquire a lock on a data item before reading or writing it, and release the lock after finishing its operation. Locks can be exclusive (for write operations) or shared (for read operations). Locking-based algorithms can be centralized, decentralized, or hierarchical, depending on how the locks are managed and granted.
- Timestamp-based algorithms assign a unique timestamp to each transaction, and use the timestamps to order the transactions and resolve conflicts. A transaction can read or write a data item only if its timestamp is compatible with the read and write timestamps of the data item, which record the latest transactions that have accessed the data item. Timestamp-based algorithms can be basic, Thomas's write rule, or multiversion, depending on how the conflicts are handled and how the versions of the data items are maintained.
- Optimistic algorithms assume that conflicts are rare and allow transactions to execute without any synchronization. However, before committing, each transaction must validate its read and write sets against the global state of the data, and abort and restart if any conflict is detected. Optimistic algorithms can be based on validation numbers, certification, or snapshot isolation, depending on how the validation is performed and how the global state is captured.
- Consensus-based algorithms use a distributed agreement protocol, such as two-phase commit (2PC) or three-phase commit (3PC), to coordinate the commit or abort decision of the participating servers in a distributed transaction. Each server votes to commit or abort based on its local outcome, and the transaction coordinator collects the votes and broadcasts the final decision. Consensus-based algorithms can be blocking or non-blocking, depending on how they handle failures and timeouts.




### Distributed Deadlocks

- A distributed deadlock is a situation where a set of processes in a distributed system are waiting for each other to release resources or messages, and none of them can proceed.
- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems .
- Distributed deadlocks are harder to detect, avoid, and prevent than deadlocks in centralized systems, because there is no single authority that can oversee resource allocation and dependency graphs.
- There are three main approaches to handle distributed deadlocks :
  - Prevention: This approach tries to ensure that deadlocks never occur by imposing some constraints on resource allocation, such as ordering, preemption, or timeouts.
  - Avoidance: This approach tries to avoid deadlocks by dynamically analyzing the resource requests and granting them only if they do not lead to a potential deadlock, such as using the Banker's algorithm or timestamps.
  - Detection and recovery: This approach tries to detect deadlocks after they occur and then recover from them by aborting or restarting some processes, or by breaking cycles in the dependency graph.
- There are two main techniques to detect distributed deadlocks :
  - Global wait-for graph: This technique involves constructing a global graph of processes and resources from local graphs at each node, and then finding cycles in the global graph. This technique requires a centralized or distributed coordinator that can collect and analyze the local graphs.
  - Edge chasing: This technique involves sending probe messages along the edges of the local wait-for graphs, and detecting cycles when a probe returns to its originator. This technique does not require a coordinator, but it may generate a lot of messages and false positives.



### Transaction recovery for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A distributed transaction is a transaction that spans multiple sites or nodes in a distributed system.
- A distributed transaction system must ensure the ACID properties of transactions: atomicity, consistency, isolation, and durability.
- Atomicity means that either all the operations of a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction does not interfere with other concurrent transactions.
- Durability means that the effects of a committed transaction are permanent and survive failures.
- Transaction recovery is the process of restoring the database to a consistent state after a failure or an abort of a transaction.
- Transaction recovery is essential for maintaining the ACID properties of transactions in a distributed system.
- Transaction recovery in a distributed system is more complex than in a centralized system because of the following challenges:
  - Communication failures: A site may not be able to communicate with other sites due to network problems or partitioning.
  - Site failures: A site may crash or become unavailable due to hardware or software faults.
  - Distributed concurrency control: A site may have to coordinate with other sites to ensure the isolation of transactions.
  - Distributed commit protocol: A site may have to participate in a protocol to ensure the atomicity of transactions.
- Transaction recovery in a distributed system can be based on different techniques, such as:
  - Logging and checkpointing: A site records the operations of transactions in a log file and periodically saves the state of the database in a checkpoint. In case of a failure, a site can use the log and the checkpoint to undo or redo the operations of transactions.
  - Shadow versions: A site maintains multiple versions of the database and updates only the latest version. In case of a failure, a site can switch to a previous version of the database that is consistent.
  - Compensation: A site executes compensating transactions to undo the effects of aborted transactions. A compensating transaction is a transaction that reverses the actions of another transaction without violating the consistency of the database.



## Unit 10 - Replication

- Replication is a biological process of duplicating or producing an exact copy, such as a polynucleotide strand (DNA) .
- Replication is essential for the transmission of genetic information from one generation to the next and for the maintenance of genetic stability within a population .
- Replication relies on the fact that each strand of DNA can serve as a template for duplication, following the complementary base pairing rules .
- Replication can be divided into three main stages: initiation, elongation, and termination .
- Initiation is the stage where the DNA helix is unwound and the replication machinery is assembled at the origin of replication .
- Elongation is the stage where the DNA polymerase enzyme synthesizes new DNA strands by adding nucleotides to the 3' end of the growing chain, following the template strand .
- Termination is the stage where the replication process is completed and the newly synthesized DNA strands are separated and rewound into a double helix .
- Replication can be either semiconservative or conservative. Semiconservative replication means that each new DNA molecule consists of one old and one new strand, while conservative replication means that the original DNA molecule is preserved and a new one is formed .
- Replication can also be either bidirectional or unidirectional. Bidirectional replication means that the replication fork moves in both directions from the origin of replication, while unidirectional replication means that the replication fork moves in only one direction .
- Replication can vary between different types of organisms and cells. For example, bacteria usually have a single circular chromosome with a single origin of replication, while eukaryotes usually have multiple linear chromosomes with multiple origins of replication .



### System model and group communication for replication in distributed systems

- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by passing messages.
- Replication is a technique to improve the availability, reliability, and performance of a distributed system by creating and maintaining multiple copies of data or services across different processes or nodes.
- A system model is a set of assumptions and properties that describe the behavior and characteristics of a distributed system, such as the communication model, the failure model, the timing model, and the security model.
- A group is a subset of processes in a distributed system that share some common interest or functionality, such as a replicated service or a multicast group.
- Group communication is a mechanism to send and receive messages among the members of a group in a distributed system, such as broadcast, multicast, or anycast.
- Group communication can be classified into two types: reliable and unreliable.
  - Reliable group communication guarantees that a message sent by a group member is delivered to all other group members in the same order, regardless of failures or network delays.
  - Unreliable group communication does not provide any delivery or ordering guarantees, and may lose, duplicate, or reorder messages.
- Group communication can also be classified into two modes: atomic and non-atomic.
  - Atomic group communication ensures that a message is delivered to all group members or none of them, and that all group members agree on the same view of the group membership and the message order.
  - Non-atomic group communication does not provide any atomicity or agreement guarantees, and may deliver a message to a subset of group members or to different views of the group.
- Group communication is essential for replication in distributed systems, as it enables the coordination and synchronization of the replicas, the dissemination of updates and queries, and the detection and recovery of failures.
- Group communication can be implemented using various protocols and algorithms, such as IP multicast, gossip, Paxos, Raft, or ZooKeeper.



### Fault-Tolerant Services for the Notes of the Unit 10 - Replication in the Subject of Distributed System

- Fault-tolerance is the ability of a system to continue functioning correctly despite the presence of failures in some of its components.
- Replication is a technique for achieving fault-tolerance by creating and maintaining multiple copies of the same service or data across different nodes in a distributed system.
- Replication can improve the availability, performance, and reliability of a service or data, but also introduces challenges such as consistency, coordination, and recovery.
- The replicated state machine approach is a general method for implementing a fault-tolerant service by replicating servers and coordinating client interactions with server replicas. This approach was proposed by Lamport and further elaborated by Schneider .
- The replicated state machine approach requires that the service be deterministic, that is, the same input should always produce the same output. This ensures that all replicas can reach the same state by executing the same sequence of requests.
- The replicated state machine approach also requires a consensus protocol to ensure that all replicas agree on the order of requests to execute. A consensus protocol is a distributed algorithm that allows a set of nodes to reach agreement on a value, even if some nodes are faulty or malicious.
- There are two main classes of replication techniques: primary-backup replication and active replication. In primary-backup replication, one replica is designated as the primary and the others are backups. The primary receives and executes all requests from clients, and sends updates to the backups. The backups only execute requests when the primary fails. In active replication, all replicas receive and execute the same requests from clients, and use a consensus protocol to agree on the order of execution. The active replication approach can tolerate more faults than the primary-backup approach, but also incurs more overhead in terms of communication and computation.
- Fused state machines are an alternative method for fault-tolerance that combines ideas from replication and coding theory. Fused state machines use a combination of coding theory and replication to ensure efficiency as well as savings in storage and messages during normal operations. Fused state machines may incur higher overhead during recovery from crash or Byzantine faults, but that may be acceptable if the probability of fault is low. Fused state machines require fewer replicas than pure replication based schemes to tolerate the same number of faults.



### Highly Available Services for the Notes of the Unit 10 - Replication in the Subject of Distributed System

- Replication is the process of creating and maintaining multiple copies of data or services across different locations in a distributed system.
- Replication can improve the availability, reliability, performance, and scalability of distributed systems by reducing the impact of failures, network latency, and load imbalance.
- Replication can also enable fault tolerance, disaster recovery, and data consistency in distributed systems.
- Replication can be classified into two types: eager replication and lazy replication.
  - Eager replication ensures that all copies of data or services are updated as soon as a change occurs, using synchronous or semi-synchronous communication protocols. Eager replication provides strong consistency, but may incur high overhead and delay, and may not tolerate network partitions or failures well.
  - Lazy replication allows some copies of data or services to be updated later than others, using asynchronous communication protocols. Lazy replication provides weak or eventual consistency, but may reduce overhead and delay, and may tolerate network partitions or failures better.
- Replication can be implemented at different levels of abstraction, such as data replication, service replication, or process replication.
  - Data replication involves creating and maintaining multiple copies of data items, such as files, records, or objects, across different nodes or servers in a distributed system. Data replication can be used to improve the availability and performance of distributed databases, file systems, or object stores.
  - Service replication involves creating and maintaining multiple copies of services, such as web servers, application servers, or microservices, across different nodes or servers in a distributed system. Service replication can be used to improve the availability and performance of distributed applications, web services, or cloud services.
  - Process replication involves creating and maintaining multiple copies of processes, such as threads, tasks, or actors, across different nodes or servers in a distributed system. Process replication can be used to improve the availability and performance of distributed computations, parallel programs, or distributed algorithms.
- Replication can be managed by different techniques, such as primary-backup, quorum, or gossip.
  - Primary-backup technique involves designating one copy of data or service as the primary, and the other copies as backups. The primary is responsible for processing requests and updating backups, while the backups are responsible for taking over the primary role in case of failure. The primary-backup technique can provide high availability and strong consistency, but may introduce a single point of failure or contention, and may not scale well with the number of replicas or requests.
  - Quorum technique involves requiring a minimum number of copies of data or service to agree on a request or an update, using a voting or consensus protocol. The quorum technique can provide high availability and tunable consistency, but may incur high communication and coordination costs, and may not tolerate network partitions or failures well.
  - Gossip technique involves disseminating requests or updates to copies of data or service using a probabilistic or epidemic protocol. The gossip technique can provide high availability and eventual consistency, but may introduce uncertainty and inconsistency, and may not guarantee delivery or order of messages.



### Transactions with replicated data

- Transactions are a sequence of operations that are executed atomically, consistently, isolatedly, and durably (ACID properties) on a database system.
- Replication is the process of copying and maintaining data in multiple locations to improve availability, performance, and fault tolerance of a distributed system.
- Transactions with replicated data involve executing operations on multiple copies of the same data item, while ensuring that the copies remain consistent and synchronized with each other.
- There are different types and schemes of replication, such as:
  - Synchronous vs. asynchronous replication: In synchronous replication, the updates are propagated to all the replicas before the transaction commits, ensuring strong consistency but increasing latency. In asynchronous replication, the updates are propagated to the replicas after the transaction commits, reducing latency but allowing temporary inconsistency.
  - Primary vs. update-anywhere replication: In primary replication, there is a designated primary copy of each data item that receives all the updates, and the other copies are secondary replicas that only receive updates from the primary. In update-anywhere replication, any copy of a data item can be updated, and the updates are propagated to the other copies.
  - Eager vs. lazy replication: In eager replication, the updates are propagated to all the replicas as soon as they occur, ensuring strong consistency but increasing communication overhead. In lazy replication, the updates are propagated to the replicas periodically or on demand, reducing communication overhead but allowing temporary inconsistency.
- Transactions with replicated data face several challenges, such as:
  - Concurrency control: How to coordinate the concurrent execution of transactions on replicated data without violating the ACID properties or the consistency of the replicas.
  - Recovery: How to recover from failures or aborts of transactions on replicated data without losing or corrupting the data or violating the ACID properties or the consistency of the replicas.
  - Consensus: How to reach agreement among the replicas on the outcome of a transaction or the state of a data item, especially in the presence of failures or network partitions.
- There are different techniques and protocols to address these challenges, such as:
  - Two-phase commit (2PC): A protocol that ensures atomicity of transactions on replicated data by using a coordinator node that communicates with all the participant nodes and decides whether to commit or abort the transaction based on their votes.
  - Quorum-based protocols: Protocols that ensure consistency of transactions on replicated data by requiring a minimum number of replicas (a quorum) to participate in the execution and validation of each operation, and resolving conflicts based on timestamps or version numbers.
  - Paxos: A protocol that ensures consensus of transactions on replicated data by using a leader node that proposes values to the other nodes (acceptors) and decides on a value based on their responses, and using a majority voting mechanism to elect a new leader in case of failures.

