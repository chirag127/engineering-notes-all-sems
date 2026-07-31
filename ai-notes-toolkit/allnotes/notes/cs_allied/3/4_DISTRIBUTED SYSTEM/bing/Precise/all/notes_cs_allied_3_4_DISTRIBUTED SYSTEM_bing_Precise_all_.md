

# Distributed System

A distributed system is a computing environment in which various components are spread across multiple computers (or other computing devices) on a network. These devices split up the work, coordinating their efforts to complete the job more efficiently than if a single device had been responsible for the task.

Some of the most common examples of distributed systems include:
- Telecommunications networks (including cellular networks and the fabric of the internet)
- Graphical and video-rendering systems
- Scientific computing, such as protein folding and genetic research
- Airline and hotel reservation systems.

A distributed system is any network structure that consists of autonomous computers that are connected using a distribution middleware. Distributed systems facilitate sharing different resources and capabilities, to provide users with a single and integrated coherent network. The opposite of a distributed system is a centralized system.

A distributed system is a collection of computer programs that utilize computational resources across multiple, separate computation nodes to achieve a common, shared goal. Distributed systems aim to remove bottlenecks or central points of failure from a system.

A distributed database is a database that is located over multiple servers and/or physical locations. The data can either be replicated or duplicated across systems. Most popular applications use a distributed database and need to be aware of the homogenous or heterogenous nature of the distributed database system.



## Unit 1 - Characterization of Distributed Systems

1. **Introduction:** A distributed system is a collection of independent computers that appear to the users of the system as a single computer. The computers in a distributed system communicate with each other through a network.

2. **Transparency:** One of the main goals of a distributed system is to achieve transparency. This means that the system should hide the fact that its processes and resources are physically distributed across multiple computers. There are several types of transparency, including location transparency, access transparency, and failure transparency.

3. **Scalability:** Another important characteristic of distributed systems is scalability. This means that the system should be able to accommodate an increasing number of users, processes, and resources without a decrease in performance. Scalability can be achieved through techniques such as load balancing and data partitioning.

4. **Concurrency:** In a distributed system, multiple processes may be executing simultaneously. This can lead to issues such as race conditions and deadlocks. To manage concurrency, distributed systems use synchronization mechanisms such as locks and semaphores.

5. **Fault Tolerance:** Distributed systems must be able to continue functioning even in the presence of failures. This is achieved through techniques such as replication and redundancy.

6. **Consistency:** In a distributed system, it is important to ensure that all copies of data are consistent. This can be achieved through techniques such as distributed transactions and consensus algorithms.

7. **Security:** Security is an important concern in distributed systems. The system must be able to protect against threats such as unauthorized access and data tampering. This can be achieved through techniques such as encryption and access control.



### Introduction for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

1. A distributed system is a collection of independent computers that appears to its users as a single coherent system.
2. The main goal of a distributed system is to make it easy for users and applications to access remote resources and to share them in a controlled and efficient manner.
3. Distributed systems can be characterized by several key properties, including concurrency, lack of a global clock, independent failures, and the need for coordination and communication among components.
4. The design of distributed systems must take into account issues such as transparency, scalability, fault tolerance, and security.
5. Distributed systems can be found in many different application domains, including telecommunications, scientific computing, and e-commerce.




# Examples of Distributed Systems

Distributed systems are systems in which components located on networked computers communicate and coordinate their actions by passing messages. Here are some examples of distributed systems:

1. **The World Wide Web:** The web is a distributed system that consists of millions of web servers and clients that communicate with each other using the HTTP protocol.

2. **Peer-to-Peer Networks:** Peer-to-peer networks are distributed systems in which nodes share resources and communicate directly with each other, rather than relying on a central server.

3. **Cloud Computing:** Cloud computing is a distributed system in which computing resources are provided as a service over the internet. Users can access these resources from anywhere in the world.

4. **Distributed Databases:** Distributed databases are databases in which data is stored across multiple computers, rather than on a single machine. This allows for faster access to data and improved scalability.

5. **Distributed File Systems:** Distributed file systems are file systems in which files are stored on multiple computers, rather than on a single machine. This allows for faster access to files and improved scalability.

6. **Distributed Computing:** Distributed computing is a field of computer science that studies distributed systems in which multiple computers work together to solve a common problem. Examples of distributed computing projects include SETI@home and Folding@home.

These are just a few examples of distributed systems. There are many other types of distributed systems, each with its own unique characteristics and challenges.



# Resource Sharing and the Web Challenges

Resource sharing is a fundamental concept in distributed systems, where multiple independent computers work together to achieve a common goal. The World Wide Web (Web) is a prime example of a distributed system that enables resource sharing on a global scale. However, there are several challenges associated with resource sharing and the Web, including:

1. **Scalability**: As the number of users and resources on the Web grows, it becomes increasingly difficult to ensure that the system can handle the load and provide a satisfactory user experience.

2. **Heterogeneity**: The Web is composed of a wide variety of devices, platforms, and technologies, which can make it difficult to ensure interoperability and seamless resource sharing.

3. **Security**: Sharing resources on the Web can expose them to various security threats, such as unauthorized access, data theft, and malware. Ensuring the security of shared resources is a major challenge.

4. **Reliability**: The Web is a complex and dynamic environment, and ensuring the reliability of shared resources can be difficult. This includes ensuring that resources are available when needed and that they provide accurate and consistent information.

5. **Consistency**: In a distributed system like the Web, ensuring consistency of shared resources can be challenging. This includes ensuring that all users see the same version of a resource and that updates to resources are propagated in a timely and reliable manner.

These challenges must be addressed in order to ensure effective resource sharing on the Web and in other distributed systems. Various techniques and technologies have been developed to address these challenges, including load balancing, replication, encryption, and consensus algorithms. However, there is still much work to be done in this area, and it remains an active area of research and development.



# Architectural models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

1. **Layered Architecture**: This model organizes the system into layers, where each layer provides services to the layer above it and uses the services of the layer below it. This model is commonly used in network protocols, where each layer corresponds to a different level of abstraction.

2. **Client-Server Architecture**: This model divides the system into two main components: clients and servers. Clients request services from servers, which process the requests and return the results. This model is commonly used in web applications, where the client is a web browser and the server is a web server.

3. **Peer-to-Peer Architecture**: This model is similar to the client-server model, but instead of having a central server, each node in the system can act as both a client and a server. This model is commonly used in file-sharing systems, where each node can share files with other nodes.

4. **Object-Oriented Architecture**: This model organizes the system into objects, where each object represents a real-world entity and has a well-defined interface for interacting with other objects. This model is commonly used in object-oriented programming languages, where objects are instances of classes.

5. **Service-Oriented Architecture**: This model organizes the system into services, where each service provides a specific functionality and has a well-defined interface for interacting with other services. This model is commonly used in distributed systems, where services can be located on different machines and communicate over a network.

6. **Event-Driven Architecture**: This model organizes the system into components that communicate by exchanging events. When an event occurs, the components that are interested in that event are notified and can react accordingly. This model is commonly used in graphical user interfaces, where user actions generate events that are handled by the system.

7. **Microservices Architecture**: This model organizes the system into small, independent services that communicate with each other using lightweight protocols. Each service is responsible for a specific business capability and can be developed and deployed independently of the other services. This model is commonly used in cloud-based systems, where services can be easily scaled and updated.



# Fundamental Models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

1. **Interaction Model**: This model describes the ways in which the components of a distributed system communicate and coordinate with each other. The two main types of interaction are message passing and shared memory.

2. **Failure Model**: This model describes the ways in which components of a distributed system can fail. The two main types of failure are crash failure and Byzantine failure.

3. **Security Model**: This model describes the ways in which a distributed system can be secured against malicious attacks. The two main types of security are access control and cryptographic security.

4. **Concurrency Model**: This model describes the ways in which multiple processes can execute concurrently in a distributed system. The two main types of concurrency are synchronization and mutual exclusion.

5. **Consistency Model**: This model describes the ways in which data can be kept consistent across multiple components of a distributed system. The two main types of consistency are strong consistency and eventual consistency.

These are the fundamental models that are used to characterize distributed systems. They provide a framework for understanding the behavior and properties of distributed systems, and for designing and implementing distributed systems.



### Theoretical Foundation for Distributed System

Unit 1 - Characterization of Distributed Systems

1. A distributed system is a collection of independent computers that appears to its users as a single coherent system.
2. The main goal of a distributed system is to make it easy for users and applications to access remote resources and to share data and processing power with other users.
3. Distributed systems can be characterized by several key properties, including concurrency, lack of a global clock, independent failures, and the need for coordination and communication between components.
4. Theoretical foundations for distributed systems include models for communication, computation, and coordination, as well as algorithms for achieving consensus, fault tolerance, and other important properties.
5. Some of the key challenges in designing and implementing distributed systems include dealing with heterogeneity, scalability, transparency, and security.




### Limitation of Distributed system

Distributed systems have several limitations that can affect their performance, reliability, and scalability. Here are some of the limitations of distributed systems:

1. **Network Dependence:** Distributed systems rely on the network to communicate and exchange data between different nodes. If the network is slow or unreliable, the performance of the distributed system can be affected.

2. **Complexity:** Distributed systems are inherently more complex than centralized systems. This complexity can make it difficult to design, implement, and maintain distributed systems.

3. **Consistency:** Ensuring consistency of data across different nodes in a distributed system can be challenging. This is because data can be updated simultaneously on different nodes, leading to conflicts and inconsistencies.

4. **Security:** Distributed systems can be more vulnerable to security threats than centralized systems. This is because there are more points of entry for attackers to exploit.

5. **Fault Tolerance:** Distributed systems must be designed to be fault-tolerant, meaning they can continue to operate even if one or more nodes fail. However, achieving fault tolerance can be challenging and can add to the complexity of the system.

These are some of the limitations of distributed systems that must be considered when designing and implementing such systems. Despite these limitations, distributed systems can provide many benefits, such as scalability, reliability, and flexibility. It is important to carefully weigh the benefits and limitations when deciding whether to use a distributed system.



# Absence of Global Clock

- In a distributed system, there is no global clock that all nodes can use to synchronize their actions.
- Each node has its own local clock, which may not be synchronized with the clocks of other nodes.
- This can lead to inconsistencies and conflicts when nodes try to coordinate their actions or share data.
- To address this issue, distributed systems use various synchronization algorithms and protocols to achieve a common notion of time among the nodes.
- Some common synchronization techniques include the use of logical clocks, vector clocks, and global time services.
- Despite these efforts, the absence of a global clock remains a fundamental challenge in the design and implementation of distributed systems.




### Shared Memory

Shared memory is a type of memory that can be accessed by multiple processes. It is used in distributed systems to enable communication and synchronization between processes. Here are some key points to remember about shared memory:

1. Shared memory is a form of inter-process communication (IPC) that allows multiple processes to access the same memory location.
2. It is a fast and efficient way to share data between processes, as it eliminates the need for data to be copied between processes.
3. Shared memory can be implemented using hardware or software mechanisms.
4. In hardware-based shared memory, the memory is physically shared between multiple processors. This is typically achieved using a shared memory bus or a cache-coherent non-uniform memory access (ccNUMA) architecture.
5. In software-based shared memory, the memory is not physically shared, but is instead made to appear as if it is shared using virtual memory techniques.
6. Shared memory can be used to implement various synchronization primitives, such as semaphores and mutexes, to coordinate access to shared data.
7. Shared memory can also be used to implement message passing, where processes communicate by writing messages to and reading messages from shared memory locations.
8. Shared memory can be challenging to use correctly, as it requires careful synchronization to avoid race conditions and other concurrency issues.




### Logical Clocks

Logical clocks are an essential concept in the characterization of distributed systems. Here are some key points to remember:

1. A logical clock is a mechanism for capturing the causal relationships between events in a distributed system.
2. Logical clocks are used to assign timestamps to events in a distributed system, which can be used to determine the order of events.
3. Logical clocks do not measure the actual time, but rather the relative order of events.
4. There are two main types of logical clocks: Lamport clocks and vector clocks.
5. Lamport clocks assign a unique timestamp to each event, based on the number of events that have occurred in the system.
6. Vector clocks assign a vector of timestamps to each event, where each element of the vector represents the number of events that have occurred at each process in the system.
7. Logical clocks can be used to solve problems such as mutual exclusion and deadlock detection in distributed systems.




### Lamport’s & vectors logical clocks

Lamport’s logical clocks and vector clocks are algorithms used for ordering events in a distributed system. These algorithms are important for understanding the behavior of distributed systems and for implementing distributed algorithms.

#### Lamport’s Logical Clocks:

- Lamport’s logical clocks are based on the idea of associating a logical timestamp with each event in a distributed system.
- The logical timestamp is an integer value that represents the relative order of events in the system.
- The logical clock of a process is incremented whenever an event occurs at that process.
- When a message is sent from one process to another, the sender includes its current logical clock value in the message.
- When a process receives a message, it updates its logical clock to be the maximum of its current value and the timestamp in the received message, and then increments its clock by one.
- This ensures that the logical clocks of all processes in the system are consistent with the happened-before relation.

#### Vector Clocks:

- Vector clocks are an extension of Lamport’s logical clocks that provide more information about the relative ordering of events.
- In a vector clock, each process maintains a vector of logical clocks, one for each process in the system.
- The vector clock of a process is updated whenever an event occurs at that process, or when a message is sent or received.
- When a process sends a message, it includes its entire vector clock in the message.
- When a process receives a message, it updates its vector clock by taking the element-wise maximum of its current vector clock and the vector clock in the received message.
- This allows processes to determine the causal relationship between any two events in the system.

These algorithms are important for understanding the behavior of distributed systems and for implementing distributed algorithms such as mutual exclusion, deadlock detection, and global snapshots. They provide a way to order events in a distributed system and to reason about the causal relationships between events.



# Concepts in Message Passing Systems

Message passing systems are a fundamental concept in distributed systems. They allow processes to communicate and synchronize their actions by exchanging messages. Here are some key concepts in message passing systems:

1. **Message**: A message is a unit of data that is sent from one process to another. It can contain any type of data and can be of any size.

2. **Send and Receive Operations**: The send operation is used to transmit a message from one process to another. The receive operation is used to receive a message that has been sent to a process.

3. **Blocking and Non-Blocking Operations**: A blocking send or receive operation will cause the process to wait until the operation is completed. A non-blocking send or receive operation will allow the process to continue executing while the operation is being performed.

4. **Point-to-Point and Collective Communication**: Point-to-point communication involves the exchange of messages between two processes. Collective communication involves the exchange of messages between a group of processes.

5. **Synchronous and Asynchronous Communication**: In synchronous communication, the sender and receiver must be synchronized in time. In asynchronous communication, the sender and receiver do not need to be synchronized in time.

6. **Buffering**: Buffering refers to the temporary storage of messages in a message passing system. It can be used to improve the performance of the system by reducing the number of messages that need to be transmitted.

7. **Deadlock**: Deadlock is a situation in which two or more processes are blocked, waiting for each other to release resources. It can occur in message passing systems when processes are waiting for messages that will never arrive.

These are some of the key concepts in message passing systems. Understanding these concepts is essential for the design and implementation of distributed systems.



### Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems in the Subject of Distributed System

- Causal order is a fundamental concept in distributed systems.
- It refers to the ordering of events in a distributed system based on their cause-and-effect relationships.
- In a distributed system, events can occur concurrently and independently on different nodes.
- Causal order ensures that the events that are causally related are delivered in the correct order to all nodes in the system.
- This is important for maintaining consistency and correctness in the system.
- Causal order can be achieved through various algorithms and protocols, such as vector clocks and Lamport timestamps.
- These algorithms and protocols help to track the causal relationships between events and ensure that they are delivered in the correct order.
- Causal order is essential for many applications in distributed systems, such as distributed databases, distributed file systems, and distributed consensus algorithms.
- Understanding and implementing causal order is an important aspect of designing and building distributed systems.



### Total Order

Total order is a concept in distributed systems that refers to the ordering of events across all processes in the system. It is a way to ensure that all processes in the system agree on the order in which events occur, even if the events are generated by different processes.

Here are some key points to remember about total order:

1. Total order is a stronger form of ordering than causal order. Causal order only requires that causally related events be ordered, while total order requires that all events be ordered.

2. Total order can be achieved through the use of a consensus algorithm, such as Paxos or Raft. These algorithms allow all processes in the system to agree on the order of events.

3. Total order is important for ensuring consistency in distributed systems. By agreeing on the order of events, all processes can have a consistent view of the system state.

4. Total order can be difficult to achieve in practice, due to the challenges of achieving consensus in a distributed system. However, many distributed systems use total order to ensure consistency and correctness.




### Total Causal Order

Total causal order is a concept in distributed systems that refers to the ordering of events in a system. It is a way to ensure that all processes in the system have a consistent view of the order in which events occur. Here are some key points to remember about total causal order:

1. Total causal order is achieved by using a logical clock to assign timestamps to events. These timestamps are used to order the events in the system.

2. The logical clock is updated whenever an event occurs, and the timestamp of an event is determined by the current value of the logical clock.

3. Total causal order ensures that if event A causally precedes event B, then the timestamp of event A will be less than the timestamp of event B.

4. Total causal order is important in distributed systems because it allows processes to agree on the order of events, even if the events occur at different times on different processes.

5. Total causal order is not the same as total order, which refers to a global ordering of all events in the system. Total causal order only concerns the ordering of causally related events.

6. Total causal order can be achieved using various algorithms, such as vector clocks or matrix clocks.

In summary, total causal order is a way to ensure that all processes in a distributed system have a consistent view of the order in which events occur. It is achieved by using a logical clock to assign timestamps to events, and it is an important concept in the design of distributed systems.



# Techniques for Message Ordering

In distributed systems, message ordering is an important aspect to ensure consistency and correctness of the system. There are several techniques for message ordering in distributed systems, including:

1. **FIFO (First-In-First-Out) Ordering**: This technique ensures that messages sent from one process to another are received in the order they were sent. This is achieved by attaching a sequence number to each message, and the receiving process buffers the messages until they can be delivered in order.

2. **Causal Ordering**: This technique ensures that messages that are causally related are delivered in the order of their causal relationship. This is achieved by attaching a vector timestamp to each message, and the receiving process buffers the messages until they can be delivered in the order of their causal relationship.

3. **Total Ordering**: This technique ensures that all messages are delivered in the same order to all processes. This is achieved by using a consensus algorithm to agree on the order of messages, and the receiving processes buffer the messages until they can be delivered in the agreed order.

4. **Partial Ordering**: This technique ensures that certain subsets of messages are delivered in a specific order, while other messages may be delivered in any order. This is achieved by attaching a partial order relation to the messages, and the receiving processes buffer the messages until they can be delivered in the specified partial order.

These are some of the common techniques for message ordering in distributed systems. Each technique has its own advantages and disadvantages, and the choice of technique depends on the specific requirements of the system.



### Causal ordering of messages

Causal ordering of messages is a concept in distributed systems that ensures that messages are delivered in a way that respects the cause-and-effect relationship between events.

Here are some key points to understand about causal ordering of messages:

1. Causal ordering is important in distributed systems because it helps to ensure that the system behaves in a predictable and consistent manner.

2. Causal ordering is achieved by enforcing certain rules on the order in which messages are delivered. For example, if event A causes event B, then any message related to event A must be delivered before any message related to event B.

3. There are several algorithms that can be used to implement causal ordering of messages in a distributed system. These algorithms typically involve attaching timestamps or other metadata to messages in order to determine the correct order of delivery.

4. Causal ordering is not the same as total ordering or FIFO ordering. Total ordering ensures that all messages are delivered in the same order to all recipients, while FIFO ordering ensures that messages are delivered in the order in which they were sent. Causal ordering, on the other hand, only ensures that messages are delivered in an order that respects the cause-and-effect relationship between events.

5. Causal ordering can be challenging to implement in practice, particularly in large and complex distributed systems. However, it is an important concept to understand when designing and building distributed systems. 




# Global State

- In a distributed system, the global state is the collection of the local states of all the processes and the state of the communication channels.
- The global state is used to determine the properties of the system, such as whether a computation has terminated or whether a message has been delivered.
- The global state is difficult to determine in a distributed system because the local states of the processes and the state of the communication channels can change rapidly and independently.
- One approach to determine the global state is to use a snapshot algorithm, which records the local states of the processes and the state of the communication channels at a certain point in time.
- Another approach is to use a consistent cut, which is a set of local states that are consistent with the causal order of events in the system.
- The global state can also be used to detect global predicates, which are conditions that must hold for the entire system.
- The global state is an important concept in the study of distributed systems, as it provides a way to reason about the behavior of the system as a whole.



### Termination Detection

Termination detection is an important problem in distributed systems. It refers to the process of determining when a distributed computation has completed. This is a non-trivial task in a distributed system, as the computation may involve multiple processes running on different machines, and the termination of one process does not necessarily imply the termination of the entire computation.

There are several approaches to termination detection in distributed systems, including:

1. **Counting messages:** In this approach, each process keeps track of the number of messages it has sent and received. When a process has sent and received the same number of messages, it knows that it has completed its part of the computation. When all processes have completed their part of the computation, the entire computation is considered to be terminated.

2. **Dijkstra-Scholten algorithm:** This is a well-known algorithm for termination detection in distributed systems. It is based on the idea of a "diffusing computation," where a computation is initiated by a single process and then spreads to other processes. The algorithm uses a control structure called a "dependency graph" to keep track of the progress of the computation and to determine when it has terminated.

3. **Snapshots:** Another approach to termination detection is to take a snapshot of the system at regular intervals. This snapshot captures the state of all processes and messages in the system. By analyzing the snapshot, it is possible to determine whether the computation has terminated.

Termination detection is an important problem in distributed systems, as it is necessary to ensure that all processes have completed their part of the computation before moving on to the next step. There are several approaches to solving this problem, each with its own advantages and disadvantages. It is important to choose the right approach for the specific distributed system and computation being performed.



## Unit 2 - Distributed Mutual Exclusion

Distributed mutual exclusion refers to the coordination of processes in a distributed system to ensure that only one process can access a shared resource at a time. This is necessary to prevent conflicts and ensure data consistency in the system.

There are several algorithms that can be used to achieve distributed mutual exclusion, including:

1. **Centralized Algorithm**: In this approach, a central coordinator is responsible for granting access to the shared resource. Processes send requests to the coordinator, which grants access to one process at a time.

2. **Distributed Algorithm**: In this approach, there is no central coordinator. Instead, processes communicate with each other to coordinate access to the shared resource. Examples of distributed algorithms include Ricart-Agrawala and Maekawa's algorithms.

3. **Token-based Algorithm**: In this approach, a token is passed between processes in the system. The process holding the token has the right to access the shared resource. Examples of token-based algorithms include Suzuki-Kasami and Raymond's algorithms.

Each of these algorithms has its own advantages and disadvantages, and the choice of algorithm depends on the specific requirements of the system. It is important to carefully evaluate the trade-offs between performance, scalability, and fault tolerance when selecting an algorithm for distributed mutual exclusion.



# Classification of Distributed Mutual Exclusion

Distributed mutual exclusion is a fundamental problem in distributed computing systems. It ensures that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner. In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion. Message passing is the sole means for implementing distributed mutual exclusion.

There are three basic approaches for implementing distributed mutual exclusion :

1. **Token-based approach**: A unique token (also known as the PRIVILEGE message) is shared among the sites. A site is allowed to enter its critical section if it possesses the token. Mutual exclusion is ensured because the token is unique .
2. **Non-token-based approach**: This approach does not use a unique token to ensure mutual exclusion.
3. **Quorum-based approach**: This approach uses a quorum (a subset of sites) to ensure mutual exclusion.

These are the prime classifications of distributed mutual exclusion algorithms.



### Requirement of Mutual Exclusion Theorem

Mutual exclusion is a fundamental concept in the field of distributed systems. It refers to the property that ensures that only one process can access a shared resource at a time. The mutual exclusion theorem is a formal statement of this property, and it is essential for the correct functioning of many distributed algorithms.

Here are some reasons why mutual exclusion is important in distributed systems:

1. **Consistency**: Mutual exclusion ensures that the shared resource remains in a consistent state, even when accessed by multiple processes simultaneously. This is important for maintaining the integrity of the data stored in the resource.

2. **Concurrency**: Mutual exclusion allows multiple processes to access the shared resource concurrently, without interfering with each other. This can improve the performance of the system by allowing multiple processes to make progress simultaneously.

3. **Fault tolerance**: Mutual exclusion can help to improve the fault tolerance of a distributed system. By ensuring that only one process can access the shared resource at a time, mutual exclusion can prevent errors caused by concurrent access from propagating through the system.

In summary, the mutual exclusion theorem is an essential requirement for the correct functioning of many distributed algorithms. It ensures that shared resources remain consistent, allows for concurrent access, and improves the fault tolerance of the system.



# Unit 2 - Distributed Mutual Exclusion

## Token based and non token based algorithms

Distributed mutual exclusion is a fundamental problem in distributed systems. It refers to the problem of ensuring that, in a distributed system, only one process can access a shared resource at a time. There are two main approaches to solving this problem: token-based algorithms and non-token-based algorithms.

### Token-based algorithms

Token-based algorithms use a token to control access to the shared resource. The token is passed between processes in the system, and only the process that holds the token is allowed to access the shared resource. This approach has the advantage of being simple and easy to implement. However, it can suffer from performance issues, as the token must be passed between processes, which can take time.

Some examples of token-based algorithms include:
- The Ricart-Agrawala algorithm
- The Suzuki-Kasami algorithm
- The Raymond's tree-based algorithm

### Non-token-based algorithms

Non-token-based algorithms do not use a token to control access to the shared resource. Instead, they use other mechanisms, such as message passing or timestamps, to ensure that only one process can access the shared resource at a time. This approach can be more efficient than token-based algorithms, as it does not require the passing of a token between processes. However, it can be more complex to implement.

Some examples of non-token-based algorithms include:
- The Lamport's algorithm
- The Maekawa's algorithm
- The Carvalho-Roucairol algorithm

Both token-based and non-token-based algorithms have their advantages and disadvantages, and the choice of which approach to use will depend on the specific requirements of the distributed system in question. It is important to carefully evaluate the trade-offs between the two approaches before making a decision.



### Performance Metrics for Distributed Mutual Exclusion Algorithms

Distributed mutual exclusion algorithms are used to ensure that only one process can access a shared resource at a time in a distributed system. There are several performance metrics that can be used to evaluate the effectiveness of these algorithms:

1. **Message complexity:** This refers to the number of messages that must be exchanged between processes in order to grant a request for the shared resource. Lower message complexity is generally desirable, as it reduces the communication overhead and improves the overall performance of the system.

2. **Synchronization delay:** This is the time it takes for a process to gain access to the shared resource after making a request. A lower synchronization delay is desirable, as it means that processes can access the shared resource more quickly, improving the responsiveness of the system.

3. **Response time:** This is the time it takes for a process to complete its critical section (i.e., the section of code that accesses the shared resource) after making a request. A lower response time is desirable, as it means that processes can complete their work more quickly, improving the overall performance of the system.

4. **Fairness:** This refers to the degree to which the algorithm ensures that all processes have an equal opportunity to access the shared resource. An algorithm is considered fair if it prevents starvation, where one or more processes are perpetually denied access to the shared resource.

These are some of the key performance metrics that can be used to evaluate the effectiveness of distributed mutual exclusion algorithms. It is important to consider these metrics when designing and implementing such algorithms in order to ensure that they provide good performance and fairness in a distributed system.



## Unit 3 - Distributed Deadlock Detection

Distributed deadlock detection is the process of detecting deadlocks in a distributed system. A deadlock occurs when two or more processes are blocked, waiting for resources held by each other. In a distributed system, this can happen when processes on different nodes are involved.

1. **Deadlock detection algorithms**: There are several algorithms for detecting deadlocks in distributed systems, including the path-pushing algorithm, the edge-chasing algorithm, and the diffusing computation algorithm.

2. **Path-pushing algorithm**: In the path-pushing algorithm, each node maintains a wait-for graph, which represents the dependencies between processes. When a process is blocked, it sends a probe message to the node holding the resource it is waiting for. The probe message contains the path of nodes it has visited. If the probe message reaches a node that has already been visited, a deadlock is detected.

3. **Edge-chasing algorithm**: The edge-chasing algorithm is similar to the path-pushing algorithm, but instead of sending a probe message, each node sends a probe message to all of its outgoing edges in the wait-for graph. If a node receives a probe message from one of its incoming edges, it forwards the message to all of its outgoing edges. If a node receives a probe message from an edge that it has already sent a probe message to, a deadlock is detected.

4. **Diffusing computation algorithm**: In the diffusing computation algorithm, each node maintains a set of diffusing computations, which represent the dependencies between processes. When a process is blocked, it initiates a diffusing computation. The diffusing computation is propagated to all nodes in the system, and if a cycle is detected, a deadlock is detected.

5. **Deadlock resolution**: Once a deadlock is detected, it must be resolved. This can be done by aborting one or more of the processes involved in the deadlock, or by preempting resources from one or more of the processes.

6. **Challenges**: Detecting deadlocks in a distributed system can be challenging due to the lack of global knowledge and the need for coordination between nodes. Additionally, the detection and resolution of deadlocks can introduce additional overhead and complexity into the system.



# System Model for Distributed Deadlock Detection

In the context of distributed systems, a deadlock refers to a situation where two or more processes are blocked and unable to proceed because they are waiting for resources held by other processes. Distributed deadlock detection is the process of detecting and resolving deadlocks in a distributed system.

Here are some key points to consider when studying the system model for distributed deadlock detection:

1. **Resources**: In a distributed system, resources can be located on different nodes and can be shared by multiple processes. Resources can be physical, such as memory or disk space, or logical, such as a file or a database record.

2. **Process**: A process is an instance of a program that is executing on a node in the distributed system. Processes can request, hold, and release resources.

3. **Wait-for graph**: A wait-for graph is a directed graph that represents the dependencies between processes and resources in a distributed system. Nodes in the graph represent processes and resources, and edges represent the relationships between them. An edge from a process to a resource indicates that the process is waiting for the resource, while an edge from a resource to a process indicates that the resource is held by the process.

4. **Deadlock detection algorithms**: There are several algorithms that can be used to detect deadlocks in a distributed system, including the centralized, hierarchical, and distributed algorithms. These algorithms use different approaches to construct and analyze the wait-for graph to identify cycles that represent deadlocks.

5. **Deadlock resolution**: Once a deadlock has been detected, it must be resolved to allow the blocked processes to proceed. Common approaches to resolving deadlocks include preemption, rollback, and killing one or more of the deadlocked processes.

This is a brief overview of the system model for distributed deadlock detection. It is important to understand these concepts when studying distributed systems and how to detect and resolve deadlocks in such systems.



# Resource Vs Communication Deadlocks

## Unit 3 - Distributed Deadlock Detection

### Resource Deadlocks
- Resource deadlocks occur when two or more processes are blocked and waiting for resources held by the other processes.
- In a distributed system, resource deadlocks can occur when processes on different nodes request and hold resources on other nodes.
- Detection and resolution of resource deadlocks in a distributed system can be challenging due to the lack of a global view of the system.

### Communication Deadlocks
- Communication deadlocks occur when two or more processes are blocked and waiting for messages from the other processes.
- In a distributed system, communication deadlocks can occur when processes on different nodes are waiting for messages from each other.
- Detection and resolution of communication deadlocks in a distributed system can be challenging due to the lack of a global view of the system.

### Comparison
- Both resource and communication deadlocks can occur in a distributed system and can be challenging to detect and resolve.
- Resource deadlocks involve the blocking of processes due to the unavailability of resources, while communication deadlocks involve the blocking of processes due to the unavailability of messages.
- The methods for detecting and resolving resource and communication deadlocks may differ, but both require coordination and communication between the nodes in the distributed system.



# Deadlock Prevention

Deadlock prevention is a technique used in distributed systems to avoid the occurrence of deadlocks. Deadlocks occur when two or more processes are blocked, waiting for resources held by each other. Deadlock prevention techniques aim to ensure that at least one of the four necessary conditions for a deadlock does not occur. These conditions are:

1. **Mutual exclusion**: A resource can only be held by one process at a time.
2. **Hold and wait**: A process holding a resource can request additional resources.
3. **No preemption**: Resources cannot be forcibly taken away from a process.
4. **Circular wait**: A circular chain of processes exists, where each process is waiting for a resource held by the next process in the chain.

To prevent deadlocks, one or more of these conditions must be negated. Some common techniques for deadlock prevention include:

- **Resource allocation**: Resources are allocated in a way that prevents circular waits. For example, resources can be numbered, and processes must request resources in increasing order of their numbers.
- **Preemption**: Resources can be forcibly taken away from a process if it is causing a deadlock. The process must then restart or roll back its operations.
- **Process ordering**: Processes are ordered in a way that prevents deadlocks. For example, processes can be assigned priorities, and lower-priority processes must wait for higher-priority processes to release resources before they can acquire them.

These techniques can be used individually or in combination to prevent deadlocks in distributed systems. It is important to carefully design and implement deadlock prevention techniques to ensure that they are effective and do not introduce additional problems or inefficiencies.



### Avoidance

In the context of distributed deadlock detection in distributed systems, avoidance refers to the techniques used to prevent deadlocks from occurring in the first place. Here are some key points to consider when studying avoidance as part of Unit 3 - Distributed Deadlock Detection:

1. **Resource allocation graph**: One common technique for deadlock avoidance is to use a resource allocation graph. This graph represents the allocation of resources to processes and can be used to detect potential deadlocks before they occur.

2. **Banker's algorithm**: Another technique for deadlock avoidance is the Banker's algorithm. This algorithm is used to determine if a resource allocation is safe, meaning that there is a sequence of resource allocation that will not result in a deadlock.

3. **Wait-for graph**: A wait-for graph is another tool that can be used for deadlock avoidance. This graph represents the dependencies between processes and can be used to detect cycles, which indicate the presence of a potential deadlock.

4. **Conservative resource allocation**: One way to avoid deadlocks is to use a conservative resource allocation strategy. This means that resources are only allocated to processes if it is certain that the allocation will not result in a deadlock.

5. **Process initiation denial**: Another technique for deadlock avoidance is to deny the initiation of new processes if it is determined that the initiation could result in a deadlock.

These are some of the key techniques used for deadlock avoidance in distributed systems. It is important to understand these techniques and how they can be applied in practice to prevent deadlocks from occurring.



# Unit 3 - Distributed Deadlock Detection

### Detection & Resolution

1. **Detection**: In a distributed system, deadlock detection is more complex than in a centralized system. This is because the resources and processes are distributed across multiple nodes, and there is no global state available to detect deadlocks. Several algorithms have been proposed for distributed deadlock detection, including edge-chasing, diffusing computation, and global state detection.

2. **Resolution**: Once a deadlock has been detected, it must be resolved. There are several methods for resolving deadlocks in a distributed system, including preemption, rollback, and killing one or more processes. The choice of method depends on the specific system and the nature of the deadlock.

3. **Edge-Chasing**: This algorithm uses a probe message that is sent from a blocked process to its dependent processes. If the probe message returns to the originating process, a deadlock has been detected.

4. **Diffusing Computation**: This algorithm uses a diffusing computation to detect deadlocks. Each process maintains a wait-for graph, and when a process becomes blocked, it initiates a diffusing computation to determine if a deadlock exists.

5. **Global State Detection**: This algorithm uses a global state detection approach to detect deadlocks. A global state is constructed by collecting local state information from each node, and then a global wait-for graph is constructed to detect deadlocks.

6. **Preemption**: This method involves taking a resource away from a process and giving it to another process to resolve the deadlock.

7. **Rollback**: This method involves rolling back one or more processes to a previous state to release resources and resolve the deadlock.

8. **Killing Processes**: This method involves killing one or more processes to release resources and resolve the deadlock. This is typically a last resort, as it can result in lost work and data.



# Centralized Deadlock Detection

Centralized deadlock detection is a method for detecting deadlocks in a distributed system. In this approach, a single designated node, called the coordinator, is responsible for detecting deadlocks. The following are the key points to note about centralized deadlock detection:

1. The coordinator maintains a global wait-for graph (WFG) that represents the dependencies between transactions in the system.
2. Each node in the system periodically sends information about its local wait-for graph to the coordinator.
3. The coordinator merges the local wait-for graphs to construct the global wait-for graph.
4. The coordinator then checks the global wait-for graph for cycles. If a cycle is detected, it indicates the presence of a deadlock.
5. The coordinator can then initiate a recovery procedure to resolve the deadlock, such as aborting one or more transactions involved in the deadlock.

Centralized deadlock detection has the advantage of being relatively simple to implement and understand. However, it has some drawbacks, such as the potential for the coordinator to become a bottleneck and the need for all nodes to periodically send information to the coordinator, which can generate a significant amount of network traffic. Additionally, if the coordinator fails, the entire deadlock detection mechanism is disrupted.




# Distributed Deadlock Detection

Distributed deadlocks can occur in distributed systems when distributed transactions or concurrency control are utilized. Deadlock detection in distributed systems seems to be the best approach to handle deadlocks in distributed systems. There are two basic issues that need to be addressed when handling deadlocks using the approach of deadlock detection: First, the detection of existing deadlocks and second, the resolution of detected deadlocks  .

Distributed deadlock detection algorithms can be divided into four classes: path-pushing, edge-chasing, diffusion computation, and global state detection . In the deadlock avoidance approach to distributed systems, a resource is granted to a process if the resulting global system is safe. Deadlock detection requires an examination of the status of the process-resources interaction for the presence of a deadlock condition. To resolve the deadlock, a deadlocked process has to be aborted .

The techniques of deadlock detection in the distributed system require the following: Progress – The method should be able to detect all the deadlocks in the system. Safety – The method should not detect false or phantom deadlocks. There are three approaches to detect deadlocks in distributed systems: constructing a global wait-for graph from local wait-for graphs at a deadlock detector, using a distributed algorithm like edge chasing, and phantom deadlocks  .




# Path Pushing Algorithms

Path pushing algorithms are a type of distributed deadlock detection algorithm used in distributed systems. These algorithms are used to detect deadlocks in a distributed system by maintaining a wait-for graph at each site in the system.

Here are some key points to remember about path pushing algorithms:

1. In a path pushing algorithm, each site maintains a local wait-for graph that represents the dependencies between transactions at that site.
2. When a transaction at a site is blocked, the site sends a probe message to the site that holds the resource the transaction is waiting for.
3. The probe message contains the blocked transaction's identifier and the identifier of the transaction that is holding the resource.
4. When a site receives a probe message, it adds an edge to its local wait-for graph representing the dependency between the two transactions.
5. If the site detects a cycle in its local wait-for graph, it initiates a global deadlock detection procedure to determine if a deadlock exists in the system.
6. If a deadlock is detected, one of the transactions involved in the deadlock is aborted to resolve the deadlock.




# Edge Chasing Algorithms

Edge chasing algorithms are used for distributed deadlock detection in distributed systems. These algorithms are also known as path-pushing algorithms. The basic idea behind edge chasing algorithms is to detect cycles in the wait-for graph of the distributed system.

Here are some key points to remember about edge chasing algorithms:

1. Edge chasing algorithms work by sending probe messages along the edges of the wait-for graph.
2. When a process receives a probe message, it checks if it is waiting for any other process. If it is, it forwards the probe message to the process it is waiting for.
3. If a process receives a probe message that it has already seen, it means that a cycle has been detected in the wait-for graph, indicating a deadlock.
4. Edge chasing algorithms can be classified into two types: diffusing computation and edge chasing.
5. In diffusing computation, the probe messages are sent along the edges of the wait-for graph in a breadth-first manner.
6. In edge chasing, the probe messages are sent along the edges of the wait-for graph in a depth-first manner.




## Unit 4 - Agreement Protocols

Agreement protocols are a class of protocols used in distributed systems to ensure that all nodes in the system agree on a common value or decision. These protocols are essential for the correct functioning of distributed systems, as they allow nodes to reach a consensus despite the presence of faults or failures.

Some key points to remember about agreement protocols are:

1. Agreement protocols are used to ensure that all nodes in a distributed system agree on a common value or decision.
2. These protocols are essential for the correct functioning of distributed systems.
3. Agreement protocols allow nodes to reach a consensus despite the presence of faults or failures.
4. There are several types of agreement protocols, including two-phase commit, three-phase commit, and Paxos.
5. The choice of agreement protocol depends on the specific requirements of the distributed system, such as the level of fault tolerance required.



### Introduction for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

1. Agreement protocols are used in distributed systems to ensure that all nodes in the system reach a consensus on a particular value or decision.
2. These protocols are important for maintaining consistency and reliability in distributed systems, especially in the presence of failures or unreliable communication.
3. Some common agreement problems in distributed systems include consensus, atomic commitment, and leader election.
4. There are several algorithms and approaches for solving these problems, including Paxos, Raft, and Two-Phase Commit.
5. These protocols typically involve multiple rounds of communication between nodes and may require a majority or all nodes to participate in the decision-making process.
6. The choice of agreement protocol can depend on factors such as the size of the system, the reliability of communication, and the desired level of fault tolerance.
7. Understanding and implementing agreement protocols is a key aspect of designing and maintaining distributed systems.




### System Models for Unit 4 - Agreement Protocols in Distributed Systems

1. **Synchronous System Model**: In this model, there are known bounds on message transmission delays and the relative speeds of processes. This model is useful for designing algorithms with deterministic behavior.

2. **Asynchronous System Model**: In this model, there are no known bounds on message transmission delays or the relative speeds of processes. This model is more realistic and is used to design algorithms that can tolerate unpredictable behavior.

3. **Partially Synchronous System Model**: This model is a hybrid of the synchronous and asynchronous models. It assumes that the system is synchronous most of the time, but can occasionally behave asynchronously.

4. **Failure Models**: These models describe the types of failures that can occur in a distributed system. Common failure models include crash failures, omission failures, and Byzantine failures.

5. **Communication Models**: These models describe the ways in which processes in a distributed system can communicate with each other. Common communication models include message passing, shared memory, and remote procedure calls.

6. **Consistency Models**: These models describe the ways in which data can be kept consistent across multiple processes in a distributed system. Common consistency models include sequential consistency, causal consistency, and eventual consistency.

These system models are important for understanding the behavior of distributed systems and for designing algorithms that can operate correctly in the presence of failures and unpredictable behavior. They provide a framework for reasoning about the correctness of distributed algorithms and for analyzing their performance.



# Classification of Agreement Problem

In the context of distributed systems, an agreement problem refers to the challenge of getting multiple processes to agree on a single value. Agreement problems are a fundamental issue in distributed systems and are studied in the subject of agreement protocols in Unit 4.

There are several types of agreement problems, including:

1. **Consensus**: In this problem, all processes must agree on a single value, which must be proposed by one of the processes. This problem is also known as the Byzantine Generals Problem.

2. **Interactive consistency**: In this problem, each process has an initial value, and all processes must agree on a vector of values, where the i-th value is the initial value of the i-th process.

3. **Atomic Commit**: In this problem, all processes must agree on whether to commit or abort a transaction.

4. **Non-blocking Atomic Commit**: This is a variant of the atomic commit problem, where processes must agree on whether to commit or abort a transaction, but the decision must be made even if some processes fail.

These are some of the main types of agreement problems studied in distributed systems. Each type of problem has its own set of challenges and solutions, and understanding these problems is essential for designing robust and reliable distributed systems.



# Byzantine Agreement Problem

The Byzantine agreement problem is one of the fundamental problems in fault-tolerant distributed computing. It was first defined by Lamport, who also provided the first solution under the situation of processor failure . The problem requires a set of parties in a distributed environment to agree on a value even if some of the parties are corrupted .

According to the concept of Byzantine agreement problem, a source processor is taken to broadcast its initial value to another processor in the system . The problem of obtaining Byzantine consensus was conceived and formalized by Robert Shostak, who dubbed it the interactive consistency problem. This work was done in 1978 in the context of the NASA-sponsored SIFT project in the Computer Science Lab at SRI International .

To solve the Byzantine Generals problem, loyal generals need a secure way to come to agreement on a plan (known as consensus) and carry out their chosen plan (known as coordination) . While actually solving the Byzantine Generals Problem is quite complex, we now understand the fundamental challenge .



### Consensus problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

The consensus problem is a fundamental problem in distributed computing. It involves a group of processes (or agents) that must agree on a single value, based on their individual inputs. The problem is complicated by the fact that some of the processes may fail or be unreliable.

Some key points to consider when studying the consensus problem in the context of distributed systems are:

1. The consensus problem is a fundamental problem in distributed computing, where multiple processes must agree on a single value.
2. The problem is complicated by the fact that some of the processes may fail or be unreliable.
3. There are several algorithms and protocols that have been developed to solve the consensus problem, including Paxos, Raft, and Two-Phase Commit.
4. The consensus problem is closely related to other problems in distributed computing, such as leader election and atomic broadcast.
5. Solving the consensus problem is essential for ensuring the reliability and consistency of distributed systems.




# Interactive Consistency Problem

The interactive consistency problem is a fundamental problem in computer science and distributed systems. It was introduced by Pease, Shostak, and Lamport. The goal of distributed consensus is to reach an agreement in a distributed system in the presence of faults.

In the interactive consistency problem, every processor broadcasts its initial value to all other processors. The initial values of the processors may be different. A protocol for the interactive consistency problem should meet the following conditions:

1. **Agreement**: All non-faulty processors agree on the same vector (V1, V2, …, Vn).
2. **Validity**: If the ith processor is non-faulty and the initial value is Vi, then the ith value to be agreed on by all non-faulty processors must be Vi.

This problem is also known as the Byzantine Agreement Problem, where there are a total of n processes, at most m of which can be faulty. The communication medium is reliable and fully connected, and the receiver always knows the identity of the sender of a message. The system is synchronous, where in each round, a process receives messages, performs computation, and sends messages.



### Solution to Byzantine Agreement problem

The Byzantine Agreement problem, also known as the Byzantine Generals problem, is a fundamental challenge in distributed computing. It was first defined by Lamport, who also provided a solution under the situation of processor failure.

To solve the Byzantine Agreement problem, loyal generals need a secure way to come to agreement on a plan, known as consensus, and carry out their chosen plan, known as coordination. The solution to the Byzantine Generals Problem is quite complex and involves hashing, heavy computing work, and communication between all of the nodes (generals) to verify the message.

There are also other solutions to the Byzantine Agreement problem, such as the Quantum Solution presented by Matthias Fitzi, Nicolas Gisin, and Ueli Maurer.

In summary, the solution to the Byzantine Agreement problem involves secure communication and coordination between all nodes in a distributed system to achieve consensus and carry out a chosen plan. There are multiple approaches to solving this problem, and it remains an active area of research in distributed computing.



# Application of Agreement problem

The Agreement problem is a fundamental problem in distributed systems, where multiple processes need to agree on a single value. This problem arises in various scenarios, such as:

1. **Consensus**: In a distributed system, multiple processes need to agree on a single value, such as the result of a computation or the state of a shared resource. This is known as the consensus problem.

2. **Atomic Commit**: In a distributed database, multiple processes need to agree on whether to commit or abort a transaction. This is known as the atomic commit problem.

3. **Leader Election**: In a distributed system, multiple processes need to agree on a single process to act as the leader. This is known as the leader election problem.

4. **Byzantine Agreement**: In a distributed system, multiple processes need to agree on a single value, even in the presence of faulty processes that may send incorrect or conflicting information. This is known as the Byzantine agreement problem.

Agreement protocols are used to solve these problems in distributed systems. These protocols ensure that all processes in the system agree on a single value, even in the presence of failures or unreliable communication. Some common agreement protocols include Paxos, Raft, and Two-Phase Commit. These protocols are used in various applications, such as distributed databases, distributed file systems, and distributed consensus systems.



### Atomic Commit in Distributed Database System

An atomic commit is a fundamental concept in distributed database systems. It refers to the process of ensuring that a transaction is either completed in its entirety or not at all, even in the presence of failures. This is important for maintaining the consistency and integrity of the data in the distributed database.

Here are some key points to remember about atomic commit in distributed database systems:

1. Atomic commit is implemented using agreement protocols, which ensure that all participating nodes in the distributed database system agree on the outcome of the transaction.

2. Two-phase commit (2PC) is a commonly used agreement protocol for implementing atomic commit. In the first phase, the coordinator node sends a prepare message to all participating nodes, asking them to prepare to commit the transaction. In the second phase, the coordinator node sends a commit or abort message to all participating nodes, based on whether all nodes were able to prepare successfully.

3. Three-phase commit (3PC) is another agreement protocol that can be used to implement atomic commit. It adds an additional phase to the 2PC protocol, in which the coordinator node sends a pre-commit message to all participating nodes before sending the final commit or abort message.

4. Atomic commit is important for ensuring the ACID properties of transactions in distributed database systems. ACID stands for Atomicity, Consistency, Isolation, and Durability.

5. Atomic commit can be challenging to implement in distributed database systems due to the possibility of node failures, network partitions, and other issues. Various techniques, such as using timeouts and failure detectors, can be used to handle these challenges.




## Unit 5 - Distributed Resource Management

Distributed Resource Management refers to the process of managing resources in a distributed computing environment. This includes the allocation, scheduling, and coordination of resources such as processing power, memory, storage, and network bandwidth across multiple systems.

Some key concepts in Distributed Resource Management include:

1. **Resource allocation**: The process of assigning resources to tasks or processes based on their requirements and priorities.
2. **Scheduling**: The process of determining the order in which tasks or processes are executed, taking into account their resource requirements and dependencies.
3. **Load balancing**: The process of distributing workloads across multiple systems to optimize resource utilization and minimize response time.
4. **Fault tolerance**: The ability of a system to continue functioning in the event of a failure of one or more of its components.
5. **Scalability**: The ability of a system to handle increasing workloads by adding additional resources.

Distributed Resource Management is important in ensuring the efficient and effective use of resources in a distributed computing environment. It can help to improve system performance, reduce costs, and increase reliability and availability. There are various tools and techniques available for managing resources in a distributed environment, including cluster management software, resource allocation algorithms, and scheduling policies.



# Issues in Distributed File Systems

Distributed file systems are designed to provide transparent access to files stored on a network of computers. However, there are several issues that arise when implementing and managing a distributed file system. Some of these issues include:

1. **Consistency**: Ensuring that all copies of a file stored on different nodes in the system are consistent and up-to-date can be challenging, especially in the presence of concurrent updates.

2. **Availability**: In a distributed file system, files are stored on multiple nodes to improve availability. However, if one or more nodes fail, the system must be able to recover and continue to provide access to the files.

3. **Scalability**: As the number of nodes and the amount of data stored in the system grows, the system must be able to scale to handle the increased load.

4. **Security**: Ensuring the security of the data stored in a distributed file system is crucial. This includes protecting against unauthorized access, as well as ensuring the integrity of the data.

5. **Performance**: The performance of a distributed file system can be affected by factors such as network latency and the load on individual nodes. The system must be designed to provide acceptable performance under a wide range of conditions.

These are some of the key issues that must be addressed when designing and implementing a distributed file system. By carefully considering these issues and designing the system accordingly, it is possible to build a distributed file system that is reliable, scalable, and efficient.



# Mechanism for building distributed file systems

Distributed file systems are designed to provide shared access to files and data across a network of computers. Here are some key mechanisms for building distributed file systems:

1. **Data distribution:** One of the main challenges in building a distributed file system is deciding how to distribute data across multiple nodes. There are several approaches to this, including data striping, where data is split into blocks and distributed across multiple nodes, and data replication, where multiple copies of the data are stored on different nodes.

2. **Consistency:** Ensuring consistency of data across multiple nodes is another important mechanism in building a distributed file system. This can be achieved through techniques such as versioning, where each update to a file is assigned a unique version number, and conflict resolution, where conflicts between updates from different nodes are resolved.

3. **Fault tolerance:** Distributed file systems must be designed to be fault-tolerant, meaning that they can continue to operate even in the presence of failures. This can be achieved through mechanisms such as data replication, where multiple copies of data are stored on different nodes, and failure detection and recovery, where failed nodes are detected and their data is recovered from other nodes.

4. **Scalability:** As the number of nodes in a distributed file system increases, it is important to ensure that the system can scale to handle the increased load. This can be achieved through mechanisms such as distributed hash tables, where data is distributed across multiple nodes based on a hash function, and load balancing, where the load is distributed evenly across multiple nodes.

5. **Security:** Security is an important consideration in building a distributed file system, as data is being shared across multiple nodes. Mechanisms for ensuring security include encryption, where data is encrypted before being transmitted across the network, and access control, where access to data is restricted based on user permissions.

These are some of the key mechanisms for building distributed file systems. By implementing these mechanisms, it is possible to build a distributed file system that provides shared access to files and data across a network of computers.



# Design issues in Distributed Shared Memory

Distributed Shared Memory (DSM) is a mechanism that manages memory across multiple nodes and makes inter-process communications clear to end-users. To design a DSM system, certain issues must be addressed:

1. **Granularity**: Granularity refers to the block size of a DSM system. It is the unit of sharing and the level of detail at which the system maintains coherence.
2. **Structure of shared memory space**: Structure refers to the design of the shared data in the memory. The structure of the shared memory space affects the performance and scalability of the system.
3. **Memory coherence**: Memory coherence is the consistency of shared data across multiple nodes. It is important to ensure that all nodes have a consistent view of the shared data.
4. **Design choices**: Design choices include structure and granularity, coherence semantics, scalability, and heterogeneity.
5. **Implementation methods**: Implementation methods refer to the techniques used to implement the DSM system. These methods affect the performance and scalability of the system.

These are some of the key design issues that must be addressed when designing a DSM system. A well-designed DSM system can provide the ease-of-programming benefits of bus-based SMP systems with the scalability of MPP/Cluster message-passing systems.



### Algorithm for Implementation of Distributed Shared Memory

Distributed Shared Memory (DSM) is a system that allows multiple computers to share a single virtual memory space. This is achieved by implementing a software layer that manages the distribution of data across the network. Here is an algorithm for the implementation of DSM:

1. **Initialization**: The DSM system is initialized by creating a shared memory space that is accessible to all participating computers. This can be done by allocating a portion of each computer's physical memory to the shared space.

2. **Data Distribution**: The data in the shared memory space is distributed across the network using a data distribution algorithm. This can be done using techniques such as data replication, data partitioning, or a combination of both.

3. **Memory Access**: When a computer needs to access data in the shared memory space, it sends a request to the DSM system. The DSM system then determines the location of the data and retrieves it from the appropriate computer.

4. **Data Consistency**: To ensure data consistency, the DSM system must implement a consistency protocol. This can be done using techniques such as invalidation, update, or a combination of both.

5. **Fault Tolerance**: To ensure fault tolerance, the DSM system must implement a fault tolerance protocol. This can be done using techniques such as replication, checkpointing, or a combination of both.

This is a basic algorithm for the implementation of DSM. The specific details of the algorithm may vary depending on the requirements of the system and the specific implementation.



## Unit 6 - Failure Recovery in Distributed Systems

1. **Introduction:** In distributed systems, failure recovery is the process of restoring the system to a consistent state after a failure has occurred. This is important because failures are inevitable in any system, and the ability to recover from them is crucial for maintaining the availability and reliability of the system.

2. **Types of Failures:** There are several types of failures that can occur in a distributed system, including node failures, network failures, and Byzantine failures. Node failures occur when a single node in the system fails, while network failures occur when there is a problem with the communication between nodes. Byzantine failures are more complex and can involve nodes sending incorrect or conflicting information.

3. **Failure Detection:** In order to recover from a failure, the system must first be able to detect that a failure has occurred. This can be done through the use of heartbeat messages, timeouts, and other mechanisms that allow nodes to monitor the health of the system.

4. **Recovery Strategies:** There are several strategies that can be used to recover from a failure in a distributed system. These include checkpointing, replication, and rollback recovery. Checkpointing involves periodically saving the state of the system so that it can be restored in the event of a failure. Replication involves maintaining multiple copies of data or services so that if one fails, another can take over. Rollback recovery involves rolling back the system to a previous consistent state and replaying the operations that occurred since that state.

5. **Conclusion:** Failure recovery is an important aspect of distributed systems, as it allows the system to maintain its availability and reliability in the face of failures. There are several types of failures that can occur, and various strategies can be used to recover from them. Effective failure recovery requires careful design and implementation of the system, as well as ongoing monitoring and maintenance.



### Concepts in Backward and Forward recovery for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- **Backward recovery** is a technique used to restore the system to a consistent state after a failure has occurred. This is done by undoing the changes made by the failed transaction and restoring the system to its previous state.

- **Forward recovery** is a technique used to restore the system to a consistent state after a failure has occurred by redoing the changes made by the failed transaction. This is done by applying the changes made by the failed transaction to the system again.

- Both backward and forward recovery techniques are used to ensure the consistency and reliability of the system in the event of a failure.

- Backward recovery is also known as **rollback recovery**. It is commonly used in database systems where transactions are used to ensure the consistency of the data.

- Forward recovery is also known as **rollforward recovery**. It is commonly used in systems where the data is continuously updated and the changes made by the failed transaction are still valid.

- The choice between backward and forward recovery depends on the nature of the system and the type of failure that has occurred. In some cases, a combination of both techniques may be used to ensure the consistency and reliability of the system.

- In distributed systems, failure recovery is more complex due to the presence of multiple nodes and the need for coordination between them. Techniques such as **checkpointing** and **message logging** may be used to facilitate failure recovery in distributed systems.

- Checkpointing involves periodically saving the state of the system to a stable storage so that it can be restored in the event of a failure. Message logging involves recording the messages exchanged between the nodes in the system so that they can be replayed to restore the system to a consistent state after a failure.

- Failure recovery is an important aspect of distributed systems and various techniques and protocols have been developed to ensure the consistency and reliability of these systems in the event of a failure. Backward and forward recovery are two such techniques that are commonly used in distributed systems.



### Recovery in Concurrent Systems

Recovery in concurrent systems is an important aspect of failure recovery in distributed systems. Here are some key points to consider:

1. **Concurrency control** is necessary to ensure the consistency and correctness of data in a distributed system. This involves managing access to shared resources and preventing conflicts that may arise from concurrent operations.

2. **Failure recovery** is the process of restoring a system to a consistent state after a failure has occurred. This can involve rolling back transactions, restoring data from backups, and re-executing failed operations.

3. **Checkpointing** is a technique used to periodically save the state of a system, allowing it to recover more quickly in the event of a failure. This can involve saving the state of individual processes, as well as the state of shared resources.

4. **Logging** is used to record the history of operations performed in a system, allowing it to recover from failures by replaying the log and restoring the system to a consistent state.

5. **Recovery algorithms** are used to determine the appropriate actions to take in the event of a failure. These algorithms can vary depending on the type of failure that has occurred, and the specific requirements of the system.

6. **Distributed commit protocols** such as the two-phase commit protocol, are used to ensure that transactions are either committed or aborted consistently across all nodes in a distributed system.

7. **Redundancy** can be used to improve the resilience of a system, by replicating data and processes across multiple nodes. This allows the system to continue operating even if one or more nodes fail.

In summary, recovery in concurrent systems involves a combination of techniques and algorithms to ensure the consistency and correctness of data in the event of a failure. These techniques include concurrency control, checkpointing, logging, recovery algorithms, distributed commit protocols, and redundancy.



# Obtaining Consistent Checkpoints for the Notes of the Unit 6 - Failure Recovery in Distributed Systems in the Subject of DISTRIBUTED SYSTEM

1. **Introduction**: In distributed systems, failure recovery is an important aspect to ensure the system's reliability and availability. One of the techniques used for failure recovery is checkpointing, which involves saving the state of the system at regular intervals to enable recovery in case of failure.

2. **Consistent Checkpoints**: In order to ensure that the system can recover to a consistent state, it is important to obtain consistent checkpoints. This means that the checkpoints taken by different processes in the system must be coordinated to ensure that they represent a consistent global state.

3. **Checkpointing Protocols**: There are several protocols that can be used to obtain consistent checkpoints in distributed systems. These include the Chandy-Lamport algorithm, the coordinated checkpointing algorithm, and the communication-induced checkpointing algorithm.

4. **Chandy-Lamport Algorithm**: The Chandy-Lamport algorithm is a well-known algorithm for obtaining consistent checkpoints in distributed systems. It involves sending marker messages between processes to coordinate the taking of checkpoints.

5. **Coordinated Checkpointing Algorithm**: The coordinated checkpointing algorithm is another approach to obtaining consistent checkpoints in distributed systems. In this approach, a coordinator process is responsible for initiating the checkpointing process and coordinating the taking of checkpoints by the other processes.

6. **Communication-Induced Checkpointing Algorithm**: The communication-induced checkpointing algorithm is an approach that leverages the communication between processes to obtain consistent checkpoints. In this approach, processes take checkpoints based on the messages they receive from other processes.

7. **Conclusion**: Obtaining consistent checkpoints is an important aspect of failure recovery in distributed systems. There are several protocols that can be used to achieve this, including the Chandy-Lamport algorithm, the coordinated checkpointing algorithm, and the communication-induced checkpointing algorithm. These protocols provide different trade-offs in terms of complexity, performance, and overhead, and the choice of protocol will depend on the specific requirements of the system.



# Recovery in Distributed Database Systems

Recovery in distributed database systems is the process of restoring the database to a consistent state after a failure. Failures can occur due to various reasons such as hardware or software failures, communication failures, or site failures. Recovery strategies aim to maintain the atomicity and durability of distributed transactions.

1. **Soft Failures**: In case of soft failures that result in inconsistency of the database, the recovery strategy includes transaction undo or rollback. However, sometimes, transaction redo may also be adopted to recover to a consistent state of the transaction.

2. **Hard Failures**: In case of hard failures resulting in extensive damage to the database, recovery strategies encompass restoring a past copy of the database from archival backup.

3. **Distributed Recovery**: Distributed recovery is more complicated than centralized database recovery because failures can occur at the communication links or a remote site. Ideally, a recovery system should be simple, incur tolerable overhead, maintain system consistency, provide partial operability, and avoid global rollback.

4. **Transaction Recovery**: Transaction recovery is done to eliminate the adverse effects of faulty transactions rather than to recover from a failure. Faulty transactions include all transactions that have changed the database into an undesired state and the transactions that have used values written by the faulty transactions.




## Unit 7 - Fault Tolerance

Fault tolerance is the ability of a system to continue functioning in the event of a failure. This can be achieved through various methods, including:

1. **Redundancy**: This involves having multiple components or systems that can take over in the event of a failure. For example, a system may have multiple power supplies, so that if one fails, the other can take over.

2. **Failover**: This is the process of switching to a backup system in the event of a failure. For example, a database may have a primary and secondary server, with the secondary server taking over if the primary server fails.

3. **Error Correction**: This involves detecting and correcting errors in data. For example, a system may use error-correcting codes to detect and correct errors in data transmission.

4. **Recovery**: This involves restoring a system to a known good state after a failure. For example, a system may use backups to restore data after a failure.

Fault tolerance is an important consideration in the design of systems, particularly those that are mission-critical or that handle sensitive data. By incorporating fault tolerance into a system, designers can help ensure that the system continues to function even in the event of a failure.



# Issues in Fault Tolerance

Fault tolerance is the realization that we will have faults in our system (hardware and/or software) and we have to design the system in such a way that it will be tolerant of those faults. That is, it should compensate for the faults and continue to function.

Some of the issues in fault tolerance are:

1. **Partial failure**: A major difference between distributed systems and single machine systems is that with the former, partial failure is possible, i.e., when one component in a distributed system fails.
2. **Process resilience**: Techniques by which one or more processes can fail without seriously disturbing the rest of the system.
3. **Reliable multicasting**: To keep processes synchronized by which message transmission to a collection of processes is guaranteed to succeed.
4. **Error containment**: Fault tolerance consists of noticing active faults and component subsystem failures, and doing something helpful in response. One such helpful response is error containment, which is another close relative of modularity and the building of systems out of subsystems.
5. **Cost**: A fault tolerant system can be costly, as it requires the continuous operation and maintenance of additional, redundant components.




# Commit Protocols

Commit protocols are used in distributed systems to ensure that a transaction is either completed successfully on all sites or aborted on all sites. This is important for maintaining consistency in the system.

There are several types of commit protocols, including two-phase commit (2PC) and three-phase commit (3PC).

## Two-Phase Commit (2PC)

In the first phase of 2PC, the coordinator sends a prepare message to all participants, asking them to prepare to commit the transaction. The participants then respond with either a yes or no vote.

If all participants vote yes, the coordinator sends a commit message to all participants in the second phase. The participants then commit the transaction and send an acknowledgment to the coordinator.

If any participant votes no, the coordinator sends an abort message to all participants in the second phase. The participants then abort the transaction and send an acknowledgment to the coordinator.

## Three-Phase Commit (3PC)

3PC is similar to 2PC, but adds an additional phase to make the protocol more resilient to failures. In the first phase, the coordinator sends a canCommit message to all participants, asking if they can commit the transaction. The participants then respond with either a yes or no vote.

If all participants vote yes, the coordinator sends a preCommit message to all participants in the second phase. The participants then prepare to commit the transaction and send an acknowledgment to the coordinator.

In the third phase, the coordinator sends a doCommit message to all participants. The participants then commit the transaction and send an acknowledgment to the coordinator.

If any participant votes no in the first phase, or if the coordinator does not receive acknowledgments from all participants in the second phase, the coordinator sends an abort message to all participants. The participants then abort the transaction and send an acknowledgment to the coordinator.

These are the basic concepts of commit protocols in distributed systems. They are essential for ensuring consistency and fault tolerance in the system. It is important to understand these concepts when studying distributed systems.



# Voting Protocols

Voting protocols are used in distributed systems to achieve fault tolerance. They are used to ensure that the system can continue to function correctly even if some of its components fail. Here are some key points to remember about voting protocols:

1. **Redundancy**: Voting protocols rely on the principle of redundancy. This means that multiple copies of the same data are stored on different nodes in the system. If one node fails, the data can still be accessed from the other nodes.

2. **Majority Voting**: One common approach to voting is majority voting. In this approach, each node in the system casts a vote for the value of the data. The value that receives the majority of the votes is considered to be the correct value.

3. **Weighted Voting**: Another approach to voting is weighted voting. In this approach, each node is assigned a weight, and the value that receives the highest total weight is considered to be the correct value. This approach can be useful when some nodes are considered to be more reliable than others.

4. **Quorum-based Voting**: Quorum-based voting is another approach to voting in distributed systems. In this approach, a quorum is a subset of the nodes in the system. A read or write operation can only be performed if a quorum of nodes agrees on the value of the data.

5. **Byzantine Fault Tolerance**: Byzantine fault tolerance is a type of voting protocol that is designed to handle Byzantine faults. These are faults where a node may behave arbitrarily, including sending incorrect or conflicting information to other nodes. Byzantine fault tolerance protocols use complex algorithms to ensure that the system can continue to function correctly even in the presence of Byzantine faults.

These are some of the key points to remember about voting protocols in distributed systems. They are an important tool for achieving fault tolerance and ensuring that the system can continue to function correctly even in the presence of faults.



# Dynamic Voting Protocols

Dynamic voting protocols are used in distributed systems to achieve fault tolerance. They are a part of Unit 7 - Fault Tolerance in the subject of Distributed Systems. Here are some key points to note about dynamic voting protocols:

1. Dynamic voting protocols are used to ensure data consistency in the presence of failures.
2. They work by dynamically adjusting the number of votes required to perform an operation based on the current state of the system.
3. The number of votes required is determined by a quorum function, which takes into account factors such as the number of available replicas and the number of failed replicas.
4. Dynamic voting protocols can be used to implement both read and write operations.
5. They can be used in conjunction with other fault tolerance techniques, such as replication, to provide a high level of reliability and availability.




## Unit 8 - Transactions and Concurrency Control

1. **Transaction** - A transaction is a logical unit of work that comprises one or more database operations, such as retrieval, insertion, deletion, or updating of data. A transaction must be atomic, consistent, isolated, and durable (ACID).
2. **Concurrency Control** - Concurrency control is the process of managing simultaneous operations on a database without having them interfere with one another. It ensures that transactions are executed in a safe and consistent manner while maintaining transaction isolation.
3. **Locking** - Locking is a mechanism used to prevent multiple transactions from accessing the same data concurrently. Locks can be shared or exclusive, and can be applied at different levels of granularity, such as at the row, page, or table level.
4. **Two-Phase Locking (2PL)** - Two-phase locking is a concurrency control method that guarantees serializability. It is divided into two phases: the growing phase, where locks are acquired, and the shrinking phase, where locks are released.
5. **Deadlocks** - A deadlock occurs when two or more transactions are waiting for each other to release locks. Deadlock prevention and detection are two methods used to handle deadlocks.
6. **Timestamp Ordering** - Timestamp ordering is a concurrency control method that assigns a timestamp to each transaction and uses these timestamps to determine the order in which transactions are executed.
7. **Optimistic Concurrency Control** - Optimistic concurrency control is a concurrency control method that assumes that conflicts between transactions are rare and allows transactions to execute without acquiring locks. Conflicts are detected at commit time, and transactions are rolled back and restarted if necessary.




# Transactions

A transaction is a logical unit of work that comprises one or more database operations. These operations can include the reading, updating, inserting, or deleting of data in a database. Transactions are used to ensure that data remains consistent and correct, even in the event of system failures or errors.

Here are some key points to remember about transactions:

1. **Atomicity**: A transaction is atomic, meaning that it is either completed in its entirety or not at all. If a transaction fails at any point, all changes made during the transaction are rolled back to their previous state.

2. **Consistency**: Transactions ensure that the database remains in a consistent state. This means that the data in the database must satisfy a set of integrity constraints, such as unique key constraints and referential integrity constraints.

3. **Isolation**: Transactions are isolated from one another, meaning that the changes made by one transaction are not visible to other transactions until the first transaction is committed.

4. **Durability**: Once a transaction is committed, its changes are permanent and must survive any subsequent system failures.

In the context of distributed systems, transactions can become more complex due to the need to coordinate changes across multiple nodes. This is where concurrency control mechanisms, such as locking and timestamp ordering, come into play to ensure that transactions can be executed correctly and efficiently in a distributed environment.



### Nested Transactions

Nested transactions are a type of transaction that allows for sub-transactions within a larger transaction. This is useful in distributed systems where multiple operations may need to be performed as part of a single transaction.

Here are some key points to remember about nested transactions:

1. Nested transactions are a way to structure complex transactions into smaller, more manageable sub-transactions.
2. Each sub-transaction can be committed or aborted independently, allowing for more fine-grained control over the transaction as a whole.
3. If a sub-transaction is aborted, any changes made within that sub-transaction are rolled back, but the larger transaction can still continue.
4. Nested transactions can help to improve concurrency and reduce contention in distributed systems by allowing multiple sub-transactions to execute in parallel.
5. Nested transactions can also help to improve fault tolerance by allowing for partial rollback and recovery in the event of a failure.

Overall, nested transactions are a powerful tool for managing complex transactions in distributed systems. They provide a way to break down large transactions into smaller, more manageable pieces, while still maintaining the atomicity and consistency guarantees of a traditional transaction.



# Locks for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- Locks are a mechanism used to ensure that only one transaction can access a data item at a time.
- Locks can be shared or exclusive. Shared locks allow multiple transactions to read a data item simultaneously, while exclusive locks allow only one transaction to write to a data item.
- Locks can be applied at different levels of granularity, such as at the row, page, or table level.
- Locks can be acquired and released explicitly by the transaction, or they can be managed automatically by the database system.
- Deadlocks can occur when two or more transactions are waiting for each other to release locks. Deadlock detection and resolution techniques are used to handle this situation.
- Locks are an important part of concurrency control in distributed systems, as they help to ensure the consistency and correctness of data in the presence of concurrent transactions.



# Optimistic Concurrency Control

Optimistic Concurrency Control (OCC) is a method used in distributed systems to manage transactions and concurrency control. It is based on the assumption that conflicts between transactions are rare and that it is more efficient to allow transactions to execute concurrently and only check for conflicts at the end, rather than using locks to prevent conflicts from occurring.

Here are some key points to remember about Optimistic Concurrency Control:

1. OCC is based on the assumption that conflicts between transactions are rare.
2. Transactions are allowed to execute concurrently without acquiring locks.
3. Conflicts are detected at the end of the transaction, during the validation phase.
4. If a conflict is detected, the transaction is rolled back and must be restarted.
5. OCC can improve performance in systems where conflicts are rare, as it reduces the overhead of acquiring and releasing locks.
6. However, in systems where conflicts are common, OCC can result in a high number of transaction rollbacks, reducing performance.

In summary, Optimistic Concurrency Control is a method used in distributed systems to manage transactions and concurrency control. It allows transactions to execute concurrently without acquiring locks, and checks for conflicts at the end of the transaction. OCC can improve performance in systems where conflicts are rare, but can result in reduced performance in systems where conflicts are common.



# Unit 8 - Transactions and Concurrency Control in Distributed Systems

### Timestamp Ordering

Timestamp ordering is a concurrency control protocol used in distributed systems to ensure serializability of transactions. It assigns a unique timestamp to each transaction, which represents the order in which the transactions are to be executed.

- Each transaction is assigned a unique timestamp when it enters the system.
- The timestamp of a transaction determines its priority in conflict resolution.
- If two transactions conflict, the one with the earlier timestamp is allowed to proceed, while the other must wait or be rolled back.
- Timestamps can be assigned using either the system time or a logical counter.
- Timestamp ordering ensures conflict serializability, but not necessarily recoverability or cascadelessness.
- One of the main advantages of timestamp ordering is that it is a decentralized protocol, which makes it suitable for distributed systems.
- However, timestamp ordering can suffer from the "Thomas write rule" problem, where a transaction may be allowed to write an older value, resulting in an inconsistent database state.




# Comparison of methods for concurrency control

Concurrency control is a critical component of distributed systems, as it ensures that multiple transactions can be executed simultaneously without interfering with one another. There are several methods for achieving concurrency control, each with its own advantages and disadvantages.

1. **Locking**: Locking is a widely used method for concurrency control. It involves placing locks on data items to prevent multiple transactions from accessing the same data simultaneously. Locking can be implemented using different levels of granularity, such as row-level, page-level, or table-level locking. The main advantage of locking is its simplicity and ease of implementation. However, locking can lead to contention and deadlocks, which can reduce system performance.

2. **Timestamp ordering**: Timestamp ordering is another method for concurrency control. It assigns a unique timestamp to each transaction and uses these timestamps to determine the order in which transactions are executed. Transactions with earlier timestamps are given priority over transactions with later timestamps. The main advantage of timestamp ordering is that it avoids deadlocks. However, it can lead to increased contention and reduced system performance.

3. **Optimistic concurrency control**: Optimistic concurrency control is a method that allows transactions to execute concurrently without locking. Instead, it uses a validation phase to ensure that transactions do not interfere with one another. If a conflict is detected, one of the conflicting transactions is rolled back and restarted. The main advantage of optimistic concurrency control is that it can provide high levels of concurrency and system performance. However, it can be more complex to implement than other methods.

4. **Multiversion concurrency control**: Multiversion concurrency control is a method that maintains multiple versions of data items. Transactions can read older versions of data items without locking, which can reduce contention and improve system performance. However, multiversion concurrency control can be more complex to implement than other methods and can require additional storage space to maintain multiple versions of data items.

In summary, there are several methods for achieving concurrency control in distributed systems, each with its own advantages and disadvantages. The choice of method will depend on the specific requirements of the system, such as the level of concurrency required and the complexity of the implementation.



## Unit 9 - Distributed Transactions

1. **Introduction:** A distributed transaction is a transaction that spans multiple systems, typically databases, and ensures that all changes are committed or rolled back together.

2. **Two-Phase Commit Protocol:** The two-phase commit protocol is a distributed algorithm used to coordinate the commit or rollback of a distributed transaction. The first phase involves the coordinator sending a prepare message to all participants, and the participants responding with a vote to either commit or abort. In the second phase, the coordinator sends a commit or abort message to all participants based on the votes received.

3. **Three-Phase Commit Protocol:** The three-phase commit protocol is an extension of the two-phase commit protocol that adds an additional phase to ensure that all participants are ready to commit before the final commit message is sent. This additional phase helps to avoid blocking in the case of a coordinator failure.

4. **Global Transaction Identifier:** A global transaction identifier is a unique identifier assigned to a distributed transaction to track its progress across multiple systems.

5. **Distributed Deadlocks:** Distributed deadlocks can occur when multiple transactions are waiting for resources held by other transactions in a distributed system. Deadlock detection and resolution techniques must be used to prevent or resolve these deadlocks.

6. **Distributed Concurrency Control:** Distributed concurrency control is the process of managing concurrent access to data in a distributed system. Common techniques include two-phase locking and timestamp ordering.

7. **Recovery:** Recovery in a distributed system involves restoring the system to a consistent state after a failure. This can involve rolling back or committing transactions based on the state of the system at the time of the failure.

8. **Conclusion:** Distributed transactions are an important concept in distributed systems, allowing for coordinated changes across multiple systems. Various protocols and techniques are used to ensure the consistency and correctness of these transactions.



### Flat and Nested Distributed Transactions

A flat or nested transaction that accesses objects handled by different servers is referred to as a distributed transaction. When a distributed transaction reaches its end, in order to maintain the atomicity property of the transaction, it is mandatory that all of the servers involved in the transaction either commit the transaction or abort it.

Distributed transactions can be structured in two different ways: Flat transactions and Nested transactions.

#### Flat Transactions
A flat transaction has a single initiating point (Begin) and a single end point (Commit or abort). They are usually very simple and are generally used for short activities rather than larger ones.

#### Nested Transactions
Nested transactions offer a finer granularity of control over transactions. They take a top-down approach to decompose a complex transaction into subtransactions. Distributed transactions provided global integrity constraints over multiple resources. These resources soon started to be heterogeneous as well.

However, it is important to note that while flat transactions are the most prevalent model and are supported by most commercial database systems, nested transactions are supported by far fewer commercial database systems.



# Atomic Commit Protocols

Atomic Commit Protocols are used in Distributed Systems to ensure that a transaction is either committed on all sites or aborted on all sites. This is important to maintain the consistency of data across all sites in a distributed system.

There are two main types of Atomic Commit Protocols:

1. Two-Phase Commit Protocol (2PC)
2. Three-Phase Commit Protocol (3PC)

## Two-Phase Commit Protocol (2PC)

The Two-Phase Commit Protocol (2PC) is a distributed algorithm that coordinates all the processes that participate in a distributed atomic transaction on whether to commit or abort the transaction. The protocol is initiated by the coordinator after the last step of the transaction has been reached.

The 2PC protocol consists of two phases:

1. **Voting Phase:** In this phase, the coordinator sends a `VOTE-REQUEST` message to all participants and waits for their response. Each participant replies with either a `VOTE-COMMIT` if it is ready to commit the transaction or a `VOTE-ABORT` if it is not ready to commit the transaction.

2. **Decision Phase:** In this phase, the coordinator makes the final decision on whether to commit or abort the transaction based on the votes received from the participants. If all participants voted to commit, the coordinator sends a `GLOBAL-COMMIT` message to all participants. If any participant voted to abort, the coordinator sends a `GLOBAL-ABORT` message to all participants.

## Three-Phase Commit Protocol (3PC)

The Three-Phase Commit Protocol (3PC) is an extension of the 2PC protocol that adds an additional phase to avoid blocking in case of a coordinator failure. The 3PC protocol consists of three phases:

1. **Voting Phase:** This phase is the same as the voting phase in the 2PC protocol.

2. **Pre-Commit Phase:** In this phase, the coordinator sends a `PRE-COMMIT` message to all participants if all participants voted to commit. Each participant acknowledges the receipt of the `PRE-COMMIT` message by sending an `ACK` message to the coordinator.

3. **Commit Phase:** In this phase, the coordinator makes the final decision on whether to commit or abort the transaction based on the acknowledgements received from the participants. If all participants sent an `ACK` message, the coordinator sends a `GLOBAL-COMMIT` message to all participants. If any participant did not send an `ACK` message, the coordinator sends a `GLOBAL-ABORT` message to all participants.




# Concurrency Control in Distributed Transactions

Concurrency control is an essential component of distributed transactions in distributed systems. It ensures that multiple transactions can execute concurrently without interfering with each other, thus maintaining the consistency and integrity of the data.

Here are some key points to consider when studying concurrency control in distributed transactions:

1. **Concurrency control algorithms:** There are several concurrency control algorithms used in distributed transactions, including two-phase locking, timestamp ordering, and optimistic concurrency control. Each algorithm has its own advantages and disadvantages, and the choice of algorithm depends on the specific requirements of the system.

2. **Distributed deadlock:** Distributed transactions can lead to distributed deadlocks, where two or more transactions are waiting for each other to release resources. Deadlock detection and resolution is an important aspect of concurrency control in distributed transactions.

3. **Serialization:** Concurrency control ensures that the concurrent execution of transactions results in a serializable schedule, meaning that the final state of the data is the same as if the transactions were executed one at a time in some order.

4. **Recovery:** In the event of a failure, the system must be able to recover to a consistent state. Concurrency control plays a role in recovery by ensuring that transactions are either committed or aborted in a consistent manner.

5. **Performance:** Concurrency control can have a significant impact on the performance of distributed transactions. The choice of concurrency control algorithm and its implementation can affect the throughput and response time of the system.

In summary, concurrency control is a crucial aspect of distributed transactions in distributed systems, ensuring the consistency and integrity of data while allowing for concurrent execution of transactions. It involves the use of algorithms, deadlock detection and resolution, serialization, recovery, and performance considerations. It is an important topic to study when learning about distributed transactions in distributed systems.



# Distributed Deadlocks

Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems. It may be identified via a distributed technique like edge chasing or by creating a global wait-for graph (WFG) from local wait-for graphs at a deadlock detector.

In distributed systems, there are two main categories of deadlocks: Resource Deadlock and Communication Deadlock.

- **Resource Deadlock**: Resource deadlock refers to the deadlock state when the resource required by the first process is locked by the second one and the resource required by the second process is locked by the first process.

- **Communication Deadlock**: Communication deadlock refers to the deadlock state when two or more processes are blocked and waiting for messages from each other.

Deadlocks can be dealt with using any one of the following three strategies: deadlock prevention, deadlock avoidance, and deadlock detection.

- **Deadlock Prevention**: Deadlock prevention is a strategy that ensures that at least one of the necessary conditions for deadlock does not hold. This can be achieved by imposing constraints on resource allocation.

- **Deadlock Avoidance**: Deadlock avoidance is a strategy that ensures that the system never enters a deadlock state. This can be achieved by careful resource allocation and by maintaining information about the current allocation of resources and the future requests of processes.

- **Deadlock Detection**: Deadlock detection is a strategy that allows the system to enter a deadlock state, detects the deadlock, and then takes action to recover from the deadlock.

In the distributed approach, different nodes work together to detect deadlocks. There is no single point of failure as the workload is equally divided among all nodes.



# Transaction Recovery in Distributed Systems

Transaction recovery is the procedure used to recover from failures in a distributed database system. Recovery is one of the most difficult procedures in distributed databases, as it can be extremely difficult to recover a communication network system that has failed .

In distributed transaction processing, transactions may be performed effectively. However, there are instances in which a transaction may fail for a variety of causes. System failure, hardware failure, network error, inaccurate or invalid data, and application problems are all probable causes .

A recovery subsystem is an essential component of a distributed database system (DDBS). Failures in the midst of transaction processing, such as the failure of a site where a subtransaction is being processed, may lead to an inconsistent database .

Transaction recovery is done to eliminate the adverse effects of faulty transactions rather than to recover from a failure. Faulty transactions include all transactions that have changed the database into an undesired state and the transactions that have used values written by the faulty transactions .

A distributed transaction is a transaction that affects several resources. For a distributed transaction to commit, all participants must guarantee that any change to data will be permanent. Changes must persist despite system crashes or other unforeseen events .



## Unit 10 - Replication

1. Replication is the process of creating an exact copy of something.
2. In the context of biology, replication refers to the process by which DNA is copied within a cell.
3. DNA replication is a fundamental process that occurs in all living organisms and is essential for the continuation of life.
4. The process of DNA replication is complex and involves many different enzymes and proteins.
5. DNA replication occurs during the S phase of the cell cycle, in preparation for cell division.
6. During DNA replication, the two strands of the DNA molecule are separated, and each strand serves as a template for the synthesis of a new complementary strand.
7. The end result of DNA replication is two identical DNA molecules, each containing one original strand and one newly synthesized strand.
8. Errors can occur during DNA replication, leading to mutations that can have various effects on the organism.
9. DNA replication is tightly regulated to ensure that it occurs accurately and efficiently.
10. Understanding the process of DNA replication is important for many fields, including medicine, genetics, and biotechnology.




# System Model and Group Communication

In the context of replication in distributed systems, the system model and group communication play important roles. Here are some key points to consider:

1. **System Model:** The system model defines the assumptions made about the system, including the behavior of the network, the processors, and the failure modes. Common system models include the synchronous model, the asynchronous model, and the partially synchronous model.

2. **Group Communication:** Group communication refers to the exchange of messages between multiple processes in a distributed system. It is used to coordinate the actions of the processes and to ensure consistency in the replicated data.

3. **Reliable Group Communication:** Reliable group communication ensures that messages are delivered to all members of the group in a consistent and reliable manner. This is important for maintaining consistency in the replicated data.

4. **Atomic Broadcast:** Atomic broadcast is a type of reliable group communication that ensures that messages are delivered to all members of the group in the same order. This is important for maintaining consistency in the replicated data.

5. **Virtual Synchrony:** Virtual synchrony is a model of group communication that provides strong consistency guarantees. It ensures that all members of the group see the same sequence of events, even in the presence of failures.

These are some of the key concepts related to system model and group communication in the context of replication in distributed systems. Understanding these concepts is important for designing and implementing effective replication strategies.



# Fault-Tolerant Services

Fault-tolerant services are designed to continue operating even in the presence of failures. In the context of distributed systems, this means that the system is able to continue providing its services even if some of its components fail. This is achieved through the use of replication, where multiple copies of the same data or service are maintained across different nodes in the system.

Some key points to consider when designing fault-tolerant services in distributed systems include:

1. **Redundancy**: To achieve fault tolerance, it is necessary to have redundant components in the system. This can be achieved through the use of replication, where multiple copies of the same data or service are maintained across different nodes in the system.

2. **Consistency**: When using replication to achieve fault tolerance, it is important to ensure that all copies of the data remain consistent. This can be achieved through the use of consensus algorithms, which ensure that all nodes in the system agree on the state of the data.

3. **Failure Detection**: In order to recover from failures, it is necessary to detect when a component has failed. This can be achieved through the use of heartbeat messages, where nodes periodically send messages to each other to confirm that they are still operational.

4. **Recovery**: Once a failure has been detected, the system must be able to recover from it. This can be achieved through the use of techniques such as checkpointing and rollback, where the system periodically saves its state and is able to roll back to a previous state in the event of a failure.

Overall, the goal of fault-tolerant services in distributed systems is to ensure that the system is able to continue providing its services even in the presence of failures. This is achieved through the use of techniques such as replication, consistency, failure detection, and recovery.



### Unit 10 - Replication: Highly Available Services

- Highly available services are designed to ensure that the system remains operational and accessible to users, even in the event of failures or disruptions.
- Replication is a key technique used to achieve high availability, by creating multiple copies of data or services and distributing them across different nodes or locations.
- This allows the system to continue functioning even if one or more nodes fail, as other nodes can take over and provide the necessary services.
- Replication can be implemented at different levels, such as data replication, where multiple copies of the data are stored, or service replication, where multiple instances of a service are run.
- There are different approaches to replication, such as active-active, where all replicas are actively used and updated, or active-passive, where one replica is active and others are passive backups.
- Replication can also be synchronous, where updates are propagated to all replicas before the operation is considered complete, or asynchronous, where updates are propagated in the background.
- The choice of replication approach depends on factors such as the required level of availability, performance, and consistency.
- Replication can also be combined with other techniques such as load balancing and failover to further improve the availability and reliability of the system.



# Transactions with Replicated Data

In a distributed system, data replication is the process of storing copies of data on multiple nodes to improve data availability, reliability, and performance. Transactions with replicated data involve executing a sequence of operations on multiple copies of data stored on different nodes.

Here are some key points to consider when dealing with transactions with replicated data:

1. **Consistency**: Ensuring consistency of replicated data is a major challenge in distributed systems. This involves ensuring that all copies of data are updated correctly and consistently when a transaction is executed.

2. **Concurrency control**: Concurrency control mechanisms are used to ensure that transactions are executed in a way that preserves the consistency of replicated data. This involves managing conflicts that may arise when multiple transactions are executed concurrently on different copies of data.

3. **Commit protocols**: Commit protocols are used to ensure that transactions are executed atomically, i.e., either all operations of a transaction are executed successfully or none are executed. Two-phase commit (2PC) and three-phase commit (3PC) are commonly used commit protocols in distributed systems.

4. **Fault tolerance**: Replicated data provides fault tolerance by allowing transactions to be executed even if some nodes fail. However, ensuring fault tolerance in the presence of node failures requires careful design of replication protocols and transaction management mechanisms.

In summary, transactions with replicated data involve executing a sequence of operations on multiple copies of data stored on different nodes. Ensuring consistency, concurrency control, atomicity, and fault tolerance are key challenges in managing transactions with replicated data in distributed systems.

