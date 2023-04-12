

# DISTRIBUTED SYSTEM

A distributed system is a system whose components are located on different networked computers, which communicate and coordinate their actions by passing messages to one another. A distributed system can also be defined as a number of independent computers linked by a network, or a computing environment in which various components are spread across multiple computers (or other computing devices) on a network.

Some of the advantages of distributed systems are:

- They can share different resources and capabilities, to provide users with a single and integrated coherent network.
- They can achieve higher performance, scalability, reliability, and availability than centralized systems.
- They can handle partial failures and recover from them without affecting the whole system.

Some of the challenges of distributed systems are:

- They have to deal with concurrency, consistency, synchronization, and replication issues.
- They have to cope with network latency, bandwidth limitations, and communication failures.
- They have to handle security, privacy, and authentication problems.

Some of the examples of distributed systems are:

- The Internet, which is a network of networks that connects millions of computers and devices across the world.
- Cloud computing, which is a model of delivering computing resources and services over the Internet on demand.
- Peer-to-peer networks, which are networks of nodes that share resources and data without a central authority or server.



## Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- The main characteristics of distributed systems are:
  - Concurrency: Multiple components can operate in parallel and interact with each other.
  - No global clock: There is no shared physical clock among the components, and the ordering of events is based on logical clocks or timestamps.
  - Independent failures: Each component can fail independently without affecting the whole system, and the system can tolerate partial failures.
  - Heterogeneity: The components can have different hardware, software, network, and data formats, and the system can handle the diversity and interoperability issues.
  - Transparency: The system can hide the complexity and diversity of the components from the users and provide a uniform interface and behavior.
- The main challenges of distributed systems are:
  - Communication: The system has to deal with network latency, bandwidth, reliability, and security issues, and provide efficient and reliable communication protocols and mechanisms.
  - Coordination: The system has to synchronize the actions and states of the components, and ensure consistency, atomicity, and durability of the data and operations.
  - Fault tolerance: The system has to detect, mask, and recover from the failures of the components, and provide availability, reliability, and resilience.
  - Scalability: The system has to cope with the increasing number of components, users, and requests, and provide performance, load balancing, and resource management.
  - Security: The system has to protect the data and operations from unauthorized access, modification, and disclosure, and provide authentication, authorization, confidentiality, integrity, and non-repudiation.



# Introduction for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

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
- A distributed system has the following advantages:
  - Resource sharing: The system can enable the sharing of hardware, software, data, and services among the components and users.
  - Performance: The system can exploit the parallelism and load balancing of the components to improve the speed and efficiency of the computation.
  - Fault tolerance: The system can use replication and redundancy of the components to increase the availability and reliability of the system.
  - Modularity: The system can be composed of modular and reusable components that can be easily added, removed, or replaced.



# Examples of Distributed Systems

A distributed system is a collection of independent computers that communicate and coordinate their actions by passing messages. The computers in a distributed system may be physically close or geographically dispersed, and they may be connected by a network or a bus. Distributed systems can provide higher performance, reliability, scalability, and availability than centralized systems.

Some examples of distributed systems are:

- **Telecommunication networks**: Telephone networks are an early example of a peer-to-peer network, where each node can initiate or receive calls. Cellular and telephone networks are forms and examples of distributed networks. They use protocols such as TCP/IP, HTTP, and SMTP to exchange data and messages .
- **Real-time systems**: Many industries use real-time systems distributed in various areas, locally and globally. For example, air traffic control systems, power grid systems, industrial control systems, and online gaming systems are all examples of real-time distributed systems. They require fast and accurate communication and synchronization among the nodes to ensure safety and quality of service .
- **Distributed database systems**: A distributed database has locations across multiple servers, physical locations, or both. The data can be replicated or partitioned to improve performance, availability, and fault tolerance. Examples of distributed database systems are Google's Bigtable, Amazon's Dynamo, and MongoDB .
- **Distributed computing systems**: A distributed computing system is a system that uses the idle resources of many computers to perform a large-scale computation or task. Examples of distributed computing systems are SETI@home, Folding@home, and Bitcoin. They use techniques such as grid computing, cloud computing, and peer-to-peer computing to distribute the workload and coordinate the results .
- **Distributed web systems**: A distributed web system is a system that uses the web as a platform for delivering services and applications. Examples of distributed web systems are web search engines, social networks, e-commerce sites, and content delivery networks. They use technologies such as web servers, web browsers, web services, and web protocols to provide scalable, reliable, and secure web applications .



# Resource sharing and the web challenges in distributed systems

A distributed system is a collection of independent computers that appears to its users as a single coherent system . Distributed systems enable resource sharing among different computers, such as software, hardware or data. Resource sharing can be achieved in different ways, such as:

- Data migration: the process of transferring data from one location to another location in the system.
- Computation migration: the process of transferring computation from one location to another location in the system.
- Service migration: the process of transferring services from one location to another location in the system.

Resource sharing in distributed systems poses several challenges, such as:

- Transparency: the property of hiding the details of the distribution of components in a shared system from the user and the application programmer, so that the system is perceived as a whole, rather than as a collection of independent components . Transparency can be classified into different types, such as:

  - Location transparency: the property of hiding the physical location of resources from the user and the application programmer.
  - Naming transparency: the property of hiding the mapping of names to resources from the user and the application programmer.
  - Replication transparency: the property of hiding the existence of multiple copies of resources from the user and the application programmer.
  - Migration transparency: the property of hiding the movement of resources from one location to another from the user and the application programmer.
  - Concurrency transparency: the property of hiding the concurrent access of resources by multiple users or processes from the user and the application programmer.
  - Failure transparency: the property of hiding the failures of resources or components from the user and the application programmer.

- Scalability: the property of a distributed system to maintain its performance and functionality when the load or the number of components increases . Scalability can be classified into different types, such as:

  - Size scalability: the property of a distributed system to support a large number of components or users.
  - Geographical scalability: the property of a distributed system to support components or users that are widely distributed across different locations.
  - Administrative scalability: the property of a distributed system to support components or users that belong to different administrative domains or organizations.

- Heterogeneity: the property of a distributed system to support different types of components or devices, such as hardware, operating systems, programming languages, data formats, etc . Heterogeneity poses challenges for interoperability, communication, security, etc.

- Fault tolerance: the property of a distributed system to continue its operation despite the failures of some of its components or resources. Fault tolerance can be achieved by using techniques such as replication, redundancy, recovery, etc.

- Security: the property of a distributed system to protect its resources and data from unauthorized access, modification, or disclosure. Security can be achieved by using techniques such as encryption, authentication, authorization, etc.

- Consistency: the property of a distributed system to ensure that all the components or users have a coherent view of the state of the system or the data. Consistency can be achieved by using techniques such as synchronization, coordination, consensus, etc.

The web is an example of a large-scale distributed system that enables resource sharing among different computers connected by the internet. The web faces many of the challenges mentioned above, such as transparency, scalability, heterogeneity, fault tolerance, security, and consistency. The web also introduces some specific challenges, such as:

- Content management: the challenge of storing, organizing, indexing, searching, and retrieving the large amount of data and information available on the web.
- Content delivery: the challenge of efficiently and reliably delivering the data and information from the web servers to the web clients, such as browsers, applications, etc.
- Content adaptation: the challenge of customizing the data and information according to the preferences, needs, and capabilities of the web clients, such as language, format, device, etc.
- Content quality: the challenge of ensuring the accuracy, relevance, timeliness, and trustworthiness of the data and information available on the web.
- Content analysis: the challenge of extracting, processing, and understanding the meaning, structure, and relationships of the data and information available on the web.
- Content creation:



# Architectural models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Architectural models are a type of system model that describe the organization and placement of components in a distributed system and their interrelationships .
- Architectural models can help to understand the design trade-offs, performance, scalability, reliability, and security of distributed systems.
- There are various architectural models that are commonly used for distributed systems, such as:
  - Client-server model: A model where one or more servers provide services to multiple clients that request them over a network. The servers are usually centralized and the clients are distributed. The clients and servers can have different hardware and software platforms. Examples of client-server systems are web applications, email systems, and online banking systems.
  - Peer-to-peer model: A model where each node in the system can act as both a client and a server, and communicate directly with other nodes without a central coordinator. The nodes are usually distributed and decentralized. The nodes can have similar or different hardware and software platforms. Examples of peer-to-peer systems are file sharing systems, distributed hash tables, and blockchain systems.
  - Broker model: A model where a broker component acts as an intermediary between clients and servers, and handles the communication, coordination, and translation of requests and responses. The broker can be centralized or distributed. The clients and servers can have different hardware and software platforms. Examples of broker systems are CORBA, Java RMI, and SOAP.
  - Service-oriented model: A model where the system is composed of loosely coupled and interoperable services that provide functionality to other services or applications through well-defined interfaces and protocols. The services can be distributed and decentralized. The services can have different hardware and software platforms. Examples of service-oriented systems are web services, RESTful APIs, and microservices.
  - Layered model: A model where the system is divided into layers of abstraction, each providing a set of services to the higher layer and using the services of the lower layer. The layers can be distributed or centralized. The layers can have different hardware and software platforms. Examples of layered systems are TCP/IP stack, OSI model, and MVC architecture.



# Fundamental Models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Fundamental models are descriptions of properties that are present in all distributed architectures  .
- They help us to understand the characteristics, challenges and trade-offs of distributed systems .
- There are three main types of fundamental models: interaction models, failure models and security models  .

## Interaction Models
- Interaction models deal with the issues of communication and coordination among processes in a distributed system  .
- They include aspects such as performance, timing, ordering and synchronization of events  .
- Some examples of interaction models are:
  - Synchronous vs. asynchronous communication: whether the sender and receiver of a message have to wait for each other or not.
  - Remote procedure call (RPC): a method of invoking a procedure on a remote machine as if it were local.
  - Publish-subscribe: a pattern of message exchange where publishers send messages to a broker and subscribers receive messages that match their interests.
  - Distributed shared memory (DSM): a model of memory access where processes can read and write to a shared virtual memory space.

## Failure Models
- Failure models specify the types of faults that can occur in a distributed system and how they affect the system's behavior  .
- They include aspects such as fault detection, fault tolerance, fault recovery and fault prevention  .
- Some examples of failure models are:
  - Crash failure: a process stops executing and does not resume.
  - Omission failure: a process fails to send or receive a message.
  - Timing failure: a process does not meet a timing constraint.
  - Byzantine failure: a process behaves arbitrarily or maliciously.

## Security Models
- Security models describe the goals and mechanisms of protecting a distributed system from unauthorized or malicious actions  .
- They include aspects such as confidentiality, integrity, availability, authentication, authorization and non-repudiation  .
- Some examples of security models are:
  - Symmetric-key cryptography: a method of encryption and decryption where the same secret key is used by both parties.
  - Public-key cryptography: a method of encryption and decryption where each party has a public key and a private key.
  - Digital signature: a way of verifying the authenticity and integrity of a message using public-key cryptography.
  - Kerberos: a protocol for authenticating users and services in a distributed system using symmetric-key cryptography and a trusted third party.



# Theoretical Foundation for Distributed System

A distributed system is a collection of independent processes that communicate with each other by exchanging messages over a network. The processes may be located on different machines, have different speeds, and operate under different failure modes. The main challenges of designing and implementing distributed systems are:

- How to achieve coordination and agreement among the processes, despite the possibility of message delays, failures, and malicious behavior.
- How to ensure consistency and correctness of the shared data and resources, despite the concurrent and asynchronous access by the processes.
- How to cope with the heterogeneity and scalability of the system, while maintaining efficiency and performance.

Some of the theoretical concepts and tools that help to address these challenges are:

- **Logical clocks**: A way of assigning logical timestamps to events and messages in a distributed system, such that the causal order of events is preserved. Logical clocks can be used to detect and resolve conflicts, synchronize processes, and implement distributed algorithms. There are different types of logical clocks, such as Lamport's scalar clocks and vector clocks.
- **Global states and snapshots**: A way of capturing a consistent view of the global state of a distributed system at a certain point in time, without stopping or synchronizing the processes. Global states and snapshots can be used to monitor and debug the system, detect global properties, and implement checkpointing and rollback recovery.
- **Distributed mutual exclusion**: A way of ensuring that only one process at a time can access a shared resource or execute a critical section of code in a distributed system. Distributed mutual exclusion can be implemented using various algorithms, such as token-based, permission-based, or quorum-based algorithms.
- **Distributed consensus**: A way of reaching agreement among a group of processes on a common value or action in a distributed system, despite the possibility of failures and asynchrony. Distributed consensus is a fundamental problem in distributed systems, as it enables coordination, fault tolerance, and replication. There are different algorithms for solving distributed consensus, such as Paxos, Raft, and Byzantine agreement.



# Limitation of Distributed System

A distributed system is a system that consists of multiple independent components that communicate with each other over a network. Distributed systems have many advantages, such as scalability, fault-tolerance, availability, and performance. However, they also face some limitations that make them challenging to design and implement. Some of the main limitations of distributed systems are:

- **Absence of a global state**: In a distributed system, there is no single point of control or coordination for the entire system. Each component has its own local state and view of the system, which may differ from the views of other components. This makes it difficult to reason about the behavior and correctness of the system, especially in the presence of concurrency, failures, and network delays. To cope with this limitation, distributed systems need to use techniques such as consensus algorithms, distributed transactions, and replication protocols to achieve some form of consistency and agreement among the components.

- **Absence of a global clock**: In a distributed system, there is no common notion of time or ordering of events across the components. Each component has its own local clock, which may not be synchronized with the clocks of other components. This makes it hard to measure and compare the durations and sequences of events in the system, and to coordinate the actions of the components. To deal with this limitation, distributed systems need to use methods such as logical clocks, vector clocks, and lamport timestamps to establish some form of causality and ordering among the events.

- **Absence of shared memory**: In a distributed system, there is no shared memory or storage that can be accessed by all the components. Each component has its own local memory or storage, which may not be consistent or coherent with the memories or storages of other components. This makes it challenging to share and update data and state in the system, and to ensure the integrity and validity of the data and state. To overcome this limitation, distributed systems need to use mechanisms such as message passing, remote procedure calls, distributed file systems, and distributed databases to exchange and manage data and state among the components.

- **Network issues**: In a distributed system, the network is a critical and unreliable component that connects the components and enables communication among them. However, the network may suffer from various issues, such as latency, bandwidth, congestion, packet loss, duplication, reordering, and partitioning. These issues can affect the performance, availability, and correctness of the system, and cause errors and failures. To handle these issues, distributed systems need to use strategies such as timeout, retry, acknowledgment, buffering, compression, encryption, and fault-tolerance to ensure the reliability and security of the communication.

- **Scalability issues**: In a distributed system, the system may need to scale up or down to meet the changing demands and requirements of the users and the environment. However, scaling a distributed system is not a trivial task, as it involves adding or removing components, balancing the load, distributing the data, and maintaining the consistency and performance of the system. To address these issues, distributed systems need to use approaches such as horizontal and vertical scaling, load balancing, sharding, caching, and elasticity to achieve the desired scalability.



# Absence of Global Clock

- A global clock is a system-wide clock that is equally accessible to all processes in a distributed system.
- A global clock can provide a common notion of time and a consistent ordering of events across different processes.
- However, a global clock is hard to realize in distributed systems due to two inherent limitations: lack of shared memory and unpredictable message delays.
- Lack of shared memory means that processes in a distributed system do not have access to a common storage that can store and update the global clock value.
- Unpredictable message delays mean that the communication channel between processes is unreliable and can introduce variable and unknown delays in message transmission.
- As a result, processes in a distributed system may have different and inaccurate views of the global clock value, and may disagree on the order of events that happened on different processes.
- The absence of a global clock poses challenges for designing and implementing distributed algorithms that require synchronization, coordination, and consistency among processes.



# Shared Memory

- Shared memory is a programming model for distributed systems that provides a virtual address space shared by all nodes in the system .
- Shared memory can be implemented by hardware or software. Hardware examples include cache coherence circuits and network interface controllers. Software examples include page-based, object-based, or tuple-based approaches.
- Shared memory has some advantages over message passing, such as:
  - It is a natural extension of the uniprocessor memory model and familiar to programmers.
  - It simplifies the communication and synchronization among processes .
  - It allows dynamic and flexible data sharing and load balancing.
- Shared memory also has some challenges and limitations, such as:
  - It requires a consistent view of the shared data among all nodes, which may incur high overhead and latency .
  - It may suffer from false sharing, coherence misses, or thrashing due to the granularity and placement of shared data .
  - It may not scale well with the number of nodes or the size of the shared data .



# Logical Clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A logical clock is a mechanism for capturing chronological and causal relationships in a distributed system  .
- A distributed system may have no physically synchronous global clock, so a logical clock allows global ordering on events from different processes in such systems .
- A logical clock is not a physical device, but a software counter that is incremented according to some rules .
- A logical clock can be used for computation analysis, distributed algorithm design, individual event tracking, and exploring computational progress.
- Some examples of logical clock algorithms are:
  - Lamport timestamps, which are monotonically increasing software counters that are updated based on the send and receive events of messages .
  - Vector clocks, which are arrays of software counters that are updated based on the send and receive events of messages and the causal dependencies among them  .
  - Matrix clocks, which are matrices of software counters that are updated based on the send and receive events of messages and the causal and concurrent dependencies among them.
- A logical clock must satisfy the following property: if event A causally precedes event B, then the logical clock value of A is less than the logical clock value of B  .
- A logical clock may not satisfy the following property: if event A and event B are concurrent, then the logical clock values of A and B are incomparable  .
- A logical clock may not reflect the real-time order of events, as different processes may have different clock rates and delays .
- A logical clock can be implemented by using message passing protocols, synchronization algorithms, or consensus algorithms  .



# Lamport's Logical Clocks

- Lamport's logical clocks are a way of ordering events in a distributed system without relying on physical clocks.
- Lamport's logical clocks are based on the concept of **happens-before** relation, denoted by `->`, which defines a partial order among events.
- If `a` and `b` are events on the same process, then `a -> b` if `a` occurs before `b` based on the local clock.
- If `a` is the event of sending a message by one process and `b` is the event of receiving that message by another process, then `a -> b`.
- If `a -> b` and `b -> c`, then `a -> c`.
- Two events `a` and `b` are **concurrent**, denoted by `a || b`, if neither `a -> b` nor `b -> a`.
- Lamport's logical clocks assign a numerical value, called a **timestamp**, to each event that occurs in the system, such that if `a -> b`, then the timestamp of `a` is less than the timestamp of `b`.
- A Lamport logical clock is a numerical software counter value maintained in each process. Conceptually, this logical clock can be thought of as a clock that only has meaning in relation to messages moving between processes.
- When a process receives a message, it re-synchronizes its logical clock with that sender by taking the maximum of its own clock value and the timestamp in the message, and then incrementing it by one.
- When a process sends a message, it increments its logical clock by one and attaches the updated timestamp to the message.
- Lamport's logical clocks ensure that the timestamps reflect the happens-before relation, but they do not guarantee that concurrent events have distinct timestamps.
- Lamport's logical clocks are widely used in distributed systems to provide a logical ordering of events, but they do not capture the causal dependencies among events.
- Lamport's logical clocks provide a basis for the more advanced vector clock algorithm, which can distinguish between concurrent events and preserve the causal order of events.



# Concepts in Message Passing Systems

- Message passing is a technique for invoking behavior on a computer by sending a message to a process.
- Message passing is used in distributed systems, where processes communicate by exchanging messages over a network  .
- Message passing systems provide a collection of message-based interprocess communication (IPC) protocols that hide the complexities of network protocols and heterogeneous platforms  .
- Message passing systems can be classified into two categories: synchronous and asynchronous .
  - Synchronous message passing systems require the sender and the receiver to be ready at the same time for communication. The sender blocks until the receiver acknowledges the message, and the receiver blocks until a message arrives .
  - Asynchronous message passing systems do not require the sender and the receiver to be ready at the same time for communication. The sender does not block after sending a message, and the receiver does not block if no message is available. Instead, messages are stored in buffers or queues until they are delivered .
- Message passing systems can also be classified into two types: direct and indirect .
  - Direct message passing systems require the sender and the receiver to explicitly name each other in the communication. A communication link must be established between the cooperating processes before messages can be sent .
  - Indirect message passing systems do not require the sender and the receiver to explicitly name each other in the communication. Instead, messages are sent and received through a shared entity called a mailbox or a port. A communication link is established implicitly by the processes accessing the same mailbox or port .
- Message passing systems can also be distinguished by the format and structure of the messages they support .
  - Fixed-format messages have a predefined size and layout, and are easy to implement and efficient to transmit. However, they are less flexible and expressive than variable-format messages .
  - Variable-format messages have a variable size and layout, and can contain different types of data and metadata. They are more flexible and expressive than fixed-format messages, but they are harder to implement and less efficient to transmit .
- Message passing systems can also be characterized by the reliability and ordering of the messages they deliver .
  - Reliable message passing systems guarantee that every message sent by a process will eventually be received by the intended recipient, without duplication or corruption .
  - Unreliable message passing systems do not guarantee that every message sent by a process will eventually be received by the intended recipient, or that the messages will be delivered without duplication or corruption .
  - Ordered message passing systems guarantee that messages sent by a process will be received by the intended recipient in the same order as they were sent .
  - Unordered message passing systems do not guarantee that messages sent by a process will be received by the intended recipient in the same order as they were sent .
- Message passing systems can also be evaluated by the features and properties they offer, such as scalability, performance, security, fault tolerance, transparency, and interoperability  .



# Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent and autonomous processes that communicate by exchanging messages over a network.
- A distributed system may exhibit concurrency, asynchrony, partial failure, and non-determinism.
- In a distributed system, it is important to reason about the order of events and messages, as it affects the consistency and correctness of the system.
- Causal order is a partial order relation that captures the potential causal dependencies between events and messages in a distributed system.
- Causal order is defined as follows: 
  - If event A happens before event B in the same process, then A causally precedes B, denoted as A -> B.
  - If event A is the sending of a message m and event B is the receiving of the same message m, then A causally precedes B, denoted as A -> B.
  - If A -> B and B -> C, then A -> C (transitivity).
  - If A and B are concurrent events, meaning that neither A -> B nor B -> A, then they are causally unrelated, denoted as A || B.
- Causal order is a natural and intuitive way of ordering events and messages in a distributed system, as it reflects the possible causal influences between them.
- Causal order is also useful for ensuring causal consistency, which is a weaker form of consistency than sequential consistency, but allows more concurrency and scalability.
- Causal consistency requires that if a process observes an update, then it must also observe all the updates that causally precede it.
- Causal order can be implemented by using logical clocks, such as vector clocks or matrix clocks, that encode the causal dependencies between events and messages in a distributed system.
- Causal order can also be enforced by using causal delivery protocols, such as causal broadcast or causal multicast, that ensure that messages are delivered according to their causal order.



# Total Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent entities that communicate by message passing and coordinate their actions to achieve a common goal.
- Events are the occurrences of actions or state changes in a distributed system, such as sending or receiving a message, executing a computation, or accessing a resource.
- The order of events is important for understanding the behavior and correctness of a distributed system, especially when there are concurrent or conflicting events.
- A partial order is a binary relation that satisfies three properties: reflexivity, antisymmetry, and transitivity. A partial order can be represented by a directed acyclic graph (DAG), where the nodes are the events and the edges are the order relation.
- A distributed system is said to have partial order if we can have a partial order relationship among the events in the system. For example, if two entities communicate by message passing, then the send event is said to 'happen before' the receive event, and the logical order can be established.
- A total order is a binary relation that satisfies four properties: reflexivity, antisymmetry, transitivity, and totality. A total order can be represented by a linear sequence, where the events are ordered from left to right.
- A distributed system is said to have total order if 'totality', i.e., causal relationship among all events in the system, can be established. For example, if we use some arbitrary mechanism to break ties (e.g. the ID of the process), then we can create a total order of events in a distributed system.
- Total order is very useful for distributed system implementation, as it can help ensure consistency, agreement, and fault tolerance among the entities. For example, if a system has a shared resource that can be used by only one process at a time, then a total order can help determine which process has the priority to access the resource.



# Total Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by exchanging messages.
- Events are the basic units of activity in a distributed system. An event can be a message send, a message receive, a local computation, or a failure.
- The order of events is important for understanding the behavior and correctness of a distributed system. However, due to the lack of a global clock and the uncertainty of message delays, it is not always possible to determine the exact order of events in a distributed system.
- A partial order is a relation that satisfies three properties: reflexivity, antisymmetry, and transitivity. A partial order can be used to compare events that are causally related, i.e., events that have a direct or indirect influence on each other.
- A total order is a relation that satisfies the properties of a partial order and also the property of totality, i.e., any two events can be compared. A total order can be used to compare events that are concurrent, i.e., events that have no causal relation.
- A causal order is a partial order that captures the causal dependencies among events in a distributed system. A causal order can be defined using the happened-before relation (→), which is derived from the following rules:
  - If a and b are events in the same process, and a occurs before b, then a → b.
  - If a is the sending of a message by one process and b is the receipt of the same message by another process, then a → b.
  - If a → b and b → c, then a → c.
- A total causal order is a total order that is consistent with the causal order, i.e., if a → b, then a precedes b in the total order. A total causal order can be achieved by using a logical clock, such as a Lamport clock or a vector clock, to assign timestamps to events and compare them according to the timestamps.
- A total causal order is useful for ensuring consistency and agreement among processes in a distributed system. For example, a total causal order can be used to implement a reliable broadcast service, where every process delivers the same set of messages in the same order. A total causal order can also be used to take consistent snapshots of the global state of a distributed system.



# Techniques for Message Ordering in Distributed Systems

A distributed system is a collection of independent computers that communicate with each other via messages. The order in which messages are processed determines the final outcome of the actions in any distributed system. However, message ordering is not trivial, as messages may be delayed, lost, or reordered by the network. Therefore, different techniques are needed to ensure a consistent and correct message ordering in distributed systems.

Some of the common techniques for message ordering are:

- **Non-FIFO ordering**: This is the simplest and most basic technique, where messages are processed in the order they are received, regardless of the order they were sent. This technique does not guarantee any ordering property, and may lead to inconsistent or incorrect results. For example, if a process sends two messages m1 and m2 to another process, and m1 arrives later than m2, then the receiver may process m2 before m1, which may violate the sender's intention or the application logic.

- **FIFO ordering**: This technique ensures that messages sent by the same process are processed in the order they were sent. This technique can be implemented by attaching a sequence number to each message, and buffering the messages at the receiver until they are received in order. This technique guarantees that if a process sends m1 before m2, then any other process that receives both m1 and m2 will process m1 before m2. However, this technique does not guarantee any ordering among messages sent by different processes. For example, if a process sends m1 to p1 and m2 to p2, and another process sends m3 to p2 and m4 to p1, then there is no guarantee on the order of processing m1, m2, m3, and m4 at p1 and p2.

- **Causal ordering**: This technique ensures that messages that are causally related are processed in the order they were sent. Two messages are causally related if one message is sent as a result of receiving or sending another message. For example, if a process sends m1 to p1 and m2 to p2, and p1 sends m3 to p2 after receiving m1, then m1, m2, and m3 are causally related. This technique can be implemented by using vector clocks, which are arrays of logical timestamps that track the causal dependencies among messages. This technique guarantees that if a process sends m1 before m2, and m2 causally depends on m1, then any other process that receives both m1 and m2 will process m1 before m2. However, this technique does not guarantee any ordering among messages that are not causally related. For example, if a process sends m1 to p1 and m2 to p2, and another process sends m3 to p2 and m4 to p1, and none of these messages are causally related, then there is no guarantee on the order of processing m1, m2, m3, and m4 at p1 and p2.

- **Total ordering**: This technique ensures that all messages are processed in the same order by all processes. This technique can be implemented by using a centralized sequencer, which assigns a global sequence number to each message, or by using a distributed consensus algorithm, such as Paxos or Raft, which elects a leader to order the messages. This technique guarantees that if a process sends m1 before m2, then any other process that receives both m1 and m2 will process m1 before m2, and all processes will agree on the same order of processing all messages. However, this technique is the most expensive and complex, as it requires coordination and agreement among all processes, and may incur high latency and overhead.



# Causal ordering of messages

- Causal ordering of messages is a partial ordering of messages in a distributed computing environment .
- It places a restriction on communication between processes by requiring that if the transmission of message mi to process pk necessarily preceded the transmission of message mj to the same process, then the delivery of these messages to that process must be ordered such that mi is delivered before mj  .
- Causal ordering of messages is one of the four semantics of multicast communication, namely unordered, totally ordered, causal, and sync-ordered communication.
- Multicast communication methods vary according to the message’s reliability guarantee and ordering guarantee.
- Causal ordering of messages is useful for ensuring consistency and correctness of distributed applications that depend on the causal relationships between events .
- Causal ordering of messages is not automatically guaranteed in distributed systems, because of transmission delays, network congestion, or different clock rates .
- To achieve causal ordering of messages, various algorithms and protocols have been proposed, such as vector clocks, logical clocks, Lamport timestamps, or causal multicast   .
- These algorithms and protocols use different mechanisms to track and enforce the causal dependencies between messages, such as appending timestamps, piggybacking information, or maintaining buffers   .
- Causal ordering of messages is a weaker form of ordering than total ordering or synchronous ordering, which impose a global order on all messages in the system .
- Causal ordering of messages is also stronger than FIFO ordering or unordered communication, which do not respect the causal dependencies between messages .



# Global State for the Notes of the Unit 1 - Characterization of Distributed Systems

- A **distributed system** is a collection of independent processes that communicate with each other by exchanging messages over a network.
- A **process** is an entity that can perform computation and communication.
- A **channel** is a communication link that connects two or more processes and allows them to send and receive messages.
- A **local state** of a process is the set of values of its variables and data structures at a given point in time.
- A **local state** of a channel is the sequence of messages that have been sent but not yet received on that channel.
- A **global state** of a distributed system is a collection of the local states of all the processes and channels in the system  .
- A **global state** can be used to determine properties of the distributed system, such as deadlock, termination, consistency, etc  .
- A **global state** can be recorded by taking a **snapshot** of the local states of the processes and channels at some point in time .
- A **snapshot** can be taken by using a **global state recording algorithm**, which is a protocol that specifies how the processes and channels cooperate to capture a consistent global state  .
- A **consistent global state** is one that could have occurred during the execution of the distributed system, i.e., it does not contain any causal inconsistency .
- A **causal inconsistency** is a situation where a message is received before it is sent, or a message is sent but not received, or a message is received by a process that has not yet sent any message .
- A **cut** is a partition of the set of events that have occurred in the distributed system into two subsets: past and future .
- A **consistent cut** is a cut that does not cross any message, i.e., if a message is in the past, then its sender and receiver are also in the past, and vice versa .
- A **consistent global state** is equivalent to the global state of a consistent cut .
- A **global state recording algorithm** should ensure that the snapshot is taken along a consistent cut, and that the snapshot is complete, i.e., it contains the local state of every process and channel in the system  .
- A **global state recording algorithm** can be classified into two types: **synchronous** and **asynchronous**  .
- A **synchronous global state recording algorithm** assumes that the processes and channels are synchronized by a global clock, and that the messages have bounded transmission delays  .
- A **synchronous global state recording algorithm** can take a snapshot by having each process record its local state at a predefined time, and each channel record the messages that are in transit at that time  .
- An **asynchronous global state recording algorithm** does not make any assumptions about the synchronization or the message delays in the distributed system  .
- An **asynchronous global state recording algorithm** can take a snapshot by using a **marker message**, which is a special message that initiates and propagates the snapshot process  .
- An example of an asynchronous global state recording algorithm is the **Chandy-Lamport algorithm**, which works as follows  :
  - A process that wants to initiate a snapshot sends a marker message to all its outgoing channels, and records its local state.
  - A process that receives a marker message for the first time records its local state, and sends a marker message to all its outgoing channels.
  - A process that receives a marker message after recording its local state records the state of the incoming channel as the sequence of messages received after the first marker message and before the second marker message.
  - A process that has recorded its local state and



# Termination Detection for Distributed Systems

Termination detection is the problem of determining if a distributed computation has finished. This is a fundamental and non-trivial problem in distributed systems, because no process has complete knowledge of the global state, and global time does not exist. Termination detection is useful for many applications, such as garbage collection, deadlock detection, load balancing, and fault tolerance.

One of the algorithms for termination detection is Huang's algorithm, proposed by Shing-Tsaan Huang in 1989. Huang's algorithm is based on the concept of a process' state in a distributed system. A process can be either active or idle at any given time. An active process may become idle at any time, but an idle process may only become active again upon receiving a computational message, which is a message that affects the local state of the process. A distributed computation terminates when all processes are idle and there are no computational messages in transit.

Huang's algorithm uses a special process called the controller, which initiates and coordinates the termination detection. The controller maintains a counter called the control message count (CMC), which represents the number of control messages in the system. A control message is a message that is used for termination detection, such as a probe or a reply. The controller also maintains a boolean variable called the termination flag (TF), which indicates whether the termination has been detected or not.

The algorithm works as follows:

- The controller initiates the termination detection by sending a probe message to each process in the system. The probe message contains the current value of the CMC. The controller also sets the TF to false and increments the CMC by the number of probes sent.
- When a process receives a probe message, it records the value of the CMC in the probe as its local CMC. It also records its current state (active or idle) and the number of computational messages it has sent since receiving the probe. If the process is idle and has not sent any computational messages, it sends a reply message to the controller with its local CMC. The process also increments its local CMC by the number of replies sent.
- When the controller receives a reply message, it decrements the CMC by one. If the CMC becomes zero and the TF is false, the controller sets the TF to true and announces the termination to all processes.
- If a process becomes active after receiving a probe message, it sends a new probe message to each process in the system with its updated local CMC. The process also increments its local CMC by the number of probes sent.
- If a process receives a new probe message, it compares the value of the CMC in the probe with its local CMC. If the probe's CMC is greater than the local CMC, the process updates its local CMC to the probe's CMC and repeats the steps above. If the probe's CMC is less than or equal to the local CMC, the process discards the probe message.

The algorithm guarantees that the termination is detected correctly and eventually, as long as the following conditions are met:

- The communication channels are reliable and FIFO.
- The processes do not fail or recover during the termination detection.
- The controller does not initiate a new termination detection before the previous one is completed.

The algorithm has the following properties:

- The algorithm is distributed, as each process participates in the termination detection and maintains its own local CMC.
- The algorithm is efficient, as the number of control messages is proportional to the number of processes and the number of state changes.
- The algorithm is non-intrusive, as the computational messages are not modified or delayed by the termination detection.



# Unit 2 - Distributed Mutual Exclusion

- Distributed mutual exclusion is a fundamental problem in distributed computing systems .
- It ensures that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner  .
- It prevents race conditions, which are situations where the outcome of a computation depends on the relative timing of events.
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion. Message passing is the sole means for implementing distributed mutual exclusion .
- There are three basic approaches for implementing distributed mutual exclusion:
  - Token-based algorithms: A process can enter the critical section only if it possesses a unique token. The token is passed among the processes in a predefined order or based on some request-reply scheme.
  - Permission-based algorithms: A process can enter the critical section only if it obtains permission from all or a subset of other processes in the system. The permission is granted or denied based on some logical or physical clock values or some priority scheme.
  - Quorum-based algorithms: A process can enter the critical section only if it obtains permission from a majority or a quorum of processes in the system. The quorum is defined based on some voting scheme or some graph-theoretic properties.
- The performance of distributed mutual exclusion algorithms can be measured by the following metrics:
  - Message complexity: The number of messages exchanged per critical section entry.
  - Synchronization delay: The time elapsed between the instant a process requests to enter the critical section and the instant it is allowed to do so, assuming that no other process is in the critical section.
  - Response time: The time elapsed between the instant a process requests to enter the critical section and the instant it actually enters the critical section, assuming that no other process is in the critical section.
  - System throughput: The number of times the critical section is executed per unit time in the system.



# Classification of distributed mutual exclusion

Distributed mutual exclusion is a problem of ensuring that only one process in a distributed system can access a shared resource or data at a time. It is a fundamental requirement for achieving consistency, coordination and synchronization among the processes.

There are three basic approaches for implementing distributed mutual exclusion:

- Token-based approach
- Non-token based approach
- Quorum-based approach

## Token-based approach

In this approach, a unique token is shared among the sites or processes in the system. A site is allowed to enter its critical section (CS) if it possesses the token. Mutual exclusion is ensured because the token is unique and only one site can have it at a time. The token is passed from one site to another according to some predefined order or algorithm. Some examples of token-based algorithms are:

- Suzuki-Kasami algorithm
- Raymond's algorithm
- Singhal's heuristic algorithm

The advantages of token-based approach are:

- It is simple and easy to implement
- It does not require any knowledge of the global state of the system
- It does not generate any unnecessary messages for requesting or granting access to the CS

The disadvantages of token-based approach are:

- It may cause starvation if the token is lost or delayed
- It may cause performance degradation if the token is far away from the requesting site
- It may cause deadlock if the token is held by a faulty or malicious site

## Non-token based approach

In this approach, a site does not need to possess a token to enter its CS. Instead, it sends a request message to all other sites in the system and waits for their replies. A site is allowed to enter its CS if it receives a reply or an acknowledgment from all other sites. Some examples of non-token based algorithms are:

- Lamport's algorithm
- Ricart-Agrawala algorithm
- Maekawa's algorithm

The advantages of non-token based approach are:

- It does not depend on the existence or availability of a token
- It does not cause starvation or deadlock due to token loss or delay
- It can achieve lower response time and higher throughput than token-based approach

The disadvantages of non-token based approach are:

- It requires more messages and communication overhead than token-based approach
- It requires some knowledge of the global state of the system, such as the number and identity of the sites
- It may cause unnecessary blocking or waiting if some sites are slow or faulty

## Quorum-based approach

In this approach, a site does not need to communicate with all other sites in the system to enter its CS. Instead, it communicates with a subset of sites, called a quorum, that has enough voting power to grant access to the CS. A site is allowed to enter its CS if it receives a majority of votes from the quorum. Some examples of quorum-based algorithms are:

- Majority voting algorithm
- Tree-based algorithm
- Grid-based algorithm

The advantages of quorum-based approach are:

- It reduces the number of messages and communication overhead than non-token based approach
- It allows some degree of concurrency and fault tolerance among the sites
- It can adapt to dynamic changes in the system, such as site addition or deletion

The disadvantages of quorum-based approach are:

- It requires a careful design and selection of the quorum to ensure mutual exclusion and deadlock freedom
- It may cause performance degradation if the quorum is too large or too small
- It may cause inconsistency or violation of mutual exclusion if the quorum overlaps with other quorums



# Requirement of mutual exclusion theorem for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM

- Mutual exclusion is a concurrency control property which is introduced to prevent race conditions.
- Race conditions occur when multiple processes access a shared resource or data simultaneously and at least one of them modifies it.
- Mutual exclusion ensures that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner .
- Mutual exclusion in a distributed system states that only one process is allowed to execute the critical section (CS) at any given time .
- A critical section is a piece of code that accesses or modifies a shared resource or data.
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion .
- Message passing is the sole means for implementing distributed mutual exclusion .
- There are three basic approaches for implementing distributed mutual exclusion:
  - Token-based algorithms: A process can enter the CS only if it possesses a unique token that is passed among the processes in a logical ring or a tree.
  - Permission-based algorithms: A process can enter the CS only if it receives permission messages from all or a subset of other processes in the system.
  - Quorum-based algorithms: A process can enter the CS only if it receives permission messages from a majority or a weighted majority of other processes in the system.
- The requirement of mutual exclusion theorem is to ensure the correctness and consistency of the distributed system by avoiding race conditions, data corruption, and deadlock  .



# Token based and non token based algorithms for distributed mutual exclusion

Distributed mutual exclusion (DME) is the problem of ensuring that only one process at a time can access a shared resource in a distributed system. There are two main approaches to solve this problem: token based and non token based algorithms.

## Token based algorithms

- In token based algorithms, a unique token is shared among all the sites in the distributed system. The token represents the permission to enter the critical section. Only the site that holds the token can execute the critical section.
- Token based algorithms guarantee mutual exclusion and freedom from deadlock, but they may suffer from starvation and high message complexity.
- Examples of token based algorithms are:
  - **Suzuki-Kasami algorithm**: This is a modification of Ricart-Agrawala algorithm, a permission based algorithm that uses REQUEST and REPLY messages to ensure mutual exclusion. In Suzuki-Kasami algorithm, the token is a vector that records the number of requests made by each site. The token is passed to the site with the highest request number that has not yet executed the critical section. This algorithm reduces the number of messages from O(n^2) to O(n) per critical section execution, where n is the number of sites.
  - **Raymond's algorithm**: This is a tree based algorithm that organizes the sites into a logical tree. The token is initially held by the root of the tree. A site that wants to enter the critical section sends a REQUEST message to its parent in the tree. The parent forwards the request to its parent, and so on, until it reaches the token holder. The token holder sends the token to the site that requested it, and updates its parent pointer to that site. This algorithm reduces the number of messages to O(log n) per critical section execution, but it may cause starvation and high delay.

## Non token based algorithms

- In non token based algorithms, also known as permission based algorithms, a site communicates with a set of other sites to determine who should execute the critical section next. The site that wants to enter the critical section sends a REQUEST message to the other sites, and waits for their REPLY messages. The site can enter the critical section only after receiving all the REPLY messages.
- Non token based algorithms do not require a unique token, but they may generate more messages and cause more delay than token based algorithms. They also need to use timestamps to order the requests and resolve conflicts.
- Examples of non token based algorithms are:
  - **Lamport's algorithm**: This is a centralized algorithm that uses a coordinator site to manage the requests. The site that wants to enter the critical section sends a REQUEST message to the coordinator, along with its logical clock value. The coordinator maintains a queue of requests, ordered by their timestamps. The coordinator sends a REPLY message to the site whose request is at the head of the queue, granting it the permission to enter the critical section. This algorithm ensures mutual exclusion and fairness, but it has a single point of failure and a high message complexity of O(n) per critical section execution, where n is the number of sites.
  - **Ricart-Agrawala algorithm**: This is a decentralized algorithm that uses a totally ordered multicast to broadcast the requests. The site that wants to enter the critical section sends a REQUEST message to all the other sites, along with its logical clock value. The other sites reply with a REPLY message, either immediately or after releasing the critical section, depending on their states and timestamps. The site can enter the critical section only after receiving all the REPLY messages. This algorithm ensures mutual exclusion and fairness, but it has a high message complexity of O(n^2) per critical section execution, where n is the number of sites.



# Performance Metric for Distributed Mutual Exclusion Algorithms

Distributed mutual exclusion algorithms are algorithms that ensure that only one process at a time can access a shared resource in a distributed system. There are different types of distributed mutual exclusion algorithms, such as token-based, non-token-based, and quorum-based algorithms .

The performance of distributed mutual exclusion algorithms can be evaluated by the following four metrics :

- **Message complexity**: It is the number of messages that are required per critical section (CS) execution by a process. It measures the communication overhead of the algorithm. The lower the message complexity, the better the performance.
- **Synchronization delay**: It is the time elapsed between the moment when a process leaves the CS and the moment when the next process enters the CS. It measures the responsiveness of the algorithm. The lower the synchronization delay, the better the performance.
- **Response time**: It is the time elapsed between the moment when a process requests to enter the CS and the moment when it actually enters the CS. It measures the waiting time of the process. The lower the response time, the better the performance.
- **Throughput**: It is the number of CS executions per unit time in the system. It measures the efficiency of the algorithm. The higher the throughput, the better the performance.

The performance metrics of distributed mutual exclusion algorithms may vary depending on the best case and the worst case scenarios. For example, the best case scenario for message complexity is when the process that requests the CS already has the token or the permission, and the worst case scenario is when the process has to wait for the token or the permission from all other processes. The performance metrics may also depend on the system parameters, such as the number of processes, the network topology, the network delay, and the CS execution time. Therefore, it is important to compare the performance of different algorithms under the same system settings and assumptions.



# Unit 3 - Distributed Deadlock Detection

- A **deadlock** is a condition where a set of processes request resources that are held by other processes in the set, and none of the processes can proceed until they obtain the resources they need.
- A **distributed deadlock** is a deadlock that involves processes and resources located on different machines in a distributed system.
- **Deadlock detection** is a strategy to handle deadlocks by examining the status of the process-resource interactions for the presence of cyclic wait.
- **Deadlock resolution** is a strategy to handle deadlocks by aborting one or more deadlocked processes or preempting some resources from them.
- Deadlock detection in distributed systems can be done by two main approaches:
  - **Global wait-for graph (WFG)**: A graph that represents the waiting relationships among processes and resources in the system. A node in the WFG can be either a process or a resource, and an edge from node A to node B means that A is waiting for B. A cycle in the WFG indicates a deadlock. To construct a global WFG, each machine in the system maintains a local WFG and periodically sends it to a designated deadlock detector, which merges the local WFGs and checks for cycles.
  - **Edge chasing**: A distributed algorithm that uses probe messages to detect cycles in the WFG. A probe message contains the identity of the sender and a list of nodes visited by the message. When a process requests a resource that is held by another process, it sends a probe message to that process. When a process receives a probe message, it appends its identity to the list and forwards the message to the process that holds the resource it is waiting for. If a process receives a probe message that contains its own identity in the list, it detects a cycle and initiates deadlock resolution.



# System Model for Distributed Deadlock Detection

- A distributed system consists of a collection of nodes that communicate and cooperate to achieve a common goal.
- A node can be a process, a processor, a computer, or a cluster of computers.
- A node can request, hold, and release resources that are shared among other nodes.
- A resource can be a physical device, a file, a message, a lock, or any other entity that can be accessed by a node.
- A node can be in one of the following states: running, blocked, or aborted.
- A node is running if it is executing its instructions and not waiting for any resource.
- A node is blocked if it is waiting for a resource that is held by another node.
- A node is aborted if it is terminated due to a failure or a deadlock resolution.
- A deadlock is a situation where a set of nodes are blocked and each node in the set is waiting for a resource that is held by another node in the set.
- A deadlock can be detected by examining the wait-for graph (WFG) of the system, which is a directed graph that represents the resource requests and holds of the nodes.
- A node in the WFG corresponds to a node in the system, and an edge from node A to node B indicates that node A is waiting for a resource that is held by node B.
- A deadlock exists in the system if and only if the WFG contains a cycle.
- There are three main approaches to deadlock detection in distributed systems: centralized, hierarchical, and distributed.
- In the centralized approach, there is a designated node called the deadlock detector (DD) that is responsible for collecting the local WFGs from all the nodes and constructing the global WFG of the system. The DD periodically checks the global WFG for cycles and initiates deadlock resolution if a deadlock is found.
- In the hierarchical approach, the system is divided into clusters of nodes, and each cluster has a local DD that handles the deadlock detection within the cluster. The local DDs communicate with a global DD that handles the deadlock detection across the clusters. The global DD periodically requests the local WFGs from the local DDs and constructs the global WFG of the system. The global DD checks the global WFG for cycles and initiates deadlock resolution if a deadlock is found.
- In the distributed approach, there is no central or global DD, and each node participates in the deadlock detection process. The nodes exchange messages to construct and check the global WFG of the system. There are different algorithms for distributed deadlock detection, such as edge chasing, diffusing computation, and probe-based algorithms. These algorithms differ in the way they propagate and process the information about the resource requests and holds of the nodes.



# Resource Vs Communication Deadlocks

- A deadlock occurs when a set of processes requests resources that are already occupied by other processes in the group.
- Because each process possesses a resource and waits for another resource held by another process, the execution of two or more processes is blocked.
- There are two types of deadlock in distributed systems: resource deadlock and communication deadlock .
- In resource deadlocks, processes access resources, such as data objects in database systems and buffers in store and forward communication networks .
- A process acquires a resource before accessing it and releasing it after using it.
- A resource deadlock occurs when a process cannot acquire a resource because it is held by another process that is also waiting for a resource.
- In communication deadlocks, processes communicate by message passing, such as in client-server systems and distributed algorithms .
- A process sends a message to another process and waits for a reply before continuing its execution.
- A communication deadlock occurs when a process cannot receive a message because it is blocked by another process that is also waiting for a message.
- A communication deadlock may involve a single server or multiple servers, not all of which need to be involved in the deadlock.
- A communication deadlock is also called a message deadlock or a distributed termination problem .
- Resource deadlocks and communication deadlocks have different characteristics and require different detection and resolution techniques .
- Resource deadlocks are more common and easier to detect than communication deadlocks .
- Resource deadlocks can be detected by using wait-for graphs, timestamps, or probe messages .
- Communication deadlocks can be detected by using message sequence charts, message dependency graphs, or message passing automata .
- Resource deadlocks can be resolved by using timeouts, preemption, or deadlock avoidance algorithms .
- Communication deadlocks can be resolved by using timeouts, acknowledgments, or deadlock prevention algorithms .



# Deadlock Prevention for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process. Deadlocks can occur in distributed systems, where processes and resources are located on different machines connected by a network.

Deadlock prevention is a technique to avoid the occurrence of deadlocks by imposing some constraints on the resource allocation policies. There are two main ways to prevent deadlock in a distributed system:

- Ordered request: In this method, each resource type is assigned a certain level to maintain a resource request policy for a process. This is known as the resource allocation policy. A process can request resources only in an increasing order of levels. This prevents circular wait condition, which is one of the necessary conditions for deadlock. For example, if there are three resource types A, B, and C with levels 1, 2, and 3 respectively, then a process can request A before B, B before C, but not C before A or B. 

- Collective request: In this method, a process must request all the resources it needs at the same time before starting execution. This prevents hold and wait condition, which is another necessary condition for deadlock. A process cannot request any additional resources after it has started execution. This also reduces the fragmentation of resources, as a process will not hold any resources that it does not need. For example, if a process needs resources A, B, and C, then it must request them all together, and not request A first, then B, then C.  

These methods can prevent deadlock in a distributed system, but they also have some drawbacks. They may reduce the concurrency and efficiency of the system, as some processes may have to wait longer for resources or may not be able to use some resources at all. They may also increase the complexity and overhead of the system, as some coordination and communication among processes and machines may be required to implement the resource allocation policies. Therefore, deadlock prevention is not always the best solution for distributed systems, and other techniques such as deadlock detection and avoidance may be preferred in some cases.



# Avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- Avoidance is a technique to prevent deadlocks from occurring in a distributed system by ensuring that the system is always in a safe state.
- A safe state is a state where there is at least one sequence of resource allocation that does not lead to a deadlock.
- Avoidance requires the system to have some knowledge of the current and future resource requests and releases of each process.
- Avoidance can be implemented by using either a centralized or a decentralized approach.
- In a centralized approach, there is a single coordinator that maintains the global state of the system and decides whether to grant or deny a resource request based on a safety algorithm.
- In a decentralized approach, each site maintains its own local state and communicates with other sites to exchange information and reach a consensus on resource allocation.
- Some of the advantages of avoidance are:
  - It does not require the detection and recovery of deadlocks, which can be costly and complex.
  - It can reduce the resource utilization and the waiting time of processes by avoiding unnecessary blocking.
  - It can improve the performance and reliability of the system by avoiding deadlock situations.
- Some of the disadvantages of avoidance are:
  - It requires the system to have accurate and complete information about the resource requests and releases of each process, which may not be feasible or realistic in a distributed system.
  - It may impose a high overhead on the system due to the communication and computation involved in the safety algorithm.
  - It may be too conservative and deny some resource requests that would not actually cause a deadlock, thus reducing the concurrency and throughput of the system.



# Detection and Resolution of Distributed Deadlocks

- A distributed deadlock is a situation where a set of processes in a distributed system are waiting for each other to release resources or send messages, and none of them can proceed.
- Distributed deadlocks are more difficult to detect and resolve than centralized deadlocks, because there is no global knowledge of the system state and no central authority to coordinate the actions of the processes.
- Detection and resolution of distributed deadlocks involve two main steps: 
  - Maintenance of the wait-for graph (WFG), which is a directed graph that represents the dependencies among the processes and resources in the system.
  - Searching of the WFG for the presence of cycles (or knots), which indicate the existence of deadlocks.
- There are three main approaches to detect and resolve distributed deadlocks:
  - Centralized approach: One designated node (called the coordinator) is responsible for collecting the information about the WFG from all the other nodes, and detecting and resolving the deadlocks. This approach is simple and efficient, but it has a single point of failure and a high communication overhead.
  - Distributed approach: Each node maintains a local WFG for its own processes and resources, and exchanges messages with other nodes to detect and resolve global deadlocks. This approach is more fault-tolerant and scalable, but it has a higher complexity and a higher risk of false or phantom deadlocks.
  - Hierarchical approach: The nodes are organized into a hierarchy of clusters, and each cluster has a local coordinator that maintains a partial WFG for its own cluster, and communicates with other coordinators to detect and resolve inter-cluster deadlocks. This approach is a compromise between the centralized and distributed approaches, and it can reduce the communication and computation costs, but it still has some drawbacks such as the need for a global deadlock detection algorithm and the possibility of false or phantom deadlocks.
- Various resolutions of distributed deadlocks are as follows:
  - Deadlock resolution includes the breaking of existing wait-for dependencies in the system WFG. It involves rolling back some or all of the deadlocked processes and releasing their resources to the blocked processes in the deadlock so that they may resume execution.
  - The choice of which processes to roll back depends on several factors, such as the priority, the execution time, the number of resources, and the cost of rollback of each process.
  - Some common strategies for deadlock resolution are:
    - Victim selection: Choose one or more processes in the deadlock cycle as victims, and roll them back to a safe state or abort them completely.
    - Successive rollback: Roll back the processes in the deadlock cycle one by one, starting from the youngest or the lowest priority process, until the deadlock is resolved.
    - Global restart: Roll back all the processes in the system to their initial states, and restart them with a new order or allocation of resources.
    - Preemption: Temporarily take away some resources from some processes in the deadlock cycle, and give them to other processes, and then return them later when the deadlock is resolved.
- Deadlock detection and resolution algorithms must be resilient to failures, such as node crashes, message losses, or network partitions. Some techniques to achieve this are:
  - Checkpointing and logging: Periodically save the state of each process and the WFG to a stable storage, and use the logged information to recover from failures and resume the deadlock detection and resolution.
  - Timeout and retransmission: Use timers to detect the loss or delay of messages, and retransmit the messages if necessary.
  - Failure detection and recovery: Use heartbeat messages or other mechanisms to detect the failure of nodes or coordinators, and use backup nodes or coordinators to take over their roles and continue the deadlock detection and resolution.



# Centralized Deadlock Detection

- Centralized deadlock detection is a technique used in distributed systems to handle deadlock detection.
- According to this technique, the system maintains one global wait-for graph in a single chosen site, which is named as deadlock-detection coordinator.
- The coordinator collects information about the local wait-for graphs of each site and constructs the global wait-for graph.
- The coordinator periodically runs a deadlock detection algorithm on the global wait-for graph to identify any cycles.
- If a cycle is detected, the coordinator selects one or more processes involved in the cycle and sends abort messages to their sites.
- The advantages of this technique are simplicity and efficiency, as only one site is responsible for deadlock detection.
- The disadvantages of this technique are the single point of failure and the communication overhead, as the coordinator needs to collect and update the global wait-for graph frequently.

: https://www.exploredatabase.com/2014/06/centralized-deadlock-detection-approach-in-distributed-database.html
: https://www.javatpoint.com/deadlock-detection-in-distributed-systems
: https://people.cs.rutgers.edu/~pxk/417/notes/deadlock.html
: https://www.geeksforgeeks.org/deadlock-detection-in-distributed-systems/



# Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set.
- A distributed deadlock is a deadlock that involves processes and resources located on different machines in a distributed system.
- Distributed deadlock detection is the process of identifying and resolving deadlocks in a distributed system.
- Distributed deadlock detection involves two basic issues:
  - Detection of existing deadlocks
  - Resolution of detected deadlocks
- There are three main approaches to distributed deadlock detection:
  - Global wait-for graph (WFG) approach
  - Local wait-for graph (LWFG) approach
  - Path-pushing (edge-chasing) approach
- The global WFG approach constructs a global graph of processes and resources from local graphs at each site, and detects cycles in the global graph.
  - Advantages: simple and efficient cycle detection algorithm.
  - Disadvantages: high communication and storage overhead, single point of failure, inconsistency due to concurrency.
- The local WFG approach maintains a local graph of processes and resources at each site, and initiates a distributed cycle detection algorithm when a process is blocked.
  - Advantages: lower communication and storage overhead, no single point of failure, consistency due to synchronization.
  - Disadvantages: complex and costly cycle detection algorithm, multiple initiators, false cycles due to outdated information.
- The path-pushing approach propagates deadlock information along the wait-for edges, and detects cycles when a process receives its own information.
  - Advantages: no global or local graph construction, no cycle detection algorithm, low storage overhead, no false cycles.
  - Disadvantages: high communication overhead, multiple initiators, deadlock information may be lost or duplicated.
- The resolution of detected deadlocks can be done by aborting one or more deadlocked processes, or by preempting one or more resources from deadlocked processes.
  - The selection of processes or resources to abort or preempt can be based on criteria such as priority, age, cost, number, etc.
  - The resolution of deadlocks should be done in a coordinated and consistent manner to avoid partial or cascading aborts or preempts.



# Path Pushing Algorithms

- Path pushing algorithms are a class of distributed deadlock detection algorithms that use an explicit global wait-for graph (WFG) to detect cycles  .
- The main idea is to build a global WFG for each site of the distributed system by sending the local WFG to all the neighboring sites .
- The global WFG is updated whenever a new edge is added or deleted in the local WFG .
- A site initiates a deadlock detection by checking its global WFG for cycles. If a cycle is found, it means that a deadlock exists and the site can initiate a recovery action .
- Path pushing algorithms have the advantage of detecting deadlocks quickly and accurately, but they have the disadvantage of requiring a lot of communication and storage overhead .
- An example of a path pushing algorithm is the Chandy-Misra-Haas algorithm .



# Edge Chasing Algorithms

- Edge chasing algorithms are a class of distributed deadlock detection algorithms that use special messages called probes to detect cycles in the wait-for graph of processes.
- A probe is a triplet (i, j, k) that denotes that the deadlock detection is initiated by process P_i and the message is sent by the home site of process P_j to the home site of process P_k.
- The home site of a process is the site where the process is located and where its local wait-for graph is maintained.
- The probe message contains the information about the initiator of the deadlock detection and the path of the probe in the global wait-for graph.
- The algorithm works as follows:
  - When a process P_i initiates a deadlock detection, it sends a probe (i, i, j) to the home site of each process P_j that it is waiting for.
  - When the home site of a process P_j receives a probe (i, k, j), it checks if P_j is waiting for any other process. If not, it discards the probe. If yes, it appends P_j to the probe and forwards it to the home site of each process P_l that P_j is waiting for, as (i, j, l).
  - When the home site of a process P_i receives a probe (i, k, i), it means that a cycle involving P_i has been detected and a deadlock exists. It informs P_i about the deadlock and the processes involved in the cycle.
  - The algorithm terminates when either a deadlock is detected or all the probes are discarded.
- An example of edge chasing algorithm is the Chandy-Misra-Haas algorithm, which is designed for the AND request model, where a process waits for all the resources it requests before proceeding.
- The advantages of edge chasing algorithms are that they are simple, efficient, and scalable. They do not require global synchronization or centralized control. They only involve the processes and sites that are potentially deadlocked.
- The disadvantages of edge chasing algorithms are that they may generate a large number of probe messages, which can increase the network traffic and delay the deadlock detection. They also require each site to maintain the local wait-for graph of its processes, which can be costly in terms of memory and update overhead.



## Unit 4 - Agreement Protocols

- Agreement protocols are a class of distributed algorithms that allow a set of processes to reach a common decision or consensus, despite the possibility of failures or malicious behavior.
- Agreement protocols are useful for implementing fault-tolerant services, such as distributed databases, replicated state machines, atomic broadcast, leader election, etc.
- Agreement protocols can be classified into different types, depending on the assumptions and guarantees they provide. Some common types are:
  - **Byzantine agreement**: The processes can have arbitrary faults or behave maliciously, and the protocol guarantees that all correct processes agree on the same value, and that the value is valid (i.e., proposed by some correct process).
  - **Crash-recovery agreement**: The processes can only have crash faults or recover from them, and the protocol guarantees that all correct processes agree on the same value, and that the value is valid.
  - **Crash-stop agreement**: The processes can only have crash faults and do not recover from them, and the protocol guarantees that all correct processes agree on the same value, and that the value is valid.
  - **Uniform agreement**: The protocol guarantees that all correct processes agree on the same value, regardless of whether they are in the same component or not (i.e., the agreement is not affected by network partitions).
  - **Non-uniform agreement**: The protocol guarantees that all correct processes in the same component agree on the same value, but processes in different components may disagree (i.e., the agreement is affected by network partitions).
- Agreement protocols can also be characterized by the number of rounds or messages they require, the communication model they use (e.g., synchronous, asynchronous, partially synchronous, etc.), the failure model they tolerate (e.g., crash, omission, Byzantine, etc.), the validity condition they satisfy (e.g., validity, integrity, termination, etc.), and the complexity or performance trade-offs they involve (e.g., time, space, communication, etc.).
- Some examples of agreement protocols are:
  - **Paxos**: A crash-recovery agreement protocol that uses a leader-based approach to propose and accept values, and ensures safety (i.e., agreement and validity) in asynchronous systems, and liveness (i.e., termination) in partially synchronous systems.
  - **Raft**: A crash-stop agreement protocol that uses a leader-based approach to propose and accept values, and ensures safety and liveness in partially synchronous systems, and also provides a simple and understandable algorithm.
  - **Two-phase commit**: A crash-stop agreement protocol that uses a coordinator-based approach to propose and commit transactions, and ensures atomicity (i.e., all or nothing) and consistency (i.e., no conflicts) in synchronous systems, but may block in case of failures.
  - **Three-phase commit**: A crash-stop agreement protocol that uses a coordinator-based approach to propose and commit transactions, and ensures atomicity and consistency in asynchronous systems, and also avoids blocking in case of failures, but requires more rounds and messages.
  - **Lamport's Byzantine generals**: A Byzantine agreement protocol that uses a message-passing approach to propose and agree on a common action, and ensures safety and liveness in synchronous systems, but requires a high number of messages and rounds, and can only tolerate a minority of faulty processes.
  - **Practical Byzantine fault tolerance**: A Byzantine agreement protocol that uses a leader-based approach to propose and agree on a common value, and ensures safety and liveness in partially synchronous systems, and also provides a practical and efficient algorithm, but requires a high number of replicas and messages, and can only tolerate a minority of faulty processes.



Hello, I am Sydney, your AI assistant. I can help you with writing notes on various topics. Here is the content I have generated for the topic of Introduction for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM.

# Introduction

- Agreement protocols are a class of protocols that allow a set of processes in a distributed system to reach a consensus on some value or action.
- Consensus is a fundamental problem in distributed systems, as it enables processes to coordinate their actions and ensure consistency of shared data.
- Agreement protocols are useful for various applications, such as leader election, atomic commit, distributed transactions, fault tolerance, replication, and distributed locking.
- Agreement protocols are challenging to design and implement, as they have to cope with various sources of uncertainty and failure, such as network delays, message losses, process crashes, and malicious attacks.
- Agreement protocols are often characterized by the following properties:
  - **Validity**: The value or action agreed upon by the processes is valid, meaning that it satisfies some predefined criteria or constraints.
  - **Agreement**: All correct processes agree on the same value or action.
  - **Termination**: All correct processes eventually decide on some value or action.
  - **Integrity**: The value or action agreed upon by the processes is proposed by some process.
- Agreement protocols can be classified into different types, depending on the assumptions they make about the system model, the communication model, the failure model, and the adversary model.
- Some examples of agreement protocols are:
  - **Paxos**: A family of protocols that achieve consensus in asynchronous systems with crash failures, using a quorum-based approach and a leader-based approach.
  - **Raft**: A protocol that achieves consensus in asynchronous systems with crash failures, using a leader-based approach and a log-based approach.
  - **Two-phase commit (2PC)**: A protocol that achieves atomic commit in distributed transactions, using a coordinator-based approach and a voting-based approach.
  - **Three-phase commit (3PC)**: A protocol that achieves atomic commit in distributed transactions, using a coordinator-based approach and a voting-based approach, with an additional phase to prevent blocking in case of failures.
  - **Byzantine agreement**: A protocol that achieves consensus in asynchronous systems with Byzantine failures, using a message authentication-based approach and a majority-based approach.



# System models for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

System models are abstract representations of the properties and behaviors of distributed systems. They help to understand, design, and analyze distributed systems by simplifying the complexity and highlighting the essential aspects. System models can be classified into three types:

- **Architectural models**: describe the structure and organization of the components of a distributed system and their interactions. Architectural models can be further divided into subtypes based on the roles and responsibilities of the components, such as client-server, peer-to-peer, broker, publish-subscribe, etc.
- **Interaction models**: describe the communication and coordination mechanisms among the components of a distributed system. Interaction models can be further divided into subtypes based on the timing, ordering, and reliability of the messages, such as synchronous, asynchronous, causal, total, FIFO, etc.
- **Fault models**: describe the types and effects of failures that can occur in a distributed system and the assumptions and guarantees that can be made about them. Fault models can be further divided into subtypes based on the nature and severity of the failures, such as crash, omission, timing, response, Byzantine, etc.

Agreement protocols are algorithms that allow the components of a distributed system to reach a common decision or consensus on some value or action, despite the presence of faults and uncertainties. Agreement protocols are essential for ensuring the consistency, availability, and fault-tolerance of distributed systems. Some examples of agreement protocols are:

- **Leader election**: a protocol that allows the components of a distributed system to elect a single component as the leader or coordinator for some task or function. Leader election protocols can be based on different criteria, such as identifiers, priorities, randomization, etc.
- **Atomic commit**: a protocol that allows the components of a distributed system to agree on whether to commit or abort a transaction that involves multiple resources or databases. Atomic commit protocols can be based on different techniques, such as two-phase commit, three-phase commit, Paxos commit, etc.
- **Consensus**: a protocol that allows the components of a distributed system to agree on a single value that is proposed by one or more components. Consensus protocols can be based on different assumptions, such as synchrony, asynchrony, partial synchrony, failure detectors, etc.
- **Byzantine agreement**: a protocol that allows the components of a distributed system to agree on a single value that is proposed by one or more components, even if some of the components are faulty or malicious. Byzantine agreement protocols can be based on different techniques, such as digital signatures, cryptography, quorums, etc.



# Classification of Agreement Problem in Distributed Systems

An agreement problem in a distributed system is a problem where a set of processes need to agree on a common value or decision, despite the possibility of failures or malicious behavior of some processes. Agreement problems are fundamental to achieving fault tolerance and consistency in distributed systems.

There are different types of agreement problems, depending on the assumptions and requirements of the system. Some of the well-known agreement problems are:

- **Byzantine agreement problem**: A single value, which is to be agreed on, is initialized by an arbitrary process and all non-faulty processes have to agree on that value. The processes may have different initial values and may behave arbitrarily (including lying or sending conflicting messages). The goal is to reach agreement despite the presence of such Byzantine faults .
- **Consensus problem**: A generalization of the Byzantine agreement problem, where each process has an initial value and proposes it to the other processes. The processes have to agree on a common value, which must be one of the proposed values. The processes may fail by crashing, but not by behaving arbitrarily .
- **Interactive consistency problem**: A generalization of the consensus problem, where each process has an initial value and the processes have to agree on a vector of values, one for each process. The value for each process must be either its initial value or the default value (if the process is faulty). The processes may behave arbitrarily, as in the Byzantine agreement problem .

These problems are related by the following implications:

- If a system can solve the interactive consistency problem, it can also solve the Byzantine agreement problem and the consensus problem.
- If a system can solve the Byzantine agreement problem, it can also solve the consensus problem, but not necessarily the interactive consistency problem.
- If a system can solve the consensus problem, it cannot necessarily solve the Byzantine agreement problem or the interactive consistency problem.

The difficulty of solving these problems depends on the number of processes, the number of faulty processes, the type of communication (synchronous or asynchronous), and the type of failure (crash or Byzantine). There are various algorithms and impossibility results for different combinations of these parameters .



# Byzantine Agreement Problem

The Byzantine agreement problem is a fundamental problem in fault-tolerant distributed computing. It requires a set of parties in a distributed system to agree on a value even if some of the parties are faulty or malicious. The problem was first defined by Lamport  and inspired by a hypothetical scenario of Byzantine generals who need to coordinate an attack on an enemy city  .

Some of the main aspects of the Byzantine agreement problem are:

- The parties communicate by sending messages to each other. The messages may be delayed, lost, corrupted, or forged by faulty parties or the network.
- The parties have an initial value, which may be different for each party. The value may represent a preference, a vote, a sensor reading, or any other piece of information.
- The parties need to reach a consensus on a common value, which is the output of the agreement protocol. The consensus value should satisfy some validity and agreement properties, depending on the problem specification.
- The parties may have different types of faults, such as crashing, sending incorrect messages, or behaving arbitrarily. The faults may be permanent or transient, and may affect a known or unknown fraction of the parties.

Some of the main challenges of the Byzantine agreement problem are:

- The parties need to cope with the uncertainty and inconsistency caused by faults and network delays. They need to distinguish between honest and faulty parties, and between valid and invalid messages.
- The parties need to ensure that the consensus value is consistent with the initial values of the honest parties, and that all honest parties agree on the same value.
- The parties need to terminate the agreement protocol in a finite number of steps, and to guarantee the safety and liveness of the consensus.

Some of the main applications of the Byzantine agreement problem are:

- Distributed consensus protocols, such as Paxos, Raft, and PBFT, which are used to implement fault-tolerant replicated state machines and distributed ledgers.
- Secure multiparty computation protocols, which allow parties to jointly compute a function on their private inputs without revealing them to each other or to a third party.
- Cryptographic protocols, such as digital signatures, threshold cryptography, and secret sharing, which enable parties to perform secure and verifiable operations on shared secrets or public keys.
- Distributed systems, such as cloud computing, peer-to-peer networks, sensor networks, and blockchain networks, which rely on the coordination and cooperation of multiple parties with different interests and capabilities.



# Consensus problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- The consensus problem is the problem of getting a set of nodes in a distributed system to agree on something - it might be a value, a course of action or a decision.
- Achieving consensus allows a distributed system to act as a single entity, with every individual node aware of and in agreement with the actions of the whole of the network.
- Consensus is a general agreement on a decision made by the majority of those involved.
- Consensus is needed in a distributed system to ensure overall system reliability on top of unreliable system components.
- Consensus is also needed to coordinate distributed transactions, replicate data, elect leaders, and implement fault tolerance mechanisms.
- There are many ways in which processes in a distributed system can reach a consensus, but there is usually a trade-off between security and performance.
- The more we want our algorithm to be secure against ways in which failure can happen, the less performant it tends to become.
- Some of the common types of failures that can affect consensus are:
  - Crash failures: A process stops executing and does not resume.
  - Byzantine failures: A process behaves arbitrarily, deviating from the protocol.
  - Network failures: Messages are lost, delayed, duplicated, or reordered.
- Some of the common consensus algorithms are:
  - Two-phase commit: A coordinator process initiates a transaction and asks other processes to vote on whether to commit or abort.
  - Three-phase commit: An extension of two-phase commit that adds a pre-commit phase to avoid blocking in case of coordinator failure.
  - Paxos: A family of algorithms that use a quorum of processes to propose and accept values.
  - Raft: A simplified version of Paxos that uses a leader election and a replicated log to achieve consensus.
  - Byzantine fault tolerance: A class of algorithms that can tolerate arbitrary failures of up to a third of the processes.



# Interactive Consistency Problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- Interactive consistency is the problem in which n distinct nodes, each having its own private value, where up to t may be Byzantine, run an algorithm that allows all non-faulty nodes to infer the values of each other node  .
- Byzantine nodes are nodes that can behave arbitrarily, such as sending incorrect or conflicting messages, or remaining silent .
- Interactive consistency is a generalization of the consensus problem, where the goal is to reach agreement on a single value among all non-faulty nodes .
- Interactive consistency is also known as the Byzantine Generals Problem, where the nodes are generals who need to coordinate a common attack plan, and some of them may be traitors .
- Interactive consistency is a fundamental problem in distributed systems, especially for critical applications that rely on the combination of the opinions of multiple peers to provide a service, such as fault-tolerant control systems, distributed databases, or blockchain systems  .
- Interactive consistency is a challenging problem because it requires both reliability and security in the presence of faults and attacks  .
- Interactive consistency has been shown to be solvable only if n > 3t, where n is the total number of nodes and t is the maximum number of Byzantine nodes  .
- Interactive consistency can be solved using different algorithms, such as the original Oral Messages Algorithm by Pease, Shostak and Lamport, the Signed Messages Algorithm by Lamport, Shostak and Pease, or the Randomized Byzantine Consensus Algorithm by Rabin  .
- Interactive consistency algorithms typically involve multiple rounds of message exchange, where each node broadcasts its value and receives values from other nodes, and then applies some rules to determine the final values of all nodes  .
- Interactive consistency algorithms may require some assumptions, such as synchronous or partially synchronous communication, digital signatures, or random number generators  .
- Interactive consistency algorithms may have different performance metrics, such as communication complexity, time complexity, or resilience  .
- Interactive consistency algorithms may have different trade-offs, such as accuracy, efficiency, or scalability  .
- Interactive consistency is an active research area, where new algorithms and applications are being developed and evaluated .



# Solution to Byzantine Agreement problem

The Byzantine agreement problem is a fundamental problem in fault-tolerant distributed computing. It requires a set of parties in a distributed environment to agree on a value even if some of the parties are corrupted or faulty. The problem is also known as the Byzantine generals problem, the interactive consistency problem, or the source congruency problem.

The problem can be illustrated by the following scenario:

- Several divisions of the Byzantine army are camped outside an enemy city, each division commanded by its own general.
- The generals can communicate with one another only by messenger.
- After observing the enemy, they must decide upon a common plan of action: either attack or retreat.
- Some of the generals may be traitors, who try to prevent the loyal generals from reaching agreement.
- The generals must have an algorithm to guarantee that:
  - All loyal generals decide upon the same plan of action.
  - A small number of traitors cannot cause the loyal generals to adopt a bad plan.

The solution to the Byzantine agreement problem depends on the following factors:

- The number of parties involved, denoted by n.
- The number of faulty parties, denoted by f.
- The type of faults, such as crash, omission, or arbitrary (Byzantine).
- The type of communication, such as synchronous, asynchronous, or partially synchronous.
- The type of messages, such as signed, authenticated, or anonymous.

One of the most well-known solutions to the Byzantine agreement problem is the oral message algorithm proposed by Lamport, Shostak, and Pease. The algorithm works as follows:

- The source party broadcasts its initial value to all other parties.
- Each party that receives a value from the source party forwards it to all other parties.
- Each party repeats this process for m rounds, where m is the maximum number of faulty parties.
- After m rounds, each party decides on the value that it received from the majority of parties, or the source party's value if there is no majority.

The oral message algorithm can tolerate up to f = (n-1)/3 faulty parties, and requires n > 3f. It also assumes that the communication is synchronous and the messages are authenticated.

There are other solutions to the Byzantine agreement problem that relax some of the assumptions or improve the efficiency of the oral message algorithm. For example, some solutions use digital signatures, cryptography, randomization, or quorums to achieve Byzantine agreement under different settings . However, the Byzantine agreement problem is impossible to solve in some cases, such as when the communication is asynchronous and there is at least one faulty party.



# Application of Agreement Problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- Agreement problem is a fundamental problem in distributed systems, where a set of processes need to reach a common decision based on their individual inputs and messages exchanged with each other.
- Agreement problem has many variants, such as consensus, atomic broadcast, atomic commitment, group membership, etc. Each variant has different requirements and assumptions about the system model, such as synchrony, communication reliability, failure types, etc.
- Agreement problem is essential for many applications in distributed systems, such as fault tolerance, replication, coordination, distributed transactions, distributed databases, etc. 
- Some examples of applications that use agreement protocols are:

  - Atomic snapshot: A distributed data structure that allows processes to atomically read and write multiple shared registers. Atomic snapshot can be implemented using lattice agreement, a variant of consensus where processes agree on a value from a lattice structure .
  - Replicated state machine: A technique to implement a fault-tolerant service by replicating the service state and operations across multiple processes. Replicated state machine requires atomic broadcast, a variant of consensus where processes agree on a total order of messages .
  - Distributed commit: A protocol to ensure the atomicity and durability of a distributed transaction, where multiple processes need to agree on whether to commit or abort the transaction. Distributed commit requires atomic commitment, a variant of consensus where processes agree on a binary value .
  - Group membership: A service that maintains the membership information of a group of processes in a dynamic distributed system, where processes may join or leave the group or fail. Group membership requires a variant of consensus where processes agree on a consistent view of the group .



# Atomic Commit in Distributed Database System

- Atomic commit is an operation that applies a set of distinct changes as a single operation.
- Atomic commit ensures the atomicity property of transactions, which means either all or none of the changes are made.
- Atomic commit is of prime importance in distributed database systems, where transactions may span multiple sites and failures may occur .
- Atomic commit protocols are algorithms that coordinate the sites involved in a transaction and decide whether to commit or abort the transaction.
- Atomic commit protocols can be classified into two categories: blocking and non-blocking .
  - Blocking protocols may block the progress of some transactions if a site fails during the commit process .
  - Non-blocking protocols guarantee the progress of all transactions regardless of failures, but they may require more messages or additional assumptions .
- Some examples of blocking protocols are two-phase commit (2PC), three-phase commit (3PC), and presumed commit .
- Some examples of non-blocking protocols are presumed abort, non-blocking 2PC, and failure-aware commit (FLAC)  .
- Atomic commit protocols can be integrated with other components of distributed database systems, such as concurrency control, replication, and recovery.
- Atomic commit protocols can be optimized for different scenarios, such as read-only transactions, single-site transactions, or network partitions.



## Unit 5 - Distributed Resource Management

- Distributed resource management (DRM) is an evolving discipline consisting of a set of software, hardware, network tools, procedures and policies for enabling distributed enterprise systems to operate effectively in production.
- Distributed enterprise systems are systems that span multiple locations, platforms, and domains, and that rely on distributed computing technologies such as cloud computing, grid computing, peer-to-peer computing, and edge computing.
- DRM aims to achieve the following objectives:
  - Optimize the utilization of distributed resources, such as computing power, storage, bandwidth, and energy, by allocating them to the tasks that need them most.
  - Ensure the quality of service (QoS) of distributed applications, such as performance, availability, reliability, security, and scalability, by monitoring and controlling the resources and the network conditions.
  - Support the dynamic and heterogeneous nature of distributed environments, by adapting to the changes in resource availability, demand, and configuration, and by enabling interoperability and integration among different resource types and providers.
  - Facilitate the management of distributed resources, by providing a unified and transparent view of the resources and their status, and by automating the resource discovery, scheduling, provisioning, and configuration processes.
- DRM can be applied to various domains and scenarios, such as:
  - Distributed energy resource management system (DERMS), which is the combination of hardware and software that allows real-time communication and control across the batteries, solar panels, and other edge devices that normally lie behind-the-meter and outside grid operators’ direct control.
  - Distributed data management system (DDMS), which is the system that handles the storage, processing, and analysis of large-scale and distributed data sets, such as big data, data streams, and data lakes.
  - Distributed application management system (DAMS), which is the system that manages the deployment, execution, and coordination of distributed applications, such as web services, microservices, and serverless functions.
- DRM can be implemented in a centralized or decentralized manner, depending on the scale, complexity, and requirements of the distributed system. Centralized DRM relies on a single or a few central servers or controllers that have the global knowledge and authority of the resources and the tasks, and that make the resource management decisions for the whole system. Decentralized DRM distributes the resource management functions among multiple nodes or agents that have local or partial knowledge and authority of the resources and the tasks, and that make the resource management decisions based on local or collective information and rules.
- DRM faces several challenges and issues, such as:
  - Resource heterogeneity and diversity, which refers to the differences and variations in the types, capabilities, and characteristics of the resources, such as CPU, memory, disk, network, energy, etc.
  - Resource dynamism and uncertainty, which refers to the changes and fluctuations in the availability, demand, and configuration of the resources, due to factors such as failures, faults, maintenance, load, mobility, etc.
  - Resource scalability and elasticity, which refers to the ability to handle the increase or decrease in the number and size of the resources, and to adjust the resource allocation and provisioning accordingly.
  - Resource interoperability and integration, which refers to the ability to communicate and cooperate among different resource types and providers, and to use common standards and protocols for resource discovery, scheduling, provisioning, and configuration.
  - Resource security and privacy, which refers to the protection of the resources and the data from unauthorized access, modification, or disclosure, and to the compliance with the regulations and policies for resource usage and sharing.



# Issues in Distributed File Systems

A distributed file system (DFS) is a system that allows multiple clients to access and manipulate files stored on one or more servers over a network. DFSs aim to provide high performance, reliability, scalability, and transparency to the users and applications. However, there are many challenges and issues in designing and implementing DFSs, such as:

- **Naming and name resolution**: How to assign unique and meaningful names to the files and directories in a DFS, and how to resolve the names to the physical locations of the files. Naming schemes can be flat, hierarchical, or attribute-based, and name resolution can be done by centralized or distributed servers, or by embedding location information in the names.
- **Replication and consistency**: How to maintain multiple copies of the same file on different servers for fault tolerance, load balancing, and data locality, and how to ensure that the replicas are consistent with each other. Replication can be static or dynamic, and consistency can be strict or relaxed, depending on the application requirements and the network conditions.
- **Caching and cache coherence**: How to store frequently accessed files or file blocks in the local memory or disk of the clients or intermediate nodes, and how to invalidate or update the cached data when the original file is modified. Caching can improve the performance and reduce the network traffic, but it also introduces the problem of cache coherence, which can be handled by various protocols, such as write-through, write-back, or lease-based.
- **Concurrency control and locking**: How to coordinate the concurrent accesses and updates of the same file by multiple clients, and how to prevent or resolve conflicts and ensure data integrity. Concurrency control and locking can be done by using pessimistic or optimistic methods, such as two-phase locking, timestamp ordering, or version vectors.
- **Security and access control**: How to protect the files and directories from unauthorized or malicious accesses, modifications, or deletions, and how to enforce the access rights and permissions of different users and groups. Security and access control can be achieved by using encryption, authentication, authorization, and auditing mechanisms, such as Kerberos, public-key cryptography, or access control lists.
- **Fault tolerance and recovery**: How to detect and handle the failures of the servers, clients, or network components, and how to restore the normal operation and data consistency of the DFS. Fault tolerance and recovery can be done by using techniques such as replication, checkpointing, logging, or rollback.



# Mechanism for building distributed file systems

A distributed file system (DFS) is a file system that enables clients to access file storage from multiple hosts through a computer network as if the user was accessing local storage. Files are spread across multiple storage servers and in multiple locations, which enables users to share data and storage resources.

Some of the benefits of using a DFS are:

- Improved availability and fault tolerance: If one server fails, the files can still be accessed from another server.
- Improved scalability and performance: The load can be distributed among multiple servers, and the clients can access the files from the nearest server.
- Improved security and access control: The files can be encrypted and protected by different authentication and authorization mechanisms.
- Improved administration and management: The files can be organized into logical namespaces, and the administrators can monitor and control the file access and replication.

Some of the challenges of building a DFS are:

- Consistency and concurrency: The files need to be synchronized and updated across multiple servers, and the conflicts need to be resolved when multiple clients access or modify the same file.
- Naming and location: The files need to be named and located in a way that is transparent and convenient for the clients, and the name resolution and location service need to be efficient and reliable.
- Replication and caching: The files need to be replicated and cached to improve availability and performance, and the replication and caching policies need to be adaptive and flexible.
- Security and privacy: The files need to be secured and protected from unauthorized access and modification, and the privacy of the clients and the data need to be preserved.

Some of the mechanisms for building a DFS are:

- File service architecture: This is a client-server model, where the clients request file operations from the servers, and the servers perform the operations and return the results. The servers can be centralized or distributed, and the clients can use a remote procedure call (RPC) or a message passing interface (MPI) to communicate with the servers.
- File system semantics: This defines the behavior and guarantees of the file system, such as the consistency, concurrency, and atomicity of the file operations. The file system semantics can be strict, which means the file system behaves as if it was local, or relaxed, which means the file system allows some deviations from the local behavior to improve performance or availability.
- Naming and location service: This is a service that maps the logical names of the files to their physical locations on the servers, and provides the clients with the information to access the files. The naming and location service can use a flat or a hierarchical namespace, and can use a centralized or a distributed directory service to store and resolve the names.
- Replication and caching service: This is a service that copies and stores the files or parts of the files on multiple servers or clients, and maintains the consistency and coherence of the copies. The replication and caching service can use a push or a pull strategy, and can use a synchronous or an asynchronous mode to update the copies.
- Security and privacy service: This is a service that protects the files and the clients from unauthorized or malicious access and modification, and preserves the confidentiality and integrity of the data and the communication. The security and privacy service can use encryption, authentication, authorization, auditing, and anonymization techniques to achieve the security and privacy goals.



# Design issues in Distributed Shared Memory

Distributed Shared Memory (DSM) is a mechanism that allows multiple processes on different nodes to share a common logical address space and access data transparently. DSM can simplify the programming of distributed systems by hiding the details of inter-process communication. However, DSM also introduces several design issues that affect its performance, scalability, and correctness. Some of the main design issues in DSM are:

- **Granularity**: Granularity refers to the size of the unit of sharing and the unit of coherence in DSM. A smaller granularity (such as a byte or a word) can reduce the amount of false sharing and improve the locality of access, but it can also increase the overhead of coherence maintenance and communication. A larger granularity (such as a page or a segment) can reduce the overhead of coherence and communication, but it can also increase the amount of false sharing and waste bandwidth and memory. Therefore, choosing an appropriate granularity is a trade-off between these factors.

- **Structure**: Structure refers to the organization of the shared data in the logical address space and the mapping of the shared data to the physical memory of the nodes. The structure of DSM can be flat, hierarchical, or object-based. A flat structure treats the shared data as a single linear array and maps it to the nodes using a static or dynamic hashing function. A hierarchical structure divides the shared data into multiple regions and assigns each region to a node or a group of nodes. An object-based structure organizes the shared data into objects and allows the nodes to access them by name or reference. The structure of DSM can affect the locality, load balancing, and fault tolerance of the system.

- **Coherence semantics**: Coherence semantics define the consistency model of DSM, which specifies the rules and guarantees for the ordering and visibility of the updates to the shared data. Coherence semantics can be strict, relaxed, or weak. A strict coherence semantics requires that all the nodes see the same value for a shared variable at any time, which is equivalent to the sequential consistency model. A relaxed coherence semantics allows some nodes to see stale values for a shared variable for a limited time, which can improve the performance and scalability of the system. A weak coherence semantics does not provide any guarantees for the ordering and visibility of the updates, and relies on the programmer to use synchronization primitives to ensure the correctness of the program.

- **Coherence protocols**: Coherence protocols implement the coherence semantics of DSM by maintaining the consistency and validity of the copies of the shared data on different nodes. Coherence protocols can be classified into two categories: directory-based and broadcast-based. A directory-based protocol uses a directory to keep track of the location and state of each shared data unit, and sends messages to the nodes that have a copy of the data when an update occurs. A broadcast-based protocol uses a broadcast medium to send messages to all the nodes when an update occurs, and relies on the nodes to invalidate or update their copies of the data. Coherence protocols can also be classified into two types: write-invalidate and write-update. A write-invalidate protocol invalidates the copies of the data on other nodes when a write occurs, and requires a read miss to fetch the latest value. A write-update protocol updates the copies of the data on other nodes when a write occurs, and avoids read misses but increases the communication cost.

- **Scalability**: Scalability refers to the ability of DSM to handle the increase in the number of nodes, the size of the shared data, and the frequency of the access to the shared data. Scalability can be affected by several factors, such as the granularity, the structure, the coherence semantics, and the coherence protocols of DSM. To achieve scalability, DSM should minimize the overhead of coherence and communication, balance the load and the memory usage among the nodes, and exploit the locality and the parallelism of the access patterns.

- **Heterogeneity**: Heterogeneity refers to the diversity of the nodes in terms of the hardware architecture, the operating system, the network interface, and the communication protocol. Heterogeneity can pose several challenges for DSM, such as the compatibility, the portability, the interoperability, and the performance of the system. To cope with heterogeneity, DSM should use a common interface and a standard protocol for the communication and the coordination of the nodes, and should use a uniform representation and a consistent ordering for the shared data.



# Algorithm for Implementation of Distributed Shared Memory

Distributed Shared Memory (DSM) is a technique that allows multiple processes on different nodes of a distributed system to access a common virtual address space as if they were running on a single machine. DSM provides a high-level abstraction for interprocess communication and synchronization, and can simplify the design and development of distributed applications. However, DSM also introduces challenges such as maintaining consistency, coherence, and fault tolerance of the shared data.

There are different algorithms for implementing DSM, each with its own advantages and disadvantages. Some of the basic algorithms are:

- **Central Server Algorithm**: In this algorithm, a central server maintains all the shared data and services read and write requests from other nodes. The central server can use a page-based or an object-based approach to manage the shared data. The advantage of this algorithm is that it is simple and ensures consistency and coherence of the shared data. The disadvantage is that it introduces a single point of failure and a performance bottleneck, and it does not exploit the locality of access patterns.
- **Migration Algorithm**: In this algorithm, the shared data is distributed among the nodes, and each node has a local copy of the data it accesses. When a node wants to read or write a data item that is not present in its local memory, it requests the data item from the node that currently owns it. The owner node then transfers the data item to the requester node, and updates its ownership information. The advantage of this algorithm is that it reduces the communication overhead and exploits the locality of access patterns. The disadvantage is that it may cause frequent data transfers and increase the latency of access.
- **Replication Algorithm**: In this algorithm, the shared data is replicated among the nodes, and each node has a local copy of the entire shared data. When a node wants to read a data item, it can access its local copy without any communication. When a node wants to write a data item, it broadcasts the write request to all other nodes, and waits for their acknowledgments. The advantage of this algorithm is that it eliminates the data transfer overhead and reduces the latency of access. The disadvantage is that it consumes a lot of memory and network bandwidth, and it may cause inconsistency and coherence problems.
- **Invalidation Algorithm**: In this algorithm, the shared data is distributed among the nodes, and each node has a local copy of the data it accesses. When a node wants to read a data item, it can access its local copy if it is valid, or request the data item from the owner node if it is invalid. When a node wants to write a data item, it invalidates the copies of the data item in other nodes, and updates its own copy. The advantage of this algorithm is that it reduces the data transfer and network bandwidth overhead, and it exploits the locality of access patterns. The disadvantage is that it may cause invalidation messages and increase the latency of access.



## Unit 6 - Failure Recovery in Distributed Systems

- A distributed system is a collection of independent computers that communicate and cooperate to achieve a common goal.
- A failure in a distributed system is an event that prevents one or more components from functioning correctly or at all.
- Failure recovery is the process of restoring the system to a consistent and correct state after a failure.
- Failure recovery is important for ensuring the availability, reliability, and performance of distributed systems.
- Failure recovery can be classified into two types: backward recovery and forward recovery.

### Backward Recovery
- Backward recovery is the process of restoring the system to a previous consistent and correct state before the failure occurred.
- Backward recovery can be implemented using techniques such as checkpoints, logging, and rollback.
- Checkpoints are snapshots of the system state that are periodically saved on stable storage.
- Logging is the process of recording the actions or events that occur in the system on stable storage.
- Rollback is the process of restoring the system state to a previous checkpoint and replaying the logged actions or events until the failure point is reached.
- Backward recovery can be performed at different granularities, such as process-level, transaction-level, or system-level.
- Backward recovery can also be performed in different modes, such as pessimistic, optimistic, or causal.
- Pessimistic mode ensures that the system is always in a consistent state by using synchronous checkpoints and logging, but it incurs high overhead and latency.
- Optimistic mode allows the system to continue execution without waiting for checkpoints and logging, but it may require more rollback and replay in case of a failure.
- Causal mode ensures that the system is in a consistent state that respects the causal dependencies among the actions or events, by using asynchronous checkpoints and logging, but it may require some coordination and synchronization among the components.

### Forward Recovery
- Forward recovery is the process of restoring the system to a new consistent and correct state after the failure occurred.
- Forward recovery can be implemented using techniques such as redundancy, replication, and reconfiguration.
- Redundancy is the provision of extra resources or components that can take over the functionality of the failed ones.
- Replication is the process of creating and maintaining multiple copies of the same data or service on different components.
- Reconfiguration is the process of changing the structure or configuration of the system to adapt to the failure.
- Forward recovery can be performed at different levels, such as hardware-level, software-level, or application-level.
- Forward recovery can also be performed in different modes, such as passive, active, or hybrid.
- Passive mode relies on a primary component that performs the functionality and a backup component that takes over in case of a failure, but it may incur high recovery time and data loss.
- Active mode relies on multiple components that perform the functionality in parallel and coordinate with each other, but it may incur high resource consumption and complexity.
- Hybrid mode combines the advantages of passive and active modes by using a primary component and multiple backup components that perform the functionality in parallel, but it may incur high communication overhead and inconsistency.



# Concepts in Backward and Forward Recovery

- Backward recovery and forward recovery are two techniques to deal with failures in distributed systems.
- A failure in a distributed system can affect one or more processes, transactions, or messages, and can cause inconsistency, deadlock, or data loss.
- The goal of recovery is to restore the system to a consistent and correct state after a failure, and to ensure the atomicity, consistency, isolation, and durability (ACID) properties of transactions.

## Backward Recovery

- Backward recovery involves moving the system from its current state back to a previous error-free state, by undoing the effects of the failed operations.
- Backward recovery requires the system to periodically record its state, either locally or globally, in the form of checkpoints or logs.
- When a failure is detected, the system can roll back to the most recent checkpoint or log, and discard any changes made after that point.
- Backward recovery has the following advantages:
  - It does not depend on the nature or cause of the failure, and can handle any type of error.
  - It can recover from multiple failures, as long as there is a valid checkpoint or log available.
  - It can reduce the amount of work lost due to a failure, by rolling back only the affected processes or transactions.
- Backward recovery has the following disadvantages:
  - It can cause the system to lose some valid work done by other processes or transactions that are not affected by the failure, as they may have to roll back as well.
  - It can introduce inconsistency or deadlock in the system, if the checkpoints or logs are not synchronized or coordinated among the processes or transactions.
  - It can increase the overhead and complexity of the system, as it needs to maintain and manage the checkpoints or logs, and detect and resolve conflicts or dependencies.

## Forward Recovery

- Forward recovery involves moving the system from its current state to a new error-free state, by correcting or compensating the effects of the failed operations.
- Forward recovery requires the system to detect and diagnose the failure, and to apply a suitable recovery action, such as retrying, aborting, or compensating the failed operation.
- When a failure is detected, the system can continue the execution of the processes or transactions, by applying the recovery action and ensuring the consistency and correctness of the system.
- Forward recovery has the following advantages:
  - It can preserve the valid work done by other processes or transactions that are not affected by the failure, as they do not have to roll back or restart.
  - It can avoid inconsistency or deadlock in the system, as it does not depend on the checkpoints or logs, and does not introduce any conflicts or dependencies.
  - It can reduce the overhead and complexity of the system, as it does not need to maintain and manage the checkpoints or logs, and only needs to perform the recovery action.
- Forward recovery has the following disadvantages:
  - It depends on the nature and cause of the failure, and can only handle certain types of errors, such as transient or recoverable errors.
  - It can fail to recover from multiple or permanent failures, as it may not have a suitable recovery action available, or it may exhaust the resources or time limits of the system.
  - It can increase the amount of work lost due to a failure, by retrying, aborting, or compensating the failed operation, which may not be necessary or desirable.



# Recovery in Concurrent Systems

- Recovery in concurrent systems is the process of restoring the system to a consistent state after a failure or an error.
- Recovery is essential to ensure the correctness and reliability of concurrent systems, especially in distributed environments where failures are more common and unpredictable.
- Recovery in concurrent systems involves the following aspects:
  - **Logging**: Recording the actions and changes made by the transactions in a persistent storage, such as a disk or a tape. Logging is used to keep track of the history and state of the system, and to undo or redo the effects of transactions in case of failures.
  - **Concurrency control**: Regulating the access and modification of shared data by multiple transactions to prevent conflicts and inconsistencies. Concurrency control is used to ensure the atomicity, consistency, isolation, and durability (ACID) properties of transactions, and to avoid the problems of lost updates, dirty reads, unrepeatable reads, and phantom reads.
  - **Checkpointing**: Saving the current state of the system periodically or at certain points in the execution. Checkpointing is used to reduce the amount of logging and recovery work, and to speed up the restart process after a failure.
  - **Restart recovery**: Restoring the system to a consistent state after a failure by using the logs and checkpoints. Restart recovery is used to undo the effects of incomplete or aborted transactions, and to redo the effects of committed transactions that were not reflected in the database due to the failure.
  - **Transaction rollback**: Aborting a transaction and undoing its effects in case of an error or a conflict. Transaction rollback is used to maintain the consistency and isolation of transactions, and to resolve deadlocks or concurrency violations.



# Obtaining consistent Checkpoints for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Failure recovery in distributed systems is the process of restoring the system to a consistent and correct state after a failure occurs.
- Failure recovery is essential for fault tolerance, which is the ability of the system to continue functioning despite the presence of errors.
- Failure recovery can be achieved by using checkpoints, which are snapshots of the system state at certain points in time.
- Checkpoints can be used to roll back the system to a previous state and resume the execution from there, avoiding the need to restart the system from scratch.
- Checkpoints can be classified into two types: local and global.
  - Local checkpoints are taken by each process independently, without any coordination with other processes.
  - Global checkpoints are taken by all processes in a coordinated manner, such that they form a consistent view of the system state.
- A global checkpoint is consistent if it satisfies the following property: for any pair of processes P and Q, if P's checkpoint contains a message sent by P to Q, then Q's checkpoint contains the corresponding message received by Q from P.
- A consistent global checkpoint can be used to recover the system from any failure, without introducing any inconsistency or causality violation.
- Obtaining a consistent global checkpoint can be challenging in distributed systems, due to the following issues:
  - The lack of a global clock or a common notion of time among the processes.
  - The possibility of partial failures, such as node crashes or communication link failures.
  - The overhead of coordinating the checkpointing process among the processes.
- There are different algorithms and techniques for obtaining consistent global checkpoints in distributed systems, such as:
  - Synchronous checkpointing, which requires all processes to take checkpoints simultaneously, using a global synchronization signal.
  - Asynchronous checkpointing, which allows each process to take checkpoints independently, without any synchronization.
  - Coordinated checkpointing, which requires some form of communication and agreement among the processes to take checkpoints in a coordinated manner.
  - Communication-induced checkpointing, which piggybacks checkpointing information on the application messages exchanged by the processes.
  - Log-based checkpointing, which records the causal dependencies among the processes in a log file, and uses it to construct a consistent global checkpoint.
- Each of these techniques has its own advantages and disadvantages, depending on the characteristics of the system, such as the failure rate, the communication pattern, the checkpoint frequency, the checkpoint size, the recovery time, and the performance overhead.
- The choice of the best technique for obtaining consistent global checkpoints depends on the trade-off between the checkpointing cost and the recovery cost.



# Recovery in Distributed Database Systems

- Recovery in distributed database systems is the process of restoring the database to a consistent and correct state after a failure or an error .
- Recovery in distributed database systems is more complicated than in centralized database systems because failures can occur at multiple sites, communication links, or during the execution of distributed transactions.
- Recovery in distributed database systems aims to maintain the atomicity and durability of distributed transactions, which means that either all or none of the subtransactions at different sites should be committed, and the committed changes should be permanent.
- Recovery in distributed database systems can be classified into two types: local recovery and global recovery .
  - Local recovery is the process of recovering a single site from a failure, such as a disk crash or a power outage. Local recovery techniques include restoring a backup copy of the database, applying the redo and undo operations from the log, and using checkpoints to reduce the recovery time.
  - Global recovery is the process of recovering the entire distributed database system from a failure, such as a network partition or a site failure. Global recovery techniques include using distributed commit protocols, such as two-phase commit (2PC) or three-phase commit (3PC), to coordinate the commit or abort of distributed transactions, and using distributed concurrency control protocols, such as timestamp ordering or locking, to prevent conflicts and deadlocks among distributed transactions.
- Recovery in distributed database systems faces several challenges, such as:
  - How to handle the partial failures of sites or links, and how to resume the execution of distributed transactions after the failures are repaired.
  - How to ensure the consistency and correctness of the distributed database, and how to detect and resolve any inconsistencies or conflicts that may arise due to failures or errors.
  - How to minimize the overhead and performance degradation caused by the recovery techniques, such as the communication and synchronization costs, the logging and checkpointing overhead, and the global rollback and restart costs.
  - How to provide partial operability and availability of the distributed database system during the recovery process, and how to balance the trade-off between availability and consistency.



## Unit 7 - Fault Tolerance

- Fault tolerance is the ability of a system to continue functioning correctly in the presence of failures.
- Fault tolerance can be achieved by using techniques such as redundancy, replication, recovery, and reconfiguration.
- Redundancy is the provision of extra components or resources that can take over the function of a failed component or resource.
- Replication is the creation of multiple copies of data or services that can be accessed in case of a failure.
- Recovery is the process of restoring a system to a consistent and correct state after a failure.
- Reconfiguration is the process of changing the structure or configuration of a system to adapt to a failure or a change in the environment.
- Fault tolerance can be classified into two types: passive and active.
- Passive fault tolerance relies on redundancy to mask failures without requiring any intervention or detection.
- Active fault tolerance relies on detection and recovery to handle failures by activating redundant components or resources.
- Fault tolerance can be applied at different levels of a system, such as hardware, software, network, and application.
- Fault tolerance can improve the reliability, availability, and performance of a system, but it also introduces challenges such as complexity, cost, and consistency.



# Issues in Fault Tolerance for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Fault tolerance is the ability of a system to continue functioning correctly in the presence of failures.
- Fault tolerance is important for distributed systems because they consist of multiple components that may be subject to failures, such as hardware, software, network, or power outages.
- Fault tolerance can be achieved by using various techniques, such as redundancy, replication, checkpointing, recovery, consensus, and fault detection .
- Redundancy is the provision of extra resources or components that can take over the functionality of a failed component.
- Replication is the creation of multiple copies of data or processes that can be accessed or executed by different components in case of a failure.
- Checkpointing is the saving of the state of a process or a system at regular intervals, so that it can be restored to a consistent state in case of a failure.
- Recovery is the process of restoring the system to a correct state after a failure, by using checkpoints, backups, or other methods.
- Consensus is the agreement among multiple components on a common value or decision, despite the presence of failures or conflicting information.
- Fault detection is the identification of faulty components or behaviors in a system, by using techniques such as timeouts, heartbeats, or voting.
- Some of the challenges and issues in fault tolerance for distributed systems are :
  - The complexity and diversity of distributed systems, which make it difficult to design, implement, and test fault-tolerant algorithms and protocols.
  - The uncertainty and unpredictability of failures, which may affect different components, types, and levels of the system, and may have different causes and effects.
  - The trade-offs and costs of fault tolerance, which may involve performance, availability, consistency, scalability, and security issues.



# Commit Protocols

## Introduction

- A commit protocol is a method for ensuring that a distributed transaction either commits or aborts atomically across all the participating sites.
- A commit protocol is necessary to achieve atomicity and durability in the presence of failures, such as site crashes, network partitions, or message losses.
- A commit protocol typically involves a coordinator site and one or more participant sites that exchange messages to reach a consensus on the outcome of the transaction.
- A commit protocol can be classified into two-phase commit (2PC), three-phase commit (3PC), or other variants based on the number and type of messages exchanged.

## Two-Phase Commit (2PC)

- 2PC is the most widely used commit protocol in distributed systems.
- 2PC consists of two phases: a prepare phase and a commit phase.
- In the prepare phase, the coordinator sends a PREPARE message to all the participants, asking them to vote on whether they are ready to commit or abort the transaction.
- Each participant replies with a YES vote if it has successfully executed its part of the transaction and is ready to commit, or a NO vote if it has encountered any failure or inconsistency and wants to abort the transaction.
- In the commit phase, the coordinator collects the votes from all the participants and decides the final outcome of the transaction based on the following rules:
  - If all the participants vote YES, the coordinator decides to commit the transaction and sends a COMMIT message to all the participants, instructing them to make their changes permanent and release any locks or resources held by the transaction.
  - If any participant votes NO, or if the coordinator does not receive a vote from any participant within a timeout period, the coordinator decides to abort the transaction and sends an ABORT message to all the participants, instructing them to undo their changes and release any locks or resources held by the transaction.
- Each participant follows the coordinator's decision and sends an ACK message to the coordinator, confirming that it has completed the commit or abort operation.
- The coordinator waits for the ACK messages from all the participants and then terminates the transaction.

## Three-Phase Commit (3PC)

- 3PC is a commit protocol that aims to avoid blocking in the presence of network partitions or coordinator failures.
- 3PC consists of three phases: a prepare phase, a pre-commit phase, and a commit phase.
- In the prepare phase, the coordinator sends a PREPARE message to all the participants, asking them to vote on whether they are ready to commit or abort the transaction.
- Each participant replies with a YES vote if it has successfully executed its part of the transaction and is ready to commit, or a NO vote if it has encountered any failure or inconsistency and wants to abort the transaction.
- In the pre-commit phase, the coordinator collects the votes from all the participants and decides the final outcome of the transaction based on the following rules:
  - If all the participants vote YES, the coordinator decides to commit the transaction and sends a PRE-COMMIT message to all the participants, instructing them to prepare to commit the transaction and wait for the final confirmation.
  - If any participant votes NO, or if the coordinator does not receive a vote from any participant within a timeout period, the coordinator decides to abort the transaction and sends an ABORT message to all the participants, instructing them to undo their changes and release any locks or resources held by the transaction.
- Each participant follows the coordinator's decision and sends an ACK message to the coordinator, confirming that it has received the PRE-COMMIT or ABORT message.
- In the commit phase, the coordinator waits for the ACK messages from all the participants and then sends a COMMIT message to all the participants, instructing them to make their changes permanent and release any locks or resources held by the transaction.
- Each participant follows the coordinator's decision and sends an ACK message to the coordinator, confirming that it has completed the commit or abort operation.
- The coordinator waits for the ACK messages from all the participants and then terminates the transaction.



# Voting Protocols for Fault Tolerance in Distributed Systems

- Voting protocols are a class of consensus algorithms that allow a set of distributed nodes to agree on a common value or decision, despite the presence of faults or attacks.
- Voting protocols are based on the idea of collecting votes from a quorum of nodes and applying a voting function to determine the outcome.
- Voting protocols can be classified into two types: exact voting and inexact voting.
  - Exact voting requires that all nodes agree on the same value or decision, and that the value or decision is correct according to some predefined criterion. Examples of exact voting are two-phase commit, three-phase commit, and Paxos.
  - Inexact voting allows for some degree of disagreement or error among the nodes, as long as the outcome satisfies some probabilistic or statistical properties. Examples of inexact voting are majority voting, weighted voting, and probabilistic voting.
- Voting protocols can also be distinguished by their security and fault-tolerance properties, such as:
  - Byzantine fault tolerance: the ability to tolerate arbitrary faults or malicious behavior by some nodes.
  - Crash fault tolerance: the ability to tolerate benign faults or failures by some nodes.
  - Fairness: the property that all nodes have equal or proportional influence on the outcome, regardless of their order or timing of voting.
  - Liveness: the property that the protocol eventually terminates and produces an outcome.
  - Safety: the property that the protocol never produces an incorrect or inconsistent outcome.
- Voting protocols can be used for various applications in distributed systems, such as:
  - Data replication: ensuring that copies of data are consistent across different nodes or locations.
  - Transaction processing: ensuring that transactions are executed atomically and reliably across multiple nodes or databases.
  - Leader election: choosing a node to coordinate or perform some tasks on behalf of the system.
  - Group membership: maintaining a list of active or available nodes in the system.
  - Configuration management: updating or changing the parameters or settings of the system.



# Dynamic voting protocols

- Dynamic voting protocols are techniques for consistency and recovery control of replicated files in distributed systems  .
- The purpose of a replicated file is to improve the availability of a logical file in the presence of site failures and network partitions  .
- A dynamic voting protocol assigns a number of votes to each copy of a replicated file, and requires a majority of votes to access or update the file   .
- The number of votes assigned to each copy can change dynamically depending on the system state, such as the number of available copies, the network topology, or the access pattern    .
- The advantages of dynamic voting protocols are:
  - They can increase the availability of a replicated file by allowing access even when some copies are inaccessible   .
  - They can reduce the communication cost of accessing a replicated file by assigning more votes to copies that are closer or more frequently accessed   .
  - They can improve the fault tolerance of a replicated file by reassigning votes upon node or link failure .
- The challenges of dynamic voting protocols are:
  - They need to maintain the consistency of the vote assignments among the copies and avoid conflicts or deadlocks    .
  - They need to cope with dynamic changes in the system state and adapt the vote assignments accordingly    .
  - They need to balance the trade-off between availability and communication cost, as well as between fault tolerance and performance    .
- Some examples of dynamic voting protocols are:
  - The dynamic weighted voting scheme proposed by Davcev  , which assigns votes to copies based on their availability and distance.
  - The topological dynamic voting algorithm proposed by Agrawal and Abbadi, which assigns votes to copies based on their network connectivity and access frequency.
  - The protocols for dynamic vote reassignment proposed by Gifford, which reassign votes to copies based on their availability and proximity.



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
- Concurrency control also prevents data inconsistency and ensures serializability, which is the equivalence of concurrent execution to some serial execution of the transactions.
- Concurrency control techniques implement some protocols that can be broadly classified into two categories: lock-based protocols and timestamp-based protocols.
- Lock-based protocols use locks to control the access of transactions to data items. A lock is a mechanism that grants or denies permission to read or write a data item. There are different types of locks, such as binary locks, shared/exclusive locks, and multiple granularity locks.
- Timestamp-based protocols use timestamps to order the transactions and determine their precedence. A timestamp is a unique identifier that indicates the time at which a transaction started. There are two types of timestamps: commit timestamps and logical timestamps.



# Transactions

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the operations in a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction is not affected by the concurrent execution of other transactions.
- Durability means that the effects of a committed transaction are permanent and survive failures.

# Distributed Transactions

- A distributed transaction is a transaction that spans multiple data servers in a distributed database system.
- A distributed transaction consists of a set of subtransactions, each of which is executed by one data server.
- A distributed transaction coordinator (DTC) is a component that manages the coordination and execution of distributed transactions.
- A distributed transaction has two phases: the prepare phase and the commit phase.
- In the prepare phase, the DTC sends a prepare message to each data server involved in the transaction, asking them to vote on whether they are ready to commit or abort the transaction.
- In the commit phase, the DTC collects the votes from the data servers and decides whether to commit or abort the transaction. If all the data servers vote to commit, the DTC sends a commit message to each data server, asking them to make the changes permanent. If any data server votes to abort, the DTC sends an abort message to each data server, asking them to undo the changes.

# Distributed Concurrency Control

- Distributed concurrency control is the concurrency control of a system distributed over a computer network.
- Distributed concurrency control provides a mechanism to synchronize distributed transactions in such a way that the ACID properties are not violated by their interleaved execution.
- Distributed concurrency control makes sure that all subtransactions of a set of distributed transactions are serialized identically in all data servers involved.
- Distributed concurrency control can be classified into two categories: centralized and decentralized.
- Centralized concurrency control relies on a single coordinator to manage the concurrency control of all the data servers. This approach simplifies the design and implementation, but introduces a single point of failure and a performance bottleneck.
- Decentralized concurrency control distributes the responsibility of concurrency control among the data servers. This approach improves the availability and scalability, but increases the complexity and communication overhead.
- Distributed concurrency control can use various techniques to ensure serializability, such as locking, timestamping, validation, and multiversioning.



# Nested transactions for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A transaction is a unit of work that accesses and possibly modifies data in a database or a distributed system.
- A transaction has the properties of atomicity, consistency, isolation, and durability (ACID).
- A nested transaction is a transaction that is composed of subtransactions, each of which may have its own begin and end points, and may be executed concurrently or sequentially.
- A nested transaction has the following advantages:
  - It allows for partial rollback and recovery of subtransactions without affecting the whole transaction.
  - It enables concurrency control and deadlock detection at different levels of granularity.
  - It facilitates modular design and implementation of complex transactions.
  - It supports distributed transactions that span multiple servers or systems.
- A nested transaction has the following challenges:
  - It requires a mechanism to coordinate the commit or abort of subtransactions and the parent transaction.
  - It may introduce additional overhead and complexity in maintaining the consistency and serializability of transactions.
  - It may increase the risk of cascading aborts or inconsistent states if subtransactions are not properly isolated or synchronized.
- A nested transaction can be structured in two different ways:
  - Flat transactions: A flat transaction has a single begin and end point, and may access data from multiple servers or systems. It is usually simple and suitable for short activities.
  - Nested transactions: A nested transaction has a hierarchical structure of subtransactions, each of which may have its own begin and end point, and may access data from different servers or systems. It is usually complex and suitable for long or composite activities.
- A nested transaction can be implemented using different protocols, such as:
  - Two-phase commit (2PC): A protocol that ensures atomicity of a distributed transaction by coordinating the commit or abort decision among all the servers or systems involved in the transaction. It consists of two phases: prepare and commit/abort.
  - Presumed abort (PA): A protocol that optimizes 2PC by reducing the number of messages and log entries required for commit or abort. It assumes that a transaction will abort unless it receives a commit request from the coordinator.
  - Presumed commit (PC): A protocol that optimizes 2PC by reducing the number of messages and log entries required for commit or abort. It assumes that a transaction will commit unless it receives an abort request from the coordinator or a participant.
  - Nested two-phase commit (N2PC): A protocol that extends 2PC to support nested transactions by allowing subtransactions to prepare and commit/abort independently, and propagating the final decision to the parent transaction.
  - Saga: A protocol that implements a long-running transaction as a sequence of subtransactions, each of which can be committed or compensated (undone) independently. It ensures eventual consistency of the transaction by applying compensating actions in case of failures or aborts.



# Locks for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A lock is a mechanism that allows only one of the innumerable nodes or processes to access and modify a resource or data that is being shared commonly to prevent execution of the same task twice and also maintain data integrity.
- In distributed systems, locks are used to coordinate access to a shared resource among multiple nodes or processes that may be geographically dispersed or communicate asynchronously.
- Locks can be classified into different types based on the security of lock resources, the granularity of lock resources, the duration of lock holding, and the lock acquisition protocol.
- Some of the common types of locks are:
  - Exclusive lock: A lock that allows only one node or process to access and modify a resource or data, and prevents any other node or process from accessing or modifying it until the lock is released.
  - Shared lock: A lock that allows multiple nodes or processes to access but not modify a resource or data, and prevents any other node or process from modifying it until all the shared locks are released.
  - Read lock: A lock that allows a node or process to read a resource or data, and prevents any other node or process from modifying it until the lock is released. It is equivalent to a shared lock.
  - Write lock: A lock that allows a node or process to modify a resource or data, and prevents any other node or process from accessing or modifying it until the lock is released. It is equivalent to an exclusive lock.
  - Optimistic lock: A lock that does not block a node or process from accessing or modifying a resource or data, but checks for conflicts at the end of the operation and rolls back the changes if a conflict is detected.
  - Pessimistic lock: A lock that blocks a node or process from accessing or modifying a resource or data until the lock is acquired, and holds the lock until the end of the operation or until the lock is explicitly released.
  - Fine-grained lock: A lock that applies to a small unit of a resource or data, such as a record, a field, or a byte, and allows for higher concurrency and lower contention.
  - Coarse-grained lock: A lock that applies to a large unit of a resource or data, such as a file, a table, or a database, and allows for lower concurrency and higher contention.
  - Short-term lock: A lock that is held for a short duration, such as a single operation or a transaction, and is released as soon as possible.
  - Long-term lock: A lock that is held for a long duration, such as a session or a batch job, and is released only when the session or the job is completed.
  - Centralized lock: A lock that is managed by a single node or process that acts as a lock manager or a coordinator, and grants or denies lock requests from other nodes or processes.
  - Distributed lock: A lock that is managed by multiple nodes or processes that cooperate to reach a consensus or an agreement on the lock status, and use a distributed lock protocol to communicate and coordinate.
- Locks can be implemented using various techniques, such as:
  - Database locks: Locks that are provided by a database system to ensure the consistency and isolation of transactions that access and modify the data stored in the database.
  - Redis locks: Locks that are implemented using Redis, an in-memory data structure store, to provide fast and scalable locking for distributed systems.
  - ZooKeeper locks: Locks that are implemented using ZooKeeper, a distributed coordination service, to provide reliable and fault-tolerant locking for distributed systems.
  - Paxos locks: Locks that are implemented using Paxos, a distributed consensus algorithm, to provide strong and consistent locking for distributed systems.



# Optimistic Concurrency Control

- Optimistic concurrency control (OCC) is a concurrency control method applied to transactional systems such as relational database management systems and software transactional memory.
- OCC assumes that multiple transactions can frequently complete without interfering with each other, and does not use locking or timestamping techniques to prevent conflicts .
- Instead, a transaction is executed without restrictions until it is committed, and then it is validated to ensure that no conflicts have occurred with other concurrent transactions.
- If a conflict is detected, the transaction is aborted and restarted, possibly with some backoff or priority adjustment mechanism to reduce the likelihood of further conflicts .
- OCC has the advantage of allowing a high degree of concurrency and avoiding the overhead of locking or timestamping, but it also has the drawback of wasting resources and increasing latency when conflicts are frequent and transactions have to be restarted .
- OCC can be implemented in a centralized or distributed system, depending on where the validation and commit phases are performed .
- In a centralized system, there is a single validator that checks all the transactions before they are committed, and a single commit log that records the committed transactions.
- In a distributed system, there may be multiple validators and commit logs, each responsible for a subset of the data or transactions, and they may communicate with each other to ensure global consistency.
- A distributed OCC protocol may have different design choices, such as whether to use two-phase commit, how to handle network failures, how to acquire locks for the second execution, and how to optimize the validation and commit phases.
- A distributed OCC protocol should aim to minimize the number of restarts, the communication overhead, and the commit latency, while ensuring correctness and consistency of the transactions.



# Timestamp Ordering for Transactions and Concurrency Control in Distributed Systems

- Timestamp ordering is a class of concurrency control protocols that use timestamps to determine the serializability order of transactions in a distributed system .
- A timestamp is a monotonically increasing number that is assigned to each transaction when it starts . It can be based on the system clock or a logical counter.
- The main idea of timestamp ordering is to order the transactions based on their timestamps, such that a schedule in which the transactions participate is serializable and equivalent to a serial schedule that has the transactions in the order of their timestamps.
- There are two types of timestamp ordering protocols: basic timestamp ordering and optimistic timestamp ordering .
- Basic timestamp ordering protocol uses two timestamps for each data item: read timestamp (RTS) and write timestamp (WTS). RTS is the largest timestamp of any transaction that has successfully read the data item, and WTS is the largest timestamp of any transaction that has successfully written the data item .
- Basic timestamp ordering protocol enforces two rules: read-write rule and write-write rule .
  - Read-write rule: A transaction T can read a data item X only if T's timestamp is greater than or equal to the WTS of X. Otherwise, T is aborted and restarted with a new timestamp. This rule ensures that a transaction does not read a data item that has been overwritten by a later transaction .
  - Write-write rule: A transaction T can write a data item X only if T's timestamp is greater than both the RTS and the WTS of X. Otherwise, T is aborted and restarted with a new timestamp. This rule ensures that a transaction does not overwrite a data item that has been read or written by a later transaction .
- Optimistic timestamp ordering protocol uses three timestamps for each transaction: start timestamp (STS), commit timestamp (CTS), and validation timestamp (VTS). STS is the timestamp assigned to the transaction when it starts, CTS is the timestamp assigned to the transaction when it commits, and VTS is the timestamp assigned to the transaction when it validates.
- Optimistic timestamp ordering protocol consists of three phases: read phase, validation phase, and write phase.
  - Read phase: A transaction T reads the data items it needs and stores them in a private workspace. It also records the WTS of each data item it reads. It does not write any data item to the database.
  - Validation phase: A transaction T validates its read set by comparing the WTS of each data item it read with the current WTS of the same data item in the database. If any of the WTS values have changed, it means that T has read a stale value and it is aborted and restarted with a new timestamp. Otherwise, T is assigned a CTS that is the maximum of its STS and the largest WTS of any data item it read. T also sets its VTS to the current time.
  - Write phase: A transaction T writes the data items it modified in its private workspace to the database. It also updates the WTS of each data item it wrote to its CTS. It does not read any data item from the database.
- Optimistic timestamp ordering protocol enforces two rules: commit order rule and validation order rule.
  - Commit order rule: A transaction T can commit only if its CTS is greater than the CTS of any other transaction that has committed. Otherwise, T is aborted and restarted with a new timestamp. This rule ensures that the transactions commit in the order of their timestamps.
  - Validation order rule: A transaction T can validate only if its VTS is greater than the VTS of any other transaction that has validated. Otherwise, T is aborted and restarted with a new timestamp. This rule ensures that the transactions validate in the order of their timestamps.
- Timestamp ordering protocols have the advantages of being deadlock-free, avoiding unnecessary blocking, and being easy to implement in a distributed system  .
- Timestamp ordering protocols have the disadvantages of being prone to starvation, aborting transactions unnecessarily, and requiring extra storage and communication overhead for timestamps  .



# Comparison of methods for concurrency control

Concurrency control is the process of managing the concurrent access of multiple transactions to a shared data in a distributed system, such that the ACID properties are preserved and the system consistency is maintained.

There are various methods for concurrency control, each with its own advantages and disadvantages. Some of the common methods are:

- **Two-phase locking protocol (2PL)**: This method requires each transaction to acquire locks on the data items it needs to access, and release them after it finishes. There are two phases: the growing phase, where the transaction can only acquire locks, and the shrinking phase, where the transaction can only release locks. The transaction cannot request any new locks after it releases any lock. This method ensures serializability, which means the concurrent execution of transactions is equivalent to some serial execution. However, it may cause deadlock, where two or more transactions are waiting for each other to release locks, and starvation, where some transactions are delayed indefinitely due to lock contention.

- **Timestamp ordering protocol (TO)**: This method assigns a unique timestamp to each transaction, and uses it to order the transactions. Each data item has two timestamps: the read timestamp (RTS), which records the timestamp of the last transaction that read the item, and the write timestamp (WTS), which records the timestamp of the last transaction that wrote the item. A transaction can read or write a data item only if its timestamp is compatible with the timestamps of the item, otherwise it is aborted and restarted with a new timestamp. This method avoids deadlock, since there is no waiting for locks, but it may cause more aborts and restarts, which increases the overhead and reduces the throughput.

- **Multi-version concurrency control (MVCC)**: This method allows multiple versions of the same data item to coexist, and assigns a timestamp to each version. A transaction can read the latest version of a data item that is older than or equal to its timestamp, and can write a new version of a data item only if its timestamp is greater than the timestamp of the latest version. This way, the read operations do not block the write operations, and vice versa. This method improves the concurrency and performance of the system, especially for read-intensive workloads, but it requires more storage space and garbage collection to manage the multiple versions.

- **Validation concurrency control (VCC)**: This method divides each transaction into three phases: the read phase, where the transaction reads the data items and stores them in a private workspace, the validation phase, where the transaction checks if it can commit without violating the serializability, and the write phase, where the transaction writes the updated data items to the database. The validation phase uses a validation test, such as the precedence graph test or the serial validation test, to determine if the transaction is serializable with respect to the other transactions that have committed or are in the validation phase. This method also avoids deadlock, but it may cause more aborts and restarts, and it requires the transactions to be read-only or write-only.

The choice of the concurrency control method depends on the characteristics of the distributed system, such as the network latency, the communication cost, the data replication, the transaction workload, and the performance requirements. There is no single best method that suits all scenarios, and some systems may use a combination of different methods to achieve the desired concurrency control.



## Unit 9 - Distributed Transactions

- A distributed transaction is a type of transaction that involves two or more network hosts, usually providing transactional resources, such as databases, message queues, file systems, etc.   
- A distributed transaction is coordinated by a transaction manager, which is responsible for creating and managing a global transaction that encompasses all the operations against the transactional resources.  
- A distributed transaction requires the following properties to ensure data consistency and reliability: atomicity, consistency, isolation, and durability (ACID). 
- Atomicity means that either all the operations in a distributed transaction are executed successfully, or none of them are. If any operation fails, the transaction manager should roll back the changes made by the previous operations. 
- Consistency means that the distributed transaction should preserve the integrity constraints and business rules of the data. The transaction manager should ensure that the data is in a valid state before and after the transaction. 
- Isolation means that the distributed transaction should not interfere with other concurrent transactions. The transaction manager should prevent the data from being accessed or modified by other transactions until the current transaction is committed or aborted. 
- Durability means that the effects of a committed distributed transaction should be permanent and survive any failures. The transaction manager should ensure that the data is safely stored and replicated on the transactional resources. 
- A distributed transaction can be implemented using different protocols, such as two-phase commit (2PC), three-phase commit (3PC), or the saga pattern.  
- Two-phase commit (2PC) is a protocol that involves two phases: prepare and commit. In the prepare phase, the transaction manager asks all the transactional resources to vote on whether they are ready to commit the transaction. If all the resources vote yes, the transaction manager proceeds to the commit phase, where it instructs all the resources to commit the transaction. If any resource votes no, or fails to respond, the transaction manager aborts the transaction and instructs all the resources to roll back the changes.  
- Three-phase commit (3PC) is a protocol that involves three phases: prepare, pre-commit, and commit. In the prepare phase, the transaction manager asks all the transactional resources to vote on whether they are ready to commit the transaction. If all the resources vote yes, the transaction manager proceeds to the pre-commit phase, where it informs all the resources that the transaction is about to be committed. If any resource fails to acknowledge, the transaction manager aborts the transaction and instructs all the resources to roll back the changes. In the commit phase, the transaction manager instructs all the resources to commit the transaction.  
- The saga pattern is a protocol that involves a sequence of compensating actions. A compensating action is an operation that reverses the effect of a previous operation. In the saga pattern, the transaction manager executes each operation in the sequence and records its compensating action. If any operation fails, the transaction manager executes the compensating actions in reverse order to undo the changes made by the previous operations. 
- A distributed transaction can face various challenges, such as network failures, resource failures, concurrency conflicts, deadlock, or partial failures. The transaction manager should handle these challenges by using appropriate protocols, timeouts, retries, locks, or recovery mechanisms.



# Flat and Nested Distributed Transactions

A distributed transaction is a transaction that accesses objects managed by multiple servers. A distributed transaction must maintain the ACID properties of a transaction, which means that it must be atomic, consistent, isolated, and durable. Atomicity means that either all the changes made by the transaction are committed or none of them are. Consistency means that the transaction preserves the integrity constraints of the data. Isolation means that the transaction does not interfere with other concurrent transactions. Durability means that the committed changes are permanent and survive failures.

There are two ways to structure a distributed transaction: flat or nested.

## Flat Transactions

A flat transaction has a single begin point and a single end point, where it either commits or aborts. A flat transaction is usually simple and short-lived, and it does not have any subtransactions. A flat transaction can be coordinated by a single server, called the transaction manager, which communicates with the other servers involved in the transaction, called the resource managers. The transaction manager uses a two-phase commit protocol to ensure the atomicity of the transaction. The two-phase commit protocol consists of two phases: prepare and commit.

- In the prepare phase, the transaction manager asks each resource manager to vote on whether they are ready to commit the transaction or not. Each resource manager replies with either yes or no. If any resource manager replies with no, the transaction manager aborts the transaction and informs all the resource managers to roll back their changes. If all the resource managers reply with yes, the transaction manager moves to the commit phase.
- In the commit phase, the transaction manager sends a commit message to all the resource managers, instructing them to make their changes permanent. Each resource manager acknowledges the commit message and releases the locks on the objects. The transaction manager then completes the transaction.

## Nested Transactions

A nested transaction is a transaction that has one or more subtransactions, which are transactions themselves. A nested transaction has a hierarchical structure, where the top-level transaction is called the root transaction, and the subtransactions are called the branches. A nested transaction can be coordinated by multiple servers, each of which acts as a transaction manager for its subtransactions. A nested transaction uses a two-phase commit protocol for each subtransaction, and a three-phase commit protocol for the root transaction. The three-phase commit protocol consists of three phases: prepare, pre-commit, and commit.

- In the prepare phase, the root transaction manager asks each branch transaction manager to vote on whether they are ready to commit their subtransactions or not. Each branch transaction manager replies with either yes or no. If any branch transaction manager replies with no, the root transaction manager aborts the root transaction and informs all the branch transaction managers to abort their subtransactions. If all the branch transaction managers reply with yes, the root transaction manager moves to the pre-commit phase.
- In the pre-commit phase, the root transaction manager sends a pre-commit message to all the branch transaction managers, instructing them to prepare to commit their subtransactions. Each branch transaction manager acknowledges the pre-commit message and waits for the final commit message. The root transaction manager then moves to the commit phase.
- In the commit phase, the root transaction manager sends a commit message to all the branch transaction managers, instructing them to commit their subtransactions. Each branch transaction manager acknowledges the commit message and makes their changes permanent. The root transaction manager then completes the root transaction.

## Advantages and Disadvantages of Flat and Nested Transactions

Flat transactions are simpler and faster than nested transactions, as they involve fewer messages and less coordination. However, flat transactions are less flexible and more prone to conflicts and deadlocks, as they lock the objects for the entire duration of the transaction. Flat transactions are suitable for short and simple transactions that do not require much concurrency control.

Nested transactions are more complex and slower than flat transactions, as they involve more messages and more coordination. However, nested transactions are more flexible and more tolerant to failures and partial aborts, as they allow subtransactions to commit or abort independently. Nested transactions are suitable for long and complex transactions that require more concurrency control and fault tolerance.



# Atomic Commit Protocols for Distributed Transactions

- A distributed transaction is a transaction that involves multiple servers or nodes in a distributed system.
- An atomic commit protocol is a protocol that ensures that a distributed transaction is either committed or rolled back in its entirety, even if the system fails or some of the nodes fail or crash.
- Ensuring atomic commit is important for maintaining the consistency and integrity of the data in a distributed system.
- There are different types of atomic commit protocols, such as two-phase commit, three-phase commit, parallel commit, and failure-aware commit.

## Two-phase commit (2PC)

- Two-phase commit is the most widely used atomic commit protocol.
- It involves two phases: a prepare phase and a commit phase.
- In the prepare phase, a coordinator node sends a prepare message to all the participant nodes, asking them to vote on whether to commit or abort the transaction.
- Each participant node replies with a yes or no vote, depending on whether it is ready to commit or not.
- In the commit phase, the coordinator node collects all the votes and decides whether to commit or abort the transaction based on the majority rule.
- If all the votes are yes, the coordinator node sends a commit message to all the participant nodes, instructing them to commit the transaction.
- If any of the votes are no, or if the coordinator node does not receive all the votes within a timeout, the coordinator node sends an abort message to all the participant nodes, instructing them to roll back the transaction.
- Two-phase commit ensures atomicity, but it has some drawbacks, such as blocking, high latency, and vulnerability to failures.

## Three-phase commit (3PC)

- Three-phase commit is an extension of two-phase commit that aims to overcome some of its drawbacks.
- It involves three phases: a prepare phase, a pre-commit phase, and a commit phase.
- In the prepare phase, the coordinator node sends a prepare message to all the participant nodes, asking them to vote on whether to commit or abort the transaction.
- Each participant node replies with a yes or no vote, depending on whether it is ready to commit or not.
- In the pre-commit phase, the coordinator node collects all the votes and decides whether to commit or abort the transaction based on the majority rule.
- If all the votes are yes, the coordinator node sends a pre-commit message to all the participant nodes, instructing them to prepare to commit the transaction.
- If any of the votes are no, or if the coordinator node does not receive all the votes within a timeout, the coordinator node sends an abort message to all the participant nodes, instructing them to roll back the transaction.
- In the commit phase, the coordinator node sends a commit message to all the participant nodes, instructing them to commit the transaction.
- If the coordinator node does not receive an acknowledgment from all the participant nodes within a timeout, it sends a commit message again until it does.
- Three-phase commit reduces the blocking problem of two-phase commit, but it still has high latency and vulnerability to failures.

## Parallel commit

- Parallel commit is a new atomic commit protocol that aims to reduce the latency of distributed transactions to only a single round-trip of distributed consensus.
- It involves two phases: a staging phase and a commit phase.
- In the staging phase, each participant node writes the transaction data to a staging area, which is a temporary location that is not visible to other transactions.
- Each participant node also generates a unique transaction identifier and sends it to a consensus service, which is a distributed system that provides reliable and consistent agreement among nodes.
- The consensus service assigns a global commit timestamp to each transaction identifier and returns it to the participant node.
- In the commit phase, each participant node checks whether its transaction identifier has a global commit timestamp that is lower than the current timestamp of the system.
- If yes, the participant node commits the transaction by moving the data from the staging area to the final location, which is visible to other transactions.
- If no, the participant node aborts the transaction by discarding the data from the staging area.
- Parallel commit ensures atomicity and reduces latency, but it requires a reliable and consistent consensus service.

## Failure-aware commit (FLAC)

- Failure-aware commit is a practical atomic commit protocol that leverages the failure information of the participant nodes to optimize the commit decision and reduce the latency of distributed transactions.
- It involves two phases: a prepare phase and a commit phase.
- In the prepare phase, a coordinator node sends a prepare message to all the participant nodes, asking them to vote on whether to commit or abort the transaction.
- Each participant node replies



# Concurrency control in distributed transactions

Concurrency control is the process of managing the concurrent access and modification of shared data by multiple transactions in a database system. Concurrency control ensures that the transactions preserve the ACID (atomicity, consistency, isolation, and durability) properties and do not interfere with each other.

Distributed transactions are transactions that span multiple data servers in a distributed database system. A distributed database system is a system where data is stored and managed by a network of interconnected data servers that cooperate to provide a unified view of the data. Distributed transactions may access and update data on different servers, and thus require coordination and synchronization among the servers.

Concurrency control in distributed transactions is the problem of ensuring that the concurrent execution of distributed transactions does not violate the ACID properties and maintains the consistency and integrity of the distributed database. Concurrency control in distributed transactions is more challenging than in centralized transactions, because of the following issues:

- Network latency and communication overhead: The data servers need to communicate with each other to coordinate and synchronize the distributed transactions, which may incur delays and costs due to the network distance and bandwidth.
- Network failures and partitions: The data servers may become unreachable or disconnected from each other due to network failures or partitions, which may cause the distributed transactions to abort, retry, or wait indefinitely.
- Data replication and consistency: The data servers may replicate the same data for availability and performance reasons, which may introduce the problem of maintaining the consistency of the replicated data across the servers.
- Distributed deadlock detection and resolution: The distributed transactions may acquire locks on different data items on different servers, which may lead to circular wait and deadlock situations that need to be detected and resolved.

There are different approaches and algorithms for concurrency control in distributed transactions, such as:

- Locking-based concurrency control protocols: These protocols use the concept of locking data items to prevent concurrent transactions from accessing or modifying the same data item. Locking-based protocols can be classified into two-phase locking (2PL), rigorous two-phase locking (R2PL), and tree-structured locking (TSL) protocols. Locking-based protocols require a distributed lock manager (DLM) to manage the locks across the servers.
- Timestamp-based concurrency control algorithms: These algorithms use a transaction's timestamp to order and serialize the transactions. Timestamp-based algorithms can be classified into basic timestamp ordering (BTO), conservative timestamp ordering (CTO), and optimistic timestamp ordering (OTO) algorithms. Timestamp-based algorithms require a global clock or a logical clock to generate timestamps across the servers.
- Optimistic concurrency control algorithms: These algorithms allow transactions to execute without locking or checking timestamps, and validate the transactions at commit time. Optimistic algorithms can be classified into basic optimistic concurrency control (BOCC), optimistic concurrency control with certification (OCC-C), and optimistic concurrency control with version numbers (OCC-VN) algorithms. Optimistic algorithms require a validation manager (VM) to validate the transactions across the servers.

Each approach and algorithm has its own advantages and disadvantages in terms of performance, scalability, availability, and complexity. The choice of the best approach and algorithm depends on the characteristics of the distributed database system and the workload.



# Distributed Deadlocks

- A **distributed deadlock** is a situation where a set of processes in a distributed system are waiting for each other to release resources or messages, and none of them can proceed .
- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems .
- Distributed deadlocks are harder to detect, avoid, and prevent than deadlocks in centralized systems, because there is no single authority that can oversee resource allocation and monitor the state of the system.
- There are three main approaches to handle distributed deadlocks :
  - **Prevention**: This approach tries to prevent deadlocks from occurring by imposing some constraints on resource allocation, such as ordering the resources, limiting the number of resources per process, or using timeouts. However, this approach may reduce the concurrency and performance of the system, and may not be applicable to all types of resources.
  - **Avoidance**: This approach tries to avoid deadlocks by making informed decisions about resource allocation, based on the current and future requests of the processes. For example, a process may request all the resources it needs at once, or a resource manager may grant a resource only if it does not lead to a potential deadlock. However, this approach requires accurate and up-to-date information about the system state, which may be difficult or costly to obtain in a distributed system.
  - **Detection and resolution**: This approach tries to detect deadlocks after they occur, and then resolve them by aborting or restarting some of the processes involved in the deadlock. This approach requires a mechanism to detect deadlocks, either by constructing a global wait-for graph from local wait-for graphs at a deadlock detector, or by using a distributed algorithm like edge chasing  . This approach also requires a policy to select which processes to abort or restart, which may affect the fairness and efficiency of the system.

- There are different types of distributed deadlocks, depending on the nature of the resources and the communication model of the system:
  - **Communication deadlocks**: These are deadlocks that occur when processes are waiting for messages from each other, and no message can be delivered. For example, a process may send a request message and wait for a reply message, but the reply message may be blocked by another process that is waiting for a different message. Communication deadlocks can be detected by using a distributed algorithm that tracks the dependencies among messages, such as the Chandy-Misra-Haas algorithm or the Suzuki-Kasami algorithm.
  - **Resource deadlocks**: These are deadlocks that occur when processes are waiting for resources that are held by other processes, and no resource can be released. For example, a process may hold a lock on a file and wait for a lock on another file, but the other file may be locked by another process that is waiting for the first file. Resource deadlocks can be detected by using a centralized or distributed algorithm that constructs a global wait-for graph from local wait-for graphs, such as the Ho-Ramamoorthy algorithm or the Obermarck algorithm.
  - **Hybrid deadlocks**: These are deadlocks that involve both communication and resource dependencies among processes. For example, a process may hold a lock on a file and wait for a message from another process, but the message may be blocked by another process that is waiting for the same file. Hybrid deadlocks can be detected by using a combination of communication and resource deadlock detection algorithms, or by using a unified algorithm that handles both types of dependencies, such as the Menasce-Muntz algorithm or the Singhal algorithm.



# Transaction recovery for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

- A **transaction** is a logical unit of work that accesses and possibly modifies the data in a database.
- A **distributed transaction** is a transaction that involves multiple sites or nodes in a distributed system, such as a network of databases or servers.
- A **transaction recovery** is the process of restoring the database to a consistent state after a transaction failure, such as a system crash, a network partition, or a user abort.
- Transaction recovery is essential for ensuring the **ACID** properties of transactions, which are:
  - **Atomicity**: A transaction either commits (completes) or aborts (undoes) as a whole.
  - **Consistency**: A transaction preserves the integrity constraints of the database.
  - **Isolation**: A transaction does not interfere with other concurrent transactions.
  - **Durability**: The effects of a committed transaction are permanent and survive failures.
- Transaction recovery in distributed systems is more challenging than in centralized systems, because of the following issues:
  - **Partial failures**: Some sites or nodes may fail while others continue to operate, making it difficult to coordinate the outcome of a distributed transaction.
  - **Network failures**: The communication links between sites or nodes may fail, causing network partitions or message losses, which may prevent the exchange of information or acknowledgments among the participants of a distributed transaction.
  - **Concurrency control**: The concurrent execution of distributed transactions may cause conflicts or deadlocks, which may require aborting or restarting some transactions.
  - **Heterogeneity**: The sites or nodes involved in a distributed transaction may have different hardware, software, or data models, which may require data conversion or protocol adaptation.

- To address these challenges, transaction recovery in distributed systems typically relies on the following techniques:
  - **Logging**: Each site or node maintains a log of the operations performed by the transactions, as well as the commit or abort decisions. The log is used to undo or redo the effects of transactions in case of failures.
  - **Two-phase commit (2PC)**: A distributed transaction is coordinated by a designated site or node, called the **coordinator**, which communicates with the other sites or nodes, called the **participants**. The coordinator initiates the commit protocol, which consists of two phases:
    - **Prepare phase**: The coordinator asks each participant to prepare to commit, i.e., to flush its log to stable storage and vote either yes or no. A participant votes yes if it can commit, and no if it cannot or has aborted. The coordinator collects the votes from all participants.
    - **Commit phase**: The coordinator decides to commit the transaction if all participants voted yes, and to abort otherwise. The coordinator sends the decision to all participants, and waits for their acknowledgments. The participants execute the decision and send the acknowledgments to the coordinator.
  - **Three-phase commit (3PC)**: A variation of 2PC that adds a third phase, called the **pre-commit phase**, to avoid blocking in case of network failures. The pre-commit phase is between the prepare and commit phases, and involves the following steps:
    - **Pre-commit phase**: The coordinator decides to pre-commit the transaction if all participants voted yes, and to abort otherwise. The coordinator sends the decision to all participants, and waits for their acknowledgments. The participants execute the decision and send the acknowledgments to the coordinator.
    - **Commit phase**: The coordinator decides to commit the transaction if it has received the acknowledgments from all participants, and to abort otherwise. The coordinator sends the decision to all participants, and waits for their acknowledgments. The participants execute the decision and send the acknowledgments to the coordinator.
  - **Shadow versions**: An alternative to logging that avoids the need to undo or redo the effects of transactions. A shadow version is a copy of the data item that is modified by a transaction, which is stored in a separate location from the original data item. The original data item is not overwritten until the transaction commits, and the shadow version is discarded. If the transaction aborts, the original data item is unchanged, and the shadow version is discarded.



## Unit 10 - Replication

- Replication is the process of creating and maintaining multiple copies of the same data on different database servers.
- Replication provides benefits such as high availability, fault tolerance, load balancing, and scalability.
- Replication can be classified into two types: synchronous and asynchronous.
  - Synchronous replication ensures that all copies of the data are updated at the same time, but it may incur performance overhead and network latency.
  - Asynchronous replication allows updates to be applied to the copies at different times, but it may introduce data inconsistency and conflict resolution issues.
- Replication can be implemented using different architectures, such as master-slave, peer-to-peer, multi-master, and hybrid.
  - Master-slave replication involves one primary server (master) that receives all the updates and propagates them to one or more secondary servers (slaves) that only read the data.
  - Peer-to-peer replication involves multiple servers that can both read and write the data, and exchange updates among themselves using a gossip protocol.
  - Multi-master replication involves multiple servers that can both read and write the data, and coordinate updates using a consensus protocol or a conflict detection and resolution mechanism.
  - Hybrid replication combines different replication architectures to achieve the desired trade-offs between consistency, availability, and performance.
- Replication can be applied at different levels of granularity, such as statement-based, row-based, or logical.
  - Statement-based replication replicates the SQL statements that modify the data, and executes them on the replicas.
  - Row-based replication replicates the changes made to individual rows of the data, and applies them on the replicas.
  - Logical replication replicates the changes made to the logical entities of the data, such as tables, indexes, or views, and applies them on the replicas.



# System model and group communication for replication in distributed systems

- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by passing messages.
- Replication is a technique to create and maintain multiple copies of the same data or service on different processes in a distributed system.
- Replication can improve performance, availability, fault tolerance, and scalability of a distributed system, but also introduces challenges such as maintaining consistency and transparency among the replicas.
- A system model is a set of assumptions and abstractions that describe the properties and behaviors of a distributed system, such as the communication model, the failure model, the timing model, and the security model.
- A communication model defines how processes can exchange messages in a distributed system, such as the network topology, the message ordering, the message delivery, and the message reliability.
- A group communication model is a special case of a communication model that supports communication among a subset of processes in a distributed system, called a group.
- A group is a logical entity that represents a collection of processes that share some common interest or goal, such as a replicated service or a distributed application.
- Group communication can be classified into two types: broadcast communication and multicast communication.
- Broadcast communication is when a process sends a message to all other processes in the distributed system, regardless of their group membership.
- Multicast communication is when a process sends a message to a specific group of processes, identified by a group identifier or a group address.
- Group communication can also be characterized by the properties of the messages, such as the ordering, the reliability, the atomicity, and the causality.
- Ordering refers to the sequence in which messages are delivered to the processes in a group, which can be FIFO, causal, total, or causal-total.
- Reliability refers to the guarantee that messages are delivered to the processes in a group, which can be unreliable, reliable, or safe.
- Atomicity refers to the guarantee that messages are delivered to all or none of the processes in a group, which can be non-atomic or atomic.
- Causality refers to the guarantee that messages are delivered in a way that respects the potential causal dependencies among them, which can be non-causal or causal.
- Group communication can be implemented by various protocols and algorithms, such as IP multicast, reliable multicast, atomic multicast, causal multicast, and total order multicast.
- Group communication can be used to support replication in distributed systems, by providing mechanisms for creating, managing, and coordinating groups of replicas, and for disseminating updates and requests among them.
- Group communication can also be used to implement distributed consensus, which is a fundamental problem in replication, where a group of processes have to agree on a common value or decision, despite the possibility of failures and asynchrony.



# Fault-Tolerant Services for the Notes of the Unit 10 - Replication in the Subject of Distributed System

- Fault-tolerant services are services that can continue to function correctly even in the presence of failures, such as server crashes, network partitions, or malicious attacks.
- Replication is a technique for implementing fault-tolerant services by creating and maintaining multiple copies of the same service or data on different servers or locations.
- Replication can improve the availability, performance, and reliability of distributed systems, but also introduces challenges such as consistency, coordination, and recovery.
- There are two main classes of replication techniques: primary-backup replication and active replication.
  - Primary-backup replication: One server acts as the primary and handles all the requests from the clients, while the others act as backups and receive updates from the primary. The primary is responsible for ensuring the consistency and order of the updates. If the primary fails, one of the backups takes over as the new primary.
  - Active replication: All servers are active and execute the same requests from the clients in the same order. The servers use a consensus protocol to agree on the order of the requests. The clients receive responses from all servers and ignore the faulty ones.
- There are also different models of faults that can affect the replicated services: crash faults, omission faults, and Byzantine faults.
  - Crash faults: A server stops functioning and does not send or receive any messages.
  - Omission faults: A server fails to send or receive some messages, but otherwise functions correctly.
  - Byzantine faults: A server behaves arbitrarily and may send incorrect or conflicting messages to other servers or clients.
- The number and type of faults that a replicated service can tolerate depends on the replication technique and the assumptions about the system. For example, to tolerate f crash faults, a primary-backup replication scheme needs at least f+1 replicas, while an active replication scheme needs at least 2f+1 replicas. To tolerate f Byzantine faults, an active replication scheme needs at least 3f+1 replicas.
- Replication can also be combined with other techniques, such as coding theory, to achieve fault-tolerance with less overhead or more efficiency. For example, fused state machines use a combination of coding theory and replication to ensure low overhead during normal operations and savings in storage and messages, but may incur higher overhead during recovery from faults .



# Highly Available Services for the Notes of the Unit 10 - Replication in the Subject of Distributed System

- Replication is the process of creating and maintaining multiple copies of data in different locations in a distributed system.
- Replication can improve the availability, reliability, performance, and scalability of distributed services.
- Replication can also introduce challenges such as consistency, concurrency, and fault tolerance.
- There are different types of replication, such as:
  - Synchronous replication: The updates are propagated to all replicas before the operation is considered complete. This ensures strong consistency, but increases latency and reduces availability.
  - Asynchronous replication: The updates are propagated to some or all replicas after the operation is considered complete. This improves availability and performance, but may cause inconsistency or data loss.
  - Lazy replication: The updates are propagated to the replicas only when they are needed or requested. This reduces network traffic and storage overhead, but may increase response time and inconsistency.
- There are different strategies for managing replication, such as:
  - Primary-backup: One replica is designated as the primary, and the others are backups. The primary receives all the updates and propagates them to the backups. The backups take over the primary role in case of failure.
  - Quorum-based: Each replica has a vote, and a quorum is a subset of replicas that can decide on the outcome of an operation. The operation is considered complete if a quorum of replicas agrees on it. This can tolerate failures and improve availability, but may increase communication overhead and complexity.
  - Group communication: The replicas are organized into groups, and use multicast communication to exchange updates and coordinate actions. This can simplify the replication protocol and reduce network traffic, but may introduce ordering and delivery issues.
- There are different techniques for implementing replication, such as:
  - State machine replication: The replicas are modeled as deterministic state machines that execute the same sequence of commands. This ensures consistency and fault tolerance, but requires agreement on the command order and execution.
  - Data replication: The replicas store copies of the same data, and use update or query operations to access and modify them. This can improve performance and scalability, but requires consistency maintenance and conflict resolution.
  - Hybrid replication: The replicas combine state machine and data replication, and use different levels of consistency and synchronization depending on the application requirements. This can optimize the trade-offs between availability, performance, and consistency, but may increase complexity and overhead.



# Transactions with replicated data

- Transactions are a sequence of operations that are executed atomically, consistently, isolatedly, and durably (ACID properties) on a database system.
- Replication is the process of copying and maintaining data in multiple locations, such as different servers or nodes, to improve data availability, reliability, and performance.
- Transactions with replicated data are transactions that involve accessing or modifying data that is replicated across a distributed system.
- Transactions with replicated data pose some challenges, such as:
  - How to ensure that the replicas are consistent and synchronized with each other and with the source data?
  - How to handle concurrency control and recovery of replicated data in the presence of failures or network partitions?
  - How to balance the trade-off between data consistency and availability in a distributed system?
- There are different approaches to address these challenges, such as:
  - Replication protocols: These are algorithms that define how the replicas are updated and synchronized with each other and with the source data. Some examples are primary-backup, quorum-based, gossip-based, and log-based replication protocols.
  - Transaction models: These are abstractions that define the semantics and guarantees of transactions with replicated data. Some examples are one-copy serializability, snapshot isolation, eventual consistency, and causal consistency.
  - Replication architectures: These are design choices that affect the performance and scalability of transactions with replicated data. Some examples are master-slave, peer-to-peer, hierarchical, and hybrid replication architectures.

