

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
- Peer-to-peer networks, which are networks of equal nodes that can share resources and data without a central server.



## Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- The main characteristics of distributed systems are:
  - Concurrency: Multiple components can execute simultaneously and interact with each other.
  - No global clock: There is no shared physical clock among the components, and the clocks may drift apart over time.
  - Independent failures: Each component can fail independently without affecting the whole system, and the system should be able to tolerate and recover from failures.
  - Heterogeneity: The components may have different hardware, software, network, data formats, and protocols.
  - Scalability: The system should be able to grow in size and complexity without degrading its performance or functionality.
  - Transparency: The system should hide the details of its distribution from the users and provide a consistent and uniform interface.
- The main challenges of distributed systems are:
  - Communication: The components need to exchange messages over unreliable and heterogeneous networks, and deal with issues such as latency, bandwidth, congestion, and routing.
  - Coordination: The components need to synchronize their actions and agree on a consistent view of the system state, and cope with issues such as concurrency control, deadlock, and consensus.
  - Fault tolerance: The system needs to detect, mask, and recover from failures of components or communication links, and provide guarantees such as reliability, availability, and consistency.
  - Security: The system needs to protect its resources and data from unauthorized access, modification, or disclosure, and provide mechanisms such as authentication, authorization, encryption, and auditing.



### Introduction for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- A distributed system has the following characteristics:
  - Concurrency: The components of the system can execute simultaneously and independently.
  - No global clock: The components of the system do not share a common notion of time or a global clock.
  - Independent failures: The components of the system can fail independently and recover from failures without affecting the rest of the system.
  - Heterogeneity: The components of the system can have different hardware, software, network, and data formats.
  - Transparency: The system hides the details of its distribution from the users and provides a uniform interface and behavior.
- A distributed system has the following advantages:
  - Scalability: The system can grow in size and performance by adding more components without affecting the existing ones.
  - Availability: The system can tolerate failures and provide continuous service by replicating or replacing faulty components.
  - Resource sharing: The system can share and access resources across different locations and domains.
  - Fault tolerance: The system can detect and recover from errors and maintain consistency and correctness.
  - Performance: The system can distribute the workload and balance the load among the components to improve efficiency and speed.
- A distributed system has the following challenges:
  - Coordination: The system needs to coordinate the actions and states of the components to achieve a common goal or a consistent view.
  - Communication: The system needs to exchange messages and data among the components over a network that may be unreliable, insecure, or congested.
  - Consistency: The system needs to ensure that the components have a consistent view of the data and the system state despite concurrent updates and failures.
  - Security: The system needs to protect the data and the components from unauthorized access, modification, or disclosure.
  - Quality of service: The system needs to provide a satisfactory level of service to the users in terms of reliability, availability, latency, throughput, etc.



### Examples of Distributed Systems

A distributed system is a collection of independent computers that communicate and cooperate with each other to achieve a common goal. Distributed systems can have different architectures, such as client-server, peer-to-peer, or hybrid. Distributed systems can also have different properties, such as scalability, fault-tolerance, consistency, or availability.

Some examples of distributed systems are:

- **Telecommunication networks**: Telephone networks are an early example of a peer-to-peer network, where each phone can communicate with any other phone without a central server. Cellular and telephone networks are forms and examples of distributed networks .
- **Real-time systems**: Many industries use real-time systems distributed in various areas, locally and globally. For example, air traffic control systems, power grid systems, industrial control systems, or autonomous vehicles. These systems have strict timing and reliability requirements and need to coordinate actions across multiple nodes .
- **Distributed database systems**: A distributed database has locations across multiple servers, physical locations, or both. The data can be replicated or partitioned to improve performance, availability, or consistency. Examples of distributed databases are Google's Bigtable, Amazon's DynamoDB, or MongoDB .
- **Content delivery networks**: A content delivery network (CDN) is a system that distributes web content to users based on their geographic location, network conditions, or content type. A CDN consists of a network of servers that cache and deliver web pages, images, videos, or other content to users. Examples of CDNs are Akamai, Cloudflare, or Amazon CloudFront .
- **Distributed computing platforms**: A distributed computing platform is a system that allows multiple computers to work together on a common task, such as processing large data sets, performing complex calculations, or running simulations. Examples of distributed computing platforms are Apache Hadoop, Apache Spark, or Google's MapReduce.
- **Distributed file systems**: A distributed file system is a system that allows users to access and manipulate files stored on multiple computers as if they were on a single device. A distributed file system can provide features such as replication, caching, security, or concurrency control. Examples of distributed file systems are Google File System, Hadoop Distributed File System, or Network File System.
- **Distributed applications**: A distributed application is a software system that consists of multiple components that run on different computers and communicate over a network. A distributed application can have different architectures, such as service-oriented, microservices, or event-driven. Examples of distributed applications are web applications, online games, or peer-to-peer applications.



### Resource sharing and the web challenges

Resource sharing is the process of making the resources of a distributed system available to the users and applications in a transparent and efficient way. Resources can be hardware, software, or data. Resource sharing can be achieved by different methods, such as data migration, computation migration, and service sharing .

The web is an example of a large-scale distributed system that enables resource sharing among heterogeneous and geographically dispersed computers. The web challenges the design and implementation of distributed systems in several aspects, such as  :

- Scalability: The web must be able to handle the increasing number of users, requests, and data without degrading the performance or functionality of the system.
- Heterogeneity: The web must be able to communicate with different devices, platforms, protocols, and formats, and cope with the diversity and evolution of the web standards and technologies.
- Fault tolerance: The web must be able to tolerate the failures of individual components, such as servers, networks, or browsers, and provide reliable and consistent services to the users.
- Security: The web must be able to protect the confidentiality, integrity, and availability of the resources and the users from malicious attacks, such as unauthorized access, modification, or denial of service.
- Consistency: The web must be able to maintain the consistency of the data and the services across different replicas, caches, and updates, and provide the users with a coherent view of the system.
- Transparency: The web must be able to hide the complexity and the details of the distributed system from the users and the applications, and provide them with a simple and uniform interface to access the resources and the services.



### Architectural models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Architectural models are system models that describe the organization of components across the network and their interrelationship.
- Architectural models can help to design, implement, and evaluate distributed systems by providing a high-level view of the system structure and behavior.
- There are various hardware and software architectures that are commonly used for distributed computing, such as:
  - Client-server architecture: A distributed system where one or more servers provide services to multiple clients that request and consume them. This architecture forms the base for multi-tier architectures, where servers can be further divided into different layers of functionality, such as presentation, application, and data.
  - Broker architecture: A distributed system where a broker component acts as an intermediary between clients and servers, facilitating communication, coordination, and location transparency. An example of a broker architecture is the Common Object Request Broker Architecture (CORBA), which defines a standard for interoperability among heterogeneous distributed objects.
  - Service-oriented architecture (SOA): A distributed system where services are loosely coupled, reusable, and discoverable components that communicate using standard protocols and formats. An example of a service-oriented architecture is the Web Services Architecture, which uses XML, SOAP, WSDL, and UDDI to enable web-based service interactions.
  - Peer-to-peer architecture: A distributed system where each node can act as both a client and a server, sharing resources and collaborating with other nodes without a central authority or hierarchy. An example of a peer-to-peer architecture is the BitTorrent protocol, which enables efficient file distribution among multiple peers.
  - Distributed network architecture: A distributed system where each network can interact with other networks for the purpose of service resiliency, performance gains, and automated resource sharing. An example of a distributed network architecture is the Internet, which consists of multiple interconnected networks that use common protocols and standards.



### Fundamental Models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Fundamental models are descriptions of properties that are present in all distributed architectures  .
- They help us understand the characteristics, challenges and trade-offs of designing and implementing distributed systems.
- There are three main types of fundamental models: interaction models, failure models and security models  .

#### Interaction Models
- Interaction models deal with the issues of how processes communicate and coordinate with each other in a distributed system  .
- They include aspects such as performance, timing, ordering, synchronization and consistency of events and messages  .
- Some examples of interaction models are:
  - Synchronous vs. asynchronous communication: whether the sender and receiver of a message have to wait for each other or not  .
  - Remote procedure call (RPC): a method of invoking a procedure or function on a remote machine as if it were local  .
  - Publish-subscribe: a pattern where publishers send messages to a broker, and subscribers receive messages that match their interests  .
  - Message queue: a data structure that stores messages from senders and delivers them to receivers in a FIFO order  .

#### Failure Models
- Failure models specify the types of faults that can occur in processes and communication channels in a distributed system  .
- They help us design fault-tolerant mechanisms and protocols to cope with failures and ensure reliability and availability  .
- Some examples of failure models are:
  - Crash failure: a process stops executing and does not resume  .
  - Omission failure: a process fails to send or receive a message  .
  - Timing failure: a process does not meet the timing constraints of the system  .
  - Byzantine failure: a process behaves arbitrarily or maliciously  .

#### Security Models
- Security models define the threats and attacks that can compromise the confidentiality, integrity and availability of data and resources in a distributed system  .
- They help us design security mechanisms and protocols to protect the system from unauthorized access and manipulation  .
- Some examples of security models are:
  - Cryptographic model: a model that uses mathematical techniques to encrypt and decrypt data, and to verify the identity and authenticity of the sender and receiver  .
  - Access control model: a model that specifies the permissions and policies that govern who can access what data and resources in the system  .
  - Trust model: a model that evaluates the trustworthiness and reputation of the entities in the system based on their behavior and feedback  .



### Theoretical Foundation for Distributed System

- A distributed system is a collection of processes that are spatially separated and do not share a common memory and communicate with one another by exchanging messages with arbitrary delays .
- Theoretical foundation for distributed system aims to understand the inherent limitations, capabilities, and trade-offs of a distributed system and to develop abstract models, algorithms, and techniques for solving problems in a distributed environment .
- Some of the topics covered by the theoretical foundation for distributed system are:
  - Limitation of distributed system: such as the impossibility of consensus, the lack of global time, the uncertainty of failures, the complexity of coordination, and the scalability issues  .
  - Logical clocks: a way of ordering events in a distributed system based on causality and consistency, without relying on physical clocks. There are different types of logical clocks, such as Lamport's logical clocks and vector clocks, that have different properties and applications  .
  - Message passing system: a model of communication in a distributed system where processes exchange messages through channels that may have different characteristics, such as reliability, ordering, and synchrony. Message passing system can be used to implement various distributed algorithms, such as leader election, mutual exclusion, broadcast, and consensus  .



### Limitation of Distributed system

A distributed system is a system that consists of multiple independent components that communicate with each other over a network. Distributed systems have many advantages, such as scalability, availability, fault-tolerance, and performance. However, they also face some limitations that make them challenging to design and implement. Some of the main limitations of distributed systems are:

- **Absence of a global state**: In a distributed system, there is no single point of control or coordination for the entire system. Each component has its own local state and view of the system, which may differ from the views of other components. This makes it difficult to reason about the behavior and correctness of the system, and to synchronize the actions and data of different components. For example, it is hard to ensure consistency and atomicity of transactions that span multiple components, or to detect and resolve conflicts and failures that may occur in the system.

- **Absence of a global clock**: In a distributed system, there is no common notion of time or ordering of events for the entire system. Each component has its own local clock, which may drift or be inaccurate. This makes it hard to measure and compare the timestamps and durations of events that happen in different components, and to establish causality and concurrency relationships among them. For example, it is hard to implement synchronization and coordination mechanisms that rely on timestamps, such as mutual exclusion, election, or consensus algorithms.

- **Network latency and unreliability**: In a distributed system, the communication between components is subject to delays and failures that are unpredictable and variable. This makes it hard to guarantee the timeliness and reliability of the messages and data that are exchanged in the system, and to handle the possible errors and exceptions that may arise. For example, it is hard to determine if a component is alive or dead, or if a message has been delivered or lost, or if a data item is up-to-date or stale.

- **Security and privacy issues**: In a distributed system, the components and the network may be exposed to malicious attacks or unauthorized access that compromise the integrity and confidentiality of the system. This makes it hard to ensure the security and privacy of the messages and data that are transmitted and stored in the system, and to protect the system from threats such as eavesdropping, tampering, spoofing, or denial-of-service attacks.

- **Complexity and heterogeneity**: In a distributed system, the components and the network may have different characteristics, capabilities, and requirements that vary over time and space. This makes it hard to design and implement a system that is compatible and adaptable to the diversity and dynamism of the system, and to manage the complexity and heterogeneity of the system. For example, it is hard to deal with the issues such as interoperability, scalability, load balancing, or fault tolerance that arise in a distributed system.



### Absence of Global Clock

- A global clock is a system-wide clock that is equally accessible to all processes in a distributed system and provides a common notion of time.
- A global clock is useful for determining the order of events, synchronizing processes, and obtaining a consistent state of the system.
- However, a global clock is hard to realize in distributed systems due to two inherent limitations: lack of shared memory and unpredictable message delays.
- Lack of shared memory means that processes in a distributed system do not have access to a common storage that can store and update the global clock value.
- Unpredictable message delays mean that the communication channel between processes is unreliable and the transmission time of messages is variable and unknown.
- Therefore, processes in a distributed system may have different and inaccurate views of the global clock value, and the global clock may not reflect the actual order of events or the actual state of the system.
- Due to the absence of a global clock, distributed systems have to rely on other mechanisms to achieve coordination, consistency, and correctness. Some of these mechanisms are logical clocks, vector clocks, causal ordering, global snapshots, and distributed algorithms.



### Shared Memory

- Shared memory is a form of memory architecture where physically separated memories can be addressed as a single shared address space.
- Shared memory can be implemented in hardware or software, or a combination of both.
- Shared memory can be used to facilitate communication and synchronization among processes or threads in a distributed system.
- Shared memory can be classified into two types: physical shared memory and distributed shared memory.

#### Physical Shared Memory

- Physical shared memory is a memory architecture where multiple processors or nodes share a common physical memory.
- Physical shared memory can be accessed by all processors or nodes using the same address space.
- Physical shared memory requires hardware support for cache coherence, memory consistency, and memory protection.
- Physical shared memory can provide high performance and low latency, but it is limited by the scalability and reliability of the hardware.

#### Distributed Shared Memory

- Distributed shared memory (DSM) is a memory architecture where multiple processors or nodes have their own local memories, but they can access each other's memories as if they were shared.
- Distributed shared memory can be implemented using software techniques, such as page-based, object-based, or tuple-based approaches .
- Distributed shared memory provides a virtual address space that is shared among all processors or nodes.
- Distributed shared memory can overcome the limitations of physical shared memory, such as scalability and reliability, but it introduces challenges such as data consistency, data replication, and data migration .



### Logical Clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A logical clock is a mechanism for capturing chronological and causal relationships in a distributed system  .
- A distributed system may have no physically synchronous global clock, so a logical clock allows global ordering on events from different processes in such systems .
- A logical clock is not a physical device, but a software counter that is incremented according to some rules .
- A logical clock can be used for computation analysis, distributed algorithm design, individual event tracking, and exploring computational progress .
- Some examples of logical clock algorithms are:
  - Lamport timestamps, which are monotonically increasing software counters that are updated based on the send and receive events of messages .
  - Vector clocks, which are arrays of software counters that are updated based on the send, receive, and local events of processes .
  - Matrix clocks, which are matrices of software counters that are updated based on the send, receive, and local events of processes and also capture the causal dependencies among them.
- The main properties of logical clocks are:
  - Consistency: If event A causally precedes event B, then the logical clock value of A is less than the logical clock value of B  .
  - Accuracy: The logical clock values reflect the actual order of events as closely as possible  .
  - Efficiency: The logical clock algorithm should have low overhead in terms of time and space complexity  .



### Lamport's logical clocks

- Lamport's logical clocks are a way of ordering events in a distributed system based on their causal relationships, rather than their physical timestamps.
- Lamport's logical clocks are also known as logical timestamps or scalar clocks.
- Lamport's logical clocks are based on the idea of a **happens-before** relation, denoted by `->`, which captures the notion of causality between events.
- If `a` and `b` are events on the same process, then `a -> b` if `a` occurs before `b` based on the local clock.
- If `a` is the event of sending a message by one process and `b` is the event of receiving that message by another process, then `a -> b`.
- If `a -> b` and `b -> c`, then `a -> c`. This is the transitivity property of the happens-before relation.
- Two events `a` and `b` are said to be **concurrent** if neither `a -> b` nor `b -> a`. This means that they are causally unrelated and can happen in any order.
- Lamport's logical clocks assign a numerical value, called a **logical clock**, to each event in a distributed system. This value is maintained by each process and incremented whenever an event occurs.
- The logical clock of an event is denoted by `C(a)`, where `C` is a function that maps events to integers.
- The logical clocks satisfy the following rules:
  - If `a` and `b` are events on the same process, and `a` occurs before `b`, then `C(a) < C(b)`.
  - If `a` is the event of sending a message by one process and `b` is the event of receiving that message by another process, then `C(a) < C(b)`.
  - A process increments its logical clock before sending a message, and includes the logical clock value in the message.
  - A process updates its logical clock when receiving a message, by taking the maximum of its own logical clock and the logical clock value in the message, and then increments it by one.
- Lamport's logical clocks ensure that if `a -> b`, then `C(a) < C(b)`. However, the converse is not true, i.e., if `C(a) < C(b)`, it does not imply that `a -> b`. This means that Lamport's logical clocks can only partially order events, and cannot distinguish between concurrent events.
- Lamport's logical clocks are simple and easy to implement, but they have some limitations. For example, they cannot capture the causal dependencies between events that happen on different processes, and they cannot measure the actual duration of events or the physical time difference between them.



### Concepts in Message Passing Systems for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Message passing is a technique for invoking behavior on a computer by sending a message to a process, which may be an actor or object, and relying on that process and its supporting infrastructure to then select and run some appropriate code.
- Message passing is used in distributed systems, where communication is carried out between processes by passing messages from one process to another .
- A message-passing system is a subsystem of a distributed operating system that provides a set of message-based interprocess communication (IPC) protocols while sheltering programmers from the complexities of sophisticated network protocols and many heterogeneous platforms.
- Message passing systems can be classified into two categories: synchronous and asynchronous.
  - Synchronous message passing systems require the sender and the receiver to be ready at the same time for the communication to take place. The sender blocks until the receiver acknowledges the message, and the receiver blocks until a message arrives.
  - Asynchronous message passing systems do not require the sender and the receiver to be ready at the same time. The sender can send a message and continue its execution without waiting for the receiver's acknowledgment, and the receiver can receive a message at any time without blocking.
- Message passing systems can also be classified into two types: direct and indirect.
  - Direct message passing systems require the sender and the receiver to explicitly name each other in the communication. A communication link must be established between the cooperating processes before messages can be sent.
  - Indirect message passing systems do not require the sender and the receiver to explicitly name each other in the communication. Instead, messages are sent and received through a common entity called a mailbox or a port, which acts as an intermediary between the processes.
- Message passing systems can have different features that affect their performance and reliability, such as message ordering, message buffering, message delivery guarantees, message format, message size, message security, and message routing.
- Message passing systems can be implemented using different methods, such as sockets, remote procedure calls (RPCs), remote method invocation (RMI), message-oriented middleware (MOM), and publish-subscribe systems.
- Message passing systems can be used for various purposes in distributed systems, such as data transfer, synchronization, coordination, load balancing, fault tolerance, and distributed algorithms.



### Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent and autonomous processes that communicate by exchanging messages over a network.
- The processes in a distributed system may have different views of the global state of the system, depending on the order and delivery of the messages they receive.
- Causal order is a relation that captures the potential causal dependencies between the events that occur in a distributed system.
- An event is causally dependent on another event if the occurrence of the first event influences or affects the occurrence of the second event, either directly or indirectly.
- For example, if process A sends a message m to process B, and process B sends a message n to process C after receiving m, then the event of sending n is causally dependent on the event of sending m, and the event of receiving n is causally dependent on the event of receiving m.
- Causal order is a partial order, meaning that not all events are comparable. Two events are concurrent if they are not causally dependent on each other, meaning that they could have occurred in any order without affecting the outcome of the system.
- Causal order is important for ensuring the consistency and correctness of distributed systems, especially for applications that require coordination, synchronization, or replication of data or state across multiple processes.
- Causal order can be enforced by various algorithms or protocols that ensure that messages are delivered and processed in a way that respects the causal dependencies between them.
- Some examples of causal order algorithms or protocols are:
  - Vector clocks: a mechanism that assigns a logical timestamp to each event, consisting of a vector of integers that represents the number of events that each process has observed or caused. A vector clock can be used to compare the causal order of two events by comparing their timestamps element-wise.
  - Lamport timestamps: a simpler mechanism that assigns a scalar timestamp to each event, consisting of a single integer that represents the number of events that a process has observed or caused. A Lamport timestamp can be used to compare the causal order of two events by comparing their timestamps numerically.
  - Causal multicast: a communication service that guarantees that messages are delivered to all processes in the same causal order as they were sent. Causal multicast can be implemented using vector clocks or Lamport timestamps to label and order the messages.
  - Causal consistency: a consistency model that ensures that all processes see the same order of updates to a shared data item, as long as those updates are causally dependent on each other. Causal consistency can be achieved by using causal multicast or other mechanisms to propagate the updates.



### Total Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent entities that communicate by message passing and coordinate their actions to achieve a common goal.
- Events are occurrences that happen at a specific point in time and space in a distributed system, such as sending or receiving a message, or executing a local operation.
- The order of events is important for understanding the behavior and correctness of a distributed system, especially when there are concurrent or conflicting events.
- A partial order is a binary relation that satisfies three properties: reflexivity, antisymmetry, and transitivity. A partial order can be represented by a directed acyclic graph (DAG) or a Hasse diagram.
- A total order is a partial order that also satisfies the property of totality, which means that any two events are comparable, i.e., either one happens before the other or they are equal. A total order can be represented by a linear sequence or a timeline.
- A distributed system is said to have partial order if we can have a partial order relationship among the events in the system. If totality, i.e., causal relationship among all events in the system, can be established, then the system is said to have total order .
- Total order is useful for ensuring consistency, agreement, and coordination among the entities in a distributed system, especially when there are failures, delays, or asynchrony.
- Total order can be achieved by using logical clocks, such as Lamport timestamps or vector clocks, that assign a unique and monotonically increasing value to each event based on the causal dependencies among them .
- Total order can also be achieved by using consensus algorithms, such as Paxos or Raft, that allow the entities to agree on a single value or a sequence of values that represent the order of events in the system.
- Total order can be implemented by using various protocols, such as multicast, broadcast, or atomic commit, that ensure that the messages are delivered to all the entities in the same order and without duplication or loss.



### Total Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems in the Subject of Distributed System

- A distributed system is a collection of independent and autonomous processes that communicate and coordinate with each other by exchanging messages.
- Events are the actions or occurrences that happen in a distributed system, such as sending or receiving a message, executing a local operation, or detecting a failure.
- The order of events is important for understanding the behavior and correctness of a distributed system, especially in the presence of concurrency and failures.
- A partial order is a binary relation that satisfies three properties: reflexivity, antisymmetry, and transitivity. A partial order can be represented by a directed acyclic graph (DAG), where the nodes are the events and the edges are the order relation.
- A causal order is a partial order that captures the notion of potential causality or influence between events. An event e1 is causally related to an event e2, denoted by e1 -> e2, if one of the following conditions holds:
  - e1 and e2 are events in the same process, and e1 happened before e2.
  - e1 is the sending of a message m, and e2 is the receipt of the same message m.
  - There exists an event e3 such that e1 -> e3 and e3 -> e2.
- A causal order can be implemented by using logical clocks, which are counters that are incremented by each process at each local event and piggybacked on each message. A logical clock value can be used to label an event, and the causal order relation can be determined by comparing the logical clock values of the events.
- A total order is a partial order that satisfies an additional property: totality. This means that for any two events e1 and e2 in the system, either e1 -> e2 or e2 -> e1 or both. A total order can be represented by a linear sequence, where the events are ordered from left to right according to the order relation.
- A total order is useful for ensuring consistency and agreement among the processes in a distributed system, such as when delivering messages, taking snapshots, or executing transactions.
- A total order can be implemented by using physical clocks, which are synchronized clocks that measure the real time. A physical clock value can be used to label an event, and the total order relation can be determined by comparing the physical clock values of the events.
- A total-causal order is a total order that is consistent with the causal order, meaning that if e1 -> e2 in the causal order, then e1 -> e2 in the total order as well. A total-causal order is the strictest ordering in distributed systems; it establishes only one linearization, consistent with the causal ordering, among all the events that occur in the system, even those that occur concurrently.
- A total-causal order can be implemented by using a combination of logical and physical clocks, or by using a distributed algorithm that assigns a unique sequence number to each event based on the causal order and the process identifier. A total-causal order can be used to provide fault tolerance and reliability for constructing distributed systems.



### Techniques for Message Ordering in Distributed Systems

- Message ordering is the problem of ensuring that messages are processed in a consistent and predictable order in a distributed system .
- Message ordering is important because it affects the final outcome of the actions and the correctness of the algorithms in a distributed system .
- There are different types of message ordering techniques, depending on the desired level of consistency and synchronization among the processes in the system  .
- Some of the common message ordering techniques are:

  - **Unordered**: Messages are delivered in any order, without any guarantee of consistency or synchronization. This is the simplest and fastest technique, but also the least reliable and useful .
  - **FIFO**: Messages are delivered in the same order as they are sent by each sender, but not necessarily in the same order as they are received by each receiver. This technique ensures that messages from the same sender are processed in a sequential order, but does not guarantee any global order among messages from different senders .
  - **Causal**: Messages are delivered in a way that respects the causal dependencies among them, meaning that if a message m1 causally precedes a message m2, then m1 is delivered before m2 at every receiver. This technique ensures that messages that are related by some logical or temporal relation are processed in a consistent order, but does not guarantee any total order among unrelated messages  .
  - **Total**: Messages are delivered in the same order at every receiver, regardless of their causal dependencies or their senders. This technique ensures that messages are processed in a globally consistent order, but also requires a high degree of synchronization and coordination among the processes in the system .
  - **Synchronous**: Messages are delivered in the same order at every receiver, and also in the same order as they are sent by each sender. This technique ensures that messages are processed in a globally and locally consistent order, but also requires the highest degree of synchronization and coordination among the processes in the system .

- Each message ordering technique has its own advantages and disadvantages, depending on the application and the network characteristics of the distributed system. There is no single best technique for all scenarios, and different techniques may be combined or adapted to suit different needs  .



### Causal ordering of messages

- Causal ordering of messages is a partial ordering of messages in a distributed computing environment .
- It places a restriction on communication between processes by requiring that if the transmission of message mi to process pk necessarily preceded the transmission of message mj to the same process, then the delivery of these messages to that process must be ordered such that mi is delivered before mj  .
- Causal ordering of messages is one of the four semantics of multicast communication, namely unordered, totally ordered, causal, and sync-ordered communication.
- Multicast communication methods vary according to the message’s reliability guarantee and ordering guarantee.
- Causal ordering of messages is useful for applications that need to preserve the logical dependencies between events in a distributed system .
- Causal ordering of messages is not automatically guaranteed in distributed systems, because of transmission delays, network congestion, or clock synchronization issues .
- To achieve causal ordering of messages, various algorithms have been proposed, such as vector clocks, logical clocks, or piggybacking techniques  .
- These algorithms use timestamps or counters to label the messages and compare them at the receiver side to determine the causal order  .
- Causal ordering of messages is a weaker form of ordering than total ordering or synchronous ordering, but stronger than unordered or FIFO ordering .



### Global State for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent processes that communicate through message passing.
- The global state of a distributed system is the union of the local states of the processes and the channels .
- A local state of a process is the values of its variables and registers at a given point in time.
- A channel state is the set of messages that have been sent but not yet received by the processes.
- A global state is consistent if it reflects a possible execution of the system, i.e., no causal violations occur .
- A causal violation is when a message is received before it is sent, or a process observes the effect of a message before it observes the message itself.
- A consistent global state can be used for various purposes, such as debugging, checkpointing, termination detection, garbage collection, etc .
- A consistent global state can be recorded by using distributed snapshot algorithms, which capture the local states of the processes and the channel states in a coordinated manner.
- A distributed snapshot algorithm must satisfy two properties:
  - Safety: The recorded global state is consistent.
  - Liveness: The algorithm eventually terminates and does not interfere with the normal execution of the system.



### Termination Detection

Termination detection is a fundamental problem in distributed systems, where a set of processes cooperate to perform a computation. The goal is to determine when all the processes have finished their work and there are no more messages in transit between them. This is non-trivial because no process has complete knowledge of the global state, and global time does not exist.

One of the algorithms for termination detection is Huang's algorithm, proposed by Shing-Tsaan Huang in 1989. The algorithm is based on the concept of a process' state, which can be either active or idle. An active process may become idle at any time, but an idle process may only become active again upon receiving a computational message (a message that affects the computation). A process that is idle and has no outgoing messages is called passive.

The algorithm works as follows:

- Each process maintains a counter of the number of messages it has sent and received, called the diff count. The diff count is initialized to zero, and is incremented by one for each message sent, and decremented by one for each message received.
- Each process also maintains a control message, which contains its diff count and a boolean flag indicating whether it is passive or not. The control message is initialized to (0, false), and is updated whenever the diff count or the state changes.
- There is a designated process, called the initiator, that initiates and coordinates the termination detection. The initiator periodically sends a probe message to its neighbor in a logical ring of processes, and waits for a reply. The probe message contains the initiator's control message.
- When a process receives a probe message, it compares its control message with the one in the probe. If they are the same, it means that the process has not changed its state or diff count since the last probe, and it forwards the probe to its neighbor. If they are different, it means that the process has changed its state or diff count since the last probe, and it updates the probe with its current control message, and resets its own control message to (0, false). It then forwards the updated probe to its neighbor.
- When the initiator receives the probe back, it checks the control message in the probe. If it is (0, true), it means that all the processes are passive and the diff count is zero, which implies that the computation has terminated. If it is not (0, true), it means that some processes are still active or there are still messages in transit, and the computation has not terminated. The initiator then waits for some time and repeats the process.

The algorithm ensures that the termination is detected correctly and eventually, and does not interfere with the underlying computation. The algorithm also does not require additional communication channels between processes, and only uses one probe message at a time. The algorithm has a time complexity of O(n), where n is the number of processes, and a message complexity of O(m), where m is the number of messages exchanged in the computation.



## Unit 2 - Distributed Mutual Exclusion

- Distributed mutual exclusion is the problem of ensuring that only one process at a time can access a shared resource in a distributed system.
- Distributed mutual exclusion algorithms can be classified into two categories: permission-based and token-based.
- Permission-based algorithms require a process to obtain permission from other processes before entering the critical section. Examples of permission-based algorithms are Ricart-Agrawala algorithm, Lamport's algorithm, and Maekawa's algorithm.
- Token-based algorithms use a special message, called a token, that grants the right to enter the critical section. A process can enter the critical section only if it has the token. Examples of token-based algorithms are Suzuki-Kasami algorithm, Raymond's algorithm, and Singhal's algorithm.
- The performance of distributed mutual exclusion algorithms can be measured by the following metrics: message complexity, synchronization delay, response time, and fault tolerance.



### Classification of distributed mutual exclusion

- Distributed mutual exclusion is a problem of ensuring that only one process can access a shared resource or data at a time in a distributed system.
- Distributed mutual exclusion algorithms are solutions that use message passing to coordinate the access of processes to the shared resource or data.
- Distributed mutual exclusion algorithms can be classified into three basic approaches: token-based, non-token-based, and quorum-based .

- Token-based approach: A unique token is shared among the sites. A site is allowed to enter its critical section if it possesses the token. Mutual exclusion is ensured because the token is unique. Examples of token-based algorithms are Suzuki-Kasami's algorithm, Raymond's algorithm, and Maekawa's algorithm .
- Non-token-based approach: A site requests permission from other sites before entering its critical section. A site is allowed to enter its critical section if it receives permission from all or a majority of other sites. Mutual exclusion is ensured by the voting mechanism. Examples of non-token-based algorithms are Ricart-Agrawala's algorithm, Lamport's algorithm, and Singhal's algorithm .
- Quorum-based approach: A site requests permission from a subset of sites, called a quorum, before entering its critical section. A site is allowed to enter its critical section if it receives permission from all the sites in its quorum. Mutual exclusion is ensured by the intersection property of quorums. Examples of quorum-based algorithms are Sankararaman's algorithm, Agrawal-El Abbadi's algorithm, and Thomas's algorithm .



### Requirement of mutual exclusion theorem for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM

- Mutual exclusion is a concurrency control property which is introduced to prevent race conditions.
- It is the requirement that a process can not enter its critical section while another concurrent process is currently present or executing in its critical section i.e only one process is allowed to execute the critical section at any given time.
- A critical section is a section of code that accesses a shared resource or data.
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

- Distributed mutual exclusion (DME) is the problem of ensuring that only one process at a time can access a shared resource in a distributed system.
- There are two main approaches to solve DME: token based and non token based algorithms.
- Token based algorithms use a special message, called a token, that grants the permission to enter the critical section. Only the process that holds the token can access the shared resource. The token is passed among the processes in a predefined order or based on requests.
- Non token based algorithms use timestamps to order the requests for the critical section and to resolve conflicts between simultaneous requests. A process communicates with a set of other processes to determine who should execute the critical section next. The process that has the earliest timestamp or the highest priority is granted the permission.
- Some examples of token based algorithms are:
  - Suzuki-Kasami algorithm: a modification of Ricart-Agrawala algorithm, which uses a token that contains a vector of sequence numbers. The token is sent to the process that has the highest sequence number in the vector.
  - Raymond's algorithm: a tree-based algorithm, which organizes the processes in a logical tree. The token is initially held by the root of the tree. A process that wants to enter the critical section sends a request to its parent in the tree. The token is forwarded along the path from the holder to the requester.
- Some examples of non token based algorithms are:
  - Lamport's algorithm: a basic algorithm, which uses logical clocks to assign timestamps to the requests. A process that wants to enter the critical section broadcasts its request with its timestamp to all other processes. A process replies to a request if it is not in the critical section or it has a later timestamp. A process enters the critical section when it receives replies from all other processes.
  - Maekawa's algorithm: a voting-based algorithm, which divides the processes into disjoint subsets, called quorums. A process that wants to enter the critical section sends a request to all processes in its quorum. A process grants a vote to a request if it has not voted for another request. A process enters the critical section when it receives votes from all processes in its quorum.



### Performance metric for distributed mutual exclusion algorithms

- Distributed mutual exclusion algorithms are algorithms that ensure that only one process can access a shared resource or execute a critical section at a time in a distributed system.
- The performance of distributed mutual exclusion algorithms can be evaluated by the following four metrics :
  - **Message complexity**: It is the number of messages that are required per critical section execution by a process. It reflects the communication overhead and network congestion caused by the algorithm. The lower the message complexity, the better the performance.
  - **Synchronization delay**: It is the time elapsed between the moment a process leaves the critical section and the moment the next process enters the critical section. It reflects the degree of concurrency and fairness achieved by the algorithm. The lower the synchronization delay, the better the performance.
  - **Response time**: It is the time elapsed between the moment a process requests to enter the critical section and the moment it actually enters the critical section. It reflects the waiting time and the latency experienced by the process. The lower the response time, the better the performance.
  - **Throughput**: It is the number of critical section executions per unit time in the system. It reflects the efficiency and utilization of the shared resource by the algorithm. The higher the throughput, the better the performance.
- Different distributed mutual exclusion algorithms may have different trade-offs among these metrics, depending on the underlying assumptions, design choices, and network conditions. For example, some algorithms may achieve low message complexity but high synchronization delay, while others may achieve low synchronization delay but high message complexity.
- Some examples of distributed mutual exclusion algorithms are:
  - **Central server algorithm**: One process acts as the coordinator and grants access to the critical section to other processes based on a request queue. It has low message complexity (two messages per critical section execution) but high synchronization delay and response time (depending on the coordinator's availability and network delay) .
  - **Token ring algorithm**: A unique token is circulated among the processes in a logical ring. A process can enter the critical section only if it holds the token. It has low message complexity (one message per critical section execution) but high synchronization delay and response time (depending on the token's position and network delay) .
  - **Ricart-Agrawala algorithm**: A process broadcasts its request to enter the critical section to all other processes and waits for their replies. A process replies to a request only if it is not in the critical section or it has a lower priority. It has high message complexity ((n-1) messages per critical section execution, where n is the number of processes) but low synchronization delay and response time (depending on the network delay) .



## Unit 3 - Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set, and none of the processes can proceed.
- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems.
- Deadlock detection in distributed systems entails addressing two basic issues: detection of existing deadlocks and resolution of detected deadlocks.
- Deadlock detection requires examination of the status of process-resource interactions for presence of cyclic wait.
- There are three approaches to detect deadlocks in distributed systems: global wait-for graph, edge chasing, and probe-based.
- Global wait-for graph: A deadlock detector collects local wait-for graphs from all sites and constructs a global wait-for graph. A cycle in the global wait-for graph indicates a deadlock.
- Edge chasing: A deadlock detector initiates a probe message along the edges of the local wait-for graph. If the probe message returns to the initiator, a deadlock is detected.
- Probe-based: A deadlock detector periodically sends a probe message to each process. The probe message contains the identifier of the sender and a timestamp. If a process receives a probe message with its own identifier or a smaller timestamp, it detects a deadlock.
- To resolve the deadlock, one or more deadlocked processes have to be aborted. The selection of the victim process can be based on criteria such as priority, execution time, number of resources, etc.



### System Model for Distributed Deadlock Detection

- A distributed system consists of a collection of nodes that communicate and cooperate to achieve a common goal.
- A node can be a process, a processor, a computer, or a cluster of computers.
- A node can request, hold, and release resources that are shared among the nodes.
- A resource can be a physical device, a logical entity, or a message.
- A node can be in one of the following states: active, waiting, or blocked.
- An active node is executing its own instructions and does not need any resource.
- A waiting node is waiting for a resource that is currently held by another node.
- A blocked node is waiting for a resource that is not currently available in the system.
- A node can transition from one state to another by sending or receiving messages.
- A deadlock is a situation where a set of nodes are blocked and none of them can proceed.
- A deadlock can be detected by examining the status of the nodes and the resources in the system.
- A wait-for graph (WFG) is a directed graph that represents the dependency among the nodes and the resources in the system.
- A node in the WFG is either a process node or a resource node.
- A process node corresponds to a node in the distributed system that is waiting or blocked.
- A resource node corresponds to a resource in the distributed system that is held by a node or requested by a node.
- An edge in the WFG is either a request edge or an assignment edge.
- A request edge goes from a process node to a resource node, indicating that the process is waiting for the resource.
- An assignment edge goes from a resource node to a process node, indicating that the resource is held by the process.
- A cycle in the WFG indicates the existence of a deadlock in the system.
- A global WFG is a WFG that contains all the nodes and edges in the distributed system.
- A local WFG is a WFG that contains only the nodes and edges that are relevant to a subset of the nodes in the distributed system.
- A system model for distributed deadlock detection defines the following components:
  - The structure and representation of the WFG.
  - The algorithm and protocol for constructing and updating the WFG.
  - The mechanism and frequency for detecting cycles in the WFG.
  - The strategy and policy for resolving deadlocks in the system.



### Resource Vs Communication Deadlocks

- A deadlock is a condition where a process cannot proceed because it needs to obtain a resource held by another process, and it itself is holding a resource that the other process needs.
- Four requirements must be met for a deadlock to occur: mutual exclusion, hold and wait, no preemption, and circular wait.
- In distributed systems, deadlocks can be classified into two types: resource deadlocks and communication deadlocks.
- Resource deadlocks occur when processes access resources, such as data objects in database systems and buffers in store and forward communication networks.
- A process acquires a resource before accessing it and releases it after using it.
- Resource deadlocks can be detected by constructing a wait-for graph, where nodes represent processes and edges represent resource requests.
- Communication deadlocks occur when processes exchange messages, such as in message passing systems and distributed algorithms.
- A process sends a message to another process and waits for a reply before continuing.
- Communication deadlocks can be detected by constructing a dependency graph, where nodes represent processes and edges represent message dependencies.
- The main difference between resource deadlocks and communication deadlocks is that resource deadlocks involve contention for resources, while communication deadlocks involve loss or corruption of signals.
- Another difference is that resource deadlocks can be resolved by aborting or preempting processes, while communication deadlocks can be resolved by retransmitting or discarding messages.
- Both types of deadlocks can be prevented by avoiding the four requirements for deadlock occurrence, such as using timeouts, ordering resources, or using deadlock-free algorithms .



### Deadlock Prevention for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

- A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
- A distributed deadlock is a deadlock that involves processes and resources located on different machines connected by a network.
- Deadlock prevention is a technique to ensure that at least one of the necessary conditions for deadlock does not hold in a system.
- There are two main ways to prevent deadlock in a distributed system: ordered request and collective request.
- Ordered request is a method where each resource type is assigned a certain level and a process can only request resources in increasing order of levels. This prevents circular wait condition.
- Collective request is a method where a process must request all the resources it needs at the same time before starting execution. This prevents hold and wait condition.
- Both methods have some drawbacks, such as reduced concurrency, increased overhead, and increased complexity.



### Avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- Deadlock avoidance is a technique that prevents the occurrence of deadlocks by ensuring that the system is always in a safe state.
- A safe state is a state where there exists a safe sequence of processes that can finish their execution without causing a deadlock.
- In a distributed system, deadlock avoidance is impractical due to several problems, such as:
  - The lack of global information about the resource allocation and request of all processes in the system.
  - The dynamic and unpredictable nature of the system, where processes and resources may join or leave at any time.
  - The high communication and synchronization overhead involved in maintaining a global safe state.
- Therefore, deadlock detection is preferred over deadlock avoidance in distributed systems, as it allows more concurrency and flexibility in resource allocation and request.
- Deadlock detection is a technique that identifies the existence of a deadlock after it has occurred, and then takes some recovery actions to resolve it.
- Deadlock detection in distributed systems requires the following steps:
  - Collecting local information about the resource allocation and request of each process in the system.
  - Constructing a global wait-for graph that represents the dependency among processes and resources in the system.
  - Detecting a cycle in the wait-for graph, which indicates a deadlock condition.
  - Initiating a recovery procedure to break the cycle and release some resources.
- Deadlock detection algorithms in distributed systems can be classified into four categories, based on the way they construct and analyze the wait-for graph:
  - Path-pushing algorithms, which propagate the dependency information along the paths of the wait-for graph.
  - Edge-chasing algorithms, which send probe messages along the edges of the wait-for graph to detect cycles.
  - Diffusion computation algorithms, which perform a distributed computation to determine the deadlock status of each process.
  - Global state detection algorithms, which collect and examine the global state of the system to detect cycles.



### Detection and Resolution of Distributed Deadlocks

- A distributed deadlock is a situation where a set of processes in a distributed system are waiting for each other to release resources, and none of them can proceed.
- A distributed deadlock can be detected by constructing a global wait-for graph (WFG) that represents the dependencies among the processes and the resources in the system.
- A cycle in the WFG indicates the presence of a deadlock. A knot is a strongly connected component of the WFG that contains all the processes and resources involved in a deadlock.
- There are two main issues in deadlock detection: how to maintain the WFG and how to search the WFG for cycles or knots.
- There are three approaches to maintain the WFG: centralized, distributed, and hierarchical.
  - In the centralized approach, a single coordinator is responsible for collecting the information about the local WFGs of each site and constructing the global WFG. The coordinator periodically initiates a detection algorithm and searches the global WFG for cycles or knots. The advantages of this approach are simplicity and efficiency, but the disadvantages are the single point of failure and the communication overhead.
  - In the distributed approach, each site maintains its own local WFG and exchanges information with other sites to construct a global WFG. The detection algorithm is initiated by any site that suspects a deadlock and involves a distributed cycle detection algorithm. The advantages of this approach are fault tolerance and scalability, but the disadvantages are the complexity and the synchronization issues.
  - In the hierarchical approach, the sites are organized into a tree structure, and each site maintains a partial WFG that includes its descendants in the tree. The detection algorithm is initiated by the root of the tree and involves a hierarchical cycle detection algorithm. The advantages of this approach are the reduced communication overhead and the balanced load, but the disadvantages are the possible false deadlocks and the dependency on the tree structure.
- There are two main methods to search the WFG for cycles or knots: edge chasing and diffusing computation.
  - In the edge chasing method, a special message called a probe is sent along the edges of the WFG to detect a cycle. A probe contains the identifiers of the processes and resources that it has visited. If a probe returns to its originator, a cycle is detected. The advantages of this method are the simplicity and the low storage requirement, but the disadvantages are the possible message duplication and the delay in detection.
  - In the diffusing computation method, a distributed computation is initiated by a site that suspects a deadlock and involves the cooperation of other sites. A computation consists of a set of agents that are created, propagated, and terminated by the sites. An agent carries the information about the state of the computation and the WFG. If a computation terminates with a positive result, a cycle is detected. The advantages of this method are the avoidance of message duplication and the early detection, but the disadvantages are the complexity and the high storage requirement.
- There are various resolutions of deadlock detection in the distributed system, such as:
  - Deadlock prevention: avoiding the conditions that may lead to a deadlock, such as mutual exclusion, hold and wait, no preemption, and circular wait. This can be done by using appropriate resource allocation policies, such as ordering the resources, requesting all the resources at once, or releasing the resources before requesting new ones.
  - Deadlock avoidance: ensuring that the system always remains in a safe state, where there is at least one sequence of resource allocation that can satisfy all the processes. This can be done by using appropriate resource request protocols, such as the banker's algorithm, that check the availability and the demand of the resources before granting them.
  - Deadlock recovery: breaking the existing wait-for dependencies in the system WFG. This can be done by using appropriate recovery actions, such as aborting one or more deadlocked processes, preempting one or more resources from the deadlocked processes, or rolling back one or more deadlocked processes to a previous state.



### Centralized Deadlock Detection

- This is a technique used in distributed systems to handle deadlock detection.
- According to this technique, the system maintains one global wait-for graph in a single chosen site, which is named as deadlock-detection coordinator.
- The coordinator collects information about the local wait-for graphs of each site and constructs the global wait-for graph.
- The coordinator periodically runs a deadlock detection algorithm on the global wait-for graph and identifies any cycles that indicate deadlocks.
- The coordinator then informs the involved sites to abort one or more processes to break the deadlock.
- The advantages of this technique are simplicity and low communication overhead.
- The disadvantages of this technique are the single point of failure and the bottleneck of the coordinator.

: https://www.exploredatabase.com/2014/06/centralized-deadlock-detection-approach-in-distributed-database.html
: https://www.javatpoint.com/deadlock-detection-in-distributed-systems
: https://people.cs.rutgers.edu/~pxk/417/notes/deadlock.html



### Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set, and none of the processes can proceed or release the resources.
- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems.
- Deadlock detection in distributed systems entails addressing two basic issues: detection of existing deadlocks and resolution of detected deadlocks.
- Deadlock detection requires an examination of the status of the process-resource interactions for the presence of a cyclic wait.
- There are three approaches to detect deadlocks in distributed systems: centralized, hierarchical, and distributed.
- Centralized approach: A single node is designated as the deadlock detector and collects the local wait-for graphs from all the nodes and constructs a global wait-for graph to detect cycles.
- Hierarchical approach: The nodes are organized into a hierarchy of clusters and each cluster has a coordinator that collects the local wait-for graphs from the nodes in the cluster and constructs a cluster wait-for graph. The coordinators communicate with each other to detect cycles in the global wait-for graph.
- Distributed approach: There is no central coordinator or hierarchy of clusters. Each node communicates with other nodes to detect cycles in the global wait-for graph. There are two main techniques for distributed deadlock detection: edge chasing and diffusing computation.
- Edge chasing: A node initiates a probe message that contains the identity of the initiator and the sequence of nodes and resources visited by the probe. The probe message is forwarded along the wait-for edges until it either reaches the initiator (deadlock detected) or a node that is not waiting for any resource (deadlock not detected).
- Diffusing computation: A node initiates a computation that involves sending queries to the nodes that it is waiting for and receiving replies from them. The initiator maintains a counter that indicates the number of outstanding queries. When the counter reaches zero, the initiator either detects a deadlock (if it has not received a positive reply from any node) or terminates the computation (if it has received a positive reply from at least one node).
- To resolve the deadlock, one or more processes involved in the cycle have to be aborted and their resources have to be released. The selection of the victim process can be based on criteria such as priority, execution time, number of resources, etc.



### Path Pushing Algorithms

- Path pushing algorithms detect distributed deadlocks by maintaining an explicit global wait-for graph (WFG) at each site of the distributed system .
- The global WFG is constructed by sending the local WFG of each site to all its neighboring sites whenever a deadlock computation is performed .
- The neighboring sites are those that share a common resource or process in the WFG.
- The global WFG is updated whenever a new edge is added or deleted in the local WFG due to a request or a release of a resource.
- The global WFG contains all the edges of the local WFGs and may also contain some false edges that do not exist in the actual WFG of the system.
- A false edge is an edge that represents a dependency that has already been resolved but has not been reflected in the global WFG yet.
- A site can detect a deadlock by checking if there is a cycle in its global WFG that involves one of its local processes .
- If a cycle is detected, the site can initiate a recovery action by sending a message to the processes involved in the cycle.
- The advantages of path pushing algorithms are that they are simple, efficient, and scalable.
- The disadvantages of path pushing algorithms are that they require a lot of communication and storage overhead, and they may detect false deadlocks due to false edges.



### Edge Chasing Algorithms for Distributed Deadlock Detection

- Edge chasing algorithms are a class of distributed deadlock detection algorithms that use special messages called probes to trace the dependency graph of processes and resources in a distributed system.
- A probe is a triplet (i, j, k) that denotes that the deadlock detection is initiated by process P_i and the message is being sent by the home site of process P_j to the home site of process P_k.
- The probe message follows the edges of the dependency graph from the waiting processes to the blocking processes until either a cycle is detected or all the edges are traversed.
- A cycle is detected when a probe message returns to the initiator process or when a process receives a probe message with its own identifier in the triplet.
- The most common edge chasing algorithm is the Chandy-Misra-Haas algorithm, which works for the AND request model, where a process can request multiple resources simultaneously and wait for all of them to be granted.
- The Chandy-Misra-Haas algorithm works as follows:

  - Each process maintains a wait-for graph that contains the processes and resources it is waiting for and the processes and resources that are waiting for it.
  - When a process P_i initiates a deadlock detection, it sends a probe message (i, i, j) to the home site of each process P_j that it is waiting for.
  - When a process P_j receives a probe message (i, k, j), it checks if it is involved in a deadlock with P_i. If yes, it sends a reply message to P_i indicating the deadlock. If no, it forwards the probe message (i, j, l) to the home site of each process P_l that it is waiting for.
  - When a process P_i receives a reply message from P_j, it knows that there is a deadlock involving P_i and P_j and possibly other processes. It can then take appropriate actions to resolve the deadlock, such as aborting or preempting some processes or resources.



## Unit 4 - Agreement Protocols

- Agreement protocols are used in distributed systems to ensure that processes can reach a common goal or decision in the presence of failures  .
- Agreement protocols can be classified into different types based on the type of failure, the type of communication, and the type of agreement  .
- Some common types of agreement protocols are:
  - Consensus: All processes must agree on a single value proposed by one or more processes  .
  - Atomic commit: All processes must agree on whether to commit or abort a transaction that involves multiple processes  .
  - Leader election: All processes must agree on a single process that acts as the leader or coordinator of the system  .
  - Group membership: All processes must agree on the set of processes that belong to a group or a cluster  .
- Agreement protocols must satisfy some properties to ensure correctness and termination  :
  - Validity: The agreed value must be one of the proposed values.
  - Agreement: All correct processes must agree on the same value.
  - Termination: All correct processes must eventually decide on a value.
  - Integrity: The agreed value must be proposed by at most one process.
- Agreement protocols face some challenges in distributed systems, such as  :
  - Asynchronous communication: Processes may have different speeds and message delays may be unpredictable.
  - Partial failures: Some processes may fail or crash while others continue to operate normally.
  - Byzantine failures: Some processes may behave maliciously or arbitrarily and send conflicting or incorrect messages.
  - Network partitions: Some processes may be unable to communicate with others due to network failures or disruptions.
- Agreement protocols use various techniques to overcome these challenges, such as  :
  - Message passing: Processes exchange messages with each other to share information and coordinate actions.
  - Quorums: Processes form subsets of processes that have enough votes or authority to make decisions.
  - Fault tolerance: Processes use redundancy, replication, or recovery mechanisms to cope with failures.
  - Synchronization: Processes use clocks, timestamps, or logical ordering to ensure consistency and causality.



### Introduction for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by passing messages.
- Agreement protocols are algorithms that enable the processes in a distributed system to reach a common decision or a consistent state, despite the presence of failures or uncertainties.
- Agreement protocols are essential for ensuring the reliability, consistency, fault-tolerance, and security of distributed systems.
- Some examples of agreement problems are:
  - Consensus: All processes agree on a single value from a set of proposed values.
  - Atomic commit: All processes agree on whether to commit or abort a distributed transaction.
  - Byzantine agreement: All processes agree on a single value from a set of proposed values, even if some processes are faulty or malicious.
  - Leader election: All processes agree on which process is the leader or coordinator of the system.
  - Mutual exclusion: All processes agree on which process has exclusive access to a shared resource.
- Agreement protocols are challenging to design and implement because of the following issues:
  - Asynchrony: The processes and the communication channels in a distributed system may have arbitrary delays or unpredictable behaviors, making it hard to synchronize or order events.
  - Failures: The processes and the communication channels in a distributed system may fail or crash, making it hard to detect or recover from errors.
  - Uncertainty: The processes and the communication channels in a distributed system may have incomplete or inconsistent information, making it hard to verify or trust the messages.
- Agreement protocols are often based on the following techniques:
  - Message passing: The processes exchange messages to communicate and coordinate their actions.
  - Quorums: The processes form subsets of processes that have enough information or authority to make decisions.
  - Replication: The processes maintain copies of the same data or state to ensure consistency and availability.
  - Voting: The processes use majority or weighted votes to resolve conflicts or choose values.
  - Cryptography: The processes use encryption, signatures, or hashes to ensure the confidentiality, integrity, or authenticity of the messages.



### System models for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- A system model is a description of the properties and assumptions of a distributed system that are relevant for its design and analysis.
- System models can be classified into three types: network models, node models, and timing models .
- Network models capture the behavior and characteristics of the communication network, such as the topology, latency, bandwidth, reliability, and ordering of messages .
- Node models capture the behavior and characteristics of the nodes (computers or devices) that participate in the distributed system, such as the availability, failure modes, processing power, and memory capacity .
- Timing models capture the behavior and characteristics of the clocks and timers that are used to measure and synchronize time in the distributed system, such as the accuracy, drift, and synchronization of clocks .
- System models can also be classified into two categories: synchronous and asynchronous .
- A synchronous system model assumes that there are known bounds on the network latency, node processing speed, and clock drift . This simplifies the design and analysis of distributed algorithms, but it is often unrealistic in practice .
- An asynchronous system model assumes that there are no known bounds on the network latency, node processing speed, and clock drift . This reflects the reality of most distributed systems, but it makes the design and analysis of distributed algorithms more challenging .
- A partially synchronous system model is a compromise between the synchronous and asynchronous models, where some bounds are known or hold eventually, but not always . This captures the dynamic and unpredictable nature of distributed systems, but it also allows for some guarantees and optimizations .
- Consensus system models are a special type of system models that describe the assumptions and requirements for solving the consensus problem in distributed systems .
- The consensus problem is the problem of reaching agreement among a set of nodes on a common value, despite the presence of failures and uncertainties .
- The consensus system model specifies the number and type of nodes, the number and type of failures, the type and order of messages, and the type and accuracy of clocks .
- Popular consensus algorithms, such as Paxos and Raft, assume partially synchronous and crash-recovery system models, where nodes can fail by crashing and restarting, messages can be delayed or lost, and clocks can drift or be inaccurate .
- Other consensus algorithms, such as Byzantine fault tolerance and blockchain, assume asynchronous and Byzantine system models, where nodes can fail by behaving arbitrarily, messages can be forged or tampered, and clocks can be manipulated or inconsistent .

: https://inelpandzic.com/articles/system-models-distributed-systems/
: https://www.uio.no/studier/emner/matnat/ifi/INF5040/h11/lectures/SystemModels.pdf
: https://rashmininayanathara.medium.com/system-models-for-distributed-and-cloud-computing-c1d994970682
: https://knowledgeburrow.com/what-are-the-different-system-models-of-distributed-system/
: https://www.baeldung.com/cs/distributed-systems-guide
: https://www.splunk.com/en_us/data-insider/what-are-distributed-systems.html



### Classification of Agreement Problem

An agreement problem is a problem in which a set of processes in a distributed system have to agree on some value or decision, despite the possibility of failures or malicious behavior. Agreement problems are fundamental to the design of fault-tolerant distributed systems, as they provide a way to achieve consistency and coordination among the processes.

There are different types of agreement problems, depending on the assumptions and requirements of the system. Some of the well-known agreement problems are:

- **Byzantine agreement problem**: A single value, which is to be agreed on, is initialized by an arbitrary process and all non-faulty processes have to agree on that value. The processes may be subject to Byzantine failures, which means they can behave arbitrarily or maliciously, such as sending conflicting or incorrect messages. The goal is to ensure that all non-faulty processes agree on the same value, and that value is the initial value of some non-faulty process.   

- **Consensus problem**: A generalization of the Byzantine agreement problem, where each process can propose a value and all non-faulty processes have to agree on a common value. The value agreed on must be one of the proposed values. The processes may be subject to crash failures, which means they can stop executing at any point, but they cannot behave maliciously. The goal is to ensure that all non-faulty processes agree on the same value, and that value is one of the proposed values.   

- **Interactive consistency problem**: A variation of the Byzantine agreement problem, where each process has an initial value and all non-faulty processes have to agree on a vector of values, one for each process. The vector agreed on must satisfy two properties: (1) the value for each process is the initial value of that process, if it is non-faulty, or any value, if it is faulty; and (2) all non-faulty processes agree on the same vector. The processes may be subject to Byzantine failures, as in the Byzantine agreement problem. The goal is to ensure that all non-faulty processes agree on the same vector, and that vector satisfies the two properties.  

These agreement problems are related to each other, and can be solved using similar techniques, such as message passing, voting, or cryptography. However, they also have different limitations and impossibility results, depending on the number of processes, the number of faulty processes, the type of failures, the type of communication, and the synchrony of the system. For example, the Byzantine agreement problem is impossible to solve if more than one-third of the processes are faulty, or if the communication is asynchronous. The consensus problem is impossible to solve if even one process can fail, or if the communication is asynchronous. The interactive consistency problem is impossible to solve if more than half of the processes are faulty, or if the communication is asynchronous.  

Therefore, the classification of agreement problems helps to understand the trade-offs and challenges involved in designing fault-tolerant distributed systems, and to choose the appropriate problem and solution for a given system.



### Byzantine agreement problem

- The Byzantine agreement problem is a fundamental problem in fault tolerant distributed computing that requires a set of parties in a distributed environment to agree on a value even if some of the parties are corrupted.
- The problem was first defined by Lamport and inspired by the scenario of several divisions of the Byzantine army camped outside an enemy city, each division commanded by its own general. The generals can communicate with one another only by messenger. After observing the enemy, they must decide upon a common plan of action.
- The problem is challenging because some of the generals may be traitors who try to prevent the loyal generals from reaching agreement. The traitors may send conflicting messages to different generals, or lie about their own observations or preferences.
- A solution to the Byzantine agreement problem is a protocol that ensures that all loyal generals agree on the same value, and that the value is the initial value of some loyal general. The protocol must be resilient to arbitrary failures and malicious behaviors of the corrupted parties.
- The Byzantine agreement problem is also known as the interactive consistency problem, the source congruency problem, the error avalanche problem, or the Byzantine failure problem. It has applications in distributed systems, cryptography, consensus algorithms, and blockchain technology .



### Consensus problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- The consensus problem is the problem of getting a set of nodes in a distributed system to agree on something - it might be a value, a course of action or a decision.
- Achieving consensus allows a distributed system to act as a single entity, with every individual node aware of and in agreement with the actions of the whole of the network.
- Consensus is a general agreement on a decision made by the majority of those involved.
- Consensus is needed in a distributed system to ensure overall system reliability on top of unreliable system components.
- Consensus is also needed to coordinate actions, synchronize state, and detect failures among the nodes in a distributed system.
- Some examples of consensus problems in distributed systems are:
  - Leader election: choosing a node to act as the coordinator or the primary among a group of nodes.
  - Atomic commit: ensuring that a transaction is either committed or aborted by all the nodes involved.
  - Distributed lock: granting exclusive access to a shared resource among competing nodes.
  - Configuration management: maintaining a consistent view of the system parameters and state among the nodes.
- There are many ways in which processes in a distributed system can reach a consensus. However, there is usually a constant struggle between security and performance.
- The more we want our algorithm to be secure against ways in which failure can happen, the less performant it tends to become.
- Some of the factors that affect the security and performance of consensus algorithms are:
  - The number of nodes involved.
  - The communication model (synchronous or asynchronous).
  - The failure model (crash, omission, or Byzantine).
  - The availability and consistency guarantees.
- Some of the common consensus algorithms in distributed systems are:
  - Two-phase commit (2PC): a simple and efficient algorithm that requires two rounds of communication between a coordinator and the participants.
  - Three-phase commit (3PC): an extension of 2PC that adds a pre-commit phase to avoid blocking in case of coordinator failure.
  - Paxos: a family of algorithms that use a quorum-based approach to tolerate crash failures and network partitions.
  - Raft: a simplified version of Paxos that uses a leader-based approach to ensure safety and liveness.
  - Byzantine fault tolerance (BFT): a class of algorithms that can tolerate arbitrary failures and malicious behavior of some nodes.



### Interactive Consistency Problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- Interactive consistency is the problem in which n distinct nodes, each having its own private value, where up to t may be Byzantine, run an algorithm that allows all non-faulty nodes to infer the values of each other node  .
- Byzantine nodes are nodes that can behave arbitrarily, such as sending incorrect or conflicting messages, or remaining silent .
- Interactive consistency is a generalization of distributed consensus, which is the problem of reaching agreement on a single value among n nodes, where up to t may be Byzantine .
- Interactive consistency is also known as Byzantine generals problem, which is a metaphor for the situation where a group of generals must coordinate an attack or retreat, but some of them may be traitors who try to sabotage the plan .
- Interactive consistency is relevant to critical applications that rely on the combination of the opinions of multiple peers to provide a service, such as fault-tolerant distributed systems, blockchain systems, or voting systems  .
- Interactive consistency is a hard problem to solve, especially in asynchronous or partially synchronous systems, where there is no global clock or bounded message delays  .
- Interactive consistency has some fundamental limitations, such as the impossibility of achieving it with less than 3t + 1 nodes, or the impossibility of achieving it deterministically in asynchronous systems  .
- Interactive consistency can be achieved by using various algorithms, such as the original oral messages algorithm by Pease, Shostak and Lamport, which requires multiple rounds of message exchanges and exponential message complexity , or the more efficient algorithms based on broadcast and randomized Byzantine consensus, which require only a single synchronization barrier and polynomial message complexity .



### Solution to Byzantine Agreement problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- The Byzantine agreement problem is a fundamental problem in distributed systems, where a set of processors need to agree on a common value, even if some of them are faulty or malicious.
- The problem is named after the Byzantine Generals Problem, which is a metaphor for the situation where several generals of the Byzantine army need to coordinate their attack or retreat plan, but some of them may be traitors who send conflicting messages  .
- A solution to the Byzantine agreement problem requires that the following properties are satisfied :
  - **Termination**: Every non-faulty processor eventually decides on a value.
  - **Agreement**: All non-faulty processors decide on the same value.
  - **Validity**: If all non-faulty processors start with the same value, then they decide on that value.
- A necessary condition for solving the Byzantine agreement problem is that the number of faulty processors is less than one-third of the total number of processors .
- A possible solution to the Byzantine agreement problem is the **EAC protocol** proposed by El-Attar and Chen, which works as follows:
  - Each processor broadcasts its initial value to all other processors.
  - Each processor collects the values received from all other processors and forms a vector of values, sorted in ascending order.
  - Each processor computes the median of the vector and broadcasts it to all other processors.
  - Each processor collects the medians received from all other processors and forms another vector of medians, sorted in ascending order.
  - Each processor computes the median of the second vector and decides on that value.
- The EAC protocol satisfies the termination, agreement and validity properties, and can tolerate up to (n-1)/3 faulty processors, where n is the total number of processors.
- The EAC protocol has a message complexity of O(n^2) and a time complexity of O(1), where n is the total number of processors.



### Application of Agreement problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- Agreement problem is a fundamental problem in distributed computing and multi-agent systems, where a set of processes need to coordinate and reach a common decision or value .
- Agreement problem can be classified into different types, such as consensus, atomic commitment, atomic broadcast, and group membership.
- Consensus is the problem of getting all the processes to agree on a single value, which can be proposed by any process . Consensus is useful for implementing fault-tolerant services, such as replicated state machines, leader election, and distributed transactions.
- Atomic commitment is the problem of getting all the processes to agree on whether to commit or abort a transaction, which involves multiple resources . Atomic commitment is useful for ensuring the atomicity and consistency properties of distributed transactions .
- Atomic broadcast is the problem of getting all the processes to deliver the same set of messages in the same order . Atomic broadcast is useful for implementing reliable and consistent communication channels, such as message queues, publish-subscribe systems, and distributed logs .
- Group membership is the problem of getting all the processes to agree on the current set of active processes in the system . Group membership is useful for managing the dynamic changes of the system, such as failures, recoveries, and joins .
- Agreement problem is challenging to solve in the presence of failures, such as crash, omission, or Byzantine failures   . Different types of failures require different assumptions and algorithms to achieve agreement   .
- Agreement protocols are the algorithms that aim to solve the agreement problem under various assumptions and conditions . Some examples of agreement protocols are Paxos, Raft, Two-Phase Commit, Three-Phase Commit, and Byzantine Agreement  .



### Atomic Commit in Distributed Database System

- An atomic commit is an operation that applies a set of distinct changes as a single operation. If the changes are applied, then the atomic commit is said to have succeeded. If the changes are not applied, then the atomic commit is said to have failed or aborted.
- In distributed database systems, the primary need for commit protocols is to maintain the atomicity of distributed transactions. A distributed transaction is a transaction that accesses data stored in multiple sites of a distributed system .
- Atomic commitment issue is of prime importance in the distributed system and the issue becomes more necessary to deal with if some of the sites participating in the execution of the transaction commitment fail .
- An atomic commit protocol is a protocol that coordinates the distinct operations of a distributed transaction and then commits or aborts the transaction as needed. An atomic commit protocol guarantees, in spite of possible failures, that either all the sites agree to commit the transaction, or all the sites agree to abort the transaction .
- There are two main types of atomic commit protocols: blocking and non-blocking. Blocking protocols require that some sites block or wait until the final decision (commit or abort) is reached, while non-blocking protocols allow some sites to proceed without waiting for the final decision .
- Blocking protocols are simpler and faster than non-blocking protocols, but they are less resilient to failures. Non-blocking protocols are more complex and slower than blocking protocols, but they are more resilient to failures .
- Some examples of blocking protocols are two-phase commit (2PC), three-phase commit (3PC), and presumed commit (PC). Some examples of non-blocking protocols are presumed abort (PA), presumed nothing (PN), and failure-aware atomic commit (FLAC)  .



## Unit 5 - Distributed Resource Management

- Distributed resource management (DRM) is an evolving discipline that aims to enable distributed enterprise systems to operate effectively in production.
- DRM involves a set of software, hardware, network tools, procedures and policies for managing various types of resources in a distributed system, such as computing, storage, communication, energy, and data.
- DRM can be applied to different domains and scenarios, such as cloud computing, grid computing, edge computing, Internet of Things, smart grid, and distributed energy resources.
- DRM can provide various benefits to the distributed system, such as:
  - Improving performance, scalability, availability, and reliability of the system.
  - Optimizing resource utilization, allocation, and scheduling.
  - Enhancing system security, privacy, and resilience.
  - Supporting dynamic adaptation and reconfiguration of the system.
  - Enabling interoperability and coordination among heterogeneous and autonomous resources.
- DRM faces various challenges and issues, such as:
  - Dealing with resource heterogeneity, diversity, and complexity.
  - Handling resource uncertainty, variability, and volatility.
  - Balancing resource supply and demand.
  - Resolving resource conflicts and dependencies.
  - Achieving resource efficiency, fairness, and quality of service.
  - Coping with resource failures and faults.
  - Ensuring resource compliance and accountability.
- DRM can be implemented using different approaches and techniques, such as:
  - Centralized, decentralized, or hybrid resource management architectures.
  - Resource discovery, monitoring, and modeling methods.
  - Resource allocation, scheduling, and negotiation algorithms.
  - Resource coordination, collaboration, and consensus protocols.
  - Resource control, feedback, and adaptation mechanisms.
  - Resource security, privacy, and trust solutions.



### Issues in Distributed File Systems

Distributed file systems (DFS) are systems that allow users to access and manipulate files stored on remote servers as if they were local. DFS provide advantages such as fault tolerance, scalability, and performance. However, they also face several challenges and issues in their design and implementation, such as:

- **Naming and transparency**: How to assign unique and meaningful names to files and directories in a distributed environment, and how to hide the details of the physical location and replication of files from the users.
- **Consistency and replication**: How to ensure that multiple copies of the same file are kept consistent and up-to-date, and how to handle concurrent updates and conflicts among different users or processes.
- **Security and access control**: How to protect the confidentiality, integrity, and availability of files and directories from unauthorized or malicious access, and how to enforce different levels of permissions and privileges for different users or groups.
- **Fault tolerance and availability**: How to cope with partial failures such as network partitions, node crashes, or disk failures, and how to ensure that files and directories are always accessible and recoverable.
- **Performance and scalability**: How to optimize the throughput, latency, and bandwidth of file operations, and how to handle the increasing demand for storage and processing resources in a distributed environment.
- **Incentive and auditing mechanisms**: How to motivate and reward the participants of a distributed file system, especially in peer-to-peer (P2P) settings, and how to verify and monitor the behavior and performance of the system and its components.



### Mechanism for building distributed file systems

- A distributed file system (DFS) is a file system that is distributed on multiple file servers or locations, allowing programs to access or store isolated files as they do with the local ones.
- A DFS may use different mechanisms to build a coherent and consistent file system that can handle concurrency, replication, caching, fault tolerance, security, and scalability issues.
- Some of the common mechanisms for building DFS are:

  - **Use of file models**: A file model defines the structure and modifiability of a file. A file can be unstructured (a sequence of bytes) or structured (a sequence of records or objects) depending on the application. A file can also be immutable (read-only) or mutable (read-write) depending on the access mode.
  - **Use of file accessing models**: A file accessing model defines how a client can access a file on a server. There are three main models: upload/download, remote access, and remote service. In upload/download, the client copies the entire file from the server, modifies it locally, and uploads it back to the server. In remote access, the client sends requests to read or write specific parts of the file to the server. In remote service, the client sends requests to perform high-level operations on the file, such as searching or sorting, to the server.
  - **Use of file caching**: File caching is a technique to improve the performance and reduce the network traffic of a DFS. It involves storing copies of frequently accessed files or parts of files on the client side or intermediate nodes. File caching can be done at different levels, such as block level, file level, or subfile level. File caching also requires consistency mechanisms to ensure that the cached copies are up-to-date with the original files on the server.
  - **Use of file replication**: File replication is a technique to improve the availability and reliability of a DFS. It involves storing multiple copies of a file on different file servers. File replication can be done at different granularities, such as whole file, subfile, or block. File replication also requires synchronization mechanisms to ensure that the replicated copies are consistent with each other.
  - **Use of file naming**: File naming is a technique to identify and locate files in a DFS. It involves assigning names to files and mapping them to physical locations. File naming can be done using different schemes, such as flat naming, hierarchical naming, or attribute-based naming. File naming also requires resolution mechanisms to translate names to locations and handle name conflicts.
  - **Use of file mounting**: File mounting is a technique to integrate different file systems or namespaces into a single hierarchical namespace. It involves binding a file system or a directory from one server to a mount point on another server. File mounting can be done using different methods, such as static mounting, dynamic mounting, or automatic mounting. File mounting also requires authentication and authorization mechanisms to control the access to the mounted files.
  - **Use of file migration**: File migration is a technique to move files from one server to another in a DFS. It involves transferring the ownership and the data of a file to a new location. File migration can be done for different purposes, such as load balancing, data backup, or data locality. File migration also requires update and redirection mechanisms to ensure that the clients can access the migrated files without interruption.

: https://www.geeksforgeeks.org/mechanism-for-building-distributed-file-system/
: https://www.cs.nuim.ie/~dkelly/CS402-06/Distributed%20File%20Systems.htm
: https://www.geeksforgeeks.org/what-is-dfsdistributed-file-system/



### Design issues in Distributed Shared Memory

Distributed Shared Memory (DSM) is a mechanism that allows multiple processes on different nodes to share a common logical address space and access data transparently. DSM can simplify the programming of distributed systems by hiding the details of inter-process communication. However, DSM also introduces several design issues that affect its performance, scalability, and correctness. Some of the main design issues in DSM are:

- **Granularity**: Granularity refers to the size of the unit of sharing and the unit of coherence in DSM. A smaller granularity (such as a byte or a word) can reduce the amount of false sharing and improve the locality of access, but it can also increase the overhead of coherence maintenance and communication. A larger granularity (such as a page or a segment) can reduce the overhead of coherence and communication, but it can also increase the amount of false sharing and waste bandwidth and memory. Therefore, choosing an appropriate granularity is a trade-off between these factors.

- **Structure**: Structure refers to the organization of the shared data in the logical address space and the mapping of the shared data to the physical memory of the nodes. The structure of DSM can be flat, hierarchical, or object-based. A flat structure treats the shared data as a single linear array and maps it to the nodes using a static or dynamic hashing function. A hierarchical structure divides the shared data into multiple regions and maps each region to a node using a directory or a home-based scheme. An object-based structure treats the shared data as a collection of objects and maps each object to a node using a location service or a naming service. The structure of DSM affects the ease of programming, the locality of access, and the scalability of the system.

- **Coherence semantics**: Coherence semantics define the consistency model of DSM, which specifies the order and visibility of the updates to the shared data. Coherence semantics can be strict, relaxed, or weak. A strict coherence semantics (such as sequential consistency or cache coherence) guarantees that all processes see the same order and value of the updates to the shared data. A relaxed coherence semantics (such as release consistency or entry consistency) allows some reordering and delay of the updates to the shared data, but requires the programmer to use synchronization primitives to ensure correctness. A weak coherence semantics (such as eventual consistency or lazy consistency) does not guarantee any order or visibility of the updates to the shared data, but relies on the application logic to tolerate inconsistency. The coherence semantics of DSM affects the performance, scalability, and correctness of the system.

- **Coherence protocols**: Coherence protocols implement the coherence semantics of DSM by maintaining the consistency of the shared data across the nodes. Coherence protocols can be classified into two categories: replication-based and migration-based. A replication-based coherence protocol allows multiple copies of the same data to exist on different nodes, but requires a mechanism to invalidate or update the copies when the data is modified. A migration-based coherence protocol allows only one copy of the data to exist on one node at a time, but requires a mechanism to transfer the ownership of the data when the data is accessed. Coherence protocols can also be classified into two types: centralized and distributed. A centralized coherence protocol uses a single node or a group of nodes to coordinate the coherence actions, such as invalidation, update, or transfer. A distributed coherence protocol uses a peer-to-peer communication among the nodes to coordinate the coherence actions, such as request, reply, or notification. The coherence protocol of DSM affects the performance, scalability, and fault-tolerance of the system.

- **Scalability**: Scalability refers to the ability of DSM to handle a large number of nodes, a large amount of shared data, and a high degree of concurrency. Scalability depends on several factors, such as the granularity, the structure, the coherence semantics, and the coherence protocol of DSM. To achieve scalability, DSM should minimize the overhead of coherence and communication, maximize the locality of access, and balance the load among the nodes. Scalability can be measured by various metrics, such as speedup, efficiency, throughput, or latency.

- **Heterogeneity**: Heterogeneity refers to the diversity of the nodes in DSM, such as the hardware architecture, the operating system, the network interface, or the communication protocol. Heterogeneity can pose several challenges for DSM, such as the compatibility, the interoperability, the portability, and the performance of the system. To cope with heterogeneity, DSM should use a common interface, a common protocol, a common format, and a common mechanism for the nodes. Heterogeneity can also be exploited by DSM, such as using the best node for a



### Algorithm for Implementation of Distributed Shared Memory

Distributed Shared Memory (DSM) is a technique that allows multiple processes on different nodes of a distributed system to share a common virtual address space and access the same data objects. DSM can simplify the programming of distributed applications by providing a uniform view of memory and hiding the details of data distribution and communication.

There are different algorithms for implementing DSM, each with its own advantages and disadvantages. Some of the main algorithms are:

- **Central Server Algorithm**: In this algorithm, a central server maintains all the shared data and services the read and write requests from other nodes. The central server can use a page-based or an object-based approach to manage the shared data. The advantage of this algorithm is that it is simple and ensures data consistency. The disadvantage is that it introduces a single point of failure and a performance bottleneck, as all the requests have to go through the central server.   

- **Migration Algorithm**: In this algorithm, the shared data is initially stored at the central server, but it can migrate to other nodes upon request. When a node wants to read or write a data item, it requests the central server for the location of that item. If the item is not at the central server, the server forwards the request to the node that has the item. The node that has the item can either send a copy of the item to the requester, or transfer the ownership of the item to the requester. The advantage of this algorithm is that it reduces the network traffic and the load on the central server by moving the data closer to the nodes that need it. The disadvantage is that it may cause data inconsistency and coherence problems, as multiple copies of the same data item may exist in the system.  

- **Replication Algorithm**: In this algorithm, the shared data is replicated on multiple nodes, and each node can access the local copy of the data. The replication can be done eagerly or lazily, depending on whether the updates are propagated to all the replicas immediately or on demand. The advantage of this algorithm is that it improves the availability and fault-tolerance of the data, as well as the performance of read operations. The disadvantage is that it increases the storage and communication overhead, and requires a complex mechanism to ensure data consistency and coherence among the replicas.  

- **Invalidation Algorithm**: In this algorithm, the shared data is initially stored at the central server, but it can be cached on other nodes upon request. When a node wants to read a data item, it checks its local cache first. If the item is not in the cache, it requests the central server for the item and caches it locally. When a node wants to write a data item, it sends an invalidation message to the central server and all the other nodes that have cached the item, informing them that their copies are invalid. The central server updates its copy of the item and sends an acknowledgement to the writer. The advantage of this algorithm is that it reduces the network traffic and the load on the central server by allowing the nodes to access the cached data locally. The disadvantage is that it may cause data inconsistency and coherence problems, as the cached copies may become stale or invalid.



## Unit 6 - Failure Recovery in Distributed Systems

- Failure recovery is the process of restoring a distributed system to a consistent and correct state after a failure occurs.
- Failure recovery is essential for fault tolerance, which is the ability of a system to continue functioning despite faults or errors.
- There are different types of failures that can affect a distributed system, such as:
  - Node failures: when a site or a process in the system stops working or crashes.
  - Communication failures: when a message between two sites or processes is lost, delayed, corrupted, or duplicated.
  - Network failures: when a link or a network segment in the system becomes unavailable or partitioned.
  - Media failures: when a secondary storage device in the system fails or gets damaged.
  - Byzantine failures: when a site or a process in the system behaves maliciously or arbitrarily, violating the system assumptions or protocols.
- There are different techniques for failure recovery in distributed systems, such as:
  - Checkpointing: when a site or a process periodically saves its state to a stable storage, which can resist major disasters. In case of a failure, the site or the process can resume from the last saved checkpoint.
  - Logging: when a site or a process records its actions or events to a stable storage, which can be used to replay or undo the actions or events in case of a failure.
  - Replication: when a site or a process maintains multiple copies of its state or data across different sites or processes in the system, which can provide redundancy and availability in case of a failure.
  - Consensus: when a group of sites or processes in the system agree on a common value or decision, which can ensure consistency and correctness in case of a failure.
  - Fault detection: when a site or a process monitors the status or the behavior of other sites or processes in the system, which can help to identify and isolate the faulty ones.
  - Fault masking: when a site or a process hides or compensates the effects of a failure from the rest of the system, which can prevent the failure from propagating or affecting the system functionality.



### Concepts in Backward and Forward Recovery

- Backward recovery and forward recovery are two techniques to restore the system to a consistent state after a failure in a distributed system.
- Backward recovery involves rolling back the system to a previous error-free state by using checkpoints and logs. Forward recovery involves correcting the errors and continuing the execution from the current state.
- The main difference between backward and forward recovery is that backward recovery discards the work done after the error, while forward recovery preserves the work done before and after the error.
- Backward recovery is more general and independent of the nature of faults, but it may incur more overhead and waste of resources. Forward recovery is more efficient and avoids unnecessary rollbacks, but it requires accurate assessment and removal of errors.
- Some examples of backward recovery protocols are checkpointing, message logging, and rollback-dependency tracking. Some examples of forward recovery techniques are redundancy, error correction codes, and exception handling.



### Recovery in Concurrent Systems

- Recovery in concurrent systems is the process of restoring the system to a consistent state after a failure, while preserving the effects of concurrent transactions that did not cause the failure.
- Recovery in concurrent systems is challenging because of the interleaving of operations from different transactions, which may affect the same data items or resources.
- Recovery in concurrent systems requires coordination between the concurrency control and the recovery mechanisms, to ensure that the system maintains the ACID properties of transactions (atomicity, consistency, isolation, and durability).
- Recovery in concurrent systems can be classified into two main categories: backward recovery and forward recovery.
- Backward recovery is the process of undoing the effects of failed or aborted transactions, by restoring the system to a previous consistent state. Backward recovery can be implemented using techniques such as:
  - Logging: Recording the changes made by transactions in a persistent log, which can be used to undo or redo the operations in case of a failure.
  - Checkpointing: Periodically saving the state of the system in a stable storage, which can be used as a recovery point in case of a failure.
  - Shadow paging: Maintaining a copy of the database pages in a shadow file, which can be used to replace the original pages in case of a failure.
- Forward recovery is the process of redoing the effects of committed transactions, by applying the changes to the system after a failure. Forward recovery can be implemented using techniques such as:
  - Deferred updates: Delaying the updates to the database until the transaction commits, and recording them in a log, which can be used to redo the operations in case of a failure.
  - Replication: Maintaining multiple copies of the database on different nodes, which can be used to recover from a failure of one or more nodes.
  - Compensation: Executing compensating transactions that reverse the effects of failed or aborted transactions, without affecting the committed transactions.



### Obtaining consistent Checkpoints for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Failure recovery in distributed systems is the process of restoring the system to a consistent and correct state after a failure occurs.
- A failure in a distributed system can be caused by various factors, such as hardware faults, software bugs, network errors, malicious attacks, or natural disasters.
- A failure can affect one or more components of the system, such as nodes, processes, messages, or data.
- A failure can have different consequences, such as data loss, data corruption, performance degradation, or system unavailability.
- To recover from a failure, the system needs to detect the failure, identify the cause and the scope of the failure, and restore the system to a consistent and correct state.
- A consistent state is a state where all the components of the system agree on the same view of the system and its data.
- A correct state is a state where the system and its data satisfy the specifications and the invariants of the system.
- One of the common techniques for failure recovery in distributed systems is checkpointing.
- Checkpointing is the process of periodically saving the state of the system or its components to a stable storage, such as a disk or a cloud service.
- Checkpointing can be done at different levels, such as process level, node level, or system level.
- Checkpointing can be done in different ways, such as synchronous, asynchronous, coordinated, or uncoordinated.
- Checkpointing can be used to recover the system or its components to a previous consistent and correct state in case of a failure.
- Checkpointing can also be used to improve the performance and availability of the system by reducing the amount of work that needs to be redone after a failure.
- Checkpointing has some challenges and trade-offs, such as the overhead of saving and restoring the state, the frequency and granularity of checkpointing, the consistency and correctness of the checkpoints, and the coordination and synchronization of the checkpoints.
- To obtain consistent checkpoints, the system needs to ensure that the checkpoints of different components are compatible and reflect the same global state of the system.
- To obtain consistent checkpoints, the system can use different algorithms, such as the Chandy-Lamport algorithm, the Lai-Yang algorithm, or the Manivannan-Singhal algorithm.
- These algorithms use different techniques, such as message logging, vector clocks, or dependency graphs, to capture the causal dependencies and the logical order of the events in the system.
- These algorithms can also handle different types of failures, such as crash failures, omission failures, or Byzantine failures.
- These algorithms can also deal with different types of communication, such as reliable or unreliable, FIFO or non-FIFO, or multicast or broadcast.
- These algorithms have different properties, such as the number of checkpoints, the number of messages, the storage space, the recovery time, and the fault tolerance.



### Recovery in Distributed Database Systems

- Recovery in distributed database systems is the process of restoring the database to a consistent and correct state after a failure or a transaction abort.
- Recovery in distributed database systems is more complex than in centralized database systems because of the following reasons:
  - Failures can occur at multiple sites or communication links, affecting different parts of a distributed transaction.
  - A distributed transaction may involve multiple sites that have different recovery protocols and failure modes.
  - A distributed transaction may commit at some sites and abort at others, leading to inconsistency and partial results.
  - A distributed transaction may depend on other transactions that are executed at different sites and have different commit or abort statuses.
- Recovery in distributed database systems aims to achieve the following objectives:
  - Atomicity: A distributed transaction should either commit or abort as a whole, regardless of the failures or aborts of its subtransactions at different sites.
  - Durability: The effects of a committed distributed transaction should be permanent and survive any subsequent failures.
  - Consistency: The database should be in a consistent state after the recovery, meaning that all integrity constraints and business rules are satisfied.
  - Availability: The database should be accessible and operational as much as possible, even in the presence of failures or recovery actions.
- Recovery in distributed database systems can be classified into two types:
  - Local recovery: The recovery of a single site or a single subtransaction, without considering the effects on other sites or subtransactions.
  - Global recovery: The recovery of a distributed transaction as a whole, considering the effects on all sites and subtransactions involved.
- Local recovery can be further divided into two types:
  - Undo recovery: The recovery that restores the database to its state before the execution of a faulty or aborted subtransaction, by undoing the changes made by the subtransaction.
  - Redo recovery: The recovery that restores the database to its state after the execution of a successful subtransaction, by redoing the changes made by the subtransaction.
- Global recovery can be further divided into two types:
  - Backward recovery: The recovery that aborts a distributed transaction and undoes the effects of its subtransactions at all sites, by using undo recovery at each site.
  - Forward recovery: The recovery that commits a distributed transaction and redoes the effects of its subtransactions at all sites, by using redo recovery at each site.
- Recovery in distributed database systems requires the following mechanisms:
  - Logging: The recording of the changes made by subtransactions and the commit or abort statuses of subtransactions and distributed transactions in persistent storage, such as disk or tape.
  - Checkpointing: The periodic saving of the database state and the log records to persistent storage, to reduce the amount of recovery work needed after a failure.
  - Commit protocols: The protocols that coordinate the commit or abort decision of a distributed transaction among all sites involved, such as the two-phase commit protocol or the three-phase commit protocol.
  - Recovery protocols: The protocols that coordinate the recovery actions of a distributed transaction among all sites involved, such as the backward recovery protocol or the forward recovery protocol.



## Unit 7 - Fault Tolerance

- Fault tolerance is the ability of a system to continue functioning correctly in the presence of failures.
- Fault tolerance can be achieved by using techniques such as redundancy, replication, recovery, and reconfiguration.
- Redundancy is the provision of extra components or resources that can take over the function of a failed component or resource.
- Replication is the creation of multiple copies of data or services that can be accessed in case of a failure.
- Recovery is the process of restoring a system to a consistent and correct state after a failure.
- Reconfiguration is the process of changing the structure or parameters of a system to adapt to a failure or a changing environment.
- Fault tolerance can be classified into two types: passive and active.
- Passive fault tolerance relies on redundancy to mask failures without requiring any intervention or detection.
- Active fault tolerance relies on detection and recovery to handle failures by activating redundant components or resources.
- Fault tolerance can be applied at different levels of a system, such as hardware, software, network, and application.
- Fault tolerance can improve the reliability, availability, and safety of a system, but it also introduces challenges such as complexity, cost, performance, and consistency.



### Issues in Fault Tolerance for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Fault tolerance is the ability of a system to continue functioning correctly in the presence of failures.
- Fault tolerance is important for distributed systems because they consist of multiple components that may be subject to failures, such as hardware, software, network, or human errors .
- Fault tolerance can be achieved by using various mechanisms, such as redundancy, replication, checkpointing, recovery, consensus, and fault detection .
- Some of the issues and challenges in fault tolerance for distributed systems are:
  - How to design and implement fault-tolerant algorithms that can cope with different types of failures, such as crash, omission, timing, byzantine, or self-stabilizing failures.
  - How to ensure the consistency and availability of data and services in the presence of failures, especially in large-scale and dynamic systems, such as cloud, grid, or peer-to-peer systems.
  - How to balance the trade-offs between performance, cost, and reliability in fault-tolerant systems, such as choosing the optimal level of redundancy, replication, or checkpointing.
  - How to evaluate and measure the fault tolerance of distributed systems, such as using metrics, models, or benchmarks .



### Commit Protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Commit protocols are algorithms that ensure the atomicity of distributed transactions, i.e., all the sites involved in a transaction either commit or abort it unanimously, even in the presence of failures  .
- Atomicity is one of the ACID properties of transactions, which guarantees that either all the changes made by a transaction are visible to other transactions, or none of them are.
- There are different types of commit protocols, such as one-phase commit, two-phase commit, and three-phase commit, which differ in the number of phases and messages exchanged between the coordinator and the participants of a transaction   .
- One-phase commit protocol is the simplest and fastest commit protocol, but it is not fault-tolerant. It involves a single message from the coordinator to the participants, instructing them to either commit or abort the transaction.
- Two-phase commit protocol is the most widely used commit protocol, which ensures atomicity and durability of distributed transactions, but it is blocking, i.e., it may cause the participants to wait indefinitely for the coordinator's decision in case of failures  . It involves two phases: a voting phase and a decision phase  .
  - In the voting phase, the coordinator sends a prepare message to all the participants, asking them to vote either yes or no for committing the transaction. The participants reply with their votes after writing a prepare log record  .
  - In the decision phase, the coordinator collects the votes from all the participants and decides whether to commit or abort the transaction based on the majority rule. The coordinator then sends a commit or abort message to all the participants, and writes a commit or abort log record. The participants follow the coordinator's decision and write a commit or abort log record as well  .
- Three-phase commit protocol is an extension of the two-phase commit protocol, which aims to overcome the blocking problem by introducing an extra phase called pre-commit . It involves three phases: a prepare phase, a pre-commit phase, and a commit/abort phase.
  - In the prepare phase, the steps are the same as in the two-phase commit protocol.
  - In the pre-commit phase, the coordinator sends an enter prepared state message to all the participants who voted yes, and waits for their acknowledgments. The participants enter the prepared state and reply with an ok message.
  - In the commit/abort phase, the coordinator decides whether to commit or abort the transaction based on the acknowledgments received. The coordinator then sends a commit or abort message to all the participants, and writes a commit or abort log record. The participants follow the coordinator's decision and write a commit or abort log record as well.
- Three-phase commit protocol is non-blocking, i.e., it allows the participants to make a decision independently of the coordinator in case of failures, but it requires more messages and delays than the two-phase commit protocol .



### Voting protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Voting protocols are a type of consensus protocols that allow a set of distributed nodes to agree on a common value or decision.
- Voting protocols are useful for achieving fault tolerance in distributed systems, as they can tolerate the failure or malicious behavior of some nodes, as long as a majority of nodes are correct and reachable.
- Voting protocols can be classified into two categories: exact voting and inexact voting.
  - Exact voting requires that all nodes agree on the same value or decision, and that the value or decision is correct according to some predefined criteria. Examples of exact voting are the two-phase commit protocol and the Paxos algorithm.
  - Inexact voting allows some nodes to have different or incorrect values or decisions, as long as the majority of nodes have the same or correct value or decision. Examples of inexact voting are the majority voting protocol and the Byzantine agreement protocol.
- Voting protocols can also be distinguished by the level of security they provide against malicious nodes or external attacks. Some voting protocols assume that all nodes are honest and cooperative, while others assume that some nodes may be faulty or compromised, and try to prevent or detect their influence on the voting outcome.
- Voting protocols can also be affected by the fairness of the voting process, which refers to the degree to which each node's vote is equally considered and respected. Some voting protocols may give more weight or priority to some nodes based on their reputation, performance, or other criteria, while others may treat all nodes equally. Fairness can have an impact on the efficiency, reliability, and robustness of the voting protocols.



### Dynamic voting protocols

- Dynamic voting protocols are a class of protocols for consistency and recovery control of replicated data in distributed systems  .
- The purpose of replicating data is to improve the availability and fault tolerance of a logical file or object in the presence of site failures and network partitions  .
- Dynamic voting protocols assign weights or votes to each replica of a file or object, and require a quorum or majority of votes to access or update the file or object  .
- The weights or votes of replicas can be dynamically changed or reassigned based on the current state of the system, such as the number of active sites, the network connectivity, or the access patterns  .
- Dynamic voting protocols aim to achieve the following goals  :
  - Availability: The file or object should be accessible or updatable by any site that is not isolated from the rest of the system.
  - Consistency: The file or object should have a consistent state across all replicas, and any update should be propagated to all replicas eventually.
  - Efficiency: The file or object should be accessed or updated with minimal communication and synchronization overhead.
- Dynamic voting protocols can be classified into two categories  :
  - Static-weight dynamic voting protocols: The weights or votes of replicas are fixed at the beginning of the system operation, and do not change during normal operation. However, the weights or votes can be reassigned when a site or link failure occurs, or when a site or link recovers.
  - Dynamic-weight dynamic voting protocols: The weights or votes of replicas can change dynamically during normal operation, based on some criteria such as the frequency of access, the distance between sites, or the load of sites.
- Dynamic voting protocols can use different quorum schemes to determine the minimum number of votes required to access or update a file or object   :
  - Majority quorum scheme: The quorum is more than half of the total votes in the system.
  - Read-one write-all quorum scheme: The quorum for read operations is one vote, and the quorum for write operations is all votes in the system.
  - Read-one write-all-available quorum scheme: The quorum for read operations is one vote, and the quorum for write operations is all votes in the available sites.
  - Tree quorum scheme: The quorum is a subset of votes that forms a connected subtree in a logical tree structure of the system.
  - Grid quorum scheme: The quorum is a subset of votes that forms a connected row or column in a logical grid structure of the system.



## Unit 8 - Transactions and Concurrency Control

- A **transaction** is a logical unit of work that consists of a sequence of operations on a database, such as reading, writing, inserting, deleting, or updating data.
- A transaction has four main properties, known as **ACID**:
  - **Atomicity**: A transaction is either executed completely or not at all. If any operation in the transaction fails, the whole transaction is aborted and the database is restored to its previous state.
  - **Consistency**: A transaction preserves the integrity and validity of the database. It ensures that the database satisfies all the constraints and rules before and after the transaction.
  - **Isolation**: A transaction is executed independently of other concurrent transactions. It does not interfere with or see the intermediate results of other transactions.
  - **Durability**: A transaction's effects are permanent and persistent in the database. They are not lost even in the case of system failures or power outages.
- **Concurrency control** is the management of simultaneously executing transactions in a shared database. It ensures that correct results for concurrent operations are generated while getting those results as quickly as possible .
- Concurrency control is important because it helps to maintain the **isolation** and **consistency** properties of transactions. Without concurrency control, concurrent transactions may cause problems such as:
  - **Lost update**: A transaction overwrites the changes made by another transaction without seeing them.
  - **Dirty read**: A transaction reads the uncommitted changes made by another transaction that may be rolled back later.
  - **Non-repeatable read**: A transaction reads the same data twice but gets different results because another transaction has modified the data in between.
  - **Phantom read**: A transaction reads a set of data that satisfies some condition but gets different results because another transaction has inserted or deleted some data that also satisfies the condition.
- Concurrency control techniques implement some protocols that can be broadly classified into two categories:
  - **Lock-based protocol**: This protocol uses locks to prevent concurrent transactions from accessing the same data item. A lock is a mechanism that grants or denies access to a data item. There are two types of locks: shared locks and exclusive locks. A shared lock allows a transaction to read a data item but not to modify it. An exclusive lock allows a transaction to both read and write a data item. A transaction must acquire a lock before accessing a data item and release it after finishing. A lock manager is responsible for granting, denying, and releasing locks. A lock-based protocol must follow two rules: 
    - **Two-phase locking**: A transaction must acquire all the locks it needs before releasing any lock. This ensures that a transaction holds all the locks until it commits or aborts, which preserves the atomicity property.
    - **No lock request is blocked**: A transaction must not wait indefinitely for a lock that is held by another transaction. This prevents deadlock, which is a situation where two or more transactions are waiting for each other to release locks.
  - **Timestamp-based protocol**: This protocol uses timestamps to order the execution of concurrent transactions. A timestamp is a unique identifier that indicates the start time of a transaction. Each data item has two timestamps: read timestamp and write timestamp. The read timestamp records the latest time when a data item was read by a transaction. The write timestamp records the latest time when a data item was written by a transaction. A timestamp-based protocol must follow two rules:
    - **Read-write conflict**: A transaction T1 can read a data item X only if the write timestamp of X is less than or equal to the timestamp of T1. This ensures that T1 does not read a data item that was modified by a later transaction, which preserves the consistency property.
    - **Write-write conflict**: A transaction T1 can write a data item X only if the write timestamp of X is less than the timestamp of T1. This ensures that T1 does not overwrite the changes made by a later transaction, which preserves the consistency property.



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
- Distributed concurrency control provides a mechanism to synchronize distributed transactions in such a way that the ACID properties are not violated by their interleaved execution.
- Distributed concurrency control makes sure that all subtransactions of a set of distributed transactions are serialized identically in all data servers involved.
- Distributed concurrency control can be implemented using various techniques, such as two-phase locking, two-phase commit, distributed timestamping, and distributed validation.



### Nested transactions for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A transaction is a sequence of operations that satisfies the ACID properties (Atomicity, Consistency, Isolation, Durability).
- A nested transaction is a transaction that is composed of subtransactions, each of which may have its own begin and end points, and may be committed or aborted independently.
- A nested transaction that accesses objects handled by different servers is referred to as a distributed nested transaction.
- Nested transactions can be used to improve the performance, reliability, and modularity of distributed systems, by allowing partial results to be committed or aborted without affecting the whole transaction, and by supporting concurrency control and recovery mechanisms at different levels of granularity.
- Nested transactions can be classified into two types: closed nested transactions and open nested transactions.
- Closed nested transactions are those in which the commit or abort of a subtransaction is only visible to its parent transaction, and not to other concurrent transactions. This ensures that the nested transaction is serializable with respect to other transactions, but it also limits the concurrency and parallelism that can be achieved.
- Open nested transactions are those in which the commit or abort of a subtransaction may be visible to other concurrent transactions, depending on the isolation level and the conflict resolution policy. This allows for more concurrency and parallelism, but it also introduces the possibility of inconsistency and cascading aborts.
- A common technique for implementing open nested transactions is to use compensating actions, which are operations that undo the effects of a committed subtransaction in case of a later abort. Compensating actions must be idempotent, commutative, and inverse to the original operations.
- A common technique for implementing distributed nested transactions is to use the two-phase commit protocol (2PC), which is a coordination protocol that ensures that all the servers involved in a transaction agree on its outcome. 2PC consists of two phases: a prepare phase, in which the coordinator asks the participants to vote on whether to commit or abort the transaction, and a commit phase, in which the coordinator informs the participants of the final decision based on the votes.
- 2PC can be extended to support nested transactions by using a hierarchical structure of coordinators and participants, where each subtransaction has its own coordinator that communicates with its parent coordinator and its participants. This allows for parallel execution of subtransactions and partial commit or abort of subtransactions. However, 2PC also has some drawbacks, such as blocking, vulnerability to failures, and lack of scalability.



### Locks for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A lock is a mechanism that allows only one of the innumerable nodes or processes to access and modify a resource or data that is being shared commonly to prevent execution of same task twice and also maintain data integrity.
- Locks are designed to enforce a mutual exclusion concurrency control policy, which means that only one transaction can hold a lock on a data item at a time.
- Locks can be classified into different types based on the following criteria:
  - The granularity of the data item being locked, such as record-level, page-level, or table-level locks.
  - The mode of the lock, such as shared (read) or exclusive (write) locks.
  - The duration of the lock, such as long (until the transaction commits or aborts) or short (until the operation finishes) locks.
  - The protocol of acquiring and releasing locks, such as two-phase locking (2PL), timestamp ordering, or optimistic concurrency control.
- In distributed systems, locks can be implemented using different strategies, such as:
  - Wait-and-see strategy, which involves pausing the operation until the lock is available or a timeout occurs.
  - Retry strategy, which involves aborting the operation and retrying it later with a backoff mechanism.
  - Fail-fast strategy, which involves aborting the operation and returning an error immediately.
- Distributed locks can be based on different types of systems, such as:
  - Distributed systems based on asynchronous replication, such as MySQL, Tair, and Redis, which use a leader-follower model and rely on the leader node to grant locks.
  - Paxos-based distributed consensus systems, such as ZooKeeper, etcd, and Consul, which use a quorum-based model and rely on a majority of nodes to agree on locks.
  - Distributed systems based on atomic operations, such as Redis, which use a single-key model and rely on the atomicity of operations such as SETNX and EXPIRE to acquire and release locks.



### Optimistic Concurrency Control

- Optimistic concurrency control (OCC) is a concurrency control method applied to transactional systems such as relational database management systems and software transactional memory.
- OCC assumes that multiple transactions can frequently complete without interfering with each other, and avoids locking of data items that can reduce performance.
- OCC only locks records from the time when the actual update is performed, not when they are fetched from the database for an update.
- OCC works by ensuring that the record being updated or deleted has the same values as it did when the updating or deleting process started.
- OCC can prevent lost updates and deletes by detecting concurrent, conflicting operations and aborting or retrying them.
- OCC is supported on many tables in Microsoft Dataverse, and can be checked by retrieving the table's metadata and looking for the column IsOptimisticConcurrencyEnabled.



### Timestamp ordering

- Timestamp ordering is a technique for ensuring serializability of transactions in a distributed system.
- A timestamp is a unique identifier assigned to each transaction that reflects its start time or priority.
- Timestamp ordering enforces a partial order on the transactions based on their timestamps, such that conflicting operations are executed in timestamp order.
- Timestamp ordering can be implemented in two ways: basic timestamp ordering and optimistic timestamp ordering.

#### Basic timestamp ordering

- Basic timestamp ordering assigns a timestamp to each transaction when it starts, and uses these timestamps to order the conflicting operations.
- Each data item has two timestamp fields: read timestamp (RTS) and write timestamp (WTS), which record the largest timestamp of any transaction that has read or written the item, respectively.
- A transaction can read an item if its timestamp is greater than or equal to the item's WTS, and can write an item if its timestamp is greater than both the item's RTS and WTS.
- If a transaction cannot read or write an item, it is aborted and restarted with a new timestamp.
- Basic timestamp ordering ensures serializability, but it may cause unnecessary aborts and restarts, and it does not guarantee freedom from deadlock.

#### Optimistic timestamp ordering

- Optimistic timestamp ordering is a variation of basic timestamp ordering that allows transactions to execute optimistically without checking timestamps, and validates them at commit time.
- Each transaction is divided into three phases: read phase, validation phase, and write phase.
- In the read phase, the transaction reads the data items from the database and stores them in a private workspace, without checking timestamps or locking the items.
- In the validation phase, the transaction checks if its operations are serializable with respect to the other transactions that have committed or are validating.
- In the write phase, the transaction writes its updates to the database, if it passes the validation.
- Optimistic timestamp ordering reduces the number of aborts and restarts, and avoids deadlock, but it may increase the overhead of validation and write phases, and it may not be suitable for high-conflict workloads.



### Comparison of methods for concurrency control

Concurrency control is the process of managing the simultaneous execution of transactions in a distributed system, such that the consistency and correctness of the data are preserved. There are various methods for concurrency control, each with its own advantages and disadvantages. Some of the common methods are:

- **Two-phase locking (2PL)**: This method requires each transaction to acquire locks on the data items it needs to access, and release them after it finishes. There are two phases: the growing phase, where the transaction can only acquire locks, and the shrinking phase, where the transaction can only release locks. The transaction cannot acquire any new locks after it releases any lock. This method ensures serializability, which means the concurrent execution of transactions is equivalent to some serial execution. However, it may cause deadlock, where two or more transactions are waiting for each other to release locks, and thus cannot proceed. Deadlock can be prevented or detected and resolved by using various techniques, such as timeouts, deadlock prevention protocols, or deadlock detection algorithms.  

- **Timestamp ordering (TO)**: This method assigns a unique timestamp to each transaction, which reflects its start time or priority. The timestamp is used to order the transactions and determine their precedence. Each data item has two timestamps: the read timestamp (RTS), which records the timestamp of the last transaction that read the item, and the write timestamp (WTS), which records the timestamp of the last transaction that wrote the item. When a transaction tries to read or write a data item, it has to check its timestamp against the RTS and WTS of the item, and follow some rules to decide whether to proceed, abort, or wait. This method avoids deadlock, but may cause aborts and restarts of transactions, which can affect the performance and throughput of the system. There are different variants of TO, such as basic TO, Thomas' write rule, and multiversion TO.  

- **Multiversion concurrency control (MVCC)**: This method allows multiple versions of the same data item to coexist, and assigns a timestamp or a version number to each version. Each transaction can read the most recent version of the data item that is compatible with its timestamp, and write a new version of the data item with its own timestamp. This method reduces the conflicts between read and write operations, and allows more concurrency and availability. However, it requires more storage space and overhead to maintain and garbage collect the versions. It also requires a mechanism to ensure the consistency and freshness of the versions.  

- **Validation (or optimistic) concurrency control (VCC)**: This method assumes that conflicts between transactions are rare, and allows transactions to execute without any locking or checking. However, before committing, each transaction has to validate its read and write sets against the committed transactions, and ensure that it does not violate the serializability property. If a conflict is detected, the transaction has to abort and restart. This method avoids locking and deadlock, and improves the performance for low-conflict workloads. However, it may cause a high abort rate and waste of resources for high-conflict workloads.  

- **Distributed concurrency control**: This is the general term for the concurrency control of a system distributed over a computer network, where the data is hosted by a group of linked data servers. The methods mentioned above can be applied to distributed systems, but they may face some additional challenges, such as network latency, communication cost, partial failures, and data replication. Therefore, some trade-offs and adaptations may be needed to balance the consistency, availability, and partition tolerance of the system. For example, some systems may use weaker consistency models, such as eventual consistency or causal consistency, to allow more concurrency and availability. Some systems may use distributed locking protocols, such as two-phase commit or three-phase commit, to coordinate the locks across multiple servers. Some systems may use distributed timestamp protocols, such as Lamport timestamps or vector clocks, to order the transactions across multiple servers.



## Unit 9 - Distributed Transactions

- A distributed transaction is a type of transaction that involves two or more network hosts, usually providing transactional resources, such as databases, message queues, file systems, etc.
- A distributed transaction is coordinated by a transaction manager, which is responsible for creating and managing a global transaction that encompasses all the operations against the transactional resources.
- A distributed transaction ensures the ACID properties (atomicity, consistency, isolation, and durability) across multiple hosts, meaning that either all the operations succeed or none of them, and the data remains consistent, isolated, and durable after the transaction.
- A distributed transaction can be implemented using different protocols, such as two-phase commit, three-phase commit, Paxos commit, etc. These protocols typically involve communication and coordination among the transaction manager, the resource managers, and the participants (the hosts that execute the operations).
- A distributed transaction can improve the performance, availability, and scalability of a system, by allowing concurrent and parallel access to distributed data. However, it also introduces challenges, such as network latency, concurrency control, fault tolerance, and security.



### Flat and Nested Distributed Transactions

- A **flat or nested transaction** that accesses objects handled by different servers is referred to as a **distributed transaction** .
- When a distributed transaction reaches its end, in order to maintain the **atomicity property** of the transaction, it is mandatory that all of the servers involved in the transaction either **commit** the transaction or **abort** it .
- Distributed transactions can be structured in two different ways: **flat transactions** and **nested transactions** .
- A **flat transaction** has a single initiating point (**Begin**) and a single end point (**Commit** or **Abort**). They are usually very simple and are generally used for short activities rather than larger ones .
- A **nested transaction** is a transaction that consists of several subtransactions, each of which may be distributed. A nested transaction has a **root transaction** and several **subtransactions**. Each subtransaction may have its own subtransactions, forming a **tree structure** .
- A nested transaction has the following properties:
  - **Atomicity**: If the root transaction commits, then all the subtransactions commit. If the root transaction aborts, then all the subtransactions abort.
  - **Consistency**: Each subtransaction preserves the consistency of the data it accesses.
  - **Isolation**: The effects of a subtransaction are not visible to other subtransactions until the root transaction commits.
  - **Durability**: The effects of a committed subtransaction are persistent and not lost due to failures.
- A nested transaction allows more **flexibility** and **concurrency** than a flat transaction, as it can handle partial failures and independent recoveries of subtransactions. It also allows more **modularity** and **reuse** of subtransactions, as they can be composed into larger transactions.



### Atomic Commit Protocols for Distributed Transactions

- A distributed transaction is a transaction that involves multiple servers or nodes in a distributed system.
- An atomic commit protocol is a protocol that ensures that a distributed transaction is either committed or rolled back in its entirety, even if the system fails or some of the nodes fail or crash.
- Ensuring atomic commit is important for maintaining the consistency and integrity of the data in a distributed system.
- There are different types of atomic commit protocols, such as two-phase commit (2PC), three-phase commit (3PC), parallel commit, and failure-aware commit (FLAC).
- Two-phase commit (2PC) is the most widely used atomic commit protocol. It consists of two phases: a prepare phase and a commit phase. In the prepare phase, a coordinator node sends a prepare message to all the participant nodes, asking them to vote on whether they are ready to commit or not. In the commit phase, the coordinator node collects the votes and decides whether to commit or abort the transaction, and sends the decision to all the participant nodes. The participant nodes then execute the decision and send an acknowledgment to the coordinator node. The coordinator node waits for all the acknowledgments before ending the transaction.
- Three-phase commit (3PC) is an extension of 2PC that adds a pre-commit phase between the prepare and commit phases. In the pre-commit phase, the coordinator node sends a pre-commit message to all the participant nodes, indicating that they have voted to commit. The participant nodes then send an acknowledgment to the coordinator node. In the commit phase, the coordinator node sends a commit message to all the participant nodes, and the participant nodes execute the commit and send an acknowledgment to the coordinator node. The coordinator node waits for all the acknowledgments before ending the transaction. The pre-commit phase is intended to avoid blocking in case of failures, by allowing the participant nodes to reach a consistent state before committing.
- Parallel commit is a new atomic commit protocol that reduces the latency of transactions down to only a single round-trip of distributed consensus. It does not use a coordinator node, but instead relies on the participant nodes to communicate with each other and reach a consensus on whether to commit or abort the transaction. The participant nodes use a timestamp-based protocol to determine the order of transactions and resolve conflicts. The participant nodes also use a write intent mechanism to indicate their intention to commit a transaction, and a transaction record to store the final status of the transaction. The participant nodes can commit a transaction in parallel, as long as they have written their write intents and transaction records, and have obtained the consensus of the other participant nodes.
- Failure-aware commit (FLAC) is a practical atomic commit protocol that leverages the failure information of the participant nodes to optimize the commit process. It uses a typical transactional system architecture, where a client node initiates a transaction and sends requests to the participant nodes. The participant nodes execute the requests and send responses to the client node. The client node then decides whether to commit or abort the transaction, and sends the decision to the participant nodes. The participant nodes execute the decision and send an acknowledgment to the client node. The client node waits for all the acknowledgments before ending the transaction. FLAC introduces a failure-awareness mechanism, where the participant nodes monitor the status of the other participant nodes and report the failure information to the client node. The client node then uses the failure information to adjust the commit decision and the acknowledgment waiting time, to reduce the commit latency and avoid blocking.



### Concurrency control in distributed transactions

- Concurrency control is the process of ensuring that concurrent operations on a shared data do not violate the consistency and isolation properties of transactions.
- Distributed transactions are transactions that span multiple data servers that are connected by a network.
- Distributed concurrency control provides a mechanism to synchronize distributed transactions in such a way that the ACID properties are not violated by their interleaved execution .
- There are different types of distributed concurrency control protocols, such as locking-based, timestamp-based, optimistic, and consensus-based  .
- Locking-based protocols use the concept of locking data items to prevent conflicting operations from different transactions.
- Timestamp-based protocols use a transaction’s timestamp to determine the order of operations and to detect and resolve conflicts.
- Optimistic protocols assume that conflicts are rare and allow transactions to execute without any synchronization, but validate them before committing.
- Consensus-based protocols use a distributed agreement protocol, such as two-phase commit (2PC) or three-phase commit (3PC), to coordinate the commit or abort decision of distributed transactions.



### Distributed Deadlocks

- A distributed deadlock is a situation where a set of processes in a distributed system are waiting for each other to release resources or messages, and none of them can proceed .
- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems .
- Distributed deadlocks are harder to detect, avoid, and prevent than deadlocks in centralized systems, because there is no single authority that can oversee resource allocation and dependency graphs.
- There are three main approaches to handle distributed deadlocks :
  - Prevention: This approach tries to ensure that at least one of the necessary conditions for deadlock (mutual exclusion, hold and wait, no preemption, circular wait) is never satisfied. For example, by using timeouts, ordering resources, or aborting transactions.
  - Avoidance: This approach tries to ensure that the system will always remain in a safe state, where there is at least one possible sequence of resource allocation that will not lead to deadlock. For example, by using the banker's algorithm or timestamps.
  - Detection and recovery: This approach tries to identify the existence of deadlocks and then take some actions to resolve them. For example, by constructing a global wait-for graph, using edge chasing algorithms, or initiating rollback or restart mechanisms.
- The techniques of deadlock detection in distributed systems require the following properties:
  - Progress: The method should be able to detect all the deadlocks in the system.
  - Safety: The method should not detect false or phantom deadlocks.



### Transaction recovery for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

- Transaction recovery is the process of restoring a distributed database system to a consistent state after a failure of one or more components, such as sites, networks, or transactions.
- Transaction recovery is essential for maintaining the ACID properties of transactions, especially atomicity and durability.
- Transaction recovery involves two main steps: failure detection and failure recovery.
- Failure detection is the process of identifying and reporting the occurrence of a failure in the system. Failure detection can be done by various methods, such as timeouts, acknowledgments, heartbeats, or voting.
- Failure recovery is the process of restoring the system to a consistent state after a failure. Failure recovery can be done by various methods, such as undoing, redoing, or compensating the effects of failed transactions, or using backup copies or shadow versions of the data.
- Transaction recovery can be classified into two types: local recovery and global recovery.
- Local recovery is the process of recovering a single site or transaction after a failure. Local recovery can be done by using techniques such as write-ahead logging, checkpoints, or shadow paging.
- Global recovery is the process of recovering the entire system or a distributed transaction after a failure. Global recovery can be done by using techniques such as two-phase commit, three-phase commit, or presumed abort/commit protocols.



## Unit 10 - Replication

- Replication is a biological process of duplicating or producing an exact copy, such as a polynucleotide strand (DNA) .
- Replication is essential for the transmission of genetic information from one generation to the next and for the maintenance of genetic stability within a population .
- Replication relies on the fact that each strand of DNA can serve as a template for duplication, following the complementary base pairing rules .
- Replication can be divided into three stages: initiation, elongation, and termination .
- Initiation is the stage where the DNA helix is unwound and the replication machinery is assembled at the origin of replication .
- Elongation is the stage where the DNA polymerase enzyme synthesizes new DNA strands by adding nucleotides to the 3' end of the growing chain, following the template strand .
- Termination is the stage where the replication process is completed and the newly synthesized DNA strands are separated and rewound into a double helix .
- Replication can be either semiconservative or conservative. Semiconservative replication means that each new DNA molecule consists of one old and one new strand, while conservative replication means that the original DNA molecule is preserved and a new one is formed .
- Replication can also be either bidirectional or unidirectional. Bidirectional replication means that the replication fork moves in both directions from the origin of replication, while unidirectional replication means that the replication fork moves in only one direction .
- Replication can vary between different organisms and cell types. For example, bacteria usually have a single circular chromosome with a single origin of replication, while eukaryotes usually have multiple linear chromosomes with multiple origins of replication .



### System model and group communication for replication in distributed systems

- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by passing messages.
- Replication is a technique to improve the availability, performance, and fault tolerance of a distributed system by creating and maintaining multiple copies of data or services across different processes or nodes.
- A system model is a set of assumptions and properties that describe the behavior and characteristics of a distributed system, such as the communication model, the failure model, the timing model, and the security model.
- A group is a subset of processes in a distributed system that share some common interest or functionality, such as maintaining a replicated service or data item.
- Group communication is a mechanism for sending messages from one process to a group of processes in a reliable, ordered, and efficient way.
- Group communication can be classified into two types: broadcast communication and multicast communication.
- Broadcast communication is when a process sends a message to all other processes in the system, regardless of their group membership or interest. Broadcast communication can be used for disseminating information, discovering resources, or electing leaders in a distributed system.
- Multicast communication is when a process sends a message to a subset of processes in the system, based on their group membership or interest. Multicast communication can be used for implementing replicated services, synchronizing clocks, or coordinating transactions in a distributed system.
- Group communication can be implemented using various protocols and algorithms, such as reliable broadcast, causal broadcast, atomic broadcast, reliable multicast, causal multicast, and atomic multicast. These protocols and algorithms differ in their guarantees and properties, such as reliability, ordering, atomicity, and causality.
- Group communication can also be supported by various middleware and infrastructures, such as publish-subscribe systems, message brokers, message queues, group communication toolkits, and overlay networks. These middleware and infrastructures provide different levels of abstraction, functionality, and scalability for group communication in distributed systems.



### Fault-tolerant services for the notes of the Unit 10 - Replication in the subject of DISTRIBUTED SYSTEM

- Fault-tolerant services are services that can continue to function correctly even in the presence of failures, such as server crashes, network partitions, or malicious attacks.
- Replication is a technique for implementing fault-tolerant services by creating and maintaining multiple copies of the same service (or object) on different servers in a distributed system.
- Replication can improve availability, performance, and reliability of the service, but also introduces challenges such as consistency, concurrency, and communication overhead.
- The main classes of replication techniques are:
  - Primary-backup replication: One server acts as the primary (or leader) and handles all the requests from the clients, while the other servers act as backups (or followers) and receive updates from the primary. The primary is responsible for ensuring that the backups are consistent with it. If the primary fails, a new primary is elected from the backups.
  - Active replication: All servers act as replicas and execute the same requests from the clients in the same order. The replicas use a consensus protocol to agree on the order of requests and ensure consistency. If a replica fails, the remaining replicas can continue to serve the clients.
- The correctness criterion for replicated services is linearizability, which means that the service behaves as if there is only one copy of it and every request is executed atomically and in the order specified by the clients.
- The trade-offs between primary-backup replication and active replication are:
  - Primary-backup replication has lower communication overhead and latency than active replication, but requires more complex recovery mechanisms and may have lower availability and fault-tolerance.
  - Active replication has higher communication overhead and latency than primary-backup replication, but requires simpler recovery mechanisms and may have higher availability and fault-tolerance.



### Highly Available Services for the Notes of the Unit 10 - Replication in the Subject of Distributed System

- Replication is the process of creating and maintaining multiple copies of data or services across different nodes or locations in a distributed system.
- Replication can enhance the availability, reliability, performance, and scalability of distributed systems by reducing the impact of failures, network congestion, and data access latency.
- Replication can also enable load balancing, fault tolerance, and disaster recovery for distributed systems.
- Replication can be classified into two types: eager replication and lazy replication.
  - Eager replication ensures that all copies of data or services are updated synchronously or quasi-synchronously whenever a change occurs. This guarantees strong consistency and high availability, but at the cost of higher communication and coordination overhead.
  - Lazy replication allows some copies of data or services to be updated asynchronously or periodically after a change occurs. This improves performance and scalability, but may result in weaker consistency and lower availability.
- Replication can be implemented at different levels of abstraction, such as data replication, service replication, or process replication.
  - Data replication involves creating and maintaining multiple copies of data items or databases across different nodes or locations. Data replication can be further divided into full replication and partial replication, depending on whether all or some of the data items are replicated.
  - Service replication involves creating and maintaining multiple copies of a service or a functionality across different nodes or locations. Service replication can be further divided into stateful replication and stateless replication, depending on whether the service maintains some state or not.
  - Process replication involves creating and maintaining multiple copies of a process or a computation across different nodes or locations. Process replication can be further divided into active replication and passive replication, depending on whether all or some of the processes execute the same requests or not.
- Replication can be coordinated by different protocols or algorithms, such as primary-backup, quorum-based, or viewstamped replication.
  - Primary-backup replication assigns a primary node to handle all requests and updates, and one or more backup nodes to receive and store the updates from the primary. The primary node can be elected by a leader election algorithm, such as Paxos or Raft. If the primary node fails, a backup node can take over as the new primary.
  - Quorum-based replication requires a minimum number of nodes (a quorum) to agree on each update or read operation. A quorum can be calculated by a majority rule, a weighted rule, or a dynamic rule, depending on the system configuration and requirements. Quorum-based replication can tolerate node failures and network partitions, as long as a quorum can be reached.
  - Viewstamped replication organizes the nodes into a sequence of views, where each view has a leader node and a set of follower nodes. The leader node coordinates the updates and sends them to the follower nodes in a viewstamped order. If the leader node fails or a network partition occurs, the nodes can switch to a new view with a new leader.



### Transactions with replicated data

- Transactions are a sequence of operations that are executed atomically, consistently, isolatedly, and durably (ACID properties) on a database system.
- Replication is a technique to distribute data across multiple servers or locations, so that users can access data relevant to their activities without interfering with the work of others, and to improve availability, performance, and fault-tolerance of the system.
- Transactions with replicated data are transactions that involve data items that are replicated on different servers or locations, and need to be synchronized and consistent after the transaction.
- Transactions with replicated data pose several challenges for distributed systems, such as:
  - How to ensure atomicity and durability of transactions that span multiple servers or locations?
  - How to ensure consistency and isolation of transactions that access or update replicated data items?
  - How to handle concurrency, conflicts, and failures of transactions with replicated data?
  - How to balance the trade-offs between performance, availability, and consistency of transactions with replicated data?
- There are different approaches to handle transactions with replicated data, such as:
  - Two-phase commit protocol (2PC): A distributed protocol that ensures atomicity and durability of transactions that span multiple servers or locations, by using a coordinator and participants to agree on the outcome of the transaction (commit or abort) in two phases: prepare and commit/abort.
  - Quorum-based protocols: A distributed protocol that ensures consistency and availability of transactions that access or update replicated data items, by using a quorum (a subset of replicas) to perform read or write operations, and to resolve conflicts or failures.
  - Optimistic replication: A distributed protocol that allows transactions to access or update replicated data items without coordination or locking, and to detect and resolve conflicts or inconsistencies later, by using versioning, validation, and reconciliation techniques.
  - Elastic database transactions: A distributed protocol that enables transactions across cloud databases that are part of the same logical group, by using .NET libraries that ensure two-phase commit where necessary to ensure atomicity.

