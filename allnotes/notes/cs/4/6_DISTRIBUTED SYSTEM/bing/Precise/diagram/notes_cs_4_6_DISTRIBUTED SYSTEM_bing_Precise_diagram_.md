

## Unit 1 - Characterization of Distributed Systems

1. **Introduction:** A distributed system is a collection of independent computers that appear to the users of the system as a single coherent system.
2. **Transparency:** One of the main goals of a distributed system is to hide the fact that its processes and resources are physically distributed across multiple computers. This is known as transparency.
3. **Scalability:** Distributed systems should be scalable, meaning that the system should be able to expand in size without a loss of performance.
4. **Concurrency:** In a distributed system, multiple processes can run concurrently, and the system must be able to coordinate their actions to ensure that they do not interfere with each other.
5. **Fault tolerance:** Distributed systems must be able to continue functioning even in the presence of failures, such as the failure of individual nodes or communication links.
6. **Consistency:** In a distributed system, it is important to ensure that all nodes have a consistent view of the system's state. This can be challenging due to the inherent delays in communication between nodes.




### Introduction for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

1. A distributed system is a collection of independent computers that appears to its users as a single coherent system.
2. The main goal of a distributed system is to make it easy for users and applications to access remote resources and to share them in a controlled and efficient manner.
3. Distributed systems can be characterized by several key properties, including concurrency, lack of a global clock, independent failures, and the need for coordination and communication between components.
4. The design of distributed systems must take into account issues such as transparency, scalability, fault tolerance, and security.
5. There are several common architectures for distributed systems, including client-server, peer-to-peer, and multi-tier architectures.
6. Distributed systems can be used for a wide range of applications, including distributed computing, distributed databases, distributed file systems, and distributed web services.



### Examples of Distributed Systems

Distributed systems are systems in which components located on networked computers communicate and coordinate their actions by passing messages. Here are some examples of distributed systems:

1. **The World Wide Web:** The web is a distributed system where web pages are stored on different servers and accessed by clients using web browsers.
2. **Telecommunication networks:** Telecommunication networks, such as the telephone network and the Internet, are distributed systems that allow communication between devices located in different parts of the world.
3. **Peer-to-peer networks:** Peer-to-peer networks, such as BitTorrent, are distributed systems where each node acts as both a client and a server, sharing resources with other nodes in the network.
4. **Cloud computing:** Cloud computing is a distributed system where data and computational resources are stored on remote servers and accessed by clients over the Internet.
5. **Distributed databases:** Distributed databases are databases that are stored on multiple servers and accessed by clients over a network. This allows for faster access to data and improved reliability.
6. **Distributed file systems:** Distributed file systems, such as the Hadoop Distributed File System, are file systems that are stored on multiple servers and accessed by clients over a network. This allows for faster access to data and improved reliability.

These are just a few examples of distributed systems. Distributed systems are used in many different applications and industries, and their use is becoming increasingly common as technology advances.



### Resource Sharing

Resource sharing is one of the key characteristics of distributed systems. It refers to the ability of multiple processes or systems to access and use shared resources, such as data, hardware, and services, in a coordinated and efficient manner.

Some key points to consider when discussing resource sharing in distributed systems include:

1. **Transparency**: Resource sharing should be transparent to the user, meaning that the user should not have to be aware of the location or other details of the shared resources in order to access and use them.

2. **Scalability**: Distributed systems should be able to scale to accommodate an increasing number of shared resources and users accessing those resources.

3. **Reliability**: Resource sharing should be reliable, meaning that shared resources should be available and accessible when needed.

4. **Consistency**: Shared data should be consistent across all nodes in the distributed system, meaning that all users should see the same data regardless of where they access it from.

5. **Security**: Resource sharing should be secure, meaning that access to shared resources should be controlled and protected from unauthorized access.

Resource sharing is an important aspect of distributed systems, as it allows for the efficient use of resources and can improve the performance and functionality of the system as a whole. It is important to carefully consider the design and implementation of resource sharing mechanisms in order to ensure that they meet the needs of the system and its users.



### The Web Challenges

Unit 1 - Characterization of Distributed Systems

Distributed systems are systems that consist of multiple autonomous computers that communicate through a computer network. The computers interact with each other in order to achieve a common goal. The web is a distributed system that presents several challenges, including:

1. **Scalability**: The web must be able to handle a large number of users and requests. This requires the system to be able to scale horizontally, by adding more machines, or vertically, by adding more resources to existing machines.

2. **Heterogeneity**: The web is composed of a wide variety of devices, operating systems, and applications. This requires the system to be able to handle different data formats and communication protocols.

3. **Fault tolerance**: The web must be able to handle failures of individual components without affecting the overall functionality of the system. This requires the system to be able to detect and recover from failures.

4. **Security**: The web must be able to protect the confidentiality, integrity, and availability of data. This requires the system to be able to authenticate users, authorize access, and prevent attacks.

5. **Transparency**: The web must be able to hide the complexity of the distributed system from the user. This requires the system to be able to provide a seamless and consistent user experience.

These are some of the main challenges that must be addressed when designing and implementing distributed systems for the web.



### Architectural models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

1. **Layered architecture**: This model organizes the system into layers, where each layer provides services to the layer above it and uses the services of the layer below it. This model is commonly used in network protocols, where each layer corresponds to a different level of abstraction.

2. **Client-server architecture**: This model involves two types of components: clients and servers. Clients send requests to servers, which process the requests and return responses. This model is commonly used in web applications, where the client is a web browser and the server is a web server.

3. **Peer-to-peer architecture**: This model involves multiple components that act as both clients and servers. Each component can initiate requests and provide services to other components. This model is commonly used in file-sharing systems, where each component can share files with other components.

4. **Service-oriented architecture**: This model involves multiple components that provide services to other components. The components communicate using a standard protocol, such as SOAP or REST. This model is commonly used in enterprise systems, where different components provide different business services.

5. **Event-driven architecture**: This model involves multiple components that communicate by sending and receiving events. When a component receives an event, it processes the event and may generate new events. This model is commonly used in systems that need to respond to external events, such as user input or sensor data.

6. **Microservices architecture**: This model involves multiple small, independent components that communicate using a lightweight mechanism, such as HTTP or messaging. Each component provides a specific service and can be developed and deployed independently. This model is commonly used in cloud-native systems, where components can be easily scaled and updated.

These are some of the common architectural models used in distributed systems. Each model has its own advantages and disadvantages, and the choice of model depends on the specific requirements of the system. It is important to carefully evaluate the different models and choose the one that best fits the needs of the system.



### Fundamental Models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

1. **Interaction Model**: This model describes the ways in which distributed system components interact with each other. It includes communication protocols, message passing, and remote procedure calls.

2. **Failure Model**: This model describes the ways in which components of a distributed system can fail. It includes crash failures, omission failures, and Byzantine failures.

3. **Security Model**: This model describes the ways in which a distributed system can be secured. It includes authentication, access control, and data confidentiality.

4. **Concurrency Model**: This model describes the ways in which multiple processes can execute concurrently in a distributed system. It includes synchronization, mutual exclusion, and deadlock prevention.

5. **Consistency Model**: This model describes the ways in which data can be kept consistent across multiple components of a distributed system. It includes strong consistency, eventual consistency, and causal consistency.

These models are fundamental to the design and implementation of distributed systems, and understanding them is crucial to building robust and reliable systems.



### Theoretical Foundation for Distributed System

Distributed systems are a collection of independent computers that appear to the users as a single coherent system. The theoretical foundation for distributed systems includes the following concepts:

1. **Transparency**: This refers to the ability of the system to hide the complexity of the distributed nature of the system from the users. This includes location transparency, access transparency, concurrency transparency, and failure transparency.

2. **Scalability**: This refers to the ability of the system to handle an increasing number of users, resources, and processes without a decrease in performance. This can be achieved through techniques such as load balancing and data partitioning.

3. **Reliability**: This refers to the ability of the system to continue functioning correctly even in the presence of failures. This can be achieved through techniques such as replication and fault tolerance.

4. **Consistency**: This refers to the ability of the system to provide a consistent view of the data to all users. This can be achieved through techniques such as distributed transactions and consensus algorithms.

5. **Concurrency**: This refers to the ability of the system to handle multiple processes or threads executing simultaneously. This can be achieved through techniques such as locking and synchronization.

These concepts form the basis for the design and implementation of distributed systems. Understanding these concepts is crucial for building robust and efficient distributed systems.



### Limitation of Distributed system

Distributed systems have several limitations that can affect their performance, reliability, and scalability. Some of the limitations of distributed systems are:

1. **Network dependency**: Distributed systems rely on the network to communicate and exchange data between different nodes. If the network is slow, unreliable, or congested, the performance of the distributed system can be severely affected.

2. **Complexity**: Distributed systems are inherently more complex than centralized systems. This complexity can make it difficult to design, implement, and maintain distributed systems.

3. **Consistency**: Ensuring consistency of data across different nodes in a distributed system can be challenging. This is particularly true in systems where data is updated frequently and where there are many nodes.

4. **Fault tolerance**: Distributed systems must be designed to be fault-tolerant, meaning that they can continue to operate even if one or more nodes fail. Designing and implementing fault-tolerant distributed systems can be challenging.

5. **Security**: Security is a major concern in distributed systems. Ensuring the security of data and communications in a distributed system can be challenging, particularly in systems where there are many nodes and where data is exchanged frequently.

These are some of the limitations of distributed systems that must be considered when designing and implementing such systems. It is important to carefully evaluate the trade-offs between the benefits and limitations of distributed systems when deciding whether to use a distributed system for a particular application.



### Absence of Global Clock

- In a distributed system, there is no global clock that all nodes can use to synchronize their actions.
- Each node has its own local clock, which may not be synchronized with the clocks of other nodes.
- This can lead to inconsistencies and conflicts when nodes try to coordinate their actions or share data.
- To address this issue, distributed systems use various algorithms and protocols to synchronize the clocks of different nodes or to establish a logical order of events.
- Some common approaches include the use of logical clocks, vector clocks, and Lamport timestamps.
- Despite these efforts, the absence of a global clock remains a fundamental challenge in the design and implementation of distributed systems.



### Shared Memory

Shared memory is a type of memory architecture where multiple processors can access the same memory region. It is used in distributed systems to enable communication and synchronization between processes.

1. **Overview**: Shared memory is a memory region that can be accessed by multiple processes. This allows processes to share data and communicate with each other.

2. **Interprocess Communication**: Shared memory is one way to achieve interprocess communication (IPC) in a distributed system. Processes can read and write to the shared memory region to exchange information.

3. **Synchronization**: When multiple processes access shared memory, synchronization is necessary to ensure data consistency. This can be achieved through the use of locks, semaphores, or other synchronization mechanisms.

4. **Advantages**: Shared memory can provide fast and efficient communication between processes. It can also simplify the design of distributed systems by providing a common memory space for processes to share data.

5. **Disadvantages**: Shared memory can be difficult to implement and manage. It can also introduce synchronization overhead and increase the complexity of the system.

6. **Applications**: Shared memory is commonly used in parallel computing, where multiple processors work together to solve a problem. It is also used in multi-threaded applications, where multiple threads share data within a single process.



### Logical Clocks

Logical clocks are an essential concept in the characterization of distributed systems. They are used to provide a partial ordering of events in a distributed system and to detect causality violations.

Here are some key points to remember about logical clocks:

1. A logical clock is a monotonically increasing software counter that is maintained by each process in a distributed system.
2. Each process increments its logical clock counter before executing an event.
3. When a process sends a message, it includes the current value of its logical clock in the message.
4. When a process receives a message, it updates its logical clock to be the maximum of its current value and the value received in the message, and then increments the clock by one.
5. Logical clocks allow us to determine whether one event happened before another event in a distributed system, but they do not provide a total ordering of events.
6. Logical clocks can be used to detect causality violations, which occur when the order of events in a distributed system does not match the cause-and-effect relationships between those events.

These are some of the key points to remember about logical clocks in the context of distributed systems. They provide a useful tool for reasoning about the behavior of distributed systems and for detecting potential problems.



### Lamport’s & vectors logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- **Lamport’s Logical Clock** was created by Leslie Lamport. It provides a basis for the more advanced Vector Clock Algorithm .
- Due to the absence of a Global Clock in a Distributed Operating System, Lamport Logical Clock is needed .
- Logical clocks are based on capturing chronological and causal relationships of processes and ordering events .
- The idea behind Lamport clocks is to disregard physical time and capture just a “happens-before” relationship between a pair of events .
- **Vector Clocks** extend the capabilities of Lamport Clocks to allow us to understand the ordering across multiple processes which cross communicate .
- They can also be invaluable in understanding the flow of messages in a distributed system .
- As a data level, Vector clocks are vectors of event counters .



### Concepts in Message Passing Systems

Message passing systems are a fundamental concept in distributed systems. They allow processes to communicate and synchronize their actions by exchanging messages. Here are some key concepts in message passing systems:

1. **Message**: A message is a unit of data that is sent from one process to another. Messages can contain any type of data and can be of any size.

2. **Send and Receive**: The basic operations in a message passing system are send and receive. A process can send a message to another process, and a process can receive a message from another process.

3. **Blocking and Non-Blocking**: Send and receive operations can be either blocking or non-blocking. A blocking send operation does not return until the message has been delivered to the receiver. A blocking receive operation does not return until a message has been received. Non-blocking operations return immediately, regardless of whether the message has been delivered or received.

4. **Point-to-Point and Collective**: Message passing systems can support both point-to-point and collective communication. Point-to-point communication involves sending a message from one process to another. Collective communication involves sending a message from one process to multiple processes, or receiving a message from multiple processes.

5. **Synchronous and Asynchronous**: Message passing systems can be either synchronous or asynchronous. In a synchronous system, the sender and receiver must both be ready to communicate at the same time. In an asynchronous system, the sender and receiver do not need to be ready at the same time.

6. **Buffering**: Message passing systems can use buffering to store messages that are sent but not yet received. Buffering can improve performance by allowing the sender to continue without waiting for the receiver.

7. **Reliability**: Message passing systems can provide different levels of reliability. A reliable message passing system guarantees that messages are delivered without errors and in the order they were sent. An unreliable message passing system does not provide these guarantees.

These are some of the key concepts in message passing systems. Understanding these concepts is essential for designing and implementing distributed systems.



### Causal Order

Causal order is a concept in distributed systems that refers to the ordering of events based on their cause-and-effect relationships. In a distributed system, events can occur concurrently and messages can be delivered in different orders to different processes. Causal order ensures that related events are ordered in a way that reflects their causal relationships.

Here are some key points to remember about causal order in distributed systems:

1. Causal order is a partial order, meaning that not all events are comparable. Only events that are causally related are ordered with respect to each other.

2. Causal order is transitive. If event A causally precedes event B, and event B causally precedes event C, then event A causally precedes event C.

3. Causal order is preserved by message passing. If a message is sent from one process to another, the sending of the message causally precedes the receipt of the message.

4. Causal order can be implemented using vector clocks. Each process maintains a vector clock that records the number of events that have occurred at each process. When a process sends a message, it includes its current vector clock in the message. When a process receives a message, it updates its vector clock based on the vector clock in the message.

5. Causal order is important for ensuring consistency in distributed systems. By ensuring that events are ordered in a way that reflects their causal relationships, causal order helps to prevent inconsistencies that can arise when events are processed in the wrong order.




### Total Order

Total order is a concept in distributed systems that refers to the ordering of events or messages in a system. In a distributed system, it is important to ensure that all nodes or processes in the system agree on the order of events or messages, even if they are generated concurrently.

Here are some key points to remember about total order:

1. Total order is a property of a distributed system that ensures that all nodes or processes in the system agree on the order of events or messages.
2. Total order is achieved through the use of algorithms and protocols that ensure that messages are delivered in the same order to all nodes or processes in the system.
3. Total order is important in distributed systems because it ensures consistency and helps to prevent conflicts or errors that can arise when nodes or processes have different views of the order of events or messages.
4. Total order is not the same as causal order, which is another type of ordering used in distributed systems. Causal order ensures that messages are delivered in an order that is consistent with the causal relationships between events, while total order ensures that all nodes or processes agree on the order of all events or messages.




### Total Causal Order

Total causal order is a property of distributed systems that ensures that all events are ordered in a way that is consistent with their causal relationships. This means that if an event `e1` causally precedes another event `e2`, then `e1` must be ordered before `e2` in the total order.

Total causal order is important in distributed systems because it helps to ensure that all nodes in the system have a consistent view of the events that have occurred. This can be useful for ensuring that all nodes have the same data, for example, or for ensuring that all nodes agree on the outcome of a distributed computation.

Total causal order can be achieved using a variety of algorithms, including vector clocks and logical clocks. These algorithms allow nodes to assign timestamps to events in a way that reflects their causal relationships, and to use these timestamps to order events in a total causal order.

In summary, total causal order is a property of distributed systems that ensures that all events are ordered in a way that is consistent with their causal relationships. This can be useful for ensuring consistency and agreement among nodes in a distributed system. Total causal order can be achieved using algorithms such as vector clocks and logical clocks.



### Techniques for Message Ordering

In distributed systems, message ordering is an important aspect to ensure consistency and correctness of the system. Here are some techniques for message ordering in distributed systems:

1. **FIFO (First-In-First-Out) Ordering**: This technique ensures that messages sent from one process to another are received in the order they were sent.

2. **Causal Ordering**: This technique ensures that messages are delivered in a way that respects the cause-and-effect relationship between events in the system.

3. **Total Ordering**: This technique ensures that all processes in the system agree on the order of messages, even if the messages are sent concurrently.

4. **Partial Ordering**: This technique allows for some flexibility in the ordering of messages, while still ensuring that certain ordering constraints are met.

Each of these techniques has its own advantages and disadvantages, and the choice of technique depends on the specific requirements of the distributed system in question. It is important to carefully consider the message ordering technique used in a distributed system to ensure its correctness and consistency.



### Causal ordering of messages

Causal ordering of messages is a concept in distributed systems that ensures that messages are delivered in an order that respects the cause-and-effect relationship between events. This is important in distributed systems because messages can be delayed or lost, and processes can fail, leading to inconsistencies in the system.

Here are some key points to remember about causal ordering of messages:

1. Causal ordering is based on the happened-before relationship, which is a partial order on the set of events in a distributed system.
2. The happened-before relationship is transitive, meaning that if event A happened before event B, and event B happened before event C, then event A happened before event C.
3. Causal ordering ensures that if event A happened before event B, then any message sent as a result of event A will be delivered before any message sent as a result of event B.
4. Causal ordering can be implemented using vector clocks, which are data structures that allow processes to track the happened-before relationship between events.
5. Causal ordering is important for maintaining consistency in distributed systems, as it ensures that messages are delivered in an order that respects the cause-and-effect relationship between events.




### Global State

- In a distributed system, the global state is the collection of the local states of all the processes and the state of the communication channels.
- The global state is used to determine the properties of the system, such as whether it is in a safe or unsafe state.
- The global state is difficult to determine in a distributed system due to the lack of a global clock and the asynchronous nature of communication.
- One approach to determine the global state is through the use of snapshot algorithms, which allow processes to record their local state and the state of incoming channels in a consistent manner.
- Another approach is through the use of vector clocks, which allow processes to determine the causal relationships between events in the system.
- The global state is important for debugging, monitoring, and analyzing the behavior of distributed systems.




### Termination Detection

Termination detection is an important problem in distributed systems. It refers to the process of determining when a distributed computation has completed. This is a non-trivial problem because, in a distributed system, processes may be executing concurrently and asynchronously, and communication between processes may be subject to delays and failures.

There are several approaches to termination detection in distributed systems, including:

1. **Counting messages:** In this approach, each process keeps track of the number of messages it has sent and received. When a process has sent and received the same number of messages, it knows that all of its messages have been received and it can terminate.

2. **Dijkstra-Scholten algorithm:** This is a diffusing computation algorithm for termination detection. In this approach, a process initiates a computation by sending messages to other processes. When a process receives a message, it becomes active and can send messages to other processes. When a process has no more messages to send, it becomes passive. The computation terminates when all processes are passive and there are no messages in transit.

3. **Snapshots:** In this approach, processes periodically take snapshots of their state and exchange these snapshots with other processes. When all processes have exchanged snapshots and no process has any pending messages, the computation can terminate.

These are just a few examples of the many approaches to termination detection in distributed systems. The specific approach used will depend on the characteristics of the distributed system and the computation being performed.



## Unit 2 - Distributed Mutual Exclusion

Distributed mutual exclusion refers to the coordination of processes in a distributed system to ensure that only one process can access a shared resource at a time. This is important to prevent conflicts and ensure data consistency.

There are several algorithms for achieving distributed mutual exclusion, including:

1. **Centralized Algorithm**: In this approach, a central coordinator is responsible for granting access to the shared resource. Processes send requests to the coordinator, which grants access to one process at a time.

2. **Distributed Algorithm**: In this approach, there is no central coordinator. Instead, processes communicate with each other to determine which process should have access to the shared resource.

3. **Token-based Algorithm**: In this approach, a token is passed between processes. The process holding the token has access to the shared resource.

Each of these algorithms has its own advantages and disadvantages, and the choice of algorithm depends on the specific requirements of the distributed system. It is important to carefully consider the trade-offs between performance, scalability, and fault tolerance when choosing an algorithm for distributed mutual exclusion.



### Classification of Distributed Mutual Exclusion

Distributed mutual exclusion is a fundamental problem in distributed computing systems. It ensures that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner. In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion. Message passing is the sole means for implementing distributed mutual exclusion.

There are three basic approaches for implementing distributed mutual exclusion :

1. **Token-based approach**: A unique token (also known as the PRIVILEGE message) is shared among the sites. A site is allowed to enter its critical section if it possesses the token. Mutual exclusion is ensured because the token is unique .
2. **Non-token-based approach**: This approach does not use a token for mutual exclusion.
3. **Quorum-based approach**: This approach uses a quorum of sites to implement mutual exclusion.

These are the prime classifications of distributed mutual exclusion algorithms.



### Requirement of Mutual Exclusion Theorem

Mutual exclusion is a fundamental concept in the field of distributed systems. It refers to the requirement that, in a system of multiple processes, only one process can access a shared resource at a time. This is necessary to prevent conflicts and ensure the integrity of the data being accessed.

Here are some key points to consider when studying the requirement of mutual exclusion theorem for Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM:

1. Mutual exclusion is necessary to prevent race conditions, where multiple processes attempt to access and modify the same data simultaneously, leading to unpredictable and undesirable results.

2. The mutual exclusion theorem provides a formal framework for designing and analyzing algorithms that ensure mutual exclusion in distributed systems.

3. The theorem states that, in a system of N processes, a mutual exclusion algorithm must satisfy three conditions: safety, liveness, and fairness.

4. Safety means that at any given time, only one process can be in its critical section (i.e., accessing the shared resource).

5. Liveness means that if a process requests to enter its critical section, it will eventually be granted permission to do so.

6. Fairness means that no process should be indefinitely prevented from entering its critical section while other processes are allowed to do so.

7. There are several algorithms that can be used to achieve mutual exclusion in distributed systems, including the Ricart-Agrawala algorithm, the Maekawa algorithm, and the Lamport's bakery algorithm.

8. Understanding the requirement of mutual exclusion theorem and the various algorithms used to achieve it is essential for designing and implementing effective distributed systems.



### Unit 2 - Distributed Mutual Exclusion: Token-based and Non-token-based Algorithms

Distributed mutual exclusion is a fundamental problem in distributed systems. It deals with the coordination of processes in a distributed system to ensure that only one process can access a shared resource at a time. There are two main approaches to solving this problem: token-based and non-token-based algorithms.

#### Token-based Algorithms
Token-based algorithms use a token to control access to the shared resource. The token is passed between processes in a predefined order, and only the process holding the token is allowed to access the shared resource. Some examples of token-based algorithms include:
- **The Ricart-Agrawala Algorithm:** This algorithm uses a logical clock to order requests for the shared resource. Each process maintains a queue of pending requests, and the token is passed to the process with the earliest request.
- **The Suzuki-Kasami Algorithm:** This algorithm uses a vector of sequence numbers to order requests for the shared resource. Each process maintains a queue of pending requests, and the token is passed to the process with the highest sequence number.

#### Non-token-based Algorithms
Non-token-based algorithms do not use a token to control access to the shared resource. Instead, they rely on message passing and other mechanisms to coordinate access. Some examples of non-token-based algorithms include:
- **The Lamport Algorithm:** This algorithm uses a logical clock to order requests for the shared resource. Each process maintains a queue of pending requests, and the process with the earliest request is granted access to the shared resource.
- **The Maekawa Algorithm:** This algorithm uses a voting mechanism to coordinate access to the shared resource. Each process maintains a set of voting processes, and a process is granted access to the shared resource only if it receives a majority of votes.

In summary, distributed mutual exclusion can be achieved using either token-based or non-token-based algorithms. Each approach has its own advantages and disadvantages, and the choice of algorithm depends on the specific requirements of the distributed system.



### Performance Metrics for Distributed Mutual Exclusion Algorithms

Distributed mutual exclusion algorithms are used to ensure that only one process can access a shared resource at a time in a distributed system. There are several performance metrics that can be used to evaluate the effectiveness of these algorithms:

1. **Message complexity:** This refers to the number of messages that must be exchanged between processes in order to grant a request for the shared resource. Lower message complexity is generally desirable, as it reduces the communication overhead and improves the overall performance of the system.

2. **Synchronization delay:** This is the time it takes for a process to gain access to the shared resource once it has made a request. A lower synchronization delay is desirable, as it means that processes can access the shared resource more quickly, improving the responsiveness of the system.

3. **Response time:** This is the time it takes for a process to receive a response to its request for the shared resource. A lower response time is desirable, as it means that processes can receive confirmation that they have access to the shared resource more quickly.

4. **Fairness:** This refers to the ability of the algorithm to ensure that all processes have an equal opportunity to access the shared resource. An algorithm that is fair will prevent any one process from monopolizing the shared resource, ensuring that all processes have a chance to access it.

These are some of the key performance metrics that can be used to evaluate distributed mutual exclusion algorithms. By considering these metrics, it is possible to select an algorithm that is well-suited to the needs of a particular distributed system.



## Unit 3 - Distributed Deadlock Detection

Distributed deadlock detection is the process of detecting deadlocks in a distributed system. A deadlock occurs when two or more processes are blocked and unable to proceed because they are waiting for resources held by other processes. In a distributed system, deadlocks can occur across multiple nodes, making them more difficult to detect and resolve.

There are several approaches to distributed deadlock detection, including:

1. **Centralized approach:** In this approach, a single node is designated as the deadlock detector and is responsible for detecting deadlocks in the entire system. This approach can be efficient, but it introduces a single point of failure and can become a bottleneck as the system grows.

2. **Hierarchical approach:** In this approach, the system is organized into a hierarchy of nodes, with each node responsible for detecting deadlocks within its subtree. This approach can reduce the load on individual nodes, but it can be more complex to implement.

3. **Distributed approach:** In this approach, each node is responsible for detecting deadlocks within its local environment and communicating with other nodes to detect global deadlocks. This approach can be more scalable, but it can also be more complex to implement and can require more communication overhead.

Distributed deadlock detection algorithms can be based on various techniques, including graph-based algorithms, probe-based algorithms, and timestamp-based algorithms. Each technique has its own advantages and disadvantages, and the choice of technique will depend on the specific requirements of the system.



### System Model

A system model is a representation of a system that is used to understand and analyze its behavior. In the context of distributed deadlock detection, the system model typically includes the following components:

1. **Processes:** A set of processes that execute concurrently and may request and release resources.
2. **Resources:** A set of resources that can be requested and released by processes.
3. **Resource allocation:** A function that maps resources to the processes that currently hold them.
4. **Resource requests:** A set of resource requests made by processes.
5. **Wait-for graph:** A directed graph that represents the dependencies between processes and resources.

The system model is used to detect deadlocks in the system by analyzing the wait-for graph. If the wait-for graph contains a cycle, then a deadlock exists in the system. Various algorithms can be used to detect cycles in the wait-for graph and resolve the deadlock.



### Resource Vs Communication Deadlocks

#### Unit 3 - Distributed Deadlock Detection

In the subject of Distributed Systems, it is important to understand the difference between resource and communication deadlocks.

1. **Resource Deadlocks** occur when two or more processes are waiting for resources held by each other, resulting in a circular wait. This can happen in a distributed system when processes on different nodes are competing for shared resources.

2. **Communication Deadlocks** occur when two or more processes are waiting for messages from each other, resulting in a circular wait. This can happen in a distributed system when processes on different nodes are waiting for messages from each other to proceed.

Distributed deadlock detection algorithms can be used to detect and resolve both resource and communication deadlocks in a distributed system. These algorithms can be classified into two categories: centralized and distributed.

- **Centralized algorithms** rely on a single coordinator to collect information about the state of the system and detect deadlocks.

- **Distributed algorithms** rely on the cooperation of all nodes in the system to detect deadlocks.

Both types of algorithms have their advantages and disadvantages, and the choice of algorithm depends on the specific requirements of the system. It is important to carefully design and implement distributed deadlock detection algorithms to ensure the correct and efficient operation of the distributed system.



### Unit 3 - Distributed Deadlock Detection
#### Deadlock Prevention

Deadlock prevention is a technique used in distributed systems to ensure that deadlocks do not occur. Here are some methods for deadlock prevention:

1. **Resource ordering**: Resources are assigned a unique number and processes can only request resources in increasing order of their assigned numbers. This prevents circular wait, one of the necessary conditions for deadlock.

2. **Resource allocation denial**: A process is denied its resource request if granting the request could potentially lead to a deadlock. This requires the system to have knowledge of the current resource allocation state and the future requests of processes.

3. **Preemption**: Resources are forcibly taken away from a process if it is determined that a deadlock could occur. The process is then restarted with its resource requests.

4. **Concurrency control**: The number of processes that can access a resource at the same time is limited. This can prevent deadlocks by ensuring that resources are not over-allocated.

These are some of the methods used for deadlock prevention in distributed systems. It is important to note that these methods may not always be effective and may have their own drawbacks, such as reduced system performance or increased complexity. Therefore, it is important to carefully evaluate the trade-offs when implementing deadlock prevention techniques.



### Avoidance

Avoidance is a technique used in distributed deadlock detection in distributed systems. It involves preventing deadlocks from occurring by careful resource allocation and process scheduling. Here are some key points to remember about avoidance in the context of distributed deadlock detection:

1. Avoidance is a proactive approach to deadlock management, as opposed to reactive approaches such as detection and resolution.
2. In avoidance, the system maintains information about the current allocation of resources and the resource requirements of each process.
3. Based on this information, the system makes decisions about resource allocation and process scheduling to prevent deadlocks from occurring.
4. One common avoidance algorithm is the Banker's algorithm, which uses the concept of a safe state to ensure that the system never enters a deadlock state.
5. Avoidance can be more efficient than detection and resolution, as it prevents deadlocks from occurring in the first place, rather than having to detect and resolve them after they have occurred.
6. However, avoidance can also result in lower resource utilization, as the system may need to deny resource requests or delay process execution in order to prevent deadlocks.
7. In a distributed system, avoidance can be more challenging to implement, as the system must maintain information about resource allocation and process requirements across multiple nodes.




### Unit 3 - Distributed Deadlock Detection

#### Detection & Resolution

1. **Detection**: In a distributed system, deadlock detection is more complex than in a centralized system. This is because the resources and processes are distributed across multiple nodes, and there is no global state available to detect deadlocks. There are two main approaches to deadlock detection in distributed systems: centralized and distributed.

    - **Centralized approach**: In this approach, a single node is designated as the deadlock detector. This node is responsible for collecting information about resource allocation and process states from all other nodes in the system. It then uses this information to construct a global wait-for graph and detect cycles, which indicate the presence of a deadlock.

    - **Distributed approach**: In this approach, each node in the system is responsible for detecting deadlocks locally. Nodes communicate with each other to exchange information about resource allocation and process states. Each node constructs a local wait-for graph and detects cycles. If a cycle is detected, the nodes involved in the cycle coordinate to resolve the deadlock.

2. **Resolution**: Once a deadlock has been detected, it must be resolved. There are several approaches to resolving deadlocks in distributed systems, including:

    - **Preemption**: In this approach, one or more processes involved in the deadlock are forced to release some or all of their resources, allowing other processes to proceed.

    - **Rollback**: In this approach, one or more processes involved in the deadlock are rolled back to a previous state, releasing their resources and allowing other processes to proceed.

    - **Process termination**: In this approach, one or more processes involved in the deadlock are terminated, releasing their resources and allowing other processes to proceed.



### Centralized Deadlock Detection

Centralized deadlock detection is a technique used in distributed database systems to handle deadlock detection. In this approach, the system maintains one global wait-for graph in a single chosen site, which is named as the deadlock-detection coordinator .

There are two techniques used in the centralized approach of deadlock detection: the Completely Centralized Algorithm and the Ho Ramamurthy Algorithm (One phase and Two-phase) .

#### Completely Centralized Algorithm
In a network of n sites, one site is chosen as a control site. This site is responsible for deadlock detection .

#### Ho Ramamurthy Algorithm
This algorithm uses only two levels: Master control nodes and Cluster control nodes. Cluster control nodes are used for detecting deadlock among their members and reporting dependencies outside their cluster to the Master control node .

#### Central Coordinator
A centralized deadlock detection approach uses a central coordinator to manage a resource graph of processes and the resources they are using. Each time a process gets a lock or releases a lock on a resource, it sends a message to this coordinator (waiting-for or releasing) .



# Unit 3 - Distributed Deadlock Detection

### Distributed Deadlock Detection

- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems.
- Deadlock detection in distributed systems seems to be the best approach to handle deadlocks in distributed systems.
- Deadlock handling using the approach of deadlock detection entails addressing two basic issues: First, detection of existing deadlocks and second resolution of detected deadlocks.
- In the deadlock avoidance approach to distributed systems, a resource is granted to a process if the resulting global system is safe.
- Deadlock detection requires an examination of the status of the process–resources interaction for the presence of a deadlock condition.
- To resolve the deadlock, we have to abort a deadlocked process.
- Distributed deadlocks can be detected either by constructing a global wait-for graph, from local wait-for graphs at a deadlock detector or by a distributed algorithm like edge chasing.
- Phantom deadlocks are deadlocks that are detected in a distributed system due to system internal delays but no longer actually exist at the time of detection.




### Path Pushing Algorithms

Path pushing algorithms are a class of algorithms used in distributed deadlock detection. These algorithms work by propagating information about blocked processes along wait-for edges in the resource graph. The basic idea is to push information about blocked processes along the wait-for edges until a cycle is detected, indicating a deadlock.

Here are some key points to remember about path pushing algorithms:

1. Path pushing algorithms are used in distributed deadlock detection.
2. These algorithms work by propagating information about blocked processes along wait-for edges in the resource graph.
3. The basic idea is to push information about blocked processes along the wait-for edges until a cycle is detected, indicating a deadlock.
4. Path pushing algorithms can be classified into two categories: edge-chasing algorithms and diffusing computation algorithms.
5. Edge-chasing algorithms work by sending probe messages along wait-for edges to detect cycles in the resource graph.
6. Diffusing computation algorithms work by initiating a distributed computation to detect cycles in the resource graph.




### Edge Chasing Algorithms

Edge chasing algorithms are used for distributed deadlock detection in distributed systems. Here are some key points to note about edge chasing algorithms:

1. Edge chasing algorithms are based on the concept of sending probe messages to detect cycles in the wait-for graph.
2. A probe message contains information about the initiator of the probe, the current transaction, and the dependent transaction.
3. When a transaction receives a probe message, it checks if it is waiting for any other transaction. If it is, it forwards the probe message to the transaction it is waiting for.
4. If a transaction receives a probe message that it has initiated, it means that a cycle has been detected and a deadlock has occurred.
5. Edge chasing algorithms can be classified into two types: the basic edge chasing algorithm and the diffusing computation edge chasing algorithm.
6. The basic edge chasing algorithm is simple to implement but can generate a large number of probe messages.
7. The diffusing computation edge chasing algorithm is more efficient as it reduces the number of probe messages generated.

This is a brief overview of edge chasing algorithms for distributed deadlock detection in distributed systems. It is important to understand these algorithms in order to effectively detect and resolve deadlocks in distributed systems.



## Unit 4 - Agreement Protocols

Agreement protocols are a class of protocols used in distributed systems to ensure that all processes in the system agree on a certain value or state. These protocols are important for maintaining consistency and reliability in distributed systems.

Some common types of agreement protocols include:

1. **Consensus protocols:** These protocols are used to ensure that all processes in the system agree on a single value. This is typically achieved through a series of rounds of communication between the processes.

2. **Byzantine fault tolerance protocols:** These protocols are designed to handle situations where some processes in the system may behave maliciously or fail in arbitrary ways. They ensure that the system can still reach agreement even in the presence of such failures.

3. **Atomic commit protocols:** These protocols are used to ensure that a set of transactions are either all committed or all aborted, even in the presence of failures. This is important for maintaining the consistency of data in distributed systems.

4. **Leader election protocols:** These protocols are used to elect a leader among a group of processes. The leader is responsible for coordinating the actions of the other processes and ensuring that the system reaches agreement.

Agreement protocols are a crucial component of distributed systems and are used to ensure the reliability and consistency of these systems. They are an active area of research and development, with new protocols and techniques being developed to improve their performance and resilience.



### Introduction for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- Agreement protocols are a fundamental part of distributed systems.
- They are used to ensure that all nodes in a distributed system agree on a common value or decision.
- Agreement protocols are necessary for the correct functioning of distributed systems, as they ensure consistency and reliability.
- There are several types of agreement protocols, including consensus, atomic commit, and leader election.
- These protocols are used in various applications, such as distributed databases, distributed file systems, and distributed transaction processing systems.
- In this unit, we will study the different types of agreement protocols and their applications in distributed systems.



### System Models

A system model is an abstract representation of a distributed system that captures the essential features of the system and its environment. It is used to reason about the behavior of the system and to derive algorithms and protocols for the system.

In the context of agreement protocols in distributed systems, the following system models are commonly used:

1. **Synchronous System Model**: In this model, there are known bounds on the time it takes for a message to be delivered and for a process to perform a step. This allows for the design of algorithms that rely on timing assumptions.

2. **Asynchronous System Model**: In this model, there are no known bounds on message delivery time or the time it takes for a process to perform a step. This makes the design of algorithms more challenging, as they cannot rely on timing assumptions.

3. **Partially Synchronous System Model**: This model is a hybrid of the synchronous and asynchronous models. It assumes that the system is synchronous most of the time, but may occasionally behave asynchronously.

4. **Crash-Recovery Model**: This model assumes that processes may crash and later recover. It is used to design algorithms that can tolerate process failures and recover from them.

5. **Byzantine Model**: This model assumes that processes may behave arbitrarily, including sending incorrect or conflicting information to other processes. It is used to design algorithms that can tolerate malicious behavior.

These system models provide a framework for the design and analysis of agreement protocols in distributed systems. By making explicit assumptions about the behavior of the system and its environment, they allow for the development of algorithms that can achieve agreement despite the challenges of distributed computing.



### Classification of Agreement Problem

Agreement problems are a class of problems in distributed systems where multiple processes need to agree on a single value or decision. These problems arise in various scenarios, such as distributed databases, distributed consensus, and fault-tolerant systems.

There are several types of agreement problems, including:

1. **Consensus:** In this problem, all processes must agree on a single value, even if some processes fail or behave maliciously.
2. **Byzantine Agreement:** This is a more challenging version of the consensus problem, where some processes may behave arbitrarily, including sending conflicting information to different processes.
3. **Interactive Consistency:** In this problem, each process has an initial value, and all processes must agree on a vector of these values, even if some processes fail.
4. **Atomic Commit:** This problem arises in distributed databases, where multiple processes must agree on whether to commit or abort a transaction.

These problems are closely related and solutions to one problem can often be adapted to solve another. However, the exact requirements and assumptions of each problem can vary, making it important to carefully define and classify the problem at hand.



### Byzantine Agreement Problem

The Byzantine agreement problem is one of the fundamental problems in fault-tolerant distributed computing. It requires a set of parties in a distributed environment to agree on a value even if some of the parties are corrupted. The problem was first defined by Lamport, who also provided the first solution under the situation of processor failure. According to the concept of Byzantine agreement problem, a source processor is taken to broadcast its initial value to another processor in the system.

The problem of obtaining Byzantine consensus was conceived and formalized by Robert Shostak, who dubbed it the interactive consistency problem. This work was done in 1978 in the context of the NASA-sponsored SIFT project in the Computer Science Lab at SRI International.

To solve the Byzantine Generals problem, loyal generals need a secure way to come to agreement on a plan (known as consensus) and carry out their chosen plan (known as coordination). While actually solving the Byzantine Generals Problem is quite complex, we now understand the fundamental challenge.



# Consensus Problem in Distributed Systems

The consensus problem is a fundamental problem in distributed computing and multi-agent systems. It is the problem of getting a set of nodes in a distributed system to agree on something. This something might be a value, a course of action, or a decision .

Achieving consensus allows a distributed system to act as a single entity, with every individual node aware of and in agreement with the actions of the whole of the network . This is important for achieving overall system reliability in the presence of a number of faulty processes.

There are many ways in which processes in a distributed system can reach a consensus. However, there is usually a constant struggle between security and performance. The more we want our algorithm to be secure against ways in which failure can happen, the less performant it tends to become.



### Interactive Consistency Problem

Interactive consistency, also known as distributed consensus, is a fundamental problem in computer science. The goal of distributed consensus is to reach an agreement in a distributed system in the presence of faults.

The problem was introduced by Pease, Shostak, and Lamport. It involves `n` nodes, where up to `t` may be Byzantine, each with its own private value. The nodes run an algorithm that allows all non-faulty nodes to infer the values of each other node.

A protocol for the interactive consistency problem should meet the following conditions :
- **Agreement**: All non-faulty processors agree on the same vector `(V1,V2,…,Vn)`.
- **Validity**: If the `ith` processor is non-faulty and the initial value is `Vi`, then the `ith` value to be agreed on by all non-faulty processors must be `Vi`.

This problem is relevant to critical applications that rely on the combination of the opinions of multiple peers to provide a result.



### Solution to Byzantine Agreement problem

The Byzantine Agreement problem was first defined by Lamport, who also provided the first solution under the situation of processor failure . To solve the Byzantine Generals problem, loyal generals need a secure way to come to agreement on a plan (known as consensus) and carry out their chosen plan (known as coordination) . The solution to the Byzantine Generals Problem involves some hashing, heavy computing work, and communication between all of the nodes (generals) to verify the message .

According to the concept of Byzantine agreement problem, a source processor is taken to broadcast its initial value to another processor in the system . While actually solving the Byzantine Generals Problem is quite complex, we now understand the fundamental challenge .



### Application of Agreement problem

The agreement problem is a fundamental problem in distributed systems, where multiple processes must agree on a single value. This problem arises in various scenarios, such as:

1. **Consensus**: In a distributed system, processes must agree on a common value, even in the presence of failures. This is known as the consensus problem, and it is a fundamental problem in distributed computing.

2. **Atomic Commit**: In a distributed database system, a transaction may involve multiple sites. The atomic commit problem is to ensure that either all sites commit the transaction or all sites abort the transaction.

3. **Leader Election**: In a distributed system, it is often necessary to elect a leader among the processes. The leader election problem is to ensure that all processes agree on the same leader.

4. **Byzantine Agreement**: In a distributed system, some processes may behave maliciously. The Byzantine agreement problem is to ensure that all non-faulty processes agree on the same value, even in the presence of malicious processes.

These are some of the applications of the agreement problem in distributed systems. The agreement protocols are designed to solve these problems and ensure that all processes in a distributed system agree on a common value.



### Atomic Commit in Distributed Database system

Atomic commit is a fundamental concept in distributed database systems. It refers to the process of ensuring that a transaction is either completed successfully or aborted, with no intermediate states. This is important in distributed systems, where multiple nodes may be involved in a transaction, and failure of one node can affect the entire transaction.

In a distributed database system, an atomic commit protocol is used to coordinate the commit or abort of a transaction across all participating nodes. The most commonly used atomic commit protocol is the two-phase commit (2PC) protocol.

The 2PC protocol has two phases: the prepare phase and the commit phase. In the prepare phase, the coordinator node sends a prepare message to all participating nodes, asking them to prepare to commit the transaction. Each node then writes the changes to its local log and sends an acknowledgement to the coordinator. If all nodes respond with an acknowledgement, the coordinator moves to the commit phase.

In the commit phase, the coordinator sends a commit message to all participating nodes, instructing them to commit the transaction. Each node then makes the changes permanent and sends an acknowledgement to the coordinator. If any node fails to respond, the coordinator aborts the transaction and sends an abort message to all participating nodes.

The 2PC protocol ensures that a transaction is either committed on all nodes or aborted on all nodes, providing atomicity and consistency in the distributed database system.



# Unit 5 - Distributed Resource Management

Distributed resource management refers to the process of managing resources in a distributed computing environment. This includes the allocation, scheduling, and coordination of resources such as processing power, memory, storage, and network bandwidth across multiple systems.

Some key points to consider when studying distributed resource management include:

1. **Resource allocation:** In a distributed system, resources must be allocated efficiently to ensure that all tasks are completed in a timely manner. This involves determining which resources are available, and assigning them to tasks based on their requirements.

2. **Scheduling:** Once resources have been allocated, they must be scheduled to ensure that tasks are completed in the correct order. This involves determining the order in which tasks should be executed, and assigning resources to them accordingly.

3. **Coordination:** In a distributed system, it is important to coordinate the use of resources to ensure that they are used efficiently. This involves managing dependencies between tasks, and ensuring that resources are not over- or under-utilized.

4. **Load balancing:** In a distributed system, it is important to balance the load across all systems to ensure that no single system becomes a bottleneck. This involves distributing tasks and resources evenly across all systems, to ensure that they are all utilized efficiently.

5. **Fault tolerance:** In a distributed system, it is important to ensure that the system can continue to function even in the event of a failure. This involves implementing mechanisms to detect and recover from failures, and to ensure that resources are reallocated as needed.

Overall, distributed resource management is a complex and challenging task that requires careful planning and coordination to ensure that resources are used efficiently and effectively. By understanding the key concepts and techniques involved, it is possible to design and implement effective distributed resource management systems.



### Issues in Distributed File Systems

Distributed file systems are designed to provide transparent access to files stored on a network of computers. However, there are several issues that arise in the design and implementation of distributed file systems. Some of the key issues are:

1. **Consistency**: Ensuring that all clients see the same view of the file system, even when updates are made concurrently by multiple clients, is a major challenge in distributed file systems.

2. **Replication**: Replicating files across multiple servers can improve availability and performance, but it also introduces challenges in maintaining consistency and managing updates.

3. **Fault tolerance**: Distributed file systems must be designed to be resilient to failures of individual nodes or network links. This requires mechanisms for detecting and recovering from failures, as well as for ensuring data integrity and availability.

4. **Scalability**: As the number of clients and servers in a distributed file system grows, the system must be able to scale to handle the increased load. This requires efficient algorithms for data placement, load balancing, and resource management.

5. **Security**: Distributed file systems must provide mechanisms for securing data and controlling access to files. This includes authentication, authorization, and encryption.

6. **Heterogeneity**: Distributed file systems must be able to operate across a wide range of hardware and software platforms, and must be able to accommodate differences in file formats, naming conventions, and other system-specific details.

These are some of the key issues that must be addressed in the design and implementation of distributed file systems. A thorough understanding of these issues is essential for building robust and reliable distributed file systems.



### Mechanism for building distributed file systems

Distributed file systems are designed to provide shared access to files and directories across a network of computers. Here are some key mechanisms for building distributed file systems:

1. **Data distribution:** One of the main challenges in building a distributed file system is deciding how to distribute data across multiple servers. There are several approaches to this, including data striping, where data is split into blocks and distributed across multiple servers, and data replication, where multiple copies of the data are stored on different servers.

2. **Consistency:** Ensuring consistency of data across multiple servers is another important mechanism in building distributed file systems. This can be achieved through techniques such as versioning, where each update to a file is assigned a unique version number, and conflict resolution, where conflicts between updates are resolved through a predefined set of rules.

3. **Fault tolerance:** Distributed file systems must be designed to be fault-tolerant, meaning that they can continue to operate even in the presence of failures. This can be achieved through mechanisms such as data replication, where multiple copies of data are stored on different servers, and failure detection and recovery, where the system can detect when a server has failed and take steps to recover from the failure.

4. **Scalability:** As the number of users and the amount of data stored in a distributed file system grows, the system must be able to scale to accommodate this growth. This can be achieved through mechanisms such as dynamic data distribution, where data is automatically redistributed across servers as the system grows, and load balancing, where the system can balance the load across multiple servers to ensure that no single server becomes overloaded.

5. **Security:** Security is an important consideration in building distributed file systems, as the system must be able to protect data from unauthorized access. This can be achieved through mechanisms such as access control, where users are granted or denied access to files and directories based on a set of predefined rules, and encryption, where data is encrypted before being stored on the servers to protect it from unauthorized access.

These are some of the key mechanisms for building distributed file systems. By carefully considering these mechanisms and designing the system accordingly, it is possible to build a distributed file system that is scalable, fault-tolerant, consistent, and secure.



### Design issues in Distributed Shared Memory

Distributed Shared Memory (DSM) is a mechanism that manages memory across multiple nodes and makes inter-process communications clear to end-users. To design a distributed shared memory system, certain issues must be addressed. Some of these issues include:

1. **Granularity**: Granularity refers to the block size of a DSM system. It is the unit of sharing and the unit of transfer between nodes. The choice of granularity affects the performance of the system.

2. **Structure of shared memory space**: Structure refers to the design of the shared data in the memory. The structure of the shared memory space affects the performance and scalability of the system.

3. **Memory coherence**: Memory coherence is the consistency of shared data across multiple nodes. Ensuring memory coherence is a major challenge in the design of DSM systems.

4. **Design choices**: Design choices include structure and granularity, coherence semantics, scalability, and heterogeneity. These choices affect the performance, scalability, and ease of use of the system.

5. **Implementation methods**: The implementation methods used to achieve memory coherence, such as directory-based or snooping-based, affect the performance and scalability of the system.

These are some of the design issues that must be addressed when designing a distributed shared memory system. Each issue presents its own challenges and trade-offs, and the choices made will affect the overall performance and usability of the system.



### Algorithm for Implementation of Distributed Shared Memory

Distributed Shared Memory (DSM) is a system that allows multiple computers to share a single virtual memory space. This is achieved by implementing a software layer that manages the distribution of data across the network. Here is an algorithm for implementing DSM:

1. **Initialization:** The DSM system is initialized by creating a shared virtual memory space that is accessible to all participating computers. This space is divided into pages, and each page is assigned a unique identifier.

2. **Data Distribution:** When a computer needs to access a page of shared memory, it sends a request to the DSM system. The DSM system checks if the page is already stored locally. If it is, the data is returned to the requesting computer. If the page is not stored locally, the DSM system retrieves it from another computer that has a copy and sends it to the requesting computer.

3. **Data Consistency:** To ensure data consistency, the DSM system uses a coherence protocol. This protocol ensures that when multiple computers are accessing the same page of shared memory, they all see the same data. There are several coherence protocols that can be used, including the write-invalidate protocol and the write-update protocol.

4. **Fault Tolerance:** The DSM system must be able to handle failures of individual computers. This is achieved by replicating data across multiple computers. If one computer fails, the data can still be accessed from another computer.

This is a basic algorithm for implementing a Distributed Shared Memory system. There are many variations and optimizations that can be applied to improve performance and reliability.



## Unit 6 - Failure Recovery in Distributed Systems

1. **Introduction:** In distributed systems, failure recovery is the process of restoring the system to a consistent state after a failure has occurred.
2. **Types of Failures:** There are several types of failures that can occur in distributed systems, including node failures, network failures, and Byzantine failures.
3. **Fault Tolerance:** Fault tolerance is the ability of a system to continue functioning despite the presence of failures. This can be achieved through techniques such as replication and redundancy.
4. **Checkpointing:** Checkpointing is a technique used to save the state of a system at regular intervals, allowing the system to recover from failures by restoring the saved state.
5. **Logging:** Logging is the process of recording system events and actions, allowing the system to recover from failures by replaying the logged events.
6. **Recovery Protocols:** There are several recovery protocols that can be used in distributed systems, including two-phase commit, three-phase commit, and Paxos.
7. **Conclusion:** Failure recovery is an important aspect of distributed systems, allowing the system to continue functioning despite the presence of failures. Techniques such as fault tolerance, checkpointing, and logging can be used to achieve this goal.




### Concepts in Backward and Forward recovery for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- **Backward recovery** is a technique used to recover from failures in distributed systems by restoring the system to a previous consistent state.
- This is achieved by maintaining a log of all changes made to the system and using this log to undo any changes made after the failure occurred.
- Backward recovery is also known as **rollback recovery**.
- **Forward recovery** is a technique used to recover from failures in distributed systems by attempting to continue execution from the point of failure.
- This is achieved by maintaining redundant copies of data and using these copies to continue execution in the event of a failure.
- Forward recovery is also known as **rollforward recovery**.
- Both backward and forward recovery techniques are used to ensure the **consistency** and **availability** of distributed systems in the event of failures.
- The choice of recovery technique used depends on the specific requirements of the system and the nature of the failure.



### Recovery in Concurrent Systems

Recovery in concurrent systems is an important aspect of failure recovery in distributed systems. Here are some key points to consider:

1. **Concurrency control** is necessary to ensure that multiple processes can access shared data and resources without interfering with each other. This is important for maintaining data consistency and integrity in a distributed system.

2. **Recovery techniques** are used to restore the system to a consistent state after a failure. This can involve rolling back transactions, restoring data from backups, or using other methods to recover from the failure.

3. **Checkpointing** is a common technique used to facilitate recovery in concurrent systems. This involves periodically saving the state of the system to stable storage, so that it can be restored in the event of a failure.

4. **Logging** is another technique used to facilitate recovery. This involves recording changes to the system in a log, which can be used to reconstruct the state of the system after a failure.

5. **Distributed commit protocols** such as the two-phase commit protocol can be used to ensure that transactions are either committed or aborted consistently across all nodes in a distributed system.

6. **Fault tolerance** is an important aspect of recovery in concurrent systems. This involves designing the system to be resilient to failures, so that it can continue to operate even in the presence of faults.

Overall, recovery in concurrent systems is a complex and challenging task, but it is essential for ensuring the reliability and availability of distributed systems. By using techniques such as concurrency control, checkpointing, logging, and distributed commit protocols, it is possible to recover from failures and maintain the consistency and integrity of the system.



### Obtaining consistent Checkpoints for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

1. **Introduction**: In distributed systems, failure recovery is an important aspect to ensure the system's reliability and availability. One of the techniques used for failure recovery is checkpointing, which involves saving the state of the system at regular intervals to enable faster recovery in case of a failure.

2. **Checkpointing**: Checkpointing is the process of taking a snapshot of the system's state at a particular point in time. This snapshot can be used to restore the system to a consistent state in case of a failure.

3. **Consistent Checkpoints**: A consistent checkpoint is a snapshot of the system's state that satisfies the consistency criteria. This means that the checkpoint represents a global state of the system where all the processes are in a consistent state with respect to each other.

4. **Obtaining Consistent Checkpoints**: There are several techniques that can be used to obtain consistent checkpoints in a distributed system. Some of these techniques include coordinated checkpointing, communication-induced checkpointing, and independent checkpointing.

5. **Coordinated Checkpointing**: In coordinated checkpointing, all the processes in the system coordinate with each other to take a global snapshot of the system's state. This involves exchanging messages between the processes to ensure that all the processes reach a consistent state before taking the checkpoint.

6. **Communication-Induced Checkpointing**: In communication-induced checkpointing, the processes take checkpoints based on the communication pattern between them. This technique uses the information about the messages exchanged between the processes to determine when to take a checkpoint.

7. **Independent Checkpointing**: In independent checkpointing, each process takes its checkpoint independently without coordinating with other processes. This technique is simpler than the other techniques, but it may result in an inconsistent global state.

8. **Conclusion**: Obtaining consistent checkpoints is an important aspect of failure recovery in distributed systems. There are several techniques that can be used to obtain consistent checkpoints, and the choice of technique depends on the specific requirements of the system.



### Recovery in Distributed Database Systems

Recovery in distributed database systems is the process of restoring the database to a consistent state after a failure. The goal of recovery is to maintain the atomicity and durability of distributed transactions. A database must guarantee that all statements in a transaction, distributed or non-distributed, either commit or roll back as a unit.

There are two types of failures that can occur in a distributed database system: soft failures and hard failures.

1. **Soft Failures**: In case of soft failures that result in inconsistency of the database, the recovery strategy includes transaction undo or rollback. However, sometimes, transaction redo may also be adopted to recover to a consistent state of the transaction.

2. **Hard Failures**: In case of hard failures resulting in extensive damage to the database, recovery strategies encompass restoring a past copy of the database from archival backup.

Distributed recovery is more complicated than centralized database recovery because failures can occur at the communication links or a remote site. Ideally, a recovery system should be simple, incur tolerable overhead, maintain system consistency, provide partial operability and avoid global rollback.

Transaction recovery is done to eliminate the adverse effects of faulty transactions rather than to recover from a failure. Faulty transactions include all transactions that have changed the database into an undesired state and the transactions that have used values written by the faulty transactions.



## Unit 7 - Fault Tolerance

Fault tolerance is the ability of a system to continue functioning in the event of a failure. This can be achieved through various methods, including:

1. **Redundancy**: This involves having multiple components or systems that can take over in the event of a failure. For example, a system may have multiple power supplies, so that if one fails, the others can continue to provide power.

2. **Failover**: This involves automatically switching to a backup system in the event of a failure. For example, a database may have a standby server that can take over if the primary server fails.

3. **Error correction**: This involves detecting and correcting errors in data. For example, a system may use error-correcting codes to detect and correct errors in data storage or transmission.

4. **Recovery**: This involves restoring a system to a known good state after a failure. For example, a system may use backups to restore data after a disk failure.

Fault tolerance is an important consideration in the design of many systems, including computer systems, networks, and power grids. By incorporating fault tolerance into a system, designers can help ensure that the system will continue to function even in the event of a failure. This can help prevent downtime, data loss, and other negative consequences of system failures.



### Unit 7 - Fault Tolerance in Distributed Systems
#### Issues in Fault Tolerance

1. **Redundancy**: One of the main issues in fault tolerance is the need for redundancy. This can be in the form of hardware, software, or data redundancy. The goal is to have backup systems or components that can take over in case of a failure.

2. **Reliability**: Another issue is the reliability of the system. This refers to the ability of the system to continue functioning correctly even in the presence of faults. This can be achieved through various techniques such as error detection and correction, and failure recovery.

3. **Consistency**: In a distributed system, it is important to maintain consistency across all nodes. This can be challenging in the presence of faults, as some nodes may have outdated or incorrect information.

4. **Recovery**: In the event of a failure, it is important to have a recovery plan in place. This can involve restoring data from backups, restarting failed components, or switching to backup systems.

5. **Testing**: It is important to thoroughly test a fault-tolerant system to ensure that it can handle various types of faults and failures. This can involve simulating failures and testing the system's response.

6. **Cost**: Implementing fault tolerance can be expensive, as it often involves adding additional hardware or software components. It is important to balance the cost of implementing fault tolerance with the potential cost of system downtime or data loss.

7. **Complexity**: Adding fault tolerance to a system can increase its complexity, making it more difficult to design, implement, and maintain. It is important to carefully consider the trade-offs between fault tolerance and system complexity.



### Commit Protocols

Commit protocols are used in distributed systems to ensure that all the nodes in the system agree on the final outcome of a transaction. This is important for maintaining the consistency and integrity of the data in the system. There are several types of commit protocols, including two-phase commit (2PC) and three-phase commit (3PC).

1. **Two-Phase Commit (2PC)**: In the first phase of 2PC, the coordinator node sends a prepare message to all the participant nodes, asking them to prepare to commit the transaction. The participant nodes then respond with a yes or no vote, indicating whether they are ready to commit the transaction. In the second phase, the coordinator node sends a commit or abort message to all the participant nodes, based on the votes received in the first phase. All the participant nodes then commit or abort the transaction accordingly.

2. **Three-Phase Commit (3PC)**: 3PC is an extension of 2PC, with an additional phase added to make the protocol more resilient to failures. In the first phase of 3PC, the coordinator node sends a canCommit message to all the participant nodes, asking them if they can commit the transaction. The participant nodes then respond with a yes or no vote. In the second phase, the coordinator node sends a preCommit message to all the participant nodes that voted yes, asking them to prepare to commit the transaction. The participant nodes then respond with an ack message, indicating that they are ready to commit the transaction. In the third phase, the coordinator node sends a doCommit message to all the participant nodes that sent an ack message, instructing them to commit the transaction.

These are some of the commit protocols used in distributed systems to ensure fault tolerance and consistency of data. They play a crucial role in maintaining the integrity of the system and preventing data loss or corruption.



### Voting protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Fault tolerance is a major difference between distributed systems and single machine systems. With the former, partial failure is possible, i.e., when one component in a distributed system fails.
- Distributed voting is a well-known fault-tolerance technique. For the most part, however, security had not been a concern in systems that used voting.
- A new, more general voting protocol has been presented that reduces the vulnerability of the voting process to both attacks and faults. The algorithm is contrasted with the traditional 2-phase commit protocols typically used in distributed voting and with other proposed secure voting schemes.
- Distributed voting is a common method for achieving fault-tolerance, consisting of a set of distributed processors all working on the same task, then voting on the independent results to pick one as the correct answer.
- Various schemes are used for the vote assignment, including the dynamic vote assignment policies. Group voting mechanism is used for effective message passing.



### Dynamic Voting Protocols

Dynamic voting protocols are used in distributed systems to achieve fault tolerance. These protocols allow the system to continue functioning even in the presence of failures. Here are some key points to note about dynamic voting protocols:

1. Dynamic voting protocols are used to ensure data consistency in the presence of failures.
2. These protocols work by dynamically adjusting the number of votes required to perform an operation based on the current state of the system.
3. The number of votes required to perform an operation can change over time based on factors such as the number of failed nodes or the level of contention in the system.
4. Dynamic voting protocols can help to improve the availability of the system by allowing operations to proceed even when some nodes have failed.
5. These protocols can also help to improve the performance of the system by reducing the number of votes required to perform an operation when the system is under low contention.
6. Dynamic voting protocols can be used in conjunction with other fault tolerance techniques such as replication to provide even greater levels of fault tolerance.

In summary, dynamic voting protocols are an important tool for achieving fault tolerance in distributed systems. These protocols allow the system to continue functioning even in the presence of failures by dynamically adjusting the number of votes required to perform an operation. This can help to improve both the availability and the performance of the system.



## Unit 8 - Transactions and Concurrency Control

1. **Transactions** are a sequence of database operations that are executed as a single unit of work. The purpose of a transaction is to ensure data consistency and integrity in the face of failures, such as system crashes or power outages.

2. **Concurrency control** is the process of managing simultaneous access to a database by multiple users. The goal of concurrency control is to ensure that transactions are executed in a way that maintains the consistency and integrity of the data.

3. **Locking** is a common concurrency control mechanism used to prevent conflicts between transactions. Locking involves placing locks on data items to prevent other transactions from accessing or modifying them until the lock is released.

4. **Two-phase locking (2PL)** is a locking protocol that ensures serializability. In 2PL, a transaction must acquire all the locks it needs before it can release any locks. This is done in two phases: the growing phase, where the transaction acquires locks, and the shrinking phase, where the transaction releases locks.

5. **Deadlocks** can occur when two or more transactions are waiting for each other to release locks. Deadlock prevention and detection techniques can be used to avoid or resolve deadlocks.

6. **Timestamp ordering** is another concurrency control mechanism that assigns a timestamp to each transaction and uses the timestamps to determine the order in which transactions are executed.

7. **Optimistic concurrency control** is a technique that assumes that conflicts between transactions are rare and allows transactions to execute without acquiring locks. Conflicts are detected at the end of the transaction, and if a conflict is detected, the transaction is rolled back and restarted.

8. **Multiversion concurrency control** is a technique that maintains multiple versions of data items to allow transactions to read data without acquiring locks. Transactions can read the version of the data item that was current at the start of the transaction, even if the data item has been modified by other transactions.



### Transactions

A transaction is a logical unit of work that contains one or more database operations. These operations can include reading, updating, inserting, or deleting data in a database. Transactions are used to ensure data consistency and integrity in a database.

Here are some key points to remember about transactions in the context of distributed systems and concurrency control:

1. **Atomicity**: Transactions are atomic, meaning that either all the operations in a transaction are completed successfully, or none of them are applied. This ensures that the database remains in a consistent state even if a failure occurs during the transaction.

2. **Consistency**: Transactions ensure that the database remains in a consistent state by enforcing integrity constraints. For example, if a transaction transfers funds from one account to another, it must ensure that the total balance of the two accounts remains the same.

3. **Isolation**: Transactions are executed in isolation from one another, meaning that the changes made by one transaction are not visible to other transactions until the first transaction is committed. This ensures that transactions do not interfere with one another and prevents concurrency-related issues such as dirty reads and lost updates.

4. **Durability**: Once a transaction is committed, its changes are permanent and must survive any subsequent failures. This is typically achieved by writing the changes to a durable storage medium such as a disk.

In a distributed system, transactions may span multiple nodes, and concurrency control mechanisms are used to ensure that transactions are executed correctly and in a coordinated manner across all the nodes involved. Some common concurrency control mechanisms used in distributed systems include two-phase locking, timestamp ordering, and optimistic concurrency control. These mechanisms help to ensure that transactions are executed in a way that preserves the ACID properties of atomicity, consistency, isolation, and durability.



### Unit 8 - Transactions and Concurrency Control in DISTRIBUTED SYSTEMS
#### Nested Transactions

- A nested transaction is a transaction that is executed within the context of another transaction, called the parent transaction.
- Nested transactions provide a way to structure complex transactions into smaller, more manageable units.
- Each nested transaction has its own independent workspace, which is used to store changes made during the transaction.
- If a nested transaction commits, its changes are saved to the workspace of its parent transaction.
- If a nested transaction aborts, its changes are discarded and do not affect the parent transaction.
- The parent transaction can choose to commit or abort the changes made by its nested transactions.
- Nested transactions can be used to implement advanced concurrency control techniques, such as optimistic concurrency control and multiversion concurrency control.
- Nested transactions can also be used to implement advanced recovery techniques, such as nested top actions and partial rollbacks.




### Locks for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

1. Locks are a mechanism used to ensure that only one transaction can access a data item at a time.
2. Locks can be either shared or exclusive. Shared locks allow multiple transactions to read a data item simultaneously, while exclusive locks allow only one transaction to write to a data item.
3. Locks are typically implemented using a lock manager, which maintains a table of locks and their current status.
4. When a transaction requests a lock, the lock manager checks the lock table to see if the requested lock is available. If it is, the lock is granted and the transaction can proceed. If the lock is not available, the transaction must wait until the lock is released.
5. Locks can be released either explicitly by the transaction that holds them or implicitly when the transaction commits or aborts.
6. Deadlocks can occur when two or more transactions are waiting for locks held by each other. Deadlock detection and resolution techniques are used to detect and resolve such situations.
7. Locks can be used in conjunction with other concurrency control techniques such as timestamps and optimistic concurrency control to ensure the consistency and correctness of transactions in a distributed system.



### Optimistic Concurrency Control

Optimistic Concurrency Control (OCC) is a method used in distributed systems to manage transactions and concurrency control. It is based on the assumption that conflicts between transactions are rare and that it is more efficient to allow transactions to execute concurrently and only check for conflicts at the end, rather than locking resources and preventing conflicts from occurring.

Here are some key points to remember about Optimistic Concurrency Control:

1. OCC allows transactions to execute concurrently without acquiring locks on the data they access.
2. At the end of a transaction, the system checks if any conflicts have occurred with other transactions.
3. If a conflict is detected, the transaction is rolled back and must be restarted.
4. OCC is best suited for environments where conflicts between transactions are rare.
5. OCC can improve system performance by reducing the overhead of acquiring and releasing locks.

In summary, Optimistic Concurrency Control is a method used in distributed systems to manage transactions and concurrency control. It allows transactions to execute concurrently without acquiring locks, and checks for conflicts at the end of the transaction. OCC can improve system performance in environments where conflicts between transactions are rare.



### Timestamp Ordering

Timestamp ordering is a concurrency control technique used in distributed systems to ensure the consistency of transactions. It is a method of serializing transactions based on their timestamps, which are assigned when the transaction is initiated.

Here are some key points to note about timestamp ordering:

1. Each transaction is assigned a unique timestamp when it is initiated. This timestamp is used to determine the order in which transactions are executed.

2. Transactions are executed in the order of their timestamps. This means that a transaction with an earlier timestamp will be executed before a transaction with a later timestamp.

3. If two transactions have the same timestamp, a tie-breaking mechanism is used to determine their order of execution.

4. Timestamp ordering ensures that conflicting operations are executed in the order of their timestamps. This means that if two transactions have conflicting operations, the transaction with the earlier timestamp will be executed first.

5. Timestamp ordering can be implemented using a centralized or decentralized approach. In a centralized approach, a single entity is responsible for assigning timestamps and ensuring that transactions are executed in the correct order. In a decentralized approach, each node in the distributed system is responsible for assigning timestamps and ensuring the correct order of execution.

6. Timestamp ordering can help to prevent conflicts and ensure the consistency of transactions in a distributed system. However, it can also lead to increased waiting times and reduced concurrency if not implemented correctly.

Overall, timestamp ordering is an important technique for ensuring the consistency of transactions in a distributed system. It is important to carefully consider the design and implementation of timestamp ordering to ensure that it is effective and efficient.



### Comparison of methods for concurrency control

Concurrency control is the process of managing simultaneous access to a shared resource in a distributed system. There are several methods for concurrency control, including:

1. **Locking**: This method involves placing locks on the shared resource to prevent multiple transactions from accessing it simultaneously. Locks can be shared or exclusive, and can be placed at different levels of granularity.

2. **Timestamp ordering**: This method assigns a unique timestamp to each transaction and uses these timestamps to determine the order in which transactions are allowed to access the shared resource.

3. **Optimistic concurrency control**: This method assumes that conflicts between transactions are rare and allows multiple transactions to access the shared resource simultaneously. If a conflict is detected, one of the transactions is rolled back and restarted.

4. **Multiversion concurrency control**: This method maintains multiple versions of the shared resource and allows transactions to access the version that was current at the time the transaction started.

Each of these methods has its own advantages and disadvantages, and the choice of method depends on the specific requirements of the distributed system. For example, locking can provide strong consistency guarantees, but can also result in reduced concurrency and increased waiting times for transactions. On the other hand, optimistic concurrency control can provide high levels of concurrency, but may result in increased overhead due to the need to detect and resolve conflicts.



## Unit 9 - Distributed Transactions

1. **Introduction:** A distributed transaction is a transaction that spans multiple systems or databases. It ensures that either all the changes are committed or none of them are, even if the systems are distributed across different locations.

2. **Two-Phase Commit Protocol:** The two-phase commit protocol is a distributed algorithm that coordinates all the processes that participate in a distributed transaction to either commit or abort the transaction. The protocol has two phases: the prepare phase and the commit phase.

3. **Three-Phase Commit Protocol:** The three-phase commit protocol is an extension of the two-phase commit protocol that introduces an additional phase, the pre-commit phase, to make the protocol more resilient to failures.

4. **Global Transaction Identifier:** A global transaction identifier is a unique identifier that is assigned to a distributed transaction. It is used to track the progress of the transaction across all the systems that participate in the transaction.

5. **Transaction Manager:** A transaction manager is a component that coordinates the execution of distributed transactions. It is responsible for managing the communication between the different systems that participate in the transaction and for ensuring that the transaction is executed atomically.

6. **Distributed Deadlocks:** A distributed deadlock is a situation where two or more transactions are waiting for each other to release locks on resources, but none of them can proceed because the locks are held by the other transactions. Distributed deadlocks can be detected and resolved using various algorithms, such as the wait-for graph algorithm.

7. **Distributed Concurrency Control:** Distributed concurrency control is the process of managing concurrent access to data in a distributed system. It ensures that transactions are executed in a way that preserves the consistency of the data, even if the transactions are executed concurrently on different systems.

8. **Conclusion:** Distributed transactions are an important concept in distributed systems, as they allow multiple systems to participate in a single transaction and ensure that the transaction is executed atomically. Various protocols and algorithms, such as the two-phase commit protocol and the wait-for graph algorithm, can be used to manage distributed transactions and ensure their correctness.



### Flat and Nested Distributed Transactions

Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

- A distributed transaction is a transaction that spans multiple systems or resources.
- Flat distributed transactions involve a single coordinator that manages the transaction across all the involved resources.
- Nested distributed transactions, on the other hand, involve multiple coordinators, each managing a subset of the resources involved in the transaction.
- In a nested distributed transaction, the top-level coordinator is responsible for coordinating the commit or rollback of the entire transaction, while the lower-level coordinators are responsible for managing the commit or rollback of their respective sub-transactions.
- Nested distributed transactions can provide increased flexibility and performance compared to flat distributed transactions, as they allow for more fine-grained control over the transaction and can reduce the amount of coordination required.
- However, nested distributed transactions can also be more complex to implement and manage, as they require additional coordination and communication between the different coordinators.



### Atomic Commit protocols

Atomic Commit protocols are used in distributed systems to ensure that a transaction is either committed on all sites or aborted on all sites. This is important to maintain the consistency of data across all sites in a distributed system.

There are two main types of atomic commit protocols:

1. Two-phase commit (2PC)
2. Three-phase commit (3PC)

#### Two-phase commit (2PC)

The two-phase commit protocol is a distributed algorithm that coordinates all the processes that participate in a distributed atomic transaction on whether to commit or abort the transaction. The protocol is initiated by the coordinator after the last step of the transaction has been reached.

The first phase of the protocol is the voting phase. In this phase, the coordinator sends a query to commit message to all participants and waits for their response. Each participant replies with either a yes or no vote, depending on whether it is ready to commit the transaction.

In the second phase, the decision phase, the coordinator makes a decision based on the votes received from the participants. If all participants voted yes, the coordinator sends a global commit message to all participants. If any participant voted no, the coordinator sends a global abort message to all participants.

#### Three-phase commit (3PC)

The three-phase commit protocol is an extension of the two-phase commit protocol that introduces an additional phase to make the protocol more resilient to failures. The additional phase is called the pre-commit phase.

In the pre-commit phase, the coordinator sends a pre-commit message to all participants after receiving all yes votes in the voting phase. The participants acknowledge the receipt of the pre-commit message by sending an acknowledgement to the coordinator.

In the commit phase, the coordinator sends a do-commit message to all participants after receiving all acknowledgements. The participants then commit the transaction and send an acknowledgement to the coordinator.

In the abort phase, the coordinator sends an abort message to all participants if it does not receive all acknowledgements in the pre-commit phase or if any participant voted no in the voting phase. The participants then abort the transaction.

These are the basics of Atomic Commit protocols in distributed systems. They are an important part of ensuring the consistency of data across all sites in a distributed system.



### Concurrency control in distributed transactions

Concurrency control in distributed transactions refers to the mechanism used to synchronize distributed transactions in such a way that the ACID properties are not violated by their interleaved execution. These transactions are performed in a distributed database system where relevant data is hosted by a group of linked data servers.

There are several approaches to achieving concurrency control in distributed transactions, including:

1. **Locking-based concurrency control protocols**: These protocols use the concept of locking data to prevent multiple transactions from accessing the same data simultaneously.
2. **Timestamp-based concurrency control algorithms**: These algorithms use a transaction’s timestamp to determine the order in which transactions should be executed.
3. **Optimistic concurrency control**: This approach assumes that conflicts between transactions are rare and allows transactions to execute concurrently. Conflicts are detected at commit time, and the transaction is rolled back if a conflict is detected.

One example of a distributed transaction control protocol is 2PC*, which is an optimized protocol based on the traditional 2PC. It can extract more concurrent processing capabilities under high-intensity competitive workloads than previous approaches for a multi-microservice.



### Distributed Deadlocks

Distributed deadlocks can occur in a distributed system when distributed transactions or concurrency control is being used. In this context, a deadlock refers to a situation where two or more transactions are blocked and unable to proceed because they are waiting for each other to release resources.

Some key points to consider when studying distributed deadlocks include:

1. **Detection**: Detecting distributed deadlocks can be more challenging than detecting deadlocks in a centralized system. This is because the information about resource usage and transaction dependencies is spread across multiple nodes in the system.

2. **Prevention**: One way to prevent distributed deadlocks is to use a deadlock prevention protocol. These protocols are designed to ensure that deadlocks cannot occur by imposing restrictions on how transactions can acquire resources.

3. **Resolution**: If a distributed deadlock does occur, it must be resolved in order to allow the blocked transactions to proceed. This can be done by aborting one or more of the transactions involved in the deadlock, and then restarting them.

4. **Algorithms**: There are several algorithms that can be used for distributed deadlock detection and resolution. These include edge-chasing algorithms, probe-based algorithms, and global state detection algorithms.

Overall, distributed deadlocks are an important topic to understand when studying distributed transactions in a distributed system. By understanding how deadlocks can occur and how they can be detected, prevented, and resolved, you can design more robust distributed systems that are able to handle the challenges of distributed transactions and concurrency control.



### Transaction Recovery

Transaction recovery is a crucial component of distributed transactions in distributed systems. Here are some key points to consider:

1. Transaction recovery is the process of restoring a distributed system to a consistent state after a failure.
2. This is achieved by undoing or redoing the effects of transactions that were in progress at the time of the failure.
3. Recovery techniques are based on the use of logs, which record the changes made by transactions.
4. The two main approaches to transaction recovery are forward recovery and backward recovery.
5. Forward recovery involves redoing the effects of committed transactions and completing the effects of in-progress transactions.
6. Backward recovery involves undoing the effects of in-progress transactions and restoring the system to a previous consistent state.
7. The choice of recovery technique depends on factors such as the nature of the failure, the availability of backup data, and the performance requirements of the system.




## Unit 10 - Replication

Replication is the process of creating an exact copy of something. In the context of biology, replication refers to the process by which DNA is copied. This process is essential for cell division, as each new cell must contain an exact copy of the genetic material present in the parent cell.

1. DNA replication is a semi-conservative process, meaning that each new DNA molecule consists of one strand from the original DNA molecule and one newly synthesized strand.
2. The process of DNA replication begins at specific locations on the DNA molecule called origins of replication.
3. The two strands of the DNA molecule are separated by an enzyme called helicase, which breaks the hydrogen bonds between the base pairs.
4. Once the strands are separated, an enzyme called primase adds a short RNA primer to the template strand.
5. The enzyme DNA polymerase then adds nucleotides to the template strand, using the primer as a starting point.
6. As the replication fork moves along the DNA molecule, the leading strand is synthesized continuously, while the lagging strand is synthesized in short, discontinuous segments called Okazaki fragments.
7. The RNA primers are eventually removed and replaced with DNA by the enzyme DNA polymerase, and the Okazaki fragments are joined together by the enzyme DNA ligase to form a continuous strand.

In summary, replication is a complex process that involves the coordinated action of multiple enzymes and proteins to ensure the accurate copying of genetic information. It is essential for the growth and development of all living organisms.



### System Model and Group Communication

#### System Model
A system model is a representation of the components and interactions within a distributed system. It is used to describe the behavior and properties of the system, and to reason about its correctness and performance.

#### Group Communication
Group communication is a mechanism for exchanging messages among a group of processes in a distributed system. It is used to implement replication, fault tolerance, and other distributed algorithms.

#### Replication
Replication is the process of creating and maintaining multiple copies of data or services in a distributed system. It is used to improve availability, reliability, and performance.

#### Replication Techniques
There are several techniques for implementing replication in a distributed system, including:
- Primary-backup replication: One copy of the data is designated as the primary, and all updates are applied to it first. The updates are then propagated to the backup copies.
- Active replication: All copies of the data are updated simultaneously, using a group communication protocol to ensure consistency.
- Lazy replication: Updates are applied to one copy of the data, and propagated to the other copies at a later time.

#### Consistency Models
Different replication techniques provide different levels of consistency, which is the degree to which the copies of the data agree with each other. Some common consistency models include:
- Strict consistency: All copies of the data are always identical.
- Sequential consistency: All copies of the data are identical, but updates may be applied in a different order on different copies.
- Eventual consistency: The copies of the data may temporarily diverge, but will eventually become identical.

#### Group Communication Protocols
Group communication protocols are used to implement group communication and replication in a distributed system. Some common group communication protocols include:
- Atomic broadcast: A message is delivered to all members of the group, or to none of them.
- Reliable multicast: A message is delivered to all members of the group, even if some members fail.
- Total order broadcast: Messages are delivered to all members of the group in the same order.




### Fault-tolerant services

Fault-tolerant services are an essential component of distributed systems, as they ensure that the system can continue to function even in the presence of failures. In the context of replication, fault tolerance is achieved by maintaining multiple copies of data and services across different nodes in the system. This allows the system to continue to operate even if one or more nodes fail.

Some key points to consider when designing fault-tolerant services in a distributed system include:

1. **Redundancy**: Redundancy is the practice of maintaining multiple copies of data and services to ensure that the system can continue to operate even if one or more nodes fail. This can be achieved through techniques such as data replication and service replication.

2. **Failure detection**: In order to recover from failures, the system must be able to detect when a node has failed. This can be achieved through techniques such as heartbeats, which involve sending periodic messages between nodes to check if they are still operational.

3. **Failure recovery**: Once a failure has been detected, the system must be able to recover from it. This can involve techniques such as failover, where a backup node takes over the responsibilities of the failed node, or data recovery, where lost data is restored from a backup.

4. **Consistency**: In a distributed system, it is important to ensure that all nodes have a consistent view of the data. This can be achieved through techniques such as consensus algorithms, which ensure that all nodes agree on the state of the system.

Overall, fault-tolerant services are an essential component of distributed systems, as they ensure that the system can continue to operate even in the presence of failures. By incorporating techniques such as redundancy, failure detection, failure recovery, and consistency, it is possible to design a distributed system that is resilient to failures and can continue to provide reliable service to its users.



### Highly Available Services

Highly available services are an important aspect of distributed systems, particularly in the context of replication. In Unit 10 of the subject of Distributed Systems, we will be discussing the following points related to highly available services:

1. **Definition:** Highly available services refer to systems that are designed to ensure that they are accessible and operational for as close to 100% of the time as possible. This means that the system is able to continue functioning even in the event of failures or disruptions.

2. **Importance:** Highly availability is important for many applications, particularly those that are critical to the functioning of an organization or that have a large user base. For example, an online banking system must be highly available to ensure that customers can access their accounts and perform transactions at any time.

3. **Techniques:** There are several techniques that can be used to achieve high availability in distributed systems. These include replication, load balancing, and failover. Replication involves creating multiple copies of data or services and distributing them across different nodes in the system. Load balancing involves distributing incoming requests across multiple nodes to ensure that no single node becomes overloaded. Failover involves automatically switching to a backup system in the event of a failure.

4. **Challenges:** Achieving high availability in distributed systems can be challenging due to the complexity of these systems and the potential for failures and disruptions. Some of the challenges that must be addressed include ensuring data consistency, handling network partitions, and managing system upgrades and maintenance.

Overall, highly available services are an essential component of distributed systems, and there are many techniques and strategies that can be used to achieve high availability. By understanding these techniques and the challenges involved, we can design and implement distributed systems that are able to provide reliable and consistent services to users.



### Transactions with Replicated Data

In a distributed system, data may be replicated across multiple nodes to improve availability, fault tolerance, and performance. However, managing transactions with replicated data can be challenging. Here are some key points to consider:

1. **Consistency**: When data is replicated, it is important to ensure that all copies of the data remain consistent with each other. This can be achieved through various consistency models, such as strong consistency, eventual consistency, or causal consistency.

2. **Concurrency control**: When multiple transactions are accessing and modifying replicated data concurrently, a concurrency control mechanism is needed to ensure that the transactions do not interfere with each other. This can be achieved through techniques such as locking, timestamp ordering, or optimistic concurrency control.

3. **Commit protocols**: When a transaction modifies replicated data, a commit protocol is needed to ensure that the changes are applied atomically to all copies of the data. Two-phase commit (2PC) and three-phase commit (3PC) are commonly used commit protocols for distributed transactions.

4. **Failure handling**: In a distributed system, node failures are inevitable. When a node fails, the system must be able to recover and continue processing transactions. This can be achieved through techniques such as replication, logging, and checkpointing.

These are some of the key considerations when managing transactions with replicated data in a distributed system. It is important to carefully design and implement these mechanisms to ensure the correctness and reliability of the system.

