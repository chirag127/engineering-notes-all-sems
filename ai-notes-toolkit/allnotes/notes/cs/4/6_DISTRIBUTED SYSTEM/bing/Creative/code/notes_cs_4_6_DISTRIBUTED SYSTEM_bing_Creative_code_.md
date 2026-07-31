

## Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- The main characteristics of distributed systems are:
  - Concurrency: Multiple components can execute simultaneously and interact with each other.
  - No global clock: There is no shared physical clock among the components, so synchronization and coordination are challenging.
  - Independent failures: Each component can fail independently, without affecting the rest of the system, unless there is a dependency.
  - Heterogeneity: The components can have different hardware, software, network, data, and protocols.
  - Scalability: The system can grow in size and complexity without losing its functionality and performance.
  - Transparency: The system should hide its complexity and heterogeneity from the users and provide a consistent and uniform interface.
- The main advantages of distributed systems are:
  - Resource sharing: The system can share physical and logical resources, such as files, printers, databases, services, etc.
  - Fault tolerance: The system can tolerate and recover from failures of some components, by using replication, redundancy, or backup mechanisms.
  - Performance: The system can achieve higher throughput and lower latency by distributing the workload among multiple components and using parallelism.
  - Availability: The system can provide continuous and reliable service to the users, by using load balancing, caching, or replication techniques.
  - Modularity: The system can be composed of smaller and simpler components, which can be developed, tested, and maintained independently.
- The main challenges of distributed systems are:
  - Coordination: The system needs to coordinate the actions and states of the components, by using algorithms, protocols, or middleware.
  - Consistency: The system needs to ensure that the components have a consistent view of the data and the system state, by using synchronization, replication, or consensus techniques.
  - Security: The system needs to protect the data and the communication from unauthorized access, modification, or disclosure, by using encryption, authentication, or authorization techniques.
  - Fault detection: The system needs to detect and identify the failures of the components, by using heartbeat, timeout, or gossip protocols.
  - Fault recovery: The system needs to restore the normal operation of the system after a failure, by using checkpoint, rollback, or recovery protocols.



Hello, I am Sydney, your AI assistant. I can help you with writing notes on various topics. Here is the content I have generated for the topic of Introduction for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM.

```markdown
# Introduction

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- A distributed system has the following characteristics:
  - Concurrency: The components of the system can execute concurrently, without interfering with each other.
  - No global clock: The components of the system do not share a common notion of time, and may have different local clocks.
  - Independent failures: The components of the system can fail independently, without affecting the whole system.
  - Heterogeneity: The components of the system can have different hardware, software, network, and data formats.
- A distributed system has the following challenges:
  - Transparency: The system should hide the complexity and diversity of the components from the users and provide a uniform interface.
  - Scalability: The system should be able to accommodate a growing number of components and users without degrading the performance or functionality.
  - Reliability: The system should be able to tolerate and recover from failures of the components and provide consistent and correct results.
  - Security: The system should be able to protect the data and resources from unauthorized access and malicious attacks.
- A distributed system has the following benefits:
  - Resource sharing: The system can enable the users to access and share the resources (such as files, printers, databases, etc.) that are distributed across the network.
  - Load balancing: The system can distribute the workload among the components and improve the efficiency and throughput of the system.
  - Fault tolerance: The system can continue to operate even if some of the components fail, by using replication and redundancy techniques.
  - Parallelism: The system can exploit the parallelism of the components and perform tasks faster and more effectively.
  - Distributed applications: The system can support various types of applications that require distributed processing and communication, such as web services, cloud computing, distributed databases, etc.
```



### Examples of distributed systems

A distributed system is a collection of independent computers that communicate and coordinate their actions by passing messages. The computers in a distributed system may be physically close or geographically dispersed, and they may be connected by a network or a bus. The main advantages of distributed systems are scalability, fault tolerance, resource sharing, and performance.

Some examples of distributed systems are:

- **Telecommunication networks**: Telephone networks are an early example of a peer-to-peer network, where each node can initiate or receive calls. Cellular and telephone networks are forms and examples of distributed networks. They use protocols such as TCP/IP, HTTP, and SMTP to exchange data and messages.  
- **Real-time systems**: Many industries use real-time systems distributed in various areas, locally and globally. For example, air traffic control systems, power grid systems, industrial control systems, and online gaming systems are all examples of real-time distributed systems. They require high reliability, availability, and responsiveness. They use protocols such as UDP, RTP, and MQTT to ensure timely and accurate delivery of data.  
- **Distributed database systems**: A distributed database has locations across multiple servers, physical locations, or both. The data is replicated or partitioned among the nodes, and the nodes coordinate their transactions using protocols such as two-phase commit, distributed locking, and consensus algorithms. Examples of distributed database systems are Google's Bigtable, Amazon's DynamoDB, and MongoDB.  
- **Distributed computing platforms**: A distributed computing platform is a system that allows multiple computers to work together on a common task, such as processing large data sets, performing complex calculations, or rendering graphics. Examples of distributed computing platforms are MapReduce, Spark, Hadoop, and BOINC. They use protocols such as RPC, RMI, and MPI to distribute the work and communicate the results.  
- **Content delivery networks**: A content delivery network (CDN) is a system that distributes web content to users based on their geographic location, network conditions, and content type. A CDN consists of a network of servers that cache and deliver web pages, images, videos, and other static or dynamic content. Examples of CDNs are Akamai, Cloudflare, and Amazon CloudFront. They use protocols such as DNS, HTTP, and HTTPS to route and serve the content.



Hello, I am Sydney, your AI assistant. I can help you with your study material for the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM. Here are some notes on the topic:

### Resource sharing

- Resource sharing is one of the main goals and challenges of distributed systems.
- Resource sharing means that different processes or users can access and use the same resources, such as files, printers, sensors, databases, etc., in a distributed system.
- Resource sharing can improve the performance, reliability, scalability, and availability of distributed systems, as well as reduce the cost and complexity of managing them.
- Resource sharing can also enable collaboration, coordination, and communication among different processes or users in a distributed system.
- Resource sharing can be achieved by different methods, such as:

  - Remote access: A process or user can access a resource that is located on a different machine or network, using a communication protocol and an interface. For example, a web browser can access a web page that is stored on a web server, using HTTP and HTML.
  - Replication: A resource can be copied or duplicated on multiple machines or networks, so that each copy can be accessed locally or remotely. For example, a file can be replicated on different servers, using a distributed file system.
  - Migration: A resource can be moved or transferred from one machine or network to another, either permanently or temporarily. For example, a process can migrate from one host to another, using a mobile agent system.
  - Distribution: A resource can be partitioned or split into multiple parts or components, each of which can be located on a different machine or network. For example, a database can be distributed across different servers, using a distributed database system.



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
- These challenges require careful design and implementation of distributed algorithms, protocols, and architectures that can balance the trade-offs and requirements of the system  .
- Some of the techniques and solutions that are used to address these challenges are   :
  - Load balancing: The distribution of work among the components of the system to optimize the resource utilization and performance.
  - Replication: The creation of multiple copies of data or services to enhance the availability and reliability of the system.
  - Caching: The storage of frequently accessed data or results in a local or intermediate component to reduce the network traffic and latency.
  - Encryption: The transformation of data into a secret form that can only be decrypted by authorized parties to ensure the confidentiality and integrity of the data.
  - Authentication: The verification of the identity and credentials of the parties involved in the communication to prevent impersonation and unauthorized access.
  - Consensus: The agreement among the components of the system on a common value or decision to ensure the consistency and coordination of the system.
  - Middleware: The software layer that provides a uniform and transparent interface for the communication and integration of heterogeneous and distributed components.



# Architectural models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Architectural models are a type of system model that deal with the organization of components across the network and their interrelationship.
- Architectural models describe the placement of parts in a distributed system and the relationship between them.
- Architectural models can be classified into different styles, such as:
  - Client-server architecture: A style where one or more servers provide services to multiple clients that request them. The servers and clients are loosely coupled and communicate through a well-defined protocol. This style forms the base for multi-tier architectures.
  - Broker architecture: A style where a broker component acts as an intermediary between clients and servers, hiding the details of communication and location from them. The broker can provide services such as naming, binding, routing, and security. An example of this style is CORBA (Common Object Request Broker Architecture).
  - Service-oriented architecture (SOA): A style where the system consists of independent and interoperable services that communicate through standardized interfaces and protocols. The services can be composed and orchestrated to achieve complex functionality. An example of this style is web services.
  - Peer-to-peer architecture: A style where the system consists of nodes that have equal roles and responsibilities. The nodes can act as both clients and servers, and can cooperate and share resources without a central authority. An example of this style is BitTorrent.
  - Distributed object architecture: A style where the system consists of distributed objects that encapsulate data and behavior, and communicate through remote method invocation. The objects can be transparently accessed and manipulated by other objects, regardless of their location. An example of this style is Java RMI (Remote Method Invocation).
  - Distributed component architecture: A style where the system consists of distributed components that provide and require interfaces, and communicate through events and messages. The components can be dynamically deployed and configured, and can support multiple languages and platforms. An example of this style is EJB (Enterprise JavaBeans).
- Architectural models can have different properties and trade-offs, such as:
  - Scalability: The ability of the system to handle increasing workload and resources without degrading performance or functionality. Scalability can be achieved by using techniques such as replication, caching, load balancing, and partitioning.
  - Availability: The ability of the system to provide continuous and correct service despite failures or faults. Availability can be achieved by using techniques such as redundancy, fault tolerance, recovery, and monitoring.
  - Consistency: The degree to which the system maintains a coherent and agreed-upon state of data and operations. Consistency can be affected by factors such as concurrency, replication, and network delays. Consistency can be ensured by using techniques such as locking, transactions, and consensus.
  - Transparency: The degree to which the system hides the complexity and heterogeneity of its components and interactions from the users and developers. Transparency can be achieved by using techniques such as naming, location, migration, and replication.
  - Security: The degree to which the system protects its data and services from unauthorized access, modification, or disclosure. Security can be achieved by using techniques such as encryption, authentication, authorization, and auditing.



### Fundamental Models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Fundamental models are descriptions of properties that are present in all distributed architectures  .
- They help us to understand the characteristics, challenges and trade-offs of designing and implementing distributed systems.
- There are three main types of fundamental models: interaction models, failure models and security models  .

#### Interaction Models
- Interaction models deal with the issues of how processes communicate and coordinate with each other in a distributed system  .
- They include aspects such as performance, timing, ordering, synchronization and consistency of events and messages  .
- Some examples of interaction models are:
  - Synchronous vs. asynchronous communication: whether the sender and receiver of a message have to wait for each other or not  .
  - Remote procedure call (RPC): a method of invoking a function or procedure on a remote machine as if it were local  .
  - Publish-subscribe: a pattern where publishers send messages to a broker, and subscribers receive messages that match their interests  .
  - Peer-to-peer: a model where each node can act as both a client and a server, and communicate directly with other nodes  .

#### Failure Models
- Failure models specify the types of faults that can occur in a distributed system, and how they affect the processes and communication channels  .
- They help us to design fault-tolerant and reliable distributed systems that can cope with failures and recover from them  .
- Some examples of failure models are:
  - Crash failure: a process stops executing and does not resume  .
  - Omission failure: a process fails to send or receive a message  .
  - Timing failure: a process does not meet the timing constraints of the system  .
  - Byzantine failure: a process behaves arbitrarily or maliciously, sending incorrect or conflicting messages  .

#### Security Models
- Security models describe the threats and attacks that can compromise the confidentiality, integrity and availability of a distributed system, and the mechanisms to prevent or mitigate them  .
- They help us to design secure and trustworthy distributed systems that can protect the data and resources from unauthorized access and manipulation  .
- Some examples of security models are:
  - Cryptography: the use of mathematical techniques to encrypt and decrypt data, and to verify the identity and authenticity of the sender and receiver  .
  - Authentication: the process of verifying the identity of a user or a process before granting access to the system  .
  - Authorization: the process of determining the permissions and privileges of a user or a process to access or modify the data and resources of the system  .
  - Intrusion detection: the process of monitoring and analyzing the activities and events in the system to detect and respond to malicious or anomalous behavior  .



### Theoretical Foundation for Distributed System

A distributed system is a collection of independent processes that communicate with each other by exchanging messages over a network. The processes may be located on different machines, have different speeds, and operate under different failure modes. The main challenges of designing and implementing distributed systems are:

- How to coordinate the actions of the processes without a global clock or a shared memory.
- How to handle the uncertainty and unpredictability of the message delays and the process failures.
- How to achieve consistency, reliability, and fault-tolerance in the presence of concurrency and partial failures.

Some of the theoretical concepts and tools that help to address these challenges are:

- **Logical clocks**: A way of assigning logical timestamps to the events that occur in a distributed system, such that the timestamps reflect the causal order of the events. Logical clocks can be used to implement synchronization, ordering, and agreement protocols in distributed systems. There are different types of logical clocks, such as Lamport's scalar clocks and vector clocks.
- **Message passing systems**: A model of distributed computation that assumes that the processes communicate only by sending and receiving messages over a network. Message passing systems can be classified according to the properties of the network, such as reliability, synchrony, and topology. Message passing systems can also be characterized by the types of communication primitives they provide, such as unicast, broadcast, multicast, or group communication.
- **Consensus and related problems**: A fundamental problem in distributed systems that requires a set of processes to agree on a common value, despite the possibility of failures and asynchrony. Consensus is essential for implementing coordination, replication, and fault-tolerance mechanisms in distributed systems. Consensus is also related to other problems, such as atomic broadcast, leader election, mutual exclusion, and distributed transactions.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on the limitation of distributed system for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM.

### Limitation of Distributed System

A distributed system is a system that consists of multiple independent components that communicate with each other over a network. Distributed systems have many advantages, such as scalability, reliability, availability, and performance. However, they also face some challenges and limitations, such as:

- **Absence of a global state**: In a distributed system, there is no single point of control or coordination for the entire system. Each component has its own local state and view of the system, which may differ from other components. This makes it difficult to achieve consistency, synchronization, and agreement among the components. For example, it is hard to determine the total number of users or transactions in a distributed system, or to ensure that all components have the same version of the data.  

- **Absence of a global clock**: In a distributed system, there is no common notion of time or order of events among the components. Each component has its own local clock, which may drift or be inaccurate. This makes it difficult to measure the duration of events, to coordinate actions, and to detect causality and concurrency. For example, it is hard to determine if an event A happened before or after an event B in a distributed system, or to ensure that all components execute a task at the same time. 

- **Network issues**: In a distributed system, the communication between the components depends on the underlying network, which may be unreliable, unpredictable, or insecure. The network may experience delays, failures, congestion, or attacks, which may affect the availability, performance, and correctness of the system. For example, a message sent by a component may be lost, duplicated, corrupted, or delayed by the network, or a component may be isolated from the rest of the system due to a network partition.  

- **Security issues**: In a distributed system, the components may not trust each other or the network, as they may be exposed to malicious or unauthorized actions. The system may face threats such as eavesdropping, tampering, spoofing, denial-of-service, or intrusion, which may compromise the confidentiality, integrity, or availability of the system. For example, an attacker may intercept, modify, or forge a message sent by a component, or may launch a distributed denial-of-service attack to overwhelm the system.  

These limitations of distributed system have an impact on both the design and the implementation of the system, and require the use of various techniques and algorithms to overcome them, such as consensus, replication, fault tolerance, distributed transactions, distributed locking, cryptography, authentication, and authorization.   




### Absence of Global Clock

- A global clock is a system-wide clock that is equally accessible to all processes in a distributed system and provides a common notion of time.
- A global clock is useful for determining the order of events and the state of the system across different processes.
- However, a global clock is hard to realize in distributed systems due to two inherent limitations: lack of shared memory and unpredictable message delays .
- Lack of shared memory means that processes in a distributed system do not have access to a common storage that can store and update the global clock value.
- Unpredictable message delays mean that the communication channel between processes is unreliable and the transmission time of messages is variable and unknown.
- Therefore, processes in a distributed system may have different and inaccurate views of the global clock value, and the notion of common time does not exist.
- As a result, it is not always possible to determine the order in which two events on different processes were executed, or to obtain an up-to-date and consistent state of the entire system.
- The absence of a global clock poses challenges for designing and implementing distributed algorithms and protocols that require synchronization, coordination, and consistency among processes.



### Shared Memory

Shared memory is a programming model for distributed systems that allows multiple processes to access a common logical address space, as if they were running on a single machine. Shared memory can simplify the communication and synchronization among processes, and enable the implementation of parallel algorithms and data structures.

There are two types of shared memory models: physical and virtual.

- Physical shared memory: The processes share the same physical memory, such as in a multiprocessor system. The hardware ensures the consistency and coherence of the shared data, and the operating system manages the allocation and protection of the memory regions.
- Virtual shared memory: The processes do not share the same physical memory, but rather a virtual memory that is mapped to their local memories, such as in a distributed system. The software ensures the consistency and coherence of the shared data, and the network provides the communication and transfer of the memory pages.

Distributed shared memory (DSM) is a form of virtual shared memory that implements the shared memory model on a distributed system that has no physically shared memory. DSM can be achieved via software as well as hardware. Software examples include middleware, libraries, and compilers that provide the abstraction of a shared memory. Hardware examples include cache coherence circuits and network interface controllers that support the transfer and synchronization of the memory pages.

DSM has some advantages over other communication models, such as message passing and remote procedure call. Some of these advantages are:

- Transparency: The processes do not need to know the location and identity of the other processes that share the memory, nor the details of the network and the communication protocols. The DSM system handles the distribution and replication of the memory pages, and the resolution of the references and the conflicts.
- Portability: The processes can run on different platforms and architectures, as long as they support the DSM system. The DSM system can also hide the heterogeneity and the failures of the underlying network and the nodes.
- Scalability: The processes can dynamically join and leave the shared memory, and the DSM system can adjust the allocation and the consistency of the memory pages accordingly. The DSM system can also exploit the locality and the concurrency of the memory accesses to improve the performance and the efficiency of the system.

However, DSM also has some challenges and limitations, such as:

- Overhead: The processes may incur additional costs for accessing the shared memory, such as network latency, bandwidth consumption, page faults, and synchronization delays. The DSM system may also consume more resources for managing the memory pages, such as memory space, network messages, and cache entries.
- Consistency: The processes may observe different values for the same memory location, depending on the timing and the order of the memory accesses, and the consistency model adopted by the DSM system. The DSM system may also need to enforce some synchronization and coherence protocols to ensure the correctness and the validity of the shared data.
- Granularity: The processes may access the shared memory at different levels of granularity, such as bytes, words, objects, or pages. The DSM system may need to balance the trade-off between the granularity and the overhead of the memory accesses, and to adapt the granularity to the characteristics and the requirements of the applications.



### Logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A logical clock is a mechanism for capturing chronological and causal relationships in a distributed system  .
- A distributed system may have no physically synchronous global clock, so a logical clock allows global ordering on events from different processes in such systems  .
- A logical clock is not a physical device, but a software counter that is incremented according to some rules .
- A logical clock must satisfy the following property: if event A causally precedes event B, then the logical clock value of A must be less than the logical clock value of B  .
- There are different types of logical clocks, such as Lamport timestamps, vector clocks, matrix clocks, etc. Each type has its own advantages and disadvantages in terms of accuracy, complexity, and overhead  .
- Logical clocks are useful in computation analysis, distributed algorithm design, individual event tracking, and exploring computational progress .



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is some content on Lamport's logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM.

### Lamport's logical clocks

- Lamport's logical clock (or timestamp) was proposed by Leslie Lamport in the 1970s and widely used in almost all distributed systems since then.
- A Lamport logical clock is a numerical software counter value maintained in each process.
- Conceptually, this logical clock can be thought of as a clock that only has meaning in relation to messages moving between processes.
- When a process receives a message, it re-synchronizes its logical clock with that sender.
- The basic idea of Lamport's logical clock is to assign a logical timestamp to each event in a distributed system, such that if event a causally precedes event b, then the timestamp of a is less than the timestamp of b.
- The logical timestamp of an event is denoted by L(e), and the logical clock of a process is denoted by C(p).
- The algorithm for Lamport's logical clock is as follows:

  - Each process p increments C(p) between any two successive events.
  - If event a is the sending of a message m by process p, then the message m contains a timestamp T(m) = C(p).
  - Upon receiving a message m, process q sets C(q) to be greater than or equal to its present value and greater than T(m).

- The advantage of Lamport's logical clock is that it is simple and easy to implement.
- The disadvantage of Lamport's logical clock is that it does not capture the concurrent events in a distributed system, i.e., two events that are not causally related may have different logical timestamps depending on the order of message delivery.
- To overcome this limitation, vector clocks were introduced by Colin Fidge and Friedemann Mattern in the 1980s.



# Concepts in Message Passing Systems

- Message passing is a technique for invoking behavior on a computer by sending a message to a process.
- Message passing is used in distributed systems, where processes communicate by exchanging messages over a network .
- Message passing systems provide a set of message-based interprocess communication (IPC) protocols that allow processes to send and receive messages .
- Message passing systems can be classified into two types: synchronous and asynchronous .
  - Synchronous message passing systems require the sender and the receiver to be ready at the same time for communication. The sender blocks until the receiver acknowledges the message, and the receiver blocks until a message arrives .
  - Asynchronous message passing systems do not require the sender and the receiver to be ready at the same time for communication. The sender does not block after sending a message, and the receiver does not block if no message is available. Messages are stored in a buffer or a queue until they are delivered .
- Message passing systems can also be classified into two modes: direct and indirect .
  - Direct message passing systems require the sender to specify the identity of the receiver, and the receiver to specify the identity of the sender. The communication link is established explicitly between the sender and the receiver .
  - Indirect message passing systems do not require the sender or the receiver to specify the identity of the other party. The communication link is established implicitly through a shared entity, such as a mailbox, a port, or a topic. The sender and the receiver can communicate anonymously or selectively .
- Message passing systems can also be classified into two styles: point-to-point and collective.
  - Point-to-point message passing systems involve communication between two processes. The sender sends a message to a specific receiver, and the receiver receives a message from a specific sender.
  - Collective message passing systems involve communication between a group of processes. The sender sends a message to all or some of the processes in the group, and the receiver receives a message from any or all of the processes in the group. Collective message passing systems can support operations such as broadcast, scatter, gather, and reduce.
- Message passing systems can also be classified into two standards: Message Passing Interface (MPI) and Remote Procedure Call (RPC).
  - MPI is a standardized and portable message-passing system developed for distributed and parallel computing. MPI provides parallel hardware vendors with a clearly defined base set of routines that can be efficiently implemented. MPI supports both synchronous and asynchronous, direct and indirect, point-to-point and collective message passing .
  - RPC is a message-passing system that allows a process to invoke a procedure or a function on a remote process. RPC hides the details of message passing and network communication from the programmer. RPC supports both synchronous and asynchronous, direct and indirect message passing.



### Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems in the Subject of Distributed System

- Causal order is a way of ordering events in a distributed system based on their causal relationships, rather than their physical timestamps or locations.
- Causal order captures the intuitive notion of "happened before" or "influenced by" among events in a distributed system, where events can be messages, actions, or state changes.
- Causal order is important for ensuring consistency, correctness, and coordination in distributed systems, especially when dealing with concurrency, replication, and fault tolerance.
- Causal order can be defined formally using Lamport's logical clocks, which assign logical timestamps to events such that if event A causally precedes event B, then the timestamp of A is less than the timestamp of B.
- Causal order can also be defined using vector clocks, which are arrays of logical clocks that track the causal dependencies among processes in a distributed system. A vector clock of a process contains the logical timestamps of the last events it has seen from each process in the system.
- Causal order can be enforced using various protocols and algorithms, such as causal broadcast, causal multicast, causal delivery, causal memory, and causal consistency. These protocols and algorithms ensure that messages or updates are delivered or applied in a causal order, respecting the dependencies among events.
- Causal order is a weaker form of ordering than total order or sequential order, which impose a single linearization of all events in a distributed system, regardless of their causal relationships. Causal order allows more concurrency and flexibility, but also more ambiguity and complexity, in distributed systems.



# Total Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent entities that communicate by message passing and coordinate their actions to achieve a common goal.
- Events are occurrences that happen at a specific point in time and space in a distributed system.
- The order of events is important for understanding the behavior and correctness of a distributed system.
- A partial order is a binary relation that satisfies three properties: reflexivity, antisymmetry, and transitivity.
- A total order is a partial order that also satisfies the property of totality, which means that any two events are comparable.
- A distributed system is said to have partial order if we can have a partial order relationship among the events in the system .
- A distributed system is said to have total order if we can establish a causal relationship among all events in the system .
- A causal relationship between two events means that one event influences or causes the other event.
- A total order of events is useful for distributed system implementation, as it can help ensure consistency, agreement, and coordination among the entities .
- A total order of events can be achieved by using logical clocks, such as Lamport timestamps or vector clocks, that assign a unique and monotonically increasing value to each event .
- A total order of events can also be achieved by using atomic broadcast, which is a communication primitive that guarantees that all entities receive the same messages in the same order .
- A total order of events can be used to implement various distributed algorithms, such as mutual exclusion, consensus, leader election, replication, and fault tolerance  .



# Total Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent and autonomous processes that communicate and coordinate with each other by exchanging messages.
- A distributed system may exhibit concurrency, asynchrony, partial failure, and non-determinism.
- To reason about the behavior and properties of a distributed system, it is necessary to define a notion of time and order among the events that occur in the system.
- An event is anything that happens at a point in time in a process, such as sending or receiving a message, performing a computation, or changing a state.
- A partial order is a binary relation that is reflexive, antisymmetric, and transitive. A partial order can be represented by a directed acyclic graph (DAG), where the nodes are the events and the edges are the order relation.
- A total order is a partial order that is also total, meaning that any two events are comparable. A total order can be represented by a linear sequence of events, where the order relation is the precedence relation.
- A causal order is a partial order that captures the notion of potential causality among events. An event e1 is said to causally precede an event e2, denoted by e1 -> e2, if one of the following conditions holds:
  - e1 and e2 are events in the same process, and e1 occurred before e2.
  - e1 is the sending of a message m, and e2 is the receipt of the same message m.
  - There exists an event e3 such that e1 -> e3 and e3 -> e2.
- A total causal order is a total order that is consistent with the causal order, meaning that if e1 -> e2, then e1 precedes e2 in the total order. A total causal order establishes a unique linearization of all the events in the system, even those that are concurrent or independent.
- A total causal order is the strictest ordering in distributed systems, as it imposes a global synchronization among all the processes. It can be useful for implementing consistent and reliable services, such as atomic broadcast, consensus, or distributed transactions.
- A total causal order can be achieved by using a logical clock, such as a vector clock, that assigns a timestamp to each event, such that the timestamp reflects the causal order. A total causal order can then be obtained by sorting the events according to their timestamps. Alternatively, a total causal order can be achieved by using a sequencer, which is a special process that assigns a sequence number to each message, such that the sequence number reflects the total order. A total causal order can then be obtained by delivering the messages according to their sequence numbers.



# Techniques for Message Ordering in Distributed Systems

A distributed system is a collection of independent computers that communicate with each other via messages. The order in which messages are processed determines the final outcome of the actions in any distributed system. However, message ordering is not trivial, as messages may be delayed, lost, or reordered by the network. Therefore, different techniques are needed to ensure that messages are delivered and processed in a consistent and correct order.

Some of the common techniques for message ordering in distributed systems are:

- **Non-FIFO ordering**: This is the simplest and most basic technique, where messages are delivered and processed in any order, regardless of the order in which they were sent. This technique does not guarantee any consistency or correctness, and may lead to unpredictable and undesirable results. For example, if a process sends two messages m1 and m2 to another process, the receiver may process m2 before m1, which may violate the sender's intention or expectation.

- **FIFO ordering**: This technique ensures that messages sent by the same sender are delivered and processed in the same order as they were sent. This technique preserves the sender's order, but does not take into account the causal dependencies or logical relationships between messages from different senders. For example, if a process sends a message m1 to another process, and then sends a message m2 to a third process, the third process may process m2 before receiving m1, which may violate the causal order.

- **Causal ordering**: This technique ensures that messages that are causally related are delivered and processed in the same order as they were causally generated. Two messages are causally related if one message could have influenced or affected the generation of the other message, either directly or indirectly. For example, if a process sends a message m1 to another process, and then sends a message m2 to a third process, the third process should process m1 before m2, as m1 could have influenced m2. Causal ordering captures the logical dependencies and relationships between messages, and guarantees that the system behaves in a consistent and correct manner.

- **Synchronous ordering**: This technique ensures that messages are delivered and processed in the same order by all the processes in the system. This technique requires global synchronization and agreement among the processes, and guarantees that the system behaves in a deterministic and predictable manner. For example, if a process sends a message m1 to another process, and then sends a message m2 to a third process, both the processes should process m1 before m2, and in the same order as the sender. Synchronous ordering is the strongest and most strict technique, but also the most expensive and difficult to implement.

Each of these techniques has its own advantages and disadvantages, and may be suitable for different applications and scenarios. Depending on the requirements and constraints of the system, one or more of these techniques may be used to ensure message ordering in distributed systems.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of causal ordering of messages in distributed systems:

### Causal ordering of messages in distributed systems

- Causal ordering is a partial ordering of messages in a distributed computing environment that reflects the potential causal relationships between events in different processes .
- Causal ordering is based on the **happened-before** relation, denoted by `->`, which is defined as follows :
  - If event `a` and event `b` occur in the same process, and `a` occurs before `b`, then `a -> b`.
  - If event `a` is the sending of a message by one process and event `b` is the receipt of the same message by another process, then `a -> b`.
  - If `a -> b` and `b -> c`, then `a -> c`.
  - Two events `a` and `b` are **concurrent**, denoted by `||`, if neither `a -> b` nor `b -> a`.
- Causal ordering of messages requires that if the sending of message `m1` by process `p1` happened before the sending of message `m2` by process `p2`, then any process that receives both messages must deliver `m1` before `m2`  .
- Causal ordering of messages is useful for ensuring consistency and correctness of distributed applications that rely on causal dependencies, such as collaborative editing, chat systems, distributed databases, etc .
- Causal ordering of messages can be implemented by various algorithms that use different techniques, such as vector clocks, logical clocks, message acknowledgments, message buffering, etc  .



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of global state for the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM.

### Global State in Distributed Systems

- A distributed system is a collection of processes that communicate through message passing and do not share memory.
- The global state of a distributed system is the union of the local states of the processes and the channels.
- A local state of a process is the values of its variables and its program counter at a given point in time.
- A channel state is the set of messages that have been sent but not yet received by the processes.
- A global state is consistent if it reflects a possible execution of the system, i.e., it does not contain any causal anomaly.
- A causal anomaly is a situation where a process observes the effect of an event before observing its cause, such as receiving a message before it is sent.
- A consistent global state can be computed along a consistent cut, which is a partition of the system's events into past and future.
- A cut is consistent if it does not cross any message, i.e., if the send event of a message is in the past, then the receive event must also be in the past, and vice versa.
- A consistent global state can be used for various purposes, such as debugging, checkpointing, termination detection, garbage collection, etc  .
- There are different algorithms for capturing a consistent global state, such as the Chandy-Lamport algorithm, the Lai-Yang algorithm, the Mattern algorithm, etc.



# Termination Detection for Distributed Systems

Termination detection is the problem of determining if a distributed computation has finished. This is a fundamental and non-trivial problem in distributed systems, since no process has complete knowledge of the global state, and global time does not exist. Termination detection is useful for many applications, such as garbage collection, deadlock detection, load balancing, and fault tolerance.

One of the algorithms for termination detection is Huang's algorithm, proposed by Shing-Tsaan Huang in 1989. Huang's algorithm is based on the concept of a process' state in a distributed system. A process can be either active or idle at any given time. An active process may become idle at any time, but an idle process may only become active again upon receiving a computational message, which is a message that affects the local state of the process. A distributed computation terminates when all processes are idle and there are no computational messages in transit.

Huang's algorithm works as follows:

- The system has a designated process called the controller, which initiates and coordinates the termination detection.
- Each process maintains a counter, called the control message count (CMC), which records the number of control messages (messages related to termination detection) sent and received by the process.
- Each process also maintains a flag, called the active flag, which indicates whether the process is active or idle.
- The controller periodically initiates a termination detection by sending a probe message to each process, along with its own CMC and active flag.
- When a process receives a probe message, it compares its CMC and active flag with those in the probe message. If they are equal, it means that the process has not sent or received any control message since the last probe, and it sends an echo message back to the controller with its CMC and active flag. If they are not equal, it means that the process has sent or received some control messages since the last probe, and it updates its CMC and active flag in the probe message and forwards it to another process.
- The controller collects the echo messages from all processes. If all echo messages have the same CMC and active flag as the controller, and the active flag is false, it means that the system has terminated. Otherwise, the controller initiates another termination detection after some time.

The following diagram illustrates an example of Huang's algorithm:

Huang's algorithm example

The advantages of Huang's algorithm are:

- It is efficient, as it only requires O(n) messages per termination detection, where n is the number of processes.
- It is scalable, as it does not depend on the topology of the system.
- It is robust, as it can tolerate message losses and process failures.

The disadvantages of Huang's algorithm are:

- It requires a designated controller, which may become a bottleneck or a single point of failure.
- It requires each process to maintain a CMC and an active flag, which may incur some overhead.
- It may cause false positives, as it may detect termination before all computational messages are delivered.



# Unit 2 - Distributed Mutual Exclusion

- Distributed mutual exclusion is a problem of ensuring that only one process in a distributed system can access a shared resource or data at a time  .
- Distributed mutual exclusion is necessary to prevent race conditions, which are situations where the outcome of a computation depends on the order or timing of concurrent processes.
- Distributed mutual exclusion cannot be implemented using shared variables or local kernels, as they are not available or reliable in a distributed system. Message passing is the only means for implementing distributed mutual exclusion .
- There are three basic approaches for implementing distributed mutual exclusion:
  - Token-based algorithms: A process can enter the critical section only if it possesses a unique token that is circulated among the processes in a logical ring or a tree.
  - Permission-based algorithms: A process can enter the critical section only if it obtains permission from all or a subset of the processes in the system.
  - Quorum-based algorithms: A process can enter the critical section only if it obtains permission from a majority or a weighted majority of the processes in the system.
- The performance of distributed mutual exclusion algorithms can be measured by the following criteria:
  - Message complexity: The number of messages exchanged per critical section entry.
  - Synchronization delay: The time elapsed between a process requesting and entering the critical section.
  - System throughput: The number of times the critical section is executed per unit time.
  - Fault tolerance: The ability of the algorithm to handle process or link failures.



### Classification of distributed mutual exclusion

Distributed mutual exclusion is a problem of ensuring that only one process in a distributed system can access a shared resource or data at a time. It is a fundamental requirement for achieving consistency, coordination and synchronization among the processes.

There are three basic approaches for implementing distributed mutual exclusion algorithms:

- Token-based approach: A unique token is shared among the sites. A site is allowed to enter its critical section if it possesses the token. Mutual exclusion is ensured because the token is unique. Examples of token-based algorithms are Suzuki-Kasami's algorithm, Raymond's algorithm and Maekawa's algorithm.
- Non-token-based approach: A site requests permission from other sites before entering its critical section. A site is allowed to enter its critical section if it receives permission from all or a majority of other sites. Mutual exclusion is ensured by the agreement of other sites. Examples of non-token-based algorithms are Ricart-Agrawala's algorithm, Lamport's algorithm and Singhal's algorithm.
- Quorum-based approach: A site requests permission from a subset of sites, called a quorum, before entering its critical section. A site is allowed to enter its critical section if it receives permission from all the sites in the quorum. Mutual exclusion is ensured by the intersection property of quorums, that is, any two quorums have at least one site in common. Examples of quorum-based algorithms are Maekawa's algorithm, Tree quorum algorithm and Grid quorum algorithm.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to discuss. You have asked me to write the content on the requirement of mutual exclusion theorem for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM. Here is the content I have written in markdown format:

### Requirement of mutual exclusion theorem

- Mutual exclusion theorem is a fundamental property of distributed systems that ensures that only one process can access a shared resource at a time.
- Mutual exclusion theorem is required for the following reasons:
  - To prevent concurrent access to a shared resource that may result in inconsistency or corruption of data.
  - To ensure fairness and avoid starvation among competing processes that request the same resource.
  - To coordinate the actions of processes that need to cooperate or synchronize on a common task or goal.
  - To implement critical sections, locks, semaphores, monitors, and other synchronization primitives in distributed systems.
- Mutual exclusion theorem can be achieved by using various algorithms that are classified into two categories:
  - Token-based algorithms: These algorithms use a special message called a token that is passed among processes in a logical ring or a tree. The process that holds the token has the exclusive right to access the shared resource. Examples of token-based algorithms are Ricart-Agrawala algorithm, Suzuki-Kasami algorithm, and Raymond's algorithm.
  - Permission-based algorithms: These algorithms use request and reply messages to obtain the permission of other processes before accessing the shared resource. The process that receives the permission from all other processes has the exclusive right to access the shared resource. Examples of permission-based algorithms are Lamport's algorithm, Maekawa's algorithm, and Quorum-based algorithm.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of token based and non token based algorithms for distributed mutual exclusion.

# Token based and non token based algorithms for distributed mutual exclusion

## Distributed mutual exclusion

- Distributed mutual exclusion (DME) is the problem of ensuring that only one process at a time can access a shared resource in a distributed system.
- DME is important for maintaining consistency, correctness and coordination among the processes in a distributed system.
- DME algorithms can be classified into two categories: token based and non token based.

## Token based algorithms

- Token based algorithms use a unique token that is shared among all the processes in the system.
- The token represents the permission to enter the critical section (CS), the section of code that accesses the shared resource.
- A process can enter the CS only if it has the token, and it must release the token after exiting the CS.
- The token is passed among the processes according to some protocol, such as a logical ring, a tree, or a graph.
- Token based algorithms guarantee mutual exclusion, fairness, and freedom from deadlock and starvation, but they may incur high message complexity and latency.

## Non token based algorithms

- Non token based algorithms do not use a token, but rely on message exchanges among the processes to achieve mutual exclusion.
- A process that wants to enter the CS must send a request message to a set of other processes and wait for their replies.
- The set of other processes may be all the processes in the system, or a subset of them, such as a quorum or a coordinator.
- The request and reply messages are ordered by some criteria, such as timestamps, logical clocks, or vector clocks, to resolve conflicts and ensure mutual exclusion.
- Non token based algorithms may reduce the message complexity and latency, but they may suffer from deadlock, starvation, or unfairness.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on the performance metric for distributed mutual exclusion algorithms for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM.

### Performance metric for distributed mutual exclusion algorithms

Distributed mutual exclusion algorithms are algorithms that ensure that only one process at a time can access a shared resource in a distributed system. There are different types of distributed mutual exclusion algorithms, such as token-based, non-token-based, and quorum-based algorithms. Each algorithm has its own advantages and disadvantages, and can be evaluated based on the following four performance metrics :

- **Message complexity**: It is the number of messages that are required per critical section (CS) execution by a process. Message complexity affects the communication overhead and the network bandwidth consumption of the algorithm. The lower the message complexity, the better the performance of the algorithm.
- **Synchronization delay**: It is the time interval between the departure of a process from the CS and the entry of the next process into the CS. Synchronization delay affects the responsiveness and the fairness of the algorithm. The lower the synchronization delay, the better the performance of the algorithm.
- **Response time**: It is the time interval between the request of a process to enter the CS and the actual entry of the process into the CS. Response time affects the waiting time and the throughput of the algorithm. The lower the response time, the better the performance of the algorithm.
- **Fault tolerance**: It is the ability of the algorithm to handle failures of processes or messages in the system. Fault tolerance affects the reliability and the availability of the algorithm. The higher the fault tolerance, the better the performance of the algorithm.

Different algorithms may have different trade-offs among these performance metrics, depending on the assumptions and the design choices they make. For example, a token-based algorithm may have low message complexity and synchronization delay, but high response time and low fault tolerance. A non-token-based algorithm may have high message complexity and synchronization delay, but low response time and high fault tolerance. A quorum-based algorithm may have moderate message complexity and synchronization delay, but variable response time and fault tolerance, depending on the quorum size and selection. Therefore, the choice of the best algorithm for a given system depends on the system requirements and the characteristics of the distributed environment.  

I hope this information is helpful for your study. If you have any further questions, please feel free to ask me.😊



```markdown
## Unit 3 - Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set.
- Deadlocks can be handled by three strategies: deadlock prevention, deadlock avoidance, and deadlock detection.
- Deadlock prevention and avoidance are impractical in distributed systems because they require global knowledge and coordination.
- Deadlock detection in distributed systems entails two basic issues: detecting existing deadlocks and resolving detected deadlocks.
- Deadlock detection requires examining the status of process-resource interactions for the presence of cyclic wait.
- Deadlock detection in distributed systems can be done by two methods: global wait-for graph (WFG) and edge chasing.
- A global WFG is a directed graph that represents the waiting relationships among processes and resources in the system.
- A global WFG can be constructed from local WFGs at each site by a centralized or distributed algorithm.
- A deadlock exists in the system if and only if the global WFG contains a cycle.
- Edge chasing is a technique that detects cycles in the global WFG without constructing it explicitly.
- Edge chasing involves sending probe messages along the edges of the local WFGs and detecting cycles when a probe returns to its origin.
- Edge chasing can be implemented by various algorithms, such as the Chandy-Misra-Haas algorithm, the Ho-Ramamoorthy algorithm, and the Huang algorithm.
- Deadlock resolution involves selecting and aborting one or more processes involved in the deadlock to break the cycle.
- Deadlock resolution can be done by a centralized or distributed algorithm, depending on the deadlock detection method.
- Deadlock resolution can be based on various criteria, such as the number of resources held, the number of resources requested, the process priority, the process seniority, or the process rollback cost.
```



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
  - The representation of the process-resource interactions, such as wait-for graphs or dependency matrices.
  - The algorithm for detecting cycles in the process-resource interactions, such as edge chasing or global wait-for graph construction.
  - The location and frequency of deadlock detection, such as centralized, hierarchical, or distributed, and periodic or on-demand.
  - The resolution of deadlocks, such as aborting or preempting some processes in the cycle.



### Resource Vs Communication Deadlocks

- A deadlock is a condition where a process cannot proceed because it needs to obtain a resource held by another process, and it itself is holding a resource that the other process needs.
- There are two types of deadlocks in distributed systems: resource deadlocks and communication deadlocks .
- Resource deadlocks occur when processes access resources, such as data objects in database systems and buffers in store and forward communication networks .
  - A process acquires a resource before accessing it and releases it after using it .
  - A resource deadlock can be modeled by a wait-for graph, where nodes represent processes and edges represent resource requests .
  - A cycle in the wait-for graph indicates a deadlock .
- Communication deadlocks occur when processes exchange messages, such as in message passing systems and distributed algorithms .
  - A process sends a message to another process and waits for a reply before continuing .
  - A communication deadlock can be modeled by a dependency graph, where nodes represent processes and edges represent message dependencies .
  - A cycle in the dependency graph indicates a deadlock .
- The main difference between resource deadlocks and communication deadlocks is that resource deadlocks involve contention for resources, while communication deadlocks involve loss or corruption of signals .
  - Resource deadlocks can be prevented by using resource allocation protocols, such as deadlock avoidance or deadlock detection and recovery .
  - Communication deadlocks can be prevented by using reliable communication protocols, such as timeouts, acknowledgments, or sequence numbers .



### Deadlock Prevention for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process. Deadlocks can occur in distributed systems, where processes and resources are located on different machines connected by a network.

Deadlock prevention is a technique to avoid the occurrence of deadlocks by imposing some constraints on the resource allocation policies. There are two main methods of deadlock prevention in distributed systems:

- Ordered request: In this method, each resource type is assigned a unique level, and a process can request a resource only if its level is lower than the level of the resource it currently holds. This ensures that there is a global ordering of resource requests, and no circular wait can occur. For example, if there are three resource types A, B, and C, with levels 1, 2, and 3 respectively, then a process can request A only if it does not hold any resource, B only if it holds A, and C only if it holds B. This method is simple and easy to implement, but it may result in low resource utilization and reduced concurrency. 

- Collective request: In this method, a process must request all the resources it needs at the same time, and either get them all or none. This ensures that there is no hold and wait condition, and no process can block another process by holding a resource. For example, if a process needs resources A and B, it must request them together, and not request A first and then B. This method is more flexible and efficient than ordered request, but it may result in deadlock if there are not enough resources available to satisfy a request. 

Both methods of deadlock prevention require global knowledge of the resource allocation state and the resource request patterns of the processes, which may be difficult or costly to obtain in a distributed system. Therefore, deadlock prevention may not be suitable for all distributed systems, and other techniques such as deadlock detection and avoidance may be preferred.   

: https://www.geeksforgeeks.org/deadlock-prevention-policies-in-distributed-system/
: https://www.javatpoint.com/deadlock-detection-in-distributed-systems
: https://www.tutorialspoint.com/distributed_dbms/distributed_dbms_deadlock_handling.htm
: https://www.cse.scu.edu/~m1wang/projects/DeadLock_prevention_14s.pdf



### Avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- Deadlock avoidance is a technique that prevents the occurrence of deadlocks by ensuring that the system is always in a safe state.
- A safe state is one in which there exists a sequence of processes that can finish their execution without waiting for any resources.
- In a distributed system, deadlock avoidance is impractical due to several problems, such as:
  - The lack of global information about the resource allocation and requests of all processes.
  - The dynamic and unpredictable nature of the system, where processes and resources may join or leave at any time.
  - The high communication and synchronization overhead involved in maintaining a global safe state.
- Therefore, deadlock detection is preferred over deadlock avoidance in distributed systems.
- Deadlock detection is a technique that identifies the existence of deadlocks by examining the status of the process-resource interactions for the presence of cyclic wait.
- Deadlock detection in distributed systems can be classified into four categories, based on the type of information exchanged among processes and resources:
  - Path-pushing algorithms: These algorithms propagate the information about the wait-for relations along the paths of the wait-for graph. Each process maintains a set of dependent processes that are waiting for it directly or indirectly. When a process requests a resource, it sends its dependency set to the resource. When a resource is released, it sends the dependency set of the previous owner to the new owner. A deadlock is detected when a process receives its own identifier in a dependency set.
  - Edge-chasing algorithms: These algorithms send special messages called probes along the edges of the wait-for graph. Each probe contains the identifiers of the sender and the receiver of the resource request. When a process receives a probe, it forwards it to the process or resource it is waiting for. A deadlock is detected when a process receives a probe that contains its own identifier.
  - Diffusion computation algorithms: These algorithms initiate a computation at each process that requests a resource. The computation involves sending queries and replies among the processes and resources. A process sends a query to the process or resource it is waiting for, and waits for a reply. A resource replies positively to a query if it is free, and negatively if it is busy. A process replies positively to a query if it has received positive replies from all the processes or resources it has sent queries to, and negatively otherwise. A deadlock is detected when a process receives a negative reply.
  - Global state detection algorithms: These algorithms collect the global state of the system, such as the resource allocation and request matrices, and apply a centralized deadlock detection algorithm on it. The global state can be obtained by using techniques such as snapshot algorithms or distributed agreement algorithms. A deadlock is detected when the global state contains a cycle in the resource allocation graph.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of distributed deadlock detection and resolution:

### Distributed Deadlock Detection and Resolution

- A deadlock is a situation where a set of processes are blocked waiting for resources held by other processes in the set.
- In a distributed system, deadlocks can occur due to conflicting requests for resources across multiple sites or nodes.
- Distributed deadlock detection and resolution involves two steps: detecting the existence of deadlocks and breaking the deadlocks by releasing some resources or aborting some processes.
- There are three main approaches for distributed deadlock detection: centralized, distributed, and hierarchical.

#### Centralized Deadlock Detection

- In this approach, one site or node is designated as the coordinator or the deadlock detector.
- The coordinator maintains a global wait-for graph (WFG) that represents the dependencies among processes and resources in the system.
- The coordinator periodically collects local WFG information from all the sites and merges them into the global WFG.
- The coordinator then searches the global WFG for cycles, which indicate the presence of deadlocks.
- If a deadlock is detected, the coordinator initiates a resolution strategy, such as aborting the youngest or the lowest priority process in the cycle, or preempting some resources from the cycle.
- The advantages of this approach are simplicity and efficiency, as the coordinator can detect deadlocks quickly and accurately.
- The disadvantages of this approach are scalability and reliability, as the coordinator can become a bottleneck and a single point of failure in the system.

#### Distributed Deadlock Detection

- In this approach, there is no central coordinator or global WFG.
- Each site or node maintains its own local WFG and communicates with other sites or nodes to detect deadlocks.
- There are two main methods for distributed deadlock detection: probe-based and path-pushing.

##### Probe-Based Method

- In this method, each site or node initiates a probe message when it detects a potential deadlock situation, such as a blocked request for a resource held by another site or node.
- The probe message contains the identity of the initiator and the blocked request.
- The probe message is forwarded along the dependency chain until it reaches the initiator or a dead end.
- If the probe message returns to the initiator, a deadlock is detected and the initiator initiates a resolution strategy.
- If the probe message reaches a dead end, no deadlock is detected and the probe message is discarded.
- The advantages of this method are scalability and reliability, as there is no central coordinator or global WFG.
- The disadvantages of this method are complexity and overhead, as multiple probe messages may be generated and propagated in the system.

##### Path-Pushing Method

- In this method, each site or node maintains a set of dependency paths that represent the dependencies among processes and resources in the system.
- A dependency path is a sequence of processes and resources that are involved in a dependency chain.
- Each site or node periodically sends its dependency paths to its neighbors, and merges the received dependency paths with its own.
- Each site or node then searches its dependency paths for cycles, which indicate the presence of deadlocks.
- If a deadlock is detected, the site or node initiates a resolution strategy, such as aborting the youngest or the lowest priority process in the cycle, or preempting some resources from the cycle.
- The advantages of this method are simplicity and efficiency, as each site or node can detect deadlocks locally and accurately.
- The disadvantages of this method are scalability and reliability, as the dependency paths may grow large and redundant in the system.

#### Hierarchical Deadlock Detection

- In this approach, the sites or nodes are organized into a hierarchy of clusters, such as a tree or a graph.
- Each cluster has a leader or a coordinator that is responsible for deadlock detection and resolution within the cluster.
- The leaders or coordinators communicate with each other to detect and resolve inter-cluster deadlocks.
- The leaders or coordinators can use any of the centralized or distributed methods for deadlock detection and resolution within and across the clusters.
- The advantages of this approach are scalability and reliability, as the system is divided into smaller and manageable units, and the failure of a leader or a coordinator can be tolerated by electing a new one.
- The disadvantages of this approach are complexity and overhead, as the hierarchy and the communication among the leaders or coordinators need to be maintained and updated.



### Centralized Deadlock Detection

- This is a technique used in distributed systems to handle deadlock detection.
- According to this technique, the system maintains one global wait-for graph in a single chosen site, which is named as deadlock-detection coordinator.
- The coordinator collects information about the local wait-for graphs of each site and constructs the global wait-for graph.
- The coordinator periodically runs a deadlock detection algorithm on the global wait-for graph and informs the sites about the deadlocks.
- The advantages of this technique are simplicity and efficiency.
- The disadvantages of this technique are single point of failure, communication overhead, and lack of scalability.

: https://www.exploredatabase.com/2014/06/centralized-deadlock-detection-approach-in-distributed-database.html
: https://www.javatpoint.com/deadlock-detection-in-distributed-systems
: https://people.cs.rutgers.edu/~pxk/417/notes/deadlock.html



### Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set.
- Deadlocks can occur in distributed systems when distributed transactions or concurrency control are utilized.
- Deadlock detection is one of the strategies to deal with deadlocks, along with deadlock prevention and deadlock avoidance.
- Deadlock detection in distributed systems entails addressing two basic issues: detection of existing deadlocks and resolution of detected deadlocks.
- Deadlock detection requires examination of the status of process-resource interactions for presence of cyclic wait.
- There are three approaches to detect deadlocks in distributed systems:
  - Centralized approach: A single node is designated as the deadlock detector and collects the local wait-for graphs from all the nodes to construct a global wait-for graph. The deadlock detector periodically runs a cycle detection algorithm on the global wait-for graph and informs the nodes about the deadlocked processes. This approach has the advantages of simplicity and low message complexity, but the disadvantages of single point of failure and bottleneck.
  - Hierarchical approach: The nodes are organized into a logical hierarchy, such as a tree, and each node has a parent and possibly some children. The leaf nodes send their local wait-for graphs to their parents, who aggregate them and send them to their parents, and so on, until the root node receives the global wait-for graph. The root node runs a cycle detection algorithm and sends the deadlock information to the affected nodes. This approach has the advantages of fault tolerance and load balancing, but the disadvantages of high message complexity and delay.
  - Distributed approach: Each node maintains its own local wait-for graph and initiates a cycle detection algorithm when it suspects a deadlock. The cycle detection algorithm involves sending probe messages along the edges of the wait-for graph and waiting for replies. If a node receives a probe message that originated from itself, it detects a cycle and initiates a deadlock resolution. This approach has the advantages of no single point of failure and no global wait-for graph, but the disadvantages of high message complexity and false deadlock detection.



### Path Pushing Algorithms

- Path pushing algorithms detect distributed deadlocks by maintaining an explicit global wait-for graph (WFG) at each site of the distributed system  .
- The global WFG is constructed by merging the local WFGs of each site, which represent the waiting relationships among the processes at that site  .
- Whenever a site performs a deadlock computation, it sends its local WFG to all its neighboring sites, which then update their global WFGs accordingly  .
- A site can initiate a deadlock computation either periodically or when it detects a change in its local WFG  .
- A site can detect a deadlock by checking for a cycle in its global WFG that involves one of its local processes  .
- The advantages of path pushing algorithms are that they can detect deadlocks quickly and accurately, and they do not require any additional messages for deadlock detection  .
- The disadvantages of path pushing algorithms are that they require a lot of storage space and communication bandwidth to maintain and exchange the global WFGs, and they may incur false positives due to stale information  .



### Edge Chasing Algorithms for Distributed Deadlock Detection

- Edge chasing algorithms are a class of distributed deadlock detection algorithms that use special messages called probes to trace the dependency graph of processes and resources in a distributed system.
- A probe is a triplet (i, j, k) that denotes that the deadlock detection is initiated by process Pi, and the message is sent by the home site of process Pj to the home site of process Pk.
- The home site of a process is the site where the process is executing, and it is responsible for sending and receiving probes on behalf of the process.
- The algorithm works as follows:
  - When a process Pi initiates a deadlock detection, it sends a probe (i, i, j) to the home site of process Pj, where Pj is the process that Pi is waiting for.
  - When the home site of process Pj receives a probe (i, j, k), it checks if Pj is waiting for any other process Pk. If yes, it forwards the probe (i, j, k) to the home site of process Pk. If no, it discards the probe.
  - When the home site of process Pk receives a probe (i, j, k), it checks if Pk is the same as Pi. If yes, it means that a cycle has been detected, and a deadlock exists. It informs Pi about the deadlock. If no, it repeats the previous step.
  - The algorithm terminates when either a deadlock is detected or all the probes are discarded.
- The algorithm is also known as Chandy-Misra-Haas's algorithm for the AND request model, where a process can request multiple resources simultaneously and wait for all of them to be granted.
- The algorithm has the following properties:
  - It is a distributed algorithm, meaning that it does not require a central coordinator or a global state of the system.
  - It is an edge-chasing algorithm, meaning that it follows the edges of the dependency graph from the waiting nodes to the blocking nodes.
  - It is a probe-based algorithm, meaning that it uses special messages to detect cycles in the dependency graph.
  - It is a local algorithm, meaning that it only involves the sites that are part of the cycle.
  - It is a demand-driven algorithm, meaning that it is initiated only when a process suspects a deadlock.



## Unit 4 - Agreement Protocols

- Agreement protocols are a class of distributed algorithms that allow a set of processes to reach a consensus on a value, despite the presence of failures or malicious behavior.
- Agreement protocols are useful for implementing fault-tolerant services, such as distributed databases, replicated state machines, leader election, atomic broadcast, etc.
- Agreement protocols can be classified into different types, depending on the assumptions they make about the system model, the communication model, the failure model, and the adversary model.
- Some common types of agreement protocols are:
  - **Byzantine agreement**: The processes have to agree on a binary value (0 or 1), and some of them may be faulty or malicious (Byzantine). The communication is synchronous, meaning that there is a known upper bound on message delays. The goal is to ensure that all correct processes agree on the same value, and that the value is valid, meaning that it was proposed by some correct process.
  - **Paxos**: The processes have to agree on a single value (not necessarily binary), and some of them may crash or recover (crash-recovery). The communication is asynchronous, meaning that there is no upper bound on message delays. The goal is to ensure that all correct processes agree on the same value, and that the value is chosen, meaning that it was proposed by some process.
  - **Raft**: The processes have to agree on a sequence of values (a log), and some of them may crash or recover (crash-recovery). The communication is partially synchronous, meaning that there is an unknown upper bound on message delays, which eventually becomes known. The goal is to ensure that all correct processes agree on the same log, and that the log is consistent, meaning that it contains the same entries in the same order.
  - **Two-phase commit**: The processes have to agree on whether to commit or abort a transaction, and some of them may crash (crash-stop). The communication is synchronous, meaning that there is a known upper bound on message delays. The goal is to ensure that all correct processes agree on the same decision, and that the decision is atomic, meaning that either all processes commit or all processes abort.
- Agreement protocols typically consist of one or more rounds of message exchange, where each process sends and receives messages from other processes, and updates its state and output accordingly.
- Agreement protocols have to deal with various challenges, such as network partitions, message losses, message duplication, message reordering, message corruption, process crashes, process recoveries, process duplications, process impersonations, etc.
- Agreement protocols have to satisfy various properties, such as validity, agreement, termination, integrity, consistency, atomicity, etc. These properties may have different definitions and implications depending on the type of agreement protocol and the system model.
- Agreement protocols are often proved correct using formal methods, such as state machines, invariants, induction, contradiction, etc. These proofs have to show that the protocol satisfies the desired properties under all possible scenarios and executions.



Hello, I am Sydney, your AI assistant. I can help you with writing notes on various topics. Here is the content I have generated for the topic of Introduction for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM.

```markdown
# Introduction for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- A distributed system is a collection of independent and geographically dispersed nodes that communicate and coordinate their actions by passing messages.
- Agreement protocols are algorithms that enable the nodes of a distributed system to reach a common decision or a consistent state, despite the presence of failures, asynchrony, or malicious behavior.
- Agreement protocols are essential for ensuring the correctness, reliability, and availability of distributed systems, especially in applications such as consensus, fault tolerance, replication, distributed transactions, and blockchain.
- Some of the challenges and requirements for designing agreement protocols are:
  - Dealing with partial failures, such as node crashes, network partitions, or message losses.
  - Handling Byzantine failures, where some nodes may behave arbitrarily or maliciously, such as sending incorrect or conflicting messages, or colluding with other faulty nodes.
  - Achieving termination, validity, and agreement properties, which ensure that all correct nodes eventually decide on a valid and consistent value.
  - Coping with asynchrony, where there is no bound on the message delays or the relative speeds of the nodes, and the nodes may have different or inaccurate views of the system state.
  - Balancing the trade-offs between performance, complexity, and resilience, such as minimizing the number of communication rounds, the message size, the computational overhead, and the number of faulty nodes tolerated.
- Some of the examples and classifications of agreement protocols are:
  - Leader election, where the nodes elect a unique coordinator or a primary node among themselves, which can then initiate or coordinate other tasks.
  - Atomic broadcast, where the nodes broadcast messages to all other nodes in a reliable and ordered manner, such that all correct nodes receive the same sequence of messages.
  - Consensus, where the nodes propose and agree on a single value, such as a state update, a transaction commit, or a block of transactions.
  - Byzantine agreement, where the nodes reach consensus in the presence of Byzantine failures, which requires a higher degree of fault tolerance and cryptographic techniques.
  - Multi-party computation, where the nodes jointly compute a function of their private inputs, without revealing their inputs to each other, such as secure auctions, voting, or data analysis.
```



# System models for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

A system model is a description of the properties and assumptions of a distributed system that are relevant for its design and analysis. System models can help us understand the behavior and limitations of a distributed system, and guide us in choosing appropriate algorithms and protocols for achieving certain goals.

There are different types of system models that capture different aspects of a distributed system, such as:

- **Network behavior**: how reliable, fast, and secure are the communication links between the nodes of the system?
- **Node behavior**: how reliable, fast, and secure are the nodes of the system, and what are their capabilities and resources?
- **Timing behavior**: how synchronized are the clocks of the nodes of the system, and how predictable are the delays and durations of events and messages?
- **Consensus behavior**: how can the nodes of the system reach agreement on a common value or action, despite the presence of failures and uncertainties?

Some examples of system models for distributed systems are:

- **Synchronous system model**: a system model that assumes bounded network delays, bounded node processing speeds, and bounded clock drifts. This model simplifies the design and analysis of distributed algorithms, but it is unrealistic for most practical systems.
- **Asynchronous system model**: a system model that assumes no bounds on network delays, node processing speeds, or clock drifts. This model is more realistic for most practical systems, but it makes the design and analysis of distributed algorithms more challenging and complex.
- **Partially synchronous system model**: a system model that assumes some bounds on network delays, node processing speeds, or clock drifts, but not all of them. This model is a compromise between the synchronous and asynchronous models, and it tries to capture the realistic behavior of most practical systems.
- **Crash-stop system model**: a system model that assumes nodes can only fail by crashing (stopping to function), and they cannot recover from failures. This model simplifies the design and analysis of fault-tolerant distributed algorithms, but it is unrealistic for most practical systems.
- **Crash-recovery system model**: a system model that assumes nodes can fail by crashing, but they can also recover from failures and resume their operation. This model is more realistic for most practical systems, but it makes the design and analysis of fault-tolerant distributed algorithms more challenging and complex.
- **Byzantine system model**: a system model that assumes nodes can fail in arbitrary ways, including behaving maliciously or inconsistently. This model is the most general and realistic for most practical systems, but it also makes the design and analysis of fault-tolerant distributed algorithms the most difficult and complex.
- **Leader-based system model**: a system model that assumes there is a special node in the system, called the leader, that coordinates the actions and decisions of the other nodes. This model simplifies the design and analysis of distributed algorithms, but it also introduces a single point of failure and a bottleneck in the system.
- **Peer-to-peer system model**: a system model that assumes there is no special node in the system, and all nodes are equal and cooperate with each other. This model is more robust and scalable than the leader-based model, but it also makes the design and analysis of distributed algorithms more challenging and complex.



### Classification of Agreement Problem

An agreement problem is a problem where a set of processes in a distributed system have to agree on a common value or decision, despite the possibility of failures or malicious behavior. Agreement problems are fundamental to the design of fault-tolerant distributed systems, as they enable coordination and consistency among the processes.

There are different types of agreement problems, depending on the assumptions and requirements of the system. Some of the well-known agreement problems are:

- **Byzantine agreement problem**: A single value, which is to be agreed on, is initialized by an arbitrary process and all non-faulty processes have to agree on that value. The processes may be subject to Byzantine failures, which means they can behave arbitrarily or maliciously. The goal is to ensure that all non-faulty processes agree on the same value, and that value is the initial value of some non-faulty process  .
- **Consensus problem**: A generalization of the Byzantine agreement problem, where each process can propose a value and all non-faulty processes have to agree on a common value. The value agreed on must be one of the proposed values, and the processes must terminate the protocol in a finite number of steps  .
- **Interactive consistency problem**: A variation of the Byzantine agreement problem, where each process has an initial value and all non-faulty processes have to agree on a vector of values, one for each process. The vector agreed on must satisfy two properties: (1) the value for each non-faulty process is its initial value, and (2) the value for each faulty process is the same for all non-faulty processes  .

These problems are related to each other, and solutions for one problem can be used to solve another problem. For example, a solution for the consensus problem can be used to solve the Byzantine agreement problem, by having each process propose the value initialized by itself. A solution for the interactive consistency problem can be used to solve the consensus problem, by having each process propose a vector of values, one for each process, and then agreeing on the first element of the vector  .

The difficulty of solving these problems depends on the system model, such as the number of processes, the number of faulty processes, the type of communication channels, the type of failures, and the type of synchrony. For example, it is impossible to solve the consensus problem in an asynchronous system with one faulty process, even if the failures are benign (such as crashes). However, it is possible to solve the consensus problem in a synchronous system with a majority of non-faulty processes, even if the failures are Byzantine  .

The applications of agreement problems are numerous, as they can be used to implement various distributed services and algorithms, such as atomic broadcast, atomic commit, group membership, leader election, distributed mutual exclusion, state machine replication, and blockchain .



### Byzantine agreement problem

The Byzantine agreement problem is a fundamental problem in fault tolerant distributed computing. It requires a set of parties in a distributed environment to agree on a value even if some of the parties are corrupted. A corrupted party may behave arbitrarily, sending conflicting or misleading messages to different parties, or remaining silent. The problem is also known as the Byzantine generals problem, the interactive consistency problem, or the source congruency problem.

The problem was first defined by Lamport in the context of a source processor broadcasting its initial value to other processors in the system. The source processor may be faulty, and some of the other processors may be faulty as well. The goal is to ensure that all the non-faulty processors agree on the same value, which is either the initial value of the source processor if it is non-faulty, or an arbitrary value otherwise.

The problem can be generalized to the case where each processor has its own initial value, and the goal is to ensure that all the non-faulty processors agree on the same value, which is a function of the initial values of the non-faulty processors. This is known as the Byzantine consensus problem.

Some of the challenges and solutions to the Byzantine agreement problem are:

- The problem is impossible to solve in a purely asynchronous system, where there is no bound on the message delivery time or the relative speed of the processors. This is because a faulty processor can delay its messages indefinitely, making it indistinguishable from a slow or crashed processor. A solution requires some form of synchrony, such as a common clock, a timeout mechanism, or a partial order of events.
- The problem is also impossible to solve if more than one-third of the processors are faulty. This is because a faulty processor can send different values to different subsets of processors, creating a split in the system. A solution requires a majority of non-faulty processors, or a stronger assumption on the fault model, such as the ability to detect or exclude faulty processors.
- The problem can be solved using various algorithms, such as the oral messages algorithm, the signed messages algorithm, the authenticated broadcast algorithm, or the randomized algorithm. These algorithms differ in the number of rounds, the number of messages, the message size, the computational complexity, and the security assumptions. A common technique is to use a reduction from the Byzantine consensus problem to the Byzantine agreement problem, and then use a recursive algorithm to reach agreement on each bit of the consensus value.

The Byzantine agreement problem is relevant for many applications in distributed systems, such as distributed databases, distributed ledgers, distributed consensus protocols, fault-tolerant replication, and secure multiparty computation. The problem illustrates the trade-offs and limitations of achieving reliability, consistency, and security in a distributed environment.

: Lamport, L., Shostak, R., & Pease, M. (1982). The Byzantine generals problem. ACM Transactions on Programming Languages and Systems (TOPLAS), 4(3), 382-401.



### Consensus problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- The consensus problem is the problem of getting a set of nodes in a distributed system to agree on something - it might be a value, a course of action or a decision.
- Achieving consensus allows a distributed system to act as a single entity, with every individual node aware of and in agreement with the actions of the whole of the network.
- Consensus is a general agreement on a decision made by the majority of those involved.
- Consensus is needed in a distributed system to ensure overall system reliability on top of unreliable system components.
- Consensus is also needed to cope with failures, such as network partitions, message losses, node crashes, or malicious attacks.
- There are many ways in which processes in a distributed system can reach a consensus, but there is usually a trade-off between security and performance.
- The more we want our algorithm to be secure against ways in which failure can happen, the less performant it tends to become.
- Some of the common consensus algorithms in distributed systems are:
  - Two-phase commit (2PC): A simple and widely used protocol that involves a coordinator and a set of participants.
  - Three-phase commit (3PC): An extension of 2PC that adds a pre-commit phase to avoid blocking in case of coordinator failure.
  - Paxos: A family of protocols that use a leader election and a majority voting mechanism to achieve consensus in the presence of failures.
  - Raft: A simplified version of Paxos that is easier to understand and implement, and that also provides strong consistency and fault tolerance.
  - Byzantine fault tolerance (BFT): A class of protocols that can tolerate arbitrary failures, including malicious or faulty nodes, by requiring a supermajority of nodes to agree.
- The consensus problem is proven to be impossible to solve in a fully asynchronous distributed system with even one faulty process.
- This is known as the FLP impossibility result, named after the authors Fischer, Lynch and Paterson.
- However, the consensus problem can be solved in a partially synchronous or a synchronous distributed system, or by making some assumptions about the failure model or the network behavior.



### Interactive Consistency Problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- Interactive consistency is the problem in which n distinct nodes, each having its own private value, where up to t may be Byzantine, run an algorithm that allows all non-faulty nodes to infer the values of each other node  .
- Byzantine nodes are those that can behave arbitrarily, such as sending incorrect or conflicting messages, or remaining silent .
- Interactive consistency is also known as Byzantine Generals Problem, which is a metaphor for a situation where a group of generals must agree on a common plan of action, while some of them may be traitors .
- Interactive consistency is a fundamental problem in distributed systems, as it is a prerequisite for achieving consensus, which is the agreement on a single value among all nodes .
- Interactive consistency is also relevant to critical applications that rely on the combination of the opinions of multiple peers to provide a service, such as voting systems, fault-tolerant control systems, or blockchain systems  .
- Interactive consistency is a challenging problem, as it requires both communication and computation among nodes, and it must tolerate the presence of faults and adversarial behavior   .
- Interactive consistency has been studied extensively in the literature, and various algorithms have been proposed to solve it under different assumptions and models, such as synchronous, asynchronous, or partially synchronous systems, or with different types of communication channels, such as reliable, authenticated, or broadcast   .
- Interactive consistency has some limitations and impossibility results, such as the lower bound on the number of messages required to achieve it, or the impossibility of achieving it in asynchronous systems with only one faulty node   .
- Interactive consistency has some variants and extensions, such as probabilistic interactive consistency, which allows some probability of error, or generalized interactive consistency, which allows different levels of agreement among nodes   .



### Solution to Byzantine Agreement problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

The Byzantine Agreement problem is a fundamental problem in fault tolerant distributed computing. It requires a set of parties in a distributed environment to agree on a value even if some of the parties are corrupted. A corrupted party may behave arbitrarily, sending conflicting or misleading messages to different parties. The problem is named after the Byzantine Generals problem, which is a metaphor for the situation where several divisions of the Byzantine army are camped outside an enemy city, each division commanded by its own general. The generals can communicate with one another only by messenger. After observing the enemy, they must decide upon a common plan of action, such as attack or retreat. However, some of the generals may be traitors, who may try to sabotage the plan by sending false messages or no messages at all. The loyal generals need to agree on a plan that is consistent with the majority of the loyal generals, and that does not depend on the traitors' messages.

The solution to the Byzantine Agreement problem depends on the following factors:

- The number of parties involved, denoted by n.
- The number of corrupted parties, denoted by t.
- The type of communication channels, whether they are synchronous or asynchronous, and whether they are authenticated or not.
- The type of initial values, whether they are binary (0 or 1) or multivalued.

Some general results for the Byzantine Agreement problem are:

- If the communication channels are synchronous and authenticated, then Byzantine Agreement is possible if and only if n > 3t. This means that the number of loyal parties must be more than three times the number of corrupted parties. A simple algorithm for this case is the oral messages algorithm, which involves sending and relaying messages among the parties for t+1 rounds, and then deciding on the majority value of the messages received in the last round.
- If the communication channels are asynchronous and authenticated, then Byzantine Agreement is possible if and only if n > 2t. This means that the number of loyal parties must be more than twice the number of corrupted parties. A simple algorithm for this case is the signed messages algorithm, which involves sending and relaying signed messages among the parties, and then deciding on the value that has been signed by more than n-t parties.
- If the communication channels are synchronous and unauthenticated, then Byzantine Agreement is possible if and only if n > 3t and the initial values are binary. This means that the number of loyal parties must be more than three times the number of corrupted parties, and the parties can only choose between 0 and 1. A simple algorithm for this case is the majority voting algorithm, which involves sending and relaying messages among the parties for t+1 rounds, and then deciding on the majority value of the messages received in the last round. However, this algorithm requires a common coin, which is a random bit that is agreed by all the loyal parties and unknown to the corrupted parties.
- If the communication channels are asynchronous and unauthenticated, then Byzantine Agreement is impossible, regardless of the number of parties, the number of corrupted parties, and the type of initial values. This is because the corrupted parties can always delay or forge messages to prevent the loyal parties from reaching a consensus.

These are some of the basic results for the Byzantine Agreement problem. There are also more advanced and efficient algorithms that can achieve Byzantine Agreement under different assumptions and scenarios. For example, there are algorithms that use cryptography, such as digital signatures or public-key encryption, to enhance the security and performance of the communication channels. There are also algorithms that use randomization, such as coin tossing or leader election, to break the symmetry and reduce the complexity of the problem. Furthermore, there are algorithms that use quorums, such as intersecting sets or threshold schemes, to reduce the number of messages and rounds required for the agreement. These algorithms are beyond the scope of this note, but they can be found in the references below.

References:

-  Byzantine Agreement Problem in Distributed System - TheCode11
-  The Byzantine Generals Problem, Explained - Komodo Platform
-  PRISM - Case Studies - Byzantine Agreement
-  The Byzantine Generals Problem - Cornell University



# Application of Agreement problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- Agreement problem is a fundamental problem in distributed computing and multi-agent systems, where a set of processes need to coordinate and reach a common decision or value, despite the presence of faults or failures .
- Agreement problem has many variants, such as consensus, atomic commitment, atomic broadcast, and group membership. Each variant has different assumptions, requirements, and guarantees.
- Consensus is the most basic and general form of agreement problem, where each process proposes a value and all correct processes must agree on the same value, which must be one of the proposed values . Consensus is essential for implementing fault-tolerant services, such as replicated state machines, distributed transactions, leader election, and distributed locking.
- Atomic commitment is a special case of consensus, where each process has a binary value (commit or abort) and all correct processes must agree on the same value, which must be commit if and only if all processes have commit as their initial value . Atomic commitment is useful for ensuring the atomicity and durability of distributed transactions, where a transaction either commits or aborts at all participating sites.
- Atomic broadcast is another special case of consensus, where each process broadcasts a message and all correct processes must deliver the same set of messages in the same order . Atomic broadcast is useful for implementing total order multicast, where messages are delivered to all processes in a consistent order, regardless of the network delays or failures.
- Group membership is a related problem to consensus, where each process maintains a view of the current set of processes in the system, and all correct processes must agree on the same view, which must reflect the actual failures and recoveries of processes . Group membership is useful for implementing fault detection, fault notification, and fault recovery mechanisms, as well as for maintaining consistent replicas of data or services.



### Atomic Commit in Distributed Database System

- A distributed database system consists of multiple database sites that are connected by a communication network.
- A distributed transaction is a transaction that accesses data from multiple sites and executes as a single logical unit of work.
- An atomic commit is an operation that applies a set of distinct changes as a single operation. If the changes are applied, then the atomic commit is said to have succeeded. If the changes are not applied, then the atomic commit is said to have failed or aborted.
- An atomic commit protocol is a protocol that ensures the atomicity of distributed transactions, i.e., either all the changes are committed at all the sites, or none of them are committed at any site.
- Atomic commit protocols are needed to maintain the consistency and reliability of distributed data, especially in the presence of failures, such as site crashes, network partitions, or message losses.
- Atomic commit protocols can be classified into two categories: blocking and non-blocking.
  - Blocking protocols are protocols that require some sites to wait for the decision of other sites before committing or aborting their changes. Blocking protocols can suffer from blocking problems, such as deadlock, livelock, or indefinite postponement, if some sites fail or become unreachable.
  - Non-blocking protocols are protocols that allow some sites to decide independently of other sites, based on the information they have. Non-blocking protocols can avoid blocking problems, but they may incur more communication overhead or require more assumptions about the system model.
- Some examples of atomic commit protocols are:
  - Two-phase commit (2PC): A blocking protocol that uses a coordinator site to collect the votes of all the participant sites and then broadcast the final decision to all the sites. 2PC ensures atomicity and agreement, but it can block if the coordinator or some participants fail.
  - Three-phase commit (3PC): A blocking protocol that extends 2PC with an additional phase to reduce the possibility of blocking. 3PC introduces a pre-commit phase, in which the coordinator and the participants prepare to commit and exchange acknowledgments. 3PC ensures atomicity, agreement, and non-triviality, but it can still block if some sites fail during the pre-commit phase.
  - Paxos commit: A non-blocking protocol that uses a consensus algorithm to elect a leader site and reach a decision among a majority of sites. Paxos commit ensures atomicity, agreement, and termination, but it requires a majority of sites to be alive and reachable, and it may incur more messages than 2PC or 3PC.
  - FLAC: A non-blocking protocol that leverages failure-awareness to optimize the communication cost and latency of atomic commit. FLAC uses a failure detector to monitor the liveness of the sites and dynamically adjusts the protocol steps based on the failure information. FLAC ensures atomicity, agreement, and termination, and it can achieve optimal performance in both failure-free and failure-prone scenarios.



# Unit 5 - Distributed Resource Management

- Distributed resource management (DRM) is an evolving discipline consisting of a set of software, hardware, network tools, procedures and policies for enabling distributed enterprise systems to operate effectively in production.
- Distributed enterprise systems are composed of multiple components that are distributed across different locations, such as data centers, cloud platforms, edge devices, etc.
- DRM aims to optimize the performance, availability, scalability, security, and cost of distributed enterprise systems by managing the allocation, utilization, and coordination of the resources involved.
- Some of the challenges and goals of DRM are:
  - Resource discovery: finding and identifying the available resources in a distributed system, such as servers, storage, network, etc. Resource discovery can be implemented in a centralized or decentralized manner.
  - Resource scheduling: assigning and executing tasks on the appropriate resources based on the requirements and constraints of the tasks, such as deadlines, priorities, dependencies, etc. Resource scheduling can be static or dynamic, depending on the degree of flexibility and adaptability of the system.
  - Resource monitoring: collecting and analyzing the status and performance metrics of the resources and the tasks, such as CPU utilization, memory usage, network latency, etc. Resource monitoring can be used for fault detection, load balancing, performance tuning, etc.
  - Resource coordination: ensuring the consistency and coherence of the resources and the tasks, such as data consistency, concurrency control, transaction management, etc. Resource coordination can be achieved by using protocols, algorithms, or middleware that facilitate the communication and synchronization among the resources and the tasks.
- DRM can be applied to various domains and scenarios, such as:
  - Distributed energy resource management system (DERMS): a system that allows real-time communication and control across the batteries, solar panels, and other edge devices that normally lie behind-the-meter and outside grid operators’ direct control. DERMS can enhance the system resiliency, reliability, efficiency, and sustainability by managing the generation, storage, and consumption of distributed energy resources.
  - Distributed database management system (DDBMS): a system that allows the storage and retrieval of data across multiple database servers that are geographically dispersed. DDBMS can improve the data availability, scalability, and performance by managing the replication, partitioning, and querying of distributed data.
  - Distributed cloud computing: a paradigm that allows the delivery of cloud services from multiple locations, such as public clouds, private clouds, edge clouds, etc. Distributed cloud computing can reduce the network latency, bandwidth consumption, and data privacy risks by managing the placement, migration, and execution of cloud applications and services.



### Issues in distributed file systems

A distributed file system (DFS) is a system that allows multiple clients to access and manipulate files stored on one or more servers over a network. A DFS provides the abstraction of a single, logical file system that spans multiple physical devices and locations. A DFS can offer benefits such as fault tolerance, scalability, performance, and transparency .

However, designing and implementing a DFS also involves many challenges and issues, such as:

- **Naming and name resolution**: A DFS needs a consistent and efficient way to name and locate files across different servers and clients. A DFS may use a hierarchical namespace, a flat namespace, or a hybrid namespace to organize files. A DFS also needs a mechanism to resolve names to physical locations, such as using a centralized or distributed directory service, or using a hash-based scheme.
- **Replication and consistency**: A DFS may replicate files or parts of files across multiple servers to improve availability, reliability, and performance. However, replication also introduces the problem of maintaining consistency among replicas, especially when concurrent updates occur. A DFS may use different consistency models, such as strict consistency, sequential consistency, causal consistency, or eventual consistency, depending on the trade-off between performance and correctness.
- **Caching and cache coherence**: A DFS may cache files or parts of files on the client side to reduce network traffic and latency. However, caching also introduces the problem of maintaining coherence between the cached copies and the original copies on the servers, especially when concurrent updates occur. A DFS may use different cache coherence protocols, such as write-through, write-back, or write-once, depending on the trade-off between performance and correctness.
- **Security and access control**: A DFS needs to ensure that only authorized users and applications can access and manipulate files on the servers. A DFS also needs to protect the confidentiality, integrity, and availability of the files from malicious attacks or accidental errors. A DFS may use different security mechanisms, such as encryption, authentication, authorization, auditing, or digital signatures, depending on the level of security required.
- **Fault tolerance and recovery**: A DFS needs to cope with various types of failures, such as server crashes, network partitions, disk failures, or corrupted data. A DFS also needs to recover from failures and restore the normal operation of the system as soon as possible. A DFS may use different fault tolerance and recovery techniques, such as replication, checkpointing, logging, or transactions, depending on the level of reliability required.
- **Scalability and performance**: A DFS needs to support a large number of files, servers, and clients, and handle a high volume of requests, without degrading the quality of service. A DFS also needs to balance the load among the servers and clients, and avoid bottlenecks and hotspots. A DFS may use different scalability and performance techniques, such as hashing, caching, replication, or partitioning, depending on the level of efficiency required.
- **Interoperability and compatibility**: A DFS may need to interoperate and communicate with other file systems, such as local file systems, network file systems, or cloud file systems. A DFS also needs to ensure that the files can be accessed and manipulated by different platforms, applications, and protocols, without losing information or functionality. A DFS may use different interoperability and compatibility techniques, such as standardization, conversion, or emulation, depending on the level of transparency required.

These are some of the main issues in distributed file systems. There may be other issues depending on the specific design and implementation of a DFS. A DFS may also use different approaches and solutions to address these issues, depending on the requirements and constraints of the system. A DFS is a complex and dynamic system that needs to balance various trade-offs and challenges.



### Mechanism for building distributed file systems

A distributed file system (DFS) is a file system that enables clients to access file storage from multiple hosts through a computer network as if the user was accessing local storage. Files are spread across multiple storage servers and in multiple locations, which enables users to share data and storage resources.

The mechanism for building distributed file systems involves the following steps:

- Designing a namespace: A namespace is a logical structure that organizes the files and directories in a DFS. A namespace can be flat or hierarchical, depending on the needs of the system. A flat namespace assigns a unique name to each file, regardless of its location. A hierarchical namespace organizes files into a tree-like structure, where each node represents a directory or a file. A namespace can also be global or local, depending on the scope of the system. A global namespace allows users to access files from any network or computer, while a local namespace restricts access to a specific domain or network.
- Implementing a naming service: A naming service is a component that maps the names of files and directories to their physical locations on the storage servers. A naming service can be centralized or distributed, depending on the scalability and reliability of the system. A centralized naming service uses a single server to store and manage the namespace, which simplifies the design but creates a single point of failure and a performance bottleneck. A distributed naming service uses multiple servers to store and manage the namespace, which improves the availability and performance but increases the complexity and overhead of the system.
- Providing file access: File access is the process of reading and writing data to and from the files in a DFS. File access can be implemented using different methods, such as remote access, upload/download, caching, replication, or migration. Remote access involves sending requests and responses over the network between the clients and the servers, which minimizes the storage space but increases the network traffic and latency. Upload/download involves transferring the entire file between the clients and the servers, which reduces the network traffic but consumes more storage space and bandwidth. Caching involves storing a copy of the file or a part of it on the client side, which improves the performance and availability but introduces the problem of cache consistency. Replication involves creating multiple copies of the file on different servers, which enhances the reliability and fault tolerance but requires more storage space and synchronization. Migration involves moving the file from one server to another, based on the access patterns or load balancing, which optimizes the resource utilization but adds more complexity and overhead to the system.
- Ensuring consistency and coherence: Consistency and coherence are the properties that ensure that the files in a DFS are up-to-date and identical across the system. Consistency and coherence can be achieved using different techniques, such as locking, versioning, or quorum. Locking involves granting exclusive or shared access to a file or a part of it, which prevents concurrent updates but reduces the concurrency and availability. Versioning involves assigning a unique identifier or a timestamp to each update of a file, which allows detecting and resolving conflicts but increases the storage and communication costs. Quorum involves requiring a minimum number of servers to agree on the state of a file, which improves the reliability and fault tolerance but reduces the performance and availability.

: https://www.techtarget.com/searchstorage/definition/distributed-file-system-DFS
: https://en.wikipedia.org/wiki/Comparison_of_distributed_file_systems
: https://cseweb.ucsd.edu/classes/sp16/cse291-e/applications/ln/lecture13.html
: https://www.geeksforgeeks.org/what-is-dfsdistributed-file-system/
: https://learn.microsoft.com/en-us/windows-server/storage/dfs-namespaces/dfs-overview



### Design issues in Distributed Shared Memory

Distributed Shared Memory (DSM) is a mechanism that allows multiple processes on different nodes to share a common logical address space and access data transparently. DSM can simplify the programming of distributed applications and improve the performance and scalability of parallel systems. However, DSM also introduces several design issues that need to be addressed, such as:

- **Granularity**: Granularity refers to the size of the unit of sharing and the unit of coherence in a DSM system. A finer granularity (such as a byte or a word) can reduce the amount of false sharing and communication overhead, but it can also increase the complexity and cost of maintaining coherence. A coarser granularity (such as a page or a segment) can simplify the coherence protocol and reduce the number of coherence messages, but it can also increase the amount of false sharing and unnecessary data transfer. Therefore, a trade-off between granularity and performance needs to be considered in the design of a DSM system.

- **Structure**: Structure refers to the organization and layout of the shared data in the memory. The structure of a DSM system can be either flat or hierarchical. A flat structure treats the shared memory as a single linear address space that can be accessed by any node. A hierarchical structure divides the shared memory into multiple regions or segments that can be mapped to different nodes or groups of nodes. A flat structure can simplify the programming and the coherence protocol, but it can also increase the contention and the communication latency. A hierarchical structure can reduce the contention and the communication latency, but it can also complicate the programming and the coherence protocol.

- **Coherence semantics**: Coherence semantics define the consistency model of a DSM system, that is, the rules and guarantees about the order and visibility of the updates to the shared data. Different coherence semantics can have different impacts on the performance and the programmability of a DSM system. For example, a strict coherence semantics (such as sequential consistency) can ensure that all nodes see the same order of updates and simplify the reasoning about the correctness of the program, but it can also impose a high synchronization and communication overhead. A relaxed coherence semantics (such as release consistency) can reduce the synchronization and communication overhead and improve the performance, but it can also introduce the possibility of data inconsistency and complicate the reasoning about the correctness of the program.

- **Scalability**: Scalability refers to the ability of a DSM system to maintain its performance and functionality as the number of nodes or the size of the shared data increases. Scalability is affected by several factors, such as the coherence protocol, the communication network, the memory allocation, and the load balancing. A scalable DSM system should be able to minimize the coherence messages, reduce the communication latency, distribute the memory and the computation evenly, and adapt to the dynamic changes in the system.

- **Heterogeneity**: Heterogeneity refers to the diversity and variability of the nodes and the network in a DSM system. Heterogeneity can arise from different aspects, such as the hardware architecture, the operating system, the network topology, the network bandwidth, the network latency, and the network reliability. Heterogeneity can pose several challenges to the design of a DSM system, such as the compatibility, the portability, the performance, and the fault tolerance. A heterogeneous DSM system should be able to support different types of nodes and networks, provide a uniform and transparent interface to the programmers, optimize the performance according to the characteristics of the nodes and the network, and handle the failures and the errors gracefully.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on the algorithm for implementation of distributed shared memory for the notes of the unit 5 - distributed resource management in the subject of distributed system.

# Algorithm for Implementation of Distributed Shared Memory

Distributed Shared Memory (DSM) is a concept that allows multiple processes running on different nodes of a distributed system to share a common virtual address space and access the same data as if they were running on a single machine with a shared physical memory. DSM can be implemented by software or hardware, or a combination of both. Some of the advantages of DSM are:

- It simplifies the programming model and reduces the need for explicit message passing among processes.
- It enables the use of existing shared memory applications and libraries on distributed systems.
- It improves the performance and scalability of distributed applications by exploiting the locality and caching of data.

There are different algorithms for implementing DSM, each with its own trade-offs and challenges. Some of the main factors that affect the design and performance of DSM algorithms are:

- The granularity of data sharing: how large are the units of data that are shared and transferred among nodes?
- The consistency model: how are the updates to the shared data propagated and synchronized among nodes?
- The coherence protocol: how are the copies of the shared data maintained and invalidated in the local caches of nodes?
- The fault tolerance: how are the failures of nodes or network handled and recovered?

In this section, we will briefly describe four basic algorithms for implementing DSM: the central server algorithm, the migration algorithm, the replication algorithm, and the invalidation algorithm. We will also mention some of the advantages and disadvantages of each algorithm.

## Central Server Algorithm

The central server algorithm is the simplest and most straightforward way of implementing DSM. In this algorithm, all the shared data is maintained by a central server node, which services the read and write requests from other nodes. The central server can also implement a consistency model and a coherence protocol to ensure the correctness and efficiency of data access. For example, the central server can use a write-through policy to update the shared data immediately after a write request, or a write-back policy to delay the update until a flush request. The central server can also use a write-invalidate policy to invalidate the local copies of the data after a write request, or a write-update policy to broadcast the updated data to all nodes.

The advantages of the central server algorithm are:

- It is easy to implement and understand.
- It provides a strong consistency model and a simple coherence protocol.
- It avoids the problems of data migration and replication, such as network congestion, data inconsistency, and cache coherence.

The disadvantages of the central server algorithm are:

- It introduces a single point of failure and a performance bottleneck in the system.
- It does not exploit the locality and caching of data, and incurs high communication overhead for every data access.
- It does not scale well with the number of nodes and the size of the shared data.

## Migration Algorithm

The migration algorithm is a variation of the central server algorithm that aims to reduce the communication overhead and improve the performance of data access. In this algorithm, instead of keeping all the shared data at the central server, the data elements can migrate to the nodes that access them. The central server still maintains the location information of each data element, and forwards the read and write requests to the appropriate nodes. The data elements can also migrate back to the central server or to other nodes, depending on the access pattern and the migration policy. For example, the migration policy can be based on the frequency, recency, or locality of data access.

The advantages of the migration algorithm are:

- It reduces the communication overhead and improves the performance of data access by exploiting the locality and caching of data.
- It balances the load and reduces the contention among nodes by distributing the shared data.
- It provides a strong consistency model and a simple coherence protocol.

The disadvantages of the migration algorithm are:

- It still introduces a single point of failure and a performance bottleneck in the central server, which maintains the location information of the shared data.
- It incurs additional communication overhead and complexity for data migration and location update.
- It may cause thrashing and instability of data access if the data elements migrate too frequently or unpredictably.

## Replication Algorithm

The replication algorithm is another variation of the central server algorithm that aims to improve the availability and reliability of data access. In this algorithm, instead of keeping a single copy of each data element at the central server or at one node, the data elements can be replicated to multiple nodes. The central server still maintains the location information



## Unit 6 - Failure Recovery in Distributed Systems

- In distributed systems, failures are inevitable and can affect the availability, consistency, and performance of the system.
- Failure recovery is the process of restoring the system to a correct and consistent state after a failure occurs.
- Failure recovery techniques can be classified into two categories: backward recovery and forward recovery.
- Backward recovery involves undoing the effects of a failure and restoring the system to a previous consistent state, such as using checkpoints, logging, or rollback.
- Forward recovery involves correcting the effects of a failure and continuing the execution from the current state, such as using redundancy, replication, or fault tolerance.
- The choice of recovery technique depends on the type and frequency of failures, the cost and complexity of recovery, and the application requirements and constraints.
- Some of the challenges and trade-offs of failure recovery in distributed systems are:
  - How to detect and diagnose failures in a timely and accurate manner.
  - How to coordinate recovery actions among multiple components and processes.
  - How to ensure consistency and correctness of the system state after recovery.
  - How to minimize the overhead and impact of recovery on the system performance and availability.
  - How to balance the trade-off between recovery speed and recovery frequency.



### Concepts in Backward and Forward Recovery

- Backward recovery and forward recovery are two techniques for restoring the system to a consistent state after a failure in a distributed system.
- A failure in a distributed system can affect one or more processes, messages, or data, and can cause inconsistency, loss of information, or incorrect results.
- Backward recovery and forward recovery have different advantages and disadvantages depending on the type, frequency, and impact of failures, and the requirements of the system.

#### Backward Recovery

- Backward recovery involves restoring the system to a previous error-free state by using checkpoints and logs.
- A checkpoint is a snapshot of the system state at a certain point in time, which can be stored locally or globally.
- A log is a record of the events or actions that occurred after a checkpoint, which can be used to undo or redo the effects of those events or actions.
- Backward recovery can be classified into three types: pessimistic, optimistic, and causal.
- Pessimistic backward recovery ensures that the system is always in a consistent state by using synchronous checkpoints and atomic actions. It has low recovery cost but high execution cost.
- Optimistic backward recovery allows the system to execute speculatively without waiting for synchronization or confirmation, and uses asynchronous checkpoints and logs. It has low execution cost but high recovery cost.
- Causal backward recovery uses causal dependency information to determine the minimum set of processes that need to roll back after a failure, and uses selective checkpoints and logs. It has moderate execution and recovery cost.

#### Forward Recovery

- Forward recovery involves correcting the system state by removing the errors or applying compensating actions, and continuing the execution from the current state.
- Forward recovery requires the system to detect and diagnose the errors, and to have a mechanism to correct them or to tolerate them.
- Forward recovery can be classified into two types: masking and non-masking.
- Masking forward recovery hides the errors from the system and the users by using redundancy, replication, or voting. It has high reliability but low efficiency.
- Non-masking forward recovery allows the errors to be visible but provides a way to recover from them by using exception handling, retrying, or alternative actions. It has low reliability but high efficiency.



### Recovery in Concurrent Systems

Recovery in concurrent systems is the process of restoring the consistency and correctness of a system after a failure or an error. Recovery is essential for distributed systems, where multiple processes or nodes may be involved in a transaction or an operation, and where failures may occur at any point.

There are two main types of recovery in concurrent systems:

- **Backward recovery**: This type of recovery involves undoing the effects of the erroneous or failed actions and restoring the system to a previous consistent state. Backward recovery requires the system to periodically record its state (such as through checkpoints or logs) and to use these records to roll back the system when a failure occurs. Backward recovery may also require the system to abort or compensate the transactions or operations that were affected by the failure. Backward recovery is suitable for systems that can tolerate some temporary inconsistency or data loss, and that have low failure rates. 

- **Forward recovery**: This type of recovery involves correcting the errors or failures without undoing the previous actions, and continuing the execution from the current state. Forward recovery requires the system to detect the errors or failures and to apply some recovery actions (such as retrying, repairing, or masking) to resolve them. Forward recovery may also require the system to coordinate with other processes or nodes to ensure the consistency and correctness of the system. Forward recovery is suitable for systems that cannot tolerate any inconsistency or data loss, and that have high failure rates. 

Some of the challenges and techniques for recovery in concurrent systems are:

- **Interaction with concurrency control**: The recovery scheme depends greatly on the concurrency control scheme that is used to ensure the serializability and isolation of the transactions or operations. For example, if the system uses locking as a concurrency control mechanism, then the recovery scheme must ensure that the locks are released or acquired properly after a failure. Similarly, if the system uses timestamps as a concurrency control mechanism, then the recovery scheme must ensure that the timestamps are consistent and updated properly after a failure. 

- **Transaction rollback**: When a transaction fails or aborts, the recovery scheme must undo the changes made by the transaction and restore the system to a consistent state. This can be done by using the undo log, which records the before-images of the data items that were modified by the transaction. The recovery scheme can use the undo log to restore the data items to their original values. Alternatively, the recovery scheme can use the redo log, which records the after-images of the data items that were modified by the transaction. The recovery scheme can use the redo log to reapply the changes made by the transaction. 

- **Checkpoints**: Checkpoints are periodic snapshots of the system state that are taken to facilitate the recovery process. Checkpoints can reduce the amount of work that needs to be done to recover the system after a failure, by limiting the number of transactions or operations that need to be rolled back or redone. Checkpoints can be taken either globally or locally, depending on the level of coordination and synchronization among the processes or nodes in the system. Checkpoints can also be taken either synchronously or asynchronously, depending on the trade-off between the performance and the consistency of the system. 

- **Restart recovery**: Restart recovery is the process of restoring the system to a consistent state after a system crash or a power failure. Restart recovery involves scanning the logs and the checkpoints to determine the transactions or operations that were committed, aborted, or in progress at the time of the failure. Restart recovery then applies the undo and redo operations to the data items that were affected by the failure, to ensure the atomicity and durability of the transactions or operations. Restart recovery may also involve resolving any deadlocks or conflicts that may have occurred due to the failure. 

- **Concurrent recovery**: Concurrent recovery is the process of recovering multiple media sets using concurrent recovery sessions. Multiple media sets are typically created when performing backups using parallel device resources. Concurrent recovery can improve the performance and efficiency of the recovery process, by reducing the recovery time and the resource utilization. Concurrent recovery requires the system to establish multiple sessions on the recovery system, and to select the recovery items that need to be recovered from each session. Concurrent recovery may also require the system to coordinate and synchronize the recovery sessions to ensure the consistency and correctness of the system.



### Obtaining consistent Checkpoints for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Failure recovery in distributed systems is the process of restoring the system to a consistent and correct state after a failure occurs.
- A failure is an event that causes a deviation from the expected behavior of the system.
- Failures can be classified into different types, such as crash failures, omission failures, timing failures, response failures, Byzantine failures, etc.
- A checkpoint is a snapshot of the system state at a certain point in time.
- Checkpoints can be used to recover from failures by rolling back the system to a previous checkpoint and resuming the execution from there.
- However, checkpoints must be consistent, meaning that they reflect a global state of the system that could have occurred during the normal execution.
- Inconsistent checkpoints may lead to incorrect or incomplete recovery, such as losing some messages, violating causality, or repeating some operations.
- Obtaining consistent checkpoints in distributed systems is challenging because of the lack of a global clock, the concurrency of processes, and the possibility of partial failures.
- There are different techniques for obtaining consistent checkpoints, such as coordinated checkpointing, uncoordinated checkpointing, and communication-induced checkpointing.
- Coordinated checkpointing requires all processes to agree on when to take a checkpoint, and to coordinate their message sending and receiving during the checkpointing.
- Uncoordinated checkpointing allows each process to take a checkpoint independently, without any synchronization with other processes.
- Communication-induced checkpointing uses piggybacking or control messages to force some processes to take checkpoints based on the causal dependencies among messages.
- Each technique has its own advantages and disadvantages, such as overhead, latency, storage, and recovery time.
- A trade-off must be made between the frequency and the cost of checkpointing, depending on the system requirements and the failure characteristics.

: Failure Recovery in Distributed Systems - 1000 Projects
: Various Failures in Distributed Systems - tutorialspoint.com
: Recovery in Distributed Systems - GeeksforGeeks



### Recovery in Distributed Database Systems

- Recovery in distributed database systems is the process of restoring the database to a consistent state after a failure, such as a site crash, a communication link failure, or a transaction abort.
- Recovery in distributed database systems is more complicated than in centralized database systems, because failures can affect multiple sites and transactions, and the system may not have a global view of the database state.
- Recovery in distributed database systems aims to maintain the atomicity and durability of distributed transactions, which means that either all or none of the subtransactions at different sites are committed, and the effects of committed transactions are permanent.
- Recovery in distributed database systems involves two main aspects: local recovery and global recovery.
  - Local recovery is the process of recovering a single site from a failure, such as a disk crash or a power outage. Local recovery involves restoring a backup copy of the database, applying the redo and undo operations from the log, and resolving the in-doubt transactions that were participating in a distributed transaction.
  - Global recovery is the process of coordinating the recovery of multiple sites that are involved in a distributed transaction, such as a two-phase commit protocol. Global recovery involves ensuring that all sites agree on the outcome of the distributed transaction, either commit or abort, and resolving any conflicts or inconsistencies that may arise due to failures.
- Recovery in distributed database systems requires the following components:
  - A logging mechanism that records the changes made by transactions to the database, both at the local and the global level. The log can be used to redo or undo the effects of transactions in case of a failure.
  - A checkpointing mechanism that periodically saves a consistent snapshot of the database to a stable storage, both at the local and the global level. The checkpoint can be used to reduce the recovery time and the amount of log processing required after a failure.
  - A commit protocol that ensures the atomicity and durability of distributed transactions, such as the two-phase commit protocol or the three-phase commit protocol. The commit protocol involves exchanging messages among the sites that participate in a distributed transaction, and deciding whether to commit or abort the transaction based on the votes of the sites.
  - A failure detection and notification mechanism that monitors the status of the sites and the communication links, and informs the other sites of any failures that occur. The failure detection and notification mechanism can be based on timeouts, heartbeats, or acknowledgments.
  - A recovery algorithm that determines how to recover the database after a failure, based on the information available from the log, the checkpoint, the commit protocol, and the failure detection and notification mechanism. The recovery algorithm can be classified into backward recovery or forward recovery, depending on whether it uses undo or redo operations to restore the database.



## Unit 7 - Fault Tolerance

Fault tolerance is the ability of a system to continue functioning correctly in the presence of failures. Fault tolerance can be achieved by using techniques such as redundancy, replication, recovery, and reconfiguration.

- Redundancy is the provision of extra components or resources that can take over the function of a failed component or resource. Redundancy can be classified into two types: static and dynamic. Static redundancy means that the redundant components are always active and ready to take over, while dynamic redundancy means that the redundant components are activated only when needed.
- Replication is the creation of multiple copies of the same data or service that can be accessed by different clients or servers. Replication can improve availability, performance, and fault tolerance of a system. Replication can be classified into two types: passive and active. Passive replication means that only one copy of the data or service is active at a time, while active replication means that all copies of the data or service are active and synchronized.
- Recovery is the process of restoring a system to a correct state after a failure. Recovery can be classified into two types: backward and forward. Backward recovery means that the system is rolled back to a previous correct state, while forward recovery means that the system is repaired or corrected to a new correct state.
- Reconfiguration is the process of changing the structure or configuration of a system to adapt to failures or changing conditions. Reconfiguration can be classified into two types: static and dynamic. Static reconfiguration means that the system is reconfigured before it is deployed or executed, while dynamic reconfiguration means that the system is reconfigured during its execution.



# Issues in Fault Tolerance for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Fault tolerance is the ability of a system to continue functioning correctly in the presence of failures.
- Fault tolerance is important for distributed systems because they consist of multiple components that may be subject to different types of failures, such as hardware failures, software failures, network failures, malicious attacks, etc .
- Fault tolerance mechanisms in distributed systems aim to detect, mask, tolerate, or recover from failures, and to maintain the consistency, availability, and reliability of the system .
- Some of the issues and challenges in fault tolerance for distributed systems are :
  - How to model and classify different types of faults and failures, and how to measure their impact on the system performance and quality of service.
  - How to design and implement fault-tolerant algorithms and protocols that can cope with various failure scenarios, such as crash failures, omission failures, timing failures, Byzantine failures, etc.
  - How to ensure the correctness and efficiency of fault-tolerant algorithms and protocols, and how to verify and test their behavior under different fault conditions.
  - How to balance the trade-offs between fault tolerance and other system properties, such as scalability, security, complexity, overhead, etc.
  - How to adapt to dynamic and heterogeneous environments, where the system configuration, workload, and failure patterns may change over time.
  - How to coordinate and cooperate with other system components and services, such as resource management, load balancing, replication, checkpointing, etc., to achieve fault tolerance.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of commit protocols for fault tolerance in distributed systems.

### Commit Protocols

- Commit protocols are used to ensure that a transaction is either executed completely or not at all, even in the presence of failures.
- Commit protocols involve multiple participants, such as the coordinator and the cohorts, who exchange messages to reach a consensus on the outcome of the transaction.
- Commit protocols can be classified into two-phase commit (2PC) and three-phase commit (3PC) protocols, depending on the number of phases involved in the consensus process.

#### Two-Phase Commit Protocol

- The 2PC protocol consists of two phases: the voting phase and the decision phase.
- In the voting phase, the coordinator sends a prepare message to all the cohorts, asking them to vote on whether they are ready to commit or abort the transaction.
- Each cohort replies with a yes or no vote, depending on its local state and the outcome of executing the transaction.
- In the decision phase, the coordinator collects all the votes and decides the final outcome of the transaction.
- If all the votes are yes, the coordinator decides to commit the transaction and sends a commit message to all the cohorts.
- If any vote is no, the coordinator decides to abort the transaction and sends an abort message to all the cohorts.
- Each cohort follows the decision of the coordinator and either commits or aborts the transaction accordingly.
- The 2PC protocol ensures atomicity and consistency of the transaction, but it has some drawbacks, such as blocking and vulnerability to failures.
- Blocking occurs when the coordinator or some cohorts fail after sending or receiving the prepare message, but before sending or receiving the commit or abort message. In this case, the other participants have to wait indefinitely for the decision of the coordinator or the votes of the cohorts, and cannot proceed with the transaction or any other transaction.
- Vulnerability to failures occurs when the coordinator or some cohorts fail after sending or receiving the commit or abort message, but before completing the transaction. In this case, the other participants may have inconsistent states of the transaction, and may need to recover from the failure and reconcile their states.

#### Three-Phase Commit Protocol

- The 3PC protocol is an extension of the 2PC protocol that aims to overcome the blocking problem by introducing a third phase: the pre-commit phase.
- In the pre-commit phase, the coordinator sends a pre-commit message to all the cohorts, indicating that it has decided to commit the transaction based on the votes received in the voting phase.
- Each cohort replies with an ack message, acknowledging the receipt of the pre-commit message.
- In the decision phase, the coordinator sends a commit message to all the cohorts, confirming the final outcome of the transaction.
- Each cohort follows the decision of the coordinator and commits the transaction accordingly.
- The 3PC protocol ensures non-blocking and atomicity of the transaction, but it has some drawbacks, such as increased message complexity and vulnerability to network partitions.
- Increased message complexity occurs because the 3PC protocol requires more messages to be exchanged than the 2PC protocol, which increases the communication overhead and latency of the transaction.
- Vulnerability to network partitions occurs when the network is split into two or more disjoint segments, and the coordinator and some cohorts are in different segments. In this case, the coordinator may decide to commit the transaction, while some cohorts may decide to abort the transaction, leading to inconsistency.



### Voting protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Voting protocols are a type of consensus protocols that allow a set of distributed nodes to agree on a common value or decision  .
- Voting protocols are useful for achieving fault tolerance in distributed systems, as they can tolerate the failure or malicious behavior of some nodes, as long as a majority of nodes are honest and reachable  .
- Voting protocols can be classified into two categories: exact voting and inexact voting .
  - Exact voting requires that all nodes agree on the same value or decision, and that the value or decision is correct according to some predefined criteria .
  - Inexact voting allows some degree of disagreement or error among the nodes, as long as the value or decision is acceptable according to some predefined criteria .
- Voting protocols can also be classified based on the number of rounds or phases they require to reach a consensus .
  - One-phase voting protocols require only one round of communication among the nodes, where each node sends its vote to a coordinator, and the coordinator decides the final value or decision based on the majority of votes .
  - Two-phase voting protocols require two rounds of communication among the nodes, where the first round is similar to one-phase voting, and the second round is used to confirm or abort the decision of the coordinator .
  - Multi-phase voting protocols require more than two rounds of communication among the nodes, where each round is used to exchange information, propose values or decisions, and reach partial agreements .
- Voting protocols can also be classified based on the level of security or fairness they provide .
  - Security refers to the ability of the voting protocol to resist attacks from malicious nodes, such as lying, cheating, or colluding .
  - Fairness refers to the ability of the voting protocol to ensure that every node has an equal chance of influencing the final value or decision, regardless of its reputation or weight .
  - Secure and fair voting protocols are desirable, but they may have trade-offs with other properties, such as efficiency, scalability, or simplicity .



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
- Some examples of dynamic voting protocols are     :
  - Weighted voting: Each replica has a weight that reflects its importance or reliability, and the total weight of all replicas is odd. A majority of weight is required to access or update the file.
  - Quorum-based voting: Each replica belongs to one or more quorums, which are subsets of replicas that have a non-empty intersection. A quorum is required to access or update the file.
  - Topological voting: Each replica is assigned a vote based on its location in the network topology, such as the distance from the root or the number of neighbors. A majority of votes is required to access or update the file.
  - Dynamic reassignment voting: Each replica can transfer its vote to another replica upon failure or disconnection, or request a vote from another replica upon recovery or reconnection. A majority of votes is required to access or update the file.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for Unit 8 - Transactions and Concurrency Control.

## Unit 8 - Transactions and Concurrency Control

- A **transaction** is a logical unit of work that consists of a sequence of database operations, such as queries, updates, inserts, and deletes.
- A transaction has four properties, known as **ACID**:
  - **Atomicity**: A transaction is either executed in its entirety or not at all. If any operation in the transaction fails, the whole transaction is aborted and the database is restored to its previous state.
  - **Consistency**: A transaction preserves the consistency of the database by ensuring that it satisfies all the integrity constraints and business rules. The database is in a consistent state before and after the transaction.
  - **Isolation**: A transaction is executed in isolation from other transactions, meaning that its intermediate results are not visible to other transactions and it is not affected by the concurrent operations of other transactions.
  - **Durability**: The effects of a committed transaction are permanent and persist even in the case of system failures or power outages. The database system ensures that the committed changes are written to the disk and can be recovered if needed.
- **Concurrency control** is the technique of managing the simultaneous execution of transactions in a multi-user database system, such that the ACID properties are maintained and the performance is optimized.
- Concurrency control can be implemented using two main approaches: **locking** and **timestamping**.
  - **Locking** is the mechanism of granting exclusive or shared access to a data item or a set of data items to a transaction, based on the type of operation it performs. A transaction must acquire a lock before accessing a data item and release it after finishing the operation. Locking can prevent concurrency problems such as lost updates, uncommitted data, and inconsistent reads, but it can also cause deadlock, starvation, and reduced concurrency.
  - **Timestamping** is the mechanism of assigning a unique identifier to each transaction based on the time of its arrival or start, and using it to order the conflicting operations of different transactions. A transaction can access a data item only if its timestamp is compatible with the timestamps of previous operations on that data item. Timestamping can avoid deadlock and starvation, but it can also cause aborts, cascading aborts, and reduced concurrency.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of transactions for the unit 8 of distributed system.

### Transactions
- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction has the following properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the operations of a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that the concurrent execution of transactions does not interfere with each other.
- Durability means that the effects of a committed transaction are permanent and survive failures.

### Transactions and Concurrency Control
- In a distributed system, transactions may span multiple sites and involve multiple processes.
- Concurrency control is the technique of ensuring that the concurrent execution of transactions preserves the ACID properties.
- Concurrency control can be implemented using locking, timestamping, or optimistic methods.
- Locking methods use locks to prevent conflicting operations on the same data item by different transactions.
- Timestamping methods assign timestamps to transactions and use them to order the operations on the data items.
- Optimistic methods allow transactions to execute without any synchronization and check for conflicts at the end of the transaction.

### Challenges and Solutions for Distributed Transactions
- Distributed transactions face some challenges such as network failures, site failures, communication delays, and inconsistent replicas.
- Some solutions for these challenges are:
  - Two-phase commit protocol: a protocol that ensures atomicity of distributed transactions by coordinating the commit or abort decision among all the participating sites.
  - Three-phase commit protocol: a protocol that improves the availability of the two-phase commit protocol by introducing a pre-commit phase that reduces the chances of blocking due to failures.
  - Distributed deadlock detection: a technique that detects and resolves deadlocks among transactions that are waiting for locks on different sites.
  - Distributed concurrency control algorithms: algorithms that extend the locking, timestamping, or optimistic methods to handle distributed transactions.



### Nested transactions for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A transaction is a sequence of operations that satisfies the ACID properties (atomicity, consistency, isolation, and durability).
- A distributed transaction is a transaction that accesses objects handled by different servers in a distributed system.
- A nested transaction is a transaction that contains subtransactions within it, which can be committed or aborted independently.
- Nested transactions can be used to improve the performance, reliability, and modularity of distributed transactions.
- Nested transactions can be classified into two types: closed nested transactions and open nested transactions.
- Closed nested transactions have the following properties:
  - The commit of a subtransaction is not visible to other transactions until the commit of the parent transaction.
  - The abort of a subtransaction causes the rollback of all its effects and the abort of the parent transaction.
  - The concurrency control and recovery mechanisms are based on the concept of conflict serializability extended to multilevel transactions.
  - The serialization graph testing is used to detect and resolve conflicts among nested transactions.
  - The two-phase commit protocol is used to coordinate the commit or abort of nested transactions across different servers.
- Open nested transactions have the following properties:
  - The commit of a subtransaction is visible to other transactions before the commit of the parent transaction.
  - The abort of a subtransaction does not affect the parent transaction or other subtransactions.
  - The concurrency control and recovery mechanisms are based on the concept of compensating actions, which are used to undo the effects of committed subtransactions in case of abort.
  - The optimistic concurrency control is used to validate the consistency of nested transactions at commit time.
  - The presumed abort protocol is used to coordinate the commit or abort of nested transactions across different servers.



# Locks for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A lock is a mechanism that allows only one of the innumerable nodes or processes to access and modify a resource or data that is being shared commonly to prevent execution of the same task twice and also maintain data integrity.
- In distributed systems, locks are used to coordinate access to a shared resource among multiple nodes or processes that may be geographically dispersed or communicate asynchronously.
- Locks can be classified into different types based on the security of lock resources, the granularity of lock resources, the duration of lock holding, and the lock acquisition protocol.
- Some of the common types of locks are:
  - Exclusive locks and shared locks: Exclusive locks allow only one node or process to access and modify a resource, while shared locks allow multiple nodes or processes to access but not modify a resource.
  - Read locks and write locks: Read locks are shared locks that allow reading a resource, while write locks are exclusive locks that allow writing a resource.
  - Binary locks and counting locks: Binary locks have only two states: locked or unlocked, while counting locks have a counter that indicates how many nodes or processes are holding the lock.
  - Pessimistic locks and optimistic locks: Pessimistic locks are acquired before accessing a resource and released after finishing the access, while optimistic locks are acquired after accessing a resource and checked for validity before committing the access.
  - Centralized locks and distributed locks: Centralized locks are managed by a single node or process that acts as a lock manager, while distributed locks are managed by multiple nodes or processes that communicate with each other using a consensus protocol.
- Locks can also be implemented using different techniques, such as:
  - Database locks: Database locks are locks that are provided by a database system to ensure the consistency and isolation of transactions. Database locks can be row-level, table-level, or database-level.
  - Redis locks: Redis locks are locks that are implemented using Redis, a key-value store that supports atomic operations and expiration. Redis locks can be implemented using the SETNX and EXPIRE commands, or using the Redlock algorithm.
  - ZooKeeper locks: ZooKeeper locks are locks that are implemented using ZooKeeper, a distributed coordination service that provides a hierarchical namespace and ephemeral nodes. ZooKeeper locks can be implemented using the sequential ephemeral nodes and the leader election pattern.



### Optimistic Concurrency Control for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- Optimistic concurrency control (OCC) is a concurrency control method applied to transactional systems such as relational database management systems and software transactional memory.
- OCC assumes that multiple transactions can frequently complete without interfering with each other, and avoids locking of data items that can reduce the performance of the system.
- OCC consists of three phases: read, validation and write.
  - In the read phase, the transaction reads the data items from the database and performs the necessary computations, but does not update the database.
  - In the validation phase, the transaction checks if any of the data items it has read have been modified by other transactions that committed after it started. If so, the transaction is aborted and restarted, otherwise it proceeds to the write phase.
  - In the write phase, the transaction updates the database with the new values of the data items it has modified.
- OCC has some advantages over locking-based concurrency control techniques, such as:
  - It avoids the overhead of acquiring and releasing locks, which can improve the performance of the system.
  - It avoids the problem of deadlock, which can occur when two or more transactions are waiting for each other to release locks.
  - It allows more concurrency, as transactions can execute without blocking each other until the validation phase.
- OCC also has some disadvantages, such as:
  - It may cause more aborts and restarts, especially when the contention for data items is high.
  - It may require more storage space, as transactions need to keep copies of the data items they have read and modified until the write phase.
  - It may not be suitable for real-time applications, as transactions may not meet their deadlines due to aborts and restarts.
- OCC can be implemented in a distributed system, where transactions may access data items stored in different nodes of the system.
  - In a distributed system, OCC requires a global validation phase, where transactions need to communicate with all the nodes they have accessed to check for conflicts.
  - A distributed OCC protocol can use different strategies to reduce the communication overhead and the number of aborts, such as:
    - Using timestamps to order transactions and detect conflicts.
    - Using locks to guarantee a failed transaction a successful second execution.
    - Using replication to increase the availability of data items and reduce the conflicts.
- OCC is a concurrency control technique that can improve the performance and concurrency of transactional systems, but it also has some limitations and challenges, especially in a distributed system    .



### Timestamp ordering for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- Timestamp ordering is a technique to ensure serializability of transactions in a distributed system.
- A transaction is a sequence of operations that must be executed atomically, i.e., either all or none of them are performed.
- Serializability is the property that the concurrent execution of transactions produces the same result as some sequential execution of them.
- Timestamp ordering assigns a unique timestamp to each transaction when it starts, and uses these timestamps to order the operations of different transactions.
- A timestamp is a logical or physical value that represents the occurrence time of an event or a message in the system.
- Logical timestamps are based on the causal relationships among events, such as Lamport timestamps , which use a logical time function that increments a counter for each event and synchronizes it with other nodes when messages are sent or received.
- Physical timestamps are based on the real time of the system clocks, such as wall-clock time or GPS time, which require clock synchronization among nodes to ensure accuracy and consistency.
- Timestamp ordering can be applied to different levels of granularity, such as transactions, operations, objects, or pages, depending on the system design and requirements.
- Timestamp ordering can be implemented in different ways, such as optimistic, pessimistic, or multiversion, depending on the system assumptions and trade-offs.
- Optimistic timestamp ordering assumes that conflicts among transactions are rare, and allows transactions to execute without checking timestamps until they commit, at which point they are validated and aborted if they violate serializability.
- Pessimistic timestamp ordering assumes that conflicts among transactions are frequent, and checks timestamps before each operation, and rejects the operation if it violates serializability.
- Multiversion timestamp ordering maintains multiple versions of each object, and assigns a timestamp to each version, and allows transactions to access the most recent version that is compatible with their timestamp, thus avoiding conflicts and aborts.



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some information that I found from the web:

### Comparison of methods for concurrency control

Concurrency control is the process of managing the simultaneous execution of transactions in a distributed system, such that the consistency and correctness of the data are preserved. There are various methods for concurrency control, each with its own advantages and disadvantages. Some of the common methods are:

- **Two-phase locking (2PL)**: This method uses locks to prevent conflicting operations on the same data item by different transactions. A transaction must acquire a lock on a data item before reading or writing it, and release the lock after finishing the operation. There are two phases in this method: the growing phase, where the transaction acquires locks and does not release any, and the shrinking phase, where the transaction releases locks and does not acquire any. 2PL ensures serializability, which means that the concurrent execution of transactions is equivalent to some serial execution. However, 2PL may cause deadlock, where two or more transactions are waiting for each other to release locks, and thus cannot proceed. 2PL also reduces concurrency, as transactions may have to wait for locks to be released by other transactions.

- **Timestamp ordering (TO)**: This method assigns a unique timestamp to each transaction, and uses the timestamp to order the operations on the same data item. A transaction can read or write a data item only if its timestamp is compatible with the timestamps of previous operations on that data item. For example, a transaction can read a data item only if its timestamp is greater than or equal to the timestamp of the last write operation on that data item. TO ensures serializability, as the concurrent execution of transactions is equivalent to the execution in timestamp order. However, TO may cause aborts, where a transaction is rejected and has to restart with a new timestamp, if its timestamp is incompatible with some previous operation. TO also requires the maintenance of timestamps for each data item and transaction, which may incur overhead.

- **Multi-version concurrency control (MVCC)**: This method allows multiple versions of the same data item to coexist, and assigns a timestamp to each version. A transaction can read or write a data item only if its timestamp is compatible with the timestamp of the version that it accesses. For example, a transaction can read a data item only if its timestamp is greater than or equal to the timestamp of the latest committed version of that data item. MVCC ensures serializability, as the concurrent execution of transactions is equivalent to the execution in timestamp order. MVCC also avoids aborts, as a transaction can always read the latest committed version of a data item, and avoids locks, as a transaction can write a new version of a data item without blocking other transactions. However, MVCC requires the storage and management of multiple versions of each data item, which may incur overhead and complexity.

- **Validation concurrency control (VCC)**: This method divides the execution of a transaction into three phases: read phase, validation phase, and write phase. In the read phase, the transaction reads the data items that it needs, but does not write anything. In the validation phase, the transaction checks whether its read set (the set of data items that it read) is still valid, i.e., whether any other transaction has written to any of the data items in the read set after the transaction started. If the read set is valid, the transaction proceeds to the write phase, where it writes the data items that it modified. Otherwise, the transaction aborts and restarts. VCC ensures serializability, as the concurrent execution of transactions is equivalent to the execution in validation order. VCC also avoids locks, as transactions do not block each other during the read and write phases. However, VCC may cause aborts, as transactions may have to restart if their read sets are invalidated by other transactions. VCC also requires the maintenance of read and write sets for each transaction, which may incur overhead.



## Unit 9 - Distributed Transactions

- A distributed transaction is a type of transaction that involves two or more network hosts, usually providing transactional resources, such as databases, message queues, file systems, etc.   
- A distributed transaction is coordinated by a transaction manager, which is responsible for creating and managing a global transaction that encompasses all the operations against the transactional resources.   
- A distributed transaction requires the following properties to ensure data consistency and reliability: atomicity, consistency, isolation, and durability (ACID).  
- Atomicity means that either all the operations in a distributed transaction are executed successfully, or none of them are. If any operation fails, the transaction manager should roll back the changes made by the other operations.  
- Consistency means that the distributed transaction preserves the integrity constraints and business rules of the data. The transaction manager should ensure that the data is in a valid state before and after the transaction.  
- Isolation means that the distributed transaction is executed independently from other concurrent transactions. The transaction manager should prevent interference and conflicts among the operations of different transactions.  
- Durability means that the effects of a distributed transaction are permanent and persistent, even in the case of failures. The transaction manager should ensure that the data is safely stored and replicated on the transactional resources.  
- A distributed transaction can be implemented using different protocols, such as two-phase commit (2PC), three-phase commit (3PC), or the saga pattern. Each protocol has its own advantages and disadvantages in terms of performance, availability, and fault tolerance.  
- Two-phase commit (2PC) is a protocol that involves two phases: prepare and commit. In the prepare phase, the transaction manager asks each transactional resource to vote on whether they are ready to commit or abort the transaction. In the commit phase, the transaction manager decides to commit or abort the transaction based on the votes, and informs each transactional resource to do the same.  
- Three-phase commit (3PC) is a protocol that involves three phases: prepare, pre-commit, and commit. In the prepare phase, the transaction manager asks each transactional resource to vote on whether they are ready to commit or abort the transaction. In the pre-commit phase, the transaction manager decides to commit or abort the transaction based on the votes, and informs each transactional resource to do the same. In the commit phase, the transaction manager confirms the commit decision to each transactional resource, and asks them to finalize the transaction.  
- The saga pattern is a protocol that involves a sequence of compensating actions. Each action is a local transaction that can be executed independently and can be undone by another action. The transaction manager coordinates the execution of the actions, and in case of a failure, it triggers the compensating actions to roll back the changes.  

: https://en.wikipedia.org/wiki/Distributed_transaction
: https://www.techopedia.com/definition/29166/distributed-transaction
: https://hazelcast.com/glossary/distributed-transaction/
: https://stackoverflow.com/questions/4217270/what-is-a-distributed-transaction



```markdown
# Flat and Nested Distributed Transactions

## Introduction

- A **distributed transaction** is a flat or nested transaction that accesses objects managed by multiple servers .
- A **flat transaction** has a single begin point and a single end point (commit or abort). It is usually simple and short-lived.
- A **nested transaction** has a hierarchical structure of subtransactions, each with its own begin and end points. It is usually complex and long-lived.
- Both flat and nested transactions require atomicity, consistency, isolation and durability (ACID) properties to be maintained across multiple servers .

## Flat Transactions

- A flat transaction can be implemented using a **two-phase commit protocol (2PC)**  .
- In 2PC, there is a **coordinator** that initiates the transaction and collects the votes from the **participants** (servers) that execute the transaction  .
- The coordinator sends a **prepare** message to all the participants, asking them to prepare to commit or abort the transaction  .
- The participants reply with a **vote** message, either **yes** (ready to commit) or **no** (ready to abort)  .
- If the coordinator receives a **yes** vote from all the participants, it sends a **commit** message to all of them, asking them to commit the transaction  .
- If the coordinator receives a **no** vote from any participant, or a timeout occurs, it sends an **abort** message to all the participants, asking them to abort the transaction  .
- The participants acknowledge the coordinator's message and release the resources held by the transaction  .
- The coordinator records the outcome of the transaction in a **log**  .

## Nested Transactions

- A nested transaction can be implemented using a **sagas** protocol .
- In sagas, a complex transaction is decomposed into a sequence of **compensatable subtransactions** .
- Each subtransaction has a **compensation action** that can undo its effects in case of a failure .
- The subtransactions are executed in a **forward** direction, committing their local effects as they go .
- If a subtransaction fails, the saga is aborted and the **backward** direction is taken, executing the compensation actions of the previous subtransactions in reverse order .
- The saga maintains the consistency of the system by ensuring that either all the subtransactions are executed or none of them are .
- The saga allows for more concurrency and flexibility than the flat transaction, as it does not require locking the resources for the entire duration of the transaction .
```



### Atomic Commit Protocols for Distributed Transactions

- A distributed transaction is a transaction that involves multiple servers or nodes in a distributed system. A distributed transaction must satisfy the ACID properties, especially the atomicity property, which means that either all the operations of the transaction are executed or none of them are.
- An atomic commit protocol is a protocol that ensures the atomicity property of a distributed transaction, even if the system or some of the nodes fail or crash. An atomic commit protocol typically involves a coordinator node and several participant nodes that execute the operations of the transaction.
- There are different types of atomic commit protocols, such as two-phase commit (2PC), three-phase commit (3PC), parallel commit, and failure-aware commit. Each protocol has its own advantages and disadvantages in terms of performance, fault tolerance, and complexity.
- Two-phase commit (2PC) is the most widely used atomic commit protocol. It consists of two phases: a prepare phase and a commit phase. In the prepare phase, the coordinator asks the participants to vote on whether they are ready to commit or abort the transaction. In the commit phase, the coordinator decides on the final outcome of the transaction based on the votes and informs the participants to either commit or abort accordingly. 2PC ensures atomicity, but it has some drawbacks, such as blocking in case of coordinator or participant failures, and high latency due to two rounds of communication.
- Three-phase commit (3PC) is an extension of 2PC that adds a pre-commit phase between the prepare and commit phases. In the pre-commit phase, the coordinator informs the participants of its decision to commit or abort, and the participants acknowledge the decision. In the commit phase, the coordinator confirms the decision and the participants finalize the transaction. 3PC avoids blocking in case of coordinator failures, but it still blocks in case of participant failures, and it has higher latency and complexity than 2PC due to three rounds of communication.
- Parallel commit is a new atomic commit protocol that reduces the latency of transactions to only one round of communication. In parallel commit, the coordinator and the participants independently decide on the outcome of the transaction based on a distributed consensus algorithm, such as Paxos or Raft. The coordinator and the participants write their provisional intents to commit or abort the transaction to a shared log, and then wait for the log to reach a quorum of replicas. Once the log reaches a quorum, the coordinator and the participants can finalize the transaction based on the majority of intents in the log. Parallel commit ensures atomicity and avoids blocking, but it requires a reliable and fast distributed consensus algorithm and a shared log.
- Failure-aware commit (FLAC) is a practical atomic commit protocol that combines the advantages of 2PC and parallel commit. FLAC uses 2PC as the default protocol, but switches to parallel commit in case of failures. FLAC also uses a failure detector to monitor the health of the nodes and to optimize the protocol parameters, such as timeouts and retries. FLAC achieves high performance and fault tolerance, but it requires a failure detector and a shared log.



# Concurrency control in distributed transactions

- Concurrency control is the process of managing the concurrent execution of transactions in a distributed database system, such that the ACID properties are preserved .
- ACID stands for Atomicity, Consistency, Isolation, and Durability, which are the desirable properties of a transaction .
- A distributed transaction is a transaction that accesses and updates data on multiple data servers that are connected by a network .
- Concurrency control in distributed transactions is more challenging than in centralized transactions, because of the issues of network communication, data replication, and failure recovery .
- There are three main approaches to concurrency control in distributed transactions: locking-based, timestamp-based, and optimistic.
- Locking-based concurrency control protocols use the concept of locking data items to prevent conflicting operations by concurrent transactions .
- Locking-based protocols can be classified into two-phase locking (2PL), rigorous 2PL, and tree-structured locking (TSL) .
- 2PL ensures serializability, but not deadlock-freedom or recoverability .
- Rigorous 2PL ensures serializability, recoverability, and avoids cascading aborts, but not deadlock-freedom .
- TSL ensures serializability, recoverability, and deadlock-freedom, but requires a hierarchical data structure .
- Timestamp-based concurrency control algorithms use a transaction’s timestamp to order conflicting operations and ensure serializability .
- Timestamp-based algorithms can be classified into basic timestamp ordering (BTO), conservative BTO, and multiversion BTO .
- BTO assigns a global timestamp to each transaction and uses it to determine the precedence of conflicting operations .
- Conservative BTO assigns a global timestamp to each transaction and uses it to determine the precedence of conflicting operations, but also checks the availability of data items before starting a transaction .
- Multiversion BTO maintains multiple versions of each data item and assigns a global timestamp to each version and each transaction, and uses them to determine the precedence of conflicting operations and the visibility of data versions .
- Optimistic concurrency control algorithms assume that conflicts are rare and allow transactions to execute without locking or checking data items, but validate them before committing .
- Optimistic algorithms can be classified into basic optimistic, optimistic with backward validation, and optimistic with forward validation .
- Basic optimistic algorithm consists of three phases: read phase, validation phase, and write phase .
- Optimistic with backward validation algorithm consists of three phases: read phase, validation phase, and write phase, but also checks the read set of a transaction against the write sets of other transactions that committed during its execution .
- Optimistic with forward validation algorithm consists of three phases: read phase, validation phase, and write phase, but also checks the write set of a transaction against the read sets of other transactions that started during its execution .
- There are also some specialized concurrency control protocols for distributed transactions, such as 2PC* for multi-microservice environments, and snapshot isolation for replicated databases.



# Distributed Deadlocks

- A **distributed deadlock** is a situation where a set of processes in a distributed system are waiting for each other to release resources, and none of them can proceed .
- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems .
- Distributed deadlocks are harder to detect, avoid, and prevent than deadlocks in centralized systems, because there is no single authority that can oversee resource allocation and process states.
- There are three main approaches to handle distributed deadlocks :
  - **Prevention**: This approach tries to ensure that deadlocks never occur by imposing some constraints on resource allocation, such as ordering, preemption, or timeouts.
  - **Avoidance**: This approach tries to avoid deadlocks by making careful decisions on resource requests, based on the current and future resource availability and process requirements, such as using the Banker's algorithm.
  - **Detection and recovery**: This approach tries to detect deadlocks after they occur and then recover from them by aborting or restarting some processes, or by releasing some resources.
- There are two main techniques to detect distributed deadlocks :
  - **Global wait-for graph**: This technique involves constructing a global graph that represents the waiting relationships among processes and resources in the system, and then checking for cycles in the graph. A cycle indicates a deadlock. The global graph can be constructed from local graphs at each node, or by a centralized coordinator that collects information from all nodes.
  - **Edge chasing**: This technique involves sending probe messages along the edges of the local wait-for graphs, and detecting cycles when a probe message returns to its originator. This technique is also known as the Chandy-Misra-Haas algorithm or the path-pushing algorithm.



### Transaction recovery for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

- A distributed transaction is a transaction that involves multiple sites or nodes in a distributed system, such as a distributed database or a microservice architecture.
- A distributed transaction must satisfy the ACID properties: atomicity, consistency, isolation, and durability.
- Atomicity means that either all the subtransactions of a distributed transaction commit or none of them do. Consistency means that the distributed transaction preserves the integrity constraints of the data. Isolation means that the distributed transaction does not interfere with other concurrent transactions. Durability means that the effects of a committed distributed transaction are permanent and survive failures.
- A failure in a distributed system can affect one or more sites or nodes, and can cause a distributed transaction to abort or become in doubt. A distributed transaction is in doubt if some of its subtransactions have committed and some have not, and the final outcome is unknown.
- Transaction recovery is the process of restoring the consistency and durability of the data after a failure in a distributed system. Transaction recovery involves detecting and resolving the in doubt transactions, as well as undoing or redoing the subtransactions that have aborted or committed.
- There are different techniques for transaction recovery in a distributed system, such as logging, shadow versions, two-phase commit protocol, and compensation transactions.
- Logging is a technique that records the changes made by a subtransaction in a log file, which can be used to undo or redo the subtransaction in case of a failure. Logging can be done locally at each site or node, or globally by a coordinator.
- Shadow versions are a technique that creates a copy of the data before a subtransaction modifies it, and keeps the original data as a backup. If the subtransaction commits, the copy becomes the current version and the original is discarded. If the subtransaction aborts, the original is restored and the copy is discarded.
- Two-phase commit protocol is a technique that coordinates the commit or abort of a distributed transaction using a coordinator and participants. The protocol has two phases: prepare and commit. In the prepare phase, the coordinator asks the participants to vote on whether they are ready to commit or not. If all the participants vote yes, the coordinator sends a commit message to all of them in the commit phase. If any participant votes no, the coordinator sends an abort message to all of them in the commit phase.
- Compensation transactions are a technique that reverses the effects of a committed subtransaction by executing another subtransaction that performs the opposite operation. Compensation transactions are useful when undoing a subtransaction is not possible or desirable, such as when the subtransaction involves external services or resources.



## Unit 10 - Replication

- Replication is the process of creating and maintaining multiple copies of the same data on different database servers.
- Replication provides benefits such as high availability, fault tolerance, load balancing, and scalability.
- Replication can also enable data distribution across different locations, platforms, or organizations.
- Replication can be classified into different types based on the direction, timing, and granularity of data transfer.
- The main types of replication are:
  - Snapshot replication: A snapshot of the data is taken at a point in time and copied to the destination server. This type of replication is suitable for static or slowly changing data.
  - Transactional replication: Each transaction that modifies the data is captured and applied to the destination server. This type of replication ensures that the data is consistent and up-to-date across the servers.
  - Merge replication: Each server can make changes to the data independently, and the changes are merged periodically or on demand. This type of replication allows for data synchronization and conflict resolution.
  - Peer-to-peer replication: Each server acts as both a source and a destination for the data, and the changes are propagated to all the servers. This type of replication enables high availability and scalability.
- Replication can be implemented using different methods or technologies, such as:
  - Log shipping: The transaction log of the source database is backed up and restored to the destination database. This method is simple and reliable, but it has a high latency and does not support read-only access to the destination database.
  - Database mirroring: The transaction log of the source database is sent and applied to the destination database in real time. This method provides high availability and automatic failover, but it does not support load balancing or multiple destinations.
  - Always On availability groups: A group of databases is replicated across multiple servers using a combination of database mirroring and failover clustering. This method provides high availability, disaster recovery, and read-only access to the secondary databases, but it requires more resources and configuration.
  - Replication services: A set of components and agents that manage the replication of data across multiple servers. This method supports various types of replication, such as snapshot, transactional, merge, and peer-to-peer, and it allows for customization and monitoring of the replication process.



### System model and group communication for replication in distributed systems

- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by exchanging messages .
- Replication is a technique to improve the availability, performance, and fault tolerance of a distributed system by creating and maintaining multiple copies of the same data or service .
- A system model is a set of assumptions and properties that describe the characteristics and behavior of a distributed system, such as the communication network, the process model, the failure model, and the timing model .
- Group communication is a form of communication between multiple processes in a distributed system that allows them to exchange messages, coordinate actions, and share state   .
- Group communication can be classified into two types: broadcast communication and multicast communication .
  - Broadcast communication is when a process sends a message to all other processes in the system, regardless of their group membership or interest .
  - Multicast communication is when a process sends a message to a subset of processes in the system, based on their group membership or interest .
- Group communication can also be characterized by the reliability and ordering guarantees it provides, such as best-effort, reliable, causal, atomic, or total order  .
  - Best-effort delivery is when a message is delivered to some or none of the intended recipients, without any guarantee of success or failure .
  - Reliable delivery is when a message is delivered to all of the intended recipients, or none of them, in case of a failure .
  - Causal delivery is when a message is delivered to all of the intended recipients in a way that preserves the causal order of events, i.e., if a message m1 causally precedes a message m2, then m1 is delivered before m2 at every process .
  - Atomic delivery is when a message is delivered to all of the intended recipients in a way that preserves the total order of messages, i.e., if a message m1 is delivered before a message m2 at one process, then m1 is delivered before m2 at every process .
  - Total order delivery is when a message is delivered to all of the intended recipients in a way that preserves the total order of messages and the sender's order of messages, i.e., if a message m1 is sent before a message m2 by the same process, then m1 is delivered before m2 at every process .
- Group communication can be implemented using various protocols and algorithms, such as flooding, gossiping, reliable broadcast, reliable multicast, causal multicast, atomic multicast, or total order multicast  .
  - Flooding is a simple protocol that sends a message to all of the neighbors of a process, and each neighbor forwards the message to its neighbors, until the message reaches all processes in the system .
  - Gossiping is a probabilistic protocol that sends a message to a random subset of neighbors of a process, and each neighbor forwards the message to another random subset of neighbors, until the message reaches a large fraction of processes in the system .
  - Reliable broadcast is a protocol that ensures that a message sent by a process is delivered to all processes in the system, or none of them, in case of a failure .
  - Reliable multicast is a protocol that ensures that a message sent by a process is delivered to all processes in a specified group, or none of them, in case of a failure .
  - Causal multicast is a protocol that ensures that a message sent by a process is delivered to all processes in a specified group in a way that preserves the causal order of events .
  - Atomic multicast is a protocol that ensures that a message sent by a process is delivered to all processes in a specified group in a way that preserves the total order of messages .
  - Total order multicast is a protocol that ensures that a message sent by a process is delivered to all processes in a specified group in a way that preserves the total order of messages and the sender's order of messages .
- Group communication can be used for replication in distributed systems, by allowing processes to share and update the state of replicated data or services, and to coordinate their actions and decisions  .



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is some content on the topic of fault-tolerant services for replication in distributed systems:

### Fault-tolerant services for replication in distributed systems

- Fault-tolerance is the ability of a system to continue functioning correctly even in the presence of failures, such as server crashes, network partitions, or malicious attacks.
- Replication is a technique to enhance fault-tolerance by creating and maintaining multiple copies of the same service or data across different nodes in a distributed system.
- Replication can improve availability, performance, and reliability of a service, but also introduces challenges such as consistency, concurrency, and coordination among replicas.
- There are two main classes of replication techniques: primary-backup replication and active replication.
  - Primary-backup replication: One replica is designated as the primary, which receives and executes all requests from clients, and updates the other replicas, called backups, asynchronously or synchronously. The backups only take over the role of the primary when the primary fails or is suspected to have failed.
  - Active replication: All replicas receive and execute the same requests from clients in the same order, and produce the same results. There is no distinction between primary and backups, and any replica can respond to clients. Active replication requires more communication and computation than primary-backup replication, but can tolerate more failures and provide faster recovery.
- The correctness criterion for replicated services is linearizability, which means that the service behaves as if there is a single copy that processes requests atomically and in the order they are received by the system. Linearizability ensures that clients see a consistent and up-to-date view of the service state, regardless of which replica they interact with.
- To achieve linearizability, replicas need to agree on the order of requests and the state of the service. This can be done by using consensus protocols, such as Paxos or Raft, or by using logical clocks, such as vector clocks or Lamport timestamps, to assign a unique and monotonically increasing identifier to each request.
- There are trade-offs between different replication techniques and consistency models, depending on the system requirements, such as latency, throughput, fault-tolerance, and scalability. For example, synchronous replication can ensure strong consistency, but may incur higher latency and lower availability than asynchronous replication, which can allow weaker consistency, such as eventual or causal consistency.



### Highly Available Services for the Notes of the Unit 10 - Replication in the Subject of Distributed System

- A highly available service is a service that can provide continuous and reliable operation despite the presence of failures in the system.
- Replication is a technique for creating and maintaining multiple copies of data or processes across different nodes in a distributed system.
- Replication can enhance the availability, performance, scalability, and fault tolerance of a service by reducing the dependency on a single point of failure or a single source of data.
- Replication can be classified into two types: eager replication and lazy replication.
  - Eager replication ensures that all the replicas are updated synchronously whenever a change occurs in the data or the process. This guarantees strong consistency and high availability, but at the cost of increased latency and reduced scalability.
  - Lazy replication allows the replicas to be updated asynchronously after a change occurs in the data or the process. This improves the latency and scalability of the system, but may result in weak consistency and temporary unavailability.
- Replication can also be classified into two modes: active replication and passive replication.
  - Active replication involves executing the same request on all the replicas simultaneously and returning the same result to the client. This ensures that the replicas are always consistent and can tolerate any number of failures, as long as one replica remains alive.
  - Passive replication involves executing the request on a primary replica and propagating the updates to the backup replicas. This reduces the overhead of executing the same request multiple times, but requires a mechanism to elect a new primary in case of a failure.
- Replication can be implemented at different levels of abstraction, such as the application level, the middleware level, or the database level.
  - Application level replication involves designing the application logic to handle replication and consistency issues. This gives the application developer more control and flexibility, but also more complexity and responsibility.
  - Middleware level replication involves using a software layer that provides replication and consistency services to the application. This simplifies the application development and hides the replication details, but also introduces some performance and compatibility overhead.
  - Database level replication involves using a database management system that supports replication and consistency features. This enables the application to use a standard database interface and benefit from the database functionality, but also limits the replication options and policies to those supported by the database system.



### Transactions with replicated data

- A transaction is a sequence of operations that transforms a consistent state of a database into another consistent state.
- Data replication is the process of copying data and storing it in different locations, such as multiple servers or nodes in a distributed system.
- The main benefits of data replication are improved availability, fault tolerance, performance, and scalability.
- The main challenges of data replication are maintaining consistency, concurrency control, and recovery .
- Consistency means that all copies of the same data should have the same value at any given time, or at least eventually converge to the same value .
- Concurrency control means that concurrent transactions on replicated data should not interfere with each other and should preserve the serializability property, which means that the final result should be the same as if the transactions executed in some serial order .
- Recovery means that the system should be able to restore the consistency and integrity of the replicated data in case of failures, such as network partitions, node crashes, or communication errors .
- There are different types and schemes of data replication, depending on the degree of replication, the location of replicas, the frequency of updates, the direction of updates, and the conflict resolution strategy  .
- The degree of replication refers to how many copies of the same data are stored in the system. It can be full replication, where every node has a copy of the entire database, or partial replication, where only some nodes have some subsets of the database .
- The location of replicas refers to where the copies of the data are stored. It can be centralized, where there is a master node that holds the primary copy of the data and other nodes have secondary copies, or decentralized, where there is no master node and every node can have a primary or secondary copy of the data .
- The frequency of updates refers to how often the replicas are synchronized with the source or the primary copy of the data. It can be synchronous, where the updates are propagated to all replicas immediately after a transaction commits, or asynchronous, where the updates are propagated to the replicas periodically or on demand .
- The direction of updates refers to who can initiate the updates on the replicated data. It can be unidirectional, where only the source or the primary copy of the data can be updated and the replicas are read-only, or bidirectional, where any replica can be updated and the updates are propagated to the source or the primary copy of the data .
- The conflict resolution strategy refers to how the system handles the situations where different replicas have different values for the same data due to concurrent or asynchronous updates. It can be based on timestamps, versions, majority voting, quorums, or application-specific rules  .
- Transactions with replicated data require special protocols and algorithms to ensure consistency, concurrency control, and recovery across the distributed system. Some examples of such protocols and algorithms are two-phase commit, three-phase commit, Paxos, Raft, primary-backup, and optimistic replication  .

