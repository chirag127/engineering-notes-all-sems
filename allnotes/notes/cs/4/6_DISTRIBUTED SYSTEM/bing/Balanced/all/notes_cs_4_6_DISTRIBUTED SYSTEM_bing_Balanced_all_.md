

# Unit 1 - Characterization of Distributed Systems

A distributed system is a system in which components located at networked computers communicate and coordinate their actions only by passing messages . The components of a distributed system may be hardware devices, software processes, or data sources. The end-users of a distributed system perceive it as a single coherent system that provides some functionality .

Some of the main characteristics of distributed systems are:

- **Resource sharing**: The components of a distributed system can share resources such as hardware, software, or data with other components, either transparently or selectively . Resource sharing enables the system to achieve higher performance, scalability, and availability.
- **Openness**: The components of a distributed system can be easily extended and improved by adding new components or replacing existing ones, without affecting the rest of the system . Openness also implies that the system follows some standard protocols and interfaces for communication and interoperability.
- **Concurrency**: The components of a distributed system can execute concurrently, meaning that they can perform multiple tasks at the same time . Concurrency allows the system to exploit parallelism and increase efficiency and responsiveness.
- **Lack of a global clock**: The components of a distributed system do not have a common notion of time, as they may have different local clocks that are not synchronized . This makes it difficult to coordinate the actions of the components and to order the events that occur in the system.
- **Independent failures**: The components of a distributed system can fail independently, without affecting the whole system . This means that the system has to cope with partial failures and ensure fault tolerance and reliability.

Some of the main challenges of distributed systems are:

- **Heterogeneity**: The components of a distributed system may have different hardware architectures, operating systems, programming languages, or network protocols . This makes it hard to ensure compatibility and interoperability among the components and to provide a uniform interface to the end-users.
- **Security**: The components of a distributed system may be exposed to various threats such as unauthorized access, data tampering, denial of service, or malicious attacks . This requires the system to implement mechanisms for authentication, authorization, encryption, and auditing.
- **Scalability**: The components of a distributed system may have to handle a large number of requests, users, or data, which may vary over time . This demands the system to adapt to the changing load and to maintain acceptable performance and quality of service.
- **Transparency**: The components of a distributed system should hide their complexity and heterogeneity from the end-users and provide them with a consistent and coherent view of the system . Transparency can be achieved at different levels, such as access, location, migration, replication, concurrency, or failure.
- **Consistency**: The components of a distributed system should provide the end-users with a consistent view of the data and the state of the system, despite the concurrency, replication, and failures that may occur . Consistency can be defined in different ways, such as sequential, causal, or eventual, depending on the application requirements and the trade-offs involved.



# Introduction for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- A distributed system has the following characteristics:
  - Concurrency: The components of the system can execute concurrently, without interfering with each other.
  - No global clock: The components of the system do not share a common notion of time, and may have different local clocks.
  - Independent failures: The components of the system can fail independently, without affecting the whole system.
  - Heterogeneity: The components of the system can have different hardware, software, network, and data formats.
- A distributed system has the following advantages:
  - Scalability: The system can grow in size and complexity, by adding more components or resources.
  - Availability: The system can tolerate failures and provide continuous service, by replicating or recovering the components.
  - Performance: The system can exploit parallelism and locality, by distributing the workload and data among the components.
  - Resource sharing: The system can allow the components to access and share common resources, such as files, printers, databases, etc.
- A distributed system has the following challenges:
  - Transparency: The system should hide the complexity and diversity of the components, and provide a uniform and consistent view to the users.
  - Coordination: The system should synchronize and coordinate the actions and states of the components, and ensure consistency and correctness.
  - Security: The system should protect the components and the data from unauthorized access, modification, or damage.
  - Fault tolerance: The system should detect and handle the failures of the components, and ensure reliability and availability.



# Examples of Distributed Systems

A distributed system is a collection of independent computers that communicate and coordinate their actions by passing messages. The computers in a distributed system may be physically close or geographically dispersed, and they may be connected by a network or a bus. Distributed systems can provide high availability, scalability, fault tolerance, and performance.

Some examples of distributed systems are:

- **Telecommunication networks**: Telephone networks are an early example of a peer-to-peer network. Cellular and telephone networks are forms and examples of distributed networks. They allow users to communicate with each other over long distances, and they use routing algorithms to find the best path for each call. Telecommunication networks also include the Internet, which is a global network of networks that connects millions of computers and devices .
- **Real-time systems**: Many industries use real-time systems distributed in various areas, locally and globally. Real-time systems have strict timing constraints and must respond to events within a specified deadline. For example, air traffic control systems, industrial control systems, and online gaming systems are real-time systems that use distributed computing to coordinate and synchronize their actions .
- **Distributed database systems**: A distributed database has locations across multiple servers, physical locations, or both. A distributed database can improve the availability, reliability, and performance of data access and processing. For example, a bank may use a distributed database to store customer information and transactions across different branches and regions. A distributed database system also allows concurrent access and updates from multiple users .
- **Distributed computing platforms**: A distributed computing platform is a software framework that enables the development and execution of distributed applications. A distributed application is composed of multiple components that run on different machines and communicate via messages. For example, cloud computing, grid computing, and cluster computing are distributed computing platforms that provide various services and resources to users and applications. Examples of distributed applications include web applications, scientific computing, and big data analytics .



# Resource sharing for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Resource sharing is one of the main motivations for constructing distributed systems  .
- Resource sharing means the ability to use any hardware, software, or data anywhere in the system.
- Resources can be managed by servers and accessed by clients, or they can be encapsulated as objects and accessed by other client objects.
- Resource sharing can vary widely in scope and in how close users collaborate together.
- Examples of resource sharing include:
  - Search engines, which provide access to a large collection of web pages and other information resources.
  - Computer-Supported Cooperative Work (CSCW), which enables users to work together on a common task or project using shared documents, applications, and communication tools.
  - Distributed file systems, which allow users to access and manipulate files stored on remote servers as if they were local files.
  - Distributed databases, which allow users to query and update data stored on multiple servers using a common interface and consistency model.
  - Distributed multimedia systems, which allow users to stream and synchronize audio and video content from different sources.
  - Distributed computing platforms, which allow users to exploit the computational power and storage capacity of multiple machines for parallel or distributed applications.
- Resource sharing can pose several challenges and requirements for distributed systems, such as:
  - Scalability, which means the ability to handle increasing numbers of users, resources, and requests without degrading the performance or functionality of the system.
  - Transparency, which means the ability to hide the complexity and heterogeneity of the system from the users and provide a uniform and consistent view of the resources.
  - Reliability, which means the ability to cope with failures and errors in the system and ensure the availability and correctness of the resources.
  - Security, which means the ability to protect the resources and the users from unauthorized access, modification, or disclosure.
  - Openness, which means the ability to extend and improve the system and allow interoperability and compatibility with other systems .



# The Web Challenges for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- The web is an example of a distributed system that allows resource sharing and communication among different devices across the internet.
- However, the web also poses several challenges for the design and implementation of distributed systems, such as:

  - Scalability: The ability to handle increasing load and demand without degrading the performance or functionality of the system. For example, a web server should be able to serve more requests as the number of users grows, without slowing down or crashing.
  - Heterogeneity: The diversity and compatibility of different devices, platforms, languages, protocols, and formats that are involved in a distributed system. For example, a web browser should be able to display and interact with web pages that are created using different technologies, such as HTML, CSS, JavaScript, etc.
  - Security: The protection of the system and its resources from unauthorized access, modification, or damage. For example, a web application should be able to authenticate the users, encrypt the data, and prevent attacks, such as phishing, malware, denial-of-service, etc.
  - Reliability: The ability to function correctly and consistently despite the presence of failures, errors, or faults in the system or its components. For example, a web service should be able to recover from network failures, server crashes, or data corruption, and provide consistent results to the users.
  - Consistency: The agreement and coherence of the data and the state of the system across different replicas, nodes, or locations. For example, a web database should be able to ensure that the data is updated and synchronized across all the copies, and that the users see the same view of the data.
  - Transparency: The hiding of the complexity and the details of the distributed system from the users and the developers. For example, a web user should not be aware of the location, the identity, or the implementation of the web server that is providing the service, and a web developer should not have to deal with the low-level details of the network communication, the concurrency, or the synchronization.



# Architectural models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Architectural models are a type of system model that describe the organization of components across the network and their interrelationship .
- Architectural models can help to design, implement, and evaluate distributed systems by providing a high-level view of the system structure and behavior.
- Architectural models can also help to identify the challenges and trade-offs involved in distributed computing, such as scalability, availability, consistency, security, and performance .
- There are various hardware and software architectures that are commonly used for distributed computing, such as client-server, peer-to-peer, broker, service-oriented, and cloud architectures  .
- Each architectural model has its own advantages and disadvantages, depending on the requirements and constraints of the application domain and the network environment .
- Some of the factors that influence the choice of an architectural model are the degree of decentralization, the level of abstraction, the communication paradigm, the resource management, and the fault tolerance .
- A distributed system can also combine different architectural models to achieve the desired functionality and quality attributes, such as service resiliency, performance gains, and automated resource sharing .
- Architectural models are not fixed or static, but can evolve over time to adapt to changing needs and technologies .



# Fundamental Models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Fundamental models are descriptions of properties that are present in all distributed architectures  .
- They help us understand the characteristics, challenges and trade-offs of designing and implementing distributed systems.
- There are three main types of fundamental models: interaction models, failure models and security models  .

## Interaction Models
- Interaction models deal with the issues of communication and coordination among processes in a distributed system  .
- They include aspects such as performance, timing, ordering and synchronization of events  .
- Some examples of interaction models are:
  - Synchronous vs. asynchronous communication: whether the sender and receiver of a message have to wait for each other or not  .
  - Remote procedure call (RPC): a method of invoking a procedure on a remote machine as if it were local  .
  - Publish-subscribe: a pattern of communication where publishers send messages to a broker, and subscribers receive messages that match their interests  .
  - Message passing interface (MPI): a standard for parallel programming that supports point-to-point and collective communication among processes  .

## Failure Models
- Failure models specify the types of faults that can occur in a distributed system and how they affect the processes and communication channels  .
- They help us design fault-tolerant mechanisms and protocols to ensure the reliability and availability of the system  .
- Some examples of failure models are:
  - Crash failure: a process stops executing and does not resume  .
  - Omission failure: a process fails to send or receive a message  .
  - Timing failure: a process does not meet the timing constraints of the system  .
  - Byzantine failure: a process behaves arbitrarily or maliciously  .

## Security Models
- Security models define the goals and threats of a distributed system in terms of confidentiality, integrity and availability  .
- They help us design cryptographic techniques and protocols to protect the system from unauthorized access and manipulation  .
- Some examples of security models are:
  - Symmetric-key cryptography: a method of encryption and decryption that uses the same secret key for both parties  .
  - Public-key cryptography: a method of encryption and decryption that uses a pair of keys: a public key that can be shared and a private key that is kept secret  .
  - Digital signature: a technique that allows a sender to prove the authenticity and integrity of a message using a private key  .
  - Authentication: a process that verifies the identity of a user or a process  .



# Theoretical Foundation for Distributed System

- A distributed system is a system whose components are located on different networked computers, which communicate and coordinate their actions by passing messages to one another.
- Distributed systems have some inherent limitations, such as the absence of a global clock, the lack of shared memory, and the possibility of arbitrary delays and failures in message passing .
- To cope with these limitations, distributed systems need some theoretical foundations that can provide models, abstractions, and algorithms for designing and analyzing distributed algorithms and platforms.
- Some of the key theoretical foundations for distributed systems are:
  - **Logical clocks**: A logical clock is a mechanism to order events in a distributed system, without relying on physical clocks. A logical clock assigns a logical timestamp to each event, such that if event A causally precedes event B, then the timestamp of A is smaller than the timestamp of B. There are different types of logical clocks, such as Lamport's clocks and vector clocks, that have different properties and trade-offs.
  - **Consensus**: Consensus is a fundamental problem in distributed systems, where a set of processes have to agree on a common value, despite the possibility of failures and asynchrony. Consensus is essential for achieving coordination, consistency, and fault tolerance in distributed systems. There are different algorithms and impossibility results for solving consensus, depending on the system model and assumptions.
  - **Distributed mutual exclusion**: Distributed mutual exclusion is a problem of ensuring that at most one process can access a shared resource at a time, without using a centralized coordinator or a shared memory. Distributed mutual exclusion is important for maintaining data integrity and avoiding conflicts in distributed systems. There are different algorithms and performance metrics for achieving distributed mutual exclusion, such as token-based, permission-based, and quorum-based algorithms.
  - **Distributed deadlock detection**: Distributed deadlock detection is a problem of detecting and resolving situations where a set of processes are waiting for each other in a circular manner, and none of them can proceed. Distributed deadlock detection is crucial for avoiding resource starvation and improving system throughput in distributed systems. There are different algorithms and techniques for detecting and resolving distributed deadlocks, such as edge-chasing, probe-based, and path-pushing algorithms.



# Limitation of Distributed System

A distributed system is a system that consists of multiple independent components that communicate with each other over a network. Distributed systems have many advantages, such as scalability, fault-tolerance, availability, and performance. However, they also face some limitations that make them challenging to design and implement. Some of the main limitations of distributed systems are:

- **Absence of a global state**: In a distributed system, there is no single point of control or coordination for the entire system. Each component has its own local state and view of the system, which may differ from the views of other components. This makes it difficult to reason about the behavior and correctness of the system, and to synchronize the actions and data of different components. For example, in a distributed database, there may be inconsistencies or conflicts between the data stored on different nodes, which need to be resolved by using protocols such as consensus or replication.

- **Absence of a global clock**: In a distributed system, there is no common notion of time or ordering of events for the entire system. Each component has its own local clock, which may not be synchronized with the clocks of other components. This makes it hard to measure the latency and performance of the system, and to coordinate the timing and ordering of operations and messages. For example, in a distributed system, it may be impossible to determine which of two concurrent events happened first, or how long it took for a message to be delivered from one node to another.

- **Network failures and partitions**: In a distributed system, the network that connects the components is prone to failures and delays, which may affect the availability and reliability of the system. For example, a network failure may cause some nodes to be unreachable or isolated from the rest of the system, creating a network partition. This may result in data loss, inconsistency, or duplication, or prevent the system from reaching a consensus or completing a transaction. To cope with network failures and partitions, distributed systems need to use techniques such as timeouts, retries, acknowledgments, and fault-tolerance protocols.

- **Security and privacy issues**: In a distributed system, the components may be located in different physical or logical domains, which may have different levels of trust and security. For example, some nodes may be malicious or compromised, and may try to disrupt, manipulate, or eavesdrop on the system. This may compromise the confidentiality, integrity, or availability of the system, or violate the privacy of the users or the data. To address security and privacy issues, distributed systems need to use mechanisms such as encryption, authentication, authorization, and auditing.



# Absence of Global Clock

- A global clock is a system-wide clock that is equally accessible to all processes in a distributed system and provides a common notion of time.
- A global clock is useful for determining the order of events and the state of the system across different processes.
- However, a global clock is hard to realize in distributed systems due to two inherent limitations: lack of shared memory and unpredictable message delays.
- Lack of shared memory means that processes in a distributed system do not have access to a common storage that can store and update the global clock value.
- Unpredictable message delays mean that the communication channel between processes is not reliable and can introduce variable and unknown delays in message transmission.
- As a result, different processes may have different and inaccurate views of the global clock value, and the notion of common time does not exist in a distributed system.
- This also makes it difficult to obtain a meaningful and consistent state of the system, as the states of different processes may not be synchronized with each other.
- Therefore, the absence of a global clock poses a challenge for designing and implementing distributed systems that require coordination, synchronization, and consistency among processes.



# Shared Memory

Shared memory is a programming model for distributed systems that allows multiple processes to access a common logical address space, as if they were running on a single machine. Shared memory can simplify the communication and synchronization among processes, and enable the implementation of parallel algorithms and data structures.

There are two types of shared memory models: physical and virtual.

## Physical Shared Memory

Physical shared memory refers to a system where multiple processors are connected to a single memory module, or a shared bus that interconnects multiple memory modules. Each processor can directly access any memory location by issuing a load or store instruction. Physical shared memory systems are also known as symmetric multiprocessors (SMPs) or uniform memory access (UMA) systems.

The advantages of physical shared memory are:

- It provides a simple and uniform programming model, where all processes can access the same variables and data structures without explicit message passing.
- It allows for low-latency and high-bandwidth communication among processes, as they do not need to copy data across the network.
- It supports fine-grained parallelism, where processes can operate on small chunks of data without incurring significant overhead.

The disadvantages of physical shared memory are:

- It is limited by the scalability and cost of the hardware, as adding more processors and memory modules increases the complexity and contention of the shared bus or interconnect.
- It requires hardware support for cache coherence, which ensures that all processors see a consistent view of the memory. Cache coherence protocols can introduce additional overhead and complexity, and may not be suitable for some applications.
- It does not tolerate faults well, as a failure of a processor or a memory module can affect the entire system.

## Virtual Shared Memory

Virtual shared memory refers to a system where multiple processors have their own local memory, but they can access a common logical address space that is distributed across the network. Virtual shared memory systems are also known as distributed shared memory (DSM) systems or non-uniform memory access (NUMA) systems.

The advantages of virtual shared memory are:

- It can scale to a large number of processors and memory modules, as they are connected by a network that can be expanded and reconfigured easily.
- It can tolerate faults better, as a failure of a processor or a memory module can be isolated and recovered from by the rest of the system.
- It can exploit locality, where processes can access their local memory faster than the remote memory, and reduce the network traffic and latency.

The disadvantages of virtual shared memory are:

- It requires software support for consistency, which ensures that all processes see a coherent view of the memory. Consistency protocols can introduce additional overhead and complexity, and may not be suitable for some applications.
- It provides a less uniform and more complex programming model, where processes need to be aware of the distribution and location of the memory, and may need to use explicit message passing or synchronization primitives.
- It supports coarse-grained parallelism, where processes need to operate on large chunks of data to amortize the network overhead.

There are different ways of implementing virtual shared memory, such as page-based, object-based, or tuple-based approaches. Each approach has its own trade-offs and challenges, such as granularity, coherence, replication, migration, and synchronization.



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
  - Efficiency: The logical clock algorithm should minimize the communication and computation overhead .



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
- Lamport's logical clocks are widely used in distributed systems to provide a logical ordering of events, but they do not capture the causal dependencies among events. For that, vector clocks are needed.



# Concepts in Message Passing Systems

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



# Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- Causal order is a partial order of messages in a distributed system that reflects the causal dependencies between events.
- Causal order is based on the happened-before relation, which is defined as follows:
  - If event a and event b occur in the same process, and a occurs before b, then a happened-before b (denoted as a -> b).
  - If event a is the sending of a message by one process and event b is the receipt of that message by another process, then a -> b.
  - If a -> b and b -> c, then a -> c (transitivity).
- Causal order ensures that if a message m1 causally precedes another message m2, then m1 is delivered before m2 to every process that receives both messages.
- Causal order is useful for maintaining consistency and coherence in distributed systems, such as replicated data, distributed transactions, and collaborative applications.
- Causal order can be implemented by various algorithms, such as vector clocks, logical clocks, or causal broadcast   .
- Causal order is weaker than total order, which requires that all messages are delivered in the same order to all processes, but stronger than unordered delivery, which does not impose any ordering constraints.



# Total Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent entities that communicate by message passing to achieve a common goal.
- Events are the occurrences of actions or changes of state in a distributed system.
- The order of events is important for understanding the behavior and correctness of a distributed system.
- A partial order is a binary relation that is reflexive, antisymmetric, and transitive. A partial order can be represented by a directed acyclic graph (DAG).
- A total order is a partial order that is also complete, meaning that any two elements are comparable. A total order can be represented by a linear sequence.
- A distributed system is said to have partial order if we can have a partial order relationship among the events in the system. If 'totality', i.e., causal relationship among all events in the system, can be established, then the system is said to have total order .
- A single entity cannot have two events occur simultaneously. However, two events in different entities may be concurrent, meaning that they are not causally related and their order is not defined.
- To establish a total order of events in a distributed system, we need a mechanism to assign timestamps to events and compare them. A timestamp is a value that reflects the occurrence time of an event.
- There are two types of timestamps: physical and logical. Physical timestamps are based on the real time of the system clocks, while logical timestamps are based on the logical order of events.
- Physical timestamps are subject to clock synchronization and drift issues, which may cause inconsistencies and anomalies in the order of events. Logical timestamps are immune to these issues, but they do not reflect the real time of events.
- One example of logical timestamps is Lamport timestamps, which are integers that are incremented by one for each event in an entity, and are updated to the maximum of the current value and the received value for each message. Lamport timestamps can be used to create a total ordering of events in a distributed system by using some arbitrary mechanism to break ties (e.g. the ID of the process) .
- Another example of logical timestamps is vector clocks, which are arrays of integers that are incremented by one for each event in an entity, and are updated to the element-wise maximum of the current value and the received value for each message. Vector clocks can be used to create a partial ordering of events in a distributed system by using the happened-before relation, which is defined as follows: if the vector clock of event A is less than or equal to the vector clock of event B in every element, then A happened before B. Vector clocks can also be used to detect concurrent events, which are those that are not related by the happened-before relation.



# Total Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent processes that communicate by exchanging messages over a network.
- Events are actions or occurrences that happen in a process, such as sending or receiving a message, executing a statement, or changing a state variable.
- The order of events in a distributed system is important for ensuring the consistency and correctness of the system's behavior and state.
- However, the order of events in a distributed system is not always obvious or unique, due to the lack of a global clock, the presence of concurrency, and the possibility of failures and delays.
- Therefore, different orderings of events can be defined based on different criteria and assumptions, such as the logical or physical time of events, the causal or potential dependencies among events, or the agreement or preference of processes.
- One of the possible orderings of events in a distributed system is the **total causal order**, which is the strictest ordering among all the orderings that respect the causal dependencies among events.
- The causal dependencies among events are defined by the **happened-before** relation, denoted by `->`, which is a partial order that satisfies the following properties:
  - If `a` and `b` are events in the same process, and `a` occurs before `b`, then `a -> b`.
  - If `a` is the event of sending a message by a process, and `b` is the event of receiving that message by another process, then `a -> b`.
  - If `a -> b` and `b -> c`, then `a -> c` (transitivity).
- The total causal order is a total order that extends the happened-before relation, meaning that it satisfies the following properties:
  - If `a -> b`, then `a` precedes `b` in the total causal order.
  - If `a` and `b` are concurrent events, meaning that neither `a -> b` nor `b -> a`, then `a` and `b` can be ordered arbitrarily in the total causal order, as long as the order is consistent for all processes.
- The total causal order establishes only one linearization, consistent with the causal ordering, among all the events that occur in the system, even those that occur concurrently. For that reason, the execution of the system is considered as synchronous.
- The total causal order can be implemented by using a **total order broadcast** protocol, which is a communication primitive that guarantees that all processes deliver the same set of messages in the same order, and that the order respects the causal dependencies among messages.
- A total order broadcast protocol can be based on different mechanisms, such as using a sequencer process, a logical clock, a vector clock, or a consensus algorithm, to assign a unique and monotonically increasing identifier to each message, and to order the messages according to their identifiers.



# Techniques for Message Ordering

Message ordering is the problem of ensuring that messages sent by different processes in a distributed system are received and processed in a consistent and predictable way. Message ordering is important for achieving coordination, consistency, and fault tolerance in distributed systems.

There are different types of message ordering techniques, depending on the desired properties and guarantees of the communication. Some of the common techniques are:

- **Non-FIFO ordering**: This is the simplest and most basic form of message ordering, where messages are delivered in any order, regardless of the order in which they were sent. This technique does not provide any guarantee of message ordering, and it may result in inconsistent or unpredictable outcomes. For example, if process A sends messages m1 and m2 to process B, and process B sends messages m3 and m4 to process A, then the possible orders of delivery are: m1, m2, m3, m4; m1, m3, m2, m4; m1, m3, m4, m2; m2, m1, m3, m4; m2, m1, m4, m3; m2, m3, m1, m4; m2, m3, m4, m1; m3, m1, m2, m4; m3, m1, m4, m2; m3, m2, m1, m4; m3, m2, m4, m1; m4, m1, m2, m3; m4, m1, m3, m2; m4, m2, m1, m3; m4, m2, m3, m1; m4, m3, m1, m2; m4, m3, m2, m1. Non-FIFO ordering is suitable for applications that do not require any ordering guarantees, such as broadcasting or multicasting messages to multiple recipients.

- **FIFO ordering**: This is a stronger form of message ordering, where messages sent by the same process are delivered in the order in which they were sent. This technique provides a guarantee of message ordering within a single sender-receiver pair, but not across different sender-receiver pairs. For example, if process A sends messages m1 and m2 to process B, and process B sends messages m3 and m4 to process A, then the possible orders of delivery are: m1, m2, m3, m4; m1, m3, m2, m4; m3, m1, m2, m4; m3, m4, m1, m2; m4, m3, m1, m2. FIFO ordering is suitable for applications that require sequential consistency, such as implementing a distributed queue or a distributed log.

- **Causal ordering**: This is a stronger form of message ordering, where messages that are causally related are delivered in the order in which they were sent. Two messages are causally related if one message depends on the occurrence or the content of the other message. For example, if process A sends message m1 to process B, and process B sends message m2 to process C after receiving m1, then m1 and m2 are causally related, and m1 must be delivered before m2. Causal ordering provides a guarantee of message ordering across different sender-receiver pairs, as long as they are causally related. For example, if process A sends messages m1 and m2 to process B, and process B sends messages m3 and m4 to process A, and process C sends messages m5 and m6 to process A, and m3 depends on m1, and m5 depends on m2, then the possible orders of delivery are: m1, m2, m3, m4, m5, m6; m1, m2, m5, m3, m4, m6; m1, m3, m2, m4, m5, m6; m1, m3, m2, m5, m4, m6. Causal ordering is suitable for applications that require causal consistency, such as implementing a distributed bulletin board or a distributed chat system.

- **Synchronous ordering**: This is the strongest form of message ordering, where messages are delivered in the same order to all processes in a group. This technique provides a guarantee of message ordering across all sender-receiver pairs, regardless of their causal relationships. For example, if process A sends messages m1 and m2 to a group



# Causal ordering of messages

- Causal ordering of messages is a partial ordering of messages in a distributed computing environment .
- It places a restriction on communication between processes by requiring that if the transmission of message mi to process pk necessarily preceded the transmission of message mj to the same process, then the delivery of these messages to that process must be ordered such that mi is delivered before mj.
- Causal ordering of messages is one of the four semantics of multicast communication, namely unordered, totally ordered, causal, and sync-ordered communication.
- Multicast communication methods vary according to the message’s reliability guarantee and ordering guarantee.
- Causal ordering of messages is based on the notion of potential causality, which is defined by the following rules :
  - If process pi sends a message m1 and then sends another message m2, then m1 -> m2 (-> denotes potential causality).
  - If process pi sends a message m1 to process pj and process pj receives m1, then m1 -> m2, where m2 is any subsequent message sent or received by process pj.
  - If m1 -> m2 and m2 -> m3, then m1 -> m3 (transitivity).
- Causal ordering of messages ensures that the messages that are causally related are delivered in the same order at all processes, while the messages that are causally unrelated can be delivered in any order .
- Causal ordering of messages can be implemented by using logical clocks, such as vector clocks or matrix clocks, to timestamp the messages and compare their causal relationships  .
- Causal ordering of messages can be useful for applications that need to maintain consistency and causality among distributed events, such as collaborative editing, distributed debugging, or replicated data management  .



# Global State

- The global state of a distributed system is a collection of the local states of the processes and the channels  .
- A local state of a process is the values of its variables and its program counter at a given point in time .
- A local state of a channel is the sequence of messages that have been sent but not yet received on that channel .
- A global state can be represented by a global state vector, which is a vector of local state vectors, one for each process and channel .
- A global state vector can be written as G = (P1, P2, ..., Pn, C1, C2, ..., Cm), where Pi is the local state vector of process i and Cj is the local state vector of channel j .
- A global state is consistent if it could have occurred during an execution of the distributed system .
- A consistent global state can be computed along a consistent cut, which is a partition of the set of events in the distributed system such that no message is received before it is sent .
- A consistent cut can be determined by using a distributed snapshot algorithm, which is a protocol that allows each process to record its local state and the state of its incoming channels without blocking the computation .
- A distributed snapshot algorithm can be based on markers, which are special messages that are sent and received by the processes to indicate the start and end of the snapshot .
- A distributed snapshot algorithm can be used for various purposes, such as detecting global predicates, checkpointing, debugging, rollback-recovery, and termination detection .



# Termination Detection for Distributed Systems

Termination detection is the problem of determining whether a distributed computation has finished or not. It is a fundamental problem in distributed systems, as it affects the correctness and efficiency of many algorithms and applications.

Some of the challenges and characteristics of termination detection are:

- No process has complete knowledge of the global state of the system, and global time does not exist.
- Processes may become idle and active at any time, depending on the arrival of messages or local events.
- Processes may communicate asynchronously, and messages may be delayed, lost, or reordered by the network.
- Processes may fail or recover during the computation, and the system may be partially or fully connected.

There are different types of termination detection, depending on the nature and structure of the distributed computation. Some of the common types are:

- Diffusing computation: A computation that starts from a single initiator process and propagates through a subset of processes in the system, forming a logical tree of dependencies. The computation terminates when all the processes in the tree become idle and no messages are in transit.
- General computation: A computation that involves any subset of processes in the system, without a predefined initiator or structure. The computation terminates when all the processes become idle and no messages are in transit.
- Fault-tolerant computation: A computation that can tolerate failures and recoveries of processes and links, and still detect termination correctly.

There are different algorithms for termination detection, depending on the type of computation and the assumptions made about the system. Some of the common algorithms are:

- Huang's algorithm: An algorithm for diffusing computation, based on the concept of a control message that travels along the logical tree and collects the information about the state of the processes and the messages. The algorithm ensures that the initiator process detects termination when the control message returns to it with zero balance of messages.
- Dijkstra-Scholten algorithm: An algorithm for diffusing computation, based on the concept of a parent-child relation between processes that reflects the dependency of the computation. The algorithm ensures that the initiator process detects termination when it has no children and no messages are in transit.
- Safra's algorithm: An algorithm for general computation, based on the concept of a token that circulates among the processes and collects the information about the state of the processes and the messages. The algorithm ensures that any process can detect termination when it receives the token with zero balance of messages.
- Chandy-Misra algorithm: An algorithm for fault-tolerant computation, based on the concept of a probe message that is sent by a process to its neighbors when it becomes idle, and is forwarded or returned depending on the state of the neighbors. The algorithm ensures that a process can detect termination when it receives all the probes it has sent.



## Unit 2 - Distributed Mutual Exclusion

- Distributed mutual exclusion is the problem of ensuring that at most one process in a distributed system can access a shared resource at a time.
- Distributed mutual exclusion algorithms can be classified into two categories: permission-based and token-based.
- Permission-based algorithms require a process to obtain permission from other processes before entering the critical section. Examples of permission-based algorithms are Lamport's algorithm, Ricart-Agrawala algorithm, and Maekawa's algorithm.
- Token-based algorithms use a special message, called a token, that grants the right to enter the critical section. A process can enter the critical section only if it has the token. Examples of token-based algorithms are Suzuki-Kasami algorithm, Raymond's algorithm, and Singhal's algorithm.
- The performance of distributed mutual exclusion algorithms can be measured by the following metrics: message complexity, synchronization delay, and fairness.
- Message complexity is the number of messages exchanged per critical section access. It reflects the communication overhead of the algorithm.
- Synchronization delay is the time elapsed between a process requesting the critical section and entering it. It reflects the responsiveness of the algorithm.
- Fairness is the degree to which the algorithm satisfies the requests of all processes in a fair manner. It reflects the absence of starvation and priority inversion.



# Classification of distributed mutual exclusion

Distributed mutual exclusion is a problem of ensuring that only one process in a distributed system can access a shared resource or data at a time. It is a fundamental requirement for achieving consistency, coordination and synchronization among the processes.

There are three basic approaches for implementing distributed mutual exclusion:

- **Token-based approach**: A unique token is shared among the sites. A site is allowed to enter its critical section if it possesses the token. Mutual exclusion is ensured because the token is unique. Examples of token-based algorithms are Suzuki-Kasami's algorithm, Raymond's algorithm and Maekawa's algorithm.
- **Non-token-based approach**: A site requests permission from other sites before entering its critical section. A site is allowed to enter its critical section if it receives permission from all or a majority of other sites. Mutual exclusion is ensured by the voting mechanism. Examples of non-token-based algorithms are Ricart-Agrawala's algorithm, Lamport's algorithm and Singhal's algorithm.
- **Quorum-based approach**: A site requests permission from a subset of sites, called a quorum, before entering its critical section. A site is allowed to enter its critical section if it receives permission from all the sites in its quorum. Mutual exclusion is ensured by the intersection property of quorums. Examples of quorum-based algorithms are Thomas's algorithm, Agrawala's algorithm and Gifford's algorithm.

The performance of distributed mutual exclusion algorithms can be evaluated based on the following metrics:

- **Message complexity**: The number of messages exchanged per critical section entry.
- **Synchronization delay**: The time elapsed between a site's request and its entry to the critical section.
- **System throughput**: The number of times the critical section is executed per unit time.
- **Fault tolerance**: The ability of the algorithm to handle failures of sites or communication links.



# Requirement of mutual exclusion theorem for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM

- Mutual exclusion is a concurrency control property which is introduced to prevent race conditions.
- Race conditions occur when multiple processes access a shared resource or data simultaneously and at least one of them modifies it.
- Mutual exclusion ensures that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner  .
- Mutual exclusion in a distributed system states that only one process is allowed to execute the critical section (CS) at any given time  .
- A critical section (CS) is a segment of code that accesses a shared resource or data  .
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion .
- Message passing is the sole means for implementing distributed mutual exclusion .
- There are three basic approaches for implementing distributed mutual exclusion:
  - Token-based algorithms: A process can enter its CS only if it possesses a unique token that is circulated among the processes.
  - Permission-based algorithms: A process can enter its CS only if it receives permission from all or a subset of the processes.
  - Quorum-based algorithms: A process can enter its CS only if it receives permission from a majority or a weighted majority of the processes.
- The requirement of mutual exclusion theorem is to ensure the correctness and consistency of the distributed system.
- The mutual exclusion theorem states that any algorithm that solves the mutual exclusion problem in a distributed system must satisfy the following properties:
  - Safety: No two processes can be in their CS at the same time.
  - Liveness: Every request to enter the CS eventually succeeds.
  - Fairness: No process is indefinitely postponed from entering its CS.
  - Fault-tolerance: The algorithm can tolerate some failures of processes or messages.



# Token based and non token based algorithms for distributed mutual exclusion

Distributed mutual exclusion (DME) is the problem of ensuring that only one process at a time can access a shared resource in a distributed system. There are two main types of algorithms for DME: token based and non token based.

## Token based algorithms

- In token based algorithms, a unique token is shared among all the sites in the distributed system. The token represents the permission to enter the critical section. Only the site that holds the token can execute the critical section.
- Token based algorithms guarantee mutual exclusion and freedom from deadlock, but they may suffer from starvation and high message complexity.
- Examples of token based algorithms are:
  - **Suzuki-Kasami algorithm**: This is a modification of Ricart-Agrawala algorithm, a permission based algorithm that uses REQUEST and REPLY messages to ensure mutual exclusion. In Suzuki-Kasami algorithm, the token is a vector that records the number of requests made by each site. The token is passed to the site with the highest request number that has not yet executed the critical section. This algorithm reduces the number of messages from O(n^2) to O(n) per critical section execution, where n is the number of sites .
  - **Raymond's algorithm**: This is a tree-based algorithm that organizes the sites into a logical tree. The token is initially held by the root of the tree. A site that wants to enter the critical section sends a REQUEST message to its parent in the tree. The parent forwards the request to the root if it does not have the token. The root sends the token to the site that requested it. A site that has the token and receives a request from its child passes the token to that child. This algorithm reduces the number of messages to O(log n) per critical section execution, but it may cause starvation and high delay.

## Non token based algorithms

- In non token based algorithms, also known as permission based algorithms, a site communicates with a set of other sites to determine who should execute the critical section next. A site that wants to enter the critical section sends a REQUEST message to the other sites and waits for their REPLY messages. A site that receives a REQUEST message replies with a REPLY message if it is not in the critical section or does not want to enter it. A site can enter the critical section only if it has received REPLY messages from all the other sites.
- Non token based algorithms do not require a unique token, but they may cause more message overhead and synchronization delay than token based algorithms. They also need to handle the failure and recovery of sites.
- Examples of non token based algorithms are:
  - **Lamport's algorithm**: This is a timestamp based algorithm that uses logical clocks to order the requests for the critical section and to resolve conflicts between simultaneous requests. A site that wants to enter the critical section sends a REQUEST message with its timestamp to all the other sites. A site that receives a REQUEST message replies with a REPLY message if it has a smaller timestamp or if it is not interested in the critical section. A site can enter the critical section only if it has received REPLY messages from all the other sites and its timestamp is the smallest among all the requests. This algorithm ensures mutual exclusion and fairness, but it requires O(n^2) messages per critical section execution, where n is the number of sites.
  - **Maekawa's algorithm**: This is a quorum based algorithm that reduces the number of messages by dividing the sites into subsets called quorums. A site that wants to enter the critical section sends a REQUEST message to all the sites in its quorum. A site that receives a REQUEST message replies with a REPLY message if it has not voted for any other site. A site can enter the critical section only if it has received REPLY messages from all the sites in its quorum. A site that exits the critical section sends a RELEASE message to all the sites in its quorum. This algorithm requires O(sqrt(n)) messages per critical section execution, where n is the number of sites, but it may cause deadlock and starvation.



# Performance Metric for Distributed Mutual Exclusion Algorithms

Distributed mutual exclusion algorithms are algorithms that ensure that only one process can access a shared resource or execute a critical section at a time in a distributed system. The performance of these algorithms can be evaluated by the following metrics :

- **Message complexity**: It is the number of messages that are required per critical section (CS) execution by a process. It reflects the communication overhead and network congestion caused by the algorithm. A lower message complexity is desirable.
- **Synchronization delay**: It is the time elapsed between the departure of a process from the CS and the entry of the next process into the CS. It reflects the degree of concurrency and fairness achieved by the algorithm. A lower synchronization delay is desirable.
- **Response time**: It is the time interval between the request of a process to enter the CS and the end of its CS execution. It reflects the waiting time and the service time experienced by the process. A lower response time is desirable.
- **Throughput**: It is the number of CS executions per unit time in the system. It reflects the efficiency and utilization of the shared resource. A higher throughput is desirable.

Different algorithms may have different trade-offs among these metrics, depending on the assumptions and design choices they make. For example, some algorithms may use a centralized coordinator to grant access to the CS, while others may use a distributed token or a quorum of processes . Some algorithms may use a FIFO queue to order the requests, while others may use a priority queue or a random order. Some algorithms may require the processes to know the global state of the system, while others may allow the processes to have incomplete or outdated information. These factors may affect the performance of the algorithms in different scenarios and workloads. Therefore, it is important to compare and analyze the algorithms using the appropriate metrics and criteria.



# Unit 3 - Distributed Deadlock Detection

- A **deadlock** is a condition where a set of processes request resources that are held by other processes in the set, and none of the processes can proceed until some of the resources are released.
- A **distributed deadlock** is a deadlock that involves processes and resources located on different machines in a distributed system.
- **Deadlock detection** is a strategy to deal with deadlocks by examining the status of the process-resource interactions for the presence of cyclic wait.
- **Deadlock resolution** is a strategy to deal with deadlocks by aborting or preempting some of the deadlocked processes or resources to break the cycle.
- **Deadlock detection** in distributed systems is challenging because of the following reasons:
  - The global state of the system is not known or easily accessible.
  - The system is dynamic and asynchronous, and the processes and resources may change their states frequently.
  - The communication and computation costs of detecting and resolving deadlocks may be high.
- There are three main approaches to **deadlock detection** in distributed systems:
  - **Centralized approach**: A designated node, called the **deadlock detector**, collects the local wait-for graphs (WFGs) from all the nodes and constructs a global WFG to detect cycles. This approach has the advantages of simplicity and low communication cost, but it has the disadvantages of single point of failure, bottleneck, and scalability issues.
  - **Distributed approach**: Each node maintains its own local WFG and periodically sends it to its neighbors. A cycle detection algorithm, such as **edge chasing** or **probe-based**, is used to trace the dependencies among the nodes and detect cycles. This approach has the advantages of fault tolerance, load balancing, and scalability, but it has the disadvantages of high communication cost, false deadlock detection, and synchronization issues.
  - **Hierarchical approach**: The nodes are organized into a hierarchy of clusters, and each cluster has a **coordinator** that collects the local WFGs from its members and constructs a cluster WFG. The coordinators communicate with each other to construct a global WFG and detect cycles. This approach has the advantages of reducing the communication cost and the size of the WFGs, but it has the disadvantages of increased complexity and dependency on the cluster structure.



# System Model for Distributed Deadlock Detection

- A distributed system consists of a collection of nodes that communicate and cooperate to achieve a common goal.
- A node can be a process, a computer, or a cluster of computers that share resources and execute tasks.
- A resource can be a physical device, such as a printer or a disk, or a logical entity, such as a file or a lock.
- A process can request, use, and release resources according to some protocol.
- A deadlock occurs when a set of processes are waiting for resources that are held by other processes in the same set, and none of them can proceed.
- Deadlock detection is the problem of finding and resolving deadlocks in a distributed system.
- There are three main approaches to deadlock detection in distributed systems: centralized, hierarchical, and distributed.

## Centralized Approach

- In the centralized approach, one node is designated as the deadlock detector, and it is responsible for collecting and analyzing the information about the process-resource interactions in the system.
- The deadlock detector maintains a global wait-for graph (WFG), which is a directed graph that represents the dependencies among processes and resources.
- A node in the WFG is either a process or a resource, and an edge from a process to a resource indicates a request, while an edge from a resource to a process indicates an allocation.
- A deadlock exists in the system if and only if the WFG contains a cycle.
- The deadlock detector periodically requests the local wait-for graphs (LWFGs) from each node, and constructs the global WFG by merging the LWFGs.
- The deadlock detector then runs a cycle detection algorithm on the global WFG, and if a cycle is found, it initiates a recovery action, such as aborting one or more processes in the cycle.
- The advantages of the centralized approach are simplicity and efficiency, as the deadlock detection is performed by a single node with a global view of the system.
- The disadvantages of the centralized approach are scalability and reliability, as the deadlock detector can become a bottleneck and a single point of failure in the system.

## Hierarchical Approach

- In the hierarchical approach, the system is divided into a hierarchy of clusters, and each cluster has a local deadlock detector that is in charge of the nodes in that cluster.
- The local deadlock detectors communicate with each other through a coordinator, which is a node that acts as the deadlock detector for the whole system.
- The coordinator maintains a global WFG, which is a reduced version of the WFG that only contains the inter-cluster dependencies.
- A node in the global WFG is either a cluster or a resource, and an edge from a cluster to a resource indicates a request, while an edge from a resource to a cluster indicates an allocation.
- A deadlock exists in the system if and only if the global WFG contains a cycle.
- The coordinator periodically requests the local WFGs from each cluster, and constructs the global WFG by merging the local WFGs.
- The coordinator then runs a cycle detection algorithm on the global WFG, and if a cycle is found, it notifies the local deadlock detectors of the clusters involved in the cycle, and they initiate a recovery action, such as aborting one or more processes in the cycle.
- The advantages of the hierarchical approach are scalability and reliability, as the deadlock detection is distributed among multiple nodes, and the coordinator can be replicated for fault tolerance.
- The disadvantages of the hierarchical approach are complexity and overhead, as the deadlock detection requires more communication and coordination among the nodes.

## Distributed Approach

- In the distributed approach, there is no central or hierarchical authority for deadlock detection, and each node participates in the deadlock detection process.
- The distributed approach relies on a technique called edge chasing, which is a distributed cycle detection algorithm that uses special messages called probes to trace the dependencies among processes and resources.
- A probe is a message that contains the identity of the sender and a list of nodes that have been visited by the probe.
- A node sends a probe to another node when it suspects that there is a dependency between them, and the probe travels along the edges of the WFG until it either reaches the sender or a dead end.
- If the probe reaches the sender, it means that a cycle has been detected, and the sender initiates a recovery action, such as aborting itself or another process in the cycle.
- If the probe reaches a dead end, it means that there is no cycle, and the probe is discarded.
- The advantages of the distributed approach are scalability and reliability, as the deadlock detection is performed by the nodes themselves, and there is no single point



# Resource vs Communication Deadlocks

- A deadlock is a condition where a process cannot proceed because it needs to obtain a resource held by another process, and it itself is holding a resource that the other process needs.
- There are two types of deadlocks in distributed systems: resource deadlocks and communication deadlocks.
- Resource deadlocks occur when processes access resources, such as data objects in database systems and buffers in store and forward communication networks. A process acquires a resource before accessing it and releasing it after using it.
- Communication deadlocks occur when processes exchange messages, such as in message passing systems and distributed algorithms. A process sends a message to another process and waits for a reply before continuing.
- The main difference between resource deadlocks and communication deadlocks is that in resource deadlocks, the resources are explicitly requested and released by the processes, while in communication deadlocks, the resources are implicitly allocated and freed by the communication system.
- Another difference is that resource deadlocks can be detected by analyzing the resource allocation graph, while communication deadlocks can be detected by analyzing the wait-for graph.
- Resource deadlocks can be prevented by using deadlock avoidance or deadlock prevention techniques, such as ordering the resources, granting resources only when all are available, or using timeouts. Communication deadlocks can be prevented by using message ordering or message acknowledgment techniques, such as using sequence numbers, timestamps, or logical clocks.
- Resource deadlocks can be resolved by using deadlock recovery techniques, such as aborting or preempting some processes, or rolling back to a safe state. Communication deadlocks can be resolved by using message retransmission or message cancellation techniques, such as using timeouts, acknowledgments, or negative acknowledgments.



# Deadlock Prevention for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process. Deadlocks can occur in distributed systems, where processes and resources are located on different machines connected by a network.

Deadlock prevention is a technique to avoid the occurrence of deadlocks by imposing some constraints on the resource allocation policies. There are two main methods of deadlock prevention in distributed systems:

- Ordered request: In this method, each resource type is assigned a certain level to maintain a resource request policy for a process. This is known as the resource allocation policy. A process can request resources only in an increasing order of levels. For example, if a process needs resources of type A, B, and C, and their levels are 1, 2, and 3 respectively, then the process must request A before B, and B before C. This prevents circular wait condition, which is one of the necessary conditions for deadlock.

- Collective request: In this method, a process must request all the resources it needs at the same time, before starting its execution. This is known as the atomic allocation policy. A process can either get all the resources it needs or none of them. This prevents hold and wait condition, which is another necessary condition for deadlock.

Both methods have some advantages and disadvantages. Ordered request method allows more concurrency and flexibility, but it may cause starvation and waste of resources. Collective request method avoids starvation and waste of resources, but it may cause blocking and reduced concurrency .

Some of the challenges and issues in implementing deadlock prevention in distributed systems are:

- How to assign levels to resources in a consistent and global way
- How to handle dynamic addition and deletion of resources and processes
- How to deal with communication delays and failures
- How to balance the trade-off between concurrency and deadlock prevention .



# Avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- Avoidance is a technique to prevent deadlocks from occurring in a distributed system by ensuring that the system is always in a safe state.
- A safe state is a state where there is at least one sequence of resource allocation that does not lead to a deadlock.
- Avoidance requires the system to have some knowledge of the current and future resource requests and releases of each process.
- Avoidance can be implemented using either static or dynamic methods.
- Static methods involve pre-allocating resources to processes before they start execution, based on some criteria such as priority, resource requirements, etc.
- Dynamic methods involve granting or denying resource requests at run-time, based on the current state of the system and the potential impact of the request on the system's safety.
- However, avoidance is impractical in distributed systems due to several problems, such as:
  - The lack of global information and synchronization among processes and resources.
  - The uncertainty and unpredictability of resource requests and releases in a dynamic and heterogeneous environment.
  - The high overhead and complexity of maintaining and checking the system's safety.
  - The possibility of starvation and unfairness for some processes that may be denied resources indefinitely.
- Therefore, deadlock detection is preferred over avoidance in distributed systems, as it allows more flexibility and concurrency for processes and resources.



# Detection and Resolution of Distributed Deadlocks

- A distributed deadlock is a situation where a set of processes in a distributed system are waiting for each other to release resources, and none of them can proceed.
- A distributed deadlock can be detected by constructing a wait-for graph (WFG) that represents the dependencies among the processes and the resources in the system.
- A WFG is a directed graph where the nodes are processes or resources, and the edges are requests or assignments. An edge from a process to a resource means the process is requesting the resource, and an edge from a resource to a process means the resource is assigned to the process.
- A cycle in the WFG indicates the presence of a deadlock. A knot is a strongly connected component of the WFG that contains at least one resource node. A knot is a necessary and sufficient condition for a deadlock.
- There are three main approaches to construct and search the WFG in a distributed system: centralized, hierarchical, and distributed.
- In the centralized approach, there is a designated coordinator process that collects the information about the requests and assignments from all the other processes, and constructs and searches the global WFG periodically or on demand.
- In the hierarchical approach, the processes are organized into a tree structure, and each process maintains a local WFG for its subtree. The local WFGs are merged and searched at different levels of the hierarchy, starting from the leaves and moving up to the root.
- In the distributed approach, there is no coordinator or hierarchy, and each process maintains a local WFG for its own requests and assignments. The processes exchange messages to construct and search the global WFG in a distributed manner, using algorithms such as edge chasing, path pushing, or diffusing computation.
- Once a deadlock is detected, it can be resolved by breaking the cycle or the knot in the WFG. There are various strategies to select which processes or resources to abort or preempt, such as random, victim, youngest, oldest, minimum cost, maximum cost, etc.
- The goal of deadlock resolution is to minimize the cost of breaking the deadlock, which can include factors such as the amount of work lost, the number of processes affected, the priority of the processes, the availability of the resources, etc.



# Centralized Deadlock Detection

- Centralized deadlock detection is a technique used in distributed systems to handle deadlock detection by maintaining a global wait-for graph in a single chosen site, called the deadlock-detection coordinator.
- The coordinator collects information about the local wait-for graphs of each site and constructs the global wait-for graph by merging them.
- The coordinator periodically runs a cycle detection algorithm on the global wait-for graph to detect deadlocks.
- If a deadlock is detected, the coordinator selects a victim process to abort and sends a message to the corresponding site to terminate the process.
- The advantages of centralized deadlock detection are simplicity, low communication overhead, and easy implementation.
- The disadvantages of centralized deadlock detection are single point of failure, scalability issues, and lack of autonomy.



# Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set.
- Deadlocks can occur in distributed systems when distributed transactions or concurrency control are used.
- Deadlock detection is the approach of handling deadlocks by identifying and resolving them after they occur.
- Deadlock detection in distributed systems entails two basic issues:
  - Detection of existing deadlocks by examining the status of process-resource interactions for the presence of cyclic wait.
  - Resolution of detected deadlocks by aborting one or more deadlocked processes.
- Deadlock detection in distributed systems can be done by three approaches:
  - Centralized approach: A single node is designated as the deadlock detector and collects information from all other nodes about their resource requests and allocations.
  - Distributed approach: Each node maintains its own local wait-for graph and periodically exchanges information with other nodes to construct a global wait-for graph.
  - Hierarchical approach: The nodes are organized into a hierarchy of clusters and each cluster has a coordinator that acts as the deadlock detector for the cluster.
- Each approach has its own advantages and disadvantages in terms of communication overhead, accuracy, scalability, and fault tolerance.



# Path Pushing Algorithms for Distributed Deadlock Detection

- Path pushing algorithms detect distributed deadlocks by keeping an explicit global wait-for graph (WFG)  .
- The main idea is to create a global WFG for each site of the distributed system  .
- A site is a node in the distributed system that can initiate, request, or grant resources .
- A WFG is a directed graph that represents the dependencies among the processes or transactions in the system .
- A node in the WFG is a process or transaction, and an edge from node A to node B means that A is waiting for a resource held by B .
- A cycle in the WFG indicates a deadlock situation .
- In this class of algorithms, at each site, whenever deadlock computation is performed, it sends its local WFG to all the neighboring sites  .
- A neighboring site is a site that shares a common edge with the sender site in the WFG .
- The receiver site then merges the received WFG with its own local WFG and checks for cycles  .
- If a cycle is detected, the receiver site initiates the deadlock resolution process .
- The advantages of path pushing algorithms are that they can detect deadlocks quickly and accurately, and they do not require probe messages or global state information .
- The disadvantages of path pushing algorithms are that they require a lot of communication and storage overhead, and they may generate false cycles due to concurrency and inconsistency .



# Edge Chasing Algorithms for Distributed Deadlock Detection

- Edge chasing algorithms are a class of distributed deadlock detection algorithms that use special messages called probes to trace the dependency graph of processes and resources in a distributed system.
- A probe is a triplet (i, j, k) that denotes that the deadlock detection is initiated by process P_i and the message is being sent by the home site of process P_j to the home site of process P_k.
- The home site of a process is the site where the process is executing.
- A probe message is sent along the edges of the wait-for graph, which represents the requests and waits of processes for resources in the system.
- If a probe message returns to the initiator process, it means that a cycle exists in the wait-for graph and a deadlock has occurred.
- One of the most well-known edge chasing algorithms is the Chandy-Misra-Haas algorithm, which works for the AND request model, where a process can request multiple resources simultaneously and wait for all of them to be granted before proceeding.
- The Chandy-Misra-Haas algorithm works as follows:

  - Each process maintains a local wait-for graph that contains only the nodes and edges relevant to the process.
  - When a process P_i requests a resource R_k from another process P_j, it sends a request message to P_j and adds an edge (P_i, R_k) to its local wait-for graph.
  - When a process P_j receives a request message from another process P_i for a resource R_k that it holds, it checks if it is waiting for any other resource. If not, it grants the resource to P_i and removes the edge (P_j, R_k) from its local wait-for graph. If yes, it adds an edge (R_k, P_i) to its local wait-for graph and sends a probe message (i, j, i) to P_i, indicating that P_j is waiting for a resource that P_i holds.
  - When a process P_i receives a probe message (i, j, k) from another process P_j, it checks if k is equal to i. If yes, it means that a cycle has been detected and P_i initiates the deadlock resolution. If no, it checks if it is waiting for any other resource. If not, it discards the probe message. If yes, it forwards the probe message (i, j, k) to all the processes that hold the resources that P_i is waiting for.
  - When a process P_i receives a grant message from another process P_j for a resource R_k that it requested, it removes the edge (P_i, R_k) from its local wait-for graph and checks if it has received all the resources that it requested. If yes, it proceeds with its execution and releases the resources when done. If no, it continues to wait for the remaining resources.

- The advantages of edge chasing algorithms are that they are simple, efficient, and scalable, as they only involve local information and minimal communication overhead.
- The disadvantages of edge chasing algorithms are that they may generate false positives, as they do not consider the global state of the system, and that they may cause unnecessary delays, as they do not allow partial grants of resources.



## Unit 4 - Agreement Protocols

- Agreement protocols are a class of distributed algorithms that allow a set of processes to reach a common decision, despite the possibility of failures or malicious behavior.
- Agreement protocols are useful for implementing fault-tolerant services, such as distributed consensus, atomic broadcast, leader election, and distributed transactions.
- Agreement protocols can be classified into different types, depending on the assumptions they make about the system model, the communication model, the failure model, and the adversary model.
- Some common types of agreement protocols are:
  - **Crash fault-tolerant protocols**: These protocols assume that processes may fail by crashing, but do not behave maliciously. They also assume that the communication is reliable and synchronous, meaning that messages are delivered within a known bounded time. Examples of crash fault-tolerant protocols are Paxos, Raft, and Two-Phase Commit.
  - **Byzantine fault-tolerant protocols**: These protocols assume that processes may fail by behaving arbitrarily, or even colluding with other faulty processes. They also assume that the communication is reliable, but may be asynchronous, meaning that messages may be delayed arbitrarily or even lost. Examples of Byzantine fault-tolerant protocols are PBFT, Zyzzyva, and Tendermint.
  - **Asynchronous fault-tolerant protocols**: These protocols assume that processes may fail by crashing, but do not behave maliciously. They also assume that the communication is unreliable and asynchronous, meaning that messages may be delayed arbitrarily, lost, duplicated, or reordered. Examples of asynchronous fault-tolerant protocols are Ben-Or, Chandra-Toueg, and Bracha.
- Agreement protocols typically have the following properties:
  - **Validity**: If all processes start with the same initial value, then they must decide on that value.
  - **Agreement**: No two correct processes decide on different values.
  - **Termination**: Every correct process eventually decides on some value.
  - **Integrity**: If a process decides on a value, then that value must have been proposed by some process.
- Agreement protocols may also have additional properties, such as:
  - **Uniform agreement**: No two processes, whether correct or faulty, decide on different values.
  - **Uniform validity**: If a process decides on a value, then that value must have been the initial value of some process.
  - **Uniform integrity**: If a process decides on a value, then that value must have been proposed by some correct process.
  - **Non-triviality**: There exists some execution in which processes decide on different values.



# Introduction for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by passing messages.
- Agreement protocols are algorithms that enable the processes in a distributed system to reach a common decision or a consistent state, despite the presence of failures or uncertainties.
- Agreement protocols are essential for ensuring the reliability, consistency, fault-tolerance, and security of distributed systems.
- Some examples of agreement problems are:
  - Consensus: All processes agree on a single value from a set of proposed values.
  - Atomic commit: All processes agree on whether to commit or abort a distributed transaction.
  - Byzantine agreement: All processes agree on a single value from a set of proposed values, even if some processes are faulty and may behave arbitrarily.
  - Leader election: All processes agree on which process is the leader or coordinator of the system.
  - Mutual exclusion: All processes agree on which process has exclusive access to a shared resource.
- Agreement protocols are challenging to design and implement because of the following issues:
  - Asynchrony: The processes and the communication channels may have unpredictable delays or failures, making it hard to synchronize or order events.
  - Partial failure: Some processes or communication channels may fail while others continue to operate, making it hard to detect or recover from failures.
  - Non-determinism: The processes may have different inputs, states, or behaviors, making it hard to predict or control the outcome of the protocol.
  - Adversarial behavior: Some processes may be malicious or compromised, making it hard to trust or verify the messages they send or receive.



# System Models for Distributed Systems

A system model is a simplified representation of a distributed system that captures its essential properties and design choices. System models can help us understand, analyze, and reason about the behavior and performance of distributed systems. System models can be classified into three types:

- **Physical models**: capture the hardware composition of a system in terms of computers and other devices and their interconnecting network;
- **Interaction models**: capture the communication and coordination mechanisms between the components of a system, such as message passing, remote procedure calls, or shared memory;
- **Fault models**: capture the possible failures and errors that can occur in a system, such as node crashes, network partitions, or message losses.

Different system models can have different assumptions and guarantees about the properties of a distributed system, such as:

- **Network behavior**: how reliable, fast, and secure is the network that connects the components of a system;
- **Node behavior**: how reliable, fast, and secure are the nodes that run the components of a system;
- **Timing behavior**: how synchronized, accurate, and predictable are the clocks and timers of the nodes and the network;
- **Consensus behavior**: how easy or hard is it for the components of a system to agree on a common value or decision.

Some examples of system models for distributed systems are:

- **Synchronous model**: assumes that the network is reliable, the nodes are reliable, the clocks are synchronized, and the message delays and node speeds are bounded. This model simplifies the design and analysis of distributed algorithms, but it is unrealistic and impractical for most real-world systems.
- **Asynchronous model**: assumes that the network is unreliable, the nodes are unreliable, the clocks are unsynchronized, and the message delays and node speeds are unbounded. This model is more realistic and general for most real-world systems, but it makes the design and analysis of distributed algorithms more difficult and complex.
- **Partially synchronous model**: assumes that the network and the nodes are unreliable, but there are some bounds on the message delays and node speeds that hold eventually or with high probability. This model is a compromise between the synchronous and asynchronous models, and it is often used for consensus algorithms, such as Paxos and Raft.
- **Crash-stop model**: assumes that the nodes can only fail by crashing (halting) and never recover. This model simplifies the fault tolerance and recovery mechanisms of distributed systems, but it is not applicable for systems that need to handle node restarts or repairs.
- **Crash-recovery model**: assumes that the nodes can fail by crashing, but they can also recover and resume their operation. This model requires the nodes to have persistent storage and recovery protocols to handle node restarts or repairs, and it is more applicable for systems that need to maintain availability and durability.
- **Byzantine model**: assumes that the nodes can fail in arbitrary ways, such as sending incorrect or malicious messages, or colluding with other faulty nodes. This model requires the nodes to have cryptographic techniques and fault tolerance protocols to handle node misbehavior, and it is more applicable for systems that need to maintain security and integrity.



# Classification of Agreement Problem in Distributed Systems

An agreement problem in a distributed system is a problem where a set of processes need to agree on a common value or decision, despite the possibility of failures or malicious behavior of some processes. Agreement problems are fundamental to achieving fault tolerance and consistency in distributed systems.

There are different types of agreement problems, depending on the assumptions and requirements of the system. Some of the well-known agreement problems are:

- **Byzantine agreement problem**: A single value, which is to be agreed on, is initialized by an arbitrary process and all non-faulty processes have to agree on that value. The processes may be subject to Byzantine failures, which means they can behave arbitrarily or maliciously, sending conflicting or incorrect messages to other processes. The goal is to ensure that all non-faulty processes agree on the same value, and that value is the initial value of some non-faulty process.   

- **Consensus problem**: A generalization of the Byzantine agreement problem, where each process can propose its own value and all non-faulty processes have to agree on a common value. The value agreed on must be one of the proposed values. The processes may be subject to crash failures, which means they can stop executing at any point, but cannot send incorrect messages. The goal is to ensure that all non-faulty processes agree on the same value, and that value is one of the proposed values.   

- **Interactive consistency problem**: A variation of the Byzantine agreement problem, where each process has its own value and all non-faulty processes have to agree on a vector of values, one for each process. The vector agreed on must satisfy two properties: (1) the value for each non-faulty process is its own initial value, and (2) the value for each faulty process is the same for all non-faulty processes. The processes may be subject to Byzantine failures, as in the Byzantine agreement problem. The goal is to ensure that all non-faulty processes agree on the same vector of values, and that vector satisfies the two properties.  

These agreement problems are related to each other and have different applications in distributed systems. For example, Byzantine agreement can be used to implement reliable broadcast, where a message sent by a process is received by all non-faulty processes. Consensus can be used to implement atomic commit, where a set of processes need to decide whether to commit or abort a transaction. Interactive consistency can be used to implement group membership, where a set of processes need to agree on who is in the group and who is not.



# Byzantine Agreement Problem

The Byzantine agreement problem is a fundamental problem in fault-tolerant distributed computing. It requires a set of parties in a distributed system to agree on a value even if some of the parties are corrupted or faulty. The corrupted parties may behave arbitrarily, sending conflicting or misleading messages to different parties, or remaining silent. The problem is also known as the Byzantine generals problem, the interactive consistency problem, or the source congruency problem.

The problem was first defined and solved by Lamport et al. in 1982, using the analogy of several divisions of the Byzantine army camped outside an enemy city, each division commanded by its own general. The generals can communicate with one another only by messenger. After observing the enemy, they must decide upon a common plan of action, such as attack or retreat. However, some of the generals may be traitors, who try to prevent the loyal generals from reaching agreement. The problem is to find an algorithm that allows the loyal generals to agree on a common plan, while tolerating a certain number of traitors.

Some of the main concepts and results related to the Byzantine agreement problem are:

- A Byzantine agreement protocol is a distributed algorithm that allows the parties to reach agreement on a value, despite the presence of Byzantine faults. A Byzantine fault is any deviation from the normal behavior of a party, such as sending incorrect or inconsistent messages, crashing, or colluding with other faulty parties.
- A Byzantine agreement protocol is said to be correct if it satisfies the following properties:
  - **Validity**: If all the parties start with the same value, then they all decide on that value.
  - **Agreement**: All the parties decide on the same value.
  - **Termination**: All the parties eventually decide on a value.
- A Byzantine agreement protocol is said to be t-resilient if it can tolerate up to t faulty parties, and it is correct for any number of parties n > t.
- A Byzantine agreement protocol is said to be deterministic if the decision of each party depends only on its initial value and the messages it receives, and it is randomized if the decision of each party may also depend on some random choices.
- A Byzantine agreement protocol is said to be synchronous if there is a known upper bound on the message delivery time, and it is asynchronous if there is no such bound. A synchronous protocol can also use rounds, where each party sends and receives messages only at certain predefined times.
- A Byzantine agreement protocol is said to be oral if it uses only point-to-point messages, and it is signed if it uses digital signatures or other cryptographic techniques to authenticate the messages.
- A Byzantine agreement protocol is said to be binary if the parties can only decide on two possible values, such as 0 or 1, and it is multivalued if the parties can decide on any value from a given domain.
- A Byzantine agreement protocol is said to be uniform if the decision of each party does not depend on its initial value, and it is non-uniform otherwise.
- A Byzantine agreement protocol is said to be interactive if the parties exchange messages with each other, and it is non-interactive if the parties only receive messages from a common source.

Some of the main challenges and limitations of the Byzantine agreement problem are:

- It is impossible to achieve Byzantine agreement in an asynchronous system with one or more faulty parties, as shown by Fischer et al. in 1985. This is known as the FLP impossibility result, and it implies that any asynchronous Byzantine agreement protocol must either sacrifice termination or agreement in some cases.
- It is impossible to achieve deterministic Byzantine agreement in a synchronous system with more than one-third of the parties being faulty, as shown by Lamport et al. in 1982. This is known as the lower bound on the resilience of deterministic Byzantine agreement, and it implies that any deterministic Byzantine agreement protocol must have n > 3t.
- It is possible to achieve randomized Byzantine agreement in a synchronous system with less than half of the parties being faulty, as shown by Rabin in 1983. This is known as the upper bound on the resilience of randomized Byzantine agreement, and it implies that any randomized Byzantine agreement protocol can have n > 2t.
- It is possible to achieve oral Byzantine agreement in a synchronous system with less than one-third of the parties being faulty, as shown by Lamport et al. in 1982. This is known as the upper bound on the resilience of oral Byzantine agreement, and it implies that any oral Byzantine



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
  - Byzantine failures: A process behaves arbitrarily, possibly maliciously.
  - Network failures: A process cannot communicate with some or all of the other processes due to network partitioning, message loss, or message delay.
- Some of the common consensus algorithms are:
  - Two-phase commit: A coordinator process initiates a transaction and asks the other processes to vote on whether to commit or abort. If all processes vote to commit, the coordinator sends a commit message to all. If any process votes to abort, the coordinator sends an abort message to all.
  - Three-phase commit: A variation of two-phase commit that adds a pre-commit phase to avoid blocking in case of coordinator failure.
  - Paxos: A family of algorithms that use a leader election process and a majority voting mechanism to reach consensus on a single value.
  - Raft: A simplified version of Paxos that uses a leader election process and a log replication mechanism to reach consensus on a sequence of values.
  - Byzantine fault tolerance: A class of algorithms that can tolerate up to one-third of the processes being Byzantine.



# Interactive Consistency Problem

- Interactive consistency is the problem in which n distinct nodes, each having its own private value, where up to t may be Byzantine, run an algorithm that allows all non-faulty nodes to infer the values of each other node   .
- Byzantine nodes are nodes that can behave arbitrarily, such as sending incorrect or conflicting messages, or remaining silent.
- Interactive consistency is also known as Byzantine Generals Problem, which is a metaphor for the situation where a group of generals must agree on a common plan of action, while some of them may be traitors.
- Interactive consistency is a fundamental problem in distributed systems, especially for critical applications that rely on the combination of the opinions of multiple peers to provide a service.
- Interactive consistency is closely related to distributed consensus, which is the problem of reaching agreement on a single value among a set of nodes, where some of them may be faulty.
- Interactive consistency is harder than distributed consensus, because it requires agreement on n values instead of one, and it requires each node to learn the values of all other nodes, not just its own.
- Interactive consistency can be solved by using algorithms that involve message exchange, cryptography, randomization, or a combination of these techniques .
- Interactive consistency has some limitations and assumptions, such as the need for a reliable communication network, a bounded number of Byzantine nodes, a synchronization barrier, or a common coin .
- Interactive consistency has many applications and implications, such as fault-tolerant distributed computing, blockchain, voting systems, secure multiparty computation, and distributed machine learning .



# Solution to Byzantine Agreement problem

- The Byzantine Agreement problem is a fundamental challenge in fault-tolerant distributed computing, where a set of processes need to agree on a common value even if some of them are faulty or malicious.
- The problem is often illustrated by the analogy of the Byzantine Generals problem, where several divisions of the Byzantine army are camped outside an enemy city, each commanded by its own general. The generals can communicate with one another only by messenger. After observing the enemy, they must decide upon a common plan of action, such as attack or retreat.
- The problem is that some of the generals may be traitors, who may try to sabotage the agreement by sending conflicting messages or lying about their observations. The loyal generals need to reach a consensus that satisfies the following conditions:
  - All loyal generals decide upon the same plan of action (agreement).
  - A small number of traitors cannot cause the loyal generals to adopt a bad plan (validity).
- The solution to the problem depends on the number of traitors, the type of communication channels, and the assumptions about the system model. Some of the possible solutions are:
  - The Oral Messages algorithm, which assumes that the communication channels are reliable and authenticated, but the messages can be altered by the traitors. The algorithm requires that the number of traitors is less than one-third of the total number of generals. The algorithm works by having each general send their initial value to all other generals, and then recursively exchanging the received values until a majority value is reached.
  - The Signed Messages algorithm, which assumes that the communication channels are unreliable and unauthenticated, but the messages can be digitally signed by the sender. The algorithm requires that the number of traitors is less than half of the total number of generals. The algorithm works by having each general send their signed initial value to all other generals, and then using a majority voting scheme to decide the final value.
  - The Randomized algorithm, which assumes that the communication channels are reliable and authenticated, but the messages can be altered by the traitors. The algorithm does not have a bound on the number of traitors, but it only guarantees a probabilistic agreement. The algorithm works by having each general flip a coin and send the result to all other generals, and then using a coin-flipping protocol to decide the final value.



# Application of Agreement Problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- Agreement problem is a fundamental problem in distributed systems, where a set of processes need to reach a common decision based on their individual inputs and messages exchanged with each other.
- Agreement problem is essential for many applications that require coordination, consistency, fault-tolerance, and reliability in distributed systems.
- There are different versions of agreement problem, such as consensus, atomic commitment, atomic broadcast, and group membership, which have different requirements and assumptions.
- Consensus problem is the most basic and general form of agreement problem, where each process proposes a value and all correct processes have to agree on the same value, which must be one of the proposed values.
- Atomic commitment problem is a special case of consensus problem, where each process proposes either to commit or abort a transaction, and all correct processes have to agree on the same decision, which must be commit if all proposed commit, and abort otherwise.
- Atomic broadcast problem is another special case of consensus problem, where one process broadcasts a message to all other processes, and all correct processes have to deliver the same message in the same order.
- Group membership problem is a variant of agreement problem, where each process has to agree on the set of processes that are currently alive and reachable in the system, and update the set whenever a process joins, leaves, or fails.
- Solving agreement problem in distributed systems is challenging due to the possibility of process failures, network failures, message delays, and asynchrony.
- Depending on the type and number of failures, and the degree of synchrony, agreement problem may be solvable or unsolvable in distributed systems.
- For example, consensus problem is solvable in a synchronous system with crash failures, but unsolvable in an asynchronous system with crash failures, or in a synchronous system with Byzantine failures.
- There are various algorithms and protocols for solving agreement problem in distributed systems, such as Paxos, Raft, Two-Phase Commit, Three-Phase Commit, Byzantine Agreement, and Viewstamped Replication.
- These algorithms and protocols have different trade-offs in terms of performance, complexity, scalability, and fault-tolerance, and are suitable for different applications and scenarios.



# Atomic Commit in Distributed Database System

- An atomic commit is an operation that applies a set of distinct changes as a single operation.
- If the changes are applied, then the atomic commit is said to have succeeded. If the changes are not applied, then the atomic commit is said to have failed or aborted.
- In distributed database systems, the primary need for commit protocols is to maintain the atomicity of distributed transactions .
- A distributed transaction is a transaction that involves multiple database sites that may be geographically dispersed.
- A commit protocol is a set of rules that ensures that either all the changes made by a distributed transaction are committed at all the sites, or none of them are.
- Atomic commitment issue is of prime importance in the distributed system and the issue becomes more necessary to deal with if some of the sites participating in the execution of the transaction commitment fail .
- There are two main types of commit protocols: blocking and non-blocking .
- Blocking protocols are those that may block the progress of the transaction if a site fails during the commit process .
- Non-blocking protocols are those that do not block the progress of the transaction even if a site fails during the commit process .
- The most common blocking protocol is the two-phase commit protocol (2PC), which consists of two phases: a prepare phase and a commit phase.
- The most common non-blocking protocol is the three-phase commit protocol (3PC), which consists of three phases: a prepare phase, a pre-commit phase, and a commit phase.
- There are also other variations and optimizations of commit protocols, such as the failure-aware atomic commit protocol (FLAC), which aims to reduce the latency and abort rate of distributed transactions.
- There are also different ways to integrate commit protocols with other aspects of distributed database systems, such as concurrency control, replication, and recovery.



## Unit 5 - Distributed Resource Management

- Distributed resource management is the process of allocating and coordinating the use of resources (such as CPU, memory, disk, network, etc.) across multiple nodes in a distributed system.
- The main objectives of distributed resource management are to improve the performance, reliability, availability, scalability, and efficiency of the distributed system, as well as to provide fairness and transparency to the users and applications.
- The main challenges of distributed resource management are to deal with the heterogeneity, dynamism, uncertainty, and complexity of the distributed system, as well as to cope with the trade-offs and conflicts among the objectives and constraints of different stakeholders.
- The main components of distributed resource management are:
  - Resource discovery: the process of finding and identifying the available resources in the distributed system.
  - Resource allocation: the process of assigning resources to tasks or applications according to some criteria or policies.
  - Resource scheduling: the process of determining the order and timing of resource allocation and execution of tasks or applications.
  - Resource monitoring: the process of collecting and analyzing the information about the status and performance of resources and tasks or applications.
  - Resource adaptation: the process of adjusting the resource allocation and scheduling in response to the changes and events in the distributed system.
- The main techniques and methods for distributed resource management are:
  - Centralized: a single entity (such as a server or a coordinator) is responsible for managing all the resources and tasks or applications in the distributed system.
  - Distributed: multiple entities (such as nodes or agents) cooperate and coordinate with each other to manage the resources and tasks or applications in the distributed system.
  - Hierarchical: the distributed system is divided into multiple levels or layers, and each level or layer has its own entity or entities for managing the resources and tasks or applications within or across the levels or layers.
  - Decentralized: each entity (such as a node or an agent) is autonomous and self-organized, and manages its own resources and tasks or applications without relying on any other entity in the distributed system.
  - Hybrid: a combination of different techniques and methods for distributed resource management, such as using centralized for some resources and distributed for others, or using hierarchical for some tasks or applications and decentralized for others.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of issues in distributed file systems for the unit 5 of distributed resource management in the subject of distributed system.

# Issues in Distributed File Systems

A distributed file system (DFS) is a system that allows multiple clients to access and manipulate files stored on one or more servers over a network. A DFS provides the abstraction of a single, logical file system that spans multiple physical devices and locations. A DFS can offer many benefits, such as fault tolerance, scalability, performance, and transparency. However, a DFS also faces many challenges and issues in its design and implementation, such as:

- **Naming and location:** A DFS needs to provide a consistent and efficient way of naming and locating files across different servers and clients. A DFS may use a hierarchical namespace, a flat namespace, or a hybrid namespace to organize files. A DFS may also use a centralized, decentralized, or distributed approach to manage the namespace. A DFS needs to handle issues such as name conflicts, name resolution, name caching, and name replication.

- **Consistency and replication:** A DFS needs to ensure that the files are consistent and up-to-date across different servers and clients. A DFS may use replication to increase the availability and reliability of files, but replication also introduces issues such as update propagation, concurrency control, and conflict resolution. A DFS may use different consistency models, such as strict consistency, sequential consistency, causal consistency, or eventual consistency, to trade off between performance and correctness.

- **Security and access control:** A DFS needs to protect the files from unauthorized access and modification. A DFS may use encryption, authentication, authorization, and auditing mechanisms to ensure the security and integrity of files. A DFS needs to handle issues such as key management, trust management, and access control policies.

- **Performance and scalability:** A DFS needs to provide high performance and scalability to support a large number of files and clients. A DFS may use techniques such as caching, prefetching, load balancing, and partitioning to improve the performance and scalability of the system. A DFS needs to handle issues such as cache coherence, cache replacement, cache consistency, and cache invalidation.

- **Fault tolerance and recovery:** A DFS needs to tolerate and recover from various types of faults, such as network failures, server failures, client failures, and storage failures. A DFS may use techniques such as replication, checkpointing, logging, and backup to enhance the fault tolerance and recovery of the system. A DFS needs to handle issues such as fault detection, fault isolation, fault masking, and fault recovery.



# Mechanism for building distributed file systems

A distributed file system (DFS) is a file system that is distributed on multiple file servers or locations. It allows programs to access or store isolated files as they do with the local ones, allowing programmers to access files from any network or computer.

The mechanism for building a DFS involves the following aspects:

- Use of file models: The DFS uses different conceptual models of a file. The following are the two basic criteria for file modeling, which include file structure and modifiability. The files can be unstructured or structured based on the applications used in file systems. The files can also be immutable or mutable depending on whether they can be modified or not.
- Use of file accessing models: A DFS may use one of the following models to service a client’s file request:
  - Upload/download model: The client downloads the entire file from the server, modifies it locally, and uploads it back to the server.
  - Remote access model: The client accesses the file on the server through remote procedure calls (RPCs) or remote method invocations (RMIs).
  - Remote service model: The client sends a request to the server, which performs the file operation and returns the result to the client.
- Use of file replication: File replication is the primary mechanism for improving file availability and performance in a DFS. A replicated file is a file that has multiple copies with each copy located on a separate file server. The challenges of file replication include:
  - Consistency: The replicated copies of a file should be consistent with each other, meaning that they should reflect the same state of the file.
  - Location: The location of the replicated copies of a file should be transparent to the client, meaning that the client should not need to know where the copies are stored.
  - Update: The update of a replicated file should be propagated to all the copies, meaning that any change made to one copy should be reflected on the others.
- Use of file caching: File caching is another mechanism for improving file performance and reducing network traffic in a DFS. File caching is the process of storing a copy of a file or a part of a file in a local memory or disk for faster access. The challenges of file caching include:
  - Coherency: The cached copy of a file should be coherent with the original file, meaning that they should have the same content and metadata.
  - Consistency: The cached copy of a file should be consistent with the other cached copies, meaning that they should reflect the same state of the file.
  - Replacement: The replacement of a cached copy of a file should be done according to some policy, meaning that the system should decide which copy to evict when the cache is full.
- Use of file naming: File naming is the mechanism for identifying and locating files in a DFS. File naming involves the following components:
  - File name: A file name is a string of characters that uniquely identifies a file within a namespace.
  - Namespace: A namespace is a collection of file names that are organized in a hierarchical or flat structure.
  - Name resolution: Name resolution is the process of mapping a file name to a file location or a file identifier.
  - Name service: A name service is a component that provides name resolution and name management functions for a DFS.

: Mechanism for building Distributed file system - GeeksforGeeks. Retrieved from https://www.geeksforgeeks.org/mechanism-for-building-distributed-file-system/



# Design issues in Distributed Shared Memory

Distributed Shared Memory (DSM) is a mechanism that allows multiple processes on different nodes to share a common logical address space and access data transparently. DSM can simplify the programming of distributed systems by hiding the details of inter-process communication and data consistency. However, DSM also introduces several design issues that affect its performance, scalability, and correctness. Some of the main design issues in DSM are:

- **Granularity**: Granularity refers to the size of the unit of sharing and the unit of coherence in a DSM system. A smaller granularity (such as a byte or a word) can reduce the amount of false sharing and improve the locality of access, but it can also increase the overhead of coherence maintenance and communication. A larger granularity (such as a page or a segment) can reduce the overhead of coherence and communication, but it can also increase the amount of false sharing and waste bandwidth and memory. Therefore, choosing an appropriate granularity is a trade-off between performance and efficiency.

- **Structure**: Structure refers to the organization and layout of the shared data in the memory. The structure of the shared data can affect the locality, the coherence, and the communication patterns of the DSM system. There are two main types of structure: flat and hierarchical. A flat structure treats the shared memory as a single linear address space that can be accessed by any node. A hierarchical structure divides the shared memory into multiple regions or segments that can be mapped to different nodes or groups of nodes. A flat structure can simplify the programming and the coherence protocols, but it can also increase the contention and the communication overhead. A hierarchical structure can reduce the contention and the communication overhead, but it can also complicate the programming and the coherence protocols.

- **Coherence semantics**: Coherence semantics define the consistency model of the DSM system, that is, the rules and guarantees about the order and visibility of the updates to the shared data. Different coherence semantics can have different impacts on the performance, the correctness, and the portability of the DSM system. There are two main types of coherence semantics: strict and relaxed. A strict coherence semantics (such as sequential consistency) ensures that all nodes see the same order of updates to the shared data, and that any read operation returns the most recent write operation. A relaxed coherence semantics (such as release consistency) allows some degree of divergence among the views of the nodes, and that some read operations may return stale values. A strict coherence semantics can simplify the programming and the verification of the DSM system, but it can also limit the concurrency and the scalability. A relaxed coherence semantics can increase the concurrency and the scalability, but it can also complicate the programming and the verification of the DSM system.

- **Scalability**: Scalability refers to the ability of the DSM system to handle an increasing number of nodes, processes, and data without degrading the performance or the functionality. Scalability depends on several factors, such as the granularity, the structure, the coherence semantics, the communication protocols, and the hardware architecture of the DSM system. Some of the challenges and techniques for achieving scalability in DSM systems are: reducing the contention and the synchronization overhead, using hierarchical or distributed coherence protocols, exploiting the locality and the affinity of the access patterns, using adaptive or dynamic granularity and structure, and using scalable and fault-tolerant communication and hardware platforms.

- **Heterogeneity**: Heterogeneity refers to the diversity and the variability of the nodes, the processes, and the data in the DSM system. Heterogeneity can arise from different sources, such as the hardware architecture, the operating system, the network topology, the communication protocols, the application requirements, and the user preferences. Heterogeneity can affect the performance, the functionality, and the portability of the DSM system. Some of the challenges and techniques for dealing with heterogeneity in DSM systems are: ensuring the compatibility and the interoperability of the nodes and the processes, using common or standard interfaces and formats for the communication and the data, adapting the granularity, the structure, the coherence semantics, and the communication protocols to the characteristics and the needs of the nodes, the processes, and the data, and using flexible and customizable policies and mechanisms for the management and the allocation of the resources.



# Algorithm for Implementation of Distributed Shared Memory

Distributed Shared Memory (DSM) is a technique that allows multiple processes on different nodes of a distributed system to access a common virtual address space as if they were running on a single machine. DSM provides a high-level abstraction for interprocess communication and synchronization, and can simplify the design and development of distributed applications. However, DSM also introduces challenges such as maintaining consistency, coherence, and fault tolerance of the shared data.

There are different algorithms for implementing DSM, each with its own advantages and disadvantages. Some of the basic algorithms are:

- **Central Server Algorithm**: In this algorithm, a central server maintains all the shared data and services read and write requests from other nodes. The central server can use a page-based or an object-based approach to manage the shared data. The advantage of this algorithm is that it is simple and ensures consistency and coherence of the shared data. The disadvantage is that it introduces a single point of failure and a performance bottleneck, and it does not exploit the locality of access patterns.
- **Migration Algorithm**: In this algorithm, the shared data is initially stored at the central server, but it can migrate to other nodes upon request. The node that currently holds the data is called the owner, and it can service read requests from other nodes. However, if another node wants to write to the data, it has to request the ownership from the current owner, and the data is transferred to the new owner. The advantage of this algorithm is that it reduces the network traffic and the load on the central server, and it adapts to the changing access patterns. The disadvantage is that it may cause frequent data transfers and ownership changes, and it may incur additional overhead for maintaining the ownership information.
- **Replication Algorithm**: In this algorithm, the shared data is replicated on multiple nodes, and each node can read and write to its local copy. The replication can be done eagerly or lazily, depending on whether the updates are propagated to other copies immediately or on demand. The advantage of this algorithm is that it improves the availability and the performance of the shared data, and it tolerates node failures. The disadvantage is that it requires more storage space and more complex mechanisms to ensure consistency and coherence of the replicated data.
- **Invalidation Algorithm**: In this algorithm, the shared data is also replicated on multiple nodes, but each node can only read from its local copy. If a node wants to write to the data, it has to invalidate the copies on other nodes, and obtain the exclusive access to the data. The invalidation can be done eagerly or lazily, depending on whether the invalidation messages are sent immediately or on demand. The advantage of this algorithm is that it reduces the network traffic and the data transfers, and it exploits the read-dominated access patterns. The disadvantage is that it may cause frequent invalidations and cache misses, and it may incur additional overhead for maintaining the validity information.



## Unit 6 - Failure Recovery in Distributed Systems

- Failure recovery is the process of restoring a distributed system to a consistent and correct state after one or more components fail.
- Failure recovery is important for ensuring the availability, reliability, and integrity of the distributed system and its data.
- Failure recovery can be classified into two types: backward recovery and forward recovery.
- Backward recovery involves undoing the effects of the failed components and restoring the system to a previous consistent state, such as a checkpoint or a backup.
- Forward recovery involves correcting the errors caused by the failed components and continuing the execution from the current state, such as by using redundancy or replication.
- Backward recovery can be further divided into three techniques: checkpointing, logging, and rollback-recovery.
- Checkpointing is the process of periodically saving the state of the system or its components to a stable storage, such as a disk or a cloud.
- Logging is the process of recording the events or actions that occur in the system or its components to a stable storage, such as a disk or a cloud.
- Rollback-recovery is the process of restoring the system or its components to a previous checkpoint or a consistent log, and replaying the events or actions that occurred after the checkpoint or the log.
- Forward recovery can be further divided into two techniques: redundancy and replication.
- Redundancy is the process of having multiple copies or versions of the system or its components, such as hardware, software, or data, that can perform the same function or provide the same service.
- Replication is the process of maintaining multiple copies or replicas of the system or its data, such as files, databases, or objects, that are synchronized and consistent with each other.
- Redundancy and replication can be used to mask, tolerate, or resolve failures, depending on the level of consistency and availability required by the system or its applications.



# Concepts in Backward and Forward Recovery

- Backward recovery and forward recovery are two techniques for restoring the system to a consistent state after a failure in a distributed system.
- Backward recovery involves rolling back the system to a previous error-free state by using checkpoints and logs. Forward recovery involves correcting the errors in the current state and continuing the execution.
- The main difference between backward and forward recovery is that backward recovery discards the work done after the error, while forward recovery preserves the work done before and after the error.
- Backward recovery is more general and independent of the nature of faults, but it may incur more overhead and waste of resources. Forward recovery is more efficient and avoids unnecessary rollbacks, but it requires accurate assessment and removal of errors.
- Some examples of backward recovery protocols are checkpointing, message logging, and rollback-dependency trackback. Some examples of forward recovery techniques are error masking, retry, and compensation.



# Recovery in Concurrent Systems

Recovery in concurrent systems is the process of restoring the system to a consistent state after a failure or an error. Recovery is essential for ensuring the reliability and availability of distributed systems that involve multiple concurrent transactions.

There are two main types of recovery in concurrent systems:

- **Backward recovery**: This type of recovery involves undoing the effects of the erroneous or failed transactions and restoring the system to a previous consistent state. Backward recovery requires the system to periodically record its state (such as by using checkpoints or logs) and to use this information to roll back the changes made by the faulty transactions.
- **Forward recovery**: This type of recovery involves correcting the errors or failures without undoing the effects of the transactions. Forward recovery requires the system to detect the errors or failures and to apply some recovery actions to fix them (such as by using redundancy or exception handling) and to continue the execution of the transactions.

Some of the challenges and techniques for recovery in concurrent systems are:

- **Interaction with concurrency control**: The recovery scheme depends on the concurrency control scheme that is used to ensure the serializability and isolation of the transactions. For example, if the system uses locking as a concurrency control mechanism, then the recovery scheme must release the locks held by the failed transactions and prevent deadlocks. If the system uses timestamps as a concurrency control mechanism, then the recovery scheme must ensure that the timestamps are consistent and do not cause cascading aborts.
- **Transaction rollback**: The recovery scheme must be able to undo the effects of a transaction that has failed or has been aborted. This can be done by using undo logs, which record the old values of the data items that have been modified by the transaction. The recovery scheme can use the undo logs to restore the data items to their previous values. Alternatively, the recovery scheme can use compensation transactions, which are transactions that perform the inverse operations of the failed transactions.
- **Checkpoints**: The recovery scheme can use checkpoints to reduce the amount of work that needs to be done in case of a failure. A checkpoint is a point in time when the system records its state (such as by writing the logs and the data to stable storage) and ensures that all the transactions that have committed before the checkpoint are durable. The recovery scheme can use the checkpoints to limit the scope of the rollback or the recovery actions to the transactions that have started after the checkpoint.
- **Restart recovery**: The recovery scheme must be able to restart the system after a failure and to resume the execution of the transactions that have not been completed. The recovery scheme can use the logs and the checkpoints to determine the status of the transactions and to decide which transactions need to be redone or undone. The recovery scheme must also ensure that the transactions are executed in a correct order and that the consistency and the serializability of the system are maintained.
- **Concurrent recovery**: The recovery scheme can use concurrent recovery to speed up the recovery process and to reduce the downtime of the system. Concurrent recovery allows the system to run multiple recovery sessions in parallel and to recover multiple media sets (such as disks or tapes) that have been used for backups. Concurrent recovery requires the system to coordinate the recovery sessions and to ensure that the dependencies and the conflicts among the transactions are resolved .



# Obtaining consistent Checkpoints for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Failure recovery in distributed systems is the process of restoring the system to a consistent and correct state after a failure occurs.
- Failure recovery is essential for fault tolerance, which is the ability of the system to continue functioning despite the presence of errors.
- Failure recovery can be achieved by using checkpoints, which are snapshots of the system state at certain points in time.
- Checkpoints can be used to rollback the system to a previous state and resume the execution from there, avoiding the need to restart the system from scratch.
- Checkpoints can be classified into two types: global and local.
  - Global checkpoints capture the state of the entire system, including all the processes and communication channels.
  - Local checkpoints capture the state of a single process or a group of processes.
- Checkpoints can also be classified into two types: synchronous and asynchronous.
  - Synchronous checkpoints require coordination among all the processes to take a consistent snapshot of the system.
  - Asynchronous checkpoints allow each process to take a snapshot independently, without waiting for others.
- Synchronous checkpoints have the advantage of simplicity and consistency, but they incur a high overhead and may cause blocking or deadlock.
- Asynchronous checkpoints have the advantage of efficiency and scalability, but they may result in inconsistent or useless snapshots that cannot be used for recovery.
- To obtain consistent checkpoints in distributed systems, several algorithms and techniques have been proposed, such as :
  - The Chandy-Lamport algorithm, which uses special messages called markers to record the state of the communication channels.
  - The Lai-Yang algorithm, which uses a global clock to synchronize the processes and record the state of the communication channels.
  - The Manetho algorithm, which uses a distributed logging mechanism to record the causal dependencies among the processes.
  - The Zorro algorithm, which uses a zero-cost reactive approach to detect and correct inconsistent checkpoints on the fly.
- The choice of the checkpointing algorithm depends on several factors, such as the system model, the failure model, the communication model, the performance requirements, and the recovery objectives.



# Recovery in Distributed Database Systems

- Recovery in distributed database systems is the process of restoring the database to a consistent and correct state after a failure or a transaction abort.
- Recovery in distributed database systems is more complex than in centralized database systems because failures can occur at multiple sites or communication links, and transactions can span multiple sites.
- Recovery in distributed database systems aims to maintain the atomicity and durability of distributed transactions, which means that either all or none of the subtransactions at different sites are committed, and the committed changes are permanent.
- Recovery in distributed database systems can be classified into two types: local recovery and global recovery.
  - Local recovery is the process of recovering a single site from a failure or a transaction abort. Local recovery techniques include undo, redo, and undo/redo logging, which record the changes made by transactions and allow to roll back or roll forward the changes as needed.
  - Global recovery is the process of coordinating the recovery of multiple sites involved in a distributed transaction. Global recovery techniques include two-phase commit (2PC), three-phase commit (3PC), and presumed abort/commit protocols, which ensure that all sites agree on the outcome of a distributed transaction and avoid the problem of orphaned or in-doubt subtransactions.



## Unit 7 - Fault Tolerance

- Fault tolerance is the ability of a system to continue functioning correctly in the presence of failures.
- Fault tolerance can be achieved by using techniques such as redundancy, replication, recovery, and reconfiguration.
- Fault tolerance can be classified into two types: hardware fault tolerance and software fault tolerance.
- Hardware fault tolerance is the ability of a system to tolerate failures in its physical components, such as processors, memory, disks, and network devices.
- Hardware fault tolerance can be achieved by using techniques such as RAID, mirroring, backup, checkpointing, and fail-over.
- Software fault tolerance is the ability of a system to tolerate failures in its software components, such as applications, operating systems, and middleware.
- Software fault tolerance can be achieved by using techniques such as exception handling, transactions, consensus, and self-healing.
- Fault tolerance can be measured by metrics such as reliability, availability, and maintainability.
- Reliability is the probability that a system will perform its intended function without failure for a given period of time.
- Availability is the fraction of time that a system is operational and ready to provide service.
- Maintainability is the ease with which a system can be repaired or restored after a failure.



# Issues in Fault Tolerance for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Fault tolerance is the ability of a system to continue functioning correctly in the presence of failures.
- Fault tolerance is important for distributed systems because they consist of multiple components that may be subject to failures, such as hardware faults, software bugs, network errors, malicious attacks, etc.
- Fault tolerance can be achieved by using various techniques, such as redundancy, replication, checkpointing, recovery, consensus, etc.
- Fault tolerance can be classified into different levels, such as detection, masking, tolerance, recovery, and prevention.
- Fault tolerance can also be categorized into different types, such as hardware fault tolerance, software fault tolerance, network fault tolerance, etc.
- Fault tolerance can be evaluated by using different metrics, such as reliability, availability, dependability, etc.
- Fault tolerance can be implemented by using different algorithms, such as Byzantine agreement, Paxos, Raft, etc.
- Fault tolerance can be challenged by various issues, such as scalability, consistency, latency, complexity, etc.

: Fault Tolerance Mechanisms in Distributed Systems
: Fault Tolerance in Distributed Systems: A Survey
: What is fault tolerance in distributed system
: Fault Tolerance Mechanisms in Distributed Systems
: 13 - Fault Tolerance in Distributed Systems



# Commit Protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Commit protocols are algorithms that ensure the atomicity of distributed transactions, i.e., all the sites involved in a transaction either commit or abort it unanimously, even in the presence of failures  .
- Commit protocols are necessary to maintain the consistency and reliability of distributed systems, as they prevent partial execution or data loss due to network or site failures  .
- There are different types of commit protocols, such as one-phase commit, two-phase commit, and three-phase commit, each with its own advantages and disadvantages    .

## One-phase commit protocol
- A one-phase commit protocol involves a coordinator site that initiates a transaction and communicates with the participant sites that execute the transaction on behalf of the coordinator .
- The coordinator site sends a commit request to all the participant sites and waits for their replies .
- If all the participant sites reply with an OK message, the coordinator site commits the transaction and sends a commit message to all the participant sites .
- If any of the participant sites reply with an abort message, the coordinator site aborts the transaction and sends an abort message to all the participant sites .
- The advantages of this protocol are simplicity and efficiency, as it requires only one round of message exchange between the coordinator and the participants .
- The disadvantages of this protocol are lack of fault tolerance and concurrency control, as it does not handle the cases where the coordinator or the participants fail or the network partitions .

## Two-phase commit protocol
- A two-phase commit protocol is an extension of the one-phase commit protocol that adds a voting phase to improve the fault tolerance and concurrency control    .
- The protocol consists of two phases: the prepare phase and the commit phase    .
- In the prepare phase, the coordinator site sends a prepare request to all the participant sites and waits for their votes    .
- The participant sites execute the transaction and write a log record of their actions, then reply with a yes vote if they are ready to commit or a no vote if they want to abort    .
- In the commit phase, the coordinator site decides whether to commit or abort the transaction based on the votes received from the participant sites    .
- If all the participant sites vote yes, the coordinator site commits the transaction and sends a commit message to all the participant sites    .
- If any of the participant sites vote no, the coordinator site aborts the transaction and sends an abort message to all the participant sites    .
- The participant sites follow the decision of the coordinator site and commit or abort the transaction accordingly    .
- The advantages of this protocol are fault tolerance and concurrency control, as it handles the cases where the coordinator or the participants fail or the network partitions by using timeouts, recovery procedures, and locking mechanisms    .
- The disadvantages of this protocol are blocking and performance overhead, as it requires two rounds of message exchange between the coordinator and the participants and may block the participants in the commit phase until the coordinator recovers or the network reconnects    .

## Three-phase commit protocol
- A three-phase commit protocol is an extension of the two-phase commit



# Voting protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Voting protocols are a type of consensus protocols that allow a set of distributed nodes to agree on a common value or decision, despite the presence of faults or attacks.
- Voting protocols are useful for achieving fault tolerance in distributed systems, such as replicated databases, distributed file systems, or blockchain networks.
- Voting protocols can be classified into two categories: exact voting and inexact voting.
  - Exact voting requires that all nodes agree on the same value or decision, and that the value or decision is correct according to some predefined criteria. Examples of exact voting protocols are two-phase commit, three-phase commit, and Paxos.
  - Inexact voting allows some degree of disagreement or error among the nodes, as long as the value or decision is acceptable according to some predefined criteria. Examples of inexact voting protocols are majority voting, weighted voting, and probabilistic voting.
- Voting protocols can also be classified into two categories based on the security properties they provide: secure voting and non-secure voting.
  - Secure voting ensures that the value or decision is not influenced by malicious nodes or external attackers, and that the voting process is resilient to denial-of-service attacks, message tampering, or impersonation. Examples of secure voting protocols are Byzantine fault-tolerant protocols, such as PBFT, Zyzzyva, and Tendermint.
  - Non-secure voting does not provide any security guarantees, and assumes that the nodes are honest and the network is reliable. Examples of non-secure voting protocols are traditional two-phase commit and three-phase commit protocols.
- Voting protocols can also be classified into two categories based on the fairness properties they provide: fair voting and unfair voting.
  - Fair voting ensures that the value or decision is not biased by the nodes' preferences, weights, or reputations, and that the voting process is equitable and proportional. Examples of fair voting protocols are approval voting, Borda count, and Condorcet methods.
  - Unfair voting allows some degree of bias or inequality among the nodes, as long as the value or decision is acceptable according to some predefined criteria. Examples of unfair voting protocols are plurality voting, weighted voting, and reputation-based voting.



# Dynamic voting protocols

- Dynamic voting protocols are techniques for consistency and recovery control of replicated files in distributed systems  .
- The purpose of a replicated file is to improve the availability of a logical file in the presence of site failures and network partitions  .
- A dynamic voting protocol assigns a number of votes to each copy of a replicated file, and only the group of copies with a majority of votes can perform a restricted operation, such as reading or writing .
- The number of votes assigned to each copy can change dynamically depending on the system state, such as the number of copies, the network topology, the failure pattern, etc    .
- The advantages of dynamic voting protocols are:
  - They can achieve higher availability than static voting protocols, which assign a fixed number of votes to each copy   .
  - They can adapt to different network configurations and failure scenarios, and optimize the performance and reliability of the system    .
  - They can reduce the communication and storage overhead of maintaining consistent copies, by minimizing the number of votes and copies involved in each operation   .
- The challenges of dynamic voting protocols are:
  - They require a mechanism to detect and handle failures, and to reassign votes accordingly    .
  - They may incur additional latency and complexity in updating the votes and coordinating the operations among the copies   .
  - They may introduce conflicts or inconsistencies if the votes are not updated or synchronized properly   .
- Some examples of dynamic voting protocols are:
  - The dynamic weighted voting scheme proposed by Davcev  , which assigns votes to copies based on their availability and distance to the requesting site.
  - The topological dynamic voting algorithm proposed by Agrawal and Abbadi, which assigns votes to copies based on their location in the network topology and the partitionability of the network.
  - The protocols for dynamic vote reassignment proposed by Gifford, which reassign votes to copies based on the failure pattern and the quorum size.



# Unit 8 - Transactions and Concurrency Control

## Transactions
- A transaction is a logical unit of work that consists of one or more operations on a database, such as reading, writing, inserting, deleting, or modifying data.
- A transaction has four properties, known as ACID: atomicity, consistency, isolation, and durability.
- Atomicity means that either all the operations of a transaction are executed or none of them are. A transaction is indivisible and cannot be split into smaller units.
- Consistency means that a transaction preserves the integrity constraints and business rules of the database. A transaction transforms the database from one consistent state to another.
- Isolation means that a transaction is executed as if it is the only one running on the database. A transaction does not see the intermediate results or effects of other concurrent transactions.
- Durability means that the effects of a transaction are permanent and do not disappear even in the case of system failures. A transaction is recorded in a non-volatile storage medium.

## Concurrency Control
- Concurrency control is the management of simultaneously executing transactions in a shared database.
- Concurrency control ensures that correct results for concurrent operations are generated while getting those results as quickly as possible.
- Concurrency control is important because it helps data remain consistent and avoids conflicts, anomalies, and inconsistencies that may arise from concurrent transactions.
- Concurrency control techniques implement some protocols that can be broadly classified into two categories: lock-based protocols and timestamp-based protocols.
- Lock-based protocols use locks to control the access of transactions to data items. A lock is a mechanism that grants or denies permission to a transaction to read or write a data item. There are different types of locks, such as shared locks, exclusive locks, and intention locks.
- Timestamp-based protocols use timestamps to order the transactions and determine their precedence. A timestamp is a unique identifier that indicates the start time of a transaction. There are different types of timestamps, such as commit timestamps, logical timestamps, and physical timestamps.



# Transactions

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the operations in a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction executes as if it were the only one in the system, without interference from other transactions.
- Durability means that the effects of a committed transaction are permanent and survive any system failures.

# Concurrency Control

- Concurrency control is the process of managing simultaneous execution of transactions in a shared database, to ensure the serializability and correctness of the transactions.
- Serializability is the property that the concurrent execution of a set of transactions is equivalent to some serial execution of the same transactions.
- Concurrency control can be achieved by using locking protocols, timestamp ordering, or optimistic methods.

# Distributed Transactions and Distributed Concurrency Control

- A distributed transaction is a transaction that spans multiple data servers in a distributed database system.
- A distributed transaction consists of a set of subtransactions, each of which is executed by one data server.
- A distributed transaction coordinator is a component that coordinates the execution and commitment of distributed transactions across multiple data servers.
- Distributed concurrency control provides a mechanism to synchronize distributed transactions in such a way that the ACID properties are not violated by their interleaved execution.
- Distributed concurrency control makes sure that all subtransactions of a set of distributed transactions are serialized identically in all data servers involved.
- Distributed concurrency control can be based on centralized, decentralized, or hierarchical approaches.
- Centralized approach uses a single coordinator to control the locking and commitment of all subtransactions in a distributed transaction.
- Decentralized approach uses a peer-to-peer communication among data servers to reach a consensus on the locking and commitment of subtransactions.
- Hierarchical approach uses a tree structure of coordinators to propagate the locking and commitment requests and responses among data servers.



# Nested Transactions for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A transaction is a unit of work that performs some operations on data and either commits or aborts as a whole.
- A nested transaction is a transaction that is composed of subtransactions, each of which may have its own commit or abort point.
- A nested transaction can be used to improve the performance, reliability, and modularity of distributed systems.
- A nested transaction can be classified into two types: closed nested transactions and open nested transactions.
- A closed nested transaction is a transaction that can only commit or abort as a whole, and its subtransactions are not visible to other transactions until the parent transaction commits.
- A closed nested transaction preserves the ACID properties of a flat transaction, but it may incur more overhead and locking than a flat transaction.
- A closed nested transaction can be implemented using a two-phase commit protocol, where the parent transaction coordinates the commit or abort of its subtransactions.
- A closed nested transaction can be represented by a tree structure, where the root node is the parent transaction and the leaf nodes are the subtransactions.
- A closed nested transaction can be serialized by using a serialization graph, where the nodes are the transactions and the edges are the conflicts between them.
- A conflict between two transactions occurs when they access the same data item and at least one of them writes to it.
- A serialization graph for nested transactions is acyclic if and only if the transactions are conflict-serializable, meaning that they can be executed in some order that is equivalent to a serial execution.
- A serialization graph for nested transactions can be tested by using a depth-first search algorithm, where the transactions are visited in a preorder traversal of the tree structure.
- An example of a closed nested transaction is shown below:

Closed nested transaction

- An open nested transaction is a transaction that allows some of its subtransactions to commit or abort independently, and their effects are visible to other transactions before the parent transaction commits.
- An open nested transaction relaxes the ACID properties of a flat transaction, but it may improve the concurrency, availability, and scalability of distributed systems.
- An open nested transaction can be implemented using a compensation-based protocol, where the parent transaction records the compensating actions for each subtransaction that commits.
- A compensating action is an action that reverses the effect of a committed subtransaction in case the parent transaction aborts.
- A compensating action must be idempotent, meaning that it can be executed multiple times without changing the outcome.
- A compensating action must be commutative, meaning that it can be executed in any order with other compensating actions without changing the outcome.
- A compensating action must be consistent, meaning that it preserves the integrity constraints of the data.
- An open nested transaction can be represented by a directed acyclic graph, where the nodes are the transactions and the edges are the dependencies between them.
- A dependency between two transactions occurs when one transaction reads or writes a data item that is written by another transaction.
- An open nested transaction can be serialized by using a topological sorting algorithm, where the transactions are ordered according to their dependencies.
- An example of an open nested transaction is shown below:

Open nested transaction



# Locks for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A lock is a mechanism that allows only one of the innumerable nodes or processes to access and modify a resource or data that is being shared commonly to prevent execution of same task twice and also maintain data integrity.
- Locks are designed to enforce a mutual exclusion concurrency control policy, which means that only one transaction can hold a lock on a data item at a time.
- Locks can be classified into different types based on the following criteria:
  - The granularity of the data item being locked, such as record-level, page-level, or table-level locks.
  - The mode of the lock, such as shared (read) or exclusive (write) locks.
  - The duration of the lock, such as long (held until the transaction commits or aborts) or short (released as soon as the operation is done) locks.
  - The protocol of acquiring and releasing locks, such as two-phase locking (2PL), which ensures serializability of transactions by acquiring all locks before releasing any, or timestamp ordering, which assigns a logical timestamp to each transaction and grants locks based on the timestamp order.
- In distributed systems, locks can be implemented using different strategies, such as:
  - Centralized locking, where a single node acts as a lock manager and grants or denies lock requests from other nodes.
  - Distributed locking, where each node has a local lock manager and communicates with other nodes to coordinate lock requests.
  - Hierarchical locking, where the nodes are organized into a tree structure and lock requests are propagated from the leaves to the root or vice versa.
- Distributed locks can also be based on different security levels of lock resources, such as:
  - Distributed systems based on asynchronous replication, such as MySQL, Tair, and Redis, where the lock resource is replicated on multiple nodes and the lock is granted by the primary node or a quorum of nodes.
  - Paxos-based distributed consensus systems, such as ZooKeeper, etcd, and Consul, where the lock resource is stored on a cluster of nodes that follow a consensus protocol to ensure consistency and availability.
- Distributed locks are useful for coordinating access to shared resources in a distributed system, but they also have some challenges and limitations, such as:
  - Lock contention, where multiple transactions compete for the same lock and cause delays or deadlocks.
  - Lock expiration, where a lock is released after a timeout or a failure of the lock holder, which may cause inconsistency or livelock.
  - Lock scalability, where the number of lock requests increases with the size and complexity of the distributed system, which may affect the performance and reliability of the lock service.
  - Lock correctness, where the lock service must ensure that the lock semantics are preserved in the presence of network partitions, message delays, or node failures.



# Optimistic Concurrency Control

- Optimistic concurrency control (OCC) is a concurrency control method applied to transactional systems such as relational database management systems and software transactional memory.
- OCC assumes that multiple transactions can frequently complete without interfering with each other, and does not use locking or timestamping techniques to prevent conflicts .
- Instead, a transaction is executed without restrictions until it is committed, and then it is validated to ensure that no conflicts have occurred with other concurrent transactions.
- If a conflict is detected, the transaction is aborted and restarted, possibly with some backoff or priority adjustment mechanism to reduce the likelihood of further conflicts .
- OCC has the advantage of allowing a high degree of concurrency and avoiding the overhead of locking or timestamping, but it also has the disadvantage of wasting resources and increasing latency when conflicts are frequent and transactions have to be restarted .
- OCC can be implemented in a centralized or distributed manner, depending on the architecture of the transactional system .
- In a centralized system, there is a single validation server that checks the read and write sets of each transaction and decides whether to commit or abort it.
- In a distributed system, there are multiple validation servers that communicate with each other to perform the validation process, using some protocol to ensure consistency and avoid deadlocks.
- OCC is suitable for applications that have low contention and high performance requirements, such as online analytical processing (OLAP), data warehousing, and scientific computing .



# Timestamp ordering

Timestamp ordering is a technique for ensuring serializability of transactions in a distributed system. It assigns a unique timestamp to each transaction and uses it to order the execution of conflicting operations.

## Lamport timestamps

Lamport timestamps are a type of logical clock that assigns a unique timestamp to each event in a distributed system, based on the causal relationships among events. Lamport timestamps are defined as follows:

- Each node in the system maintains a local counter that is incremented after each event.
- When a node sends a message, it attaches its current counter value to the message.
- When a node receives a message, it updates its counter to be the maximum of its own counter and the counter value in the message, plus one.
- The Lamport timestamp of an event is the counter value assigned to it by the node where it occurs.

Lamport timestamps provide a partial ordering of events, such that if event A causally precedes event B, then the Lamport timestamp of A is less than the Lamport timestamp of B. However, Lamport timestamps do not distinguish between concurrent events, i.e., events that are not causally related.

## Timestamp ordering protocol

The timestamp ordering protocol is a concurrency control protocol that uses Lamport timestamps to order the execution of conflicting operations in a distributed system. The protocol works as follows:

- Each transaction is assigned a unique timestamp when it starts, which is the Lamport timestamp of its first event.
- Each data item has two timestamps: a read timestamp (RTS) and a write timestamp (WTS), which record the timestamps of the last transaction that read or wrote the item, respectively.
- When a transaction T wants to read a data item X, it checks if its timestamp is greater than or equal to the WTS of X. If yes, it can read X and update the RTS of X to be the maximum of the RTS of X and the timestamp of T. If no, it means that T is trying to read a stale value of X, and the transaction is aborted and restarted with a new timestamp.
- When a transaction T wants to write a data item X, it checks if its timestamp is greater than both the RTS and the WTS of X. If yes, it can write X and update the WTS of X to be the timestamp of T. If no, it means that T is trying to overwrite a newer value of X, and the transaction is aborted and restarted with a new timestamp.

The timestamp ordering protocol ensures serializability of transactions, as it prevents any transaction from violating the precedence order of conflicting operations based on their timestamps. However, it may also abort some transactions that are not actually conflicting, due to the lack of precision of Lamport timestamps.



# Comparison of methods for concurrency control

Concurrency control is the process of managing the simultaneous execution of transactions in a distributed system, such that the consistency and correctness of the data are preserved. There are various methods for concurrency control, each with its own advantages and disadvantages. Some of the common methods are:

- **Two-phase locking (2PL)**: This method requires each transaction to acquire locks on the data items it accesses, and release them after it commits or aborts. There are two phases: a growing phase, where the transaction acquires locks and does not release any; and a shrinking phase, where the transaction releases locks and does not acquire any. 2PL ensures serializability, which means that the concurrent execution of transactions is equivalent to some serial execution. However, 2PL may suffer from deadlock, where two or more transactions are waiting for each other to release locks. 2PL also reduces concurrency, as transactions may block each other from accessing data items. There are different variants of 2PL, such as strict 2PL, rigorous 2PL, and conservative 2PL, that provide different levels of isolation and performance .

- **Timestamp ordering (TO)**: This method assigns a unique timestamp to each transaction, and uses it to order the transactions. Each data item has two timestamps: a read timestamp, which records the timestamp of the last transaction that read the item; and a write timestamp, which records the timestamp of the last transaction that wrote the item. A transaction can read or write a data item only if its timestamp is greater than the read and write timestamps of the item, respectively. Otherwise, the transaction is aborted and restarted with a new timestamp. TO ensures serializability, as the transactions are executed in the order of their timestamps. However, TO may suffer from starvation, where a transaction is repeatedly aborted and restarted due to conflicts with other transactions. TO also increases the overhead of maintaining and checking timestamps. There are different variants of TO, such as basic TO, Thomas' write rule, and multiversion TO, that provide different levels of isolation and performance .

- **Multiversion concurrency control (MVCC)**: This method allows each transaction to access a snapshot of the data that is consistent with its timestamp, and does not conflict with other transactions. Each data item has multiple versions, each with a timestamp and a value. A transaction can read the latest version of a data item that is older than or equal to its timestamp. A transaction can write a new version of a data item only if its timestamp is greater than the timestamp of the latest version. Otherwise, the transaction is aborted and restarted with a new timestamp. MVCC ensures serializability, as the transactions are executed in the order of their timestamps. However, MVCC may suffer from write skew, where two transactions update different data items based on a common predicate, and violate a consistency constraint. MVCC also increases the storage and garbage collection costs of maintaining multiple versions of data items .

- **Validation (or optimistic) concurrency control (VCC)**: This method allows each transaction to execute without any locking or timestamping, and validates its correctness at the end. Each transaction has three phases: a read phase, where the transaction reads data items and records them in a private workspace; a validation phase, where the transaction checks if its execution is serializable with respect to other transactions; and a write phase, where the transaction writes its updates to the database. VCC ensures serializability, as the transactions are validated according to some serial order. However, VCC may suffer from high abort rate, where many transactions are aborted and restarted due to validation failures. VCC also increases the complexity of the validation algorithm and the communication overhead among transactions .

The choice of the concurrency control method depends on the characteristics of the distributed system, such as the network latency, the data distribution, the transaction workload, and the performance requirements. There is no single best method for all scenarios, and trade-offs have to be made among factors such as concurrency, deadlock, starvation, overhead, and isolation  .



## Unit 9 - Distributed Transactions

- A distributed transaction is a database transaction that involves two or more network hosts.
- A transaction is a logical unit of work that guarantees the ACID properties (atomicity, consistency, isolation, durability) of a database.
- A distributed transaction requires a transaction manager that coordinates the operations on different hosts and ensures the ACID properties are maintained .
- A distributed transaction can be implemented using different protocols, such as two-phase commit, three-phase commit, or optimistic concurrency control.
- A distributed transaction can improve the performance, availability, and scalability of a database system, but also introduces challenges such as network failures, concurrency conflicts, and data inconsistency.



# Flat and Nested Distributed Transactions

A distributed transaction is a transaction that accesses objects managed by multiple servers. A distributed transaction must maintain the ACID properties of a transaction, which means that it must be atomic, consistent, isolated, and durable. Atomicity means that either all the changes made by the transaction are committed or none of them are. Consistency means that the transaction preserves the integrity constraints of the data. Isolation means that the transaction does not interfere with other concurrent transactions. Durability means that the committed changes are permanent and survive failures.

Distributed transactions can be structured in two different ways: flat transactions and nested transactions.

## Flat Transactions

A flat transaction has a single initiating point (Begin) and a single end point (Commit or Abort). A flat transaction is usually simple and short-lived, and it does not contain any subtransactions. A flat transaction can be coordinated by a single server, called the transaction manager, that communicates with the other servers involved in the transaction. The transaction manager uses a two-phase commit protocol to ensure the atomicity of the transaction. The two-phase commit protocol consists of two phases: the prepare phase and the commit phase. In the prepare phase, the transaction manager asks all the servers to vote on whether they are ready to commit or not. If all the servers vote yes, the transaction manager proceeds to the commit phase, where it instructs all the servers to commit the transaction. If any server votes no, the transaction manager aborts the transaction and instructs all the servers to roll back their changes.

## Nested Transactions

A nested transaction is a transaction that contains other transactions as its parts, called subtransactions. A nested transaction has a hierarchical structure, where the top-level transaction is the parent of all the subtransactions, and the subtransactions can have their own subtransactions as children. A nested transaction can be used to decompose a complex and long-lived transaction into smaller and simpler transactions, which can improve the concurrency and fault-tolerance of the system. A nested transaction can also span multiple servers, which makes it a distributed transaction.

A nested transaction can be coordinated by a nested transaction manager, which is responsible for managing the subtransactions and their dependencies. A nested transaction manager uses a nested two-phase commit protocol to ensure the atomicity of the transaction. The nested two-phase commit protocol extends the two-phase commit protocol by adding a third phase: the partial commit phase. In the partial commit phase, the nested transaction manager notifies the parent transaction that a subtransaction has completed. The parent transaction can then decide whether to commit or abort the subtransaction, based on its own logic and the state of other subtransactions. The partial commit phase allows the parent transaction to have more control and flexibility over the subtransactions, and also allows the subtransactions to release their resources earlier, which can improve the performance and scalability of the system.



# Atomic Commit Protocols for Distributed Transactions

- A distributed transaction is a transaction that involves multiple servers or nodes in a distributed system.
- An atomic commit protocol is a protocol that ensures that a distributed transaction is either committed or rolled back in its entirety, even if the system fails or some of the nodes fail or crash.
- Ensuring atomic commit is important for maintaining the consistency and integrity of the data in a distributed system.
- There are different types of atomic commit protocols, such as two-phase commit, three-phase commit, parallel commit, and failure-aware commit.
- Two-phase commit (2PC) is the most widely used atomic commit protocol. It consists of two phases: a prepare phase and a commit phase. In the prepare phase, a coordinator node asks all the participant nodes to vote on whether they are ready to commit or not. In the commit phase, the coordinator node decides whether to commit or abort the transaction based on the votes, and informs all the participant nodes of the decision.
- Three-phase commit (3PC) is an extension of 2PC that adds a pre-commit phase between the prepare and commit phases. In the pre-commit phase, the coordinator node informs all the participant nodes that they have agreed to commit, and waits for their acknowledgments. In the commit phase, the coordinator node sends the final commit message to all the participant nodes. 3PC can tolerate more failures than 2PC, but it has higher latency and message overhead.
- Parallel commit is a new atomic commit protocol that reduces the latency of transactions down to only a single round-trip of distributed consensus. It does not use a coordinator node, but instead relies on each participant node to independently decide whether to commit or abort the transaction based on the state of the other participant nodes. Parallel commit can achieve high performance and availability, but it requires strong consistency guarantees from the underlying distributed consensus protocol.
- Failure-aware commit (FLAC) is another new atomic commit protocol that aims to improve the performance and availability of distributed transactions in the presence of failures. It uses a hybrid approach that combines 2PC and parallel commit, and dynamically adapts to the failure scenarios. FLAC can achieve lower latency and higher throughput than 2PC and 3PC, and can tolerate more failures than parallel commit.



# Concurrency control in distributed transactions

- A distributed transaction is a transaction that accesses and updates data on multiple data servers that are connected by a network .
- A distributed transaction must satisfy the ACID properties: atomicity, consistency, isolation, and durability .
- Concurrency control is the process of managing the concurrent execution of transactions in a distributed system to ensure the ACID properties are not violated  .
- There are different types of concurrency control algorithms for distributed transactions, such as locking-based, timestamp-based, and optimistic algorithms .
- Locking-based algorithms use locks to prevent conflicting operations on the same data item by different transactions . A lock can be either shared or exclusive, depending on the type of operation. A transaction must acquire a lock before accessing a data item and release it after finishing the operation. A lock manager is responsible for granting, denying, and releasing locks .
- Timestamp-based algorithms assign a unique timestamp to each transaction and use it to order the operations on the same data item . A transaction can access a data item only if its timestamp is compatible with the timestamps of previous operations on that item. A timestamp manager is responsible for generating and comparing timestamps .
- Optimistic algorithms assume that conflicts are rare and allow transactions to execute without any synchronization until they commit . A transaction must validate its operations before committing to ensure that no conflicts have occurred. A validation manager is responsible for checking the validity of transactions .
- Each concurrency control algorithm has its own advantages and disadvantages, depending on the characteristics of the distributed system and the workload . For example, locking-based algorithms can avoid aborting transactions due to conflicts, but they may cause deadlock and reduce concurrency. Timestamp-based algorithms can avoid deadlock and increase concurrency, but they may cause aborting transactions due to timestamp conflicts. Optimistic algorithms can achieve high concurrency and avoid deadlock, but they may cause aborting transactions due to validation failures .
- Some concurrency control algorithms are designed to handle specific scenarios in distributed systems, such as multi-version concurrency control, snapshot isolation, and 2PC*  . These algorithms use different techniques to deal with the challenges of distributed transactions, such as replication, partitioning, and microservices  .



# Distributed Deadlocks

- A distributed deadlock is a situation where a set of processes in a distributed system are waiting for each other to release resources or messages, and none of them can proceed.
- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems .
- Distributed deadlocks are harder to detect, avoid, and prevent than deadlocks in centralized systems, because there is no single authority that can oversee resource allocation and dependency graphs.
- There are three main approaches to handle distributed deadlocks :
  - Prevention: This approach tries to ensure that at least one of the necessary conditions for deadlock (mutual exclusion, hold and wait, no preemption, circular wait) is never satisfied. For example, by using timeouts, ordering resources, or aborting transactions.
  - Avoidance: This approach tries to ensure that the system will always remain in a safe state, where there is at least one possible sequence of resource allocation that will not lead to deadlock. For example, by using the banker's algorithm or timestamps.
  - Detection: This approach tries to identify the existence of deadlocks after they occur, and then resolve them by breaking the circular wait. For example, by constructing a global wait-for graph (WFG) from local wait-for graphs at a deadlock detector or by a distributed algorithm like edge chasing .
- There are different types of distributed deadlocks, depending on the nature of the resources and the communication model:
  - Communication deadlocks: These occur when processes are waiting for messages from each other, and there is no buffer space to store the messages. For example, a deadlock can occur if two processes send messages to each other simultaneously, and both messages are lost due to network congestion.
  - Resource deadlocks: These occur when processes are waiting for resources that are held by other processes, and there is no mechanism to release the resources. For example, a deadlock can occur if two processes request exclusive access to two files that are stored on different machines, and each process obtains one file but not the other.
  - Hybrid deadlocks: These occur when both communication and resource deadlocks are involved. For example, a deadlock can occur if a process requests a resource from another process, and the latter process sends a message to the former process to confirm the request, but the message is blocked due to lack of buffer space.



# Transaction Recovery for the Notes of the Unit 9 - Distributed Transactions in the Subject of Distributed System

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction has the properties of atomicity, consistency, isolation, and durability (ACID).
- A distributed transaction is a transaction that spans multiple sites or nodes in a distributed system.
- A distributed transaction may fail due to various reasons, such as network failures, site failures, communication failures, or concurrency conflicts.
- Transaction recovery is the process of restoring the database to a consistent state after a transaction failure.
- Transaction recovery in a distributed system is more complex than in a centralized system, because it involves coordinating the recovery actions of multiple sites or nodes.
- Transaction recovery in a distributed system can be classified into two types: backward recovery and forward recovery.
- Backward recovery is the process of undoing the effects of a failed transaction by restoring the previous values of the data items that were modified by the transaction.
- Forward recovery is the process of redoing the effects of a committed transaction by applying the new values of the data items that were modified by the transaction.
- Transaction recovery in a distributed system can be implemented using various techniques, such as logging, shadow versions, two-phase commit protocol, three-phase commit protocol, or consensus protocols.
- Logging is a technique that records the changes made by a transaction in a log file, which can be used to undo or redo the transaction in case of a failure.
- Shadow versions is a technique that maintains multiple versions of the data items, and switches to the appropriate version depending on the outcome of the transaction.
- Two-phase commit protocol is a protocol that ensures the atomicity of a distributed transaction by coordinating the commit or abort decision of all the sites or nodes involved in the transaction.
- Three-phase commit protocol is a protocol that improves the availability of a distributed transaction by avoiding blocking situations in case of network partitions or site failures.
- Consensus protocols are protocols that enable a group of sites or nodes to agree on a common value or decision, such as the commit or abort of a distributed transaction.



## Unit 10 - Replication

- Replication is the process of creating and maintaining multiple copies of the same data on different database servers.
- Replication can improve the availability, performance, and scalability of a database system.
- Replication can also provide data redundancy and backup, as well as facilitate data distribution and synchronization across different locations.
- Replication can be classified into two types: synchronous and asynchronous.
  - Synchronous replication ensures that all changes made to the data on one server are immediately applied to the copies on the other servers, before the transaction is committed. This guarantees data consistency, but may incur high network latency and overhead.
  - Asynchronous replication allows changes made to the data on one server to be applied to the copies on the other servers after the transaction is committed. This improves performance and availability, but may result in data inconsistency or conflicts in case of network failures or concurrent updates.
- Replication can be implemented using different methods, such as:
  - Snapshot replication: a full copy of the data is periodically transferred from one server to another.
  - Transactional replication: only the changes made to the data are transferred from one server to another, using a log or a queue.
  - Merge replication: changes made to the data on different servers are merged and synchronized, using a conflict resolution mechanism.
  - Peer-to-peer replication: changes made to the data on any server are propagated to all the other servers, creating a distributed system with no single point of failure.



# System model and group communication for replication in distributed systems

- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by exchanging messages.
- Replication is a technique to improve the availability, performance, and fault tolerance of a distributed system by creating and maintaining multiple copies of the same data or service on different processes or nodes.
- A system model is a set of assumptions and properties that describe the behavior and characteristics of a distributed system, such as the communication model, the failure model, the timing model, and the security model.
- Group communication is a form of communication that involves sending messages to a subset of processes in a distributed system, called a group, rather than to a single process or to all processes. Group communication can be used to implement replication by allowing processes to coordinate their actions and exchange their states.
- There are different types of group communication, such as:
  - Broadcast communication: when a process sends a message to all processes in the system, or to all processes in a predefined group. Broadcast communication can be used to disseminate information or commands to all replicas, or to discover and join a group of replicas.
  - Multicast communication: when a process sends a message to a subset of processes in the system, or to a subset of processes in a predefined group. Multicast communication can be used to send updates or requests to a subset of replicas, or to partition a group of replicas into smaller groups.
  - Anycast communication: when a process sends a message to any one process in the system, or to any one process in a predefined group. Anycast communication can be used to send queries or requests to any replica that can provide a response or service, or to balance the load among replicas.
- Group communication can have different properties or guarantees, such as:
  - Reliability: the property that ensures that a message sent by a process is eventually delivered to all intended recipients, unless the sender or the recipients fail. Reliability can be further classified into best-effort, reliable, or atomic delivery, depending on the degree of assurance and ordering of messages.
  - Ordering: the property that ensures that messages sent by one or more processes are delivered to all recipients in the same order. Ordering can be further classified into FIFO, causal, total, or causal-total ordering, depending on the relation between the messages and the processes.
  - Agreement: the property that ensures that all correct processes in a group agree on a common value or decision, despite the presence of failures or asynchrony. Agreement can be further classified into consensus, atomic commit, or group membership, depending on the problem and the system model.



# Fault-Tolerant Services for the Notes of the Unit 10 - Replication in the Subject of Distributed System

Fault-tolerant services are services that can continue to function correctly even in the presence of failures, such as server crashes, network partitions, or malicious attacks. Replication is a common technique for achieving fault tolerance in distributed systems, by maintaining multiple copies of the same service or data across different nodes.

There are two main classes of replication techniques: primary-backup replication and active replication.

- Primary-backup replication: In this technique, one of the replicas is designated as the primary, and the others are backups. The primary is responsible for processing client requests and updating the backups. The backups are passive and only respond to the primary. If the primary fails, a new primary is elected from the backups. This technique requires less communication and computation than active replication, but it introduces a single point of failure and a bottleneck in the primary.

- Active replication: In this technique, all the replicas are active and process client requests in the same order. The replicas use a consensus protocol to agree on the order of requests and ensure consistency. This technique tolerates more failures than primary-backup replication, and does not have a single point of failure or a bottleneck. However, it requires more communication and computation than primary-backup replication, and it may introduce more latency and overhead.

There are also different models of faults that can affect replicated services, such as crash faults, omission faults, timing faults, and Byzantine faults.

- Crash faults: A crash fault occurs when a node stops functioning and does not send or receive any messages. This is the simplest and most common type of fault in distributed systems. Replication can tolerate crash faults by having enough replicas to continue the service in case some of them crash.

- Omission faults: An omission fault occurs when a node fails to send or receive some messages, but does not crash completely. This type of fault can be caused by network congestion, packet loss, or buffer overflow. Replication can tolerate omission faults by using reliable communication protocols, such as TCP, or by using timeouts and retransmissions.

- Timing faults: A timing fault occurs when a node deviates from the expected timing behavior, such as violating a deadline, sending a message too early or too late, or having a skewed clock. This type of fault can be caused by hardware or software errors, or by network delays or synchronization issues. Replication can tolerate timing faults by using synchronization protocols, such as NTP, or by using logical clocks, such as Lamport timestamps or vector clocks.

- Byzantine faults: A Byzantine fault occurs when a node behaves arbitrarily, such as sending incorrect or conflicting messages, or colluding with other faulty nodes. This type of fault can be caused by malicious attacks, software bugs, or hardware faults. Replication can tolerate Byzantine faults by using cryptographic techniques, such as digital signatures or encryption, or by using Byzantine agreement protocols, such as PBFT or Zyzzyva.



# Highly Available Services for the Notes of the Unit 10 - Replication in the Subject of Distributed System

- Replication is the process of creating and maintaining multiple copies of data or services across different nodes or locations in a distributed system.
- Replication can enhance the availability, reliability, performance, and scalability of distributed systems by reducing the impact of failures, network congestion, and data access latency.
- Replication can also enable load balancing, fault tolerance, and data consistency among the replicas.
- Replication can be classified into two types: eager replication and lazy replication.
  - Eager replication ensures that all the replicas are updated as soon as a change occurs in any of them. This requires synchronous communication and coordination among the replicas, which can increase the overhead and delay of the system. Eager replication can provide strong consistency guarantees, but it can also reduce the availability of the system in the presence of failures or partitions.
  - Lazy replication allows some replicas to be updated later than others, after a change occurs in any of them. This requires asynchronous communication and reconciliation among the replicas, which can reduce the overhead and delay of the system. Lazy replication can provide higher availability and performance, but it can also introduce inconsistency and conflicts among the replicas.
- Replication can be implemented at different levels of abstraction, such as data replication, service replication, or process replication.
  - Data replication involves creating and maintaining multiple copies of data items or databases across different nodes or locations. Data replication can be used to improve the availability and performance of data access, as well as to provide backup and recovery mechanisms. Data replication can be based on different models, such as primary-backup, master-slave, peer-to-peer, or quorum-based.
  - Service replication involves creating and maintaining multiple instances of a service or an application across different nodes or locations. Service replication can be used to improve the availability and performance of service invocation, as well as to provide load balancing and fault tolerance mechanisms. Service replication can be based on different techniques, such as stateless, stateful, or hybrid replication.
  - Process replication involves creating and maintaining multiple copies of a process or a thread across different nodes or locations. Process replication can be used to improve the availability and performance of process execution, as well as to provide fault tolerance and recovery mechanisms. Process replication can be based on different methods, such as checkpointing, logging, or message-passing.
- Replication can pose several challenges and trade-offs for distributed systems, such as:
  - How to create and maintain replicas across different nodes or locations?
  - How to ensure consistency and coherence among the replicas?
  - How to handle conflicts and concurrency among the replicas?
  - How to balance the benefits and costs of replication?
  - How to adapt to dynamic changes in the system, such as failures, partitions, or workload variations?
- Replication can be supported by various algorithms and protocols, such as:
  - Viewstamped replication, which is a primary-backup protocol that uses a leader election mechanism to select a primary replica that coordinates the updates and broadcasts them to the backup replicas.
  - Paxos, which is a quorum-based protocol that uses a consensus mechanism to agree on a sequence of updates among a set of replicas, and ensures that at least a majority of replicas are consistent at any time.
  - Raft, which is a simplified version of Paxos that uses a leader election mechanism to select a leader replica that proposes and commits the updates, and ensures that the leader and a majority of replicas are consistent at any time.
  - Dynamo, which is a peer-to-peer protocol that uses a consistent hashing mechanism to partition and replicate the data among a set of replicas, and uses a vector clock mechanism to detect and resolve conflicts among the replicas.
  - CRDTs, which are data structures that can be replicated and updated independently and concurrently by different replicas, and can be merged without conflicts or losses.



# Transactions with replicated data

- Transactions are a sequence of operations that are executed atomically, consistently, isolatedly, and durably (ACID properties) on a database system.
- Replication is a technique to distribute data across multiple servers or locations, while maintaining consistency and availability of the data.
- Transactions with replicated data are transactions that involve data items that are replicated on different servers or locations, and need to be coordinated to ensure the ACID properties.
- Transactions with replicated data pose several challenges for distributed systems, such as:
  - How to ensure atomicity of transactions that span multiple servers or locations, and may encounter failures or network partitions?
  - How to ensure consistency of replicated data items, and prevent conflicts or anomalies among concurrent transactions?
  - How to ensure isolation of transactions that access replicated data items, and avoid interference or inconsistency among concurrent transactions?
  - How to ensure durability of transactions that update replicated data items, and guarantee that the updates are persisted and propagated to all replicas?
- There are different approaches to address these challenges, such as:
  - Using two-phase commit (2PC) protocol to coordinate the commit or abort of transactions that span multiple servers or locations, and ensure atomicity and durability of transactions. 2PC involves a coordinator and multiple participants, and consists of two phases: prepare and commit. In the prepare phase, the coordinator asks the participants to vote on whether they are ready to commit or abort the transaction. In the commit phase, the coordinator decides on the final outcome of the transaction based on the votes, and informs the participants to either commit or abort the transaction accordingly. 2PC ensures that either all participants commit the transaction, or none of them do. However, 2PC has some drawbacks, such as blocking, vulnerability to failures, and performance overhead.
  - Using quorum-based protocols to coordinate the read and write operations on replicated data items, and ensure consistency and availability of the data. Quorum-based protocols involve assigning a weight to each replica, and defining a read quorum and a write quorum for each data item. A read quorum is the minimum weight of replicas that need to be contacted to perform a read operation on a data item. A write quorum is the minimum weight of replicas that need to be updated to perform a write operation on a data item. Quorum-based protocols ensure that any two read quorums or any read quorum and write quorum for the same data item have at least one replica in common, and thus prevent conflicts or anomalies among concurrent transactions. However, quorum-based protocols have some drawbacks, such as complexity, scalability, and availability issues.
  - Using optimistic concurrency control (OCC) techniques to validate the transactions that access replicated data items, and ensure isolation and consistency of transactions. OCC techniques involve three phases: read, validate, and write. In the read phase, the transaction reads the data items from the replicas, and records the versions or timestamps of the data items. In the validate phase, the transaction checks if the versions or timestamps of the data items have changed since the read phase, and aborts the transaction if there is a conflict with another concurrent transaction. In the write phase, the transaction updates the data items on the replicas, and increments the versions or timestamps of the data items. OCC techniques ensure that the transactions do not interfere or cause inconsistency with each other, and avoid locking or blocking the data items. However, OCC techniques have some drawbacks, such as aborting and restarting transactions, and maintaining versions or timestamps of data items.

