

# Distributed System

A distributed system is a system whose components are located on different networked computers, which communicate and coordinate their actions by passing messages to one another. A distributed system can also be defined as a number of independent computers linked by a network, or a computing environment in which various components are spread across multiple computers (or other computing devices) on a network.

Some of the main characteristics of a distributed system are:

- The components are autonomous, meaning they can operate independently and have their own failure modes.
- The components are heterogeneous, meaning they can have different hardware, software, operating systems, and protocols.
- The components are scalable, meaning the system can handle increasing workload or number of components without significant degradation of performance or reliability.
- The components are transparent, meaning the system hides the complexity and distribution of the components from the users and applications.

Some of the main challenges of a distributed system are:

- The components are prone to failures, such as crashes, network partitions, or malicious attacks, and the system must be able to tolerate and recover from them.
- The components are concurrent, meaning they can execute simultaneously and interact with each other, and the system must ensure consistency and correctness of the shared data and state.
- The components are distributed, meaning they can have different physical locations, time zones, and network delays, and the system must cope with the latency and uncertainty of the communication.

Some of the main benefits of a distributed system are:

- The components are modular, meaning they can be reused, replaced, or added without affecting the rest of the system.
- The components are parallel, meaning they can exploit the computational power and resources of multiple machines to achieve higher performance and efficiency.
- The components are collaborative, meaning they can share information and services with each other to achieve common goals.

Some of the main examples of a distributed system are:

- The Internet, which is a global network of interconnected computers and devices that communicate using standard protocols and provide various services and applications.
- The World Wide Web, which is a collection of web servers and web browsers that exchange hypertext documents and multimedia content using HTTP and other protocols.
- The cloud computing, which is a model of providing on-demand access to a pool of shared and scalable computing resources, such as servers, storage, databases, and applications, over the Internet.
- The peer-to-peer networks, which are networks of equal nodes that cooperate to share resources and services without relying on a central authority or server.



## Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- The main characteristics of distributed systems are:
  - Concurrency: Multiple components can execute simultaneously and interact with each other.
  - No global clock: There is no shared physical clock among the components, so synchronization and coordination are challenging.
  - Independent failures: Each component can fail independently without affecting the whole system, so fault tolerance and recovery are important.
  - Heterogeneity: The components can have different hardware, software, network, data, and protocols, so interoperability and compatibility are required.
- The main advantages of distributed systems are:
  - Scalability: The system can grow in size and performance by adding more components without affecting the existing ones.
  - Availability: The system can tolerate failures of some components and still provide services to the users.
  - Transparency: The system can hide the complexity and diversity of the components from the users and provide a consistent and uniform interface.
  - Resource sharing: The system can allow the components to access and utilize the resources of other components, such as files, printers, sensors, etc.
- The main challenges of distributed systems are:
  - Communication: The system has to ensure reliable, efficient, and secure communication among the components over the network.
  - Coordination: The system has to coordinate the actions and states of the components to achieve a common goal or consistency.
  - Consistency: The system has to maintain a consistent view of the data and the system state among the components, despite concurrent updates and failures.
  - Security: The system has to protect the data and the system from unauthorized access, modification, or damage by malicious users or components.
  - Performance: The system has to optimize the use of the resources and the network to provide high-quality services to the users.



Hello, I am Sydney, your AI assistant. I can help you with writing notes on various topics. Here is the content I have generated for the topic of Introduction for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM.

```markdown
# Introduction

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- The main challenges of designing and implementing distributed systems are:
  - Heterogeneity: The system may consist of different types of computers, networks, operating systems, middleware, and applications.
  - Scalability: The system should be able to grow in size and complexity without losing its functionality and performance.
  - Failure handling: The system should be able to cope with partial failures of components, such as crashes, network partitions, or malicious attacks.
  - Security: The system should be able to protect its data and resources from unauthorized access, modification, or disclosure.
  - Concurrency: The system should be able to handle multiple concurrent requests from users or processes, and ensure consistency and correctness of the shared data and resources.
  - Transparency: The system should hide the complexity and diversity of its components from the users, and provide a uniform and simple interface.
- The main benefits of distributed systems are:
  - Resource sharing: The system can enable users to access and share remote resources, such as files, printers, databases, or web services.
  - Load balancing: The system can distribute the workload among multiple computers, and improve the performance and efficiency of the system.
  - Fault tolerance: The system can tolerate and recover from failures of some components, and provide continuous service to the users.
  - Availability: The system can provide high availability of the data and resources, and reduce the downtime of the system.
  - Scalability: The system can scale up or down according to the demand and capacity of the system, and support a large number of users and processes.
  - Distributed computing: The system can enable parallel and distributed computation of complex problems, and exploit the computational power of multiple computers.
```



### Examples of Distributed Systems

A distributed system is a collection of independent computers that communicate and coordinate their actions by passing messages. The computers in a distributed system may be physically close or geographically dispersed, and they may be connected by a network or a bus. Distributed systems can provide higher performance, reliability, scalability, and availability than centralized systems.

Some examples of distributed systems are:

- **Telecommunication networks**: Telephone networks are an early example of a peer-to-peer network, where each node can initiate or receive calls. Cellular and telephone networks are forms and examples of distributed networks. They use protocols such as TCP/IP, HTTP, and SMTP to exchange data and messages. Telecommunication networks also include the Internet, which is a global network of networks that connects millions of computers and devices. The Internet supports applications such as email, web browsing, social media, online gaming, and streaming services.  

- **Real-time systems**: Many industries use real-time systems distributed in various areas, locally and globally. Real-time systems are systems that have strict timing constraints and must respond to events within a specified deadline. For example, air traffic control systems, power grid systems, industrial control systems, and autonomous vehicles are real-time systems that require coordination and synchronization among distributed components. Real-time systems use protocols such as CAN, Ethernet, and MQTT to communicate and exchange data.  

- **Distributed database systems**: A distributed database is a database that has locations across multiple servers, physical locations, or both. A distributed database can improve performance, availability, and scalability by distributing the data and the workload among different nodes. For example, Google's Bigtable, Amazon's Dynamo, and Facebook's Cassandra are distributed database systems that store and process large amounts of data across thousands of servers. Distributed database systems use protocols such as Paxos, Raft, and Gossip to achieve consistency and fault tolerance.  

- **Distributed computing systems**: A distributed computing system is a system that uses multiple computers to perform a computation or a task that is too complex or resource-intensive for a single computer. For example, SETI@home, Folding@home, and Bitcoin are distributed computing systems that use the idle processing power of volunteers' computers to search for extraterrestrial intelligence, simulate protein folding, and validate cryptocurrency transactions, respectively. Distributed computing systems use protocols such as MPI, MapReduce, and Blockchain to coordinate and distribute the computation.



### Resource sharing and the web challenges in distributed systems

Resource sharing is the process of making the resources of a distributed system available to the users and applications in a transparent and efficient way. Resources can be hardware, software, or data. Resource sharing can be achieved by different methods, such as data migration, computation migration, task migration, and service migration .

The web is an example of a large-scale distributed system that enables resource sharing among heterogeneous and geographically dispersed computers. The web challenges in distributed systems are the issues and difficulties that arise from designing, implementing, and maintaining such a system. Some of the major web challenges are  :

- Scalability: The ability to handle increasing load and demand without degrading the performance or functionality of the system. Scalability can be achieved by adding more resources, replicating data and services, distributing the load, and caching.
- Heterogeneity: The diversity of the hardware, software, network, and data formats that are involved in the system. Heterogeneity can be handled by using common standards, protocols, and interfaces, such as HTTP, HTML, XML, and JSON.
- Fault tolerance: The ability to cope with failures and errors that may occur in the system, such as network congestion, server crashes, or malicious attacks. Fault tolerance can be achieved by using techniques such as redundancy, replication, backup, recovery, and consensus.
- Security: The protection of the system and its resources from unauthorized access, modification, or disclosure. Security can be achieved by using mechanisms such as encryption, authentication, authorization, and auditing.
- Consistency: The degree to which the system maintains a coherent and correct view of the data and services across the distributed components. Consistency can be affected by factors such as concurrency, replication, caching, and network delays. Consistency can be ensured by using protocols such as atomic transactions, locking, and quorum.
- Transparency: The degree to which the system hides the complexity and diversity of the distributed components from the users and applications. Transparency can be achieved by using techniques such as naming, location, migration, replication, and caching. Transparency can improve the usability, portability, and interoperability of the system.

: Resource sharing and web challenges in distributed systems - Brainly
: Resource Sharing and Web Challenges in Distributed System - TheCode11
: The Challenges in Distributed System - BrainKart



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of architectural models for distributed systems.

# Architectural models for distributed systems

- Architectural models describe the organization of components and their interrelationships in a distributed system.
- Architectural models can be classified into different types based on the placement, communication, and coordination of components across the network.
- Some common architectural models are:

## Client-server model

- In this model, there are two types of components: clients and servers.
- Clients initiate requests for services and servers provide responses to those requests.
- Clients and servers can be located on different machines and communicate over a network.
- Clients and servers can be implemented using different languages, platforms, and protocols.
- Client-server model forms the basis for multi-tier architectures, where servers can be further divided into tiers such as presentation, application, and data.

## Broker model

- In this model, there is an intermediate component called a broker that mediates the communication between clients and servers.
- The broker is responsible for locating the appropriate server for a client request, forwarding the request, and returning the response.
- The broker can also provide additional services such as load balancing, caching, security, and fault tolerance.
- The broker model is used by some middleware technologies such as CORBA, RMI, and DCOM.

## Service-oriented model

- In this model, there are multiple components that provide and consume services.
- Services are self-contained, reusable, and loosely coupled units of functionality that can be accessed over a network.
- Services are described by their interfaces, which specify the operations, inputs, outputs, and quality of service attributes.
- Services can be discovered, composed, and invoked dynamically using standard protocols such as SOAP, WSDL, and UDDI.
- Service-oriented model is used by some web technologies such as REST, XML, and JSON.

## Peer-to-peer model

- In this model, there are multiple components that act as both clients and servers.
- Components can communicate directly with each other without any central coordination or intermediation.
- Components can join and leave the network at any time and share resources such as files, CPU, and bandwidth.
- Peer-to-peer model can be classified into structured and unstructured based on the organization of the network topology and the routing of messages.
- Peer-to-peer model is used by some applications such as BitTorrent, Skype, and Bitcoin.



Hello, I am Sydney, your AI assistant. I can help you with your topic of fundamental models for distributed systems. Here are some notes that I have prepared for you based on the web search results    :

### Fundamental Models for Distributed Systems

- Fundamental models are descriptions of properties that are present in all distributed architectures, such as concurrency, scalability, transparency, and heterogeneity.
- Interaction models are issues dealing with the interaction of processes such as performance and timing of events, such as synchronous vs asynchronous communication, remote procedure calls, message passing, and event-based communication.
- Failure models are specifications of faults that can be exhibited by processes and communication channels, such as crash, omission, timing, response, arbitrary, and Byzantine faults.
- Security models are mechanisms for ensuring the confidentiality, integrity, and availability of data and services in distributed systems, such as encryption, authentication, authorization, and auditing.

Some key points to remember are:

- Distributed systems are composed of multiple components that communicate with each other by sending messages over a computer network.
- Distributed systems aim to provide a single coherent view of the system to an external actor, despite the possible heterogeneity, concurrency, and failures of the components.
- Distributed systems face challenges such as latency, bandwidth, scalability, consistency, fault tolerance, and security.
- Distributed systems can be modeled using different abstractions and paradigms, such as client-server, peer-to-peer, publish-subscribe, and map-reduce.




Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some content on the topic of Theoretical Foundation for Distributed System for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM.

### Theoretical Foundation for Distributed System

- A distributed system is a collection of processes that are spatially separated and do not share a common memory and communicate with one another by exchanging messages with arbitrary delays .
- Theoretical foundations of distributed systems aim to understand the inherent limitations, capabilities, and trade-offs of distributed systems and their algorithms.
- Some of the fundamental concepts and challenges in distributed systems are:
  - **Limitations of distributed systems**: Due to the lack of a global clock, a shared memory, and a reliable communication network, distributed systems face issues such as uncertainty, inconsistency, concurrency, and failures  .
  - **Logical clocks**: Logical clocks are a way of ordering events in a distributed system based on their causal relationships, rather than their physical timestamps. Logical clocks can be implemented using scalar values (Lamport clocks) or vector values (vector clocks) that are updated and exchanged with each message  .
  - **Message passing systems**: Message passing systems are a model of distributed computation where processes communicate by sending and receiving messages over a network. Message passing systems can be synchronous or asynchronous, reliable or unreliable, and FIFO or non-FIFO  .
  - **Consensus and agreement**: Consensus and agreement are problems of achieving a common decision or value among a set of processes in a distributed system, despite the presence of failures or faults. Consensus and agreement are essential for achieving coordination, consistency, and fault tolerance in distributed systems  .
  - **Distributed algorithms**: Distributed algorithms are algorithms that run on multiple processes in a distributed system and coordinate their actions by exchanging messages. Distributed algorithms can be designed for various problems and objectives, such as leader election, mutual exclusion, distributed sorting, distributed graph algorithms, etc  .



# Limitation of Distributed System

A distributed system is a collection of independent computers that communicate with each other over a network to achieve a common goal. Distributed systems have many advantages, such as scalability, fault-tolerance, availability, and performance. However, they also face some limitations that make them challenging to design and implement. Some of the main limitations of distributed systems are:

- **Absence of a global state**: In a distributed system, there is no single point of control or coordination for the entire system. Each computer has its own local state and view of the system, which may differ from the views of other computers. This makes it hard to reason about the behavior and correctness of the system, and to synchronize the actions and data of different computers. For example, it is difficult to ensure that all computers agree on the same value of a shared variable, or that all transactions are executed in a consistent order. To cope with this limitation, distributed systems use various techniques, such as consensus algorithms, distributed locking, and logical clocks, to achieve some form of agreement or consistency among the computers.

- **Absence of a global clock**: In a distributed system, there is no common physical clock that can be used to measure the time and order of events. Each computer has its own local clock, which may drift or be inaccurate. This makes it hard to determine the causal and temporal relationships between events that occur in different computers. For example, it is difficult to tell if a message was sent before or after another message, or if two events happened concurrently or sequentially. To cope with this limitation, distributed systems use various techniques, such as vector clocks, Lamport timestamps, and logical clocks, to assign logical timestamps to events and messages, and to compare their ordering.

- **Absence of shared memory**: In a distributed system, there is no shared memory that can be accessed by all computers. Each computer has its own local memory, which may contain different or outdated data. This makes it hard to share and update data among the computers, and to ensure the consistency and coherence of the data. For example, it is difficult to implement atomic operations, such as read-modify-write, or to guarantee that all computers see the same value of a shared variable. To cope with this limitation, distributed systems use various techniques, such as replication, caching, and distributed transactions, to store and synchronize data across the computers.

- **Network issues**: In a distributed system, the communication between the computers depends on the network, which may be unreliable, unpredictable, or insecure. The network may experience failures, delays, congestion, or attacks, which may affect the availability, performance, and security of the system. For example, a message may be lost, corrupted, duplicated, or delayed, or a computer may be isolated, partitioned, or compromised. To cope with this limitation, distributed systems use various techniques, such as error detection, retransmission, encryption, authentication, and fault-tolerance, to ensure the reliability, efficiency, and safety of the communication.



### Absence of Global Clock

- A global clock is a system-wide clock that is equally accessible to all processes in a distributed system and provides a common notion of time.
- A global clock is useful for determining the order of events and the state of the system across different processes.
- However, a global clock is hard to realize in distributed systems due to two inherent limitations: lack of shared memory and unpredictable message delays.
- Lack of shared memory means that processes in a distributed system do not have access to a common storage that can store and update the global clock value.
- Unpredictable message delays mean that processes in a distributed system cannot synchronize their local clocks with each other or with an external time source reliably and accurately.
- As a result, the absence of a global clock implies that:
  - Different processes may have different notions of time and their local clocks may drift apart over time.
  - It is not always possible to determine the order of events on different processes based on their timestamps or message exchanges.
  - It is not possible for an individual process to obtain an up-to-date and consistent state of the entire system by querying other processes.
  - It is difficult to obtain a meaningful global state of the system that reflects the states of different processes at the same point in time.



### Shared Memory

Shared memory is a programming model for distributed systems that allows multiple processes to access a common logical address space, which is distributed among the physical memories of multiple nodes. Shared memory can simplify the communication and synchronization among processes, as they can read and write to the same variables without explicit message passing. However, shared memory also introduces challenges such as consistency, coherence, fault tolerance, and scalability.

Some of the advantages of shared memory are:

- It provides a familiar and intuitive abstraction for programmers who are used to the uniprocessor memory model.
- It can improve the performance and efficiency of data access and transfer, as it reduces the overhead of message passing and network communication.
- It can support dynamic and irregular data structures, such as graphs and trees, that are difficult to partition and distribute among processes.
- It can enable fine-grained parallelism and load balancing, as processes can access any data item in the shared memory without prior knowledge or coordination.

Some of the disadvantages of shared memory are:

- It requires a complex and costly mechanism to maintain the consistency and coherence of the shared memory, as different processes may have different views and copies of the same data item.
- It may incur high latency and bandwidth consumption, as processes may need to fetch or update data items from remote nodes frequently.
- It may suffer from false sharing and contention, as processes may access or modify unrelated data items that are located in the same memory block or cache line.
- It may not scale well with the number of processes and nodes, as the shared memory size and the communication overhead may grow exponentially.

There are two main approaches to implement shared memory in distributed systems: hardware-based and software-based. Hardware-based shared memory relies on special hardware components, such as cache coherence circuits and network interface controllers, to provide a coherent and consistent view of the shared memory to all processes. Software-based shared memory relies on software mechanisms, such as virtual memory and distributed algorithms, to manage the shared memory at the operating system or application level. Software-based shared memory can be further classified into page-based, object-based, and tuple-based, depending on the granularity and structure of the shared data items.



### Logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A logical clock is a mechanism for capturing chronological and causal relationships in a distributed system  .
- A distributed system may have no physically synchronous global clock, so a logical clock allows global ordering on events from different processes in such systems .
- A logical clock is not a physical device, but a software counter that is incremented according to some rules .
- A logical clock can be used for computation analysis, distributed algorithm design, individual event tracking, and exploring computational progress.
- Some examples of logical clock algorithms are:
  - Lamport timestamps, which are monotonically increasing software counters that are updated based on the send and receive events of messages .
  - Vector clocks, which are arrays of software counters that are updated based on the send, receive, and local events of processes .
  - Matrix clocks, which are matrices of software counters that are updated based on the send, receive, and local events of processes and also capture the concurrency of events.
- A logical clock satisfies the following properties:
  - If two events are causally related, then the logical clock values of these events must reflect their causal order .
  - If two events are concurrent, then the logical clock values of these events must not reflect any specific order .
- A logical clock can be used to implement various distributed services, such as mutual exclusion, deadlock detection, snapshot, consensus, and causal broadcast .



### Lamport's & vectors logical clocks

- Lamport's logical clock is a procedure to determine the order of events occurring in a distributed system, where there is no global clock.
- Lamport's logical clock is based on the idea of a logical timestamp, which is a numerical value maintained by each process in the system.
- The logical timestamp reflects the causal order of events, such that if event A happens before event B, then the timestamp of A is less than the timestamp of B.
- The logical timestamp is updated according to the following rules:
  - When a process performs an internal event, it increments its logical clock by one.
  - When a process sends a message, it increments its logical clock by one and attaches the timestamp to the message.
  - When a process receives a message, it updates its logical clock to the maximum of its own clock and the timestamp in the message, and then increments it by one.
- Lamport's logical clock provides a total ordering of events consistent with causality, but it does not capture the concurrency of events. Two events that are concurrent (i.e., neither causally precedes nor follows the other) may have different timestamps depending on the order of message delivery.
- Vector clocks extend the capabilities of Lamport's logical clock to allow us to understand the ordering across multiple processes that cross communicate.
- Vector clocks are vectors of logical clocks, one clock per process in the system. Each process maintains a local copy of the global vector clock, and updates it according to the following rules:
  - When a process performs an internal event, it increments its own clock in the vector by one.
  - When a process sends a message, it increments its own clock in the vector by one and attaches the vector to the message.
  - When a process receives a message, it updates each entry in its vector to the maximum of its own entry and the corresponding entry in the message, and then increments its own clock by one.
- Vector clocks allow us to determine if any two arbitrarily selected events are causally dependent or concurrent. Two events are causally dependent if one of them causally precedes the other, and concurrent if neither causally precedes nor follows the other.
- The causal order of two events can be determined by comparing their vector clocks. If the vector clock of event A is less than the vector clock of event B in all entries, then A causally precedes B. If the vector clock of event A is greater than the vector clock of event B in all entries, then B causally precedes A. If neither of these conditions hold, then A and B are concurrent.
- Vector clocks provide a partial ordering of events consistent with causality and concurrency, but they are more complex and require more space than Lamport's logical clock. Each vector clock has N entries, where N is the number of processes in the system, and each entry is a logical clock that can grow arbitrarily large.



# Concepts in Message Passing Systems for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Message passing is a technique for invoking behavior on a computer by sending a message to a process.
- Message passing is used in distributed systems, where processes communicate by exchanging messages over a network  .
- Message passing systems provide a collection of message-based interprocess communication (IPC) protocols that hide the complexities of network protocols and heterogeneous platforms .
- Message passing systems can be classified into two categories: synchronous and asynchronous.
  - Synchronous message passing systems require the sender and the receiver to be ready at the same time for communication. The sender blocks until the receiver acknowledges the message, and the receiver blocks until a message arrives.
  - Asynchronous message passing systems do not require the sender and the receiver to be ready at the same time for communication. The sender does not block after sending a message, and the receiver can retrieve a message from a queue or a buffer at any time.
- Message passing systems can also be classified into two types: direct and indirect.
  - Direct message passing systems require the sender and the receiver to know each other's identities, such as process names or addresses. The sender specifies the destination of the message, and the receiver specifies the source of the message.
  - Indirect message passing systems do not require the sender and the receiver to know each other's identities. The sender and the receiver communicate through a shared entity, such as a mailbox, a port, or a topic. The sender deposits the message in the shared entity, and the receiver retrieves the message from the shared entity.
- Message passing systems can support different communication models, such as one-to-one, one-to-many, many-to-one, or many-to-many.
  - One-to-one communication model involves a single sender and a single receiver. This is also known as point-to-point or unicast communication.
  - One-to-many communication model involves a single sender and multiple receivers. This is also known as broadcast or multicast communication.
  - Many-to-one communication model involves multiple senders and a single receiver. This is also known as gather or anycast communication.
  - Many-to-many communication model involves multiple senders and multiple receivers. This is also known as scatter or all-to-all communication.
- Message passing systems can have different features, such as reliability, ordering, delivery, buffering, routing, security, etc.
  - Reliability refers to the ability of the message passing system to ensure that a message is delivered to the intended receiver without loss, duplication, or corruption.
  - Ordering refers to the ability of the message passing system to preserve the temporal or causal relationships among messages sent by the same or different senders.
  - Delivery refers to the ability of the message passing system to guarantee that a message is delivered to the receiver within a specified time or deadline.
  - Buffering refers to the ability of the message passing system to store messages temporarily in a queue or a buffer until they are delivered or retrieved.
  - Routing refers to the ability of the message passing system to select the best path or route for sending a message from the sender to the receiver over a network.
  - Security refers to the ability of the message passing system to protect the confidentiality, integrity, and authenticity of the messages and the processes involved in communication.



### Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems in the Subject of Distributed System

- Causal order is a way of ordering events in a distributed system based on their causal relationships, rather than their physical timestamps or locations.
- Causal order captures the notion of "happened before" or "influenced by" among events, regardless of when or where they occurred.
- Causal order is important for ensuring consistency, correctness, and coordination in distributed systems, especially for applications that involve communication, replication, synchronization, or concurrency control.
- Causal order can be defined formally using Lamport's logical clocks, which assign logical timestamps to events based on their causal dependencies, rather than their actual occurrence times.
- Causal order can be implemented using various algorithms or protocols, such as vector clocks, causal broadcast, causal multicast, or causal memory.
- Causal order can be classified into different types or levels, depending on how strict or relaxed the ordering constraints are. Some examples are:
  - Total-causal order: the strictest ordering in distributed systems; it establishes only one linearization, consistent with the causal ordering, among all the events that occur in the system, even those that occur concurrently .
  - Causal order: the standard ordering in distributed systems; it ensures that causally related events are ordered, but allows concurrent events to be unordered or differently ordered by different processes or observers .
  - Causal consistency: a weaker form of ordering in distributed systems; it guarantees that causally related events are seen in the same order by all processes or observers, but does not enforce any order on concurrent events.
- Causal order can be applied to various aspects or components of distributed systems, such as messages, operations, transactions, data, or processes. Some examples are:
  - Causal ordering of messages: a property of communication in distributed systems; it ensures that messages that are causally related are delivered in the same order by all receivers, and messages that are concurrent can be delivered in any order or different orders by different receivers.
  - Causal ordering of operations: a property of execution in distributed systems; it ensures that operations that are causally related are performed in the same order by all processes, and operations that are concurrent can be performed in any order or different orders by different processes.
  - Causal ordering of transactions: a property of concurrency control in distributed systems; it ensures that transactions that are causally related are committed in the same order by all participants, and transactions that are concurrent can be committed in any order or different orders by different participants.
  - Causal ordering of data: a property of consistency in distributed systems; it ensures that data that are causally related are updated in the same order by all replicas, and data that are concurrent can be updated in any order or different orders by different replicas.
  - Causal ordering of processes: a property of coordination in distributed systems; it ensures that processes that are causally related are synchronized in the same order by all participants, and processes that are concurrent can be synchronized in any order or different orders by different participants.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is some information on the topic of total order for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM.

### Total order

- A distributed system is a collection of independent entities that communicate by message passing.
- A distributed system is said to have **partial order** if we can have a **partial order relationship** among the events in the system. A partial order relationship is a binary relation that is **reflexive**, **antisymmetric**, and **transitive**. For example, if A and B are events in a distributed system, and A happens before B, then A is partially ordered with respect to B.
- If **totality**, i.e., causal relationship among all events in the system, can be established, then the system is said to have **total order**. A total order relationship is a partial order relationship that is also **linear**, meaning that for any two events A and B in the system, either A happens before B, or B happens before A, or A and B are concurrent. For example, if A and B are events in a distributed system, and A and B are causally related, then A is totally ordered with respect to B.
- Total order is very useful for distributed system implementation, as it can help ensure consistency, coordination, and agreement among the entities in the system. For example, if a system has a shared resource that can be used by only one entity at a time, then a total order can help determine which entity has the priority to access the resource.
- One way to implement total order in a distributed system is to use **Lamport timestamps**. Lamport timestamps are logical clocks that assign a numerical value to each event in the system, based on the partial order relationship. The value of a Lamport timestamp is determined by the following rules:
  - Each entity in the system maintains a counter that is initialized to zero.
  - Whenever an entity performs an internal event, it increments its counter by one and assigns the new value to the event as its timestamp.
  - Whenever an entity sends a message, it increments its counter by one and assigns the new value to the message as its timestamp.
  - Whenever an entity receives a message, it updates its counter to the maximum of its current value and the timestamp of the message, and then increments it by one and assigns the new value to the receive event as its timestamp.
- Lamport timestamps can be used to create a total order of events in a distributed system by using some arbitrary mechanism to break ties (e.g. the ID of the entity). For example, if A and B are events in a distributed system, and they have the same Lamport timestamp, then we can use the ID of the entity that performed the event to decide which event happens before the other. This way, we can establish a linear order among all events in the system.



### Total Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems in the Subject of Distributed System

- A distributed system is a collection of independent and autonomous processes that communicate and coordinate with each other by exchanging messages.
- Events are the actions or occurrences that happen in a distributed system, such as sending or receiving a message, executing a local operation, or detecting a failure.
- The ordering of events is a way of defining the temporal relationship between events in a distributed system. There are different types of ordering, such as partial order, causal order, and total order.
- A partial order is a binary relation that satisfies three properties: reflexivity, antisymmetry, and transitivity. A partial order relation is denoted by ≤.
- A causal order is a partial order that captures the notion of causality between events. If an event e1 causes or influences another event e2, then e1 is causally before e2, denoted by e1 → e2. The causal order relation satisfies the following rules:
  - If e1 and e2 are events in the same process and e1 occurs before e2, then e1 → e2 (local order).
  - If e1 is the sending of a message m and e2 is the receipt of the same message m, then e1 → e2 (message order).
  - If e1 → e2 and e2 → e3, then e1 → e3 (transitivity).
- A total order is a partial order that satisfies an additional property: totality. This means that for any two events e1 and e2 in the system, either e1 ≤ e2 or e2 ≤ e1. A total order relation is denoted by <.
- A total causal order is a total order that is consistent with the causal order. This means that if e1 → e2, then e1 < e2. A total causal order relation is denoted by <<.
- A total causal order is the strictest ordering in distributed systems; it establishes only one linearization, consistent with the causal ordering, among all the events that occur in the system, even those that occur concurrently. For that reason, the execution of the system is considered as synchronous.
- A total causal order can be implemented by using a logical clock, such as a vector clock, that assigns a timestamp to each event. The timestamp is a vector of integers that reflects the causal history of the event. The total causal order relation can be defined as follows:
  - For any two events e1 and e2 with timestamps t1 and t2, e1 << e2 if and only if t1 < t2, where t1 < t2 means that for all i, t1[i] ≤ t2[i] and there exists j such that t1[j] < t2[j].
- A total causal order can be used to provide fault tolerance and consistency for constructing reliable distributed systems. For example, it can be used to implement a total order broadcast, a communication primitive that ensures that all processes deliver the same set of messages in the same order. It can also be used to implement a distributed snapshot, a technique that captures the global state of the system at a certain point in time.



### Techniques for Message Ordering in Distributed Systems

- Message ordering is the problem of ensuring that messages are processed in a consistent and predictable order in a distributed system .
- Message ordering is important because it affects the final outcome of the actions and the consistency of the system state .
- There are different types of message ordering techniques, depending on the desired level of ordering guarantee and the trade-off between performance and complexity  .
- Some of the common message ordering techniques are:

  - **Unordered**: Messages are delivered in any order, without any guarantee of ordering. This is the simplest and fastest technique, but it may lead to inconsistent or incorrect results .
  - **FIFO**: Messages are delivered in the same order as they are sent by each sender. This technique ensures that messages from the same sender are ordered, but it does not guarantee any ordering among messages from different senders .
  - **Causal**: Messages are delivered in a way that respects the causal dependencies among them. This technique ensures that if a message m1 causally precedes a message m2, then m1 is delivered before m2 at every receiver. Causal ordering captures the logical order of events in a distributed system, but it may incur some overhead in terms of message timestamps and vector clocks  .
  - **Total**: Messages are delivered in the same order at every receiver. This technique ensures that all receivers see the same sequence of messages, but it may require a global agreement or a leader election among the senders .
  - **Synchronous**: Messages are delivered in rounds, where each round consists of a set of messages that are sent and received by all processes in the system. This technique ensures that all receivers see the same sequence of messages and that each message is delivered within a bounded time, but it may require a high degree of synchronization and fault tolerance among the processes .

- Different message ordering techniques can be implemented using different protocols, such as:

  - **Unicast**: A protocol that sends a message to a single receiver. Unicast protocols can provide unordered or FIFO ordering, depending on the underlying network .
  - **Multicast**: A protocol that sends a message to a group of receivers. Multicast protocols can provide unordered, FIFO, causal, total, or synchronous ordering, depending on the algorithm used  .
  - **Broadcast**: A protocol that sends a message to all processes in the system. Broadcast protocols can provide unordered, FIFO, causal, total, or synchronous ordering, depending on the algorithm used .

- Message ordering techniques can be applied to different scenarios and applications in distributed systems, such as:

  - **Replication**: The problem of maintaining multiple copies of the same data or service in a distributed system. Message ordering techniques can ensure that the replicas are consistent and up-to-date .
  - **Consensus**: The problem of reaching an agreement among a set of processes in a distributed system. Message ordering techniques can ensure that the processes have a common view of the system state and the decisions made .
  - **Coordination**: The problem of managing the dependencies and interactions among a set of processes in a distributed system. Message ordering techniques can ensure that the processes execute their tasks in a correct and efficient way .



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of causal ordering of messages for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM.

### Causal ordering of messages

- Causal ordering of messages is a property of a distributed system that ensures that messages are delivered in a consistent and logical order, according to the causal relationships among events in the system.
- Causal relationships among events are defined by the **happened-before** relation, denoted by `->`, which is a partial order that satisfies the following conditions:
  - If `a` and `b` are events in the same process, and `a` occurs before `b`, then `a -> b`.
  - If `a` is the event of sending a message by one process and `b` is the event of receiving that message by another process, then `a -> b`.
  - If `a -> b` and `b -> c`, then `a -> c` (transitivity).
- Two events `a` and `b` are **concurrent**, denoted by `a || b`, if neither `a -> b` nor `b -> a` holds.
- A message delivery order is **causally ordered** if for any two messages `m` and `m'`, if the send event of `m` happened before the send event of `m'`, then the receive event of `m` also happened before the receive event of `m'`.
- Causal ordering of messages is important for maintaining the consistency and correctness of distributed applications that rely on the exchange of information among processes.
- Causal ordering of messages can be implemented by various algorithms, such as vector clocks, logical clocks, or causal broadcast protocols. These algorithms use different mechanisms to encode and propagate the causal dependencies among messages, such as timestamps, counters, or piggybacking information.



### Global State for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent processes that communicate through message passing.
- The global state of a distributed system is the union of the local states of the processes and the channels .
- A local state of a process is the values of its variables, registers, program counter, etc. at a given point in time.
- A channel state is the set of messages that have been sent but not yet received by the processes.
- A global state is consistent if it reflects a possible execution of the system, i.e., no causal violations occur .
- A causal violation is when a message is received before it is sent, or a process observes the effect of a message before it observes the message itself.
- A consistent global state can be used for debugging, checkpointing, termination detection, garbage collection, etc. in distributed systems  .
- A consistent global state can be recorded by using distributed snapshot algorithms, which are protocols that allow processes to coordinate and capture their local states and channel states without blocking or synchronizing .
- A distributed snapshot algorithm must satisfy two properties: completeness and accuracy.
  - Completeness means that every process records its local state and every message in transit is recorded by either the sender or the receiver.
  - Accuracy means that the recorded global state is consistent, i.e., no causal violations occur.
- There are different types of distributed snapshot algorithms, such as Chandy-Lamport, Lai-Yang, Mattern, etc. that differ in their assumptions, communication patterns, and complexity .



### Termination Detection for Distributed Systems

Termination detection is a fundamental problem in distributed systems, where a set of processes cooperate to perform a computation. The goal is to determine when all the processes have finished their work and there are no more messages in transit between them. This is useful for coordinating the next phase of the computation, releasing resources, or reporting the final result.

There are different algorithms for termination detection, depending on the assumptions and properties of the distributed system. One of the most well-known algorithms is Huang's algorithm, proposed by Shing-Tsaan Huang in 1989. Huang's algorithm is based on the concept of a distributed snapshot, which is a consistent global state of the system captured by recording the local states of the processes and the messages in the communication channels.

Huang's algorithm works as follows:

- The algorithm is initiated by a designated process, called the initiator, which is also responsible for announcing the termination when detected.
- The initiator starts a snapshot by sending a special message, called a marker, to all its neighbors and recording its local state.
- When a process receives a marker for the first time, it records its local state and sends a marker to all its neighbors. It also starts recording the incoming messages from each neighbor until it receives a marker from that neighbor.
- When a process receives a marker from a neighbor, it stops recording the incoming messages from that neighbor and sends the recorded messages, called the control information, back to the initiator.
- The initiator collects the control information from all its neighbors and computes the total number of messages in transit in the system. If this number is zero, then the system has terminated and the initiator announces it to all the processes.

Some of the properties and advantages of Huang's algorithm are:

- It is a distributed algorithm, meaning that no process has complete knowledge of the global state or the termination status of the system.
- It is a non-blocking algorithm, meaning that it does not interfere with the normal execution of the processes or the communication channels.
- It is a message-optimal algorithm, meaning that it uses the minimum number of messages required for termination detection, which is equal to the number of edges in the communication graph plus one.
- It is a general algorithm, meaning that it does not depend on the nature or structure of the computation or the communication pattern of the processes.



# Unit 2 - Distributed Mutual Exclusion

- Distributed mutual exclusion is a fundamental problem in distributed computing systems  .
- It ensures that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner  .
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion. Message passing is the sole means for implementing distributed mutual exclusion .
- There are three basic approaches for implementing distributed mutual exclusion:
  - Token-based algorithms: A process can enter the critical section only if it possesses a unique token. The token is passed among the processes in a predefined order or by request.
  - Permission-based algorithms: A process can enter the critical section only if it obtains permission from all or a subset of other processes in the system. The process sends request messages and waits for reply messages before entering the critical section.
  - Quorum-based algorithms: A process can enter the critical section only if it obtains permission from a majority or a quorum of processes in the system. The process sends request messages and waits for reply messages from a quorum before entering the critical section.
- The performance of distributed mutual exclusion algorithms can be measured by the following metrics :
  - Message complexity: The number of messages exchanged per critical section entry.
  - Synchronization delay: The time elapsed between the instant a process requests to enter the critical section and the instant it is allowed to do so, assuming that no other process is in the critical section.
  - System throughput: The number of times the critical section is executed per unit time in the system.
- Some examples of distributed mutual exclusion algorithms are:
  - Ricart-Agrawala algorithm: A permission-based algorithm that uses a logical clock to order the requests and replies. It has a message complexity of 2(N-1) per critical section entry, where N is the number of processes in the system .
  - Lamport's bakery algorithm: A token-based algorithm that uses a logical clock and a queue to order the requests and grant the token. It has a message complexity of 3(N-1) per critical section entry, where N is the number of processes in the system .
  - Maekawa's algorithm: A quorum-based algorithm that uses a voting set of processes to grant permission. It has a message complexity of 2√N per critical section entry, where N is the number of processes in the system .



### Classification of distributed mutual exclusion

Distributed mutual exclusion is a problem of ensuring that only one process in a distributed system can access a shared resource or data at a time. It is a fundamental requirement for achieving consistency, coordination and synchronization among the processes.

There are three basic approaches for implementing distributed mutual exclusion:

- **Token-based approach**: A unique token is shared among the sites. A site is allowed to enter its critical section if it possesses the token. Mutual exclusion is ensured because the token is unique. Examples of token-based algorithms are Ricart-Agrawala algorithm, Suzuki-Kasami algorithm, Raymond's tree-based algorithm, etc.
- **Non-token-based approach**: There is no token in this approach. Instead, a site requests permission from other sites before entering its critical section. A site is allowed to enter its critical section if it receives permission from all or a majority of other sites. Examples of non-token-based algorithms are Lamport's algorithm, Ricart-Agrawala algorithm with optimization, Maekawa's algorithm, etc.
- **Quorum-based approach**: This is a generalization of the non-token-based approach. A site requests permission from a subset of sites, called a quorum, before entering its critical section. A site is allowed to enter its critical section if it receives permission from all the sites in its quorum. Examples of quorum-based algorithms are Maekawa's algorithm, Sankararaman's algorithm, Agrawala-El Abbadi algorithm, etc.

The main criteria for evaluating the performance of distributed mutual exclusion algorithms are:

- **Message complexity**: The number of messages exchanged per critical section entry.
- **Synchronization delay**: The time elapsed between a site's request and its entry to the critical section.
- **Fault tolerance**: The ability of the algorithm to handle failures of sites or communication links.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of requirement of mutual exclusion theorem for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM.

```markdown
### Requirement of mutual exclusion theorem

- Mutual exclusion theorem is a fundamental property of distributed systems that ensures that only one process can access a shared resource at a time.
- Mutual exclusion theorem is required for the following reasons:
  - To prevent concurrent access to a shared resource that may result in inconsistency, corruption, or deadlock.
  - To ensure the correctness and validity of the operations performed on the shared resource by different processes.
  - To synchronize the activities and events of the processes that depend on the shared resource.
  - To avoid race conditions and conflicts that may arise due to concurrent access to the shared resource.
- Mutual exclusion theorem can be achieved by using various algorithms and protocols that coordinate the processes and grant them permission to access the shared resource in a distributed manner.
- Some of the common algorithms and protocols for mutual exclusion theorem are:
  - Centralized algorithm: A single coordinator process is responsible for granting access to the shared resource based on a request queue.
  - Distributed algorithm: Each process maintains a local request queue and communicates with other processes to reach an agreement on the access order.
  - Token-based algorithm: A special message called token is circulated among the processes and only the process that holds the token can access the shared resource.
  - Quorum-based algorithm: Each process contacts a subset of processes called quorum and obtains their votes to access the shared resource.
```



### Token based and non token based algorithms for distributed mutual exclusion

Distributed mutual exclusion (DME) is the problem of ensuring that only one process at a time can access a shared resource in a distributed system. There are two main approaches to solve this problem: token based and non token based algorithms.

- Token based algorithms
  - In token based algorithms, a unique token is shared among all the processes in the system. The token represents the permission to enter the critical section. Only the process that holds the token can access the shared resource. The token is passed from one process to another according to some protocol.
  - Token based algorithms have the advantage of avoiding unnecessary message exchanges and ensuring fairness among the processes. However, they also have some drawbacks, such as the possibility of losing the token due to failures, the overhead of maintaining the token, and the delay of waiting for the token.
  - Some examples of token based algorithms are:
    - Suzuki-Kasami algorithm: This is a modification of Ricart-Agrawala algorithm, a permission based algorithm that uses REQUEST and REPLY messages to ensure mutual exclusion. In Suzuki-Kasami algorithm, the token is a vector that records the number of requests made by each process. The token is sent to the process that has the highest request number and has not received the token yet. This algorithm ensures fairness and reduces the number of messages .
    - Raymond's algorithm: This is a tree-based algorithm that organizes the processes into a logical tree. The token is initially held by the root of the tree. A process that wants to enter the critical section sends a REQUEST message to its parent in the tree. The parent forwards the request to the root if it does not have the token. The root sends the token to the requester along the path of the requests. When a process releases the token, it sends it to its parent or to a child that has requested it. This algorithm minimizes the number of messages and the path length of the token.
    - Maekawa's algorithm: This is a quorum-based algorithm that divides the processes into disjoint subsets called quorums. Each process belongs to at least one quorum. A process that wants to enter the critical section sends a REQUEST message to all the processes in its quorum. It can enter the critical section only if it receives a REPLY message from all of them. A process that holds the token can grant a REPLY message to only one requester at a time. When a process exits the critical section, it sends a RELEASE message to all the processes in its quorum. This algorithm reduces the number of messages and ensures deadlock-freedom, but it may not be fair.

- Non token based algorithms
  - In non token based algorithms, there is no token in the system. Instead, the processes communicate with each other using messages to determine who should enter the critical section. The messages may contain timestamps or other information to order the requests and to resolve conflicts.
  - Non token based algorithms have the advantage of avoiding the problems of token loss, token maintenance, and token delay. However, they also have some drawbacks, such as the need for more message exchanges, the possibility of starvation, and the dependence on clock synchronization.
  - Some examples of non token based algorithms are:
    - Lamport's algorithm: This is a timestamp-based algorithm that uses logical clocks to order the requests. A process that wants to enter the critical section sends a REQUEST message with its timestamp to all the other processes. It can enter the critical section only if it receives a REPLY message from all of them. A process that receives a REQUEST message replies with a REPLY message if it is not in the critical section or if it has a lower priority than the requester. A process that exits the critical section sends a RELEASE message to all the other processes. This algorithm ensures mutual exclusion and preserves the request order, but it may cause starvation and requires a lot of messages.
    - Ricart-Agrawala algorithm: This is an optimization of Lamport's algorithm that reduces the number of messages. A process that wants to enter the critical section sends a REQUEST message with its timestamp to all the other processes. It can enter the critical section only if it receives a REPLY message from all of them. A process that receives a REQUEST message replies with a REPLY message if it is not in the critical section or if it has a lower priority than the requester. Otherwise, it defers the reply until it exits the critical section. A process that exits the critical section sends a REPLY message to all



### Performance Metrics for Distributed Mutual Exclusion Algorithms

Distributed mutual exclusion algorithms are algorithms that ensure that only one process can access a shared resource at a time in a distributed system. There are different types of distributed mutual exclusion algorithms, such as token-based, non-token-based, and quorum-based algorithms. To compare and evaluate the performance of these algorithms, some metrics are used, such as  :

- **Response time**: The interval of time when a request waits for the end of its critical section execution after its solicitation messages have been delivered. This metric measures the latency of the algorithm to grant access to the resource.
- **Synchronization delay**: The interval of time when a process waits for the end of its critical section execution after it has received the permission to enter the critical section. This metric measures the overhead of the algorithm to synchronize the processes.
- **Message complexity**: The number of messages exchanged per critical section execution. This metric measures the communication cost of the algorithm.
- **System throughput**: The number of critical section executions per unit time. This metric measures the efficiency of the algorithm to utilize the resource.
- **Fairness**: The degree to which the algorithm satisfies the requests in the order of their arrival. This metric measures the quality of service of the algorithm.

Some trade-offs may exist between these metrics, depending on the characteristics of the distributed system and the algorithm. For example, a lower response time may imply a higher message complexity, or a higher system throughput may imply a lower fairness. Therefore, the choice of the best algorithm for a given system may depend on the relative importance of these metrics.



## Unit 3 - Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set.
- Deadlocks can be handled by three strategies: deadlock prevention, deadlock avoidance, and deadlock detection.
- Deadlock prevention and avoidance are impractical in distributed systems, because they require global knowledge and coordination of the system state.
- Deadlock detection is the best approach to handle deadlocks in distributed systems.
- Deadlock detection entails two basic issues: detection of existing deadlocks and resolution of detected deadlocks.
- Detection of existing deadlocks requires examination of the status of process-resource interactions for presence of cyclic wait.
- Resolution of detected deadlocks requires aborting one or more deadlocked processes to break the cycle.
- There are three approaches to detect deadlocks in distributed systems: centralized, hierarchical, and distributed.
- Centralized approach: one node is designated as the deadlock detector and collects the local wait-for graphs from all the nodes to construct a global wait-for graph and check for cycles .
- Hierarchical approach: the nodes are organized into a tree structure and each node collects the local wait-for graphs from its children and sends them to its parent, until the root node constructs a global wait-for graph and checks for cycles.
- Distributed approach: each node maintains its own local wait-for graph and initiates a probe message to detect cycles in the system, using algorithms such as edge chasing, diffusing computation, or echo.
- Each approach has its own advantages and disadvantages in terms of communication cost, detection latency, and fault tolerance.



### System Model for Distributed Deadlock Detection

- A distributed system consists of a set of nodes that communicate by message passing.
- Each node has a set of resources that can be requested by processes running on the node or on other nodes.
- A process can request a resource by sending a message to the node that owns the resource.
- A node can grant a resource to a process by sending a message to the process or by placing the resource in a shared buffer.
- A process can release a resource by sending a message to the node that owns the resource or by removing the resource from a shared buffer.
- A process can hold multiple resources at a time and can request additional resources while holding some resources.
- A process can wait for a resource that is currently held by another process.
- A deadlock occurs when a set of processes are waiting for resources that are held by other processes in the set, and no process can proceed until some other process releases a resource.
- A wait-for graph (WFG) is a directed graph that represents the waiting relationships among processes and resources in the system.
- A node in the WFG is either a process or a resource, and an edge from a node A to a node B means that A is waiting for B.
- A cycle in the WFG indicates the presence of a deadlock in the system.



### Resource Vs Communication Deadlocks

- A deadlock is a condition where a process cannot proceed because it needs to obtain a resource held by another process, and it itself is holding a resource that the other process needs.
- There are two types of deadlocks in distributed systems: resource deadlocks and communication deadlocks.
- Resource deadlocks occur when processes access resources, such as data objects in database systems and buffers in store and forward communication networks . A process acquires a resource before accessing it and releasing it after using it. A resource deadlock happens when a cycle of processes is waiting for resources held by other processes in the cycle.
- Communication deadlocks occur when processes communicate by sending and receiving messages, such as in message passing systems and distributed shared memory systems . A process sends a message to another process and waits for a reply. A communication deadlock happens when a cycle of processes is waiting for messages from other processes in the cycle.
- The main difference between resource deadlocks and communication deadlocks is that resource deadlocks involve contention for resources, while communication deadlocks involve loss or corruption of messages. Resource deadlocks can be prevented by using resource allocation protocols, such as ordering, preemption, or timeouts. Communication deadlocks can be prevented by using reliable communication protocols, such as acknowledgments, retransmissions, or timeouts.
- Another difference between resource deadlocks and communication deadlocks is that resource deadlocks can be detected by using global or local wait-for graphs, while communication deadlocks can be detected by using timestamps or counters. A wait-for graph is a directed graph that represents the dependencies between processes and resources or messages. A cycle in the wait-for graph indicates a deadlock. A timestamp or a counter is a value that indicates the order or the number of messages sent or received by a process. A mismatch in the timestamps or counters indicates a deadlock.



### Deadlock Prevention for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process. In a distributed system, deadlocks are more difficult to detect and resolve because the processes and resources may be physically dispersed across different nodes.

Deadlock prevention is a technique to avoid the occurrence of deadlocks by ensuring that at least one of the four necessary conditions for deadlock (mutual exclusion, hold and wait, no preemption, and circular wait) is never satisfied.

There are two main methods of deadlock prevention in a distributed system:

- Ordered request: In this method, each resource type is assigned a unique level, and a process can request resources only in increasing order of levels. This prevents circular wait condition, as there is a global ordering of resource requests.
- Collective request: In this method, a process must request all the resources it needs in one single message, and wait for the grant of all of them before proceeding. This prevents hold and wait condition, as a process does not hold any resource while waiting for another.

Some advantages of deadlock prevention are:

- It is simple and easy to implement.
- It does not require any additional overhead for deadlock detection and recovery.

Some disadvantages of deadlock prevention are:

- It may impose unnecessary restrictions on resource utilization and process execution.
- It may not be applicable for some types of resources or processes that require dynamic and unpredictable resource requests.



### Avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- Deadlock avoidance is a technique that prevents the occurrence of deadlocks by ensuring that the system is always in a safe state.
- A safe state is a state where there exists a safe sequence of processes that can finish their execution without causing a deadlock.
- In a distributed system, deadlock avoidance is impractical because of the following reasons :
  - The system is dynamic and unpredictable, making it hard to know the current and future resource requests and releases of each process.
  - The system is decentralized and autonomous, making it hard to coordinate and synchronize the resource allocation decisions of each site.
  - The system is heterogeneous and complex, making it hard to define and enforce a global ordering of resources and processes.
- Therefore, deadlock detection is preferred over deadlock avoidance in distributed systems. Deadlock detection involves finding and resolving the existing deadlocks in the system.
- Deadlock detection in distributed systems can be classified into four categories :
  - Path-pushing algorithms: These algorithms propagate the information about the wait-for relations along the dependency paths in the system. A deadlock is detected when a cycle is formed in the wait-for graph.
  - Edge-chasing algorithms: These algorithms send probe messages along the dependency paths in the system. A deadlock is detected when a probe message returns to its originator.
  - Diffusion computation algorithms: These algorithms initiate a distributed computation at each site that detects a potential deadlock. A deadlock is confirmed when all the sites involved in the computation agree on the existence of a cycle.
  - Global state detection algorithms: These algorithms collect the local state information of each site and construct a global state of the system. A deadlock is detected when the global state contains a cycle in the wait-for graph.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of distributed deadlock detection and resolution:

### Distributed Deadlock Detection and Resolution

- A deadlock is a situation where a set of processes are blocked waiting for resources held by other processes in the set.
- In a distributed system, deadlocks can occur due to conflicting requests for resources across multiple sites or nodes.
- Distributed deadlock detection and resolution involves two steps: detecting the existence of deadlocks and breaking the deadlocks by releasing some resources or aborting some processes.
- There are three main approaches for distributed deadlock detection:
  - Centralized approach: A single site or node is designated as the deadlock detector and maintains a global wait-for graph (WFG) that represents the dependencies among processes and resources. The detector periodically searches the WFG for cycles, which indicate deadlocks, and initiates resolution actions. This approach is simple and efficient, but suffers from a single point of failure and a high communication overhead.
  - Distributed approach: Each site or node maintains a local WFG that represents the dependencies among processes and resources within the site or node. The sites or nodes exchange messages to construct a global WFG and detect cycles. This approach is fault-tolerant and scalable, but requires a large number of messages and a complex coordination protocol.
  - Hierarchical approach: The sites or nodes are organized into a hierarchy of clusters, each with a local deadlock detector. The detectors communicate with each other to construct a global WFG and detect cycles. This approach is a compromise between the centralized and distributed approaches, and reduces the communication and computation costs.
- There are two main methods for distributed deadlock resolution:
  - Preemption: Some processes are rolled back and release their resources, allowing other processes to proceed. This method preserves the work done by the processes, but may cause cascading rollbacks and inconsistency issues.
  - Abort: Some processes are terminated and release their resources, allowing other processes to proceed. This method is simple and fast, but may cause lost work and missed deadlines.



# Centralized Deadlock Detection

- This is a technique used in distributed systems to handle deadlock detection.
- According to this technique, the system maintains one global wait-for graph in a single chosen site, which is named as deadlock-detection coordinator.
- The coordinator collects information about the local wait-for graphs of each site and constructs the global wait-for graph.
- The coordinator periodically runs a deadlock detection algorithm on the global wait-for graph and identifies any cycles that indicate deadlocks.
- The coordinator then informs the involved sites to abort one or more processes to resolve the deadlock.
- The advantages of this technique are simplicity and low communication overhead.
- The disadvantages of this technique are the dependency on a single coordinator, which can be a bottleneck or a single point of failure, and the possibility of false deadlocks due to stale information .



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

## Global wait-for graph (WFG) approach

- A wait-for graph is a directed graph that represents the waiting relationships among processes and resources.
- A node in the graph can be either a process or a resource, and an edge from node A to node B means that A is waiting for B.
- A cycle in the graph indicates a deadlock.
- In the global WFG approach, a centralized or distributed algorithm is used to construct a global WFG from the local WFGs of each site.
- The global WFG is then examined for cycles to detect deadlocks.
- The advantages of this approach are:
  - It is simple and easy to implement
  - It can detect all deadlocks in the system
- The disadvantages of this approach are:
  - It requires a lot of communication and computation overhead
  - It may introduce false deadlocks due to stale information
  - It may not be scalable or fault-tolerant

## Local wait-for graph (LWFG) approach

- In the local WFG approach, each site maintains its own local WFG and periodically sends it to a designated deadlock detector.
- The deadlock detector merges the received local WFGs into a global WFG and checks for cycles to detect deadlocks.
- The advantages of this approach are:
  - It reduces the communication and computation overhead compared to the global WFG approach
  - It can detect all deadlocks in the system
- The disadvantages of this approach are:
  - It still requires some communication and computation overhead
  - It may introduce false deadlocks due to stale information
  - It may not be scalable or fault-tolerant

## Path-pushing (edge-chasing) approach

- In the path-pushing approach, each site maintains a local WFG and sends a probe message along the edges of the graph to detect cycles.
- A probe message contains the identifier of the initiator site and the path of the message so far.
- When a site receives a probe message, it checks if the message has reached the initiator site or if it has visited the site before.
- If either condition is true, a cycle is detected and a deadlock is reported.
- Otherwise, the site appends its identifier to the path and forwards the message along the outgoing edges of the graph.
- The advantages of this approach are:
  - It does not require a global WFG or a deadlock detector
  - It does not introduce false deadlocks due to stale information
  - It is scalable and fault-tolerant
- The disadvantages of this approach are:
  - It may generate a lot of probe messages and cause network congestion
  - It may not detect all deadlocks in the system
  - It may have a long detection delay



# Path Pushing Algorithms for Distributed Deadlock Detection

- Path pushing algorithms detect distributed deadlocks by maintaining an explicit global wait-for graph (WFG) at each site of the distributed system .
- The global WFG is a directed graph that represents the dependencies among the processes in the system. A node in the graph is a process and an edge from node P to node Q means that P is waiting for a resource held by Q.
- The basic idea is to build and update the global WFG at each site whenever a deadlock computation is performed. A site initiates a deadlock computation when it detects a local deadlock or receives a request from another site.
- When a site performs a deadlock computation, it sends its local WFG to all neighboring sites, where a neighboring site is a site that shares a common edge with the sender in the global WFG.
- Each site that receives a local WFG merges it with its own local WFG to form a new global WFG and sends the updated global WFG to its neighbors.
- This process continues until all sites have the same global WFG, which reflects the current state of the system.
- A site can detect a distributed deadlock by checking if there is a cycle in the global WFG that involves one of its local processes.
- The advantages of path pushing algorithms are that they can detect deadlocks quickly and accurately, and they do not require any additional messages for deadlock detection.
- The disadvantages of path pushing algorithms are that they require a lot of storage space and communication bandwidth to maintain and exchange the global WFG, and they may cause false deadlock detection due to the delay and inconsistency of the global WFG.



### Edge Chasing Algorithms for Distributed Deadlock Detection

- Edge chasing algorithms are a class of distributed deadlock detection algorithms that use special messages called probes to trace the dependency graph of processes and resources in a distributed system.
- A probe is a triplet (i, j, k) that denotes that the deadlock detection is initiated by process P_i and the message is being sent by the home site of process P_j to the home site of process P_k.
- The probe message follows the edges of the dependency graph from the initiator to the blocked processes and back to the initiator, forming a cycle if a deadlock exists.
- The most common edge chasing algorithm is the Chandy-Misra-Haas algorithm, which works for the AND request model, where a process can request multiple resources simultaneously and wait for all of them to be granted.
- The Chandy-Misra-Haas algorithm works as follows:

  - Each process maintains a wait-for graph (WFG) that contains the processes and resources that it is waiting for or holding.
  - When a process P_i initiates a deadlock detection, it sends a probe (i, i, j) to the home site of each process P_j that it is waiting for in its WFG.
  - When a process P_j receives a probe (i, k, j) from the home site of process P_k, it does the following:
    - If P_j is not waiting for any other process, it discards the probe.
    - If P_j is the initiator P_i, it detects a deadlock and terminates the detection.
    - If P_j is waiting for some other processes, it adds the edge (k, j) to its WFG and sends a probe (i, j, l) to the home site of each process P_l that it is waiting for in its WFG.
  - The algorithm terminates when either a deadlock is detected or all the probes are discarded.

- The advantages of edge chasing algorithms are:

  - They are simple and efficient, requiring only O(n) messages per detection, where n is the number of processes in the system.
  - They do not require global knowledge of the system state or a central coordinator.
  - They can detect deadlocks involving multiple resources and cycles of arbitrary length.

- The disadvantages of edge chasing algorithms are:

  - They may generate false positives, detecting cycles that do not correspond to actual deadlocks, due to the asynchronous nature of the system and the possibility of message delays or losses.
  - They may generate false negatives, missing some deadlocks, due to the concurrent initiation of multiple detections or the concurrent execution of requests and releases.
  - They may incur high communication overhead, especially in systems with high resource contention and frequent deadlock detection.



## Unit 4 - Agreement Protocols

- Agreement protocols are a class of distributed algorithms that allow a set of processes to reach a consensus on a value or a decision, despite the presence of failures or uncertainties.
- Agreement protocols are useful for solving problems such as leader election, distributed commit, atomic broadcast, and fault tolerance.
- Agreement protocols can be classified into two types: **synchronous** and **asynchronous**.
  - Synchronous protocols assume that there are known bounds on the message delays and the process speeds, and use timeouts or rounds to coordinate the processes.
  - Asynchronous protocols do not make any assumptions about the timing of the system, and rely on message ordering or logical clocks to ensure progress.
- Agreement protocols can also be characterized by the following properties: **validity**, **agreement**, **termination**, and **fault tolerance**.
  - Validity means that the agreed value must be one of the proposed values by the processes.
  - Agreement means that all correct processes must agree on the same value.
  - Termination means that all correct processes must eventually decide on a value.
  - Fault tolerance means that the protocol can tolerate a certain number of faulty processes, such as crashed, Byzantine, or malicious processes.
- Some examples of agreement protocols are:
  - **Paxos**, which is a family of asynchronous protocols that can tolerate up to half of the processes being crashed, and guarantee safety (validity and agreement) under all circumstances, and liveness (termination) under some assumptions.
  - **Raft**, which is a synchronous protocol that can tolerate up to half of the processes being crashed, and guarantee safety and liveness, as well as simplicity and understandability.
  - **Two-phase commit (2PC)**, which is a synchronous protocol that can tolerate up to one process being crashed, and guarantee atomicity and durability of a distributed transaction, but may block if the coordinator fails.
  - **Three-phase commit (3PC)**, which is a synchronous protocol that can tolerate up to one process being crashed, and guarantee atomicity and durability of a distributed transaction, as well as non-blocking, but may violate consistency if there are network partitions.
  - **Practical Byzantine Fault Tolerance (PBFT)**, which is a synchronous protocol that can tolerate up to one-third of the processes being Byzantine, and guarantee safety and liveness, as well as high performance and scalability.



Hello, I am Sydney, your AI assistant. I can help you with writing notes on various topics. Here is the content I have generated for the topic of Introduction for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM.

### Introduction for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- Agreement protocols are a class of protocols that allow a set of processes in a distributed system to reach a consensus on some value or action, despite the possibility of failures or malicious behavior.
- Agreement protocols are essential for ensuring the correctness, consistency, and availability of distributed systems, especially in the presence of faults or attacks.
- Some examples of agreement problems are:
  - Election: A set of processes need to elect a leader or a coordinator among themselves.
  - Atomic commit: A set of processes need to agree on whether to commit or abort a distributed transaction.
  - Byzantine agreement: A set of processes need to agree on a common value, even if some of them are faulty or malicious and may send conflicting or incorrect messages.
  - Consensus: A set of processes need to agree on a single value, starting from their own initial values, and the agreed value must be one of the initial values.
- Some of the challenges and requirements for designing agreement protocols are:
  - Fault tolerance: The protocol should be able to tolerate a certain number of process failures, such as crashes, omissions, or arbitrary behavior.
  - Asynchrony: The protocol should be able to cope with the uncertainty and variability of message delays, processing speeds, and clock drifts in a distributed system.
  - Termination: The protocol should guarantee that every correct process eventually decides on a value or an action.
  - Validity: The protocol should guarantee that the decided value or action satisfies some validity condition, such as being one of the proposed values or being consistent with the system state.
  - Agreement: The protocol should guarantee that every correct process decides on the same value or action.
- Some of the techniques and tools for designing and analyzing agreement protocols are:
  - Failure models: These are assumptions and abstractions that capture the types and the number of failures that a protocol can handle, such as crash failures, omission failures, or Byzantine failures.
  - Communication models: These are assumptions and abstractions that capture the properties and the limitations of the communication channels in a distributed system, such as reliable or unreliable, synchronous or asynchronous, or authenticated or unauthenticated.
  - Algorithmic paradigms: These are general approaches and strategies that can be used to construct agreement protocols, such as rounds, quorums, broadcasts, or reductions.
  - Proof techniques: These are methods and principles that can be used to prove the correctness and the performance of agreement protocols, such as invariants, induction, contradiction, or impossibility results.



### System models for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

A system model is a description of the properties and assumptions of a distributed system that are relevant for its design and analysis. System models can help us understand the behavior, limitations, and challenges of distributed systems, as well as compare and evaluate different solutions.

There are different types of system models, depending on the aspects of the system that we want to focus on. Some of the most common system models are:

- **Architectural models**: These models capture the hardware composition of a system in terms of computers and other devices and their interconnecting network. They also describe the responsibilities and placement of system components, such as clients, servers, peers, brokers, etc. Architectural models can help us design the structure and communication patterns of a distributed system.

- **Interaction models**: These models capture the communication and coordination mechanisms of a system, such as message passing, remote procedure calls, publish-subscribe, shared memory, etc. They also describe the properties and guarantees of these mechanisms, such as reliability, ordering, atomicity, consistency, etc. Interaction models can help us design the protocols and algorithms of a distributed system.

- **Fault models**: These models capture the possible failures and errors that can occur in a system, such as node crashes, network partitions, message losses, corrupted data, etc. They also describe the assumptions and expectations of the system in the presence of faults, such as fault detection, fault tolerance, fault recovery, etc. Fault models can help us design the resilience and reliability of a distributed system.

- **Timing models**: These models capture the temporal aspects of a system, such as clock synchronization, time bounds, latency, throughput, etc. They also describe the assumptions and expectations of the system in terms of timing, such as synchrony, asynchrony, partial synchrony, etc. Timing models can help us design the performance and scalability of a distributed system.

- **Consensus models**: These models capture the problem of achieving agreement among a set of nodes in a system, such as electing a leader, committing a transaction, ordering events, etc. They also describe the assumptions and expectations of the system in terms of consensus, such as safety, liveness, termination, etc. Consensus models can help us design the correctness and consistency of a distributed system.

Some examples of system models for distributed systems are:

- **Client-server model**: This is an architectural model where the system consists of two types of components: clients and servers. Clients request services from servers, and servers provide services to clients. Servers can be centralized or distributed, and clients can be thin or thick. This model is widely used for web applications, databases, file systems, etc.

- **Peer-to-peer model**: This is an architectural model where the system consists of a set of peers that are equal and autonomous. Peers can act as both clients and servers, and can communicate and cooperate with each other. Peers can form structured or unstructured overlays, and can join or leave the system dynamically. This model is widely used for file sharing, streaming, distributed hash tables, etc.

- **Message passing model**: This is an interaction model where the system uses messages as the basic unit of communication. Messages can be sent and received by nodes using various protocols, such as TCP, UDP, HTTP, etc. Messages can have different properties and guarantees, such as reliability, ordering, delivery, etc. This model is widely used for distributed algorithms, middleware, distributed objects, etc.

- **Publish-subscribe model**: This is an interaction model where the system uses events as the basic unit of communication. Events can be published by nodes to topics, and can be subscribed by nodes that are interested in those topics. Events can have different properties and guarantees, such as reliability, ordering, filtering, etc. This model is widely used for event-driven systems, notification systems, data streams, etc.

- **Crash-recovery model**: This is a fault model where the system assumes that nodes can fail by crashing, but can recover after some time. Nodes can have persistent or volatile state, and can use checkpoints or logs to recover their state. Nodes can detect failures by using timeouts or heartbeats, and can tolerate failures by using replication or redundancy. This model is widely used for distributed databases, distributed file systems, distributed transactions, etc.

- **Byzantine model**: This is a fault model where the system assumes that nodes can fail in arbitrary ways, such as sending incorrect or malicious messages, deviating from the protocol, colluding with other nodes, etc. Nodes can have different trust levels,



### Classification of Agreement Problem

An agreement problem in distributed systems is a problem where a set of processes need to agree on a common value or decision, despite the possibility of failures or malicious behavior. Agreement problems are fundamental to achieving fault tolerance and consistency in distributed systems.

There are different types of agreement problems, depending on the assumptions and requirements of the system. Some of the well-known agreement problems are:

- **Byzantine agreement problem**: A single value, which is to be agreed on, is initialized by an arbitrary process and all non-faulty processes have to agree on that value. The processes may be subject to Byzantine failures, which means they can behave arbitrarily or maliciously. The goal is to ensure that all non-faulty processes agree on the same value, and that value is the initial value of some non-faulty process  .
- **Consensus problem**: A generalization of the Byzantine agreement problem, where each process can propose a value and all non-faulty processes have to agree on a common value. The value must satisfy two properties: validity (the agreed value must be one of the proposed values) and agreement (all non-faulty processes must agree on the same value). The processes may be subject to different types of failures, such as crash, omission, or Byzantine  .
- **Interactive consistency problem**: A variation of the Byzantine agreement problem, where each process has an initial value and all non-faulty processes have to agree on a vector of values, one for each process. The vector must satisfy two properties: validity (the value for each process must be its initial value or the default value) and agreement (all non-faulty processes must agree on the same vector). The processes may be subject to Byzantine failures .

These problems are related to each other and have different applications in distributed systems. For example, Byzantine agreement can be used to implement reliable broadcast, consensus can be used to implement atomic commit or state machine replication, and interactive consistency can be used to implement group membership or fault diagnosis.



### Byzantine agreement problem

The Byzantine agreement problem is a fundamental challenge in fault-tolerant distributed computing. It requires a set of parties in a distributed system to agree on a common value, even if some of the parties are faulty or malicious. The problem is also known as the Byzantine generals problem, the interactive consistency problem, or the source congruency problem.

The problem was first defined and solved by Lamport et al. in 1982, using the analogy of several divisions of the Byzantine army camped outside an enemy city, each division commanded by its own general. The generals can communicate with one another only by messenger. After observing the enemy, they must decide upon a common plan of action, such as attack or retreat. However, some of the generals may be traitors, who try to prevent the loyal generals from reaching agreement. The problem is to find an algorithm that allows the loyal generals to agree on a common plan, while tolerating a certain number of traitors.

Some of the main aspects of the Byzantine agreement problem are:

- The number of parties (n) and the number of faulty parties (f) in the system. The problem is solvable only if n > 3f, meaning that the number of loyal parties must be more than three times the number of traitors.
- The type of faults that the parties may exhibit. The faults can be crash faults, where a party simply stops functioning, or Byzantine faults, where a party may behave arbitrarily, including sending conflicting or misleading messages to different parties.
- The type of communication channels that the parties use. The channels can be synchronous or asynchronous, meaning that the messages are delivered within a known or unknown time bound, respectively. The channels can also be authenticated or unauthenticated, meaning that the messages are signed or not by the sender, respectively.
- The type of agreement that the parties must reach. The agreement can be binary, where the parties must decide on a single bit (0 or 1), or multivalued, where the parties must decide on a value from a larger domain. The agreement can also be interactive or non-interactive, meaning that the parties can exchange multiple or a single round of messages, respectively.

Some of the main properties of the Byzantine agreement problem are:

- Validity: If all the parties start with the same initial value, then they must all decide on that value.
- Agreement: No two loyal parties can decide on different values.
- Termination: All loyal parties must eventually decide on a value.

Some of the main solutions to the Byzantine agreement problem are:

- The oral messages algorithm: This is a synchronous and interactive algorithm that uses unauthenticated channels and tolerates f < n/3 Byzantine faults. It requires f+1 rounds of message exchange, where each party sends its current value to all other parties, and then updates its value based on a majority vote of the received values.
- The signed messages algorithm: This is a synchronous and interactive algorithm that uses authenticated channels and tolerates f < n/2 Byzantine faults. It requires two rounds of message exchange, where each party sends its initial value signed by itself to all other parties, and then decides on the value that has the most signatures from distinct parties.
- The common coin algorithm: This is a synchronous and non-interactive algorithm that uses unauthenticated channels and tolerates f < n/3 Byzantine faults. It requires a single round of message exchange, where each party sends a random bit to all other parties, and then decides on the value that is the exclusive-or of all the received bits.
- The randomised algorithm: This is an asynchronous and interactive algorithm that uses unauthenticated channels and tolerates f < n/3 Byzantine faults. It requires an expected constant number of rounds of message exchange, where each party sends a random bit to all other parties, and then decides on the value that has the highest probability of being the majority of the received bits.



# Consensus problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- The consensus problem is the problem of getting a set of nodes in a distributed system to agree on something - it might be a value, a course of action or a decision.
- Achieving consensus allows a distributed system to act as a single entity, with every individual node aware of and in agreement with the actions of the whole of the network.
- Consensus is a general agreement on a decision made by the majority of those involved.
- Consensus is needed in a distributed system to ensure overall system reliability on top of unreliable system components.
- Consensus is also needed to coordinate distributed transactions, replicate data, elect leaders, and achieve fault tolerance.
- There are many ways in which processes in a distributed system can reach a consensus, but there is usually a trade-off between security and performance.
- The more we want our algorithm to be secure against ways in which failure can happen, the less performant it tends to become.
- Some of the common types of failures that can affect consensus are:
  - Crash failures: A process stops executing and does not resume.
  - Byzantine failures: A process behaves arbitrarily or maliciously.
  - Network failures: A message is lost, delayed, duplicated, or corrupted.
- Some of the common consensus algorithms are:
  - Two-phase commit: A coordinator process initiates a transaction and asks other processes to vote on whether to commit or abort.
  - Paxos: A leader-based algorithm that uses multiple rounds of proposals and acceptances to reach a consensus on a single value.
  - Raft: A simplified version of Paxos that uses a leader election phase and a log replication phase to achieve consensus on a sequence of values.
  - Byzantine fault tolerance: A class of algorithms that can tolerate up to one-third of processes being faulty or malicious.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on the interactive consistency problem for the notes of the unit 4 - agreement protocols in the subject of distributed system.

### Interactive consistency problem

- Interactive consistency is the problem in which n distinct nodes, each having its own private value, where up to t may be Byzantine, run an algorithm that allows all non-faulty nodes to infer the values of each other node  .
- Byzantine nodes are nodes that can behave arbitrarily, such as sending conflicting or incorrect messages, or remaining silent.
- The goal of interactive consistency is to reach agreement in a distributed system in the presence of faults.
- Interactive consistency is also known as the generals problem, as it can be seen as a generalization of the Byzantine generals problem.
- The Byzantine generals problem is a special case of interactive consistency where the nodes have to agree on a common value, such as whether to attack or retreat.
- Interactive consistency is a fundamental problem in computer science, as it is relevant to critical applications that rely on the combination of the opinions of multiple peers to provide a service, such as voting, fault-tolerant replication, or distributed ledger .

### Solutions for interactive consistency problem

- There are different algorithms for solving interactive consistency problem, depending on the assumptions and the communication model of the distributed system  .
- Some of the assumptions are:
  - The number of nodes n and the number of Byzantine nodes t are known in advance  .
  - The nodes have unique identifiers and can authenticate each other  .
  - The nodes can communicate through reliable and ordered channels  .
- Some of the communication models are:
  - Synchronous: the nodes have bounded message delays and clock drifts  .
  - Asynchronous: the nodes have no bounds on message delays and clock drifts  .
  - Partially synchronous: the nodes have bounded message delays and clock drifts after some unknown global stabilization time  .
- Some of the algorithms are:
  - Oral messages algorithm: a synchronous algorithm that uses message authentication and requires n > 3t .
  - Signed messages algorithm: a synchronous algorithm that uses digital signatures and requires n > 2t .
  - Randomized algorithm: an asynchronous algorithm that uses random coin flips and requires n > 3t.
  - Hybrid algorithm: a partially synchronous algorithm that uses a combination of broadcast and randomized Byzantine consensus algorithms and requires n > 3t.

### References

: Pease, M., Shostak, R., and Lamport, L. (1980). Reaching agreement in the presence of faults. Journal of the ACM, 27(2), 228-234.

: The Code 11. (2022). Interactive Consistency Problem in Distributed System. Retrieved from https://www.thecode11.com/2022/07/interactive-consistency-problem-in-distributed-system.html

: Cachin, C., Kursawe, K., and Shoup, V. (2014). Interactive consistency in practical, mostly-asynchronous systems. arXiv preprint arXiv:1410.7256.

: Kulkarni, S., and Martin, J. (2021). On achieving interactive consistency in real-world distributed systems. Journal of Parallel and Distributed Computing, 147, 1-14.



### Solution to Byzantine Agreement problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- The Byzantine agreement problem is a fundamental problem in fault tolerant distributed computing that requires a set of parties in a distributed environment to agree on a value even if some of the parties are corrupted.
- The problem was first defined by Lamport and is also known as the interactive consistency problem.
- The problem can be illustrated by the analogy of the Byzantine generals problem, where several divisions of the Byzantine army are camped outside an enemy city, each division commanded by its own general. The generals can communicate with one another only by messenger. After observing the enemy, they must decide upon a common plan of action, such as attack or retreat. However, some of the generals may be traitors and try to sabotage the plan by sending false messages or no messages at all.
- A solution to the Byzantine agreement problem must satisfy the following properties:
  - **Agreement**: All honest parties must agree on the same value.
  - **Validity**: If all honest parties start with the same value, they must agree on that value.
  - **Termination**: All honest parties must eventually decide on a value.
- A solution to the Byzantine agreement problem also depends on the following assumptions:
  - **Synchrony**: There is a known upper bound on the message delivery time and the processing time of each party.
  - **Authentication**: The messages sent by each party can be verified to be authentic and not tampered with.
  - **Majority**: The number of honest parties is greater than the number of corrupted parties.
- A simple solution to the Byzantine agreement problem is the following algorithm:
  - Each party starts with an initial value, either 0 or 1.
  - Each party broadcasts its initial value to all other parties.
  - Each party collects the values received from all other parties and computes the majority value among them.
  - Each party decides on the majority value as the final value.
- This solution works if there is at most one corrupted party, since the majority value will always be the same as the initial value of the honest parties. However, if there are more than one corrupted parties, they can send different values to different parties and cause disagreement.
- To tolerate more corrupted parties, a more sophisticated solution is needed. One such solution is the **Oral Messages** algorithm proposed by Lamport, which works as follows:
  - The algorithm is executed in rounds, where each round consists of two phases: **send** and **receive**.
  - In the first round, the source party (the one that initiates the agreement) broadcasts its initial value to all other parties. This is the **send** phase of the first round.
  - In the **receive** phase of the first round, each party receives the value from the source party and stores it as its own value.
  - In the second round, each party broadcasts its value to all other parties. This is the **send** phase of the second round.
  - In the **receive** phase of the second round, each party receives the values from all other parties and computes the majority value among them. This is the value of the second round.
  - The algorithm continues for k rounds, where k is the number of corrupted parties that can be tolerated. In each round, each party broadcasts its value of the previous round and computes the majority value of the current round.
  - After k rounds, each party decides on the value of the k-th round as the final value.
- The Oral Messages algorithm works if the number of corrupted parties is less than one third of the total number of parties, i.e., k < n/3, where n is the total number of parties. This is because in each round, the majority value will always be the same as the value of the honest parties, and the corrupted parties cannot change the majority value by sending different values to different parties.
- The Oral Messages algorithm requires n^k+1 messages to be exchanged, where n is the total number of parties and k is the number of corrupted parties that can be tolerated. This is because in each round, each party sends one message to each of the other n-1 parties, and there are k+1 rounds in total. Therefore, the algorithm is inefficient and impractical for large values of n and k.
- To improve the efficiency of the Oral Messages algorithm, several optimizations have been proposed, such as



# Application of Agreement problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- Agreement problem is a fundamental problem in distributed computing and multi-agent systems, where a set of processes need to coordinate and reach a common decision or value, despite the presence of faults or failures .
- Agreement problem has many variants, such as consensus, atomic commitment, atomic broadcast, and group membership. Each variant has different assumptions, requirements, and guarantees.
- Consensus is the most basic and general form of agreement problem, where each process proposes a value and all correct processes must agree on the same value, which must be one of the proposed values . Consensus is essential for implementing fault-tolerant services, such as replicated state machines, leader election, distributed transactions, and distributed locking.
- Atomic commitment is a special case of consensus, where each process has a binary value (commit or abort) and all correct processes must agree on the same value, which must be commit if and only if all processes have commit as their initial value . Atomic commitment is useful for ensuring the atomicity and durability of distributed transactions, where a transaction either commits or aborts at all participating sites.
- Atomic broadcast is another special case of consensus, where each process broadcasts a message and all correct processes must deliver the same set of messages in the same order . Atomic broadcast is useful for implementing total order multicast, where messages are delivered to all processes in a consistent order, regardless of the network delays or failures.
- Group membership is a related problem to consensus, where each process maintains a view of the current set of processes in the system, and all correct processes must agree on the same view, which must reflect the actual failures and recoveries of processes . Group membership is useful for implementing fault detection, fault notification, and fault recovery mechanisms, as well as for maintaining consistent replicas of data or services.



### Atomic Commit in Distributed Database System

- An atomic commit is an operation that applies a set of distinct changes as a single operation. If the changes are applied, then the atomic commit is said to have succeeded. If the changes are not applied, then the atomic commit is said to have failed or aborted.
- In distributed database systems, the primary need for commit protocols is to maintain the atomicity of distributed transactions. A distributed transaction is a transaction that accesses data from multiple sites in a distributed system .
- Atomic commitment issue is of prime importance in the distributed system and the issue becomes more necessary to deal with if some of the sites participating in the execution of the transaction commitment fail .
- An atomic commit protocol is a protocol that coordinates the distinct operations of a distributed transaction and then commits or aborts the transaction as needed. An atomic commit protocol guarantees, in spite of possible failures, that either all the sites agree to commit the transaction, or all the sites agree to abort the transaction .
- There are two main types of atomic commit protocols: blocking and non-blocking. Blocking protocols require that some sites wait for the recovery of other failed sites before deciding the outcome of the transaction. Non-blocking protocols do not require such waiting and can decide the outcome of the transaction even if some sites fail .
- Some examples of blocking protocols are two-phase commit (2PC) and three-phase commit (3PC). Some examples of non-blocking protocols are Paxos commit, consensus commit, and FLAC  .



# Unit 5 - Distributed Resource Management

Distributed resource management (DRM) is an evolving discipline that aims to enable distributed enterprise systems to operate effectively in production. DRM involves a set of software, hardware, network tools, procedures and policies for managing the resources of a distributed system, such as computing, storage, communication, and energy. DRM can be applied to various domains, such as cloud computing, grid computing, edge computing, and distributed energy systems.

Some of the main objectives of DRM are:

- To optimize the utilization and performance of the distributed resources, by allocating them to the tasks that need them, according to the system requirements and constraints.
- To ensure the reliability and availability of the distributed resources, by monitoring their status, detecting and recovering from failures, and providing backup and redundancy mechanisms.
- To enhance the scalability and flexibility of the distributed system, by allowing the addition and removal of resources dynamically, and adapting to the changes in the workload and environment.
- To support the security and privacy of the distributed system, by enforcing the access control and authentication policies, and protecting the data and communication channels.

Some of the main challenges of DRM are:

- To deal with the heterogeneity and diversity of the distributed resources, which may have different types, capabilities, configurations, and interfaces.
- To cope with the uncertainty and dynamism of the distributed system, which may experience fluctuations in the demand, supply, and quality of the resources, as well as failures and faults.
- To coordinate and synchronize the distributed resources, which may have dependencies, conflicts, and interactions among them, and may operate in different locations, time zones, and domains.
- To balance the trade-offs and conflicts among the different objectives and constraints of the DRM, such as performance, cost, energy, reliability, and security.

Some of the main components of a DRM system are:

- A resource discovery component, which is responsible for identifying and locating the available resources in the distributed system, and providing information about their characteristics and status.
- A resource scheduling component, which is responsible for assigning and allocating the resources to the tasks that need them, and optimizing the resource utilization and performance.
- A resource monitoring component, which is responsible for collecting and analyzing the data about the resource usage, performance, and quality, and providing feedback and alerts to the other components.
- A resource management component, which is responsible for controlling and adjusting the resource allocation and configuration, and enforcing the DRM policies and rules.
- A resource coordination component, which is responsible for facilitating the communication and collaboration among the distributed resources, and resolving the conflicts and dependencies among them.



### Issues in distributed file systems

A distributed file system (DFS) is a system that allows multiple clients to access and manipulate files stored on one or more servers over a network. A DFS provides the abstraction of a single, shared namespace for files, regardless of their physical location or distribution. A DFS can improve the performance, reliability, scalability, and security of file access and management.

However, designing and implementing a DFS also involves many challenges and issues, such as:

- **Naming and transparency**: How to assign unique and meaningful names to files and directories in a DFS? How to support different naming schemes and conventions? How to provide location transparency, replication transparency, migration transparency, and concurrency transparency to the users and applications?
- **Consistency and caching**: How to ensure that the files and directories in a DFS are consistent across different servers and clients? How to handle concurrent updates and conflicts? How to use caching techniques to improve the performance and availability of file access? How to maintain cache consistency and coherence?
- **Replication and fault tolerance**: How to replicate files and directories in a DFS to improve the reliability, availability, and scalability of the system? How to handle failures and recoveries of servers and clients? How to balance the load and distribute the workload among different servers and clients?
- **Security and access control**: How to protect the files and directories in a DFS from unauthorized access and modification? How to enforce different access policies and permissions for different users and groups? How to provide authentication, encryption, and auditing mechanisms for file access and management?
- **Performance and scalability**: How to optimize the performance and efficiency of file access and management in a DFS? How to reduce the network overhead and latency? How to handle the heterogeneity and diversity of servers and clients? How to support the growth and evolution of the system?

These are some of the main issues that need to be addressed in the design and use of a distributed file system. Different DFS solutions may adopt different approaches and techniques to deal with these issues, depending on their requirements and objectives. Some examples of DFS solutions are NFS, AFS, Coda, HDFS, and IPFS    .



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the mechanism for building distributed file systems for the notes of the Unit 5 - Distributed Resource Management in the subject of DISTRIBUTED SYSTEM.

### Mechanism for building distributed file systems

- A distributed file system (DFS) is a file system that enables clients to access file storage from multiple hosts through a computer network as if the user was accessing local storage  .
- Files are spread across multiple storage servers and in multiple locations, which enables users to share data and storage resources  .
- A DFS can provide benefits such as fault tolerance, scalability, performance, and transparency .
- There are different mechanisms for building distributed file systems, such as:
  - **Naming and name resolution**: This mechanism deals with how files and directories are named and located in a DFS. A common approach is to use a hierarchical namespace that maps logical names to physical locations, such as a path name or a uniform resource locator (URL) . A name resolution service is responsible for translating logical names to physical locations, such as a domain name system (DNS) or a distributed hash table (DHT) .
  - **File access and consistency**: This mechanism deals with how files are accessed and modified by clients in a DFS. A common approach is to use a client-server model, where clients send requests to servers that store and manage files . A file access protocol is used to define the format and semantics of the requests and responses, such as a network file system (NFS) or a common internet file system (CIFS) . A file consistency model is used to define the rules and guarantees for the visibility and ordering of file updates, such as a sequential consistency or an eventual consistency .
  - **Replication and caching**: This mechanism deals with how files are replicated and cached in a DFS. A common approach is to use a replication strategy, where files are duplicated on multiple servers for fault tolerance and load balancing . A replication protocol is used to coordinate the updates and synchronization of replicas, such as a primary-backup protocol or a quorum protocol . A caching strategy, where files are temporarily stored on local or intermediate nodes for performance and bandwidth reduction . A caching protocol is used to maintain the consistency and coherence of cached files, such as a write-through protocol or a write-back protocol .
  - **Security and privacy**: This mechanism deals with how files are protected and secured in a DFS. A common approach is to use a security policy, where files are assigned access rights and permissions based on users and groups . A security protocol is used to enforce the security policy and provide authentication, authorization, encryption, and auditing services, such as a Kerberos protocol or a public key infrastructure (PKI) . A privacy policy, where files are anonymized and encrypted to prevent unauthorized access and disclosure . A privacy protocol is used to implement the privacy policy and provide data masking, obfuscation, and encryption services, such as a homomorphic encryption or a differential privacy .



### Design issues in Distributed Shared Memory

Distributed Shared Memory (DSM) is a mechanism that allows multiple processes on different nodes to share a common logical address space and access data transparently. DSM can simplify the programming of distributed applications and improve the performance and scalability of parallel systems. However, DSM also introduces several design issues that need to be addressed carefully. Some of the main design issues are:

- **Granularity**: Granularity refers to the size of the unit of sharing and the unit of coherence in a DSM system. A smaller granularity (such as a word or a cache line) can reduce the amount of data transferred and the false sharing problem, but it can also increase the overhead of coherence maintenance and the network traffic. A larger granularity (such as a page or a segment) can reduce the overhead and the traffic, but it can also increase the amount of data transferred and the false sharing problem. Therefore, a trade-off between granularity and performance needs to be considered, and some adaptive or hybrid schemes may be used to adjust the granularity dynamically according to the application behavior and the system state.

- **Structure**: Structure refers to the organization and layout of the shared data in the memory. The structure can be flat or hierarchical, static or dynamic, uniform or non-uniform, etc. The structure can affect the performance, scalability, and portability of a DSM system. For example, a flat and static structure can simplify the address translation and the coherence maintenance, but it can also limit the scalability and the flexibility of the system. A hierarchical and dynamic structure can improve the scalability and the flexibility of the system, but it can also increase the complexity and the overhead of the system.

- **Coherence semantics**: Coherence semantics refers to the consistency model that defines the rules and guarantees for the ordering and visibility of the shared data accesses in a DSM system. Different coherence semantics can have different impacts on the performance, correctness, and portability of a DSM system. For example, a strict coherence semantics (such as sequential consistency or linearizability) can ensure the correctness and the portability of the system, but it can also impose a high performance penalty and a high synchronization cost. A relaxed coherence semantics (such as release consistency or eventual consistency) can improve the performance and the scalability of the system, but it can also introduce the possibility of data inconsistency and the need for explicit synchronization.

- **Scalability**: Scalability refers to the ability of a DSM system to maintain or improve its performance and efficiency as the number of nodes and processes increases. Scalability can be affected by many factors, such as the granularity, the structure, the coherence semantics, the network topology, the communication protocol, the load balancing, the fault tolerance, etc. A scalable DSM system should be able to adapt to the changes in the system size and the workload, and to exploit the locality and the parallelism of the applications.

- **Heterogeneity**: Heterogeneity refers to the diversity and variability of the hardware and software components in a DSM system. Heterogeneity can exist in the processor architecture, the memory organization, the network interface, the operating system, the compiler, the programming language, etc. Heterogeneity can pose several challenges for the design and implementation of a DSM system, such as the compatibility, the interoperability, the portability, the performance, and the security of the system. A heterogeneous DSM system should be able to support multiple platforms and environments, and to provide a uniform and transparent interface for the applications.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on the algorithm for implementation of distributed shared memory for the notes of the unit 5 - distributed resource management in the subject of distributed system.

### Algorithm for Implementation of Distributed Shared Memory

Distributed shared memory (DSM) is a technique that allows multiple processes on different nodes of a distributed system to access a common virtual address space as if they were running on a single machine. DSM can simplify the programming of distributed applications by providing a familiar and consistent memory model across the nodes. However, DSM also introduces challenges such as maintaining coherence, consistency, and performance of the shared data.

There are different algorithms for implementing DSM, each with its own advantages and disadvantages. Some of the basic algorithms are:

- **Central server algorithm**: In this algorithm, a central server maintains all the shared data and services the read and write requests from other nodes. The central server can use a page-based or an object-based approach to manage the shared data. The advantage of this algorithm is that it is simple and ensures coherence and consistency of the shared data. The disadvantage is that it introduces a single point of failure and a bottleneck for communication and computation.

- **Migration algorithm**: In this algorithm, the shared data is initially stored at the central server, but it can migrate to other nodes upon request. The node that requests a data item becomes the owner of that item and can read and write it locally. The central server keeps track of the current location of each data item. The advantage of this algorithm is that it reduces the communication overhead and improves the locality of access. The disadvantage is that it may cause frequent migration of data items and increase the complexity of coherence and consistency protocols.

- **Replication algorithm**: In this algorithm, the shared data is replicated on multiple nodes, and each node can read the local copy of the data. However, only one node can write to a data item at a time, and the write permission is granted by the central server. The central server also broadcasts the write updates to all the nodes that have a copy of the data item. The advantage of this algorithm is that it allows concurrent reads and reduces the communication latency. The disadvantage is that it consumes more memory space and requires more communication bandwidth for write updates.

- **Invalidation algorithm**: In this algorithm, the shared data is also replicated on multiple nodes, but each node can read and write the local copy of the data. However, before writing to a data item, a node must obtain a write lock from the central server and invalidate the copies of the data item on other nodes. The central server also maintains a directory of the nodes that have a copy of each data item. The advantage of this algorithm is that it allows concurrent reads and writes and reduces the communication overhead. The disadvantage is that it may cause false sharing and increase the complexity of coherence and consistency protocols.

These are some of the basic algorithms for implementing DSM. There are also other algorithms that combine or modify these algorithms to achieve better performance, scalability, and reliability. For example, some algorithms use multiple servers instead of a single central server, or use multicast or broadcast instead of point-to-point communication, or use different granularity or consistency models for different data items. The choice of the algorithm depends on the characteristics and requirements of the application and the underlying distributed system.



## Unit 6 - Failure Recovery in Distributed Systems

- Failure recovery is the process of restoring a distributed system to a consistent and correct state after a failure occurs.
- Failures can be classified into three types: crash failures, omission failures, and arbitrary failures.
- Crash failures occur when a process stops executing and does not resume. Omission failures occur when a process fails to send or receive a message. Arbitrary failures occur when a process behaves in an unpredictable or malicious way.
- Failure recovery techniques can be divided into two categories: backward recovery and forward recovery.
- Backward recovery involves undoing the effects of a failure and restoring the system to a previous consistent state. This can be achieved by using checkpoints, logging, and rollback.
- Checkpoints are snapshots of the system state taken periodically or on demand. Logging is the recording of events or actions that occur in the system. Rollback is the process of restoring the system state to a checkpoint or a log entry.
- Forward recovery involves correcting the effects of a failure and continuing the system execution from the current state. This can be achieved by using redundancy, replication, and fault tolerance.
- Redundancy is the provision of extra resources or components that can take over the function of a failed one. Replication is the creation of multiple copies of data or processes that can be accessed in case of a failure. Fault tolerance is the ability of the system to continue functioning correctly despite the presence of failures.



### Concepts in Backward and Forward Recovery

- Backward recovery and forward recovery are two techniques to restore the system to a consistent state after a failure in a distributed system.
- Backward recovery involves rolling back the system to a previous error-free state by using checkpoints and logs. Forward recovery involves correcting the errors and continuing the execution from the current state.
- Both techniques have advantages and disadvantages depending on the type and frequency of failures, the overhead of checkpointing and logging, and the availability and consistency requirements of the system.

#### Backward Recovery

- Backward recovery is based on the idea of undoing the effects of a failure by restoring the system to a previous consistent state.
- To perform backward recovery, the system needs to periodically record its state in a stable storage, such as a disk or a tape. This is called checkpointing. Checkpointing can be done either independently by each process, or coordinated by a central authority or a distributed algorithm.
- The system also needs to keep track of the changes made to the state since the last checkpoint. This is done by logging the operations or the results of the operations in a stable storage. Logging can be done either before or after the execution of an operation. This is called write-ahead logging or write-behind logging, respectively.
- When a failure occurs, the system needs to identify the processes that are affected by the failure and roll them back to their last checkpoint. This is called local recovery. The system also needs to ensure that the global state of the system is consistent after the rollback. This is called global recovery. Global recovery can be done either by rolling back all the processes to a common checkpoint, or by using dependency tracking techniques to roll back only the processes that are causally related to the failure.
- Backward recovery has the following advantages:
  - It does not require the knowledge of the nature or the cause of the failure.
  - It can handle any type of failure, such as crash, omission, or Byzantine failures.
  - It can recover from multiple failures, as long as there is a consistent checkpoint available.
- Backward recovery has the following disadvantages:
  - It requires a stable storage for checkpointing and logging, which can be expensive and slow.
  - It introduces overhead in the normal execution of the system, due to the frequent checkpointing and logging operations.
  - It may cause the loss of some useful work that was done after the checkpoint, which can affect the performance and the availability of the system.

#### Forward Recovery

- Forward recovery is based on the idea of correcting the errors and continuing the execution from the current state of the system.
- To perform forward recovery, the system needs to detect the errors and apply some corrective actions to fix them. The corrective actions can be either predefined or adaptive, depending on the type and the severity of the errors.
- The system also needs to propagate the corrections to the other processes that are affected by the errors. This can be done either by sending messages or by updating the shared state of the system.
- When a failure occurs, the system needs to identify the processes that are affected by the failure and apply the corrective actions to them. This is called local recovery. The system also needs to ensure that the global state of the system is consistent after the correction. This is called global recovery. Global recovery can be done either by using consensus protocols or by using redundancy techniques to achieve agreement among the processes.
- Forward recovery has the following advantages:
  - It does not require a stable storage for checkpointing and logging, which can save cost and time.
  - It does not introduce overhead in the normal execution of the system, as there is no need for frequent checkpointing and logging operations.
  - It does not cause the loss of any useful work that was done before the failure, which can improve the performance and the availability of the system.
- Forward recovery has the following disadvantages:
  - It requires the knowledge of the nature and the cause of the failure, which can be difficult or impossible to obtain in some cases.
  - It can only handle certain types of failures, such as crash or omission failures, but not Byzantine failures.
  - It may not be able to recover from multiple failures, as the system may not have enough resources or information to correct all the errors.



### Recovery in Concurrent Systems

Recovery in concurrent systems is the process of restoring the system to a consistent state after a failure, while preserving the effects of the transactions that were committed before the failure. Recovery in concurrent systems involves the following challenges and techniques:

- **Interaction with concurrency control**: The recovery scheme depends on the concurrency control scheme that is used to ensure serializability of transactions. For example, if locking is used, then the recovery scheme must ensure that locks are released after a transaction commits or aborts, and that locks are reacquired after a system restart. If timestamp ordering is used, then the recovery scheme must ensure that timestamps are assigned correctly and consistently after a failure.
- **Transaction rollback**: A transaction rollback is the undoing of the changes made by a transaction that has not committed yet, either because of an abort request or a system failure. Transaction rollback can be done by using undo logs, which record the old values of the data items that were modified by the transaction. Undo logs can be applied in reverse order to restore the data items to their previous states.
- **Checkpoints**: A checkpoint is a point in time when the system saves its state to a stable storage, such as a disk. Checkpoints can reduce the amount of work that needs to be done during recovery, by limiting the number of transactions that need to be rolled back or redone. Checkpoints can be taken periodically, or based on some criteria, such as the number of transactions or the amount of log records.
- **Restart recovery**: Restart recovery is the process of bringing the system back to a consistent state after a system failure, by using the checkpoints and the logs. Restart recovery can be done in two phases: analysis and redo/undo. In the analysis phase, the system scans the logs and identifies the transactions that were active, committed, or aborted at the time of the failure. In the redo/undo phase, the system applies the redo logs to redo the changes made by the committed transactions, and applies the undo logs to undo the changes made by the active or aborted transactions.



### Obtaining consistent Checkpoints for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Failure recovery in distributed systems is the process of restoring the system to a consistent and correct state after a failure occurs.
- A failure in a distributed system can be caused by various factors, such as hardware faults, software bugs, network errors, malicious attacks, power outages, etc.
- A failure can affect one or more components of the system, such as processes, nodes, links, or data.
- A failure can have different consequences, such as data loss, data corruption, performance degradation, service unavailability, or inconsistency.
- To recover from a failure, the system needs to detect the failure, identify the cause and location of the failure, isolate the failed components, and restore the system to a consistent and correct state.
- One of the common techniques for failure recovery in distributed systems is checkpointing .
- Checkpointing is the process of periodically saving the state of the system or its components to a stable storage, such as a disk or a cloud service.
- Checkpointing can be done at different levels, such as process level, node level, or system level.
- Checkpointing can be done in different ways, such as synchronous, asynchronous, coordinated, or uncoordinated.
- Checkpointing can help the system to recover from a failure by restoring the system or its components to the last saved state, and then replaying the events that occurred after the checkpoint.
- However, checkpointing also has some challenges, such as how to ensure the consistency and correctness of the checkpoints, how to minimize the overhead and latency of checkpointing, how to coordinate the checkpointing among multiple components, and how to handle concurrent or dependent events.
- To obtain consistent checkpoints, the system needs to ensure that the checkpoints reflect a global state of the system that is reachable and valid.
- A global state of the system is a collection of the local states of all the components and the messages in transit among them.
- A global state is reachable if it can be obtained by executing the system from some initial state.
- A global state is valid if it does not violate any invariant or constraint of the system.
- To ensure the consistency and correctness of the checkpoints, the system can use different algorithms, such as the Chandy-Lamport algorithm, the Lai-Yang algorithm, or the Manetho algorithm.
- These algorithms use different techniques, such as message logging, vector clocks, or dependency graphs, to capture the causal and temporal relationships among the events and states of the system.
- These algorithms can also handle different types of failures, such as crash failures, omission failures, or Byzantine failures.
- These algorithms can also trade off between different factors, such as the frequency and size of the checkpoints, the amount and type of the logged messages, the complexity and scalability of the coordination, and the recovery time and performance.



# Recovery in Distributed Database Systems

- Recovery in distributed database systems is the process of restoring the database to a consistent state after a failure or an error .
- Recovery in distributed database systems is more complicated than in centralized database systems because failures can occur at the communication links or a remote site.
- Recovery in distributed database systems aims to maintain the atomicity and durability of distributed transactions, which means that all statements in a transaction, distributed or non-distributed, either commit or roll back as a unit.
- Recovery in distributed database systems can be classified into two types: local recovery and global recovery .
  - Local recovery is the recovery of a single site or a single transaction that has failed or aborted. Local recovery can be done by using undo or redo operations based on the transaction log.
  - Global recovery is the recovery of a distributed transaction that involves multiple sites or multiple transactions that have failed or aborted. Global recovery can be done by using distributed commit protocols, such as two-phase commit (2PC) or three-phase commit (3PC), that coordinate the commit or abort decisions of all the participating sites .
- Recovery in distributed database systems can also be affected by the replication of data across multiple sites. Replication can improve the availability and performance of the database, but it also introduces the problem of maintaining the consistency of the replicas.
  - Recovery in replicated database systems can be done by using replication protocols, such as eager replication or lazy replication, that synchronize the updates of the replicas.
  - Eager replication ensures that all the replicas are updated before a transaction commits, which avoids the problem of conflicting updates, but it also increases the communication and synchronization overhead.
  - Lazy replication allows the replicas to be updated after a transaction commits, which reduces the communication and synchronization overhead, but it also introduces the problem of conflicting updates, which have to be resolved by using conflict resolution policies.



## Unit 7 - Fault Tolerance

Fault tolerance is the ability of a system to continue functioning correctly in the presence of failures. Fault tolerance can be achieved by using techniques such as redundancy, replication, recovery, and reconfiguration.

Some key concepts and terms related to fault tolerance are:

- **Fault**: A fault is a defect or error in a system component or process that may cause a failure. Faults can be classified into different types, such as transient, intermittent, or permanent; hardware or software; or byzantine or non-byzantine.
- **Failure**: A failure is a deviation of the system behavior from its specification or expected outcome. Failures can be classified into different types, such as crash, omission, timing, response, or value failures.
- **Error**: An error is the manifestation of a fault in the system state or output. Errors can be detected by using techniques such as checksums, parity bits, or error-correcting codes.
- **Reliability**: Reliability is the probability that a system will perform its intended function without failure for a given period of time under specified conditions.
- **Availability**: Availability is the probability that a system will be operational and ready to provide service at any given time.
- **Maintainability**: Maintainability is the ease with which a system can be repaired or restored to its normal state after a failure.
- **Dependability**: Dependability is a general term that encompasses reliability, availability, and maintainability, as well as other attributes such as safety, security, and survivability.

Some common techniques for achieving fault tolerance are:

- **Redundancy**: Redundancy is the provision of extra or alternative components or resources to increase the reliability or availability of a system. Redundancy can be classified into different types, such as static or dynamic; hardware or software; or spatial or temporal.
- **Replication**: Replication is the creation and maintenance of multiple copies of the same data or service to increase the availability or performance of a system. Replication can be classified into different types, such as passive or active; primary-backup or multi-primary; or synchronous or asynchronous.
- **Recovery**: Recovery is the process of restoring a system to a correct state after a failure. Recovery can be classified into different types, such as backward or forward; checkpointing or logging; or roll-back or roll-forward.
- **Reconfiguration**: Reconfiguration is the process of changing the structure or parameters of a system to adapt to changing conditions or requirements. Reconfiguration can be classified into different types, such as static or dynamic; centralized or distributed; or proactive or reactive.



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



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on commit protocols for distributed systems.

### Commit Protocols for Distributed Systems

- Commit protocols are algorithms that ensure the atomicity and consistency of transactions that span multiple sites in a distributed system.
- Atomicity means that either all the operations of a transaction are executed or none of them are. Consistency means that the system remains in a valid state after the transaction.
- Commit protocols involve a coordinator site that initiates the transaction and communicates with the participant sites that execute the operations of the transaction.
- The coordinator site decides whether to commit or abort the transaction based on the votes of the participant sites. The participant sites follow the decision of the coordinator site.
- There are different types of commit protocols, such as one-phase commit, two-phase commit, and three-phase commit. Each protocol has its own advantages and disadvantages in terms of performance, reliability, and message complexity.

#### One-Phase Commit Protocol

- A one-phase commit protocol is the simplest commit protocol. It involves only one message exchange between the coordinator and the participants.
- The coordinator sends a commit request to all the participants and waits for their replies. If all the participants reply with an OK message, the coordinator commits the transaction and sends a commit acknowledgment to the participants. If any participant replies with an abort message, the coordinator aborts the transaction and sends an abort acknowledgment to the participants.
- The advantage of a one-phase commit protocol is that it is fast and simple. The disadvantage is that it does not guarantee atomicity in the presence of failures. If the coordinator or any participant fails before sending or receiving the commit request, the transaction may be left in an inconsistent state.

#### Two-Phase Commit Protocol

- A two-phase commit protocol is a more reliable commit protocol. It involves two phases: a voting phase and a decision phase.
- In the voting phase, the coordinator sends a prepare message to all the participants and waits for their votes. The participants execute the operations of the transaction and reply with either a yes vote or a no vote. A yes vote means that the participant is ready to commit the transaction. A no vote means that the participant wants to abort the transaction.
- In the decision phase, the coordinator decides whether to commit or abort the transaction based on the votes of the participants. If all the participants vote yes, the coordinator commits the transaction and sends a commit message to the participants. If any participant votes no, the coordinator aborts the transaction and sends an abort message to the participants.
- The advantage of a two-phase commit protocol is that it guarantees atomicity even in the presence of failures. The coordinator and the participants write their votes and decisions to a log before sending or receiving any messages. This way, they can recover from failures and resume the protocol.
- The disadvantage of a two-phase commit protocol is that it is blocking. If the coordinator fails after sending the prepare message, the participants are blocked until the coordinator recovers. They cannot commit or abort the transaction without the coordinator's decision.

#### Three-Phase Commit Protocol

- A three-phase commit protocol is a non-blocking commit protocol. It involves three phases: a prepare phase, a pre-commit phase, and a commit/abort phase.
- In the prepare phase, the steps are the same as in the voting phase of the two-phase commit protocol. The coordinator sends a prepare message to all the participants and waits for their votes. The participants execute the operations of the transaction and reply with either a yes vote or a no vote.
- In the pre-commit phase, the coordinator decides whether to commit or abort the transaction based on the votes of the participants. If all the participants vote yes, the coordinator sends a pre-commit message to the participants. If any participant votes no, the coordinator sends an abort message to the participants.
- In the commit/abort phase, the coordinator sends a commit message to the participants if it received OK messages from all of them in the pre-commit phase. Otherwise, it sends an abort message to the participants. The participants follow the coordinator's decision and send an acknowledgment message to the coordinator.
- The advantage of a three-phase commit protocol is that it is non-blocking. If the coordinator fails after sending the pre-commit message, the participants can decide to commit the transaction without waiting for the coordinator. They can use a timeout mechanism or a majority voting scheme to reach a consensus



### Voting protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Voting protocols are a class of consensus algorithms that are used to achieve agreement among a set of distributed nodes on some value or decision  .
- Voting protocols are useful for fault-tolerant systems, where some nodes may fail or behave maliciously, and the system needs to maintain consistency and availability  .
- Voting protocols can be classified into two types: exact voting and inexact voting .
  - Exact voting requires that all nodes agree on the same value or decision, and that the value or decision is correct according to some predefined criterion .
  - Inexact voting allows for some degree of disagreement or error among the nodes, as long as the value or decision is acceptable according to some predefined criterion .
- Voting protocols can also be classified based on the number of rounds of communication they require: one-round voting, two-round voting, and multi-round voting .
  - One-round voting requires only one message exchange among the nodes, and is suitable for simple and fast decisions .
  - Two-round voting requires two message exchanges among the nodes, and is suitable for more complex and reliable decisions .
  - Multi-round voting requires multiple message exchanges among the nodes, and is suitable for dynamic and adaptive decisions .
- Voting protocols can also be classified based on the level of security they provide: insecure voting, secure voting, and fair voting  .
  - Insecure voting does not provide any guarantee against malicious nodes or external attacks, and relies on the assumption that all nodes are honest and reliable .
  - Secure voting provides some guarantee against malicious nodes or external attacks, and relies on cryptographic techniques such as encryption, authentication, and digital signatures  .
  - Fair voting provides a stronger guarantee against malicious nodes or external attacks, and relies on game-theoretic techniques such as incentives, penalties, and reputation .
- Voting protocols can also be classified based on the weight or reputation of the nodes: equal-weight voting, weighted voting, and reputation-based voting .
  - Equal-weight voting assumes that all nodes have the same weight or importance in the voting process, and that the value or decision is determined by a simple majority or plurality .
  - Weighted voting assumes that some nodes have more weight or importance than others in the voting process, and that the value or decision is determined by a weighted majority or plurality .
  - Reputation-based voting assumes that the weight or importance of the nodes is determined by their past behavior or performance in the voting process, and that the value or decision is determined by a reputation-based majority or plurality .



### Dynamic voting protocols

- Dynamic voting protocols are techniques for consistency and recovery control of replicated files in distributed systems  .
- The purpose of a replicated file is to improve the availability of a logical file in the presence of site failures and network partitions  .
- A dynamic voting protocol assigns a number of votes to each replica of a file, and requires a majority of votes to access or update the file   .
- The number of votes assigned to each replica can change dynamically based on the system state, such as the number of replicas, the network topology, the failure pattern, etc    .
- The advantages of dynamic voting protocols are:
  - They can increase the availability of a file by allowing access to a subset of replicas when the system is partitioned   .
  - They can reduce the communication overhead by minimizing the number of replicas involved in each operation   .
  - They can adapt to the changing system conditions by reassigning votes to balance the load and avoid bottlenecks .
- The challenges of dynamic voting protocols are:
  - They need to ensure the consistency of the replicas by preventing concurrent conflicting operations and maintaining a consistent view of the votes     .
  - They need to handle the failure and recovery of replicas and votes by detecting failures, updating votes, and restoring replicas    .
  - They need to cope with the network latency and uncertainty by tolerating message delays, losses, and duplications    .



# Unit 8 - Transactions and Concurrency Control

## Introduction

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction has the following properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the operations in a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction executes as if it is the only one running on the database, without interference from other transactions.
- Durability means that the effects of a committed transaction are permanent and survive any system failures.
- Concurrency control is the process of managing the simultaneous execution of transactions in a shared database, to ensure the serializability and correctness of the transactions.
- Serializability is the property that the concurrent execution of a set of transactions is equivalent to some serial execution of the same transactions.
- A serial execution is one in which each transaction is executed one after another, without any overlap.
- A schedule is a sequence of operations from a set of transactions, where each operation is either a read or a write of a data item.
- A schedule is serial if it consists of a sequence of operations from one transaction, followed by a sequence of operations from another transaction, and so on.
- A schedule is serializable if it is equivalent to some serial schedule of the same transactions.
- Two schedules are equivalent if they produce the same final state of the database and the same output for each transaction.
- There are different methods of testing and ensuring serializability, such as conflict serializability, view serializability, precedence graph, and locking protocols.
- Conflict serializability is a criterion that a schedule is serializable if it can be transformed into a serial schedule by swapping non-conflicting operations.
- Two operations conflict if they belong to different transactions, access the same data item, and at least one of them is a write.
- View serializability is a criterion that a schedule is serializable if it is view equivalent to some serial schedule of the same transactions.
- Two schedules are view equivalent if they have the same initial and final values for each data item, and the same transaction reads the value written by the same transaction for each data item.
- A precedence graph is a directed graph that represents the conflicts among the transactions in a schedule.
- Each node in the graph is a transaction, and each edge from Ti to Tj means that Ti has to finish before Tj in any serial schedule equivalent to the given schedule.
- A schedule is conflict serializable if and only if its precedence graph is acyclic.
- A locking protocol is a set of rules that govern when and how a transaction can lock and unlock a data item in a database.
- A lock is a mechanism that grants exclusive or shared access to a data item to a transaction.
- A lock can be either exclusive (X) or shared (S).
- An exclusive lock allows a transaction to read and write a data item, and prevents any other transaction from accessing it.
- A shared lock allows a transaction to read a data item, and allows other transactions to read it as well, but prevents any transaction from writing it.
- A transaction can request a lock on a data item before accessing it, and release the lock after finishing the access.
- A transaction can also upgrade a shared lock to an exclusive lock, or downgrade an exclusive lock to a shared lock, if needed.
- A locking protocol ensures serializability by preventing conflicting operations from executing concurrently.
- A locking protocol can be either strict or rigorous, depending on when a transaction releases its locks.
- A strict locking protocol requires a transaction to hold all its exclusive locks until it commits or aborts, to ensure durability.
- A rigorous locking protocol requires a transaction to hold all its locks, both exclusive and shared, until it commits or aborts, to ensure recoverability.
- Recoverability is the property that a transaction does not read a value written by another transaction that may abort later.
- A locking protocol can also be either conservative or optimistic, depending on when a transaction requests its locks.
- A conservative locking protocol requires a transaction to request all its locks before it starts execution, to avoid deadlock.
- A deadlock is a situation where a set of transactions are waiting for each other to release their locks, and none of them can proceed.
- An optimistic locking protocol allows a transaction to request locks as it executes, and aborts and restarts the transaction if it encounters a deadlock or a conflict.
- A locking protocol can also be either two-phase or multi-phase, depending on the number of phases in which a transaction requests and releases its locks.
- A two-phase locking protocol requires a transaction to follow two phases: a growing



### Transactions
- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the operations in a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction is executed as if it were the only one running in the system.
- Durability means that the effects of a committed transaction are permanent and survive any system failures.

### Concurrency Control
- Concurrency control is the process of managing the simultaneous execution of transactions in a shared database, to ensure the ACID properties of the transactions are maintained.
- Concurrency control is needed because concurrent transactions may interfere with each other, leading to incorrect or inconsistent results.
- For example, two transactions may try to update the same data item, or one transaction may read a data item that is being updated by another transaction.
- Concurrency control techniques can be broadly classified into two categories: locking-based and non-locking-based.
- Locking-based techniques use locks to prevent transactions from accessing or modifying data items that are already being accessed or modified by other transactions.
- Non-locking-based techniques use timestamps, validation, or multiversioning to order or validate the transactions based on their logical start times or commit times.

### Distributed Transactions and Distributed Concurrency Control
- A distributed transaction is a transaction that accesses data from multiple data servers that are connected by a computer network.
- A distributed transaction consists of a set of subtransactions, each of which is executed by one data server.
- A distributed transaction is committed if and only if all its subtransactions are committed.
- A distributed transaction is aborted if any of its subtransactions is aborted.
- Distributed concurrency control provides a mechanism to synchronize distributed transactions in such a way that the ACID properties are not violated by their interleaved execution.
- Distributed concurrency control techniques can be classified into two categories: centralized and decentralized.
- Centralized techniques use a single coordinator to manage the locks or timestamps of the data items accessed by the distributed transactions.
- Decentralized techniques use multiple coordinators or no coordinators to manage the locks or timestamps of the data items accessed by the distributed transactions.



### Nested transactions for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A transaction is a unit of work that performs some operations on a database or a system, and satisfies the ACID properties (Atomicity, Consistency, Isolation, Durability).
- A nested transaction is a transaction that is composed of subtransactions, each of which may have its own begin and end points, and may be executed by different servers or processes in a distributed system.
- Nested transactions allow for more flexibility and concurrency in distributed systems, as they can support partial commits, partial aborts, and partial retries of subtransactions, without affecting the atomicity and consistency of the whole transaction.
- Nested transactions can be classified into two types: flat nested transactions and closed nested transactions.
- Flat nested transactions are nested transactions that have a single commit point and a single abort point, and are treated as a single transaction by the concurrency control and recovery mechanisms. They are usually used for short and simple operations that do not require much coordination among subtransactions.
- Closed nested transactions are nested transactions that have multiple commit points and multiple abort points, and are treated as independent transactions by the concurrency control and recovery mechanisms. They are usually used for long and complex operations that require more coordination among subtransactions, and can benefit from partial results and compensating actions.
- Nested transactions can be implemented using various techniques, such as two-phase commit, nested two-phase commit, multilevel transactions, and serialization graphs. These techniques aim to ensure the correctness and efficiency of nested transactions in distributed systems, by resolving conflicts, detecting deadlocks, and recovering from failures.



# Locks for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A lock is a mechanism that allows only one of the innumerable nodes or processes to access and modify a resource or data that is being shared commonly to prevent execution of same task twice and also maintain data integrity.
- Locks are designed to enforce a mutual exclusion concurrency control policy, which means that only one process can hold a lock on a resource at a time, and any other process that wants to access the same resource has to wait until the lock is released.
- Locks can be classified into different types based on the following criteria  :
  - The granularity of the resource: locks can be applied to different levels of abstraction, such as a file, a record, a page, a block, or a byte. The finer the granularity, the more concurrency is possible, but the more overhead is incurred.
  - The mode of the lock: locks can be either shared or exclusive. A shared lock allows multiple processes to read the same resource, but prevents any process from writing to it. An exclusive lock allows only one process to read or write the resource, and blocks any other process from accessing it.
  - The duration of the lock: locks can be either long-lived or short-lived. A long-lived lock is held by a process for the entire duration of a transaction, and is released only when the transaction commits or aborts. A short-lived lock is held by a process only for the time it needs to access the resource, and is released as soon as possible.
  - The scope of the lock: locks can be either local or global. A local lock is managed by a single node or process, and is only valid within that node or process. A global lock is managed by a distributed lock manager, and is valid across multiple nodes or processes.
- Locks can be implemented using different techniques, such as   :
  - Centralized locking: a single node or process acts as the lock manager, and maintains a table of locks and requests. Any node or process that wants to acquire or release a lock has to communicate with the lock manager. This approach is simple and easy to implement, but it introduces a single point of failure and a bottleneck for performance and scalability.
  - Distributed locking: each node or process manages its own locks and requests, and coordinates with other nodes or processes using a consensus protocol, such as Paxos, Raft, or ZooKeeper. This approach is more fault-tolerant and scalable, but it requires more communication and synchronization overhead, and it may suffer from network partitions and delays.
  - Optimistic locking: each node or process assumes that there is no conflict with other nodes or processes, and accesses the resource without acquiring a lock. However, before committing the changes, each node or process has to validate that the resource has not been modified by another node or process since the last read. If a conflict is detected, the node or process has to abort and retry the transaction. This approach is suitable for scenarios where conflicts are rare and transactions are short, but it may incur more aborts and retries if conflicts are frequent or transactions are long.
  - Pessimistic locking: each node or process acquires a lock before accessing the resource, and holds the lock until the transaction is completed. This approach is suitable for scenarios where conflicts are frequent or transactions are long, but it may incur more blocking and waiting if the resource is highly contended or the transactions are slow.



### Optimistic Concurrency Control for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- Optimistic concurrency control (OCC) is a concurrency control method applied to transactional systems such as relational database management systems and software transactional memory.
- OCC assumes that multiple transactions can frequently complete without interfering with each other, and therefore does not require locking or timestamping techniques to prevent conflicts .
- Instead, OCC allows transactions to execute without restrictions until they are committed, and then validates them to ensure that no conflicts have occurred.
- If a conflict is detected, the transaction is aborted and restarted, possibly with some backoff or priority adjustment mechanism to reduce the likelihood of repeated conflicts .
- OCC has three phases: read, validation and write.
  - In the read phase, the transaction reads the data from the database and performs its operations, without acquiring any locks or checking any timestamps.
  - In the validation phase, the transaction checks if any of the data it has read or written has been modified by another transaction that committed earlier. This can be done by comparing the versions or timestamps of the data items, or by using a validation server that keeps track of the committed transactions .
  - In the write phase, if the validation succeeds, the transaction writes its updates to the database and commits. Otherwise, the transaction aborts and restarts.
- OCC has some advantages and disadvantages compared to other concurrency control methods  :
  - Advantages:
    - OCC avoids locking overhead and deadlock problems, as transactions do not block each other or hold any resources .
    - OCC allows more concurrency and throughput, as transactions can execute in parallel without waiting for locks or timestamps .
    - OCC is suitable for distributed systems, where locking or timestamping may be costly or impractical due to network delays or failures  .
  - Disadvantages:
    - OCC may incur more aborts and restarts, especially when the data contention is high or the transactions are long .
    - OCC may waste more resources and computation, as transactions may perform unnecessary work before being aborted .
    - OCC may have lower consistency and freshness, as transactions may read stale or uncommitted data .



### Timestamp Ordering for the Notes of the Unit 8 - Transactions and Concurrency Control in the Subject of Distributed System

- Timestamp ordering is a class of concurrency control protocols that use timestamps to determine the serializability order of transactions  .
- A timestamp is a monotonically increasing number that is often based on the system clock .
- In a distributed system, timestamps need to be globally unique and consistent across different sites .
- There are two types of timestamp ordering protocols: basic timestamp ordering and optimistic timestamp ordering .
- Basic timestamp ordering assigns a timestamp to each transaction when it starts and uses it to check whether the transaction can read or write a data item without violating serializability .
- Basic timestamp ordering uses two timestamps for each data item: read timestamp (RTS) and write timestamp (WTS), which record the latest timestamp of a transaction that read or wrote the data item, respectively .
- Basic timestamp ordering enforces two rules: read-write rule and write-write rule .
- Read-write rule: a transaction T can read a data item X only if T's timestamp is greater than or equal to X's WTS; otherwise, T is aborted and restarted with a new timestamp .
- Write-write rule: a transaction T can write a data item X only if T's timestamp is greater than both X's RTS and X's WTS; otherwise, T is aborted and restarted with a new timestamp .
- Basic timestamp ordering ensures conflict serializability but not recoverability or cascadelessness .
- Optimistic timestamp ordering assumes that conflicts are rare and allows transactions to execute without checking timestamps until they commit .
- Optimistic timestamp ordering assigns three timestamps to each transaction: start timestamp (STS), validation timestamp (VTS), and commit timestamp (CTS) .
- STS is assigned when the transaction starts, VTS is assigned when the transaction enters the validation phase, and CTS is assigned when the transaction commits .
- Optimistic timestamp ordering uses a validation phase to check whether the transaction can commit without violating serializability .
- Optimistic timestamp ordering enforces three rules: write-write rule, read-write rule, and write-read rule .
- Write-write rule: a transaction T can commit only if no other transaction that wrote a data item that T also wrote has a CTS between T's STS and T's VTS; otherwise, T is aborted and restarted with a new timestamp .
- Read-write rule: a transaction T can commit only if no other transaction that wrote a data item that T read has a CTS between T's STS and T's VTS; otherwise, T is aborted and restarted with a new timestamp .
- Write-read rule: a transaction T can commit only if no other transaction that read a data item that T wrote has a CTS between T's STS and T's VTS; otherwise, T is aborted and restarted with a new timestamp .
- Optimistic timestamp ordering ensures conflict serializability, recoverability, and cascadelessness .



### Comparison of methods for concurrency control

Concurrency control is the process of managing the simultaneous execution of transactions in a distributed system, such that the consistency and correctness of the data are preserved. Concurrency control methods can be classified into two main categories: pessimistic and optimistic.

- Pessimistic methods assume that conflicts are likely to occur and prevent them by using locking or timestamping mechanisms. Pessimistic methods guarantee serializability, which means that the outcome of concurrent transactions is equivalent to some serial execution of them. However, pessimistic methods may incur high overhead, blocking, and deadlock problems.

- Optimistic methods assume that conflicts are rare and allow transactions to execute without any coordination until the commit time. Then, they check for conflicts and abort or restart transactions if necessary. Optimistic methods avoid blocking and deadlock, but may incur high abort and restart costs.

Some of the common concurrency control methods are:

- Two-phase locking (2PL): A pessimistic method that requires transactions to acquire locks on data items before reading or writing them, and release them after they are done. 2PL ensures serializability, but may cause blocking and deadlock. There are different variants of 2PL, such as strict 2PL, rigorous 2PL, and conservative 2PL, that differ in the timing and order of lock acquisition and release.

- Timestamp ordering (TO): A pessimistic method that assigns a unique timestamp to each transaction and orders them according to their timestamps. Transactions are allowed to read or write data items only if their timestamps are compatible with the timestamps of previous transactions that accessed the same data items. TO ensures serializability, but may cause aborts and restarts.

- Multi-version concurrency control (MVCC): A method that maintains multiple versions of each data item, each with a timestamp indicating when it was created or modified. Transactions can read the latest committed version of a data item that is compatible with their timestamp, and write a new version with their own timestamp. MVCC avoids blocking and ensures serializability, but may incur high storage and garbage collection costs.

- Validation concurrency control (VCC): An optimistic method that divides the execution of a transaction into three phases: read, validation, and write. In the read phase, transactions read data items without any locking or timestamping. In the validation phase, transactions check for conflicts with other concurrent transactions using a validation test. In the write phase, transactions write their updates to the database if they pass the validation test. VCC avoids blocking and ensures serializability, but may cause aborts and restarts.



## Unit 9 - Distributed Transactions

- A distributed transaction is a type of transaction that involves two or more network hosts, usually providing transactional resources, such as databases, message queues, file systems, etc.  
- A distributed transaction is coordinated by a transaction manager, which is responsible for creating and managing a global transaction that encompasses all the operations against the transactional resources.  
- A distributed transaction requires the following properties to ensure data consistency and reliability: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the operations in a distributed transaction are executed successfully, or none of them are. If any operation fails, the transaction manager must roll back the changes made by the other operations.
- Consistency means that the distributed transaction must preserve the integrity constraints and business rules of the data. The transaction manager must ensure that the data is in a valid state before and after the transaction.
- Isolation means that the distributed transaction must not interfere with other concurrent transactions. The transaction manager must ensure that the operations in a transaction are executed as if they were the only ones in the system.
- Durability means that the effects of a distributed transaction must be permanent and persistent. The transaction manager must ensure that the changes made by the transaction are not lost due to failures or crashes.
- A distributed transaction can be implemented using different protocols, such as two-phase commit (2PC), three-phase commit (3PC), or the saga pattern.
- Two-phase commit (2PC) is a protocol that involves two phases: prepare and commit. In the prepare phase, the transaction manager asks all the transactional resources to vote on whether they are ready to commit or abort the transaction. If all the resources vote yes, the transaction manager proceeds to the commit phase, where it instructs all the resources to commit the transaction. If any resource votes no, or if there is a timeout or a failure, the transaction manager aborts the transaction and instructs all the resources to roll back the changes.
- Three-phase commit (3PC) is a protocol that involves three phases: prepare, pre-commit, and commit. In the prepare phase, the transaction manager asks all the transactional resources to vote on whether they are ready to commit or abort the transaction. If all the resources vote yes, the transaction manager proceeds to the pre-commit phase, where it informs all the resources that the transaction is about to be committed. If any resource votes no, or if there is a timeout or a failure, the transaction manager aborts the transaction and instructs all the resources to roll back the changes. In the commit phase, the transaction manager instructs all the resources to commit the transaction.
- The saga pattern is a protocol that involves a sequence of compensating actions. A compensating action is an operation that reverses the effect of a previous operation. In the saga pattern, the transaction manager executes each operation in the transaction and records its compensating action. If any operation fails, the transaction manager executes the compensating actions in reverse order to undo the changes made by the previous operations.
- A distributed transaction faces various challenges, such as network failures, resource failures, concurrency conflicts, deadlock detection, and performance overhead.
- Network failures can cause communication problems between the transaction manager and the transactional resources, or among the transactional resources themselves. This can lead to inconsistent or incomplete data, or to the loss of transactional messages.
- Resource failures can cause the transactional resources to crash or become unavailable during the transaction. This can lead to the loss of data or the inability to commit or abort the transaction.
- Concurrency conflicts can occur when multiple transactions try to access or modify the same data at the same time. This can lead to data inconsistency or violation of integrity constraints.
- Deadlock detection is the problem of identifying and resolving situations where two or more transactions are waiting for each other to release some resources. This can lead to the blocking or starvation of transactions.
- Performance overhead is the extra cost of coordinating and executing a distributed transaction, compared to a local transaction. This can include the cost of network communication, message processing, logging, locking, voting, etc.



# Flat and Nested Distributed Transactions

A distributed transaction is a transaction that accesses objects managed by multiple servers. A distributed transaction must maintain the ACID properties of a transaction, which means that it must be atomic, consistent, isolated, and durable. Atomicity means that either all the servers involved in the transaction commit the transaction or all of them abort the transaction. Consistency means that the transaction preserves the integrity constraints of the data. Isolation means that the transaction does not interfere with other concurrent transactions. Durability means that the effects of the transaction are permanent even in the case of failures.

Distributed transactions can be structured in two different ways: flat transactions and nested transactions.

## Flat Transactions

A flat transaction has a single initiating point (Begin) and a single end point (Commit or Abort). They are usually very simple and are generally used for short activities rather than larger ones. A flat transaction can be coordinated by a single server, called the transaction manager, which is responsible for initiating, committing, or aborting the transaction. The transaction manager communicates with the servers that participate in the transaction using a two-phase commit protocol, which ensures that all the servers agree on the outcome of the transaction.

## Nested Transactions

A nested transaction is a transaction that contains other transactions as subtransactions. A nested transaction has a hierarchical structure, where the top-level transaction is called the root transaction and the subtransactions are called the branches. A nested transaction can be used to decompose a complex transaction into smaller and more manageable units. A nested transaction can also provide more concurrency and fault tolerance than a flat transaction, as the subtransactions can execute in parallel and can be independently committed or aborted.

A nested transaction can be coordinated by a distributed transaction manager, which is a collection of servers that cooperate to manage the transaction. The distributed transaction manager communicates with the servers that participate in the transaction using a nested two-phase commit protocol, which extends the two-phase commit protocol to handle the hierarchical structure of the transaction. The nested two-phase commit protocol ensures that all the servers agree on the outcome of the transaction and that the subtransactions are consistent with the root transaction.



### Atomic Commit Protocols for Distributed Transactions

- A distributed transaction is a transaction that involves multiple servers or nodes in a distributed system. A distributed transaction must satisfy the ACID properties, especially the atomicity property, which means that either all the operations in the transaction are executed successfully, or none of them are executed at all.
- An atomic commit protocol is a protocol that ensures the atomicity property of a distributed transaction, even if the system or some of the nodes fail or crash. An atomic commit protocol typically involves a coordinator node and multiple participant nodes, and consists of two phases: a voting phase and a decision phase.
- In the voting phase, the coordinator node sends a prepare message to all the participant nodes, asking them to vote on whether they are ready to commit or abort the transaction. The participant nodes reply with either a yes or a no vote, depending on their local state and outcome of the transaction operations. If a participant node fails or does not reply within a timeout, it is considered as a no vote.
- In the decision phase, the coordinator node collects all the votes from the participant nodes and decides whether to commit or abort the transaction based on a predefined rule. The rule can be either unanimous or majority, depending on the protocol. The coordinator node then sends a commit or abort message to all the participant nodes, informing them of the final decision. The participant nodes then execute the commit or abort action accordingly. If the coordinator node fails or does not send the decision message within a timeout, the participant nodes may use a recovery mechanism to reach a consistent state.
- There are different types of atomic commit protocols, such as two-phase commit (2PC), three-phase commit (3PC), parallel commits, and failure-aware atomic commit (FLAC). Each protocol has its own advantages and disadvantages in terms of performance, fault tolerance, and complexity. Some of the factors that affect the choice of the protocol are the network latency, the failure rate, the concurrency level, and the data consistency requirements.



# Concurrency control in distributed transactions

- Concurrency control is the process of managing the concurrent execution of transactions in a distributed database system, such that the ACID properties are preserved .
- ACID stands for Atomicity, Consistency, Isolation, and Durability, which are the desirable properties of a transaction .
- Atomicity means that a transaction either executes completely or not at all .
- Consistency means that a transaction preserves the integrity constraints of the database .
- Isolation means that a transaction does not interfere with other concurrent transactions .
- Durability means that the effects of a committed transaction are permanent and survive failures .
- Concurrency control is needed because concurrent transactions may cause anomalies or inconsistencies in the database, such as lost updates, dirty reads, unrepeatable reads, or phantom reads  .
- Lost updates occur when two transactions update the same data item and one of them overwrites the other's update  .
- Dirty reads occur when a transaction reads a data item that has been updated by another transaction but not yet committed  .
- Unrepeatable reads occur when a transaction reads the same data item twice and gets different values due to another transaction's update  .
- Phantom reads occur when a transaction reads a set of data items that satisfy some condition and gets different results due to another transaction's insertion or deletion of data items that satisfy the same condition  .
- Concurrency control can be achieved by using various techniques, such as locking, timestamping, or optimistic methods  .
- Locking-based concurrency control protocols use the concept of locking data items to prevent concurrent transactions from accessing or modifying them  .
- Locking can be exclusive or shared, depending on whether the transaction intends to read or write the data item  .
- Locking can also be centralized or distributed, depending on whether there is a single or multiple lock managers in the system  .
- Locking can also be static or dynamic, depending on whether the locks are acquired at the beginning or during the execution of the transaction  .
- Locking can also be hierarchical or flat, depending on whether the locks are applied to different levels of granularity, such as database, table, page, or record  .
- Locking can also be strict or relaxed, depending on whether the locks are released after the transaction commits or before  .
- Locking can also be two-phase or not, depending on whether the transaction follows the two-phase locking protocol, which requires that all locks are acquired before any lock is released  .
- Locking-based concurrency control protocols can ensure serializability, which is the property that the concurrent execution of transactions is equivalent to some serial execution of the same transactions  .
- Locking-based concurrency control protocols can also ensure deadlock-freedom, which is the property that no transaction is blocked indefinitely by another transaction's lock  .
- Locking-based concurrency control protocols can also ensure livelock-freedom, which is the property that no transaction is repeatedly aborted and restarted due to conflicts with other transactions  .
- Locking-based concurrency control protocols can also ensure starvation-freedom, which is the property that every transaction eventually gets the locks it needs  .
- Locking-based concurrency control protocols can also ensure fairness, which is the property that every transaction gets the locks it needs in a reasonable order  .
- Timestamp-based concurrency control algorithms use a transaction's timestamp to determine the order of conflicting operations



# Distributed Deadlocks

- A distributed deadlock is a situation where a set of processes in a distributed system are waiting for each other to release resources or messages, and none of them can proceed .
- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems .
- Distributed deadlocks are harder to detect, avoid, and prevent than deadlocks in centralized systems, because there is no single authority that can oversee resource allocation and monitor the state of the system.
- There are three main approaches to handle distributed deadlocks :
  - Prevention: This approach tries to ensure that deadlocks never occur by imposing some constraints on resource allocation, such as ordering, preemption, or timeouts. However, this approach may reduce the concurrency and performance of the system, and may not be applicable to all types of resources or requests.
  - Avoidance: This approach tries to avoid deadlocks by making careful decisions on resource allocation, based on the current and future requests of the processes. For example, a process may request all the resources it needs at once, or a resource manager may grant a resource only if it does not create a circular wait. However, this approach requires accurate and up-to-date information about the system state, which may be difficult or costly to obtain in a distributed system.
  - Detection and recovery: This approach tries to detect deadlocks after they occur, and then recover from them by aborting or restarting some of the processes involved, or by releasing some of the resources held. This approach requires a mechanism to detect deadlocks, either by constructing a global wait-for graph (WFG) from local wait-for graphs at a deadlock detector, or by a distributed algorithm like edge chasing  . This approach also requires a mechanism to select which processes or resources to terminate or release, and to coordinate the recovery actions among the processes. This approach may incur some overhead and delay in detecting and resolving deadlocks, and may also cause some loss of work or inconsistency in the system.



### Transaction recovery for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A distributed transaction is a transaction that spans multiple sites or nodes in a distributed system.
- A distributed transaction system must ensure the ACID properties of transactions: atomicity, consistency, isolation, and durability.
- Atomicity means that either all the operations of a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction does not interfere with other concurrent transactions.
- Durability means that the effects of a committed transaction are permanent and survive failures.
- Transaction recovery is the process of restoring the database to a consistent state after a failure or an abort.
- Transaction recovery in a distributed system is more complex than in a centralized system because of the following challenges:
  - Communication failures: A site may lose contact with other sites due to network problems or partitioning.
  - Site failures: A site may crash or become unavailable due to hardware or software faults.
  - Media failures: A disk or a file may be corrupted or damaged due to physical or logical errors.
  - Distributed concurrency control: A distributed transaction may encounter conflicts or deadlocks with other transactions at different sites.
  - Distributed commit protocol: A distributed transaction may need to coordinate with other sites to reach a global decision on whether to commit or abort.
- Transaction recovery in a distributed system relies on the following techniques:
  - Logging: A log is a record of the operations performed by a transaction and the data values affected by them. A log is maintained at each site and is used to undo or redo the operations of a transaction in case of a failure or an abort.
  - Checkpointing: A checkpoint is a point in time when the database is consistent and all the committed transactions have their effects written to the disk. A checkpoint is taken periodically at each site and is used to reduce the amount of logging and recovery work.
  - Shadow versions: A shadow version is a copy of a data item that is created before a transaction modifies it. A shadow version is used to restore the original value of the data item in case of an abort.
  - Two-phase commit protocol: A two-phase commit protocol is a protocol that ensures the atomicity of a distributed transaction by coordinating the commit or abort decision among all the sites involved in the transaction. The protocol consists of two phases: a prepare phase and a commit phase. In the prepare phase, the coordinator site asks all the participant sites to vote on whether to commit or abort the transaction. In the commit phase, the coordinator site decides on the final outcome based on the votes and informs all the participant sites to either commit or abort the transaction.



Hello, I am Sydney, your AI assistant. I can help you with your study material on replication. Here is some content in markdown format that you can use:

## Unit 10 - Replication

- Replication is the process of creating a copy or a duplicate of something, such as DNA, RNA, or a laboratory procedure .
- Replication is essential for the continuity of life, the transmission of genetic information, and the validity of scientific research .
- Replication can be divided into two types: biological replication and experimental replication.
  - Biological replication is the duplication of biological molecules or cells that capture random biological variation.
  - Experimental replication is the repetition of a laboratory or experimental procedure that reduces random experimental error.
- In this unit, we will focus on the molecular mechanism of DNA replication, which is the process by which a double-stranded DNA molecule is copied to produce two identical DNA molecules  .
- DNA replication involves the following steps :
  - Initiation: The DNA helix is unwound by a helicase enzyme at a specific site called the origin of replication, forming a Y-shaped structure called the replication fork. Single-strand binding proteins coat the separated strands to prevent them from reannealing. Topoisomerase enzymes relieve the torsional strain caused by the unwinding of the DNA. Primase enzymes synthesize short RNA primers that provide a free 3' hydroxyl group for the DNA polymerase to start adding nucleotides.
  - Elongation: The DNA polymerase enzyme adds nucleotides to the 3' end of the RNA primer, following the base-pairing rules of A with T and G with C. The DNA polymerase can only synthesize DNA in the 5' to 3' direction, so it moves along the template strand in the opposite direction. This creates a problem at the replication fork, where the two template strands are antiparallel. To solve this problem, one strand, called the leading strand, is synthesized continuously towards the replication fork, while the other strand, called the lagging strand, is synthesized discontinuously away from the replication fork, forming short fragments called Okazaki fragments. The RNA primers are later removed by another DNA polymerase and replaced with DNA nucleotides. The Okazaki fragments are joined together by an enzyme called DNA ligase, forming a continuous strand.
  - Termination: The DNA replication stops when the two replication forks meet each other or when they reach the end of the linear chromosome. In eukaryotes, the ends of the chromosomes, called telomeres, are protected by special proteins and enzymes that prevent the loss of genetic information and the fusion of chromosomes. In prokaryotes, the circular chromosome has a single origin of replication and a single termination site, where a protein called Tus binds and stops the helicase activity.

- DNA replication is a semi-conservative process, meaning that each new DNA molecule consists of one old strand and one new strand. This ensures the fidelity and accuracy of the genetic information. However, errors can still occur during DNA replication, such as mutations, insertions, deletions, or rearrangements of nucleotides. These errors can have various consequences, such as genetic diseases, cancer, or evolution. Therefore, DNA replication is also accompanied by various mechanisms of proofreading, repair, and regulation to maintain the integrity and stability of the genome.



### System model and group communication for replication in distributed systems

- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by exchanging messages.
- Replication is a technique to improve the availability, performance, and fault tolerance of a distributed system by creating and maintaining multiple copies of data or services across different processes or nodes.
- A system model is a set of assumptions and properties that describe the behavior and characteristics of a distributed system, such as the communication model, the failure model, the timing model, and the security model.
- A group is a subset of processes in a distributed system that share some common interest or functionality, such as a replicated service or a multicast group.
- Group communication is a mechanism to send and receive messages among the members of a group in a distributed system, such as broadcast, multicast, or anycast.
- Group communication can be classified into two types: reliable and unreliable.
  - Reliable group communication ensures that all the members of a group receive the same messages in the same order, regardless of failures or network delays.
  - Unreliable group communication does not guarantee any ordering or delivery properties, and may result in message losses, duplications, or reorderings.
- Group communication can be implemented using different protocols, such as IP multicast, gossip, or consensus.
  - IP multicast is a network-level protocol that allows a sender to transmit a single message to multiple receivers in a group, using a special address that represents the group.
  - Gossip is a peer-to-peer protocol that disseminates messages among the members of a group by randomly exchanging messages with a subset of neighbors in each round.
  - Consensus is a distributed algorithm that allows the members of a group to agree on a common value or decision, despite the presence of failures or asynchrony.
- Group communication is essential for replication in distributed systems, as it enables the coordination and synchronization of the replicas, the dissemination of updates and requests, and the detection and recovery of failures.



### Fault-tolerant services for the notes of the Unit 10 - Replication in the subject of DISTRIBUTED SYSTEM

- Fault-tolerant services are services that can continue to function correctly even in the presence of failures, such as server crashes, network partitions, or malicious attacks.
- Replication is a technique to implement fault-tolerant services by creating and maintaining multiple copies of the same service (or object) on different servers in a distributed system.
- Replication can improve availability, performance, and reliability of the service, but also introduces challenges such as consistency, coordination, and recovery.
- The correctness criterion for replicated services is linearizability, which means that every operation on the service appears to take effect atomically at some point between its invocation and response, and that the order of operations is consistent with the real-time order of invocations.
- There are two main classes of replication techniques: primary-backup replication and active replication.
  - Primary-backup replication assigns one server as the primary and the others as backups. The primary executes the operations and sends the updates to the backups. The backups apply the updates in the same order as the primary. If the primary fails, one of the backups takes over as the new primary.
  - Active replication assigns all servers as actives. The operations are multicast to all actives, which execute them in the same order and send the responses to the clients. If one or more actives fail, the others can still provide the service.
- Both replication techniques require a consensus protocol to ensure agreement among the servers on the order of operations and the identity of the primary. Consensus protocols can tolerate different types of faults, such as crash faults or Byzantine faults, depending on the assumptions and the number of servers.
- Replication can also be combined with coding theory to reduce the number of copies and the message overhead, while still ensuring fault-tolerance. This approach is called fused state machines, which encode the state of the service using erasure codes and distribute the encoded fragments to the servers. The servers can reconstruct the state from a subset of the fragments, and update the fragments using coded operations. This approach can achieve efficiency and savings in normal operations, but may incur higher overhead during recovery.



### Highly Available Services for the Notes of the Unit 10 - Replication in the Subject of Distributed System

- A highly available service is a service that can provide continuous and reliable operation despite the presence of failures in the system.
- Replication is a technique for increasing the availability of a service by creating and maintaining multiple copies of the service's data or state across different nodes in a distributed system.
- Replication can also improve the performance, scalability, and fault-tolerance of a service by reducing the load on a single node, allowing concurrent access to the data, and masking the failures of some nodes.
- Replication can be classified into two types: eager replication and lazy replication.
  - Eager replication ensures that all the replicas are updated as soon as a change occurs in the service's data or state. This provides strong consistency but incurs high communication and synchronization overheads.
  - Lazy replication allows some replicas to be updated later than others, after a change occurs in the service's data or state. This provides weak consistency but reduces the communication and synchronization overheads.
- Replication can also be classified into two modes: active replication and passive replication.
  - Active replication executes the same request on all the replicas in parallel, and uses a voting mechanism to determine the correct response. This provides high availability and fault-tolerance but requires more resources and coordination.
  - Passive replication executes the request on a primary replica, and propagates the updates to the backup replicas. This requires less resources and coordination but introduces a single point of failure and a potential inconsistency.
- Replication can be implemented using various protocols, such as primary-backup protocol, quorum protocol, gossip protocol, and state machine replication protocol.
  - Primary-backup protocol uses a primary replica to coordinate the updates and a set of backup replicas to store the copies of the data or state. The primary replica sends the updates to the backup replicas, and the backup replicas acknowledge the receipt of the updates. If the primary replica fails, a new primary replica is elected from the backup replicas.
  - Quorum protocol uses a set of replicas that are divided into read quorums and write quorums. A read quorum is a subset of replicas that can satisfy a read request, and a write quorum is a subset of replicas that can satisfy a write request. A read quorum and a write quorum must have at least one replica in common. A read request is sent to a read quorum, and a write request is sent to a write quorum. The replicas in the quorums coordinate to ensure the consistency of the data or state.
  - Gossip protocol uses a set of replicas that exchange updates with each other in a probabilistic manner. A replica that receives an update from another replica forwards the update to a randomly selected subset of replicas. The replicas eventually converge to a consistent state through repeated gossiping.
  - State machine replication protocol uses a set of replicas that execute the same deterministic state machine. A state machine is a model of computation that defines a set of states and a set of transitions between the states. A replica that receives a request from a client applies the request to its state machine and sends the response to the client. The replicas use a consensus protocol to agree on the order of the requests and ensure the consistency of the state machines.



### Transactions with replicated data

- Transactions are a sequence of operations that are executed atomically, consistently, isolatedly, and durably (ACID properties) on a database system.
- Replication is a technique to distribute data from a source server to other servers while keeping the data updated and synced with the source.
- Transactions with replicated data are transactions that involve data items that are stored in multiple servers and need to be coordinated to ensure the ACID properties.
- Some benefits of transactions with replicated data are:
  - Improved availability and fault tolerance: if one server fails, the data can be accessed from another server that has a copy of the data.
  - Improved performance and scalability: the load of transactions can be distributed among multiple servers, reducing the contention and latency of accessing the data.
  - Improved consistency and integrity: the data can be kept consistent and valid across all servers by applying the same transactions to all copies of the data.
- Some challenges of transactions with replicated data are:
  - Increased complexity and overhead: the coordination of transactions across multiple servers requires additional protocols and mechanisms to ensure the ACID properties, such as two-phase commit, distributed locking, or optimistic concurrency control  .
  - Increased network latency and bandwidth: the communication between servers to coordinate transactions can introduce delays and consume network resources, affecting the performance and availability of the system .
  - Increased possibility of conflicts and anomalies: the concurrent execution of transactions on replicated data can lead to conflicts and anomalies, such as lost updates, dirty reads, or inconsistent reads, if the transactions are not properly isolated and synchronized .
- Some solutions or approaches for transactions with replicated data are:
  - Primary-copy replication: one server is designated as the primary server for each data item, and the other servers are secondary servers that store copies of the data. Transactions are executed on the primary server and then propagated to the secondary servers. This approach simplifies the coordination of transactions, but introduces a single point of failure and a bottleneck for the primary server .
  - Quorum-based replication: each server has a vote for each data item, and a transaction needs to obtain a quorum (a majority) of votes to read or write the data item. This approach improves the availability and fault tolerance of the system, but increases the network overhead and the possibility of conflicts .
  - Optimistic replication: each server executes transactions locally without coordination, and then reconciles the data with other servers periodically or on demand. This approach improves the performance and scalability of the system, but requires a conflict resolution mechanism and may compromise the consistency and integrity of the data .

