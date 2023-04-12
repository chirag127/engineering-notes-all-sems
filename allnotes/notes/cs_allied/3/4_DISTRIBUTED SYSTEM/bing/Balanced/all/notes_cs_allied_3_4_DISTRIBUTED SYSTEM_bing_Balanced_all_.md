

# Distributed System

A distributed system is a system whose components are located on different networked computers, which communicate and coordinate their actions by passing messages to one another. A distributed system can also be defined as a number of independent computers linked by a network, or a computing environment in which various components are spread across multiple computers (or other computing devices) on a network.

Some of the main characteristics of a distributed system are:

- The components are autonomous, meaning they can operate independently and have their own failure modes.
- The components are heterogeneous, meaning they can have different hardware, software, operating systems, and protocols.
- The components are scalable, meaning the system can handle increasing workloads by adding more components or resources.
- The components are transparent, meaning the system hides the complexity and details of the distribution from the users and applications.

Some of the main challenges of a distributed system are:

- The components are prone to failures, such as crashes, network partitions, or malicious attacks.
- The components are inconsistent, meaning they can have different views of the system state or data due to delays, replication, or concurrency.
- The components are concurrent, meaning they can execute simultaneously and interact with each other in unpredictable ways.
- The components are insecure, meaning they can be vulnerable to unauthorized access, modification, or disclosure of data or resources.

Some of the main benefits of a distributed system are:

- The components are reliable, meaning the system can tolerate failures and provide continuous service.
- The components are efficient, meaning the system can utilize the resources and capabilities of multiple components to perform tasks faster or better.
- The components are flexible, meaning the system can adapt to changing requirements and environments.
- The components are collaborative, meaning the system can enable cooperation and coordination among different users and applications.



## Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- The main characteristics of distributed systems are:
  - Concurrency: Multiple components can execute simultaneously and interact with each other.
  - No global clock: There is no shared physical clock among the components, and the clocks may drift apart over time.
  - Independent failures: Each component can fail independently without affecting the whole system, and the system can tolerate some degree of failures.
  - Heterogeneity: The components can have different hardware, software, network, and data formats, and the system can cope with the diversity.
  - Scalability: The system can grow in size and complexity without losing its functionality and performance.
  - Transparency: The system can hide the details of its internal structure and behavior from the users, and provide a uniform interface and service.
- The main challenges of distributed systems are:
  - Coordination: The components need to synchronize their actions and share their states in order to achieve a common goal.
  - Consistency: The system needs to maintain a coherent view of the data and the processes among the components, despite the concurrency, failures, and heterogeneity.
  - Fault tolerance: The system needs to detect, isolate, and recover from the failures of the components, and provide reliable and available services.
  - Security: The system needs to protect the data and the processes from unauthorized access, modification, and disruption, and ensure the confidentiality, integrity, and authenticity of the information.



# Introduction for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- A distributed system has the following characteristics:
  - Concurrency: The components of the system can execute simultaneously and independently.
  - No global clock: The components of the system do not share a common notion of time or a global clock.
  - Independent failures: The components of the system can fail independently and recover from failures without affecting the rest of the system.
- A distributed system has the following advantages:
  - Resource sharing: The system can share resources such as data, hardware, software, and services among the components.
  - Scalability: The system can grow or shrink in size and performance by adding or removing components.
  - Fault tolerance: The system can tolerate and mask failures of some components and continue to provide services to the users.
  - Transparency: The system can hide the details of its internal structure and behavior from the users and provide a uniform interface.
- A distributed system has the following challenges:
  - Heterogeneity: The system has to deal with the diversity of hardware, software, network, and data formats among the components.
  - Security: The system has to protect the confidentiality, integrity, and availability of the resources and services from unauthorized access and malicious attacks.
  - Coordination: The system has to coordinate the actions and interactions of the components to achieve a common goal or a consistent state.
  - Consistency: The system has to maintain a consistent view of the data and services among the components despite concurrent updates and failures.
  - Performance: The system has to optimize the use of resources and minimize the communication overhead and latency among the components.



# Examples of Distributed Systems

A distributed system is a collection of independent computers that communicate and coordinate their actions by passing messages. The computers in a distributed system may be physically close or geographically dispersed, and they may be connected by a network or a bus. Distributed systems can provide higher performance, reliability, scalability, and availability than centralized systems.

Some examples of distributed systems are:

- **Telecommunication networks**: Telephone networks are an early example of a peer-to-peer network, where each node can initiate or receive calls. Cellular and telephone networks are forms and examples of distributed networks. They use protocols such as TCP/IP, HTTP, and SMTP to exchange data and messages. Telecommunication networks also include the Internet, which is a global network of networks that connects millions of computers and devices.

- **Real-time systems**: Many industries use real-time systems distributed in various areas, locally and globally. For example, air traffic control systems, power grid systems, industrial control systems, and autonomous vehicles are all examples of real-time distributed systems. They require fast and accurate communication and synchronization among the components, and they have strict timing constraints and deadlines.

- **Distributed database systems**: A distributed database is a database that has locations across multiple servers, physical locations, or both. The data may be replicated or partitioned, and the database system may use different architectures such as client-server, peer-to-peer, or federated. Distributed database systems can improve performance, availability, and scalability, but they also introduce challenges such as concurrency control, transaction management, and data consistency.

- **Distributed computing systems**: A distributed computing system is a system that uses multiple computers to perform a computation or a task. The computers may be homogeneous or heterogeneous, and they may use different models of communication and coordination such as message passing, shared memory, or remote procedure calls. Examples of distributed computing systems include grid computing, cloud computing, cluster computing, and parallel computing.

- **Distributed applications**: A distributed application is an application that runs on multiple computers and provides a service or a functionality to the users. The application may use different technologies and frameworks such as web services, service-oriented architecture, microservices, or middleware. Examples of distributed applications include web applications, mobile applications, multiplayer online games, peer-to-peer applications, and blockchain applications.



# Resource sharing and the web challenges in distributed systems

Resource sharing is the process of making the resources of a distributed system available to the users and applications in a transparent and efficient way. The resources can be hardware, software, or data. The web is an example of a large-scale distributed system that enables resource sharing across the internet.

Some of the challenges for resource sharing and the web in distributed systems are:

- **Transparency**: The ability to hide the details of the distribution of components and resources from the users and applications, so that the system appears as a whole rather than as a collection of independent parts. Transparency can be achieved at different levels, such as access, location, migration, replication, concurrency, failure, and performance .
- **Scalability**: The ability to cope with the growth of the system in terms of users, resources, and geographical span, without degrading the performance or functionality of the system. Scalability can be achieved by using techniques such as caching, replication, load balancing, partitioning, and decentralization .
- **Heterogeneity**: The ability to deal with the diversity of the hardware, software, network, and data formats in the system, and to provide interoperability and compatibility among them. Heterogeneity can be achieved by using standards, protocols, middleware, and adapters .
- **Security**: The ability to protect the system and its resources from unauthorized access, modification, or damage, and to provide confidentiality, integrity, availability, and accountability. Security can be achieved by using mechanisms such as encryption, authentication, authorization, auditing, and firewalls .
- **Reliability**: The ability to ensure the correct and consistent functioning of the system and its resources, despite the failures of components, networks, or services. Reliability can be achieved by using techniques such as fault tolerance, redundancy, recovery, and consensus  .
- **Performance**: The ability to provide efficient and timely service to the users and applications, and to optimize the utilization of the system resources. Performance can be measured by metrics such as throughput, latency, bandwidth, and availability. Performance can be improved by using techniques such as parallelism, concurrency, caching, compression, and scheduling  .



# Architectural models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Architectural models are a type of system model that describe the organization and interrelationship of components in a distributed system .
- Architectural models can help to design, implement, and evaluate distributed systems by providing a high-level view of the system structure and behavior.
- Architectural models can also help to identify the challenges and trade-offs involved in distributed computing, such as scalability, performance, reliability, security, and consistency .
- There are various architectural models that are commonly used for distributed systems, such as:
  - Client-server architecture: A model where one or more servers provide services to multiple clients over a network . The servers are usually centralized and have more resources and capabilities than the clients. The clients are usually distributed and have less resources and capabilities than the servers. The clients initiate requests to the servers and wait for responses. The servers process the requests and send back responses to the clients.
  - Broker architecture: A model where a broker component acts as an intermediary between clients and servers. The broker is responsible for locating the servers that can provide the requested service, forwarding the requests from the clients to the servers, and returning the responses from the servers to the clients. The broker can also provide additional functionalities, such as load balancing, caching, and fault tolerance. The broker architecture can be seen as an extension of the client-server architecture with an extra layer of abstraction.
  - Service-oriented architecture (SOA): A model where the system is composed of loosely coupled and interoperable services that communicate with each other using standard protocols and interfaces . The services are self-contained and independent units of functionality that can be reused and composed to create complex applications . The services can be discovered, invoked, and composed dynamically at runtime using a service registry and a service bus . The SOA model can be seen as a generalization of the broker architecture with more flexibility and modularity .
  - Distributed network architecture: A model where each network within the system can interact with other networks for the purpose of service resiliency, performance gains, and automated resource sharing. The networks can have different configurations, such as mainframes, computers, workstations, and minicomputers. The networks can operate independently, but management and monitoring are centralized. The distributed network architecture can be seen as a hybrid of the client-server and the SOA models with more decentralization and heterogeneity.
  - Layered architecture: A model where the system is divided into layers, each of which communicates with its adjacent layer by sending requests and getting responses . The layers can have different responsibilities and functionalities, such as presentation, application, business, data, and infrastructure. The layers can be distributed across different nodes or co-located on the same node. The layered architecture can be seen as a way of organizing the components within a system according to their abstraction level and dependency.



# Fundamental Models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Fundamental models are descriptions of properties that are present in all distributed architectures  .
- They help us understand the characteristics, challenges and trade-offs of designing and implementing distributed systems.
- There are three main types of fundamental models: interaction models, failure models and security models  .

## Interaction Models
- Interaction models deal with the issues of how processes communicate and coordinate with each other in a distributed system  .
- They include aspects such as performance, timing, ordering and synchronization of events  .
- Some examples of interaction models are:
  - Synchronous vs. asynchronous communication: whether the sender and receiver of a message have to wait for each other or not.
  - Remote procedure call (RPC) vs. message passing: whether the communication is based on invoking a procedure on a remote machine or sending a message to a destination.
  - Publish/subscribe vs. point-to-point: whether the communication is based on broadcasting messages to multiple subscribers or sending messages to a specific receiver.
  - Client/server vs. peer-to-peer: whether the communication is based on a centralized server that provides services to clients or a decentralized network of peers that cooperate with each other.

## Failure Models
- Failure models specify the types of faults that can occur in a distributed system and how they affect the processes and communication channels  .
- They help us design fault-tolerant mechanisms and protocols to ensure the reliability and availability of the system.
- Some examples of failure models are:
  - Crash failure: a process stops executing and does not resume .
  - Omission failure: a process fails to send or receive a message .
  - Timing failure: a process fails to meet a timing constraint .
  - Byzantine failure: a process behaves arbitrarily and may send incorrect or malicious messages .

## Security Models
- Security models define the threats and attacks that can compromise the confidentiality, integrity and availability of a distributed system and the countermeasures that can be applied to prevent or mitigate them .
- They help us design secure mechanisms and protocols to ensure the authenticity, authorization and accountability of the system.
- Some examples of security models are:
  - Cryptographic models: based on mathematical techniques to encrypt and decrypt data, generate keys and signatures, and verify identities.
  - Access control models: based on policies and rules to grant or deny access to resources, such as discretionary, mandatory and role-based access control.
  - Trust models: based on assumptions and evidence to establish the trustworthiness of entities, such as certificates, reputation and trust networks.



# Theoretical Foundation for Distributed System

- A distributed system is a system whose components are located on different networked computers, which communicate and coordinate their actions by passing messages to one another.
- Distributed computing is a field of computer science that studies distributed systems and their properties, such as scalability, fault-tolerance, consistency, and concurrency.
- Theoretical foundations of distributed systems are the theories that provide formal models, methods, and tools for analyzing, designing, and verifying distributed systems.
- Some of the main theoretical perspectives of distributed systems are:
  - **Fundamental limitations**: These are the inherent trade-offs and impossibility results that constrain what distributed systems can achieve, such as the CAP theorem, the FLP impossibility, and the lower bounds on consensus and broadcast.
  - **Computational models**: These are the abstract representations of distributed systems that capture their essential features, such as the message-passing model, the shared-memory model, the synchronous and asynchronous models, and the Byzantine model.
  - **Algorithmic paradigms**: These are the general techniques and principles for designing and implementing distributed algorithms, such as leader election, mutual exclusion, distributed snapshots, state machine replication, and distributed hash tables.
  - **Verification methods**: These are the formal approaches for proving the correctness and performance of distributed algorithms, such as temporal logic, model checking, proof assistants, and game theory.



# Limitation of Distributed System

A distributed system is a system that consists of multiple independent components that communicate with each other over a network. Distributed systems have many advantages, such as scalability, fault tolerance, availability, and performance. However, they also face some limitations that make them challenging to design and implement. Some of the main limitations of distributed systems are:

- **Absence of a global state**: In a distributed system, there is no single point of control or coordination for the entire system. Each component has its own local state and view of the system, which may differ from the views of other components. This makes it difficult to reason about the behavior and correctness of the system, and to synchronize the actions and data of different components. For example, it is hard to ensure consistency and atomicity of transactions that span multiple components, or to detect and resolve conflicts and anomalies that may arise due to concurrent updates.

- **Absence of a global clock**: In a distributed system, there is no common notion of time or ordering of events for the entire system. Each component has its own local clock, which may not be synchronized with the clocks of other components. This makes it difficult to measure and compare the timestamps and durations of events that occur in different components, and to establish causal relationships and dependencies among them. For example, it is hard to implement reliable and efficient synchronization and coordination mechanisms, such as mutual exclusion, consensus, and leader election, that rely on the assumption of a global clock.

- **Network latency and failures**: In a distributed system, the communication between components is subject to delays and errors due to the network. The network latency may vary depending on the distance, bandwidth, congestion, and routing of the messages. The network failures may cause messages to be lost, duplicated, corrupted, or reordered. This makes it difficult to ensure the timeliness, reliability, and integrity of the communication, and to handle the partial failures and partitions that may occur in the system. For example, it is hard to implement reliable and efficient replication and fault tolerance mechanisms, such as consensus, quorum, and checkpointing, that rely on the assumption of a reliable and timely network.

- **Heterogeneity and diversity**: In a distributed system, the components may have different hardware, software, and network characteristics, such as processing power, memory capacity, operating system, programming language, and network protocol. This makes it difficult to ensure the compatibility, interoperability, and portability of the components, and to handle the variations and changes that may occur in the system. For example, it is hard to implement common and consistent interfaces, protocols, and standards that can support the communication and coordination of diverse and heterogeneous components.



# Absence of Global Clock

- A global clock is a system-wide clock that is equally accessible to all processes in a distributed system and provides a common notion of time.
- A global clock is useful for determining the order of events and the state of the system across different processes.
- However, a global clock is hard to realize in distributed systems due to two inherent limitations: lack of shared memory and unpredictable message delays.
- Lack of shared memory means that processes in a distributed system do not have access to a common storage that can store and update the global clock value.
- Unpredictable message delays mean that the communication channel between processes is unreliable and the transmission time of messages is variable and unknown.
- Therefore, processes in a distributed system may have different and inconsistent views of the global clock and the global state of the system.
- The absence of a global clock poses challenges for designing and implementing distributed algorithms and protocols that require synchronization, coordination, and consistency among processes.



# Shared Memory

Shared memory is a programming model for distributed systems that allows multiple processes to access a common logical address space, as if they were running on a single machine. Shared memory can simplify the communication and synchronization among processes, and enable the implementation of parallel algorithms and data structures.

There are two types of shared memory models: physical and virtual.

## Physical Shared Memory

Physical shared memory refers to a system where multiple processors are connected to a single memory module, or a shared bus that interconnects multiple memory modules. Each processor can directly access any memory location by issuing a load or store instruction. Physical shared memory systems are also known as symmetric multiprocessors (SMPs) or uniform memory access (UMA) systems.

The advantages of physical shared memory are:

- It provides a simple and uniform programming model, where all processes can access the same variables and data structures without explicit message passing.
- It allows for low-latency and high-bandwidth communication among processes, as they can access the shared memory in a single instruction cycle.
- It supports fine-grained parallelism, where processes can operate on small chunks of data without incurring significant overhead.

The disadvantages of physical shared memory are:

- It is expensive and difficult to scale, as the number of processors and memory modules increases. The shared bus or memory module can become a bottleneck for communication and contention.
- It requires hardware support for cache coherence, which ensures that all processors see a consistent view of the shared memory. Cache coherence protocols can introduce additional complexity and overhead to the system.
- It is prone to errors and inconsistencies, as processes can overwrite each other's data or access invalid memory locations. Processes need to use synchronization mechanisms, such as locks, semaphores, or atomic operations, to coordinate their access to the shared memory.

## Virtual Shared Memory

Virtual shared memory refers to a system where multiple processors have their own local memory modules, but they can access a common virtual address space that is mapped to the physical memory of different processors. Virtual shared memory systems are also known as distributed shared memory (DSM) or non-uniform memory access (NUMA) systems.

The advantages of virtual shared memory are:

- It can scale to a large number of processors and memory modules, as they are connected by a network rather than a shared bus or memory module. The network can provide higher bandwidth and lower contention than the shared bus or memory module.
- It can exploit the locality of reference, where processes access data that are close to their local memory more frequently than data that are far away. This can reduce the communication and synchronization overhead among processes.
- It can support heterogeneous processors and memory modules, where different processors can have different architectures, speeds, or capacities. This can increase the flexibility and performance of the system.

The disadvantages of virtual shared memory are:

- It requires software support for consistency, which ensures that all processes see a consistent view of the virtual shared memory. Consistency protocols can introduce additional complexity and overhead to the system.
- It can incur high-latency and low-bandwidth communication among processes, as they need to send messages over the network to access remote memory locations. The network can also introduce delays and failures to the communication.
- It can cause false sharing, where processes access different data that are mapped to the same physical memory location. This can trigger unnecessary communication and synchronization among processes.

There are different ways of implementing virtual shared memory, such as page-based, object-based, or tuple-based approaches. Each approach has its own advantages and disadvantages, depending on the granularity, distribution, and access patterns of the shared data.



# Logical Clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A logical clock is a mechanism for capturing chronological and causal relationships in a distributed system  .
- A distributed system may have no physically synchronous global clock, so a logical clock allows global ordering on events from different processes in such systems .
- A logical clock is not a physical device, but a software counter that is incremented according to some rules .
- A logical clock can be used for computation analysis, distributed algorithm design, individual event tracking, and exploring computational progress.
- Some examples of logical clock algorithms are:
  - Lamport timestamps, which are monotonically increasing software counters that are updated based on the send and receive events of messages .
  - Vector clocks, which are arrays of software counters that are updated based on the send, receive, and local events of processes  .
  - Matrix clocks, which are matrices of software counters that are updated based on the send, receive, and local events of processes and also capture the concurrency of events.
- The main properties of logical clocks are:
  - Consistency: If event A causally precedes event B, then the logical clock value of A is less than the logical clock value of B .
  - Accuracy: The logical clock values reflect the real-time order of events as closely as possible .
  - Efficiency: The logical clock algorithm should have low overhead in terms of time and space complexity .



# Lamport's Logical Clocks

- Lamport's logical clocks are a way of ordering events in a distributed system without relying on physical clocks or synchronization.
- Lamport's logical clocks are based on the idea of a **happens-before** relation, denoted by `->`, which captures the causal order of events.
- If `a` and `b` are events on the same process, then `a -> b` if `a` occurs before `b` based on the local clock.
- If `a` is the event of sending a message by one process and `b` is the event of receiving that message by another process, then `a -> b`.
- If `a -> b` and `b -> c`, then `a -> c`.
- Two events `a` and `b` are **concurrent**, denoted by `a || b`, if neither `a -> b` nor `b -> a`.
- Lamport's logical clocks assign a numerical value, called a **timestamp**, to each event that is consistent with the happens-before relation.
- A timestamp is a positive integer that represents the logical time of an event.
- Each process maintains a local logical clock, which is a counter that is incremented before each event on that process.
- When a process sends a message, it attaches its current logical clock value to the message.
- When a process receives a message, it updates its logical clock to be the maximum of its own clock and the timestamp in the message, and then increments it by one.
- Lamport's logical clocks ensure that if `a -> b`, then the timestamp of `a` is less than the timestamp of `b`.
- However, the converse is not true: if the timestamp of `a` is less than the timestamp of `b`, it does not imply that `a -> b`.
- Therefore, Lamport's logical clocks can only partially order events, and cannot distinguish between concurrent events.



# Concepts in Message Passing Systems

- Message passing is a technique for invoking behavior (i.e., running a program) on a computer.
- Message passing is used in distributed systems, where communication is carried out between processes by passing messages from one process to another .
- A message-passing system is a subsystem of a distributed operating system (DOS) that provides a set of message-based interprocess communication (IPC) protocols.
- A message-passing system can hide the complexities of sophisticated network protocols and many heterogeneous platforms from the programmers.
- A message-passing system can support different types of communication, such as synchronous or asynchronous, reliable or unreliable, point-to-point or multicast, etc.
- A message-passing system can also provide various features, such as message buffering, message ordering, message filtering, message encryption, message authentication, etc.
- A message-passing system can be implemented using different methods, such as sockets, remote procedure calls (RPCs), remote method invocation (RMI), message-oriented middleware (MOM), etc.
- A message-passing system can be evaluated based on its performance, scalability, fault-tolerance, security, and usability.



# Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by exchanging messages.
- In a distributed system, there is no global clock or shared memory, so the order of events is not always clear or consistent.
- Causal order is a partial order relation that captures the notion of potential causality between events in a distributed system.
- Causal order is based on Lamport's happened-before relation, which defines that event a happened before event b (denoted as a -> b) if one of the following conditions holds:
  - a and b are events in the same process, and a occurred before b in that process.
  - a is the sending of a message by one process, and b is the receipt of that message by another process.
  - there exists some event c such that a -> c and c -> b (transitivity).
- Causal order implies that if a -> b, then any process that observes b must also observe a, and in the same order. However, causal order does not impose any order on concurrent events, which are events that are not causally related (denoted as a || b).
- Causal order is useful for ensuring the consistency and correctness of distributed applications that rely on the causal dependencies between events, such as collaborative editing, social media, or distributed databases.
- Causal order can be implemented by various algorithms, such as vector clocks, causal broadcast, or causal memory. These algorithms use different mechanisms to track and enforce the causal dependencies between events, such as logical timestamps, message buffers, or version vectors.



# Total Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent entities that communicate by message passing and coordinate their actions to achieve a common goal.
- A distributed system can be characterized by various properties, such as scalability, fault tolerance, concurrency, transparency, heterogeneity, etc.
- One of the challenges of distributed systems is to deal with the uncertainty and inconsistency of the state of the system, which can arise due to failures, delays, or concurrency of events.
- An event is an occurrence that changes the state of an entity in the system. Events can be local (internal to an entity) or global (affecting multiple entities).
- A partial order is a binary relation that satisfies three properties: reflexivity, antisymmetry, and transitivity. A partial order can be used to compare some but not all events in the system.
- A total order is a binary relation that satisfies four properties: reflexivity, antisymmetry, transitivity, and totality. A total order can be used to compare all events in the system.
- A total order can be useful for ensuring consistency, agreement, and coordination among the entities in the system, such as for implementing mutual exclusion, atomic broadcast, consensus, etc.
- A total order can be established by using physical clocks, logical clocks, or vector clocks, which assign timestamps to events and allow them to be ordered according to some rules.
- A physical clock is a device that measures the passage of time based on some physical phenomenon, such as the rotation of the earth, the vibration of a quartz crystal, or the emission of a radio signal. Physical clocks can be synchronized by using algorithms such as NTP, GPS, or atomic clocks.
- A logical clock is an abstraction that assigns logical timestamps to events based on their causal relationships, rather than their actual occurrence times. Logical clocks can capture the happens-before relation, which is a partial order that defines the causal order of events in the system.
- A vector clock is an extension of a logical clock that assigns a vector of logical timestamps to each event, where each element of the vector represents the local logical clock of an entity in the system. Vector clocks can capture the concurrent relation, which is a partial order that defines the concurrent or independent events in the system.
- Lamport timestamps are a type of logical clock that assign a single scalar value to each event, based on the local logical clock of the entity that generates the event and the logical clocks of the entities that send messages to it. Lamport timestamps can be used to create a total order of events in the system by using some arbitrary mechanism to break ties (e.g. the ID of the process).



# Total Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent processes that communicate by exchanging messages over a network.
- Events are actions or occurrences that happen in a process, such as sending or receiving a message, executing a statement, or changing a state variable.
- The order of events in a distributed system is important for ensuring consistency, correctness, and coordination among the processes.
- A partial order is a relation that defines a precedence among some events, but not all. For example, if event A happens before event B in the same process, then A is partially ordered before B, denoted by A -> B. However, if event C happens in a different process, then there is no partial order relation between A and C or B and C, unless there is a causal dependency between them.
- A causal dependency is a relation that defines a cause-effect relationship between events. For example, if event A causes event B to happen, then A is causally dependent on B, denoted by A -> B. A causal dependency can be established by the following rules:
  - If A and B are events in the same process, and A happens before B, then A -> B.
  - If A is the event of sending a message m, and B is the event of receiving m, then A -> B.
  - If A -> B and B -> C, then A -> C (transitivity).
- A causal order is a relation that defines a partial order among all the events that are causally dependent on each other. For example, if A -> B and B -> C, then A, B, and C are causally ordered, denoted by A -> B -> C. A causal order preserves the logical time of events, meaning that if A -> B, then the logical time of A is less than the logical time of B.
- A total order is a relation that defines a precedence among all the events in the system, regardless of their causal dependency. For example, if A, B, and C are events in different processes, then a total order can assign a unique rank to each event, such as A < B < C or C < B < A. A total order imposes a global time of events, meaning that if A < B, then the global time of A is less than the global time of B.
- A total causal order is a relation that defines a total order among all the events that is consistent with the causal order. For example, if A -> B and B -> C, then a total causal order can assign a rank to each event, such as A < B < C or A < C < B, but not C < B < A or B < A < C. A total causal order preserves both the logical and the global time of events, meaning that if A -> B, then the logical and the global time of A are less than the logical and the global time of B.
- A total causal order is the strictest ordering in distributed systems; it establishes only one linearization, consistent with the causal ordering, among all the events that occur in the system, even those that occur concurrently. For that reason, the execution of the system is considered as synchronous.
- A total causal order can be implemented by using a logical clock, such as a vector clock, that assigns a timestamp to each event, such that if A -> B, then the timestamp of A is less than the timestamp of B. Alternatively, a total causal order can be implemented by using a total order broadcast, a communication primitive that delivers the same sequence of messages to all the processes in the system.



# Techniques for Message Ordering in Distributed Systems

A distributed system is one whose components are on different computers connected by a network. These computers send messages to each other to talk to each other and coordinate their actions. The order in which messages are processed determines the final outcome of the actions in any distributed system. This is actually more difficult than it appears to be, because messages may be delayed, lost, or reordered by the network, and different processes may have different views of the system state and the message order.

There are different techniques for message ordering in distributed systems, depending on the desired properties and guarantees of the communication. Some of the common techniques are:

- **Non-FIFO ordering**: This is the simplest and most basic technique, where messages are delivered in any order, regardless of the order they were sent. This technique does not provide any guarantee of message ordering, and it may lead to inconsistent or incorrect results in some applications. For example, if a process sends two messages A and B to another process, and the receiver processes B before A, it may violate the causal or logical order of the events.

- **FIFO ordering**: This technique ensures that messages sent by the same sender are delivered in the order they were sent. This technique provides a stronger guarantee than non-FIFO ordering, and it prevents some inconsistencies or errors in some applications. For example, if a process sends two messages A and B to another process, and the receiver processes A before B, it preserves the chronological order of the events. However, FIFO ordering does not guarantee that messages sent by different senders are delivered in any particular order, and it may still violate the causal or logical order of the events in some cases. For example, if a process sends a message A to another process, and then receives a message B from a third process, and then forwards B to the second process, FIFO ordering does not ensure that the second process receives A before B, even though A causally precedes B.

- **Causal ordering**: This technique ensures that messages that are causally related are delivered in the same order by all processes. Two messages are causally related if one message is sent or received as a result of another message being sent or received. This technique provides a stronger guarantee than FIFO ordering, and it prevents any violation of the causal or logical order of the events in any application. For example, if a process sends a message A to another process, and then receives a message B from a third process, and then forwards B to the second process, causal ordering ensures that the second process receives A before B, because A causally precedes B . However, causal ordering does not guarantee that messages that are not causally related are delivered in any particular order, and it may still allow some inconsistencies or errors in some applications. For example, if two processes send two messages A and B to a third process, and A and B are not causally related, causal ordering does not ensure that the third process receives A before B or B before A, even though one order may be more desirable or correct than the other.

- **Synchronous ordering**: This technique ensures that messages are delivered in the same order by all processes, regardless of whether they are causally related or not. This technique provides the strongest guarantee of message ordering, and it prevents any inconsistency or error in any application. For example, if two processes send two messages A and B to a third process, and A and B are not causally related, synchronous ordering ensures that the third process receives A before B or B before A, and that all other processes receive them in the same order. However, synchronous ordering is also the most expensive and difficult technique to implement, because it requires global synchronization and agreement among all processes, which may be impractical or impossible in some distributed systems.

These techniques can be implemented using different protocols, such as timestamps, vector clocks, logical clocks, sequence numbers, acknowledgments, etc. The choice of the technique and the protocol depends on the requirements and the characteristics of the distributed system and the application.



# Causal ordering of messages

- Causal ordering of messages is a partial ordering of messages in a distributed computing environment .
- It places a restriction on communication between processes by requiring that if the transmission of message mi to process pk necessarily preceded the transmission of message mj to the same process, then the delivery of these messages to that process must be ordered such that mi is delivered before mj .
- Causal ordering of messages is one of the four semantics of multicast communication, namely unordered, totally ordered, causal, and sync-ordered communication.
- Multicast communication methods vary according to the message’s reliability guarantee and ordering guarantee.
- Causal ordering of messages is based on the notion of potential causality, which is defined by Lamport's happened-before relation .
- The happened-before relation, denoted by ->, is a transitive, irreflexive, and antisymmetric relation that captures the causal dependencies between events in a distributed system .
- The happened-before relation is defined as follows :
  - If a and b are events in the same process, and a occurs before b, then a -> b.
  - If a is the event of sending a message by one process and b is the event of receiving the same message by another process, then a -> b.
  - If a -> b and b -> c, then a -> c.
- Causal ordering of messages ensures that if a message m1 causes another message m2, then m1 is delivered before m2 at every process that receives both messages .
- Causal ordering of messages can be implemented by various algorithms, such as vector clocks, causal broadcast, and causal multicast  .
- Vector clocks are logical clocks that assign a vector of timestamps to each event, such that the vector reflects the causal history of the event .
- Causal broadcast is a communication primitive that delivers messages to all processes in the same causal order .
- Causal multicast is a communication primitive that delivers messages to a subset of processes in the same causal order .
- Causal ordering of messages is useful for applications that require consistency and coordination among distributed processes, such as collaborative editing, distributed databases, and replicated state machines .



# Global State for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent processes that communicate through message passing.
- The state of a process is the values of its variables and registers at a given point in time.
- The state of a channel is the sequence of messages that have been sent but not yet received on that channel.
- The global state of a distributed system is the union of the states of the individual processes and channels.
- A global state is consistent if it reflects a possible execution of the system, i.e., no causal violations occur.
- A causal violation is when a message is received before it is sent, according to the global state.
- A cut is a partition of the set of events in the system into two subsets: past and future.
- A cut is consistent if it respects the causal order of events, i.e., no message crosses the cut from future to past.
- A snapshot is a mechanism to record a consistent global state of a distributed system.
- A snapshot algorithm is a distributed protocol that allows each process to record its local state and the state of its incoming channels, such that the resulting global state is consistent.
- A snapshot algorithm is correct if it satisfies the following properties:
  - Termination: every process eventually records its state and terminates the algorithm.
  - Consistency: the recorded global state is consistent.
  - Local: no process needs to record the state of another process or an outgoing channel.
- A snapshot algorithm can be used for various purposes, such as:
  - Checkpointing: saving the global state of the system for recovery purposes.
  - Monitoring: observing the global state of the system for debugging or performance analysis.
  - Global predicate evaluation: checking whether a global property holds in the system.



# Termination Detection for Distributed Systems

Termination detection is the problem of determining if a distributed computation has finished. This is a fundamental and non-trivial problem in distributed systems, because no process has complete knowledge of the global state, and global time does not exist. Termination detection is useful for many applications, such as garbage collection, deadlock detection, load balancing, and distributed debugging.

One of the algorithms for termination detection is Huang's algorithm, proposed by Shing-Tsaan Huang in 1989. The algorithm is based on the concept of a process' state in a distributed system. A process can be either active or idle at any given point of time. An active process may become idle at any time, but an idle process may only become active again upon receiving a computational message, which is a message that affects the local state of the process. A distributed computation terminates when all processes are idle and there are no computational messages in transit.

Huang's algorithm works as follows:

- Each process maintains a counter, called the control message count (CMC), which is initially zero. The CMC represents the number of control messages sent minus the number of control messages received by the process. A control message is a message that is used for termination detection, such as a probe or a reply.
- Each process also maintains a boolean variable, called the active flag, which indicates whether the process is active or idle. The active flag is initially true for all processes.
- The algorithm assumes a spanning tree of processes, rooted at a designated initiator process. The initiator process starts the termination detection by sending a probe message to all its children in the spanning tree. The probe message contains the CMC and the active flag of the initiator process.
- When a process receives a probe message, it updates its CMC by adding the CMC of the probe message to its own CMC. It also updates its active flag by performing a logical OR operation with the active flag of the probe message. Then, it sends a probe message to all its children in the spanning tree, with its updated CMC and active flag. If the process has no children, it sends a reply message to its parent in the spanning tree, with its updated CMC and active flag.
- When a process receives a reply message from a child, it updates its CMC by adding the CMC of the reply message to its own CMC. It also updates its active flag by performing a logical OR operation with the active flag of the reply message. Then, it checks if it has received a reply message from all its children. If so, it sends a reply message to its parent in the spanning tree, with its updated CMC and active flag. If the process is the initiator, it checks if its CMC is zero and its active flag is false. If so, it declares termination. Otherwise, it starts a new round of termination detection by sending a probe message to all its children.

The algorithm guarantees that termination will be detected if it occurs, and that no false termination will be declared. The algorithm also preserves the correctness of the underlying computation, as it does not interfere with the computational messages. The algorithm requires O(n) messages per round, where n is the number of processes in the system. The algorithm also requires O(log n) bits per message, where n is the number of processes in the system. The algorithm terminates in O(d) rounds, where d is the diameter of the spanning tree.



## Unit 2 - Distributed Mutual Exclusion

- Distributed mutual exclusion is a fundamental problem in distributed computing systems  .
- It ensures that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner  .
- It states that only one process is allowed to execute the critical section (CS) at any given time  .
- A critical section is an interval of time where a process accesses a shared resource or data.
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion . Message passing is the sole means for implementing distributed mutual exclusion.
- There are three basic approaches for implementing distributed mutual exclusion:
  - Token-based algorithms: A process can enter the CS only if it possesses a unique token. The token is passed among the processes in a predefined order or based on some request messages.
  - Permission-based algorithms: A process can enter the CS only if it obtains permission from all or a subset of the other processes in the system. The permission is granted or denied based on some logical clocks or timestamps.
  - Quorum-based algorithms: A process can enter the CS only if it obtains permission from a majority or a quorum of the processes in the system. The quorum can be dynamically or statically defined.
- The performance of distributed mutual exclusion algorithms can be measured by the following metrics:
  - Message complexity: The number of messages exchanged per CS execution.
  - Synchronization delay: The time elapsed between the instant a process requests the CS and the instant it is granted the CS.
  - System throughput: The number of times the CS is executed per unit time in the system.



# Classification of Distributed Mutual Exclusion

Distributed mutual exclusion is a problem of ensuring that only one process in a distributed system can access a shared resource or data at a time. It is a fundamental requirement for achieving consistency, coordination, and synchronization in distributed systems.

There are three basic approaches for implementing distributed mutual exclusion:

- **Token-based approach**: A unique token is shared among the processes. A process can enter its critical section (CS) only if it possesses the token. Mutual exclusion is ensured because the token is unique. The token is passed from one process to another according to some algorithm. Examples of token-based algorithms are Ricart-Agrawala algorithm, Suzuki-Kasami algorithm, and Raymond's algorithm.
- **Non-token-based approach**: There is no token in this approach. Instead, a process requests permission from other processes to enter its CS. The other processes reply with their consent or denial. A process can enter its CS only if it receives consent from all or a majority of the other processes. Examples of non-token-based algorithms are Lamport's algorithm, Ricart-Agrawala algorithm, and Maekawa's algorithm.
- **Quorum-based approach**: This is a variation of the non-token-based approach. A process requests permission from a subset of processes, called a quorum, to enter its CS. A process can enter its CS only if it receives consent from all the processes in the quorum. The quorum is chosen such that any two quorums have at least one process in common. This ensures mutual exclusion. Examples of quorum-based algorithms are Maekawa's algorithm, Sankaranarayanan and Ricart's algorithm, and Agrawala and El Abbadi's algorithm.

The performance of distributed mutual exclusion algorithms can be evaluated based on the following metrics:

- **Message complexity**: The number of messages exchanged per CS execution.
- **Synchronization delay**: The time elapsed between a process requesting the CS and entering the CS.
- **System throughput**: The number of CS executions per unit time in the system.
- **Fault tolerance**: The ability of the algorithm to handle failures of processes or communication links.



# Requirement of mutual exclusion theorem for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM

- Mutual exclusion is a concurrency control property which is introduced to prevent race conditions.
- Race conditions occur when multiple processes access a shared resource or data simultaneously and at least one of them modifies it.
- Mutual exclusion ensures that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner  .
- Mutual exclusion in a distributed system states that only one process is allowed to execute the critical section (CS) at any given time  .
- A critical section is a segment of code that accesses a shared resource or data.
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion .
- Message passing is the sole means for implementing distributed mutual exclusion .
- There are three basic approaches for implementing distributed mutual exclusion :
  - Token-based algorithms: A process can enter the CS only if it possesses a unique token that is passed among the processes in a logical ring or a tree .
  - Permission-based algorithms: A process can enter the CS only if it receives permission messages from all or a subset of other processes in the system .
  - Quorum-based algorithms: A process can enter the CS only if it receives permission messages from a majority or a weighted majority of other processes in the system .
- The requirement of mutual exclusion theorem is to ensure the correctness and consistency of the distributed system by avoiding race conditions, data corruption, and deadlock.



# Token based and non token based algorithms for distributed mutual exclusion

Distributed mutual exclusion (DME) is the problem of ensuring that only one process at a time can access a shared resource in a distributed system. There are two main approaches to solve this problem: token based and non token based algorithms.

## Token based algorithms

In token based algorithms, a unique token is shared among all the processes in the system. The token represents the permission to enter the critical section. A process can enter the critical section only if it has the token. The token is passed from one process to another according to some protocol.

Some examples of token based algorithms are:

- **Suzuki-Kasami algorithm**: This algorithm uses a token that contains a vector of sequence numbers, indicating the latest request of each process. The token is sent to the process with the highest sequence number in the vector. The process that has the token can enter the critical section multiple times without releasing the token, until it receives a higher request from another process.
- **Raymond's algorithm**: This algorithm organizes the processes in a logical tree structure. The token is initially held by the root of the tree. A process that wants to enter the critical section sends a request message to its parent in the tree. The parent forwards the request to the token holder, if it is not the token holder itself. The token holder sends the token to the requester along the path of the request messages. The process that has the token can enter the critical section and becomes the new root of the tree.

## Non token based algorithms

In non token based algorithms, a process communicates with a set of other processes to determine who should enter the critical section next. The communication is done using messages such as REQUEST, REPLY, and RELEASE. The processes use timestamps or logical clocks to order the requests and to resolve conflicts.

Some examples of non token based algorithms are:

- **Lamport's algorithm**: This algorithm uses logical clocks to assign timestamps to the requests. A process that wants to enter the critical section broadcasts a REQUEST message with its timestamp to all other processes. It waits for a REPLY message from each process, indicating that they have received the request and they are not in the critical section or have a higher priority request. The process with the smallest timestamp has the highest priority. After entering and exiting the critical section, the process broadcasts a RELEASE message to all other processes.
- **Ricart-Agrawala algorithm**: This algorithm is an improvement of Lamport's algorithm that reduces the number of messages. A process that wants to enter the critical section broadcasts a REQUEST message with its timestamp to all other processes. It waits for a REPLY message from each process that has a lower priority request or is not interested in the critical section. A process that has a higher priority request defers its REPLY until it exits the critical section or gives up its request. After entering and exiting the critical section, the process sends a REPLY message to all the deferred requests.



# Performance Metric for Distributed Mutual Exclusion Algorithms

- Distributed mutual exclusion algorithms are algorithms that ensure that only one process can access a shared resource or execute a critical section at a time in a distributed system.
- The performance of distributed mutual exclusion algorithms can be evaluated by the following four metrics :
  - **Message complexity**: It is the number of messages that are required per critical section execution by a process. It reflects the communication overhead and network congestion caused by the algorithm. A lower message complexity is desirable.
  - **Synchronization delay**: It is the time elapsed between the departure of a process from the critical section and the entry of the next process into the critical section. It reflects the degree of concurrency and fairness achieved by the algorithm. A lower synchronization delay is desirable.
  - **Response time**: It is the time interval between the request of a process to enter the critical section and the end of its critical section execution. It reflects the waiting time and the service time experienced by the process. A lower response time is desirable.
  - **Throughput**: It is the number of critical section executions per unit time in the system. It reflects the efficiency and utilization of the shared resource by the algorithm. A higher throughput is desirable.
- Different distributed mutual exclusion algorithms may have different performance in terms of these metrics, depending on the system model, the network topology, the request pattern, and the failure scenarios. Some examples of distributed mutual exclusion algorithms are :
  - **Central server algorithm**: One process acts as the coordinator and grants access to the critical section to other processes based on a FIFO queue. The message complexity is 3 messages per critical section execution. The synchronization delay is one message transmission time. The response time depends on the queue length and the network delay. The throughput depends on the coordinator's processing speed and the network bandwidth.
  - **Token ring algorithm**: A unique token is circulated among the processes in a logical ring. A process can enter the critical section only if it holds the token. The message complexity is 1 message per critical section execution. The synchronization delay is the token circulation time. The response time depends on the token position and the network delay. The throughput depends on the token circulation speed and the network bandwidth.
  - **Ricart-Agrawala algorithm**: A process broadcasts its request to enter the critical section to all other processes and waits for their replies. A process replies to a request only if it is not in the critical section or it has a lower priority. The message complexity is 2(N-1) messages per critical section execution, where N is the number of processes. The synchronization delay is zero. The response time depends on the network delay and the priority of the requests. The throughput depends on the network bandwidth and the degree of contention.



## Unit 3 - Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set, and none of the processes can proceed or release the resources.
- Deadlocks can occur in distributed systems when distributed transactions or concurrency control are utilized.
- Deadlock detection is one of the strategies to deal with deadlocks, where the system periodically checks for the existence of deadlocks and resolves them by aborting one or more processes.
- Deadlock detection in distributed systems entails two basic issues: detection of existing deadlocks and resolution of detected deadlocks.
- Detection of existing deadlocks requires examining the status of process-resource interactions for the presence of cyclic wait.
- Resolution of detected deadlocks requires choosing a suitable victim process to abort and recover the resources.
- Deadlock detection in distributed systems can be performed using either a centralized or a distributed approach.
- In the centralized approach, a designated node (called the deadlock detector) collects the local wait-for graphs from all the nodes and constructs a global wait-for graph to detect cycles.
- In the distributed approach, a distributed algorithm (such as edge chasing) is used to propagate probe messages along the wait-for edges and detect cycles.
- The advantages of the centralized approach are simplicity and efficiency, while the disadvantages are single point of failure and communication overhead.
- The advantages of the distributed approach are fault tolerance and scalability, while the disadvantages are complexity and message overhead.



# System Model for Distributed Deadlock Detection

- A distributed system consists of a collection of processes that communicate and share resources over a network.
- A deadlock is a situation where a set of processes are blocked waiting for resources that are held by other processes in the set.
- Distributed deadlock detection is the problem of finding and resolving deadlocks in a distributed system.
- There are three main approaches to distributed deadlock detection: centralized, hierarchical, and distributed.

## Centralized Approach

- In the centralized approach, one node is designated as the deadlock detector and collects information about the resource allocation and requests from all other nodes.
- The deadlock detector constructs a global wait-for graph (WFG) from the local WFGs of each node and checks for cycles in the graph.
- A cycle in the WFG indicates a deadlock and the deadlock detector can initiate a recovery action, such as aborting or preempting one or more processes in the cycle.
- The advantages of the centralized approach are simplicity and efficiency, as only one node needs to perform the deadlock detection algorithm.
- The disadvantages of the centralized approach are the single point of failure and the communication overhead, as the deadlock detector needs to receive and process messages from all other nodes.

## Hierarchical Approach

- In the hierarchical approach, the nodes are organized into a tree structure, where each node is responsible for a subset of nodes or clusters.
- Each node maintains a local WFG for its cluster and periodically sends it to its parent node in the tree.
- The parent node merges the WFGs from its children and sends the merged WFG to its parent, and so on, until the root node receives the global WFG.
- The root node performs the deadlock detection algorithm on the global WFG and notifies the nodes involved in the deadlock.
- The advantages of the hierarchical approach are fault tolerance and scalability, as the system can tolerate the failure of some nodes and can handle a large number of nodes by increasing the levels of the tree.
- The disadvantages of the hierarchical approach are the complexity and the delay, as the deadlock detection algorithm requires multiple steps and messages to reach the root node and the deadlock may persist for a long time before being detected.

## Distributed Approach

- In the distributed approach, each node participates in the deadlock detection algorithm without relying on a central or hierarchical coordinator.
- There are two main techniques for the distributed approach: edge chasing and probe-based.
- Edge chasing is a technique where each node sends a probe message along the edges of the WFG to detect cycles.
- A probe message contains the identity of the sender and the sequence of nodes it has visited.
- If a node receives a probe message that contains its own identity, it means that a cycle has been detected and a deadlock exists.
- Probe-based is a technique where each node periodically initiates a probe message to check the status of its outgoing edges in the WFG.
- A probe message contains the identity of the initiator and a timestamp.
- If a node receives a probe message, it compares the timestamp with its own and replies with either a positive or a negative acknowledgment.
- A positive acknowledgment means that the node is waiting for a resource that is held by another node and a negative acknowledgment means that the node is not waiting for any resource or has acquired the resource since the probe was initiated.
- If the initiator receives a positive acknowledgment from all its outgoing edges, it means that it is involved in a deadlock and can take a recovery action.
- The advantages of the distributed approach are the absence of a single point of failure and the reduced communication overhead, as the nodes only communicate with their neighbors in the WFG.
- The disadvantages of the distributed approach are the possibility of false or phantom deadlocks and the difficulty of coordinating the recovery actions, as the nodes may have inconsistent or incomplete views of the global WFG.



# Resource Vs Communication Deadlocks

- A deadlock is a condition where a process cannot proceed because it needs to obtain a resource held by another process, and it itself is holding a resource that the other process needs.
- There are two types of deadlocks in distributed systems: resource deadlocks and communication deadlocks.
- Resource deadlocks occur when processes access resources, such as data objects in database systems and buffers in store and forward communication networks. A process acquires a resource before accessing it and releasing it after using it.
- Communication deadlocks occur when processes exchange messages, such as in message passing systems and distributed algorithms. A process sends a message to another process and waits for a reply before continuing.
- The main difference between resource deadlocks and communication deadlocks is that in resource deadlocks, the resources are held by the processes until they are released, whereas in communication deadlocks, the resources are the messages themselves, which are consumed by the processes when they are received.
- Another difference is that resource deadlocks can be detected by analyzing the resource allocation graph, which shows the processes and the resources they request and hold, whereas communication deadlocks can be detected by analyzing the wait-for graph, which shows the processes and the messages they send and wait for.
- A third difference is that resource deadlocks can be prevented by using techniques such as deadlock avoidance, deadlock prevention, and deadlock detection and recovery, whereas communication deadlocks can be prevented by using techniques such as timeouts, acknowledgments, and logical clocks.



# Deadlock Prevention for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process. In a distributed system, deadlocks can occur across multiple nodes and resources, making them harder to detect and resolve.

Deadlock prevention is a technique to avoid the occurrence of deadlocks by imposing some constraints on how processes can request and acquire resources. There are two main methods of deadlock prevention in a distributed system:

- Ordered request: In this method, each resource type is assigned a certain level to maintain a resource request policy for a process. This is known as the resource allocation policy. A process can request resources only in an increasing order of levels. For example, if a process needs resources A, B, and C, and their levels are 1, 2, and 3 respectively, then the process must request A first, then B, and then C. This prevents circular wait condition, which is one of the necessary conditions for deadlock.

- Collective request: In this method, a process must request all the resources it needs at the same time before starting execution. This is known as the atomic allocation policy. A process can either get all the resources it needs or none of them. This prevents hold and wait condition, which is another necessary condition for deadlock.

Both methods have some advantages and disadvantages. Ordered request method allows more concurrency and flexibility, but it may cause resource starvation and waste. Collective request method avoids resource starvation and waste, but it may cause low resource utilization and long waiting time. Therefore, the choice of the method depends on the characteristics of the system and the application.



# Avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- Avoidance is a technique to prevent deadlocks from occurring in a distributed system by ensuring that the system is always in a safe state.
- A safe state is a state where there is at least one sequence of resource allocation that does not lead to a deadlock.
- Avoidance requires the system to have some knowledge of the current and future resource requests and releases of each process.
- Avoidance is impractical in distributed systems due to several problems, such as:
  - The lack of global information and synchronization among processes and sites.
  - The uncertainty and unpredictability of resource requests and releases in a dynamic and heterogeneous environment.
  - The high overhead and complexity of maintaining and updating the global state of the system.
- Therefore, avoidance is rarely used in distributed systems, and deadlock detection is preferred as a more feasible and realistic approach.



# Detection and Resolution of Distributed Deadlocks

- A distributed deadlock is a situation where a set of processes in a distributed system are waiting for each other to release resources or messages, and none of them can proceed.
- Detection and resolution of distributed deadlocks involve two steps: first, identifying the existence of deadlocks in the system, and second, breaking the cycles of dependency among the deadlocked processes.
- Detection of distributed deadlocks requires the following properties:
  - Progress: the method should be able to detect all the deadlocks in the system.
  - Safety: the method should not detect false or phantom deadlocks, which are cycles that do not involve any real dependency.
- There are three main approaches to detect distributed deadlocks, based on the representation and maintenance of the wait-for graph (WFG), which is a directed graph that shows the dependency relationships among the processes and resources in the system:
  - Centralized approach: a single designated node collects the information about the WFG from all the other nodes, and periodically searches the WFG for cycles. This approach is simple and efficient, but it has a single point of failure and a high communication overhead.
  - Distributed approach: each node maintains a local WFG that reflects its own dependency relationships, and exchanges messages with other nodes to detect global cycles. This approach is fault-tolerant and scalable, but it has a high complexity and a high message overhead.
  - Hierarchical approach: the nodes are organized into a hierarchy of clusters, and each cluster has a coordinator that maintains a partial WFG for its cluster. The coordinators communicate with each other to detect global cycles. This approach is a compromise between the centralized and distributed approaches, but it has a high coordination overhead and a variable detection time.
- Resolution of distributed deadlocks involves breaking the existing wait-for dependencies in the WFG, by aborting or preempting some of the deadlocked processes and releasing their resources or messages to the blocked processes. The resolution of distributed deadlocks requires the following properties:
  - Effectiveness: the method should be able to resolve all the deadlocks in the system.
  - Efficiency: the method should minimize the number of processes aborted or preempted, and the amount of resources or messages wasted.
  - Fairness: the method should not favor or penalize any process or node unfairly.
- There are two main strategies to resolve distributed deadlocks, based on the timing and the scope of the resolution:
  - Eager strategy: the resolution is performed as soon as a deadlock is detected, and it involves all the processes in the cycle. This strategy is proactive and simple, but it may abort or preempt more processes than necessary, and it may cause cascading aborts or preemptions.
  - Lazy strategy: the resolution is delayed until a deadlock affects the system performance, and it involves only a subset of processes in the cycle. This strategy is reactive and selective, but it may increase the deadlock detection time and complexity, and it may cause starvation or livelock.



# Centralized Deadlock Detection

- Centralized deadlock detection is a technique used in distributed systems to handle deadlock detection by maintaining a global wait-for graph in a single chosen site, called the deadlock-detection coordinator.
- The coordinator collects information about the local wait-for graphs of each site and constructs the global wait-for graph by merging them.
- The coordinator periodically runs a cycle detection algorithm on the global wait-for graph to detect deadlocks.
- If a deadlock is detected, the coordinator selects a victim process to abort and sends a message to the corresponding site to terminate it.
- The advantages of centralized deadlock detection are simplicity, low communication overhead, and easy implementation.
- The disadvantages of centralized deadlock detection are single point of failure, scalability issues, and lack of autonomy.



# Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set.
- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems.
- Deadlock detection in distributed systems entails addressing two basic issues: detection of existing deadlocks and resolution of detected deadlocks.
- Deadlock detection requires examination of the status of process-resource interactions for presence of cyclic wait.
- Deadlock resolution requires aborting one or more deadlocked processes to break the cycle and release the resources.
- There are three approaches to detect deadlocks in distributed systems:
  - Centralized approach: A designated node collects the local wait-for graphs from all the nodes and constructs a global wait-for graph to detect cycles.
  - Distributed approach: A distributed algorithm is used to propagate the deadlock information among the nodes and detect cycles without constructing a global wait-for graph.
  - Hierarchical approach: The nodes are organized into a hierarchy of clusters and each cluster has a coordinator that collects the local wait-for graphs and detects cycles within the cluster. The coordinators communicate with each other to detect global cycles.
- Each approach has its advantages and disadvantages in terms of communication cost, detection latency, accuracy, and scalability.



# Path Pushing Algorithms

- Path pushing algorithms detect distributed deadlocks by maintaining an explicit global wait-for graph (WFG) at each site of the distributed system .
- The global WFG is constructed by merging the local WFGs of each site, which represent the waiting relationships among the processes at that site .
- Whenever a site performs a deadlock computation, it sends its local WFG to all its neighboring sites, which then update their global WFGs accordingly .
- A site can initiate a deadlock computation either periodically or when a new edge is added to its local WFG .
- A site can detect a deadlock by finding a cycle in its global WFG that involves one of its local processes .
- The advantages of path pushing algorithms are that they can detect deadlocks quickly and accurately, and that they do not require any special messages to be exchanged among the sites .
- The disadvantages of path pushing algorithms are that they require a lot of storage space and communication bandwidth to maintain and update the global WFGs, and that they may generate false positives if the global WFGs are not consistent .



# Edge Chasing Algorithms

- Edge chasing algorithms are a class of distributed deadlock detection algorithms that use special messages called probes to trace the dependency graph of processes and resources in a distributed system.
- A probe is a triplet (i, j, k) that denotes that the deadlock detection is initiated by process P_i and the message is being sent by the home site of process P_j to the home site of process P_k.
- The probe message follows the edges of the dependency graph from the waiting processes to the blocking processes until either a cycle is detected or all the edges are traversed.
- A cycle is detected when a probe message returns to the initiator process or when a process receives a probe message with its own identifier in the triplet.
- The most well-known edge chasing algorithm is the Chandy-Misra-Haas algorithm, which works for the AND request model, where a process can request multiple resources simultaneously and wait for all of them to be granted.
- The Chandy-Misra-Haas algorithm works as follows:

  - Each process maintains a wait-for graph that contains the processes and resources that it is waiting for and the processes and resources that are waiting for it.
  - When a process P_i initiates a deadlock detection, it sends a probe message (i, i, j) to the home site of each process P_j that it is waiting for.
  - When a process P_j receives a probe message (i, k, j), it checks if it is involved in a deadlock with P_i. If yes, it sends a reply message to P_i indicating the deadlock. If no, it forwards the probe message (i, j, l) to the home site of each process P_l that it is waiting for.
  - When a process P_i receives a reply message from P_j, it knows that there is a deadlock involving P_i and P_j and possibly other processes. It can then take appropriate actions to resolve the deadlock, such as aborting or preempting some processes or resources.



## Unit 4 - Agreement Protocols

- Agreement protocols are a class of distributed algorithms that allow a set of processes to reach a common decision or consensus, despite the possibility of failures or communication delays.
- Agreement protocols are useful for implementing fault-tolerant services, such as distributed databases, replicated state machines, leader election, atomic broadcast, etc.
- The main challenges of designing agreement protocols are:
  - Dealing with asynchrony: The processes and the network may have arbitrary delays, making it hard to synchronize or order events.
  - Dealing with failures: The processes may crash or behave maliciously (Byzantine failures), making it hard to trust or coordinate with them.
  - Dealing with uncertainty: The processes may have incomplete or inconsistent information, making it hard to agree on a common value or action.
- The main properties of agreement protocols are:
  - Validity: The value decided by the processes must be one of the values proposed by them.
  - Agreement: All correct processes must decide the same value.
  - Termination: All correct processes must eventually decide a value.
- Depending on the type and number of failures, the network model, and the assumptions made, different agreement protocols may have different trade-offs in terms of efficiency, complexity, and feasibility.
- Some examples of agreement protocols are:
  - Paxos: A family of protocols that achieve consensus in a partially synchronous network with crash failures, using a quorum-based approach and a leader-based optimization.
  - Raft: A protocol that achieves consensus in a partially synchronous network with crash failures, using a simpler and more understandable design than Paxos, based on leader election and log replication.
  - Byzantine Generals: A protocol that achieves consensus in a synchronous network with Byzantine failures, using a recursive majority voting scheme and digital signatures.
  - Practical Byzantine Fault Tolerance (PBFT): A protocol that achieves consensus in a partially synchronous network with Byzantine failures, using a view-based approach and a three-phase commit protocol.



# Introduction for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- Agreement protocols are a class of protocols that allow a set of distributed processes to reach a common decision or consensus on some value or action, despite the possibility of failures or malicious behavior.
- Agreement protocols are essential for ensuring the correctness and consistency of distributed systems, especially in the presence of faults or attacks.
- Some examples of agreement problems are:
  - Leader election: electing a unique coordinator or leader among a group of processes.
  - Atomic commit: ensuring that a set of transactions are either all committed or all aborted in a distributed database.
  - Consensus: agreeing on a single value among a set of proposed values.
  - Byzantine agreement: agreeing on a single value among a set of proposed values, even if some processes are faulty or malicious and may lie or send conflicting messages.
- Agreement protocols can be classified based on the following criteria:
  - Synchronous vs asynchronous: whether the processes and the communication channels have bounded delays or not.
  - Crash vs Byzantine: whether the processes can only fail by crashing or they can exhibit arbitrary behavior.
  - Deterministic vs randomized: whether the protocol always produces the same output for the same input or it can use randomization to achieve a probabilistic guarantee.
  - Message complexity: the number of messages exchanged by the protocol.
  - Time complexity: the number of rounds or steps required by the protocol.
- The main challenges and trade-offs in designing agreement protocols are:
  - Fault tolerance: the ability to cope with failures or attacks and still reach a correct agreement.
  - Consistency: the property that all correct processes agree on the same value or action.
  - Termination: the property that all correct processes eventually decide on a value or action.
  - Liveness: the property that the protocol makes progress and does not get stuck in an infinite loop or deadlock.
  - Efficiency: the minimization of the message and time complexity of the protocol.



# System Models for Distributed Systems

A system model is a simplified representation of the properties and behavior of a distributed system. It helps to reason about the system and design algorithms and protocols that can cope with the challenges of distributed computing, such as concurrency, failures, and heterogeneity.

There are different types of system models that capture different aspects of a distributed system, such as:

- **Architectural models**: These models describe the structure and organization of the system components and their interactions. They can be classified into two main categories: client-server models and peer-to-peer models. Client-server models are based on the idea of having one or more servers that provide services to multiple clients that request them. Peer-to-peer models are based on the idea of having a network of nodes that cooperate and share resources without any central authority or hierarchy.
- **Interaction models**: These models describe the communication and coordination mechanisms used by the system components. They can be classified into two main categories: synchronous models and asynchronous models. Synchronous models assume that there are bounds on the message transmission delays, the processing speeds, and the clock drifts of the nodes. Asynchronous models do not make any such assumptions and allow for arbitrary delays, speeds, and drifts. Synchronous models are easier to reason about, but less realistic and robust than asynchronous models.
- **Fault models**: These models describe the types and frequency of failures that can occur in the system. They can be classified into two main categories: crash models and Byzantine models. Crash models assume that nodes can only fail by stopping and not responding to any messages. Byzantine models assume that nodes can fail in arbitrary ways, such as sending incorrect or malicious messages, or colluding with other faulty nodes. Byzantine models are more general and realistic, but also more difficult to cope with than crash models.

One of the main challenges of distributed systems is to achieve agreement among the nodes on some common value or decision, despite the presence of failures and uncertainties. This problem is known as **consensus** and it is fundamental for many applications, such as distributed databases, replication, leader election, and atomic broadcast.

There are different consensus algorithms that can solve the problem under different system models. For example, Paxos and Raft are two popular consensus algorithms that assume a partially synchronous and crash-recovery system model, meaning that the system is asynchronous most of the time, but eventually becomes synchronous, and that nodes can recover from crashes and rejoin the system. These algorithms can tolerate up to half of the nodes being faulty.

Another example is the Byzantine Generals Problem, which is a variant of consensus that assumes a synchronous and Byzantine system model, meaning that the system has bounded delays and speeds, but nodes can behave arbitrarily. This problem can be solved by using cryptographic techniques, such as digital signatures and hash functions, to ensure the authenticity and integrity of the messages. This problem can tolerate up to one third of the nodes being faulty.



# Classification of Agreement Problem in Distributed Systems

An agreement problem in a distributed system is a problem where a set of processes need to agree on a common value or decision, despite the possibility of failures, communication delays, or malicious behavior. Agreement problems are fundamental to achieving fault tolerance and consistency in distributed systems.

There are different types of agreement problems, depending on the assumptions and requirements of the system. Some of the well-known agreement problems are:

- **Byzantine agreement problem**: A single value, which is to be agreed on, is initialized by an arbitrary process and all non-faulty processes have to agree on that value. The processes may be subject to Byzantine failures, which means they can behave arbitrarily or maliciously, and send conflicting or incorrect messages to other processes. The goal is to ensure that all non-faulty processes agree on the same value, and that value is the initial value of some non-faulty process. This problem is also known as the Byzantine generals problem .

- **Consensus problem**: A generalization of the Byzantine agreement problem, where each process can propose its own initial value, and all non-faulty processes have to agree on a common value. The value agreed on must be one of the proposed values. The processes may be subject to different types of failures, such as crash failures, omission failures, or Byzantine failures. The goal is to ensure that all non-faulty processes agree on the same value, and that value satisfies some validity condition .

- **Interactive consistency problem**: A variation of the Byzantine agreement problem, where each process has its own initial value, and all non-faulty processes have to agree on a vector of values, one for each process. The vector agreed on must satisfy two conditions: (1) the value for each process is the initial value of that process, if it is non-faulty, or an arbitrary value, if it is faulty; and (2) all non-faulty processes agree on the same vector. This problem is also known as the Byzantine generals problem with signed messages .

These problems are related to each other, and can be solved using similar techniques, such as message passing, cryptography, or voting. However, they also have different levels of difficulty and impossibility results, depending on the system model, the number of processes, the number of faulty processes, the type of failures, the synchrony of the system, and the type of communication channels. For example, the Byzantine agreement problem is impossible to solve in a purely asynchronous system with one-third or more of the processes being faulty. The consensus problem is impossible to solve in a purely asynchronous system with even one faulty process, if the communication channels are unreliable. The interactive consistency problem is impossible to solve in a synchronous system with one-half or more of the processes being faulty.

Therefore, the classification of agreement problems in distributed systems is important to understand the trade-offs and limitations of different solutions, and to design appropriate protocols and algorithms for different scenarios and applications. Some of the applications of agreement problems in distributed systems are:

- **Atomic commitment**: A protocol that ensures that a set of processes either all commit to a transaction or all abort it, in a consistent and atomic manner.
- **Atomic broadcast**: A protocol that ensures that a set of processes deliver the same messages in the same order, despite failures or delays.
- **Group membership**: A protocol that maintains a consistent view of the processes that are part of a group, and detects and handles failures or joins and leaves of processes.
- **State machine replication**: A technique that replicates the same deterministic state machine on multiple processes, and ensures that they execute the same commands in the same order, and produce the same outputs and states, despite failures or asynchrony.



# Byzantine Agreement Problem

The Byzantine agreement problem is a fundamental problem in fault-tolerant distributed computing. It requires a set of parties in a distributed environment to agree on a value even if some of the parties are corrupted or faulty. The corrupted parties may behave arbitrarily, sending conflicting or misleading messages to different parties, or remaining silent. The problem is also known as the Byzantine generals problem, the interactive consistency problem, or the source congruency problem.

The problem was first defined and solved by Lamport et al. in 1982, using the analogy of several divisions of the Byzantine army camped outside an enemy city, each division commanded by its own general. The generals can communicate with one another only by messenger. After observing the enemy, they must decide upon a common plan of action, such as attack or retreat. However, some of the generals may be traitors, who try to prevent the loyal generals from reaching agreement. The problem is to find a protocol that allows the loyal generals to agree on the same plan, while tolerating a certain number of traitors.

Some of the main concepts and results related to the Byzantine agreement problem are:

- A protocol for Byzantine agreement is a set of rules that specify how the parties exchange messages and decide on a value, given their initial values and the messages they receive.
- A protocol is said to achieve Byzantine agreement if it satisfies the following properties:
  - **Termination**: Every loyal party eventually decides on a value.
  - **Agreement**: All loyal parties decide on the same value.
  - **Validity**: If all parties start with the same value, then all loyal parties decide on that value.
- A protocol is said to be **t-resilient** if it achieves Byzantine agreement even if up to t parties are corrupted.
- A protocol is said to be **synchronous** if it assumes that messages are delivered within a known bounded time, and parties have synchronized clocks. A protocol is said to be **asynchronous** if it makes no assumptions about message delivery time or clock synchronization.
- A protocol is said to be **authenticated** if it assumes that parties can verify the identity and authenticity of the messages they receive. A protocol is said to be **unauthenticated** if it makes no such assumptions.
- A fundamental result by Lamport et al. is that no protocol can achieve Byzantine agreement in a synchronous system with unauthenticated messages if t > n/3, where n is the number of parties and t is the number of corrupted parties. This is known as the **FLP impossibility** result.
- Another fundamental result by Pease et al. is that Byzantine agreement is possible in a synchronous system with authenticated messages if t < n/3. They also presented a protocol that achieves Byzantine agreement in this setting, using **quorums** of size at least 2t+1 and **signed messages**. This protocol requires O(n^2) messages and O(n) rounds of communication.
- Byzantine agreement is also possible in an asynchronous system with authenticated messages if t < n/3, using **randomization** or **cryptographic techniques**. However, these protocols are more complex and less efficient than the synchronous ones.
- Byzantine agreement is also possible in a synchronous or asynchronous system with unauthenticated messages if t < n/4, using **common coins** or **common randomness**. These are sources of randomness that are accessible and consistent for all parties, but unpredictable for the corrupted parties. However, these protocols also require additional assumptions and complexity.



# Consensus problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- The consensus problem is the problem of getting a set of nodes in a distributed system to agree on something - it might be a value, a course of action or a decision.
- Achieving consensus allows a distributed system to act as a single entity, with every individual node aware of and in agreement with the actions of the whole of the network.
- Consensus is a general agreement on a decision made by the majority of those involved.
- Consensus is essential for ensuring reliability, consistency, fault-tolerance, and availability in distributed systems  .
- Consensus is challenging to achieve in distributed systems because of the possibility of failures, delays, and communication errors among the nodes  .
- There are many ways in which processes in a distributed system can reach a consensus, but there is usually a trade-off between security and performance.
- The more we want our algorithm to be secure against ways in which failure can happen, the less performant it tends to become.
- Some of the common consensus algorithms in distributed systems are:
  - Two-phase commit (2PC): A simple and widely used protocol that involves a coordinator and a set of participants. The coordinator initiates the protocol by sending a prepare message to all participants, asking them to vote on a proposed value. The participants reply with either a yes or a no vote. If the coordinator receives a yes vote from all participants, it sends a commit message to all participants, asking them to commit the value. If the coordinator receives a no vote from any participant, or if it times out, it sends an abort message to all participants, asking them to abort the value .
  - Three-phase commit (3PC): An extension of 2PC that adds a pre-commit phase to avoid blocking in case of a coordinator failure. The coordinator initiates the protocol by sending a prepare message to all participants, asking them to vote on a proposed value. The participants reply with either a yes or a no vote. If the coordinator receives a yes vote from all participants, it sends a pre-commit message to all participants, asking them to prepare to commit the value. The participants reply with an ack message. If the coordinator receives an ack message from all participants, it sends a commit message to all participants, asking them to commit the value. If the coordinator receives a no vote from any participant, or if it times out, it sends an abort message to all participants, asking them to abort the value.
  - Paxos: A family of protocols that use a quorum-based approach to achieve consensus in the presence of failures. The protocol involves a set of proposers, acceptors, and learners. A proposer initiates the protocol by sending a prepare message with a proposal number to a quorum of acceptors, asking them to promise not to accept any proposal with a lower number. The acceptors reply with either a promise message, indicating the highest-numbered proposal they have accepted so far, or a reject message, indicating a higher-numbered proposal they have promised to another proposer. If the proposer receives a promise message from a quorum of acceptors, it sends an accept message with a proposal number and a value to the same quorum of acceptors, asking them to accept the value. The acceptors reply with either an accepted message, indicating they have accepted the value, or a reject message, indicating a higher-numbered proposal they have promised to another proposer. If the proposer receives an accepted message from a quorum of acceptors, it sends a learn message with the proposal number and the value to all learners, asking them to learn the value. The learners learn the value when they receive a learn message from a quorum of acceptors .
  - Raft: A simplified version of Paxos that uses a leader-based approach to achieve consensus. The protocol involves a set of servers that can be in one of three states: leader, follower, or candidate. The leader is responsible for managing the replication of a log of commands across the servers. The leader sends append entries messages to all followers, asking them to append the commands to their logs. The followers reply with either a success or a failure message, indicating whether they have appended the commands or not. The leader commits a command when it receives a success message from a majority



# Interactive Consistency Problem

- Interactive consistency is the problem in which n distinct nodes, each having its own private value, where up to t may be Byzantine, run an algorithm that allows all non-faulty nodes to infer the values of each other node  .
- Byzantine nodes are nodes that can behave arbitrarily, such as sending conflicting or incorrect messages, or remaining silent .
- Interactive consistency is a generalization of the consensus problem, where the goal is to reach agreement on a single value among all non-faulty nodes.
- Interactive consistency is relevant to critical applications that rely on the combination of the opinions of multiple peers to provide a service, such as fault-tolerant distributed systems, blockchain systems, or voting systems .
- Interactive consistency is also known as the Byzantine Generals Problem, which is a metaphor for the situation where a group of generals must coordinate an attack or retreat, but some of them may be traitors who try to sabotage the plan .
- Interactive consistency is a challenging problem to solve, especially in asynchronous or partially synchronous systems, where there is no global clock or bounded message delays .
- Interactive consistency requires at least n > 3t nodes to be solvable, where t is the number of Byzantine nodes  .
- Interactive consistency can be solved using various algorithms, such as the oral messages algorithm, the signed messages algorithm, the broadcast algorithm, or the randomized Byzantine consensus algorithm  .
- Interactive consistency algorithms typically involve multiple rounds of message exchange, where each node sends its value or a function of its value to other nodes, and then updates its own value based on the received messages  .
- Interactive consistency algorithms must ensure that the following properties are satisfied  :
  - Agreement: All non-faulty nodes agree on the same value for each node.
  - Validity: If a node is non-faulty, then its value is the same as the value agreed upon by all non-faulty nodes.
  - Termination: All non-faulty nodes eventually decide on a value for each node.



# Solution to Byzantine Agreement problem

- The Byzantine Agreement problem is a fundamental challenge in fault-tolerant distributed computing, where a set of processes need to agree on a common value despite the presence of some faulty or malicious processes that may send conflicting or incorrect messages.
- The problem is also known as the Byzantine Generals problem, which is an analogy to a scenario where several divisions of the Byzantine army are camped outside an enemy city, each division commanded by its own general. The generals can communicate with one another only by messenger. After observing the enemy, they must decide upon a common plan of action, such as attack or retreat. However, some of the generals may be traitors and try to sabotage the plan by sending false messages or no messages at all.
- The solution to the problem relies on an algorithm that can guarantee that:
  - All loyal processes decide upon the same value, and
  - A small number of faulty processes cannot cause the loyal processes to adopt a bad value.
- One of the most well-known solutions to the Byzantine Agreement problem is the **Oral Messages Algorithm** proposed by Lamport et al. in 1982. The algorithm works as follows:
  - Assume there are n processes, of which at most f are faulty. The algorithm can tolerate f < n/3.
  - Each process has an initial value, which is either 0 or 1. One of the processes is designated as the commander, and the rest are lieutenants. The commander sends its initial value to all lieutenants.
  - For each round i from 1 to f+1, each lieutenant acts as a relay and sends the value it received from the commander or the previous round to all other lieutenants. Each lieutenant then computes a majority value based on the values it received from all other lieutenants and itself. This majority value becomes the input for the next round.
  - After f+1 rounds, each lieutenant decides on the final majority value as its output.
- The Oral Messages Algorithm can ensure that if the commander is loyal, then all loyal lieutenants will decide on the same value as the commander. If the commander is faulty, then all loyal lieutenants will decide on the same value, which may or may not be the same as the commander's value. The algorithm can also ensure that a small number of faulty lieutenants cannot influence the decision of the loyal ones, as long as f < n/3. This is because in each round, a loyal lieutenant will receive at least n-f-1 > 2f messages from other loyal lieutenants, which will form a majority over the f messages from faulty lieutenants. Therefore, the majority value computed by a loyal lieutenant will always be the same as the majority value of the other loyal lieutenants.



# Application of Agreement Problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- Agreement problem is a fundamental problem in distributed systems, where a set of processes need to reach a common decision based on their individual inputs and preferences .
- Agreement problem has many variants, such as consensus, atomic commitment, atomic broadcast, and group membership.
- Consensus is the most basic and well-studied agreement problem, where each process proposes a value and all correct processes must agree on the same value, which must be one of the proposed values .
- Atomic commitment is a special case of consensus, where the proposed values are either commit or abort, and the processes must agree on whether to commit or abort a transaction .
- Atomic broadcast is a problem where a process broadcasts a message to all other processes, and all correct processes must deliver the same set of messages in the same order .
- Group membership is a problem where the processes must agree on a view of the current set of processes in the system, and update the view whenever a process joins or leaves .
- Agreement problems are essential for implementing reliable and consistent distributed applications, such as replicated state machines, atomic snapshot objects, distributed databases, fault-tolerant services, and blockchain systems   .
- Agreement problems are challenging to solve in distributed systems, especially in the presence of failures, asynchrony, and malicious behavior  .
- Agreement problems have different solvability and complexity results depending on the system model, the failure model, the communication model, and the synchrony assumptions  .
- Agreement problems have been studied extensively in the literature, and many algorithms and protocols have been proposed for different settings and scenarios    .
- Agreement problems are still an active area of research, as new applications and challenges emerge in the field of distributed systems   .



# Atomic Commit in Distributed Database System

- A distributed database system consists of multiple sites that store data and execute transactions.
- A distributed transaction is a transaction that accesses data from more than one site.
- Atomicity is a property that ensures that a distributed transaction either commits (succeeds) or aborts (fails) as a whole, regardless of failures or communication delays in the system.
- Atomic commit is a protocol that coordinates the decision of whether to commit or abort a distributed transaction among all the sites involved.
- Atomic commit is essential for maintaining the consistency and integrity of the distributed database.
- There are two main types of atomic commit protocols: blocking and non-blocking.
- Blocking protocols require some sites to wait for the response of other sites before making a decision. They guarantee atomicity, but may cause delays or deadlocks in the presence of failures.
- Non-blocking protocols allow sites to make independent decisions based on local information. They do not guarantee atomicity, but may improve performance and availability in the presence of failures.
- Examples of blocking protocols are two-phase commit (2PC) and three-phase commit (3PC).
- Examples of non-blocking protocols are one-phase commit (1PC), presumed abort (PA), presumed commit (PC), and failure-aware commit (FLAC).



# Unit 5 - Distributed Resource Management

- Distributed resource management (DRM) is an evolving discipline consisting of a set of software, hardware, network tools, procedures and policies for enabling distributed enterprise systems to operate effectively in production.
- Distributed enterprise systems are systems that span multiple locations, platforms, and domains, and require coordination and collaboration among different entities and stakeholders.
- DRM aims to optimize the utilization, performance, availability, and security of distributed resources, such as computing, storage, network, data, and energy resources.
- DRM faces various challenges, such as heterogeneity, scalability, dynamism, uncertainty, and complexity of distributed systems and their environments.
- DRM can be applied to various domains and scenarios, such as cloud computing, grid computing, edge computing, Internet of Things, smart grid, and smart cities.
- DRM can be implemented in different ways, such as centralized, decentralized, hierarchical, or hybrid architectures, depending on the trade-offs between efficiency, robustness, and flexibility.
- DRM can use different techniques and methods, such as resource discovery, resource allocation, resource scheduling, resource monitoring, resource adaptation, and resource governance, depending on the objectives and constraints of the system and the resources.
- DRM can benefit from various technologies and standards, such as web services, RESTful APIs, middleware, agents, ontologies, and protocols, to facilitate interoperability, communication, and coordination among distributed resources and systems.



# Issues in Distributed File Systems

A distributed file system (DFS) is a system that allows multiple clients to access and manipulate files stored on one or more servers over a network. A DFS provides the abstraction of a single, shared namespace for files, regardless of their physical location or the network topology. A DFS can improve the performance, reliability, scalability, and security of file access and management.

However, designing and implementing a DFS also involves many challenges and issues, such as:

- **Naming and transparency**: How to assign unique and meaningful names to files and directories in a DFS? How to support different naming schemes and conventions? How to provide location transparency, replication transparency, migration transparency, and concurrency transparency to the users and applications?
- **Consistency and caching**: How to ensure that the file data and metadata are consistent across multiple replicas and caches in a DFS? How to handle concurrent updates and conflicts? How to balance the trade-off between consistency and performance? How to implement efficient and effective caching policies and mechanisms?
- **Fault tolerance and availability**: How to cope with partial failures, such as node crashes, link failures, network partitions, and storage failures, in a DFS? How to ensure that the file service is available and accessible even in the presence of failures? How to recover from failures and restore the system state?
- **Security and access control**: How to protect the confidentiality, integrity, and authenticity of the file data and metadata in a DFS? How to prevent unauthorized access, modification, deletion, or copying of files? How to enforce access control policies and permissions for different users and groups? How to deal with malicious attacks and intrusions?
- **Scalability and performance**: How to support a large number of files, servers, and clients in a DFS? How to distribute the load and balance the workload among the servers? How to optimize the network bandwidth and latency for file transfers? How to reduce the overhead and complexity of the DFS?
- **Interoperability and compatibility**: How to enable the communication and cooperation among different DFS implementations and protocols? How to support heterogeneous platforms and environments? How to maintain backward and forward compatibility with existing and future file systems?

These are some of the main issues that need to be addressed in the design and use of a DFS. Different DFS solutions may adopt different approaches and techniques to tackle these issues, depending on their goals, assumptions, and requirements. Therefore, it is important to understand the advantages and disadvantages of each solution and compare them with respect to the criteria of functionality, performance, reliability, security, and usability.



# Mechanism for building distributed file systems

A distributed file system (DFS) is a file system that is distributed on multiple file servers or multiple locations. It allows programs to access or store isolated files as they do with the local ones, allowing programmers to access files from any network or computer.

The mechanism for building distributed file systems involves the following aspects:

- Use of file models: The DFS uses different conceptual models of a file. The following are the two basic criteria for file modeling, which include file structure and modifiability. The files can be unstructured or structured based on the applications used in file systems. The files can also be immutable or mutable depending on whether they can be modified or not .
- Use of file accessing models: A distributed file system may use one of the following models to service a client’s file requests: upload/download, remote access, or remote service. The upload/download model involves transferring the entire file between the client and the server. The remote access model involves sending file operations to the server and receiving the results. The remote service model involves invoking a service on the server that operates on the file and returns the output .
- Use of file replication: File replication is the primary mechanism for improving file availability in a distributed systems environment. A replicated file is a file that has multiple copies with each copy located on a separate file server. The challenges of file replication include maintaining consistency, managing concurrency, and handling failures .
- Use of file caching: File caching is the secondary mechanism for improving file performance in a distributed systems environment. A file cache is a temporary storage area that holds a copy of a file or a part of a file that is frequently accessed by a client. The benefits of file caching include reducing network traffic, saving disk space, and enhancing response time. The challenges of file caching include maintaining coherence, managing cache replacement, and handling failures .
- Use of file naming: File naming is the mechanism for identifying and locating files in a distributed file system. A file name consists of two parts: a file identifier and a file path. A file identifier is a unique name that distinguishes a file from other files. A file path is a sequence of names that specifies the location of a file in a hierarchical directory structure. The issues of file naming include resolving name conflicts, supporting name transparency, and providing name resolution .
- Use of cloud services: To extend a global distributed file system to the cloud is relatively straightforward. Cloud services expose file and object storage using either standard protocols such as NFS and SMB or published APIs such as Amazon S3 and Google Cloud Storage. The advantages of using cloud services include scalability, elasticity, and cost-effectiveness. The challenges of using cloud services include security, privacy, and interoperability.



# Design issues in Distributed Shared Memory

Distributed Shared Memory (DSM) is a mechanism that allows multiple processes on different nodes to share a common logical address space and access data transparently. DSM can simplify the programming of distributed systems by hiding the details of inter-process communication and data consistency. However, DSM also introduces several design issues that affect its performance, scalability, and correctness. Some of the main design issues in DSM are:

- **Granularity**: Granularity refers to the size of the unit of data that is shared and transferred among the nodes. A fine-grained DSM system uses small units, such as words or cache lines, while a coarse-grained DSM system uses large units, such as pages or segments. The choice of granularity affects the communication overhead, the memory overhead, the false sharing, and the synchronization cost of the DSM system. Generally, fine-grained DSM systems have lower memory overhead and synchronization cost, but higher communication overhead and false sharing, than coarse-grained DSM systems. False sharing occurs when different processes access different parts of the same unit of data, causing unnecessary data transfers and invalidations.

- **Structure**: Structure refers to the organization and layout of the shared data in the memory. The structure of the shared data can be flat, hierarchical, or object-based. A flat structure treats the shared data as a single linear address space that is uniformly accessible by all the nodes. A hierarchical structure divides the shared data into multiple regions or segments that can have different access rights and coherence policies. An object-based structure organizes the shared data into objects that can have methods, attributes, and inheritance relationships. The choice of structure affects the flexibility, modularity, and security of the DSM system. Generally, flat structures are simple and efficient, but lack the ability to support heterogeneous and dynamic applications. Hierarchical and object-based structures are more flexible and modular, but introduce more complexity and overhead.

- **Coherence semantics**: Coherence semantics define the consistency model of the DSM system, that is, the rules and guarantees about the order and visibility of the updates to the shared data. Coherence semantics can be strict, relaxed, or weak. A strict coherence semantics requires that all the nodes see the same value of a shared data item at any time, and that the updates are propagated in the order of their occurrence. A relaxed coherence semantics allows some nodes to see stale values of a shared data item for some time, and that the updates are propagated in the order of their synchronization operations. A weak coherence semantics does not impose any order or visibility constraints on the updates, and leaves the responsibility of ensuring consistency to the programmer. The choice of coherence semantics affects the performance, scalability, and programmability of the DSM system. Generally, strict coherence semantics are easy to program, but incur high communication and synchronization overhead. Relaxed and weak coherence semantics are more efficient and scalable, but require more programming effort and discipline.

- **Implementation methods**: Implementation methods refer to the techniques and mechanisms used to realize the DSM system. Implementation methods can be classified into two categories: software-based and hardware-based. Software-based methods rely on the operating system or the compiler to provide the DSM functionality, such as memory allocation, data transfer, coherence maintenance, and fault tolerance. Hardware-based methods rely on the network or the processor to provide the DSM functionality, such as remote memory access, cache coherence, and atomic operations. The choice of implementation methods affects the performance, portability, and reliability of the DSM system. Generally, software-based methods are more portable and flexible, but have higher overhead and complexity. Hardware-based methods are more efficient and reliable, but have higher cost and dependency.



# Algorithm for Implementation of Distributed Shared Memory

Distributed Shared Memory (DSM) is a technique that allows multiple processes on different nodes of a distributed system to access a common virtual address space as if they were running on a single machine. DSM can simplify the programming of distributed applications by providing a shared memory abstraction. However, DSM also introduces challenges such as maintaining consistency, coherence, and performance of the shared data.

There are different algorithms for implementing DSM, each with its own advantages and disadvantages. Some of the basic algorithms are:

- **Central Server Algorithm**: In this algorithm, a central server maintains all the shared data and services read and write requests from other nodes. The central server can use a page-based or an object-based approach to manage the shared data. The advantage of this algorithm is that it is simple and ensures consistency and coherence of the shared data. The disadvantage is that it introduces a single point of failure and a bottleneck for communication and computation.

- **Migration Algorithm**: In this algorithm, the shared data is distributed among the nodes and can migrate from one node to another based on the access patterns. Each data item has a home node that keeps track of its current location and grants access permissions to other nodes. When a node requests to read or write a data item, it contacts the home node and obtains a copy of the data item. The data item can then be cached locally or moved to the requesting node. The advantage of this algorithm is that it reduces the communication overhead and improves the locality of the shared data. The disadvantage is that it requires more complex protocols to ensure consistency and coherence of the shared data.

- **Replication Algorithm**: In this algorithm, the shared data is replicated on multiple nodes and can be accessed locally by the processes. Each data item has a set of replicas that are kept consistent and coherent by using a consistency protocol. The consistency protocol can be based on a centralized or a distributed approach. The advantage of this algorithm is that it provides high availability and fault tolerance of the shared data. The disadvantage is that it requires more storage space and more communication overhead to maintain the consistency and coherence of the shared data.

- **Invalidation Algorithm**: In this algorithm, the shared data is distributed among the nodes and can be cached locally by the processes. Each data item has a home node that keeps track of its current version and invalidates the cached copies on other nodes when a write occurs. When a node requests to read or write a data item, it contacts the home node and obtains the latest version of the data item. The advantage of this algorithm is that it reduces the communication overhead and improves the performance of read operations. The disadvantage is that it requires more communication overhead and reduces the performance of write operations.



## Unit 6 - Failure Recovery in Distributed Systems

- Failure recovery is the process of restoring the normal operation of a distributed system after a failure occurs.
- Failures can be classified into different types, such as crash failures, omission failures, timing failures, response failures, Byzantine failures, etc.
- Failure recovery techniques can be categorized into different levels, such as process level, communication level, data level, and application level.
- Process level recovery involves restarting or replacing failed processes, using techniques such as checkpointing, rollback, replication, and fault tolerance.
- Communication level recovery involves ensuring reliable and ordered delivery of messages, using techniques such as acknowledgments, timeouts, retransmissions, sequence numbers, and logical clocks.
- Data level recovery involves maintaining the consistency and availability of distributed data, using techniques such as transactions, concurrency control, commit protocols, logging, and recovery protocols.
- Application level recovery involves adapting the application logic to cope with failures, using techniques such as exception handling, compensation, and retry.
- Failure recovery techniques can have different properties, such as correctness, completeness, efficiency, scalability, and transparency.



# Concepts in Backward and Forward Recovery

- Backward recovery and forward recovery are two techniques for restoring the system to a consistent state after a failure in a distributed system.
- Backward recovery involves rolling back the system to a previous error-free state by using checkpoints and logs. Forward recovery involves correcting the errors and continuing the execution from the current state.
- The main difference between backward and forward recovery is that backward recovery discards the work done after the error, while forward recovery preserves the work done before and after the error.
- Backward recovery is more general and independent of the nature of faults, but it may incur more overhead and latency. Forward recovery is more efficient and responsive, but it requires accurate assessment and removal of errors.
- Some examples of backward recovery protocols are checkpointing, logging, message logging, and rollback-recovery. Some examples of forward recovery protocols are redundancy, masking, retry, and compensation.



# Recovery in Concurrent Systems

Recovery in concurrent systems is the process of restoring the system to a consistent state after a failure or an error. Recovery is essential for ensuring the reliability and availability of distributed systems that involve multiple concurrent transactions.

There are two main types of recovery in concurrent systems:

- **Backward recovery**: This type of recovery involves undoing the effects of the erroneous or failed transactions and restoring the system to a previous consistent state. Backward recovery requires the system to periodically record its state (such as through checkpoints or logs) and to use these records to rollback the changes made by the faulty transactions.
- **Forward recovery**: This type of recovery involves correcting the errors or failures without undoing the effects of the transactions. Forward recovery requires the system to detect the errors or failures and to apply some recovery actions to fix them (such as through exception handling or redundancy) .

Some of the challenges and techniques for recovery in concurrent systems are:

- **Interaction with concurrency control**: The recovery scheme depends on the concurrency control scheme that is used to ensure the serializability and isolation of the transactions. For example, if the system uses locking as a concurrency control mechanism, then the recovery scheme must release the locks held by the failed transactions and prevent deadlocks. If the system uses timestamps as a concurrency control mechanism, then the recovery scheme must ensure that the timestamps are consistent and do not cause conflicts .
- **Transaction rollback**: The recovery scheme must be able to rollback the transactions that are affected by the failure or error. This involves undoing the changes made by the transactions to the data and the system state. The recovery scheme must also ensure that the rollback does not affect the transactions that are not involved in the failure or error. The recovery scheme can use different methods to rollback the transactions, such as undo logging, redo logging, or shadow paging .
- **Checkpoints**: The recovery scheme can use checkpoints to reduce the amount of work needed to rollback the transactions. A checkpoint is a point in time when the system records its state and flushes the logs to the stable storage. The recovery scheme can use the checkpoint as a reference point to rollback the transactions that occurred after the checkpoint. The recovery scheme must also ensure that the checkpoints are consistent and do not cause conflicts with the concurrent transactions .
- **Restart recovery**: The recovery scheme must be able to restart the system after a failure or error. This involves restoring the system state from the stable storage and resuming the execution of the transactions. The recovery scheme must also ensure that the restart does not cause any inconsistency or duplication of the transactions. The recovery scheme can use different methods to restart the system, such as warm restart, cold restart, or fuzzy restart .
- **Concurrent recovery**: The recovery scheme can use concurrent recovery to speed up the recovery process and to improve the system performance. Concurrent recovery involves running multiple recovery sessions in parallel to recover different media sets or data items. Concurrent recovery requires the system to coordinate the recovery sessions and to ensure that they do not interfere with each other or with the normal transactions   .



# Obtaining consistent Checkpoints for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Failure recovery in distributed systems is the process of restoring the system to a consistent and correct state after a failure occurs.
- A failure in a distributed system can be caused by various factors, such as hardware faults, software bugs, network errors, malicious attacks, or human mistakes.
- A failure can affect one or more components of the system, such as nodes, processes, messages, or data.
- A failure can have different consequences, such as data loss, data corruption, performance degradation, or system unavailability.
- To recover from a failure, the system needs to detect the failure, identify the cause and location of the failure, and restore the system to a consistent and correct state.
- A consistent state is a state where all the components of the system agree on the same view of the system and its data.
- A correct state is a state where the system and its data satisfy the specifications and requirements of the system.
- One of the common techniques for failure recovery in distributed systems is checkpointing .
- Checkpointing is the process of periodically saving the state of the system or its components to a stable storage, such as a disk or a cloud service.
- Checkpointing can be done at different levels, such as process level, node level, or system level.
- Checkpointing can be done at different frequencies, such as every iteration, every transaction, or every time interval.
- Checkpointing can be done in different modes, such as synchronous, asynchronous, or coordinated.
- Synchronous checkpointing means that all the components of the system save their state at the same time.
- Asynchronous checkpointing means that each component of the system saves its state independently of the others.
- Coordinated checkpointing means that the components of the system save their state in a coordinated manner, such as by exchanging messages or using a global clock.
- The advantages of checkpointing are that it can reduce the amount of data loss, data corruption, and re-computation in case of a failure.
- The disadvantages of checkpointing are that it can introduce overhead, latency, and complexity to the system.
- To obtain consistent checkpoints, the system needs to ensure that the checkpoints of the components are compatible and do not contain any inconsistencies or contradictions.
- For example, if a process A sends a message to a process B, and B saves its state after receiving the message, but A saves its state before sending the message, then the checkpoints of A and B are inconsistent.
- To avoid such inconsistencies, the system can use different techniques, such as causal dependency tracking, message logging, or vector clocks.
- Causal dependency tracking means that the system records the causal relationships between the events and messages in the system, and uses them to determine the order and consistency of the checkpoints.
- Message logging means that the system logs the messages sent and received by the components, and uses them to replay the messages and restore the state of the components after a failure.
- Vector clocks means that the system assigns a logical timestamp to each event and message in the system, and uses them to compare and synchronize the checkpoints of the components.
- Obtaining consistent checkpoints is important for failure recovery in distributed systems, because it can help the system to resume its normal operation and maintain its correctness and consistency after a failure.



# Recovery in Distributed Database Systems

Recovery in distributed database systems is the process of restoring the database to a consistent and correct state after a failure. A failure can be caused by various factors, such as hardware malfunction, software bugs, network partition, power outage, or malicious attacks. Recovery is essential to ensure the atomicity and durability of distributed transactions, which are transactions that span multiple sites or nodes in a distributed system.

There are two main types of failures that can affect a distributed database system: soft failures and hard failures.

- Soft failures are temporary and do not cause permanent damage to the database. They can result in inconsistency or incompleteness of the database, such as lost updates, uncommitted changes, or deadlocks. Soft failures can be handled by transaction recovery, which involves undoing or redoing the effects of faulty transactions. Transaction recovery is based on the use of logs, which record the history of transactions and their operations on the database. Transaction recovery can be performed locally at each site, or globally across the distributed system, depending on the recovery protocol used.

- Hard failures are permanent and cause extensive damage to the database. They can result in loss or corruption of data, such as disk crashes, memory failures, or site failures. Hard failures can be handled by database recovery, which involves restoring a past copy of the database from a backup. Database recovery is based on the use of checkpoints, which are snapshots of the database taken at regular intervals. Database recovery can be performed at the level of pages, files, or databases, depending on the recovery technique used.

Some of the challenges and issues in recovery in distributed database systems are:

- How to coordinate the recovery of multiple sites or nodes that are involved in a distributed transaction, especially in the presence of network failures or communication delays.
- How to minimize the overhead and performance impact of logging, checkpointing, and recovery on the normal operation of the distributed system.
- How to maintain the consistency and correctness of the database across the distributed system, especially in the presence of concurrent and conflicting transactions.
- How to provide partial operability and availability of the distributed system during and after a failure, especially in the presence of site or node failures.
- How to avoid or reduce the need for global rollback, which is the process of undoing the effects of all transactions that have executed since the last checkpoint.

Some of the recovery protocols and techniques that are used in distributed database systems are:

- Two-phase commit protocol (2PC), which is a protocol that ensures the atomicity of distributed transactions by coordinating the commit or abort decision of all the sites or nodes involved in a transaction.
- Three-phase commit protocol (3PC), which is a protocol that improves the availability and fault-tolerance of distributed transactions by introducing a third phase of preparation before the commit or abort decision.
- Presumed abort protocol (PA), which is a protocol that optimizes the logging and recovery of distributed transactions by assuming that transactions abort unless they explicitly commit.
- Presumed commit protocol (PC), which is a protocol that optimizes the logging and recovery of distributed transactions by assuming that transactions commit unless they explicitly abort.
- Deferred update technique, which is a technique that delays the writing of updates to the database until the transaction commits, thus reducing the need for undo logging and recovery.
- Immediate update technique, which is a technique that writes the updates to the database as soon as they are generated by the transaction, thus reducing the need for redo logging and recovery.
- Shadow paging technique, which is a technique that maintains two copies of the database pages, one for the current state and one for the shadow state, and switches between them when a transaction commits or aborts, thus eliminating the need for logging and recovery.
- Fuzzy checkpointing technique, which is a technique that allows the database to continue processing transactions while a checkpoint is being taken, thus reducing the blocking and overhead of checkpointing.



## Unit 7 - Fault Tolerance

- Fault tolerance is the ability of a system to continue functioning correctly in the presence of failures.
- Fault tolerance can be achieved by using techniques such as redundancy, replication, recovery, and reconfiguration.
- Fault tolerance can be classified into two types: hardware fault tolerance and software fault tolerance.
- Hardware fault tolerance is the ability of a system to cope with failures of physical components, such as processors, memory, disks, or network links.
- Hardware fault tolerance can be implemented by using techniques such as RAID, backup power supplies, hot swapping, and fail-over clustering.
- Software fault tolerance is the ability of a system to cope with failures of software components, such as bugs, errors, or malicious attacks.
- Software fault tolerance can be implemented by using techniques such as exception handling, checkpointing, rollback, transactions, and Byzantine fault tolerance.
- Fault tolerance can be measured by using metrics such as reliability, availability, and maintainability.
- Reliability is the probability that a system will perform its intended function without failure for a given period of time.
- Availability is the fraction of time that a system is operational and ready to provide service.
- Maintainability is the ease with which a system can be repaired or restored to its normal state after a failure.



# Issues in Fault Tolerance for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Fault tolerance is the ability of a system to continue functioning correctly in the presence of failures.
- Fault tolerance is important for distributed systems because they consist of multiple components that may be subject to different types of failures, such as hardware failures, software failures, network failures, malicious attacks, etc.
- Fault tolerance can be achieved by using various techniques, such as redundancy, replication, checkpointing, recovery, consensus, etc.
- Some of the issues and challenges in fault tolerance for distributed systems are:

  - How to detect and identify failures in a timely and accurate manner.
  - How to design and implement fault-tolerant algorithms that can cope with different failure models, such as crash failures, omission failures, Byzantine failures, etc.
  - How to ensure the consistency and availability of data and services in the presence of failures and network partitions.
  - How to balance the trade-offs between performance, reliability, and cost in fault-tolerant systems.
  - How to evaluate and measure the fault tolerance of distributed systems using appropriate metrics and benchmarks.



# Commit Protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Commit protocols are algorithms that ensure the atomicity of distributed transactions, i.e., all the sites involved in a transaction either commit or abort it unanimously, even in the presence of failures  .
- Commit protocols are necessary to maintain the consistency and reliability of distributed systems, as they prevent partial execution or loss of data due to network or site failures  .
- There are different types of commit protocols, such as one-phase, two-phase, and three-phase commit protocols, each with its own advantages and disadvantages    .

## One-phase commit protocol
- A one-phase commit protocol involves a coordinator site that initiates a transaction and communicates with the participating sites to execute it .
- The coordinator site sends a commit request to all the participating sites and waits for their replies .
- If all the participating sites reply with an OK message, the coordinator site commits the transaction and informs the participating sites to do the same .
- If any of the participating sites reply with an ABORT message or fail to reply, the coordinator site aborts the transaction and informs the participating sites to do the same .
- The advantages of this protocol are simplicity and efficiency, as it requires only one round of message exchange between the coordinator and the participating sites .
- The disadvantages of this protocol are lack of fault tolerance and concurrency control, as it does not handle the cases where the coordinator site fails or the participating sites have conflicting transactions .

## Two-phase commit protocol
- A two-phase commit protocol is an extension of the one-phase commit protocol that adds a voting phase to improve the fault tolerance and concurrency control    .
- The two phases of this protocol are the prepare phase and the commit phase    .
- In the prepare phase, the coordinator site sends a prepare request to all the participating sites and waits for their votes    .
- The participating sites execute the transaction locally and write a log record of their decision (commit or abort) before sending their votes to the coordinator site    .
- If all the participating sites vote to commit, the coordinator site decides to commit the transaction and enters the commit phase    .
- In the commit phase, the coordinator site sends a commit request to all the participating sites and waits for their acknowledgments    .
- The participating sites commit the transaction and send an acknowledgment to the coordinator site    .
- If any of the participating sites vote to abort or fail to reply in the prepare phase, the coordinator site decides to abort the transaction and enters the abort phase    .
- In the abort phase, the coordinator site sends an abort request to all the participating sites and waits for their acknowledgments    .
- The participating sites abort the transaction and send an acknowledgment to the coordinator site    .
- The advantages of this protocol are fault tolerance and concurrency control, as it handles the cases where the coordinator or the participating sites fail or have conflicting transactions    .
- The disadvantages of this protocol are blocking and overhead, as it requires two rounds of message exchange and the sites



# Voting Protocols for Fault Tolerance in Distributed Systems

- Voting protocols are a type of consensus protocols that allow a set of distributed nodes to agree on a common value or decision, despite the presence of faults or attacks.
- Voting protocols are useful for achieving fault tolerance in distributed systems, such as replicated databases, distributed file systems, or blockchain networks.
- Voting protocols can be classified into two categories: exact voting and inexact voting.
  - Exact voting requires all nodes to agree on the same value or decision, and is typically implemented using two-phase commit or three-phase commit protocols.
  - Inexact voting allows nodes to agree on a value or decision that is close enough to the correct one, and is typically implemented using majority voting, weighted voting, or probabilistic voting protocols.
- Voting protocols can also be classified into two categories based on the security level: secure voting and non-secure voting.
  - Secure voting ensures that the voting process is resilient to malicious attacks, such as denial-of-service, impersonation, or tampering.
  - Non-secure voting assumes that the voting process is only subject to benign faults, such as crashes, delays, or message losses.
- Voting protocols can also be evaluated based on the fairness property, which measures how well the voting process reflects the preferences or weights of the nodes.
  - Fairness can be defined in different ways, such as proportional fairness, envy-freeness, or Pareto optimality.
  - Fairness can be affected by various factors, such as the voting rule, the network topology, the node behavior, or the adversary model.
- Voting protocols are an active area of research in distributed systems, and there are many open challenges and trade-offs to consider, such as scalability, efficiency, robustness, or adaptability.



# Dynamic voting protocols

- Dynamic voting protocols are a technique for maintaining consistency and availability of replicated data in distributed systems.
- Replicated data is a copy of a logical file that is stored at multiple sites to improve performance, reliability, and fault tolerance.
- Consistency means that all copies of a replicated file have the same value at any given time.
- Availability means that a replicated file can be accessed by any site that needs it, even in the presence of failures or network partitions.
- Dynamic voting protocols use a quorum-based approach to achieve consistency and availability. A quorum is a subset of sites that have a copy of a replicated file and can collectively decide on its value.
- Each site is assigned a number of votes, and a quorum is formed when the total number of votes exceeds a predefined threshold. Only a quorum can perform read or write operations on a replicated file.
- Dynamic voting protocols allow the votes to be reassigned dynamically based on the current state of the system, such as the number of active sites, the network connectivity, and the access patterns.
- The advantages of dynamic voting protocols are that they can adapt to changing conditions, improve the availability of replicated files, and reduce the communication overhead and the number of votes needed for a quorum.
- The challenges of dynamic voting protocols are that they require a mechanism to detect and resolve conflicts, to coordinate the vote reassignment, and to ensure the safety and liveness properties of the system.



## Unit 8 - Transactions and Concurrency Control

- A transaction is a logical unit of work that consists of a sequence of database operations, such as queries, updates, inserts, or deletes.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
  - Atomicity means that either all the operations of a transaction are executed or none of them are.
  - Consistency means that a transaction preserves the integrity constraints of the database.
  - Isolation means that a transaction does not interfere with other concurrent transactions.
  - Durability means that the effects of a committed transaction are permanent and survive any system failures.
- Concurrency control is the process of managing simultaneous access to shared data by multiple transactions, while ensuring data consistency and preventing conflicts.
- Concurrency control techniques can be classified into two categories: pessimistic and optimistic.
  - Pessimistic concurrency control assumes that conflicts are likely to occur and prevents them by locking the data items accessed by a transaction until it commits or aborts.
  - Optimistic concurrency control assumes that conflicts are rare and detects them by validating the read and write sets of a transaction before committing it.
- Some common concurrency control protocols are:
  - Two-phase locking (2PL): a transaction acquires all the locks it needs before releasing any of them. 2PL ensures serializability, but may cause deadlocks or starvation.
  - Timestamp ordering (TO): a transaction is assigned a unique timestamp when it starts, and the order of conflicting operations is determined by their timestamps. TO ensures serializability, but may cause cascading aborts or excessive restarts.
  - Validation (or optimistic) concurrency control (VCC): a transaction executes without locking any data items, and validates its read and write sets at commit time. VCC ensures serializability, but may cause high abort rates or wasted resources.
  - Multiversion concurrency control (MVCC): a transaction operates on a snapshot of the database taken at its start time, and writes to a new version of the data items. MVCC ensures serializability and avoids locking, but may cause storage overhead or garbage collection issues.



# Transactions

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the operations in a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction does not interfere with other concurrent transactions.
- Durability means that the effects of a committed transaction are permanent and survive failures.

# Concurrency Control

- Concurrency control is the process of managing simultaneous access to shared data in a database by multiple transactions.
- Concurrency control ensures that the transactions are executed in a correct and consistent manner, without violating the ACID properties.
- Concurrency control can be implemented using various techniques, such as locking, timestamping, validation, and multiversioning.

# Distributed Systems

- A distributed system is a system that consists of multiple independent components that communicate and coordinate with each other over a network.
- A distributed system can provide advantages such as scalability, availability, fault tolerance, and performance.
- A distributed system can also pose challenges such as heterogeneity, partial failures, concurrency, and consistency.

# Distributed Transactions

- A distributed transaction is a transaction that spans multiple components of a distributed system, such as different data servers, application servers, or clients.
- A distributed transaction consists of a set of subtransactions, each of which is executed by one component of the system.
- A distributed transaction coordinator is responsible for coordinating the execution and commitment of the subtransactions across the system.
- A distributed transaction has the same ACID properties as a local transaction, but it also requires additional mechanisms to ensure global atomicity and consistency.

# Distributed Concurrency Control

- Distributed concurrency control is the concurrency control of a distributed system, where multiple transactions can access and update shared data hosted by different components of the system.
- Distributed concurrency control ensures that the subtransactions of a set of distributed transactions are serialized identically in all components involved, and that the ACID properties are not violated by their interleaved execution.
- Distributed concurrency control can be implemented using various techniques, such as distributed locking, distributed timestamping, distributed validation, and distributed multiversioning.



# Nested transactions for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A transaction is a logical unit of work that consists of a sequence of operations that must be executed atomically, consistently, isolated, and durable (ACID properties).
- A distributed transaction is a transaction that accesses data or resources that are managed by different servers or nodes in a distributed system.
- A nested transaction is a transaction that is composed of subtransactions that can be committed or aborted independently, but are also coordinated by a parent transaction that ensures the overall atomicity of the whole transaction.
- Nested transactions can be useful for several reasons, such as:
  - Breaking down a complex transaction into simpler and more manageable subtransactions.
  - Allowing partial results or intermediate states to be visible or persistent without violating the ACID properties of the whole transaction.
  - Supporting concurrency control and recovery mechanisms that can handle subtransactions separately and reduce locking or logging overheads.
  - Providing modularity and flexibility for transaction processing in distributed systems, where different subtransactions can be executed by different servers or nodes.
- Nested transactions can be classified into two types, depending on how the subtransactions are related to the parent transaction:
  - Closed nested transactions: The subtransactions are completely isolated from the parent transaction and other subtransactions, and their effects are only visible to the parent transaction after they commit. The parent transaction can abort any subtransaction at any time, and can also abort itself, which causes all the subtransactions to abort as well. This type of nested transactions preserves the strict serializability of the whole transaction, but may incur high overheads for maintaining isolation and undoing subtransactions.
  - Open nested transactions: The subtransactions are allowed to share some data or resources with the parent transaction or other subtransactions, and their effects can be visible or persistent before they commit. The parent transaction cannot abort any subtransaction after it commits, and can only abort itself if none of the subtransactions have committed. This type of nested transactions relaxes the serializability of the whole transaction, but may improve the performance and availability of the system by allowing more concurrency and reducing the need for compensation or recovery.



# Locks for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A lock is a variable associated with a data item that determines whether read/write operations can be performed on that data item.
- Locking-based concurrency control protocols use locks to avoid concurrency problems between two transactions in such a way that the lock is applied on one transaction and another transaction can access it only when the lock is released.
- Locks can be applied on read and write operations, and they can be of different types, such as shared, exclusive, or update locks.
- A lock compatibility matrix is used to state whether a data item can be locked by two transactions at the same time. For example, two transactions can share a read lock on the same data item, but they cannot both have an exclusive write lock on it.
- Locks can be granted or denied by a lock manager, which is a component of the distributed system that maintains the lock information and enforces the locking protocol.
- Locks can be implemented at different levels of granularity, such as record, page, file, or table. The choice of granularity affects the performance and concurrency of the system.
- Locks can also be classified as local or global, depending on whether they are applied on a single site or across multiple sites in the distributed system. Global locks require coordination and communication among the sites, which can increase the overhead and complexity of the system.
- Locking-based concurrency control protocols can be further divided into two-phase locking (2PL), rigorous two-phase locking (R2PL), and tree-based locking (TBL) protocols.
- 2PL protocol requires that a transaction acquires all the locks it needs before releasing any lock, and it releases all the locks at the end of the transaction. This ensures serializability, but it can cause deadlocks and reduce concurrency.
- R2PL protocol is a stricter version of 2PL that requires that a transaction releases all the locks only after it commits or aborts. This ensures strict serializability and avoids cascading aborts, but it can also cause deadlocks and reduce concurrency.
- TBL protocol is a variant of 2PL that organizes the data items into a tree structure and requires that a transaction locks the data items in a top-down order and releases them in a bottom-up order. This avoids deadlocks, but it can also reduce concurrency and increase locking overhead.



# Optimistic Concurrency Control

- Optimistic concurrency control (OCC) is a concurrency control method applied to transactional systems such as relational database management systems and software transactional memory.
- OCC assumes that multiple transactions can frequently complete without interfering with each other, and avoids locking of data items that can reduce the performance of the system.
- OCC consists of three phases: read, validation and write.
  - In the read phase, the transaction reads the data items from the database and performs the necessary computations, but does not update the database.
  - In the validation phase, the transaction checks if any of the data items it has read have been modified by other transactions that committed after it started. If so, the transaction is aborted and restarted, otherwise it proceeds to the write phase.
  - In the write phase, the transaction updates the database with the new values of the data items it has modified.
- OCC has some advantages over locking-based concurrency control techniques, such as:
  - It avoids the overhead of acquiring and releasing locks, which can improve the performance of the system.
  - It avoids the problem of deadlock, which can occur when two or more transactions are waiting for each other to release locks.
  - It allows more concurrency, as transactions can read and write data items without blocking each other.
- OCC also has some disadvantages, such as:
  - It may cause more aborts and restarts, especially when the contention for data items is high.
  - It may require more storage space, as transactions need to keep copies of the data items they have read and modified.
  - It may require more communication, as transactions need to validate their read sets with the database or other transactions.
- OCC is suitable for distributed systems, where locking-based techniques may be impractical or inefficient due to the network latency and the possibility of node failures.
- OCC can be implemented in different ways, such as using timestamps, versions, or validation protocols . The choice of the implementation depends on the characteristics of the system and the application .



# Timestamp ordering

- Timestamp ordering is a technique for ensuring serializability of transactions in a distributed system.
- A transaction is a sequence of operations that must be executed atomically, i.e., either all or none of them are performed.
- Serializability is the property that the concurrent execution of transactions produces the same result as some sequential execution of them.
- Timestamp ordering assigns a unique timestamp to each transaction when it starts, and uses these timestamps to order the operations of different transactions.
- The timestamp of a transaction reflects its logical start time, not the physical time on the node where it executes.
- Timestamp ordering can be implemented using logical clocks, such as Lamport timestamps, which are monotonically increasing counters that are updated based on the causal dependencies among events in the system.
- Lamport timestamps have the property that if event A causally precedes event B, then the timestamp of A is less than the timestamp of B.
- Timestamp ordering can be applied to different levels of granularity, such as read and write operations, data items, or database pages.
- Timestamp ordering can be enforced by different protocols, such as basic timestamp ordering, optimistic timestamp ordering, or multiversion timestamp ordering.
- Basic timestamp ordering requires that a transaction's read or write operation on a data item is executed only if its timestamp is greater than the timestamp of the last write operation on that data item, otherwise the transaction is aborted and restarted with a new timestamp.
- Optimistic timestamp ordering allows a transaction to execute optimistically without checking timestamps, but validates its operations at commit time using timestamps, and aborts and restarts the transaction if any conflict is detected.
- Multiversion timestamp ordering maintains multiple versions of each data item, each with a timestamp of the transaction that created it, and allows a transaction to read the latest version of a data item that has a timestamp less than or equal to its own timestamp, and to write a new version of a data item with its own timestamp.



# Comparison of methods for concurrency control

Concurrency control is the process of managing the simultaneous execution of transactions in a distributed system, such that the consistency and correctness of the data are preserved. There are various methods for concurrency control, each with its own advantages and disadvantages. Some of the common methods are:

- **Two-phase locking (2PL)**: This method requires each transaction to acquire locks on the data items it needs to access, and release them after it finishes. There are two phases: the growing phase, where the transaction can only acquire locks, and the shrinking phase, where the transaction can only release locks. The transaction cannot request any new locks after it releases any lock. This method ensures serializability, which means the concurrent execution of transactions is equivalent to some serial execution. However, it may cause deadlocks, where two or more transactions are waiting for each other to release locks, and thus cannot proceed. It may also cause blocking, where a transaction has to wait for a lock held by another transaction, and thus reduces concurrency. Moreover, it does not guarantee recoverability, which means a transaction may commit before its dependencies, and thus may cause inconsistency if the dependencies abort.

- **Timestamp ordering (TO)**: This method assigns a unique timestamp to each transaction, and uses it to order the transactions. The timestamp can be either the start time or the commit time of the transaction. The system maintains a read timestamp and a write timestamp for each data item, which record the latest timestamps of transactions that have read or written the data item. A transaction can read or write a data item only if its timestamp is greater than or equal to the read and write timestamps of the data item, respectively. Otherwise, the transaction is aborted and restarted with a new timestamp. This method avoids deadlocks, as there is no cycle of waiting transactions. It also ensures recoverability, as a transaction can only depend on transactions with smaller timestamps, which must have committed before it. However, it may cause aborts, where a transaction is restarted due to a timestamp conflict, and thus wastes resources and reduces concurrency. It may also cause starvation, where a transaction is repeatedly aborted due to conflicts with other transactions, and thus cannot proceed.

- **Multi-version concurrency control (MVCC)**: This method allows multiple versions of the same data item to coexist, and assigns a timestamp to each version. A transaction can read the latest version of a data item that is older than or equal to its timestamp, and can write a new version of a data item with its timestamp. The system maintains a version list for each data item, which records the timestamps and values of the versions. A transaction can read or write a data item only if its timestamp is not in the version list of the data item, which means it does not conflict with any existing version. Otherwise, the transaction is aborted and restarted with a new timestamp. This method avoids aborts and starvation, as a transaction can always read a consistent version of a data item, and can write a new version without overwriting any existing version. It also avoids blocking, as a transaction does not have to wait for another transaction to release a lock. However, it may cause overhead, as the system has to maintain and manage multiple versions of the same data item, and thus consumes more space and time. It may also cause cascading aborts, where a transaction aborts due to a dependency on another aborted transaction, and thus affects the consistency of the data.

- **Validation concurrency control (VCC)**: This method divides the execution of a transaction into three phases: the read phase, where the transaction reads the data items it needs, the validation phase, where the transaction checks for conflicts with other transactions, and the write phase, where the transaction writes the data items it has modified. The system assigns a start timestamp and a commit timestamp to each transaction, and uses them to validate the transaction. A transaction can commit only if it does not conflict with any other committed transaction in the interval between its start timestamp and commit timestamp. Otherwise, the transaction is aborted and restarted with a new timestamp. This method avoids blocking and deadlocks, as a transaction does not acquire any locks on the data items. It also ensures recoverability, as a transaction can only depend on transactions with smaller commit timestamps, which must have committed before it. However, it may cause aborts and starvation, as a transaction may fail the validation due to conflicts with other transactions, and thus cannot proceed. It may also cause overhead, as the system has to maintain and compare the read and write sets of the transactions, and thus consumes more space and time.



## Unit 9 - Distributed Transactions

- A distributed transaction is a type of transaction that involves two or more network hosts, usually providing transactional resources, such as databases, message queues, file systems, etc.
- A distributed transaction is coordinated by a transaction manager, which is responsible for creating and managing a global transaction that encompasses all the operations against the transactional resources.
- A distributed transaction ensures the ACID (Atomicity, Consistency, Isolation, Durability) properties across multiple hosts, meaning that either all the operations succeed or none of them, the data remains consistent, the concurrent transactions do not interfere with each other, and the effects of the transaction are permanent.
- A distributed transaction can be implemented using different protocols, such as two-phase commit, three-phase commit, Paxos commit, etc. These protocols typically involve a coordinator (the transaction manager) and one or more participants (the transactional resources), and use messages to exchange information and reach consensus on the outcome of the transaction.
- A distributed transaction faces several challenges, such as network failures, host failures, concurrency issues, deadlock detection, performance overhead, etc. These challenges require careful design and implementation of the distributed transaction protocols and mechanisms.



# Flat and Nested Distributed Transactions

A distributed transaction is a transaction that accesses objects managed by multiple servers. A distributed transaction can be structured in two different ways: flat or nested.

## Flat Transactions

A flat transaction has a single begin point and a single end point (commit or abort). A flat transaction is atomic, meaning that either all of the servers involved in the transaction agree to commit the changes or all of them agree to abort the changes. A flat transaction is usually simple and short-lived, and it does not allow any subtransactions within it. A flat transaction can be implemented using a two-phase commit protocol, which involves a coordinator and a set of participants. The coordinator initiates the transaction and sends prepare messages to the participants, who vote to commit or abort. The coordinator then decides the outcome based on the votes and sends commit or abort messages to the participants, who execute the decision.

## Nested Transactions

A nested transaction is a transaction that contains other transactions as subtransactions. A nested transaction has a hierarchical structure, where the top-level transaction is the parent of all the subtransactions, and each subtransaction can have its own subtransactions. A nested transaction is also atomic, meaning that either the whole transaction commits or the whole transaction aborts. However, a nested transaction allows partial commits, meaning that some subtransactions can commit while others abort, as long as the parent transaction can compensate for the aborted subtransactions. A nested transaction can be implemented using a nested two-phase commit protocol, which extends the two-phase commit protocol to handle subtransactions. The nested two-phase commit protocol involves a root coordinator, a set of top-level participants, and a set of sub-coordinators. The root coordinator initiates the top-level transaction and sends prepare messages to the top-level participants, who vote to commit or abort. The top-level participants also act as sub-coordinators for their subtransactions, and they send prepare messages to their sub-participants, who vote to commit or abort. The sub-coordinators then decide the outcome of their subtransactions based on the votes and send commit or abort messages to their sub-participants, who execute the decision. The sub-coordinators also send their subtransaction outcomes to the root coordinator, who decides the outcome of the top-level transaction based on the subtransaction outcomes and sends commit or abort messages to the top-level participants, who execute the decision.

## Comparison

Flat and nested transactions have different advantages and disadvantages. Flat transactions are simpler and faster, but they do not allow concurrency and modularity. Nested transactions are more complex and slower, but they allow concurrency and modularity. Flat transactions are suitable for short and simple transactions that do not require any subtransactions. Nested transactions are suitable for long and complex transactions that require subtransactions. Flat transactions provide global consistency over multiple resources. Nested transactions provide local consistency over multiple resources and global consistency over the top-level transaction. Flat transactions use a single coordinator and a single phase of voting. Nested transactions use multiple coordinators and multiple phases of voting. Flat transactions do not allow partial commits. Nested transactions allow partial commits and compensation.



# Atomic Commit Protocols for Distributed Transactions

- A distributed transaction is a transaction that involves multiple servers or nodes in a distributed system.
- An atomic commit protocol is a protocol that ensures that a distributed transaction is either committed or rolled back in its entirety, even if the system fails or some of the nodes fail or crash.
- Ensuring atomic commit is important for maintaining the consistency and integrity of the data in a distributed system.
- There are different types of atomic commit protocols, such as two-phase commit, three-phase commit, parallel commit, and failure-aware commit.
- Two-phase commit (2PC) is the most widely used atomic commit protocol. It consists of two phases: a prepare phase and a commit phase. In the prepare phase, a coordinator node asks all the participant nodes to vote on whether they are ready to commit or not. In the commit phase, the coordinator node decides whether to commit or abort the transaction based on the votes, and informs all the participant nodes of the decision.
- Three-phase commit (3PC) is an extension of 2PC that adds a pre-commit phase between the prepare and commit phases. In the pre-commit phase, the coordinator node informs all the participant nodes of its decision to commit, and waits for their acknowledgments. In the commit phase, the coordinator node confirms the commit decision to all the participant nodes. 3PC can tolerate more failures than 2PC, but it has higher latency and message overhead.
- Parallel commit is a new atomic commit protocol that reduces the latency of transactions down to only a single round-trip of distributed consensus. It does not use a coordinator node, but instead relies on each participant node to independently decide whether to commit or abort the transaction based on a timestamp and a commit trigger. A commit trigger is a condition that indicates that all the participant nodes have agreed to commit the transaction. Parallel commit can achieve high performance and availability, but it requires a precise clock synchronization and a reliable distributed consensus mechanism.
- Failure-aware commit (FLAC) is another new atomic commit protocol that aims to improve the performance and availability of distributed transactions in the presence of failures. It uses a two-phase transaction processing framework, where each participant node executes the transaction in the first phase, and commits or aborts the transaction in the second phase. FLAC does not use a coordinator node, but instead uses a failure detector to monitor the status of each participant node. FLAC can dynamically adjust the commit decision based on the failure information, and can avoid blocking or aborting transactions unnecessarily. FLAC can achieve better performance and availability than 2PC and 3PC, but it requires a reliable failure detector and a distributed consensus mechanism.



# Concurrency control in distributed transactions

- Concurrency control is the process of managing the concurrent execution of transactions in a distributed database system, such that the ACID properties are preserved.
- Concurrency control aims to prevent conflicts and anomalies that may arise due to the interleaving of operations from different transactions, such as lost updates, dirty reads, unrepeatable reads, and phantom reads.
- Concurrency control can be achieved by using various techniques, such as locking, timestamping, optimistic methods, and validation  .
- Locking-based concurrency control protocols use the concept of locking data items to prevent concurrent transactions from accessing or modifying them. Locks can be shared or exclusive, and can be granted or denied by a lock manager. Locking protocols can be classified into two-phase locking (2PL), rigorous 2PL, conservative 2PL, and tree-structured locking.
- Timestamp-based concurrency control algorithms use a transaction’s timestamp to determine the order of execution and to detect conflicts. Timestamps can be assigned by a global clock or by a logical counter. Timestamp protocols can be classified into basic timestamp ordering (BTO), conservative BTO, and multiversion timestamp ordering (MVTO).
- Optimistic concurrency control methods assume that conflicts are rare and allow transactions to execute without any synchronization. However, before committing, each transaction has to validate its read and write sets against other transactions. If a conflict is detected, the transaction is aborted and restarted. Optimistic methods can be classified into basic optimistic concurrency control (BOCC), optimistic concurrency control with forward validation (OCCFV), and optimistic concurrency control with backward validation (OCCBV).
- Validation-based concurrency control methods use a validation phase to check whether a transaction can commit or not, based on some predefined rules. Validation methods can be classified into primary copy scheme, majority consensus scheme, and quorum consensus scheme.
- Distributed concurrency control protocols have to deal with additional challenges, such as network delays, communication failures, partial failures, and data replication  .
- Distributed concurrency control protocols can be classified into centralized, decentralized, and hierarchical, depending on the architecture of the distributed system and the location of the lock manager or the timestamp generator  .
- Distributed concurrency control protocols can also be classified into pessimistic, optimistic, and hybrid, depending on the degree of synchronization and validation required  .
- Distributed concurrency control protocols have to balance the trade-offs between performance, consistency, availability, and fault-tolerance   .



# Distributed Deadlocks

- A **distributed deadlock** is a situation where a set of processes in a distributed system are waiting for each other to release resources or messages, and none of them can proceed  .
- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems .
- Distributed deadlocks are harder to detect, avoid, and prevent than deadlocks in centralized systems, because there is no single authority that can oversee resource allocation and monitor the state of the system.
- There are three main approaches to handle distributed deadlocks :
  - **Prevention**: This approach tries to prevent deadlocks from occurring by imposing some constraints on resource allocation, such as ordering the resources, limiting the number of resources per process, or using timeouts. However, this approach may reduce the concurrency and performance of the system, and may not be applicable to all types of resources.
  - **Avoidance**: This approach tries to avoid deadlocks by dynamically analyzing the resource requests and granting them only if they do not lead to a potential deadlock. This approach requires the knowledge of the current and future resource requirements of each process, which may not be available or accurate in a distributed system. Moreover, this approach may incur a high overhead of communication and computation.
  - **Detection and resolution**: This approach tries to detect deadlocks after they occur and then resolve them by aborting or restarting some of the processes involved in the deadlock. This approach does not impose any restrictions on resource allocation, but it requires a mechanism to detect deadlocks and a policy to resolve them. There are two main techniques for deadlock detection in distributed systems :
    - **Global wait-for graph**: This technique involves constructing a global graph that represents the dependencies among processes and resources in the system, and then checking for cycles in the graph. A cycle in the graph indicates a deadlock. To construct the global graph, each node in the system maintains a local graph of its own processes and resources, and periodically sends it to a designated deadlock detector node. The deadlock detector node merges the local graphs into a global graph and checks for cycles. This technique requires a lot of communication and synchronization among the nodes, and may not be able to detect deadlocks in a timely manner.
    - **Distributed algorithm**: This technique involves a cooperative effort among the nodes in the system to detect deadlocks. One such algorithm is **edge chasing**, which works as follows: When a process requests a resource that is held by another process, it sends a probe message to the holder process. The probe message contains the identity of the sender and the requested resource. If the holder process is not waiting for any resource, it replies with a grant message. If the holder process is waiting for another resource, it forwards the probe message to the process that holds that resource. This way, the probe message follows the dependency chain of processes and resources in the system. If the probe message returns to the original sender, it means that there is a cycle in the dependency chain, and hence a deadlock. This technique requires less communication and synchronization than the global graph technique, but it may generate false positives or negatives due to concurrency and delays in the system.



# Transaction Recovery for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

- Transaction recovery is the process of restoring a distributed database system to a consistent state after a failure of a site, a communication network, or a transaction .
- Transaction recovery is essential to ensure the ACID properties of transactions, especially atomicity and durability.
- Transaction recovery involves two main steps: failure detection and failure recovery.
- Failure detection is the process of identifying the sites, transactions, or messages that are affected by a failure.
- Failure recovery is the process of applying appropriate actions to restore the consistency of the database and complete the transactions.
- There are different types of failures that can occur in a distributed system, such as site failures, network failures, transaction failures, and media failures.
- There are different techniques for transaction recovery, such as logging, shadow versions, checkpoints, and two-phase commit   .
- Logging is a technique that records the changes made by transactions in a log file, which can be used to undo or redo the operations in case of a failure   .
- Shadow versions is a technique that maintains multiple versions of the database objects, and updates them only when a transaction commits successfully .
- Checkpoints is a technique that periodically saves the state of the database and the transactions, which can be used to reduce the recovery time and the amount of logging  .
- Two-phase commit is a protocol that coordinates the commit or abort decision of a distributed transaction among all the participating sites  .



## Unit 10 - Replication

- Replication is the process of creating and maintaining multiple copies of the same data on different database servers.
- Replication provides benefits such as high availability, fault tolerance, load balancing, and scalability.
- Replication can be classified into two types: synchronous and asynchronous.
  - Synchronous replication ensures that all changes made to the data on one server are immediately applied to the copies on other servers. This guarantees data consistency, but may incur performance overhead and network latency.
  - Asynchronous replication allows changes made to the data on one server to be applied to the copies on other servers at a later time. This improves performance and network efficiency, but may result in data inconsistency or conflicts.
- Replication can be implemented using different methods, such as snapshot, transactional, merge, and peer-to-peer replication.
  - Snapshot replication creates a full copy of the data on one server and distributes it to other servers at specified intervals. This is suitable for static or slowly changing data, but may consume a lot of network bandwidth and storage space.
  - Transactional replication captures and distributes only the changes made to the data on one server to other servers. This is suitable for dynamic or frequently changing data, but may require a lot of processing and logging resources.
  - Merge replication allows changes made to the data on different servers to be merged and synchronized. This is suitable for distributed or disconnected environments, but may require conflict resolution and reconciliation mechanisms.
  - Peer-to-peer replication allows changes made to the data on any server to be propagated to all other servers. This is suitable for high availability and scalability, but may require complex configuration and management.



# System model and group communication for replication in distributed systems

- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by exchanging messages.
- Replication is a technique to improve the availability, reliability, and performance of a distributed system by creating and maintaining multiple copies of data or services across different processes or nodes.
- A system model is a set of assumptions and properties that characterize the behavior and capabilities of a distributed system, such as the communication model, the failure model, the timing model, and the security model.
- Group communication is a form of communication between multiple processes in a distributed system that share some common interest or goal, such as replicating data or coordinating actions.
- Group communication can be classified into two types: broadcast communication and multicast communication.
  - Broadcast communication is when a source process sends a message to all other processes in the system, regardless of their interest or membership in a group. Broadcast communication can be used to disseminate information widely and efficiently, such as code or a file, or to discover other processes in the system.
  - Multicast communication is when a source process sends a message to a subset of processes in the system that belong to a specific group. Multicast communication can be used to implement replication, as the source process can update or query the replicas of data or services in the group.
- Group communication can also be classified into two categories: reliable and unreliable.
  - Reliable group communication is when the communication guarantees some properties, such as delivery, ordering, or agreement, of the messages sent and received by the group members. Reliable group communication can be used to ensure consistency and correctness of the replicated data or services in the group.
  - Unreliable group communication is when the communication does not guarantee any properties of the messages sent and received by the group members. Unreliable group communication can be used to achieve higher performance and scalability of the replicated data or services in the group, at the cost of some inconsistency or inaccuracy.
- Group communication can be implemented using various protocols and algorithms, such as IP multicast, gossip, Paxos, or Raft, depending on the system model and the replication requirements.



# Fault-Tolerant Services for the Notes of the Unit 10 - Replication in the Subject of Distributed System

- Fault-tolerant services are services that can continue to function correctly even in the presence of failures, such as server crashes, network partitions, or malicious attacks.
- Replication is a technique for implementing fault-tolerant services by creating and maintaining multiple copies of the same data or state across different servers or nodes in a distributed system.
- Replication can improve the availability, performance, and reliability of a service, but also introduces challenges such as consistency, concurrency, and coordination among replicas.
- There are two main classes of replication techniques: primary-backup replication and active replication.
  - Primary-backup replication: One replica is designated as the primary, and the others are backups. The primary receives all the requests from the clients, executes them, and sends the updates to the backups. The backups apply the updates in the same order as the primary. If the primary fails, one of the backups takes over as the new primary.
  - Active replication: All replicas receive the same requests from the clients, execute them independently, and send the results back to the clients. The clients use a majority voting scheme to determine the correct result. If a replica fails, the remaining replicas can still provide the service.
- The correctness criterion for replicated services is linearizability, which means that the service appears as if there is only one copy of the data or state, and every operation appears to take effect atomically at some point between its invocation and response.
- To achieve linearizability, replicas need to agree on the order of the requests they receive and execute. This can be done by using consensus protocols, such as Paxos or Raft, or by using logical clocks, such as vector clocks or Lamport timestamps, to assign a unique and consistent order to each request.
- Replication can also be used to tolerate Byzantine faults, which are arbitrary or malicious behaviors of some replicas or clients. Byzantine fault-tolerant replication requires more replicas and more communication than crash fault-tolerant replication, and relies on cryptographic techniques, such as digital signatures and message authentication codes, to prevent or detect tampering with the messages.
- Replication can be done at different levels of granularity, such as data, objects, or state machines. Data replication is the most common form of replication, and can be further classified into passive replication and active replication.
  - Passive replication: The data is replicated on demand, when a client requests it. The client contacts a directory service to locate a replica that has the data, and reads or writes to that replica. The replica then propagates the update to the other replicas, either eagerly or lazily. Passive replication can reduce the communication overhead and improve the scalability of the system, but can also introduce inconsistency among replicas.
  - Active replication: The data is replicated proactively, before a client requests it. The client broadcasts the request to all the replicas, and waits for the responses from a majority of them. Active replication can ensure strong consistency and fault tolerance, but can also increase the communication overhead and reduce the performance of the system.



# Highly Available Services for the Notes of the Unit 10 - Replication in the Subject of Distributed System

- Replication is the process of creating and maintaining multiple copies of data or services in a distributed system.
- Replication can improve the availability, reliability, performance, and scalability of a distributed system.
- Replication can also introduce challenges such as consistency, concurrency, and fault tolerance.
- There are different types of replication, such as:
  - **Eager replication**: The updates are propagated to all the replicas as soon as they occur, ensuring strong consistency but increasing communication and synchronization overhead.
  - **Lazy replication**: The updates are propagated to the replicas periodically or on demand, allowing temporary inconsistency but reducing communication and synchronization overhead.
  - **Full replication**: All the data or services are replicated on all the nodes, maximizing availability and fault tolerance but consuming more resources and bandwidth.
  - **Partial replication**: Only a subset of the data or services are replicated on some of the nodes, saving resources and bandwidth but requiring more complex management and coordination.
- There are different techniques for implementing replication, such as:
  - **Primary-backup replication**: One of the replicas is designated as the primary, which receives all the updates and propagates them to the backups. The backups are passive and only become active when the primary fails. This technique ensures strong consistency but introduces a single point of failure and a performance bottleneck.
  - **Active replication**: All the replicas are active and receive the same updates in the same order. The updates are executed by all the replicas independently and the results are compared to detect and correct faults. This technique ensures strong consistency and fault tolerance but requires more communication and synchronization among the replicas.
  - **Quorum-based replication**: The updates are executed by a subset of the replicas, called a write quorum, and the reads are performed by another subset of the replicas, called a read quorum. The quorums are chosen such that they overlap, ensuring consistency and availability. This technique reduces the communication and synchronization overhead but requires more complex quorum management and coordination.
  - **Gossip-based replication**: The updates are propagated to the replicas randomly or probabilistically, using a gossip protocol. The replicas exchange their updates with each other and eventually converge to a consistent state. This technique is scalable and resilient to failures but allows temporary inconsistency and may not guarantee eventual consistency.



# Transactions with replicated data

- Transactions are a sequence of operations that are executed atomically, consistently, isolatedly, and durably (ACID properties) on a database system.
- Replication is the process of copying and maintaining data in multiple locations to increase availability, performance, and fault tolerance.
- Transactions with replicated data are transactions that involve accessing and updating data that is replicated across multiple servers or nodes in a distributed system.
- Transactions with replicated data pose several challenges, such as:
  - How to ensure that the replicas are consistent and synchronized with each other?
  - How to handle concurrency and conflicts among transactions that access the same or different replicas?
  - How to recover from failures and maintain the ACID properties of transactions?
- There are different approaches to address these challenges, such as:
  - Primary-copy replication: One replica is designated as the primary or master, and the others are secondary or slave replicas. All updates are performed on the primary replica, and then propagated to the secondary replicas. Read operations can be performed on any replica. This approach simplifies consistency and concurrency control, but introduces a single point of failure and a bottleneck for updates.
  - Update-everywhere replication: All replicas are equal, and updates can be performed on any replica. The replicas communicate with each other to coordinate and propagate the updates. Read operations can be performed on any replica. This approach improves availability and performance, but complicates consistency and concurrency control, and requires more communication overhead.
  - Quorum-based replication: Each replica has a vote, and a quorum is a subset of replicas that has enough votes to perform an operation. For example, a read quorum is a subset of replicas that can provide a consistent read, and a write quorum is a subset of replicas that can perform a consistent update. A transaction needs to obtain a read quorum and a write quorum to execute. This approach balances availability and consistency, but requires a trade-off between the size and the overlap of the quorums.

