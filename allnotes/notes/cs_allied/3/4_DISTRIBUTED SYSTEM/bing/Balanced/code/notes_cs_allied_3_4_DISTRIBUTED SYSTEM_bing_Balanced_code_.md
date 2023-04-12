

# Distributed System

A distributed system is a system whose components are located on different networked computers, which communicate and coordinate their actions by passing messages to one another. A distributed system can also be defined as a number of independent computers linked by a network, or a computing environment in which various components are spread across multiple computers (or other computing devices) on a network.

Some of the main characteristics of a distributed system are:

- The components are autonomous, meaning they can operate independently and have their own failure modes.
- The components are heterogeneous, meaning they can have different hardware, software, operating systems, and protocols.
- The components are scalable, meaning the system can handle increasing workload or number of components without significant degradation of performance or reliability.
- The components are transparent, meaning the system hides the complexity and distribution of the components from the users and applications.

Some of the main challenges of a distributed system are:

- The components are prone to failures, such as crashes, network partitions, or malicious attacks, and the system must be able to tolerate and recover from them.
- The components are concurrent, meaning they can execute simultaneously and interact with each other, and the system must ensure consistency and coordination among them.
- The components are distributed, meaning they can have different clocks, latencies, and bandwidths, and the system must cope with the uncertainty and variability of the network.

Some of the main benefits of a distributed system are:

- The components are modular, meaning they can be reused, replaced, or added without affecting the rest of the system.
- The components are parallel, meaning they can exploit the computational power and resources of multiple machines to achieve higher performance and efficiency.
- The components are distributed, meaning they can leverage the geographical proximity and diversity of the machines to improve availability and reliability.



# Unit 1 - Characterization of Distributed Systems

A distributed system is a collection of independent computers that appear to the users as a single coherent system. Some examples of distributed systems are the Internet, the World Wide Web, peer-to-peer networks, cloud computing, and distributed databases.

Some of the main characteristics of distributed systems are:

- **Concurrency**: Multiple components can execute simultaneously and interact with each other.
- **Lack of a global clock**: There is no shared physical clock among the components, so it is hard to synchronize events or order them causally.
- **Independent failures**: Each component can fail independently, without affecting the rest of the system. The system has to cope with partial failures and ensure availability and reliability.
- **Heterogeneity**: The components can have different hardware, software, network, and data formats. The system has to provide interoperability and transparency to the users.
- **Scalability**: The system can grow in size and complexity without degrading its performance or functionality. The system has to deal with load balancing, resource allocation, and fault tolerance.

Some of the main challenges of designing and implementing distributed systems are:

- **Transparency**: The system should hide its complexity and heterogeneity from the users and provide a consistent and uniform interface.
- **Security**: The system should protect its data and resources from unauthorized access, modification, or disclosure. The system should also ensure confidentiality, integrity, and availability of its services.
- **Performance**: The system should provide efficient and timely communication and computation among the components. The system should also minimize the overhead and latency of its operations.
- **Fault tolerance**: The system should detect, isolate, and recover from failures of its components. The system should also provide replication and backup mechanisms to ensure data consistency and durability.
- **Consistency**: The system should provide a coherent and accurate view of its data and state to the users and the components. The system should also handle concurrency and synchronization issues among the components.



### Introduction for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- The main characteristics of a distributed system are:
  - Concurrency: Multiple components can execute simultaneously and interact with each other.
  - No global clock: There is no shared physical clock among the components, so synchronization and coordination are challenging.
  - Independent failures: Each component can fail independently without affecting the whole system, so fault tolerance and recovery are important.
- The main advantages of a distributed system are:
  - Scalability: The system can grow in size and performance by adding more components.
  - Availability: The system can tolerate failures and provide continuous service to the users.
  - Heterogeneity: The system can accommodate different types of components, such as hardware, software, network, etc.
  - Transparency: The system can hide the complexity and diversity of the components from the users and provide a uniform interface.
- The main challenges of a distributed system are:
  - Communication: The system has to deal with network delays, failures, and security issues.
  - Coordination: The system has to ensure consistent and correct behavior of the components, such as mutual exclusion, agreement, etc.
  - Replication: The system has to manage multiple copies of data and ensure their consistency and availability.
  - Fault tolerance: The system has to detect, mask, and recover from failures of the components.
  - Security: The system has to protect the data and resources from unauthorized access and malicious attacks.



### Examples of Distributed Systems

A distributed system is a collection of independent computers that communicate and coordinate their actions by passing messages. The computers in a distributed system may be physically close or geographically dispersed, and they may be connected by a network or a bus. Distributed systems can provide higher performance, reliability, scalability, and availability than centralized systems.

Some examples of distributed systems are:

- **Telecommunication networks**: Telephone networks are an early example of a peer-to-peer network, where each node can initiate or receive calls. Cellular and telephone networks are forms and examples of distributed networks. They use routing algorithms and protocols to establish and maintain connections, and to handle failures and congestion.  
- **Real-time systems**: Many industries use real-time systems distributed in various areas, locally and globally. For example, air traffic control systems, power grid systems, industrial control systems, and autonomous vehicles are all examples of real-time distributed systems. They have strict timing and reliability requirements, and they use synchronization and coordination mechanisms to ensure consistent and correct behavior. 
- **Distributed database systems**: A distributed database has locations across multiple servers, physical locations, or both. The data may be replicated or partitioned, and the system may use different consistency models and concurrency control techniques to ensure data integrity and availability. Examples of distributed database systems are Google's Bigtable, Amazon's Dynamo, and MongoDB.  
- **Distributed computing platforms**: A distributed computing platform is a system that allows multiple computers to work together on a common task, such as processing large data sets, performing complex calculations, or rendering graphics. Examples of distributed computing platforms are MapReduce, Spark, Hadoop, and BOINC.  
- **Distributed web applications**: A distributed web application is a system that delivers web content and services to users over the Internet. The system may use multiple web servers, load balancers, caches, databases, and other components to handle requests and provide functionality. Examples of distributed web applications are Facebook, Twitter, Netflix, and Amazon.



### Resource sharing and the web challenges

Resource sharing is the process of making the resources of a distributed system available to the users and applications in a transparent and efficient way . Resources can be hardware, software, or data. Resource sharing can be achieved by different methods, such as:

- Data migration: transferring data from one location to another in the system.
- Computation migration: transferring computation from one location to another in the system.
- Process migration: transferring a running process from one location to another in the system.
- Load balancing: distributing the workload among different locations in the system.

The web is an example of a large-scale distributed system that enables resource sharing among millions of users and applications. The web is based on the client-server model, where clients request resources from servers and servers respond with the requested resources. The web uses the HTTP protocol for communication and the URL scheme for identifying resources.

The web faces many challenges in distributed systems, such as:

- Scalability: the ability to handle increasing load and demand without degrading the performance or functionality of the system .
- Heterogeneity: the ability to communicate and interoperate with different devices, platforms, languages, and formats .
- Fault tolerance: the ability to cope with failures and errors without losing data or service availability.
- Security: the ability to protect the data and resources from unauthorized access, modification, or disclosure.
- Consistency: the ability to maintain a coherent and accurate view of the data and resources across different locations and replicas.



### Architectural models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Architectural models are a type of system model that describe the organization and interrelationship of components in a distributed system .
- Architectural models can help to understand the design trade-offs, performance, scalability, reliability, and security of distributed systems .
- Architectural models can be classified into different styles, such as:
  - Layered architecture: Components are organized in layers, each layer communicates with its adjacent layer by sending requests and getting responses. For example, a web application can have a presentation layer, a business logic layer, and a data access layer.
  - Client-server architecture: Components are divided into clients and servers, clients request services from servers and servers provide services to clients. For example, a web browser is a client that requests web pages from a web server.
  - Broker architecture: Components are connected by a broker that mediates communication and coordination among them. For example, CORBA is a broker architecture that allows components written in different languages and running on different platforms to interoperate.
  - Service-oriented architecture: Components are loosely coupled services that can be discovered, composed, and invoked over a network. For example, SOAP and REST are protocols for implementing service-oriented architectures.
  - Peer-to-peer architecture: Components are peers that can act as both clients and servers, and communicate directly with each other without a central authority. For example, BitTorrent is a peer-to-peer architecture for file sharing.
  - Distributed network architecture: Components are networks that can interact with other networks for service resiliency, performance gains, and resource sharing. For example, the Internet is a distributed network architecture that connects millions of networks around the world.



# Fundamental Models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Fundamental models are descriptions of properties that are present in all distributed architectures  .
- They help us understand the characteristics, challenges and trade-offs of designing and implementing distributed systems.
- There are three main types of fundamental models: interaction models, failure models and security models  .

## Interaction Models
- Interaction models deal with the issues of how processes communicate and coordinate with each other in a distributed system  .
- They include aspects such as performance, timing, ordering, consistency and synchronization of events  .
- Some examples of interaction models are:
  - Synchronous vs. asynchronous communication: whether the sender and receiver of a message have to wait for each other or not  .
  - Remote procedure call (RPC): a method of invoking a procedure or function on a remote machine as if it were local  .
  - Publish-subscribe: a pattern where publishers send messages to a broker, and subscribers receive messages that match their interests  .
  - Peer-to-peer: a model where each node can act as both a client and a server, and communicate directly with other nodes  .

## Failure Models
- Failure models specify the types of faults that can occur in a distributed system, and how they affect the processes and communication channels  .
- They help us design fault-tolerant and resilient systems that can cope with failures and recover from them  .
- Some examples of failure models are:
  - Crash failures: when a process stops executing and does not resume  .
  - Omission failures: when a process fails to send or receive a message  .
  - Timing failures: when a process does not meet the timing constraints of the system  .
  - Byzantine failures: when a process behaves arbitrarily or maliciously, and may send incorrect or conflicting messages  .

## Security Models
- Security models define the goals and requirements of protecting a distributed system from unauthorized access, modification or disclosure of information  .
- They include aspects such as confidentiality, integrity, availability, authentication, authorization and non-repudiation  .
- Some examples of security models are:
  - Cryptography: the use of mathematical techniques to encrypt and decrypt data, and to verify its authenticity and origin  .
  - Kerberos: a protocol that uses tickets and keys to authenticate users and services in a distributed system  .
  - Blockchain: a distributed ledger that uses consensus algorithms and cryptographic hashes to ensure the validity and immutability of transactions  .



### Theoretical Foundation for Distributed System

A distributed system is a collection of independent processes that communicate with each other by exchanging messages over a network. The processes may be located on different machines, have different speeds, and operate under different failure modes. The main challenges of designing and implementing distributed systems are:

- **Coordination**: How to ensure that the processes agree on a consistent view of the system state and cooperate to achieve a common goal.
- **Fault-tolerance**: How to cope with the possibility of process crashes, network failures, message losses, and malicious attacks.
- **Performance**: How to optimize the system throughput, latency, scalability, and resource utilization.

To address these challenges, distributed systems rely on various theoretical concepts and techniques, such as:

- **Logical clocks**: A way of assigning logical timestamps to events and messages in a distributed system, such that the causal order of events is preserved. Logical clocks can be used to implement synchronization, concurrency control, and consistency protocols. There are different types of logical clocks, such as Lamport clocks, vector clocks, and matrix clocks.
- **Global states**: A way of capturing the global state of a distributed system at a certain point in time, by combining the local states of the processes and the messages in transit. Global states can be used to detect global properties, such as deadlock, termination, and safety. There are different methods of obtaining global states, such as snapshot algorithms, distributed debugging, and checkpointing.
- **Consensus**: A way of reaching agreement among a set of processes on a common value, despite the presence of failures and asynchrony. Consensus is a fundamental problem in distributed systems, as it enables coordination, replication, and fault-tolerance. There are different algorithms for solving consensus, such as Paxos, Raft, and Byzantine agreement.
- **Distributed algorithms**: A way of designing and analyzing algorithms that run on multiple processes and communicate by messages. Distributed algorithms have to deal with the complexity and uncertainty of distributed systems, such as partial knowledge, concurrency, asynchrony, and failures. There are different techniques for designing and analyzing distributed algorithms, such as complexity measures, correctness proofs, lower bounds, and impossibility results.



### Limitation of Distributed system

A distributed system is a system that consists of multiple independent components that communicate with each other over a network. Distributed systems have many advantages, such as scalability, fault tolerance, and performance. However, they also face some limitations that make them challenging to design and implement. Some of the main limitations of distributed systems are:

- **Absence of a global state**: In a distributed system, there is no single point of control or coordination for the entire system. Each component has its own local state and view of the system, which may differ from the views of other components. This makes it difficult to reason about the behavior and correctness of the system as a whole, and to ensure consistency and coherence among the components. For example, it is hard to implement transactions, concurrency control, and replication in a distributed system without a global state  .

- **Absence of a global clock**: In a distributed system, there is no common notion of time or ordering of events among the components. Each component has its own local clock, which may drift or be inaccurate. This makes it hard to synchronize the actions and data of the components, and to establish causality and precedence among the events. For example, it is hard to implement consensus, agreement, and coordination protocols in a distributed system without a global clock .

- **Network issues**: In a distributed system, the communication among the components depends on the underlying network, which may be unreliable, unpredictable, or insecure. The network may introduce delays, losses, errors, or failures in the messages, or may be subject to attacks or interference. This makes it hard to ensure the availability, reliability, and security of the system, and to handle the failures and recoveries of the components. For example, it is hard to implement fault tolerance, load balancing, and encryption in a distributed system without a reliable network  .

- **Scalability issues**: In a distributed system, the number and size of the components may grow or shrink dynamically, depending on the demand and resources of the system. This makes it hard to maintain the performance, efficiency, and quality of the system, and to adapt to the changing conditions and requirements of the system. For example, it is hard to implement load balancing, resource allocation, and caching in a distributed system without a scalable architecture  .

These limitations of distributed systems pose many challenges and trade-offs for the designers and developers of such systems. They require careful analysis, design, and implementation of the system components, protocols, and algorithms, as well as rigorous testing, debugging, and evaluation of the system. They also require the use of various techniques and tools, such as distributed algorithms, middleware, frameworks, and platforms, to overcome or mitigate the limitations and to achieve the desired goals and properties of the system.



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

Shared memory is a programming model for distributed systems that allows multiple processes to access a common logical address space, which may be physically distributed across different nodes. Shared memory can simplify the communication and synchronization among processes, as well as enable the efficient sharing of data and resources.

There are two main types of shared memory systems:

- **Hardware-based shared memory**: These systems have a physically shared memory that is accessed by multiple processors through a common bus or interconnection network. Hardware mechanisms, such as cache coherence protocols, ensure the consistency and coherence of the shared memory. Examples of hardware-based shared memory systems are multiprocessors and multicomputers.
- **Software-based shared memory**: These systems implement the shared memory model on top of a physically distributed memory system, using software techniques such as page-based, object-based, or tuple-based approaches. Software-based shared memory systems are also known as distributed shared memory (DSM) systems. Examples of DSM systems are Ivy, Munin, and TreadMarks.

The advantages of shared memory systems are:

- They provide a simple and familiar programming model for distributed systems, as they abstract away the details of message passing and network communication.
- They allow the efficient sharing of data and resources among processes, as they avoid the overhead of data copying and serialization.
- They facilitate the development of parallel and concurrent applications, as they enable the use of synchronization primitives such as locks, semaphores, and monitors.

The disadvantages of shared memory systems are:

- They may incur high communication costs, especially in software-based shared memory systems, as they need to transfer pages, objects, or tuples across the network to maintain the consistency and coherence of the shared memory.
- They may suffer from scalability issues, as the size and complexity of the shared memory space may increase with the number of processes and nodes.
- They may introduce security and reliability risks, as the shared memory space may be vulnerable to malicious or faulty processes that can corrupt or tamper with the shared data and resources.



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
  - Accuracy: If the logical clock of A is less than the logical clock of B, then event A causally precedes event B.
  - Completeness: If the logical clock of A is equal to the logical clock of B, then event A and event B are concurrent.
- The main challenges of logical clocks are:
  - How to synchronize the logical clocks of different processes in a distributed system .
  - How to deal with clock drift, network delays, message losses, and failures in a distributed system .
  - How to minimize the overhead of maintaining and exchanging logical clocks in a distributed system .



### Lamport's logical clocks

- Lamport's logical clocks are a way of ordering events in a distributed system without relying on physical clocks.
- Lamport's logical clocks are based on the concept of a **happens-before** relation, denoted by `->`, which captures the causal order of events.
- If `a` and `b` are events on the same process, then `a -> b` if `a` occurs before `b` based on the local clock.
- If `a` is the event of sending a message by one process and `b` is the event of receiving that message by another process, then `a -> b`.
- The happens-before relation is transitive, meaning that if `a -> b` and `b -> c`, then `a -> c`.
- Lamport's logical clocks are implemented by assigning a numerical value, called a **timestamp**, to each event that occurs in the system.
- Each process maintains a local counter that is incremented after each event that occurs on that process.
- The timestamp of an event is the value of the counter when the event occurs.
- When a process sends a message, it attaches its current counter value to the message.
- When a process receives a message, it updates its counter to be the maximum of its own counter and the timestamp of the message, and then increments it by one.
- Lamport's logical clocks ensure that if `a -> b`, then the timestamp of `a` is less than the timestamp of `b`.
- However, the converse is not true, meaning that if the timestamp of `a` is less than the timestamp of `b`, it does not imply that `a -> b`.
- Therefore, Lamport's logical clocks can only partially order the events in the system, and there may be some events that are **concurrent**, meaning that they are not causally related.
- Lamport's logical clocks are simple and easy to implement, but they do not capture the full causal order of events in the system.



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
  - Synchronous, where the sender and the receiver are synchronized by the message exchange.
  - Asynchronous, where the sender and the receiver are independent and do not wait for each other.
- Message passing can be classified into two types based on the direction of communication:
  - Unidirectional, where the messages are sent in one direction only.
  - Bidirectional, where the messages are sent and received in both directions.
- Message passing can also be classified into two types based on the number of receivers:
  - Point-to-point, where the message is sent to a single receiver.
  - Broadcast, where the message is sent to multiple receivers.
- Message passing can also be classified into two types based on the delivery order:
  - FIFO, where the messages are delivered in the same order as they are sent.
  - Non-FIFO, where the messages are delivered in any order.



### Causal order for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Causal order is a way of ordering events in a distributed system based on their causal relationships, rather than their physical timestamps or global clocks.
- Causal order captures the notion of potential influence or dependence between events, such as sending and receiving messages, updating and reading shared data, or triggering and observing actions.
- Causal order is important for ensuring consistency, correctness, and coordination in distributed systems, especially when dealing with concurrent or conflicting events.
- Causal order can be defined formally using the concept of Lamport's happened-before relation, denoted by `->`, which is a partial order on the set of events in a distributed system.
- Lamport's happened-before relation states that if event `a` happens before event `b` in the same process, then `a -> b`. If event `a` is the sending of a message by one process and event `b` is the receipt of that message by another process, then `a -> b`. If `a -> b` and `b -> c`, then `a -> c` (transitivity).
- Two events `a` and `b` are said to be concurrent, denoted by `a || b`, if neither `a -> b` nor `b -> a` holds. Concurrent events are not causally related and can happen in any order without affecting the outcome of the system.
- Causal order can be implemented in distributed systems using various techniques, such as vector clocks, logical clocks, or message ordering protocols.
- Vector clocks are arrays of integers that keep track of the number of events that have happened in each process. Each process increments its own entry in the vector clock whenever it performs a local event, and piggybacks its vector clock on every message it sends. Each process updates its vector clock by taking the element-wise maximum of its own vector clock and the vector clock received in a message. Vector clocks can be used to determine the causal order of events by comparing their vector clocks: `a -> b` if and only if `a[i] <= b[i]` for all `i`, and `a[i] < b[i]` for some `i`.
- Logical clocks are scalar values that represent the logical time of events in a distributed system. Each process maintains its own logical clock and increments it whenever it performs a local event. Each process also attaches its logical clock to every message it sends. Each process updates its logical clock by taking the maximum of its own logical clock and the logical clock received in a message, plus one. Logical clocks can be used to determine the causal order of events by comparing their logical clocks: `a -> b` if and only if `a < b`.
- Message ordering protocols are rules that specify how messages should be delivered or processed in a distributed system to ensure causal order. For example, a causal multicast protocol ensures that messages are delivered to all processes in the same causal order, by buffering messages that arrive out of order until their causal predecessors have been delivered. A causal consistency protocol ensures that read operations on shared data return the latest write operation that is causally preceding or concurrent with the read operation, by propagating updates along causal paths.



### Total Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent entities that communicate by message passing to achieve a common goal.
- Events are the occurrences of actions or changes of state in a distributed system.
- The order of events is important for ensuring the consistency and correctness of the distributed system.
- A partial order is a binary relation that is reflexive, antisymmetric, and transitive. A partial order can be represented by a directed acyclic graph (DAG).
- A total order is a partial order that is also complete, meaning that any two elements are comparable. A total order can be represented by a linear sequence.
- A distributed system is said to have partial order if we can have a partial order relationship among the events in the system .
- A distributed system is said to have total order if we can establish a causal relationship among all events in the system .
- A causal relationship means that if an event A causes or influences another event B, then A must happen before B in the order of events.
- A total order can be achieved by using logical clocks, such as Lamport timestamps, that assign a unique and monotonically increasing value to each event in the system .
- Lamport timestamps can be used to create a total order of events in a distributed system by using some arbitrary mechanism to break ties (e.g. the ID of the process).
- A total order is useful for distributed system implementation, as it can help ensure the consistency and synchronization of the shared state and resources among the entities.



### Total Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent processes that communicate by exchanging messages over a network.
- Events are occurrences that happen at a specific point in time and space in a distributed system, such as sending or receiving a message, or executing a local operation.
- The order of events is important for understanding the behavior and correctness of a distributed system, especially in the presence of concurrency and failures.
- A partial order is a binary relation that satisfies three properties: reflexivity, antisymmetry, and transitivity. A partial order can be represented by a directed acyclic graph (DAG), where nodes are events and edges are ordering relations.
- A causal order is a partial order that captures the notion of potential causality between events. An event e1 is causally related to another event e2, denoted by e1 -> e2, if one of the following conditions holds:
  - e1 and e2 are events in the same process, and e1 happened before e2.
  - e1 is the sending of a message m, and e2 is the receipt of the same message m.
  - There exists some event e3 such that e1 -> e3 and e3 -> e2.
- A total order is a partial order that satisfies an additional property: comparability. This means that for any two events e1 and e2, either e1 -> e2, or e2 -> e1, or both (if e1 and e2 are the same event). A total order can be represented by a linear sequence of events, where each event is ordered before or after every other event.
- A total causal order is a total order that is consistent with the causal order. This means that if e1 -> e2 in the causal order, then e1 -> e2 in the total order as well. A total causal order establishes a unique linearization of all the events in the system, even those that are concurrent (not causally related).
- A total causal order is useful for ensuring consistency and agreement among the processes in a distributed system. For example, a total causal order can be used to implement atomic broadcast, a communication primitive that guarantees that all processes deliver the same set of messages in the same order. A total causal order can also be used to implement distributed snapshots, a technique for capturing the global state of a distributed system at a certain point in time.
- A total causal order is difficult to achieve in a distributed system, because it requires global synchronization and coordination among the processes. There are different algorithms and protocols that can be used to implement a total causal order, such as vector clocks, logical clocks, or consensus algorithms. These algorithms typically incur some overhead in terms of time, space, or message complexity.



### Techniques for Message Ordering in Distributed Systems

Message ordering is the problem of ensuring that messages sent by different processes in a distributed system are received and processed in a consistent and meaningful order. Message ordering is important for achieving correctness, consistency, and coordination in distributed applications.

There are different techniques for message ordering in distributed systems, depending on the requirements and assumptions of the system. Some of the common techniques are:

- **Non-FIFO ordering**: This is the simplest and most basic technique, where messages are delivered in any order, without any guarantee of preserving the order of sending. This technique is suitable for applications that do not depend on the order of messages, such as broadcasting or multicasting. However, this technique can lead to confusion and inconsistency in applications that require some order of messages, such as distributed transactions or consensus protocols.

- **FIFO ordering**: This technique ensures that messages sent by the same process are delivered in the same order as they were sent. This technique is useful for applications that need to preserve the causal order of events within a process, such as logging or auditing. However, this technique does not guarantee any order between messages sent by different processes, which can still cause inconsistency or ambiguity in applications that need to coordinate across processes, such as distributed mutual exclusion or leader election.

- **Causal ordering**: This technique ensures that messages that are causally related are delivered in the same order as they were sent. Two messages are causally related if one message is sent as a result of receiving or sending another message. For example, if process A sends a message m1 to process B, and then process B sends a message m2 to process C, then m1 and m2 are causally related. This technique is useful for applications that need to preserve the logical order of events across processes, such as distributed snapshots or replicated data. However, this technique does not guarantee any order between messages that are not causally related, which can still cause inconsistency or divergence in applications that need to achieve global agreement or synchronization, such as distributed commit or atomic broadcast.

- **Total ordering**: This technique ensures that all messages are delivered in the same order to all processes. This technique is useful for applications that need to achieve global consistency and coordination across processes, such as distributed consensus or state machine replication. However, this technique is the most expensive and difficult to implement, as it requires a global agreement on the order of messages, which can be affected by network delays, failures, or partitions. There are different algorithms for achieving total ordering, such as logical clocks, vector clocks, or consensus protocols.



### Causal ordering of messages

- Causal ordering of messages is a partial ordering of messages in a distributed computing environment .
- It places a restriction on communication between processes by requiring that if the transmission of message mi to process pk necessarily preceded the transmission of message mj to the same process, then the delivery of these messages to that process must be ordered such that mi is delivered before mj .
- Causal ordering of messages is one of the four semantics of multicast communication, namely unordered, totally ordered, causal, and sync-ordered communication.
- Multicast communication methods vary according to the message’s reliability guarantee and ordering guarantee.
- Causal ordering of messages is based on the concept of potential causality, which is defined by the following rules :
  - If a process pi sends a message m1 and then sends another message m2, then m1 -> m2 (-> denotes potential causality).
  - If a process pi sends a message m1 to another process pj, and pj receives m1 and then sends a message m2 to another process pk, then m1 -> m2.
  - If m1 -> m2 and m2 -> m3, then m1 -> m3 (transitivity).
  - If not (m1 -> m2), then m1 and m2 are concurrent (denoted by m1 || m2), meaning that m1 cannot possibly have caused m2 .
- Causal ordering of messages can be implemented by various algorithms, such as vector clocks, logical clocks, or piggybacking  .
- Causal ordering of messages can help to ensure consistency, correctness, and fault tolerance in distributed systems  .



### Global State for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent processes that communicate through message passing.
- The global state of a distributed system is the union of the local states of the processes and the channels .
- A local state of a process is the values of its variables and registers at a given point in time.
- A channel state is the set of messages that have been sent but not yet received by the processes.
- A global state is consistent if it reflects a possible execution of the system, i.e., no causal violations occur .
- A causal violation is when a message is received before it is sent, or a process observes the effect of a message before it observes the message itself.
- A consistent global state can be used for debugging, checkpointing, termination detection, and other applications in distributed systems  .
- A consistent global state can be recorded by using distributed snapshot algorithms, which are protocols that allow processes to coordinate and capture their local states and channel states without blocking or synchronizing.
- A distributed snapshot algorithm must satisfy two properties: correctness and termination.
- Correctness means that the recorded global state is consistent and reflects a possible execution of the system.
- Termination means that the algorithm eventually completes and all processes resume their normal execution.



### Termination Detection

Termination detection is a fundamental problem in distributed systems, where a set of processes cooperate to perform a computation. The problem is to determine when all the processes have finished their work and there are no more messages in transit. This is non-trivial because no process has complete knowledge of the global state, and global time does not exist.

One of the algorithms for termination detection is Huang's algorithm, proposed by Shing-Tsaan Huang in 1989. The algorithm is based on the concept of a process' state, which can be either active or idle. An active process may become idle at any time, but an idle process may only become active again upon receiving a computational message (a message that affects the computation). A process is also assigned a weight, which is initially 1, and a control message counter, which is initially 0. The algorithm uses a special process called the initiator, which initiates and collects the termination information.

The algorithm works as follows:

- The initiator sends a control message to itself with its own weight and counter.
- When a process receives a control message, it adds the weight and counter of the message to its own weight and counter, and forwards the message to its successor in a logical ring of processes. If the process is idle, it also sets its weight to 0.
- When a process sends or receives a computational message, it increments its counter by 1.
- When the initiator receives the control message back, it compares the weight and counter of the message with its own weight and counter. If they are equal, it declares termination. Otherwise, it repeats the algorithm from step 1.

The algorithm ensures that termination is detected if and only if all the processes are idle and there are no messages in transit. The algorithm also preserves the correctness and progress of the underlying computation, and does not require additional communication channels. The algorithm has a message complexity of O(n) and a time complexity of O(n), where n is the number of processes.



## Unit 2 - Distributed Mutual Exclusion

- Distributed mutual exclusion is the problem of ensuring that only one process at a time can access a shared resource in a distributed system.
- Distributed mutual exclusion algorithms can be classified into two categories: token-based and permission-based.
- Token-based algorithms use a special message, called a token, that grants the right to enter the critical section. The token is passed among the processes in a predefined order or by request. Only the process that holds the token can enter the critical section. Examples of token-based algorithms are the ring algorithm, the Suzuki-Kasami algorithm, and the Raymond algorithm.
- Permission-based algorithms use a voting scheme, where a process that wants to enter the critical section must request permission from a set of processes, called the quorum. The process can enter the critical section only if it receives a positive reply from all the processes in the quorum. Examples of permission-based algorithms are the Ricart-Agrawala algorithm, the Maekawa algorithm, and the Lamport algorithm.
- Distributed mutual exclusion algorithms must satisfy the following properties:
  - Safety: No two processes can be in the critical section at the same time.
  - Liveness: Every request to enter the critical section is eventually granted.
  - Fairness: No process is indefinitely postponed from entering the critical section.
- Distributed mutual exclusion algorithms can be evaluated based on the following performance metrics:
  - Message complexity: The number of messages exchanged per critical section entry.
  - Synchronization delay: The time elapsed between a process requesting and entering the critical section.
  - Response time: The time elapsed between a process requesting and receiving the token or permission.
  - System throughput: The number of critical section executions per unit time.



### Classification of distributed mutual exclusion

Distributed mutual exclusion is a problem of ensuring that only one process in a distributed system can access a shared resource or data at a time. It is a fundamental requirement for achieving consistency, coordination and synchronization among the processes.

There are three basic approaches for implementing distributed mutual exclusion:

- Token-based approach: A unique token is shared among the sites. A site is allowed to enter its critical section if it possesses the token. Mutual exclusion is ensured because the token is unique. Examples of token-based algorithms are Suzuki-Kasami's algorithm, Raymond's algorithm and Maekawa's algorithm .
- Non-token-based approach: A site requests permission from other sites before entering its critical section. A site is allowed to enter its critical section if it receives permission from all or a majority of other sites. Mutual exclusion is ensured by using a logical clock or a vector clock to order the requests. Examples of non-token-based algorithms are Lamport's algorithm, Ricart-Agrawala's algorithm and Singhal's algorithm .
- Quorum-based approach: A site requests permission from a subset of sites, called a quorum, before entering its critical section. A site is allowed to enter its critical section if it receives permission from all the sites in the quorum. Mutual exclusion is ensured by ensuring that any two quorums have at least one site in common. Examples of quorum-based algorithms are S. Toueg's algorithm, Naimi-Trehel's algorithm and Agrawal-El Abbadi's algorithm .



### Requirement of mutual exclusion theorem for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM

- Mutual exclusion is a concurrency control property which is introduced to prevent race conditions.
- It is the requirement that a process can not enter its critical section while another concurrent process is currently present or executing in its critical section.
- A critical section is a shared resource or data that can be accessed by only one process at a time .
- Mutual exclusion in a distributed system states that only one process is allowed to execute the critical section at any given time  .
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion .
- Message passing is the sole means for implementing distributed mutual exclusion .
- There are three basic approaches for implementing distributed mutual exclusion:
  - Token-based algorithms: A process can enter the critical section only if it possesses a unique token that is passed among the processes in a logical ring or a tree.
  - Permission-based algorithms: A process can enter the critical section only if it obtains permission from all or a subset of the other processes in the system.
  - Quorum-based algorithms: A process can enter the critical section only if it obtains permission from a majority or a weighted majority of the processes in the system.
- The performance of distributed mutual exclusion algorithms can be measured by the following metrics:
  - Message complexity: The number of messages exchanged per critical section entry.
  - Synchronization delay: The delay between the time a process requests to enter the critical section and the time it actually enters it.
  - System throughput: The number of times the critical section is executed per unit time.



### Token based and non token based algorithms for distributed mutual exclusion

Distributed mutual exclusion (DME) is the problem of ensuring that only one process at a time can access a shared resource in a distributed system. There are two main types of algorithms for DME: token based and non token based.

- Token based algorithms
  - In token based algorithms, a unique token is shared among all the processes in the system. The token represents the permission to enter the critical section. Only the process that holds the token can access the shared resource.
  - A process that wants to enter the critical section must request the token from the current holder. The token is passed from one process to another in a logical order, such as a ring or a tree. The process that receives the token must release it after exiting the critical section.
  - Token based algorithms are simple and efficient, but they have some drawbacks. For example, the token may be lost or duplicated due to message failures, or the token may be delayed due to network congestion. Also, the token may be underutilized if some processes do not need to access the critical section frequently.
  - Examples of token based algorithms are:
    - Suzuki-Kasami algorithm: This is a modification of Ricart-Agrawala algorithm, a permission based algorithm that uses REQUEST and REPLY messages to ensure mutual exclusion. In Suzuki-Kasami algorithm, the token contains a vector of sequence numbers, one for each process. The sequence number of a process indicates the number of times it has entered the critical section. A process that wants to enter the critical section sends a REQUEST message with its sequence number to the token holder. The token holder compares the sequence number with the corresponding entry in the token vector. If the sequence number is larger, it means that the process has not entered the critical section since the last time it received the token, and thus it grants the token to the process. Otherwise, it ignores the request. The token holder also updates the token vector with the sequence numbers of the processes that have requested the token. This way, the token holder knows which process has the highest priority to receive the token next.
    - Raymond's algorithm: This is a tree-based algorithm that organizes the processes into a logical tree. The root of the tree holds the token, and the children of a node are the processes that have requested the token from that node. A process that wants to enter the critical section sends a REQUEST message to its parent in the tree. The parent forwards the request to its parent, and so on, until the request reaches the root. The root then sends the token to the process that requested it, along the path of the request. The process that receives the token becomes the new root of the tree, and its parent becomes its child. A process that exits the critical section sends the token to one of its children, if any, or to its parent, if none. The process that receives the token becomes the new root of the tree, and its parent becomes its child.

- Non token based algorithms
  - In non token based algorithms, there is no token in the system. Instead, the processes use timestamps to order the requests for the critical section and to resolve conflicts between simultaneous requests. A process that wants to enter the critical section sends a REQUEST message with its timestamp to a set of other processes, such as all or a subset of the processes in the system. The process waits for the REPLY messages from the other processes, indicating that they have granted the permission to enter the critical section. The process can enter the critical section only when it has received the REPLY messages from all the processes in the set. The process must also exit the critical section before the timestamp expires, otherwise it must request the permission again.
  - Non token based algorithms are more robust and flexible than token based algorithms, as they do not depend on a single token. However, they also have some drawbacks. For example, they may generate more messages than token based algorithms, as each request may involve multiple processes. Also, they may suffer from deadlock or starvation, if some processes do not reply to the requests or if some requests are delayed or lost due to network failures.
  - Examples of non token based algorithms are:
    - Lamport's algorithm: This is a basic algorithm that uses logical clocks to generate timestamps. A process that wants to enter the critical section sends a REQUEST message with its timestamp to all the other processes in the system. The process waits for the REPLY messages from all the other processes. The process can enter the critical section only when it has received the REPLY



### Performance metric for distributed mutual exclusion algorithms

Distributed mutual exclusion algorithms are algorithms that ensure that only one process at a time can access a shared resource in a distributed system. The performance of these algorithms can be evaluated by the following metrics :

- **Message complexity**: It is the number of messages that are required per critical section (CS) execution by a process. It measures the communication overhead of the algorithm. A lower message complexity is desirable.
- **Synchronization delay**: It is the time elapsed between the departure of a process from the CS and the entry of the next process into the CS. It measures the degree of concurrency achieved by the algorithm. A lower synchronization delay is desirable.
- **Response time**: It is the time interval between the request of a process to enter the CS and the end of its CS execution. It measures the waiting time experienced by a process. A lower response time is desirable.
- **Throughput**: It is the number of CS executions per unit time in the system. It measures the efficiency of the algorithm. A higher throughput is desirable.

Different algorithms may have different trade-offs among these metrics. For example, a token-based algorithm may have low message complexity but high synchronization delay, while a non-token-based algorithm may have high message complexity but low synchronization delay. A quorum-based algorithm may have low response time but low throughput. Therefore, the choice of an algorithm depends on the application requirements and the system characteristics.



```markdown
## Unit 3 - Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set.
- A distributed deadlock is a deadlock that involves processes and resources located on different machines in a distributed system.
- Deadlock detection is a strategy to handle deadlocks by identifying and resolving them after they occur.
- Deadlock detection in distributed systems requires addressing two basic issues:
  - How to detect the existence of deadlocks in the system.
  - How to resolve the detected deadlocks by aborting some deadlocked processes.
- Deadlock detection in distributed systems can be done using three approaches:
  - Global wait-for graph (WFG) approach: A centralized or distributed algorithm that constructs a global graph of processes and resources from local graphs at each node and checks for cycles in the global graph.
  - Edge chasing or path pushing approach: A distributed algorithm that initiates probes along the edges of the local wait-for graphs and detects cycles when a probe returns to its originator.
  - Diffusing computation approach: A distributed algorithm that initiates a diffusing computation when a process is blocked and detects a deadlock when the diffusing computation terminates without granting the request.
- The advantages and disadvantages of each approach depend on factors such as the frequency of deadlock occurrence, the number of processes and resources, the communication and computation costs, and the degree of concurrency.
```



### System Model for Distributed Deadlock Detection

- A distributed system consists of a set of nodes that communicate by message passing.
- Each node has a set of resources that can be requested by processes running on the same or different nodes.
- A process may request a resource, use it, and release it. A process may hold multiple resources at the same time.
- A process may block if it requests a resource that is not available. A process may also block if it waits for a message from another process.
- A deadlock occurs when a set of processes are blocked and none of them can make progress. A deadlock can be caused by circular waiting for resources or messages among the processes.
- A system model for distributed deadlock detection defines the following components:
  - The representation of the process-resource and process-message interactions, such as wait-for graphs or dependency matrices.
  - The algorithm for collecting and analyzing the global state of the system, such as edge chasing or global wait-for graph construction.
  - The strategy for resolving the deadlock, such as aborting or preempting some processes or resources.



### Resource Vs Communication Deadlocks

- A deadlock is a condition where a process cannot proceed because it needs to obtain a resource held by another process, and it itself is holding a resource that the other process needs.
- There are two types of deadlocks in distributed systems: resource deadlocks and communication deadlocks.
- Resource deadlocks occur when processes access resources, such as data objects in database systems and buffers in store and forward communication networks. A process acquires a resource before accessing it and releasing it after using it. A resource deadlock happens when a process is waiting for a resource that is held by another process, and vice versa.
- Communication deadlocks occur when processes exchange messages, such as in message passing systems and distributed algorithms. A process sends a message to another process and waits for a reply before continuing. A communication deadlock happens when a process is waiting for a message that is never sent by another process, and vice versa.
- The main difference between resource deadlocks and communication deadlocks is that resource deadlocks involve contention for resources, while communication deadlocks involve loss or corruption of messages.
- Another difference is that resource deadlocks can be detected by analyzing the resource allocation graph, while communication deadlocks can be detected by analyzing the wait-for graph.
- A resource allocation graph is a directed graph where the nodes represent processes and resources, and the edges represent requests and assignments of resources. A cycle in the graph indicates a resource deadlock.
- A wait-for graph is a directed graph where the nodes represent processes, and the edges represent waiting for messages. A cycle in the graph indicates a communication deadlock.
- An example of a resource allocation graph and a wait-for graph is shown below:

```markdown
Resource allocation graph:

P1 -> R1 -> P2 -> R2 -> P1

Wait-for graph:

P1 -> P2 -> P3 -> P1
```

- In the resource allocation graph, P1 and P2 are deadlocked because they are holding R1 and R2 respectively, and requesting R2 and R1 respectively.
- In the wait-for graph, P1, P2, and P3 are deadlocked because they are waiting for messages from each other.



### Deadlock Prevention for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process. In a distributed system, deadlocks can occur across multiple nodes and resources, making them harder to detect and resolve.

Deadlock prevention is a technique that aims to avoid the occurrence of deadlocks by imposing some constraints on how processes can request and acquire resources. There are two main methods of deadlock prevention in distributed systems:

- Ordered request: This method assigns a unique level to each resource type and requires that a process requests resources in increasing order of levels. This prevents circular wait, one of the necessary conditions for deadlock. For example, if there are three resource types A, B, and C with levels 1, 2, and 3 respectively, a process can request A, then B, then C, but not C, then A, then B. 
- Collective request: This method requires that a process requests all the resources it needs at once, before starting its execution. This prevents hold and wait, another necessary condition for deadlock. For example, if a process needs resources A, B, and C, it must request them all together, rather than requesting A, then B, then C.  

Both methods have some drawbacks, such as reducing concurrency, increasing overhead, and requiring prior knowledge of resource requirements. Therefore, deadlock prevention may not be suitable for all distributed systems and applications.



### Avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- Deadlock avoidance is a technique that prevents the occurrence of deadlocks by ensuring that the system is always in a safe state.
- A safe state is a state where there exists a sequence of resource allocations that can satisfy the requests of all processes without causing a deadlock.
- In a distributed system, deadlock avoidance is impractical because of the following problems:
  - The system is dynamic and unpredictable, as processes may join or leave, and resources may be added or removed at any time.
  - The system is decentralized and lacks global information, as processes may not know the status of other processes or resources in the system.
  - The system is heterogeneous and diverse, as processes may have different characteristics, requirements, and preferences for resources.
- Therefore, deadlock detection is preferred over deadlock avoidance in distributed systems, as it allows more concurrency and flexibility in resource allocation.
- Deadlock detection is a technique that identifies the existence of deadlocks by examining the state of the system periodically or on demand.
- Deadlock detection in distributed systems can be classified into four categories, based on the type of information and communication used:
  - Path-pushing algorithms: These algorithms propagate the information about the wait-for relations along the paths of the resource allocation graph, and detect cycles in the graph.
  - Edge-chasing algorithms: These algorithms send probe messages along the edges of the resource allocation graph, and detect cycles in the graph.
  - Diffusion computation algorithms: These algorithms initiate a computation at each node of the resource allocation graph, and collect the results of the computation to detect cycles in the graph.
  - Global state detection algorithms: These algorithms collect the global state of the system using snapshots or timestamps, and analyze the state to detect cycles in the graph.



### Detection and Resolution of Distributed Deadlocks

- A distributed deadlock is a situation where a set of processes in a distributed system are waiting for each other to release resources, and none of them can proceed.
- A distributed deadlock can be detected by constructing a wait-for graph (WFG) that represents the dependencies among the processes and the resources in the system.
- A cycle in the WFG indicates the presence of a deadlock. A knot is a strongly connected component of the WFG that contains all the processes and resources involved in a deadlock.
- There are three main approaches to construct and search the WFG for cycles or knots: centralized, distributed, and hierarchical.
- Centralized approach: One designated node collects the information about the dependencies from all the other nodes and constructs the global WFG. It then searches the WFG for cycles or knots and initiates the resolution. This approach is simple and efficient, but it has a single point of failure and a high communication overhead.
- Distributed approach: Each node maintains a local WFG that reflects its dependencies with other nodes. The nodes exchange messages to construct and search the global WFG in a distributed manner. This approach is fault-tolerant and scalable, but it has a high complexity and a high message overhead.
- Hierarchical approach: The nodes are organized into a hierarchy of clusters, and each cluster has a coordinator that maintains a partial WFG for its cluster. The coordinators exchange messages to construct and search the global WFG in a hierarchical manner. This approach is a compromise between the centralized and distributed approaches, but it has a high latency and a high coordination overhead.
- The resolution of distributed deadlocks involves breaking the existing dependencies in the WFG by aborting or preempting some of the deadlocked processes and releasing their resources to the blocked processes. The resolution can be initiated by the same node or coordinator that detected the deadlock, or by a different node or coordinator that is informed of the deadlock.
- The resolution can be based on various criteria, such as the priority, the age, the progress, the cost, or the number of resources of the processes. The resolution can also be adaptive, meaning that it can adjust the criteria or the frequency of detection and resolution based on the system state and the workload.



### Centralized Deadlock Detection

- This is a technique used in distributed systems to handle deadlock detection.
- According to this approach, the system maintains one **Global wait-for graph** in a single chosen site, which is named as **deadlock-detection coordinator**.
- The coordinator collects information about the local wait-for graphs of all the sites and constructs the global wait-for graph.
- The coordinator periodically runs a deadlock detection algorithm on the global wait-for graph to identify any cycles.
- If a cycle is detected, the coordinator selects one or more processes to abort and sends a message to the corresponding sites to terminate them.
- The advantages of this approach are:
  - It is simple and easy to implement.
  - It reduces the communication overhead and the complexity of the algorithm.
- The disadvantages of this approach are:
  - It introduces a single point of failure and a performance bottleneck in the system.
  - It requires the coordinator to have a global view of the system, which may not be feasible or accurate in a dynamic and asynchronous environment.
  - It may detect false or phantom deadlocks due to the delay in propagating the information to the coordinator.



### Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set, and none of the processes can proceed or release the resources.
- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems.
- Deadlock detection in distributed systems entails addressing two basic issues: first, detection of existing deadlocks and second, resolution of detected deadlocks.
- Deadlock detection in distributed systems can be done using any of the following three approaches:
  - Centralized approach: A single node is designated as the deadlock detector and collects information about the resource allocation and requests from all the nodes in the system. The deadlock detector constructs a global wait-for graph (WFG) and checks for cycles in the graph. If a cycle is found, a deadlock is detected and resolved by aborting one or more processes in the cycle.
  - Distributed approach: Each node maintains a local wait-for graph and periodically sends it to a neighboring node. The neighboring node merges the received graph with its own graph and forwards it to another neighbor. This process continues until the graph returns to the original node. The original node then checks for cycles in the graph and initiates deadlock resolution if needed. This approach is also known as edge chasing.
  - Hierarchical approach: The nodes in the system are organized into a hierarchy of clusters. Each cluster has a coordinator node that collects information from the nodes in the cluster and constructs a local wait-for graph. The coordinator nodes then exchange information with each other and construct a global wait-for graph at the top level of the hierarchy. The top-level coordinator checks for cycles in the graph and initiates deadlock resolution if needed. This approach is a hybrid of the centralized and distributed approaches.



### Path Pushing Algorithms

- Path pushing algorithms detect distributed deadlocks by maintaining an explicit global wait-for graph (WFG) at each site of the distributed system .
- The global WFG is constructed by merging the local WFGs of each site, which represent the waiting relationships among the processes and resources at that site .
- Whenever a site performs a deadlock computation, it sends its local WFG to all its neighboring sites, which then update their global WFGs accordingly .
- A site can initiate a deadlock computation either periodically or when it detects a potential deadlock situation, such as a request timeout or a resource contention.
- A site can detect a deadlock by checking if there is a cycle in its global WFG that involves one of its local processes .
- If a deadlock is detected, the site can either initiate a resolution action, such as aborting or preempting a process, or report the deadlock to a coordinator site that is responsible for resolving deadlocks.
- The advantages of path pushing algorithms are that they can detect deadlocks quickly and accurately, and they do not require any additional messages for deadlock detection.
- The disadvantages of path pushing algorithms are that they require a lot of storage space and communication bandwidth to maintain and exchange the global WFGs, and they may incur false deadlocks due to the inconsistency of the global WFGs.



### Edge Chasing Algorithms for Distributed Deadlock Detection

- Edge chasing algorithms are a class of distributed deadlock detection algorithms that use special messages called probes to trace the dependency graph of processes and resources in a distributed system.
- A probe is a triplet (i, j, k) that denotes that the deadlock detection is initiated by process P_i and the message is being sent by the home site of process P_j to the home site of process P_k.
- The probe message follows the edges of the dependency graph from the waiting processes to the blocking processes until either a cycle is detected or all the edges are traversed.
- A cycle in the dependency graph indicates a deadlock, and the processes involved in the cycle are notified to resolve the deadlock.
- Edge chasing algorithms can be classified into two types: the AND model and the OR model, depending on whether a process waits for all or any of its requested resources to be granted.
- The most well-known edge chasing algorithm for the AND model is the Chandy-Misra-Haas algorithm, which works as follows:

  - Each process maintains a wait-for graph that contains the processes and resources that it depends on.
  - When a process P_i initiates a deadlock detection, it sends a probe (i, i, j) to the home site of each process P_j that it is waiting for.
  - When a process P_j receives a probe (i, k, j) from the home site of process P_k, it checks if it is involved in a deadlock with P_i. If yes, it sends a reply to P_i indicating the deadlock. If no, it forwards the probe (i, j, l) to the home site of each process P_l that it is waiting for.
  - When a process P_i receives a reply from P_j indicating a deadlock, it checks if the reply is consistent with its wait-for graph. If yes, it terminates itself or aborts one of its requests to resolve the deadlock. If no, it ignores the reply.

- Edge chasing algorithms for the OR model are more complex and require additional information to be maintained and exchanged by the processes. One example of such an algorithm is the Menasce-Muntz algorithm, which works as follows:

  - Each process maintains a wait-by graph that contains the processes and resources that depend on it.
  - When a process P_i initiates a deadlock detection, it sends a probe (i, i, j) to the home site of each process P_j that it is waiting for, along with its wait-by graph.
  - When a process P_j receives a probe (i, k, j) from the home site of process P_k, along with a wait-by graph G, it checks if it is involved in a deadlock with P_i. If yes, it sends a reply to P_i indicating the deadlock. If no, it updates its wait-by graph with G and forwards the probe (i, j, l) to the home site of each process P_l that it is waiting for, along with its updated wait-by graph.
  - When a process P_i receives a reply from P_j indicating a deadlock, it checks if the reply is consistent with its wait-by graph. If yes, it terminates itself or aborts one of its requests to resolve the deadlock. If no, it ignores the reply.

- Edge chasing algorithms have the advantages of being simple, efficient, and scalable, as they only require local information and minimal communication overhead. However, they also have some drawbacks, such as the possibility of false deadlock detection, the need for unique identifiers for each probe, and the lack of coordination among multiple initiators of deadlock detection.



## Unit 4 - Agreement Protocols

- Agreement protocols are a class of distributed algorithms that allow a set of processes to reach a common decision, despite the possibility of failures or malicious behavior.
- Agreement protocols are useful for implementing fault-tolerant services, such as distributed consensus, atomic broadcast, leader election, and distributed transactions.
- Agreement protocols can be classified into different types, depending on the assumptions they make about the system model, the communication model, the failure model, and the adversary model.
- Some common types of agreement protocols are:
  - Crash fault-tolerant (CFT) protocols: These protocols assume that processes may fail by crashing, but do not behave maliciously. They typically use reliable and synchronous communication channels, and require a majority of processes to be correct.
  - Byzantine fault-tolerant (BFT) protocols: These protocols assume that processes may fail by behaving arbitrarily, or even colluding with other faulty processes. They typically use authenticated and asynchronous communication channels, and require at least two-thirds of processes to be correct.
  - Randomized protocols: These protocols use randomization techniques, such as coin tossing or sampling, to break symmetry and achieve agreement with high probability. They can tolerate different types of failures and adversaries, and can work in asynchronous or partially synchronous settings.
  - Blockchain protocols: These protocols use cryptographic techniques, such as digital signatures and hash functions, to create a tamper-proof and append-only ledger of transactions. They can tolerate Byzantine faults and adversarial behavior, and can work in asynchronous or partially synchronous settings. They typically rely on incentives and game theory to ensure the security and liveness of the system.



### Introduction for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- Agreement protocols are a class of protocols that enable a set of processes to reach a common decision or consensus in a distributed system.
- Agreement protocols are essential for ensuring the consistency, reliability, and fault-tolerance of distributed systems, especially in the presence of failures or malicious behavior.
- Agreement protocols can be classified into different types based on the problem they solve, such as:
  - Consensus: All processes agree on a single value from a set of proposed values.
  - Atomic commit: All processes agree on whether to commit or abort a transaction.
  - Byzantine agreement: All processes agree on a single value from a set of proposed values, even if some processes are faulty or malicious.
  - Leader election: All processes agree on a single process to act as the leader or coordinator.
  - Mutual exclusion: All processes agree on which process can access a shared resource exclusively.
- Agreement protocols can also be classified based on the assumptions they make about the system, such as:
  - Synchronous vs asynchronous: Whether the system has bounded or unbounded delays in message delivery and process execution.
  - Crash vs Byzantine: Whether the system can tolerate only crash failures or also arbitrary failures.
  - Authenticated vs unauthenticated: Whether the system can verify the identity and integrity of the messages and processes.
  - Deterministic vs randomized: Whether the system can guarantee the termination and correctness of the protocol or only with some probability.
- Agreement protocols are often based on the following techniques or primitives:
  - Broadcast: A process sends a message to all other processes in the system.
  - Multicast: A process sends a message to a subset of processes in the system.
  - Quorum: A process collects responses from a majority or a subset of processes in the system.
  - Round: A process executes a sequence of steps or messages in a logical order.
  - Voting: A process chooses a value based on the preferences or opinions of other processes in the system.



### System models for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

A system model is a description of the properties and assumptions of a distributed system that are relevant for its design and analysis. System models can help us understand the behavior and limitations of a distributed system, and guide us in choosing appropriate algorithms and protocols for achieving certain goals.

There are different types of system models that capture different aspects of a distributed system, such as:

- **Architectural models**: These models describe the structure and organization of the components of a distributed system, and how they communicate and interact with each other. Examples of architectural models are client-server, peer-to-peer, publish-subscribe, and service-oriented architectures.
- **Interaction models**: These models describe the patterns and rules of communication and coordination among the components of a distributed system, and how they achieve consistency and agreement. Examples of interaction models are message passing, remote procedure call, remote method invocation, and distributed shared memory.
- **Fault models**: These models describe the types and causes of failures that can occur in a distributed system, and how they affect the system's behavior and performance. Examples of fault models are crash, omission, timing, response, arbitrary, and Byzantine faults.
- **Timing models**: These models describe the assumptions and properties of the clocks and timers in a distributed system, and how they affect the ordering and synchronization of events and actions. Examples of timing models are synchronous, asynchronous, and partially synchronous models.

Some system models are more realistic and practical than others, depending on the application domain and the environment of the distributed system. For example, a synchronous system model assumes that there are known bounds on the message delays and the clock drifts, which may not be true in a large-scale or dynamic network. Similarly, a crash-recovery fault model assumes that a failed component can recover its state and resume its operation, which may not be possible in a catastrophic scenario.

One of the main challenges in distributed systems is to achieve agreement among the components on some common value or decision, despite the presence of faults and uncertainties. This problem is known as the **consensus problem**, and it is fundamental for many distributed applications, such as distributed databases, distributed transactions, distributed ledgers, and distributed coordination.

There are different algorithms and protocols for solving the consensus problem, depending on the system model and the assumptions made. Some of the most popular and widely used consensus algorithms are:

- **Paxos**: Paxos is a family of consensus algorithms that operate in a partially synchronous system model with crash-recovery faults. Paxos guarantees that the components will eventually agree on a single value, as long as a majority of them are alive and can communicate. Paxos is based on a leader election mechanism, where a leader proposes a value and tries to get the acceptance of a quorum of followers. If the leader fails or is suspected to fail, a new leader is elected and the process is repeated until consensus is reached.
- **Raft**: Raft is a consensus algorithm that is similar to Paxos, but aims to be simpler and easier to understand. Raft also operates in a partially synchronous system model with crash-recovery faults, and guarantees that the components will eventually agree on a single value, as long as a majority of them are alive and can communicate. Raft is also based on a leader election mechanism, where a leader proposes a value and tries to get the acceptance of a quorum of followers. However, Raft uses a different approach for leader election and log replication, which makes it more intuitive and modular than Paxos.
- **Zab**: Zab is a consensus algorithm that is used by Apache ZooKeeper, a distributed coordination service. Zab operates in a partially synchronous system model with crash-recovery faults, and guarantees that the components will eventually agree on a single value, as long as a majority of them are alive and can communicate. Zab is also based on a leader election mechanism, where a leader proposes a value and tries to get the acceptance of a quorum of followers. However, Zab uses a different approach for leader election and log replication, which makes it more efficient and robust than Paxos and Raft.
- **PBFT**: PBFT is a consensus algorithm that operates in an asynchronous system model with Byzantine faults. PBFT guarantees that the components will agree on a single value, as long as less than a third of them are faulty and can behave arbitrarily. PBFT is based on a three-phase protocol, where a leader proposes a value and tries to get the acceptance of a supermajority of followers. If the leader is faulty or is suspected to be faulty



# Classification of Agreement Problem in Distributed Systems

An agreement problem in a distributed system is a problem where a set of processes need to agree on a common value or decision, despite the possibility of failures or malicious behavior of some processes. Agreement problems are fundamental for achieving fault tolerance and consistency in distributed systems.

There are different types of agreement problems, depending on the assumptions and requirements of the system. Some of the well-known agreement problems are:

- **Byzantine agreement problem**: A single value, which is to be agreed on, is initialized by an arbitrary process and all non-faulty processes have to agree on that value. The processes may have different initial values and may behave arbitrarily, including sending conflicting or misleading messages. The goal is to reach agreement despite the presence of such Byzantine faults .
- **Consensus problem**: A set of processes, each with an initial value, have to agree on a common value that is equal to one of the initial values. The processes may fail by crashing, but they do not behave maliciously. The goal is to reach agreement despite the presence of crash faults .
- **Interactive consistency problem**: A set of processes, each with an initial value, have to agree on a vector of values, such that the i-th element of the vector is equal to the initial value of the i-th process, if that process is non-faulty, and can be any value otherwise. The processes may behave arbitrarily, as in the Byzantine agreement problem. The goal is to reach agreement despite the presence of Byzantine faults .

These problems are related to each other and have different levels of difficulty and impossibility results, depending on the system model and the number of faulty processes. For example, the Byzantine agreement problem is harder than the consensus problem, and the consensus problem is impossible to solve in an asynchronous system with one or more crash faults . The interactive consistency problem is equivalent to the Byzantine agreement problem, if the number of faulty processes is less than one third of the total number of processes .

These problems have various applications in distributed systems, such as atomic broadcast, atomic commit, group membership, state machine replication, leader election, and distributed cryptography .



### Byzantine agreement problem

The Byzantine agreement problem is a fundamental challenge in fault-tolerant distributed computing. It requires a set of parties in a distributed system to agree on a common value, even if some of the parties are faulty or malicious. The problem is also known as the interactive consistency problem, the source congruency problem, or the Byzantine generals problem.

The problem was first defined by Lamport in the context of the NASA-sponsored SIFT project. He used the analogy of several divisions of the Byzantine army camped outside an enemy city, each division commanded by its own general. The generals can communicate with one another only by messenger. After observing the enemy, they must decide upon a common plan of action, such as attack or retreat. However, some of the generals may be traitors, who try to prevent the loyal generals from reaching agreement. The problem is to find a protocol that allows the loyal generals to agree on the same plan, while tolerating a certain number of traitors.

The Byzantine agreement problem has several variations, depending on the assumptions made about the system. Some of the parameters that affect the problem are:

- The number of parties (n) and the number of faulty parties (f).
- The type of faults (crash, omission, arbitrary, etc.).
- The type of communication (synchronous, asynchronous, authenticated, etc.).
- The type of value (binary, multivalued, etc.).
- The type of agreement (consensus, broadcast, etc.).

The Byzantine agreement problem is important for many applications that require coordination and consistency among distributed parties, such as distributed databases, distributed ledgers, distributed consensus, fault-tolerant systems, etc. Solving the Byzantine agreement problem is often challenging, and requires trade-offs between performance, security, and availability.

Some of the solutions to the Byzantine agreement problem are:

- Lamport's oral messages algorithm, which requires n > 3f and synchronous communication.
- Lamport's signed messages algorithm, which requires n > 2f and authenticated communication.
- Pease-Shostak-Lamport algorithm, which requires n > 3f and authenticated communication.
- Dolev-Strong algorithm, which requires n > 3f and asynchronous communication.
- Practical Byzantine Fault Tolerance (PBFT) algorithm, which requires n > 3f and partially synchronous communication.



### Consensus problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- The consensus problem is the problem of getting a set of nodes in a distributed system to agree on something - it might be a value, a course of action or a decision.
- Achieving consensus allows a distributed system to act as a single entity, with every individual node aware of and in agreement with the actions of the whole of the network.
- Consensus is a general agreement on a decision made by the majority of those involved.
- Consensus is needed in a distributed system to ensure overall system reliability on top of unreliable system components.
- Consensus is also needed to coordinate distributed transactions, replicate data, elect leaders, and implement fault tolerance mechanisms.
- Consensus is hard to achieve in a distributed system due to the possibility of failures, such as node crashes, network partitions, message losses, and malicious attacks .
- There are many ways in which processes in a distributed system can reach a consensus, but there is usually a trade-off between security and performance.
- The more we want our algorithm to be secure against ways in which failure can happen, the less performant it tends to become.
- Some of the common consensus algorithms in distributed systems are:
  - Two-phase commit (2PC): A simple and efficient protocol that requires a coordinator node to initiate a commit request to all other nodes, and then decide to commit or abort based on their responses.
  - Three-phase commit (3PC): An extension of 2PC that adds a pre-commit phase to avoid blocking in case of a coordinator failure.
  - Paxos: A family of protocols that use a quorum-based approach to elect a leader and propose values to be agreed upon by the majority of nodes.
  - Raft: A simplified version of Paxos that divides the consensus problem into three subproblems: leader election, log replication, and safety.
  - Byzantine fault tolerance (BFT): A class of protocols that can tolerate arbitrary failures, including malicious or faulty nodes, by requiring a supermajority of nodes (usually 2/3 or more) to agree on a value.



### Interactive consistency problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- Interactive consistency is the problem in which n distinct nodes, each having its own private value, where up to t may be Byzantine, run an algorithm that allows all non-faulty nodes to infer the values of each other node  .
- Byzantine nodes are nodes that can behave arbitrarily, such as sending conflicting or incorrect messages, or remaining silent .
- Interactive consistency is also known as Byzantine generals problem, which is a metaphor for the situation where a group of generals must agree on a common plan of action, while some of them may be traitors .
- Interactive consistency is a fundamental problem in distributed systems, especially in critical applications that rely on the combination of the opinions of multiple peers to provide a service .
- Interactive consistency is closely related to distributed consensus, which is the problem of reaching agreement on a single value among a set of nodes in the presence of faults .
- Interactive consistency is harder than distributed consensus, because it requires agreement on n values instead of one, and it requires each node to learn the values of all other nodes, not just its own .
- Interactive consistency is impossible to achieve in a purely asynchronous system, where there is no bound on message delays or node speeds, if t >= n/3, where t is the number of Byzantine nodes and n is the total number of nodes .
- Interactive consistency can be achieved in a synchronous system, where there is a known bound on message delays and node speeds, if t < n/3, using algorithms based on message authentication, digital signatures, or public-key cryptography .
- Interactive consistency can also be achieved in a partially synchronous system, where there is a bound on message delays and node speeds that is initially unknown, but eventually becomes known, if t < n/3, using algorithms based on broadcast and randomized Byzantine consensus.
- Interactive consistency can be achieved in a practical, mostly-asynchronous system, where there is a single synchronization barrier that separates the asynchronous and synchronous phases, if t < n/3, using algorithms that combine the advantages of the previous approaches.



### Solution to Byzantine Agreement problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- The Byzantine Agreement problem is a fundamental problem in fault tolerant distributed computing that requires a set of parties in a distributed environment to agree on a value even if some of the parties are corrupted.
- The problem is also known as the Byzantine Generals problem, which is a metaphor for a scenario where several divisions of the Byzantine army are camped outside an enemy city, each division commanded by its own general. The generals can communicate with one another only by messenger. After observing the enemy, they must decide upon a common plan of action.
- The problem is challenging because some of the generals may be traitors who try to prevent the loyal generals from reaching an agreement or make them adopt a bad plan. The traitors may also collude with each other or send conflicting messages to different generals.
- The solution to the problem relies on an algorithm that can guarantee that: 1) All loyal generals decide upon the same plan of action, and 2) A small number of traitors cannot cause the loyal generals to adopt a bad plan.
- One of the most well-known solutions to the problem is the Oral Message algorithm proposed by Lamport et al. in 1982. The algorithm assumes that the messages are authenticated and reliable, and that the generals have a common knowledge of the total number of generals and the maximum number of traitors.
- The algorithm works as follows: 
  - Each general sends his initial value to every other general.
  - For each round, each general acts as a commander and sends an order (the value he received from the source general) to every other general, who act as lieutenants. The lieutenants then send the order they received to every other lieutenant, except the commander. This process is repeated for m rounds, where m is the maximum number of traitors.
  - After m rounds, each lieutenant constructs a matrix of values he received from each commander and each lieutenant. He then applies a majority function to each row of the matrix to obtain a vector of values. He then applies the majority function to the vector to obtain the final value.
- The algorithm can tolerate up to m traitors, where m < n/3, where n is the total number of generals. The algorithm requires O(n^2) messages and O(m) rounds of communication.
- The algorithm can be extended to handle the case where the messages are not authenticated, by using digital signatures or message authentication codes. However, this introduces additional complexity and overhead.
- The algorithm can also be extended to handle the case where the messages are not reliable, by using timeouts, acknowledgments, and retransmissions. However, this may introduce additional delays and inconsistencies.
- The Byzantine Agreement problem is relevant for many applications in distributed systems, such as consensus protocols, fault-tolerant replication, distributed databases, distributed ledgers, and blockchain  .



### Application of Agreement Problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- Agreement among the processes in a distributed system is a fundamental requirement for a wide range of applications.
- Many forms of coordination require the processes to exchange information to negotiate with one another and eventually reach a common understanding or agreement, before taking application-specific actions.
- Agreement problems can be classified into different versions, such as consensus, atomic commitment, atomic broadcast, and group membership.
- Consensus is the problem of getting all the processes to agree on a single value, chosen from the set of proposed values.
- Atomic commitment is the problem of getting all the processes to agree on whether to commit or abort a transaction.
- Atomic broadcast is the problem of getting all the processes to deliver the same set of messages in the same order.
- Group membership is the problem of getting all the processes to agree on the current composition of the system.
- Agreement problems are challenging to solve in distributed systems, especially in the presence of failures, asynchrony, and uncertainty.
- The FLP impossibility result shows that there is no deterministic algorithm that can solve consensus in an asynchronous system with even one faulty process.
- To overcome the FLP impossibility, various approaches have been proposed, such as using randomization, weakening the agreement condition, or strengthening the system model.
- Randomized algorithms can solve consensus with high probability in asynchronous systems, by using coin-flipping techniques.
- Weaker forms of agreement, such as approximate agreement or lattice agreement, can be solved in asynchronous systems with deterministic algorithms .
- Approximate agreement is the problem of getting all the processes to agree on a value within a predefined range.
- Lattice agreement is the problem of getting all the processes to agree on a value that is a lower bound of the proposed values, according to a partial order.
- Stronger system models, such as partially synchronous or failure detector-based, can also solve consensus with deterministic algorithms.
- Partially synchronous systems assume that there is a bound on the message delay or the relative process speed, but this bound is unknown or may change over time.
- Failure detector-based systems assume that there is a module that provides information about the failure status of the processes, but this information may be inaccurate or incomplete.
- Agreement problems have many applications in distributed systems, such as implementing atomic snapshot objects, building replicated state machines, coordinating distributed transactions, and maintaining consistent views of the system  .



### Atomic Commit in Distributed Database System

- An atomic commit is an operation that applies a set of distinct changes as a single operation. If the changes are applied, then the atomic commit is said to have succeeded. If the changes are not applied, then the atomic commit is said to have failed or aborted.
- In distributed database systems, the primary need for commit protocols is to maintain the atomicity of distributed transactions. A distributed transaction is a transaction that accesses data stored in multiple sites of a distributed system .
- Atomic commitment issue is of prime importance in the distributed system and the issue becomes more necessary to deal with if some of the sites participating in the execution of the transaction commitment fail .
- An atomic commit protocol (ACP) is a protocol that coordinates the commit or abort of a distributed transaction among the participating sites. An ACP guarantees, in spite of possible failures, that either all the sites commit the transaction, or all the sites abort the transaction .
- There are two main types of ACPs: blocking and non-blocking. Blocking ACPs require some sites to wait for the recovery of other failed sites before they can decide the outcome of the transaction. Non-blocking ACPs allow some sites to decide the outcome of the transaction without waiting for the recovery of other failed sites .
- Some examples of blocking ACPs are two-phase commit (2PC), three-phase commit (3PC), and presumed abort (PA). Some examples of non-blocking ACPs are presumed commit (PC), non-blocking two-phase commit (NB-2PC), and non-blocking three-phase commit (NB-3PC) .
- FLAC is a practical failure-aware atomic commit protocol for distributed transactions that leverages the failure information of the participating sites to optimize the commit latency and abort rate. FLAC uses a two-phase transaction processing framework that consists of a prepare phase and a commit phase. FLAC adapts the commit phase according to the failure information of the sites.



## Unit 5 - Distributed Resource Management

- Distributed resource management is the process of allocating and managing resources in a distributed system, such as processors, memory, disk space, network bandwidth, etc.
- The main objectives of distributed resource management are to improve the performance, reliability, availability, scalability, and efficiency of the system, while satisfying the user requirements and constraints.
- The main challenges of distributed resource management are to deal with the heterogeneity, dynamism, uncertainty, and complexity of the system, as well as the conflicting and changing user demands and preferences.
- Some of the key concepts and techniques for distributed resource management are:

  - **Resource discovery**: the process of finding and identifying the available resources in the system, such as their location, capacity, status, and properties.
  - **Resource description**: the process of representing and communicating the characteristics and capabilities of the resources, such as their type, name, value, quality, and constraints.
  - **Resource allocation**: the process of assigning and distributing the resources to the tasks or users that request them, such as by using optimization, negotiation, auction, or game-theoretic methods.
  - **Resource scheduling**: the process of ordering and timing the execution of the tasks or users that have been allocated the resources, such as by using priority, deadline, fairness, or load-balancing policies.
  - **Resource monitoring**: the process of observing and measuring the state and performance of the resources and the tasks or users that use them, such as by using sensors, probes, or feedback mechanisms.
  - **Resource adaptation**: the process of adjusting and modifying the resource allocation and scheduling decisions in response to the changes and events in the system or the user behavior, such as by using reconfiguration, migration, replication, or load-shedding techniques.



### Issues in distributed file systems

A distributed file system (DFS) is a system that allows multiple clients to access and manipulate files stored on one or more servers over a network. A DFS provides the abstraction of a single, shared namespace for files, regardless of their physical location or the network topology. A DFS can improve the performance, reliability, scalability, and security of file access and management.

However, designing and implementing a DFS also involves many challenges and issues, such as:

- **Naming and transparency**: How to assign unique and meaningful names to files and directories in a DFS? How to support different naming schemes and conventions? How to provide location transparency, replication transparency, and migration transparency to the users and applications?
- **Consistency and caching**: How to ensure that the files and directories in a DFS are consistent across different servers and clients? How to handle concurrent updates and conflicts? How to exploit caching techniques to improve the performance and availability of file access? How to maintain cache coherence and consistency?
- **Replication and fault tolerance**: How to replicate files and directories in a DFS to improve the reliability and availability of file access? How to balance the trade-offs between replication and consistency? How to handle failures and recoveries of servers and clients? How to provide fault tolerance and durability guarantees?
- **Security and access control**: How to protect the files and directories in a DFS from unauthorized access and modification? How to enforce different access policies and permissions for different users and groups? How to provide authentication, authorization, encryption, and auditing mechanisms?
- **Performance and scalability**: How to optimize the performance and efficiency of file access and management in a DFS? How to reduce the network overhead and latency? How to balance the load and distribute the workload among different servers and clients? How to scale the DFS to support large numbers of files, servers, and clients?
- **Interoperability and compatibility**: How to ensure that the DFS can interoperate and communicate with other file systems and protocols? How to support different file formats and standards? How to provide backward and forward compatibility for the DFS?

These are some of the main issues that need to be addressed in the design and use of a distributed file system. Different DFS solutions may adopt different approaches and techniques to deal with these issues, depending on their requirements and objectives.



### Mechanism for building distributed file systems

A distributed file system (DFS) is a file system that is distributed on multiple file servers or locations. It allows programs to access or store isolated files as they do with the local ones, allowing programmers to access files from any network or computer.

The mechanism for building distributed file systems involves the following aspects:

- Use of file models: The DFS uses different conceptual models of a file. The following are the two basic criteria for file modeling, which include file structure and modifiability. The files can be unstructured or structured based on the applications used in file systems. The files can also be immutable or mutable depending on whether they can be modified or not.
- Use of file accessing models: A distributed file system may use one of the following models to service a client’s file request: upload/download, remote access, or remote service. The upload/download model involves transferring the entire file between the client and the server. The remote access model involves sending file operations to the server and receiving the results. The remote service model involves executing the file operations on the server and returning the output to the client.
- Use of file replication: File replication is the primary mechanism for improving file availability in a distributed systems environment. A replicated file is a file that has multiple copies with each copy located on a separate file server. The challenges of file replication include maintaining consistency, coherence, and fault tolerance among the replicas .
- Use of file caching: File caching is the mechanism of storing frequently accessed files or parts of files in the local memory of the client or the server. File caching can improve the performance and reduce the network traffic of a distributed file system. The challenges of file caching include maintaining cache consistency, coherence, and fault tolerance.
- Use of file naming: File naming is the mechanism of assigning unique and meaningful names to the files in a distributed file system. File naming can be based on flat, hierarchical, or attribute-based schemes. File naming can also involve the use of namespaces, which are logical structures that group shared folders located on different servers. Namespaces can provide a virtual view of shared folders, where a single path leads to files located on multiple servers .



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of Design issues in Distributed Shared Memory for the Unit 5 - Distributed Resource Management in the subject of DISTRIBUTED SYSTEM.

### Design issues in Distributed Shared Memory

- Distributed Shared Memory (DSM) is a mechanism that allows multiple processes on different nodes to share a common logical address space and access data transparently across the network .
- DSM aims to combine the advantages of shared memory and distributed memory models, such as ease of programming, scalability, and fault tolerance .
- DSM faces several design issues that affect its performance, consistency, and usability. Some of the major issues are    :

  - **Granularity**: This refers to the size of the unit of sharing and transfer in the DSM system. It can be as small as a byte or as large as a page. The choice of granularity affects the communication overhead, the memory overhead, the false sharing, and the coherence protocol complexity .
  - **Structure**: This refers to the organization of the shared data in the DSM system. It can be flat, segmented, or object-based. The choice of structure affects the naming, allocation, and mapping of the shared data, as well as the flexibility and portability of the DSM system .
  - **Coherence semantics**: This refers to the rules that define the consistency and ordering of the shared data accesses in the DSM system. It can be strict, relaxed, or weak. The choice of coherence semantics affects the correctness, performance, and programmability of the DSM system .
  - **Coherence protocol**: This refers to the mechanism that implements the coherence semantics in the DSM system. It can be based on hardware, software, or a combination of both. The choice of coherence protocol affects the scalability, efficiency, and complexity of the DSM system .
  - **Scalability**: This refers to the ability of the DSM system to handle increasing numbers of nodes, processors, and shared data without degrading the performance or increasing the cost. It depends on the design choices of granularity, structure, coherence semantics, and coherence protocol, as well as the network topology and bandwidth .
  - **Heterogeneity**: This refers to the diversity of the hardware and software components in the DSM system. It can be in terms of processor architecture, operating system, network interface, or programming language. The choice of heterogeneity affects the portability, interoperability, and compatibility of the DSM system .

- These design issues are interrelated and involve trade-offs and compromises. There is no single optimal solution for all DSM systems, but rather different solutions for different application domains and requirements  .



# Algorithm for Implementation of Distributed Shared Memory

Distributed Shared Memory (DSM) is a technique that allows multiple processes on different nodes of a distributed system to share a common virtual address space and access the same data objects. DSM can simplify the programming of distributed applications by providing a uniform view of memory and hiding the details of data distribution and communication.

There are different algorithms for implementing DSM, each with its own advantages and disadvantages. Some of the basic algorithms are:

- **Central Server Algorithm**: In this algorithm, a central server maintains all the shared data and services read and write requests from other nodes. The server can use a page-based or an object-based approach to manage the shared data. The advantage of this algorithm is that it is simple and ensures data consistency. The disadvantage is that it introduces a single point of failure and a performance bottleneck.

- **Migration Algorithm**: In this algorithm, the shared data is initially stored at the central server, but it can migrate to other nodes upon request. The node that holds the data becomes the owner of that data and can service read requests locally. Write requests are forwarded to the server, which updates the data and invalidates the copies at other nodes. The advantage of this algorithm is that it reduces the network traffic and improves the locality of data access. The disadvantage is that it may cause frequent data migration and inconsistency.

- **Replication Algorithm**: In this algorithm, the shared data is replicated at multiple nodes, and each node can service read requests locally. Write requests are propagated to all the nodes that have a copy of the data, and a consistency protocol is used to ensure that all the copies are updated atomically. The advantage of this algorithm is that it improves the availability and fault-tolerance of the data. The disadvantage is that it increases the network traffic and the complexity of the consistency protocol.

- **Coherence Algorithm**: In this algorithm, the shared data is divided into fixed-size pages or variable-size objects, and each page or object has a coherence state that indicates its validity and ownership. A coherence protocol is used to maintain the consistency of the data across the nodes. The protocol can be based on a central manager, a distributed directory, or a multicast group. The advantage of this algorithm is that it can achieve a balance between performance and consistency. The disadvantage is that it requires additional hardware or software support for the coherence protocol.



## Unit 6 - Failure Recovery in Distributed Systems

- Failure recovery is the process of restoring a distributed system to a consistent and correct state after a failure occurs.
- Failure recovery is essential for fault tolerance, which is the ability of a system to continue functioning despite faults or errors.
- There are different types of failures that can affect a distributed system, such as:
  - Node failures: when a site or a process in the system stops working or crashes.
  - Communication failures: when a message or a connection between sites or processes is lost or delayed.
  - Media failures: when a secondary storage device, such as a disk or a tape, fails or gets corrupted.
  - Byzantine failures: when a site or a process behaves maliciously or arbitrarily, sending incorrect or conflicting messages to other sites or processes.
- There are different techniques for failure recovery in distributed systems, such as:
  - Checkpointing: when a site or a process periodically saves its state to a stable storage, which can resist major disasters. In case of a failure, the site or process can resume from the last saved checkpoint.
  - Logging: when a site or a process records its actions and messages to a stable storage, which can be used to replay or undo the actions and messages in case of a failure.
  - Replication: when a site or a process maintains multiple copies of its state or data on different sites or processes, which can be used to replace or update the faulty copy in case of a failure.
  - Voting: when a site or a process consults with other sites or processes to reach a consensus or a majority on the correct state or data, which can be used to detect or correct a failure.
  - Recovery blocks: when a site or a process executes a sequence of alternative modules or actions, each with an acceptance test, until one of them succeeds or passes the test, which can be used to handle a failure.



### Concepts in Backward and Forward Recovery

- Backward recovery and forward recovery are two techniques to deal with failures in distributed systems.
- A failure in a distributed system can affect one or more processes, transactions, or messages, and can cause inconsistency, deadlock, or data loss.
- The goal of recovery is to restore the system to a consistent and correct state after a failure, and to ensure the atomicity, consistency, isolation, and durability (ACID) properties of transactions.

#### Backward Recovery

- Backward recovery is a technique that moves the system from its current state back to a previously correct state by undoing the effects of the failure.
- Backward recovery requires the system to periodically record its state in checkpoints, and to restore the state from the checkpoints when a failure occurs.
- Backward recovery has three steps:
  - Detection: The system detects the occurrence of a failure and identifies the affected processes or transactions.
  - Rollback: The system rolls back the affected processes or transactions to their last consistent checkpoints, and discards any changes made after the checkpoints.
  - Restart: The system restarts the rolled back processes or transactions from their checkpoints, and resumes the normal execution.

- Backward recovery has some advantages and disadvantages:
  - Advantages:
    - It does not require the knowledge of the nature or cause of the failure, and can handle any type of failure.
    - It does not require the system to perform any error correction or compensation actions during the normal execution, and can focus on the performance and functionality of the system.
  - Disadvantages:
    - It may cause the loss of some useful work done by the system after the checkpoints, and may require the system to repeat some computations or communications.
    - It may cause the inconsistency or violation of the ACID properties of transactions, if the system does not coordinate the checkpoints and rollbacks among the distributed processes or transactions.

#### Forward Recovery

- Forward recovery is a technique that moves the system from its current state to a new correct state by correcting the effects of the failure.
- Forward recovery requires the system to detect and diagnose the failure, and to perform some error correction or compensation actions to fix the failure and resume the normal execution.
- Forward recovery has three steps:
  - Detection: The system detects the occurrence of a failure and identifies the affected processes or transactions.
  - Diagnosis: The system diagnoses the nature and cause of the failure, and determines the appropriate error correction or compensation actions to fix the failure.
  - Correction: The system performs the error correction or compensation actions, and resumes the normal execution.

- Forward recovery has some advantages and disadvantages:
  - Advantages:
    - It does not cause the loss of any useful work done by the system, and does not require the system to repeat any computations or communications.
    - It does not cause the inconsistency or violation of the ACID properties of transactions, if the system performs the error correction or compensation actions correctly and consistently.
  - Disadvantages:
    - It requires the knowledge of the nature and cause of the failure, and may not be able to handle some types of failures that are unpredictable or irreversible.
    - It requires the system to perform some error correction or compensation actions during the normal execution, and may affect the performance and functionality of the system.



### Recovery in Concurrent Systems

Recovery in concurrent systems is the process of restoring the system to a consistent state after a failure, while preserving the effects of the transactions that were committed before the failure. Recovery in concurrent systems is more complex than in sequential systems, because the system may have multiple transactions executing in parallel, and their operations may be interleaved in the log. Therefore, the recovery system needs to consider the following aspects:

- Interaction with concurrency control: The recovery system depends on the concurrency control system that is used to ensure the serializability and isolation of transactions. For example, if the system uses locking, the recovery system needs to release the locks held by the failed transactions and grant the locks requested by the surviving transactions. If the system uses timestamps, the recovery system needs to assign new timestamps to the restarted transactions and abort any transactions that have conflicting timestamps.
- Transaction rollback: The recovery system needs to undo the effects of the failed transactions and restore the database to a consistent state. This can be done by using the log to backtrack the operations of the failed transactions and apply the inverse operations to the database. For example, if the log records an operation that writes a value x to a data item A, the recovery system can undo this operation by writing the old value of A to the data item.
- Checkpoints: The recovery system can use checkpoints to reduce the amount of work needed to recover from a failure. A checkpoint is a point in the log where the system records the state of the database and the transactions. The recovery system can use the checkpoint as a starting point for recovery, and only consider the log entries that are after the checkpoint. Checkpoints can be taken periodically or when the system is idle.
- Restart recovery: The recovery system needs to restart the transactions that were affected by the failure and ensure that they are executed correctly. This can be done by using the log to identify the transactions that need to be restarted and their status. For example, if the log records that a transaction T was committed before the failure, the recovery system can redo the operations of T to ensure that its effects are reflected in the database. If the log records that a transaction T was aborted before the failure, the recovery system can discard the operations of T and release any resources held by T. If the log records that a transaction T was active before the failure, the recovery system can either abort T and restart it from the beginning, or continue T from the point of failure.



### Obtaining consistent Checkpoints for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Failure recovery in distributed systems is the process of restoring the system to a consistent and correct state after a failure occurs.
- A failure can be defined as a deviation of the system from its expected behavior or specification.
- Failures can be classified into different types, such as crash failures, omission failures, timing failures, response failures, Byzantine failures, etc.
- A checkpoint is a snapshot of the system state at a certain point in time, which can be used to resume the execution after a failure.
- Obtaining consistent checkpoints is a challenge in distributed systems, because the system consists of multiple processes that may communicate and synchronize with each other.
- A checkpoint is consistent if it reflects a global state that could have occurred during a correct execution of the system.
- There are different techniques for obtaining consistent checkpoints, such as coordinated checkpointing, uncoordinated checkpointing, and communication-induced checkpointing.
- Coordinated checkpointing requires all processes to agree on when to take a checkpoint, and to coordinate their communication activities during the checkpointing process.
- Uncoordinated checkpointing allows each process to take a checkpoint independently, without any coordination with other processes.
- Communication-induced checkpointing uses the communication messages between processes to trigger checkpoints, and to ensure that the checkpoints are consistent.
- Each technique has its own advantages and disadvantages, such as performance overhead, storage space, recovery time, etc.
- The choice of the checkpointing technique depends on the characteristics of the system, such as the failure rate, the communication pattern, the checkpoint frequency, etc.



### Recovery in Distributed Database Systems

- Recovery in distributed database systems is the process of restoring the database to a consistent state after a failure or an error .
- Recovery in distributed database systems is more complicated than in centralized database systems because failures can occur at multiple sites or communication links.
- Recovery in distributed database systems aims to maintain the atomicity and durability of distributed transactions, which are transactions that span multiple sites.
- Recovery in distributed database systems can be classified into two types: local recovery and global recovery .
- Local recovery is the recovery of a single site from a failure or an error. Local recovery techniques include transaction undo, transaction redo, shadow paging, and checkpointing .
- Global recovery is the recovery of the entire distributed database system from a failure or an error that affects multiple sites or communication links. Global recovery techniques include two-phase commit, three-phase commit, presumed abort, presumed commit, and non-blocking commit .
- Global recovery techniques rely on the exchange of messages and votes among the participating sites to reach a consensus on the outcome of a distributed transaction.
- Global recovery techniques also use logs, timestamps, and locks to record and coordinate the actions of distributed transactions .
- Global recovery techniques have different trade-offs in terms of performance, reliability, availability, and complexity.



## Unit 7 - Fault Tolerance

- Fault tolerance is the ability of a system to continue functioning correctly in the presence of failures.
- Fault tolerance can be achieved by using techniques such as redundancy, replication, recovery, reconfiguration, and masking.
- Fault tolerance can be classified into two types: hardware fault tolerance and software fault tolerance.
- Hardware fault tolerance is the ability of a system to tolerate failures of physical components, such as processors, memory, disks, or network links.
- Hardware fault tolerance can be achieved by using techniques such as RAID, mirroring, hot swapping, checkpointing, and voting.
- Software fault tolerance is the ability of a system to tolerate failures of software components, such as processes, threads, or messages.
- Software fault tolerance can be achieved by using techniques such as exception handling, retrying, timeouts, transactions, and consensus.
- Fault tolerance can be measured by metrics such as reliability, availability, and maintainability.
- Reliability is the probability that a system will perform its intended function without failure for a given period of time.
- Availability is the fraction of time that a system is operational and ready to provide service.
- Maintainability is the ease with which a system can be repaired or restored after a failure.



### Issues in Fault Tolerance for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Fault tolerance is the ability of a system to continue functioning correctly in the presence of failures.
- Fault tolerance is important for distributed systems because they consist of multiple components that may be subject to failures, such as hardware, software, network, or human errors.
- Fault tolerance can be achieved by using various techniques, such as redundancy, replication, checkpointing, recovery, consensus, and fault detection.
- Some of the issues and challenges in fault tolerance for distributed systems are:
  - How to classify and model different types of faults and failures.
  - How to design and implement fault-tolerant algorithms and protocols that can cope with various failure scenarios.
  - How to measure and evaluate the performance and reliability of fault-tolerant systems.
  - How to balance the trade-offs between fault tolerance and other system properties, such as efficiency, scalability, consistency, and security.
  - How to adapt to dynamic and heterogeneous environments, where failures may be unpredictable and diverse.



### Commit Protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Commit protocols are algorithms that ensure the atomicity of distributed transactions, i.e., all the sites involved in a transaction either commit or abort it unanimously, even in the presence of failures.
- Commit protocols are necessary to maintain the consistency and reliability of distributed systems, as they prevent partial execution or loss of data due to network or site failures.
- There are different types of commit protocols, such as one-phase, two-phase, and three-phase commit protocols, each with its own advantages and disadvantages.
- One-phase commit protocol: A simple and efficient protocol that involves a coordinator who communicates with the participating sites and instructs them to either commit or abort the transaction. However, this protocol does not guarantee atomicity in case of failures, as the coordinator may not receive the acknowledgments from all the sites or some sites may not receive the final decision from the coordinator.
- Two-phase commit protocol: A widely accepted standard protocol that ensures atomicity by dividing the commit process into two phases: voting and decision. In the voting phase, the coordinator asks the sites to vote on whether they are ready to commit or not, and collects their responses. In the decision phase, the coordinator decides to commit the transaction if all the sites voted yes, or abort it otherwise, and informs the sites of the final decision. However, this protocol has a blocking problem, as it requires the coordinator and all the sites to be operational until the end of the transaction, and any failure may cause the protocol to stall indefinitely.
- Three-phase commit protocol: An extension of the two-phase commit protocol that introduces an extra phase called pre-commit to overcome the blocking problem. In the pre-commit phase, the coordinator broadcasts a "prepare to commit" message to the sites that voted yes in the voting phase, and waits for their acknowledgments. In the commit/abort phase, the coordinator decides to commit the transaction if all the sites responded ok, or abort it otherwise, and informs the sites of the final decision. This protocol is non-blocking, as it allows the sites to reach a consistent decision even if the coordinator fails after the pre-commit phase. However, this protocol incurs more communication overhead and latency, as it involves an extra round of message exchange.



### Voting protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Voting protocols are a type of consensus protocols that allow a set of distributed nodes to agree on a common value or decision, despite the presence of faults or attacks.
- Voting protocols are useful for achieving fault tolerance in distributed systems, such as replicated databases, distributed ledgers, or peer-to-peer networks.
- Voting protocols can be classified into two categories: exact voting and inexact voting.
  - Exact voting requires that all nodes agree on the same value or decision, and that the value or decision is correct according to some predefined criteria. Examples of exact voting protocols are two-phase commit, three-phase commit, and Paxos.
  - Inexact voting allows for some degree of disagreement or error among the nodes, as long as the value or decision is acceptable according to some predefined criteria. Examples of inexact voting protocols are majority voting, weighted voting, and probabilistic voting.
- Voting protocols can also be classified into two categories based on the security properties they provide: secure voting and non-secure voting.
  - Secure voting ensures that the value or decision is not influenced by malicious nodes or external attackers, and that the voting process is confidential and verifiable. Examples of secure voting protocols are Byzantine agreement, threshold cryptography, and zero-knowledge proofs.
  - Non-secure voting does not provide any security guarantees, and assumes that the nodes are honest and the network is reliable. Examples of non-secure voting protocols are simple majority voting, quorum-based voting, and Lamport's algorithm.



### Dynamic voting protocols

- Dynamic voting protocols are techniques for consistency and recovery control of replicated files in distributed systems  .
- The purpose of a replicated file is to improve the availability of a logical file in the presence of site failures and network partitions  .
- A dynamic voting protocol assigns a number of votes to each copy of a replicated file, and allows a group of copies to access the file only if they have a majority of votes   .
- The number of votes assigned to each copy can change dynamically depending on the system state, such as the number of copies, the network topology, the failure pattern, etc    .
- Dynamic voting protocols can improve the performance and reliability of distributed systems by reducing the communication overhead, increasing the concurrency, and tolerating more failures    .
- Dynamic voting protocols can be classified into two categories: topological and non-topological.
  - Topological dynamic voting protocols assign votes based on the network structure and the location of copies, such as the distance, the connectivity, the partitionability, etc.
  - Non-topological dynamic voting protocols assign votes based on other criteria, such as the access frequency, the update rate, the copy age, etc.
- Examples of dynamic voting protocols are:
  - The dynamic weighted voting scheme proposed by Davcev  , which assigns votes to copies according to their distance from the center of the network and the number of copies in their partition.
  - The dynamic vote reassignment protocols proposed by Gifford, which reassign votes to the surviving copies when a node or a link fails, and restore the original votes when the failure is repaired.
  - The quorum-based voting protocols proposed by Gifford, which require a transaction to obtain a quorum of votes from a subset of copies before performing a restricted operation, such as reading or writing the file.
  - The efficient dynamic voting algorithms proposed by Agrawal and Abbadi, which assign votes to copies based on their topological properties, such as the non-partitionability, the connectivity, and the diameter of the group containing the copy.



# Unit 8 - Transactions and Concurrency Control

- A **transaction** is a logical unit of work that consists of a sequence of operations on a database, such as reading, writing, inserting, deleting, or modifying data.
- A transaction has four main properties, known as **ACID**:
  - **Atomicity**: A transaction is either executed completely or not at all. If any operation in the transaction fails, the whole transaction is aborted and the database is restored to its previous state.
  - **Consistency**: A transaction preserves the integrity and validity of the database. It ensures that the database satisfies all the constraints and rules before and after the transaction.
  - **Isolation**: A transaction is executed independently of other concurrent transactions. It does not interfere with or see the intermediate results of other transactions.
  - **Durability**: A transaction's effects are permanent and persistent in the database. They are not lost even in the event of a system failure or power outage.
- **Concurrency control** is the management of simultaneously executing transactions in a shared database. It ensures that correct results for concurrent operations are generated while getting those results as quickly as possible.
- Concurrency control is important because it helps to maintain the **serializability** and **recoverability** of transactions. 
  - **Serializability**: A schedule of transactions is serializable if it is equivalent to some serial schedule, where transactions are executed one after another without any overlap. Serial schedules are guaranteed to be correct and consistent, but they are not efficient or realistic in a multi-user system.
  - **Recoverability**: A schedule of transactions is recoverable if it does not allow any transaction to commit before all the transactions whose changes it read have committed. Recoverable schedules prevent the problem of **cascading aborts**, where the failure of one transaction causes the failure of other dependent transactions.
- Concurrency control techniques implement some protocols which can be broadly classified into two categories:
  - **Lock-based protocol**: Those database systems that are prepared with the concept of lock-based protocols employ a mechanism where any transaction cannot read or write data until it gains a suitable lock on it. A lock is a variable associated with a data item that describes the status of the item with respect to possible operations that can be applied to it. There are two types of locks: **shared lock** and **exclusive lock**. A shared lock allows a transaction to read a data item, but not to write or modify it. An exclusive lock allows a transaction to both read and write a data item, but no other transaction can access it. Lock-based protocols ensure serializability, but they may cause problems such as **deadlocks**, **starvation**, or **concurrency**.
  - **Timestamp-based protocol**: Those database systems that are prepared with the concept of timestamp-based protocols employ a mechanism where each transaction is issued a unique timestamp when it enters the system. The timestamp reflects the transaction's start time and is used to order the transactions. A transaction can read or write a data item only if its timestamp is older than the timestamp of the last transaction that accessed the item. Timestamp-based protocols ensure serializability and avoid deadlocks, but they may cause problems such as **aborts**, **retries**, or **overhead**.



### Transactions

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the operations in a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction does not interfere with other concurrent transactions.
- Durability means that the effects of a committed transaction are permanent and survive failures.

### Concurrency Control

- Concurrency control is the process of managing simultaneous access to shared data in a database by multiple transactions.
- Concurrency control ensures that the transactions are executed in a way that preserves the ACID properties and the correctness of the database.
- Concurrency control can be implemented using various techniques, such as locking, timestamping, validation, and multiversioning.

### Distributed Systems

- A distributed system is a system that consists of multiple independent components that communicate and coordinate with each other over a network.
- A distributed system can provide advantages such as scalability, availability, fault tolerance, and performance.
- A distributed system can also pose challenges such as heterogeneity, partial failures, concurrency, and consistency.

### Distributed Transactions

- A distributed transaction is a transaction that spans multiple components of a distributed system.
- A distributed transaction consists of a set of subtransactions, each of which is executed by one component (such as a data server).
- A distributed transaction coordinator is responsible for coordinating the execution and commitment of the subtransactions across the components.
- A distributed transaction has the same ACID properties as a local transaction, but it is more complex and costly to implement.

### Distributed Concurrency Control

- Distributed concurrency control is the concurrency control of a distributed system.
- Distributed concurrency control provides a mechanism to synchronize distributed transactions in such a way that the ACID properties are not violated by their interleaved execution.
- Distributed concurrency control makes sure that all subtransactions of a set of distributed transactions are serialized identically in all components involved.
- Distributed concurrency control can be implemented using various techniques, such as distributed locking, distributed timestamping, distributed validation, and distributed multiversioning.



### Nested transactions for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A transaction is a sequence of operations that satisfies the ACID properties (Atomicity, Consistency, Isolation, Durability).
- A nested transaction is a transaction that is composed of subtransactions, each of which may have its own begin and end points, and may be executed concurrently or sequentially.
- A nested transaction that accesses objects handled by different servers is referred to as a distributed transaction.
- Nested transactions can be used to improve the performance, reliability, and modularity of distributed systems, by allowing partial commits, compensating actions, and independent recovery of subtransactions.
- Nested transactions can be classified into two types: **flat** and **nested**.
  - A flat transaction has a single initiating point (Begin) and a single end point (Commit or abort). They are usually very simple and are generally used for short activities rather than larger ones.
  - A nested transaction has a hierarchical structure, where each subtransaction can be further divided into smaller subtransactions. They are more complex and are generally used for long and complex activities that involve multiple servers.
- Nested transactions can be implemented using different protocols, such as **two-phase commit (2PC)**, **presumed abort (PA)**, **presumed commit (PC)**, and **sagas**.
  - 2PC is a protocol that ensures atomicity of a distributed transaction by coordinating the commit or abort decision among all the servers involved. It consists of two phases: **prepare** and **commit**. In the prepare phase, the coordinator asks each server to vote on whether to commit or abort the transaction. In the commit phase, the coordinator decides based on the votes and informs each server to either commit or abort the transaction.
  - PA is a protocol that optimizes 2PC by reducing the number of messages exchanged. It assumes that most transactions will abort, and therefore does not require the coordinator to log the prepare messages. Instead, the coordinator logs only the commit messages, and if it fails, it presumes that the transaction has aborted.
  - PC is a protocol that optimizes 2PC by reducing the number of messages exchanged. It assumes that most transactions will commit, and therefore does not require the coordinator to log the commit messages. Instead, the coordinator logs only the abort messages, and if it fails, it presumes that the transaction has committed.
  - Sagas are a protocol that allows partial commits of a distributed transaction by using compensating actions. A saga is a sequence of subtransactions that can be executed in any order, and each subtransaction has a corresponding compensating action that can undo its effects. If a subtransaction fails, the saga aborts by executing the compensating actions of the previous subtransactions in reverse order.



### Locks for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A lock is a mechanism that allows only one of the innumerable nodes or processes to access and modify a resource or data that is being shared commonly to prevent execution of same task twice and also maintain data integrity.
- Locks are designed to enforce a mutual exclusion concurrency control policy, which means that only one process can hold a lock on a resource at a time, and any other process that wants to access the same resource has to wait until the lock is released.
- Locks can be classified into different types based on the following criteria  :
  - The granularity of the resource: locks can be applied to a whole database, a table, a page, a record, or a field.
  - The mode of the lock: locks can be either shared or exclusive. A shared lock allows multiple processes to read the same resource, but not to modify it. An exclusive lock allows only one process to read or modify the resource, and blocks any other process from accessing it.
  - The duration of the lock: locks can be either long-lived or short-lived. A long-lived lock is held for the entire duration of a transaction, and is released only when the transaction commits or aborts. A short-lived lock is held only for the duration of a single operation, and is released as soon as the operation finishes.
  - The implementation of the lock: locks can be either centralized or distributed. A centralized lock is managed by a single entity, such as a lock manager or a coordinator, that keeps track of all the locks and grants or denies lock requests from the processes. A distributed lock is managed by multiple entities, such as the processes themselves or a consensus system, that communicate with each other to coordinate the locking and unlocking of the resources.
- Locks can be used to implement different concurrency control protocols, such as two-phase locking (2PL), timestamp ordering (TO), or optimistic concurrency control (OCC) . These protocols define the rules for acquiring and releasing locks, and for resolving conflicts and deadlocks among the processes.
- Locks can also be used to implement other distributed system primitives, such as leader election, consensus, coordination, synchronization, or distributed transactions  . These primitives require the processes to agree on a common state or a common action, and to execute it atomically and consistently.
- Locks are a very useful but also a very challenging primitive in distributed systems, as they introduce additional complexity, overhead, and potential failures. Some of the challenges and trade-offs of using locks are :
  - Availability: locks can reduce the availability of the system, as they can cause blocking, starvation, or livelock. Blocking occurs when a process has to wait for a lock to be released by another process. Starvation occurs when a process is repeatedly denied a lock request by other processes with higher priority. Livelock occurs when two or more processes keep requesting and releasing locks without making any progress.
  - Consistency: locks can ensure the consistency of the system, as they can prevent concurrent updates or reads from conflicting or violating the integrity constraints. However, locks can also compromise the consistency of the system, as they can cause inconsistency, stale reads, or lost updates. Inconsistency occurs when a process reads a resource that has been modified by another process without acquiring a lock. Stale reads occur when a process reads a resource that has been modified by another process after the read operation. Lost updates occur when a process overwrites a resource that has been modified by another process without acquiring a lock.
  - Performance: locks can improve the performance of the system, as they can reduce the number of conflicts, aborts, or rollbacks. However, locks can also degrade the performance of the system, as they can increase the latency, overhead, or contention. Latency is the time it takes for a process to acquire or release a lock. Overhead is the cost of managing, communicating, or coordinating the locks. Contention is the degree of competition among the processes for the same resource.



### Optimistic Concurrency Control

- Optimistic concurrency control (OCC) is a concurrency control method applied to transactional systems such as relational database management systems and software transactional memory.
- OCC assumes that multiple transactions can frequently complete without interfering with each other, and does not use locking or timestamping techniques to prevent conflicts .
- Instead, a transaction is executed without restrictions until it is committed, and then it is validated to check if any conflicts occurred with other transactions.
- If a conflict is detected, the transaction is aborted and restarted, otherwise it is committed.
- OCC has three phases: read, validation and write.
  - In the read phase, the transaction reads data from the database and performs computations, but does not write anything to the database.
  - In the validation phase, the transaction checks if any of the data it read has been modified by another transaction that committed after it started.
  - In the write phase, the transaction writes its updates to the database, if the validation phase was successful.
- OCC is suitable for distributed systems, where locking or timestamping may incur high communication overhead or limit scalability.
- OCC can improve performance and concurrency in distributed systems, especially when conflicts are rare or when transactions are short-lived .
- However, OCC may also cause high abort rates and wasted work, if conflicts are frequent or if transactions are long-lived .
- OCC can be implemented using various techniques, such as version numbers, timestamps, validation queries, or certification  .
- OCC requires a mechanism to detect and resolve conflicts, such as serializability, snapshot isolation, or causal consistency  .



### Timestamp ordering for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- Timestamp ordering is a technique for ensuring serializability of transactions in a distributed system.
- A timestamp is a unique identifier assigned to each transaction or event that occurs in the system, based on a logical or physical clock.
- Timestamp ordering defines a partial or total order of transactions or events, according to their timestamps, such that causally related transactions or events have consistent ordering.
- Timestamp ordering can be used to prevent or detect conflicts among concurrent transactions, such as read-write, write-write, or write-read conflicts.
- Timestamp ordering can be implemented using different algorithms, such as Lamport timestamps, vector clocks, or synchronized clocks.
- Lamport timestamps are logical clocks that assign a monotonically increasing number to each event in the system, based on the local clock of the node where the event occurs and the messages received from other nodes.
- Vector clocks are logical clocks that assign a vector of numbers to each event in the system, where each element of the vector represents the local clock of a node in the system, and the vector is updated whenever an event occurs or a message is sent or received.
- Synchronized clocks are physical clocks that are adjusted periodically to maintain a common notion of time among the nodes in the system, using algorithms such as NTP or Cristian's algorithm.



### Comparison of methods for concurrency control for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

Concurrency control is the process of managing the concurrent access and modification of shared data in a distributed system, such that the ACID properties of transactions are preserved. There are various methods for concurrency control, each with its own advantages and disadvantages. Some of the common methods are:

- **Two-phase locking protocol (2PL)**: This method uses locks to grant or deny access to data items. A transaction must acquire a lock on a data item before reading or writing it, and release the lock after finishing its operation. There are two phases in this protocol: the growing phase, where the transaction acquires locks and does not release any; and the shrinking phase, where the transaction releases locks and does not acquire any. This protocol ensures serializability, which means that the concurrent execution of transactions is equivalent to some serial execution. However, it may cause deadlock, where two or more transactions are waiting for each other to release locks, and thus cannot proceed. It may also cause starvation, where some transactions are repeatedly blocked by others and never get a chance to execute. Moreover, it may reduce concurrency, as transactions have to wait for locks to be released by others.

- **Timestamp ordering protocol (TO)**: This method assigns a unique timestamp to each transaction, which reflects its start time or priority. A transaction can read or write a data item only if its timestamp is compatible with the read and write timestamps of the data item, which record the latest transactions that have read or written the data item. If the timestamp is not compatible, the transaction is aborted and restarted with a new timestamp. This protocol avoids deadlock, as there is no waiting for locks. It also ensures serializability, as the transactions are effectively executed in the order of their timestamps. However, it may cause cascading aborts, where one aborted transaction causes other transactions that have read its data to abort as well. It may also cause starvation, as some transactions may be repeatedly aborted and restarted due to timestamp conflicts. Moreover, it may reduce concurrency, as transactions have to abort and restart if they encounter newer data.

- **Multi-version concurrency control (MVCC)**: This method maintains multiple versions of each data item, each with its own read and write timestamps. A transaction can read the latest version of a data item that is compatible with its timestamp, and write a new version of a data item with its timestamp. This protocol avoids deadlock, as there is no waiting for locks. It also avoids cascading aborts, as transactions can read older versions of data that are not affected by aborted transactions. It may also increase concurrency, as transactions can read and write different versions of data without conflicts. However, it may cause inconsistency, as transactions may read stale or uncommitted data. It may also cause overhead, as multiple versions of data have to be stored and managed.

- **Validation concurrency control (VCC)**: This method divides the execution of a transaction into three phases: the read phase, where the transaction reads data and performs computations; the validation phase, where the transaction checks for conflicts with other transactions; and the write phase, where the transaction writes its results to the database. A transaction can commit only if it passes the validation phase, which ensures that its read set and write set do not intersect with the write sets of other committed transactions. This protocol avoids deadlock, as there is no waiting for locks. It also avoids cascading aborts, as transactions do not write until they are committed. It may also increase concurrency, as transactions can read data without conflicts. However, it may cause aborts, as transactions may fail the validation phase due to conflicts with other transactions. It may also cause overhead, as transactions have to store and check their read and write sets.



## Unit 9 - Distributed Transactions

- A distributed transaction is a type of transaction that involves two or more network hosts, usually providing transactional resources, such as databases, message queues, file systems, etc.   
- A distributed transaction is coordinated by a transaction manager, which is responsible for creating and managing a global transaction that encompasses all the operations against the transactional resources.   
- A distributed transaction requires the following properties to ensure data consistency and reliability: atomicity, consistency, isolation, and durability (ACID). 
- Atomicity means that either all the operations in a distributed transaction are executed successfully, or none of them are. If any operation fails, the transaction manager should roll back the changes made by the previous operations. 
- Consistency means that a distributed transaction should preserve the integrity constraints and business rules of the data. The data should be in a valid state before and after the transaction. 
- Isolation means that a distributed transaction should not interfere with other concurrent transactions. The data accessed or modified by one transaction should not be visible to other transactions until the transaction is committed. 
- Durability means that once a distributed transaction is committed, the changes made by the transaction should be permanent and survive any failures. The transaction manager should ensure that the changes are written to the transactional resources and can be recovered if needed. 
- A distributed transaction can be implemented using different protocols, such as two-phase commit (2PC), three-phase commit (3PC), or consensus algorithms (such as Paxos or Raft). These protocols aim to achieve agreement among the transactional resources and the transaction manager on the outcome of the transaction (commit or abort).  
- A distributed transaction faces various challenges, such as network failures, resource failures, concurrency conflicts, deadlock detection, and performance overhead. These challenges require careful design and implementation of the distributed transaction system.



### Flat and Nested Distributed Transactions

A distributed transaction is a transaction that accesses data or resources from multiple servers or databases. A distributed transaction must ensure the ACID properties (atomicity, consistency, isolation, and durability) across all the involved servers or databases.

There are two ways to structure a distributed transaction: flat or nested.

#### Flat Transactions

A flat transaction has a single begin point and a single end point, where it either commits or aborts. A flat transaction is simple and suitable for short activities, but it may cause problems for long or complex activities. For example, a flat transaction may hold locks on data for a long time, blocking other transactions from accessing the same data. A flat transaction may also fail due to network or server failures, requiring the whole transaction to be restarted.

#### Nested Transactions

A nested transaction is a transaction that consists of subtransactions, each with its own begin and end points. A nested transaction can commit or abort its subtransactions independently, allowing more flexibility and concurrency. A nested transaction can also recover from failures by aborting only the affected subtransactions, rather than the whole transaction.

A nested transaction has a hierarchical structure, where the top-level transaction is called the root transaction, and the subtransactions are called the branches. The branches can be either flat or nested themselves, creating a tree-like structure. The root transaction coordinates the commit or abort of all the branches, ensuring the atomicity of the whole transaction.

A nested transaction can be either closed or open. A closed nested transaction is isolated from its parent transaction, meaning that the changes made by the subtransaction are not visible to the parent until the subtransaction commits. An open nested transaction is not isolated from its parent transaction, meaning that the changes made by the subtransaction are visible to the parent immediately. Open nested transactions can improve performance and concurrency, but they may also introduce inconsistencies or conflicts.



### Atomic Commit Protocols for Distributed Transactions

- A distributed transaction is a transaction that involves multiple servers or nodes in a distributed system.
- An atomic commit protocol is a protocol that ensures that a distributed transaction is either committed or rolled back in its entirety, even if the system fails or some of the nodes fail or crash.
- Ensuring atomic commit is important for maintaining the consistency and integrity of the data in a distributed system.
- There are different types of atomic commit protocols, such as two-phase commit (2PC), three-phase commit (3PC), parallel commit, and failure-aware commit.
- Two-phase commit (2PC) is the most widely used atomic commit protocol. It consists of two phases: a prepare phase and a commit phase. In the prepare phase, the coordinator node sends a prepare message to all the participant nodes, asking them to vote on whether they are ready to commit or not. In the commit phase, the coordinator node collects the votes from the participant nodes and decides whether to commit or abort the transaction. If all the votes are yes, the coordinator node sends a commit message to all the participant nodes, instructing them to commit the transaction. If any of the votes are no, or if the coordinator node does not receive all the votes within a timeout, the coordinator node sends an abort message to all the participant nodes, instructing them to roll back the transaction.
- Three-phase commit (3PC) is an extension of 2PC that adds a pre-commit phase between the prepare phase and the commit phase. In the pre-commit phase, the coordinator node sends a pre-commit message to all the participant nodes that voted yes in the prepare phase, asking them to acknowledge that they are ready to commit. In the commit phase, the coordinator node sends a commit message to all the participant nodes that acknowledged the pre-commit message, instructing them to commit the transaction. If any of the participant nodes do not acknowledge the pre-commit message, or if the coordinator node does not receive all the acknowledgements within a timeout, the coordinator node sends an abort message to all the participant nodes, instructing them to roll back the transaction. The pre-commit phase is added to avoid blocking in case of a coordinator failure, as the participant nodes can decide whether to commit or abort based on a timeout.
- Parallel commit is a new atomic commit protocol that reduces the latency of transactions down to only a single round-trip of distributed consensus. It consists of two phases: a staging phase and a commit phase. In the staging phase, the transaction is written to a staging area on each participant node, and a distributed consensus protocol (such as Raft or Paxos) is used to agree on the transaction timestamp. In the commit phase, the transaction is moved from the staging area to the committed area on each participant node, and the transaction timestamp is written to a global commit record. The transaction is considered committed when the global commit record is updated, and the transaction is considered rolled back when the staging area is cleared. Parallel commit avoids the need for a coordinator node and a prepare phase, and leverages the existing distributed consensus protocol for transaction ordering.
- Failure-aware commit (FLAC) is a practical atomic commit protocol that adapts to the failure patterns of the participant nodes. It consists of two phases: a prepare phase and a commit phase. In the prepare phase, the coordinator node sends a prepare message to all the participant nodes, asking them to vote on whether they are ready to commit or not. In the commit phase, the coordinator node collects the votes from the participant nodes and decides whether to commit or abort the transaction. If all the votes are yes, the coordinator node sends a commit message to all the participant nodes, instructing them to commit the transaction. If any of the votes are no, or if the coordinator node does not receive all the votes within a timeout, the coordinator node sends an abort message to all the participant nodes, instructing them to roll back the transaction. The difference between FLAC and 2PC is that FLAC uses a failure-aware voting scheme, in which the participant nodes can vote yes, no, or unknown. A yes vote means that the participant node is ready to commit and has not failed. A no vote means that the participant node is not ready to commit or has failed. An unknown vote means that the participant node is ready to commit but has failed. The coordinator node can use the unknown votes to infer the failure patterns of the participant nodes and optimize the commit decision accordingly. FLAC can achieve lower latency and higher throughput than 2PC by reducing the number of aborts and retries.



### Concurrency control in distributed transactions

- Concurrency control is the process of managing the concurrent execution of transactions in a distributed database system, such that the ACID properties are preserved.
- Concurrency control aims to ensure the correctness and consistency of the database state, while allowing a high degree of parallelism and performance.
- Concurrency control can be classified into two main categories: pessimistic and optimistic.
  - Pessimistic concurrency control assumes that conflicts are likely to occur and uses locking mechanisms to prevent them. Locking-based protocols require transactions to acquire locks on the data items they access, and release them when they commit or abort. Locks can be shared or exclusive, depending on the operation (read or write) performed by the transaction. Locking-based protocols can be centralized, decentralized, or hierarchical, depending on the location and structure of the lock manager .
  - Optimistic concurrency control assumes that conflicts are rare and allows transactions to execute without locking. Optimistic protocols use timestamps or validation rules to detect conflicts at commit time, and abort the conflicting transactions. Timestamp-based protocols assign a unique timestamp to each transaction, and use it to order the transactions and determine their precedence. Validation-based protocols divide the transaction execution into three phases: read, validation, and write, and check for conflicts during the validation phase .
- Concurrency control in distributed transactions faces additional challenges, such as network delays, communication failures, partial failures, and distributed deadlock detection and resolution .
- Concurrency control in distributed transactions can use either a centralized or a distributed approach, depending on the degree of coordination and communication among the data servers.
  - Centralized approach uses a single coordinator to manage the concurrency control of all transactions. The coordinator is responsible for assigning timestamps, granting locks, detecting conflicts, and resolving deadlocks. The centralized approach simplifies the design and implementation of concurrency control, but introduces a single point of failure and a performance bottleneck.
  - Distributed approach uses multiple coordinators, each responsible for a subset of transactions or data items. The coordinators communicate with each other to coordinate the concurrency control of the transactions. The distributed approach avoids the drawbacks of the centralized approach, but increases the complexity and overhead of concurrency control.
- Concurrency control in distributed transactions can also use hybrid approaches, such as 2PC*, which is an optimized protocol based on the traditional two-phase commit (2PC) protocol. 2PC* can extract more concurrent processing capabilities under high-intensity competitive workloads than previous approaches for a multi-microservice environment.



### Distributed Deadlocks

- A distributed deadlock is a situation where a set of processes in a distributed system are waiting for each other to release resources or messages, and none of them can proceed .
- Distributed deadlocks are similar to deadlocks in centralized systems, but they are harder to detect, avoid, and prevent, because there is no single authority that can oversee resource allocation and monitor the state of the system.
- There are different types of distributed deadlocks, depending on the nature of the resources or messages involved. Some examples are:
  - Communication deadlocks: occur when processes are waiting for messages from each other that will never arrive.
  - Distributed mutual exclusion deadlocks: occur when processes are competing for exclusive access to shared resources in a distributed system.
  - Distributed transaction deadlocks: occur when transactions are waiting for locks on data items that are held by other transactions in a distributed database system.
- There are different approaches to handle distributed deadlocks, such as :
  - Prevention: use a protocol that ensures that deadlocks cannot occur, such as ordering the resources or messages, or using timeouts or timestamps.
  - Avoidance: use a protocol that avoids unsafe resource allocation or message passing, such as the banker's algorithm or the wound-wait scheme.
  - Detection: use a technique that detects the existence of deadlocks in the system, and then resolve them by aborting or restarting some processes or transactions.
  - Ignorance: ignore the possibility of deadlocks, and assume that they are rare or negligible, and rely on the user or the application to handle them.
- The techniques of deadlock detection in distributed systems require the following properties:
  - Progress: the technique should be able to detect all the deadlocks in the system.
  - Safety: the technique should not detect false or phantom deadlocks, which are not actually present in the system.
- There are two main categories of deadlock detection techniques in distributed systems :
  - Centralized: use a single node or a coordinator to collect information from all the nodes in the system, and construct a global wait-for graph (WFG) to identify cycles that indicate deadlocks.
  - Distributed: use multiple nodes or agents to cooperate and exchange information with each other, and use a distributed algorithm to identify cycles that indicate deadlocks, such as edge chasing or probe propagation.



### Transaction Recovery for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

- Transaction recovery is the process of restoring the consistency and integrity of a distributed database after a failure or an abort of a transaction.
- Transaction recovery is essential for ensuring the ACID properties of transactions in a distributed system, where failures and concurrency issues are more likely to occur.
- Transaction recovery involves two main steps: detection and resolution.
- Detection is the process of identifying the transactions that are affected by a failure or an abort, and their status (committed, aborted, or in-doubt).
- Resolution is the process of applying the appropriate actions to the affected transactions, such as undoing, redoing, or committing them, based on their status and the recovery protocol used.
- There are different types of failures that can affect transactions in a distributed system, such as site failures, network failures, media failures, or system failures.
- There are different types of recovery protocols that can be used to handle failures in a distributed system, such as two-phase commit (2PC), three-phase commit (3PC), presumed abort (PA), presumed commit (PC), or shadow versions.
- Each recovery protocol has its own advantages and disadvantages in terms of performance, reliability, and complexity.
- The choice of a recovery protocol depends on the characteristics of the distributed system, such as the degree of replication, the frequency of failures, the availability of backup copies, and the communication cost.



## Unit 10 - Replication

- Replication is a biological process of duplicating or producing an exact copy, such as a polynucleotide strand (DNA) .
- DNA replication is one of the most vital biological processes in all living things. It is a molecular process taking place in dividing cells by which the DNA creates a copy of itself .
- Replication also refers to the duplication of a laboratory or experimental procedure, which is essential for research statistics .
- Biological replicates are parallel measurements of biologically distinct samples that capture random biological variation, which can be a subject of study or a source of noise itself .
- Biological replicates are important because they address how widely your experimental results can be generalized .

### DNA replication

- DNA replication is the process by which a double-stranded DNA molecule is copied to produce two identical DNA molecules .
- DNA replication occurs in three main stages: initiation, elongation, and termination .
- Initiation is the stage where the DNA helix is unwound and the replication machinery is assembled at the origin of replication .
- Elongation is the stage where the DNA polymerase synthesizes new complementary strands of DNA using the original strands as templates .
- Termination is the stage where the replication forks meet and the newly synthesized DNA molecules are separated and sealed .
- DNA replication is semi-conservative, meaning that each new DNA molecule consists of one old and one new strand .
- DNA replication is also bidirectional, meaning that it proceeds in both directions from the origin of replication .
- DNA replication is regulated by various enzymes and proteins, such as helicase, single-strand binding proteins, topoisomerase, primase, DNA polymerase, ligase, etc. .

### Replication in experiments

- Replication in experiments is the duplication of a laboratory or experimental procedure, which is essential for research statistics .
- Replication in experiments can be classified into two types: technical replicates and biological replicates .
- Technical replicates are repeated measurements of the same sample under identical conditions, which capture random technical variation or measurement error .
- Technical replicates are useful for assessing the precision and reliability of the experimental method .
- Biological replicates are parallel measurements of biologically distinct samples that capture random biological variation, which can be a subject of study or a source of noise itself .
- Biological replicates are important because they address how widely your experimental results can be generalized .
- Biological replicates can be further divided into two subtypes: independent replicates and pseudo-replicates .
- Independent replicates are measurements of samples that are obtained from independent sources, such as different individuals, populations, or treatments .
- Independent replicates are essential for testing the statistical significance and reproducibility of the experimental findings .
- Pseudo-replicates are measurements of samples that are obtained from the same source, such as the same individual, population, or treatment .
- Pseudo-replicates are useful for increasing the precision and accuracy of the experimental estimates, but they do not provide information about the biological variation or the statistical significance .



### System model and group communication for replication in distributed systems

- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by passing messages .
- Replication is a technique to improve the availability, performance, and fault tolerance of a distributed system by creating and maintaining multiple copies of the same data or service .
- A system model is a set of assumptions and properties that describe the behavior and characteristics of a distributed system, such as the communication model, the failure model, the timing model, and the security model .
- Group communication is a form of communication between multiple processes in a distributed system that share some common interest or goal, such as replicating data or coordinating actions  .
- Group communication can be classified into two types: broadcast communication and multicast communication .
  - Broadcast communication is when a source process sends a message to all the processes in the system, regardless of their group membership or interest .
  - Multicast communication is when a source process sends a message to a subset of processes in the system that belong to a specific group or have a specific interest  .
- Group communication can also be characterized by the reliability and ordering guarantees it provides, such as reliable, atomic, causal, or total order multicast  .
  - Reliable multicast is when a message sent by a source process is delivered to all the processes in the group, or none of them, in case of a failure .
  - Atomic multicast is when a message sent by a source process is delivered to all the processes in the group atomically, meaning that either all or none of them receive the message, and they all agree on the delivery .
  - Causal multicast is when a message sent by a source process is delivered to all the processes in the group in a way that respects the causal order of events, meaning that if a message m1 causally precedes a message m2, then any process that receives m2 must have received m1 before .
  - Total order multicast is when a message sent by a source process is delivered to all the processes in the group in the same order, meaning that any two processes that receive the same set of messages agree on the order of delivery .
- Group communication is useful for replication in distributed systems because it allows the processes to synchronize their state and actions, to disseminate updates and queries efficiently, and to handle failures and inconsistencies gracefully  .



### Fault-Tolerant Services for the Notes of the Unit 10 - Replication in the Subject of Distributed System

- Fault-tolerance is the ability of a system to continue providing correct service despite the occurrence of failures, such as server crashes, network partitions, or malicious attacks.
- Replication is a technique for achieving fault-tolerance by creating and maintaining multiple copies of the same service or data across different servers or locations.
- Replication can improve the availability, performance, and reliability of a distributed system, but also introduces challenges such as consistency, coordination, and recovery.
- There are two main classes of replication techniques: primary-backup replication and active replication.
  - Primary-backup replication: One server acts as the primary and handles all the requests from the clients, while the others act as backups and receive updates from the primary. The primary is responsible for ensuring the consistency and durability of the replicas. If the primary fails, a new primary is elected from the backups.
  - Active replication: All servers act as replicas and execute the same requests from the clients in the same order. The replicas use a consensus protocol to agree on the order of requests and ensure consistency. If a replica fails, the others can continue to provide service.
- The correctness criterion for replicated services is linearizability, which means that every operation appears to take effect atomically at some point between its invocation and response, and that the order of operations is consistent with the real-time order of invocations.
- The replicated state machine approach is a general method for implementing a fault-tolerant service by replicating servers and coordinating client interactions with server replicas. This approach was proposed by Lamport and further elaborated by Schneider .
- An alternative method for fault-tolerance that combines ideas from replication and coding theory is fused state machines, which use (sufficient) replication to guarantee low overhead during normal operations and coding theory to reduce the number of copies to get space and message savings. This method was proposed by Garg.
- Geo-replicated storage systems aim at ensuring available, low-latency access to data even under server crashes and network partitions. They use different consistency models, such as causal consistency, to balance the trade-off between performance and correctness.



### Highly Available Services for the Notes of the Unit 10 - Replication in the Subject of Distributed System

- A highly available service is a service that can provide continuous and reliable operation despite the presence of failures in the system.
- Replication is a technique for increasing the availability of a service by creating and maintaining multiple copies of the service state or data across different nodes or locations in a distributed system.
- Replication can also improve the performance, scalability, and fault tolerance of a service by reducing the load on a single node, allowing concurrent access to different copies, and masking or recovering from failures.
- Replication can be classified into two types: eager replication and lazy replication.
  - Eager replication ensures that all the copies are updated as soon as a change occurs in the service state or data. This provides strong consistency but incurs high communication and synchronization overhead.
  - Lazy replication allows some copies to be updated later than others, after a change occurs in the service state or data. This provides weak consistency but reduces the communication and synchronization overhead.
- Replication can also be classified into two modes: active replication and passive replication.
  - Active replication executes the same operations on all the copies in the same order, using a group communication or a consensus protocol. This provides fault tolerance by masking failures, but requires more resources and coordination.
  - Passive replication executes the operations on a primary copy and propagates the changes to the backup copies, using a logging or a checkpointing protocol. This provides fault tolerance by recovering from failures, but requires a failure detection and a leader election mechanism.
- Replication can also be classified into two levels: full replication and partial replication.
  - Full replication maintains the entire service state or data on all the copies, providing uniform access and high availability, but requiring more storage and bandwidth.
  - Partial replication maintains only a subset of the service state or data on each copy, providing differentiated access and lower availability, but requiring less storage and bandwidth.



### Transactions with replicated data

- Transactions are a sequence of operations that are executed atomically, consistently, isolatedly, and durably (ACID properties) on a database system.
- Replication is a technique to distribute data across multiple servers or locations, for the purposes of fault tolerance, availability, scalability, or performance.
- Transactions with replicated data are transactions that involve data items that have multiple copies on different servers or locations.
- Transactions with replicated data pose several challenges for distributed systems, such as:
  - How to ensure that all copies of a data item are updated consistently and atomically, without violating the ACID properties of transactions?
  - How to handle concurrency control and recovery of replicated data items, especially in the presence of failures, network partitions, or conflicting updates?
  - How to balance the trade-offs between consistency, availability, and performance of replicated data, depending on the application requirements and the system characteristics?
- There are different approaches to deal with transactions with replicated data, such as:
  - Synchronous replication: In this approach, a transaction commits only after all copies of the updated data items are written to stable storage on all servers. This ensures strong consistency and durability, but at the cost of availability and performance, as the transaction has to wait for the slowest server and the network latency.
  - Asynchronous replication: In this approach, a transaction commits after writing the updated data items to stable storage on at least one server, and the other copies are updated later in the background. This improves availability and performance, but sacrifices consistency and durability, as the copies may diverge temporarily or permanently due to failures or conflicts.
  - Quorum-based replication: In this approach, a transaction commits after writing the updated data items to stable storage on a majority (or a weighted majority) of servers, and the other copies are updated later in the background. This provides a compromise between consistency, availability, and performance, as the copies are guaranteed to converge eventually and the transaction can tolerate some failures or network partitions.
  - Primary-copy replication: In this approach, one copy of each data item is designated as the primary copy, and the other copies are secondary copies. A transaction updates only the primary copy, and the secondary copies are updated later in the background. This simplifies concurrency control and recovery, as the primary copy is the source of truth, but introduces a single point of failure and a performance bottleneck.
  - Multi-master replication: In this approach, any copy of a data item can be updated by a transaction, and the other copies are updated later in the background. This allows load balancing and fault tolerance, as any server can process transactions, but complicates concurrency control and recovery, as conflicts may arise among concurrent updates to the same data item.
- To implement transactions with replicated data, distributed systems need to use protocols that coordinate the operations on the replicated data items, such as:
  - Two-phase commit (2PC): In this protocol, a transaction coordinator sends a prepare message to all servers involved in the transaction, asking them to vote on whether they can commit or abort the transaction. If all servers vote to commit, the coordinator sends a commit message to all servers, asking them to commit the transaction. If any server votes to abort, or if the coordinator does not receive a vote from a server within a timeout, the coordinator sends an abort message to all servers, asking them to abort the transaction. This protocol ensures atomicity and consistency, but not availability, as the transaction may block if the coordinator or any server fails or becomes unreachable.
  - Three-phase commit (3PC): In this protocol, a transaction coordinator sends a prepare message to all servers involved in the transaction, asking them to vote on whether they can commit or abort the transaction. If all servers vote to commit, the coordinator sends a pre-commit message to all servers, asking them to prepare to commit the transaction. If any server votes to abort, or if the coordinator does not receive a vote from a server within a timeout, the coordinator sends an abort message to all servers, asking them to abort the transaction. If the coordinator receives a pre-commit acknowledgment from all servers, the coordinator sends a commit message to all servers, asking them to commit the transaction. If the coordinator does not receive a pre-commit acknowledgment from a server within a timeout, the coordinator sends an abort message to all servers, asking them to abort the transaction. This protocol ensures atomicity and consistency, and improves availability, as the transaction can proceed even if the coordinator fails or becomes unreachable after sending the pre-commit message.
  - Paxos commit: In this protocol, a transaction coordinator uses the Paxos consensus algorithm to propose a commit

