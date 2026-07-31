

# Distributed System

A distributed system is a computing environment in which various components are spread across multiple computers (or other computing devices) on a network. These devices split up the work, coordinating their efforts to complete the job more efficiently than if a single device had been responsible for the task .

Some of the most common examples of distributed systems include:
- Telecommunications networks (including cellular networks and the fabric of the internet)
- Graphical and video-rendering systems
- Scientific computing, such as protein folding and genetic research
- Airline and hotel reservation systems
- Multiuser systems .

A distributed system is any network structure that consists of autonomous computers that are connected using a distribution middleware. Distributed systems facilitate sharing different resources and capabilities, to provide users with a single and integrated coherent network. The opposite of a distributed system is a centralized system .

A distributed system is a collection of computer programs that utilize computational resources across multiple, separate computation nodes to achieve a common, shared goal. Distributed systems aim to remove bottlenecks or central points of failure from a system .

A distributed system is a system whose components are located on different networked computers, which communicate and coordinate their actions by passing messages to one another. Distributed computing is a field of computer science that studies distributed systems .



## Unit 1 - Characterization of Distributed Systems

1. **Introduction:** A distributed system is a collection of independent computers that appears to its users as a single coherent system.
2. **Transparency:** One of the main goals of a distributed system is to hide the fact that its processes and resources are physically distributed across multiple computers. This is known as transparency.
3. **Scalability:** Distributed systems should be scalable, meaning that it should be easy to add more resources and computers to the system as the need arises.
4. **Concurrency:** In a distributed system, multiple processes can run concurrently, and the system must be able to coordinate their actions.
5. **Fault tolerance:** Distributed systems must be able to continue functioning even in the presence of failures, such as the failure of individual computers or network links.
6. **Consistency:** In a distributed system, it is important to ensure that all copies of data are consistent, meaning that they all contain the same information.
7. **Challenges:** Designing and implementing a distributed system is challenging due to issues such as network latency, the possibility of partial failures, and the need to ensure consistency and fault tolerance.



### Introduction for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

1. A distributed system is a collection of independent computers that appears to its users as a single coherent system.
2. The main goal of a distributed system is to make it easy for users and applications to access remote resources and to share them in a controlled and efficient manner.
3. Distributed systems can be characterized by several key properties, including concurrency, lack of a global clock, independent failures, and scalability.
4. Concurrency refers to the ability of multiple processes to execute simultaneously, potentially interacting with each other.
5. The lack of a global clock means that it is difficult to synchronize events across the system, and that it is necessary to use algorithms that can tolerate some degree of inconsistency.
6. Independent failures refer to the fact that components of the system can fail independently of each other, and that the system must be able to tolerate such failures and continue to operate.
7. Scalability refers to the ability of the system to continue to function effectively as the number of users and resources increases.
8. Distributed systems can be implemented using a variety of architectures, including client-server, peer-to-peer, and multi-tier architectures.
9. The design of distributed systems involves many challenges, including ensuring consistency, fault tolerance, and security.
10. Distributed systems are used in a wide range of applications, including distributed databases, distributed file systems, and distributed computing platforms.



### Examples of Distributed Systems

Distributed systems are systems in which components located on networked computers communicate and coordinate their actions by passing messages. Here are some examples of distributed systems:

1. **The World Wide Web:** The web is a massive distributed system that consists of web servers, web browsers, and other components that work together to deliver web pages and other content to users.

2. **Cloud Computing:** Cloud computing is a model of distributed computing that allows users to access and use shared computing resources, such as servers, storage, and applications, over the internet.

3. **Peer-to-Peer Networks:** Peer-to-peer networks are distributed systems in which nodes, or peers, share resources and communicate directly with each other, rather than relying on a central server.

4. **Telecommunication Networks:** Telecommunication networks, such as the telephone network and the internet, are distributed systems that allow users to communicate with each other over long distances.

5. **Distributed Databases:** Distributed databases are databases that are spread across multiple computers, allowing users to access and manipulate data from multiple locations.

These are just a few examples of distributed systems. Distributed systems are used in many different applications and industries, and their use is becoming increasingly widespread as technology continues to advance.



### Resource sharing and the Web Challenges

Resource sharing is one of the main motivations for constructing distributed systems. In a distributed system, resources such as software, hardware, or data can be shared among autonomous computer systems that are physically separated but connected by a centralized computer network equipped with distributed system software.

There are several ways in which resources can be made available in a distributed system. One such way is through data migration, which is the process of transferring data from one location to another within the system.

However, there are also several challenges that arise when sharing resources in a distributed system. One major challenge is scalability, which refers to the ability of the system to maintain its performance even as the load on the system increases. Another challenge is heterogeneity, which refers to the ability of the system to communicate with different devices.



### Architectural models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

1. **Layered Architecture**: This model organizes the system into layers, where each layer provides services to the layer above it and uses the services of the layer below it. This model is commonly used in network protocols, where each layer corresponds to a different level of abstraction.

2. **Client-Server Architecture**: This model involves two types of components: clients and servers. Clients request services from servers, which provide the requested services. This model is commonly used in web applications, where the client is a web browser and the server is a web server.

3. **Peer-to-Peer Architecture**: This model involves multiple components that act as both clients and servers. Each component can request services from other components and provide services to other components. This model is commonly used in file-sharing systems, where each component can share files with other components.

4. **Service-Oriented Architecture**: This model involves multiple components that provide services to other components. The components communicate with each other using a standard protocol, such as SOAP or REST. This model is commonly used in enterprise systems, where different components provide different business services.

5. **Event-Driven Architecture**: This model involves multiple components that communicate with each other by sending and receiving events. When a component receives an event, it performs some action in response to the event. This model is commonly used in systems that need to respond to external events, such as user input or sensor data.

6. **Microservices Architecture**: This model involves multiple small, independent components that communicate with each other using a lightweight mechanism, such as HTTP or messaging. Each component provides a specific service and can be developed and deployed independently of other components. This model is commonly used in cloud-based systems, where components can be easily scaled and updated.



### Fundamental Models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

1. **Interaction Model**: This model describes how the components of a distributed system communicate and coordinate with each other. It includes aspects such as message passing, remote procedure calls, and shared memory.

2. **Failure Model**: This model describes how the system handles failures, such as node crashes, network partitions, and lost messages. It includes aspects such as fault tolerance, replication, and recovery.

3. **Security Model**: This model describes how the system ensures the confidentiality, integrity, and availability of data and services. It includes aspects such as authentication, access control, and encryption.

4. **Performance Model**: This model describes how the system achieves high performance, such as low latency and high throughput. It includes aspects such as load balancing, caching, and scheduling.

These fundamental models provide a framework for understanding and designing distributed systems. By considering each of these models, designers can ensure that their system is able to communicate effectively, handle failures gracefully, maintain security, and achieve high performance.



### Theoretical Foundation for Distributed System

1. **Distributed System**: A distributed system is a collection of independent computers that appear to its users as a single coherent system.
2. **Transparency**: Distributed systems aim to hide the complexity of the underlying system by providing transparency to the user. This includes location, access, migration, relocation, replication, concurrency, and failure transparency.
3. **Scalability**: Distributed systems should be scalable, meaning that the system should be able to handle an increase in users, resources, and computing power without a decrease in performance.
4. **Concurrency**: In a distributed system, multiple processes can run concurrently and interact with each other to achieve a common goal.
5. **Fault Tolerance**: Distributed systems should be designed to be fault-tolerant, meaning that the system should be able to continue functioning even in the event of failures.
6. **Consistency**: Distributed systems should provide consistency, meaning that all users should see the same data at the same time, regardless of where they are located in the system.
7. **Resource Sharing**: Distributed systems allow for the sharing of resources, such as files, printers, and databases, among multiple users and processes.




### Limitation of Distributed system

Distributed systems have several limitations that can affect their performance, reliability, and scalability. Some of the limitations of distributed systems are:

1. **Network Dependence**: Distributed systems rely on the network to communicate and share data between different nodes. If the network is slow or unreliable, the performance of the distributed system can be affected.

2. **Complexity**: Distributed systems are inherently more complex than centralized systems. This complexity can make it difficult to design, implement, and maintain distributed systems.

3. **Security**: Distributed systems can be more vulnerable to security threats than centralized systems. Ensuring the security of data and communication in a distributed system can be challenging.

4. **Consistency**: Ensuring consistency of data in a distributed system can be difficult. Different nodes in the system may have different versions of the data, and reconciling these differences can be challenging.

5. **Fault Tolerance**: Distributed systems must be designed to be fault-tolerant, meaning that they can continue to operate even if one or more nodes fail. Designing and implementing fault-tolerant distributed systems can be challenging.

These are some of the limitations of distributed systems that must be considered when designing and implementing such systems.



### Absence of Global Clock in Distributed Systems

- In a distributed system, there is no global clock that all nodes can use to synchronize their actions.
- Each node has its own local clock, which may not be synchronized with the clocks of other nodes.
- This can lead to inconsistencies and conflicts when nodes try to coordinate their actions or share data.
- To address this issue, distributed systems use various synchronization algorithms and protocols to achieve a common notion of time among the nodes.
- Some common approaches include using logical clocks, vector clocks, and global time services.
- Despite these efforts, achieving perfect synchronization in a distributed system is challenging due to factors such as network delays, clock drift, and node failures.
- As a result, distributed systems must be designed to tolerate some degree of inconsistency and uncertainty in their operation.




### Shared Memory

Shared memory is a type of memory that can be accessed by multiple processes. It is a common method of inter-process communication (IPC) in distributed systems. Here are some key points to note about shared memory:

1. Shared memory allows multiple processes to access the same data concurrently.
2. It is a fast and efficient method of IPC as it eliminates the need for data to be copied between processes.
3. Shared memory can be implemented using hardware or software mechanisms.
4. In hardware-based shared memory, a common physical memory is shared between multiple processors.
5. In software-based shared memory, a portion of the virtual memory of each process is mapped to a common physical memory location.
6. Shared memory can be used for both data sharing and synchronization between processes.
7. However, shared memory can also introduce challenges such as the need for synchronization and the potential for race conditions.
8. Proper synchronization mechanisms such as locks, semaphores, and monitors must be used to ensure data consistency and prevent race conditions.

Shared memory is an important concept in the characterization of distributed systems and is covered in Unit 1 of the subject DISTRIBUTED SYSTEM. It is important to understand the advantages and challenges of shared memory when designing and implementing distributed systems.



### Logical Clocks

- Logical clocks are a mechanism used in distributed systems to provide a partial ordering of events.
- They are used to capture the causal relationships between events in a distributed system.
- Logical clocks are not based on physical time, but rather on the occurrence of events in the system.
- Each process in the system maintains its own logical clock, which is updated whenever an event occurs.
- When a process sends a message, it includes the current value of its logical clock in the message.
- When a process receives a message, it updates its logical clock to be greater than the maximum of its current value and the value received in the message.
- Logical clocks can be implemented using Lamport timestamps or vector clocks.
- Lamport timestamps are a simple implementation of logical clocks, where each process maintains a single integer value as its logical clock.
- Vector clocks are a more sophisticated implementation of logical clocks, where each process maintains a vector of integer values, one for each process in the system.
- Logical clocks are useful for detecting concurrency and causality in distributed systems, and can be used to implement algorithms for mutual exclusion, deadlock detection, and other distributed coordination tasks.



### Lamport’s & vectors logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Lamport’s logical clocks and vector clocks are algorithms used for ordering events in a distributed system.
- Lamport’s logical clocks algorithm is based on the idea of assigning a logical timestamp to each event in the system, which is used to determine the order of events.
- The algorithm works by assigning a logical clock value to each process in the system, which is incremented each time an event occurs at that process.
- When a message is sent from one process to another, the sender includes its current logical clock value in the message. The receiver then updates its own logical clock value to be the maximum of its current value and the value received in the message, plus one.
- Vector clocks extend the idea of Lamport’s logical clocks by maintaining a vector of logical clock values, one for each process in the system.
- Each process increments its own entry in the vector each time an event occurs, and when a message is sent, the entire vector is included in the message.
- The receiver then updates its own vector by taking the element-wise maximum of its current vector and the vector received in the message.
- Vector clocks provide more information about the causal relationships between events than Lamport’s logical clocks, as they can distinguish between concurrent events.
- Both Lamport’s logical clocks and vector clocks are useful tools for reasoning about the behavior of distributed systems and for implementing distributed algorithms.



### Concepts in Message Passing Systems

1. **Message Passing Interface (MPI)**: MPI is a standardized and portable message-passing system designed to function on a wide variety of parallel computers. It is used for communication between processes in a distributed memory system.

2. **Point-to-Point Communication**: Point-to-point communication refers to the exchange of messages between two processes. This can be done synchronously, where the sender waits for the receiver to acknowledge the message, or asynchronously, where the sender does not wait for the receiver.

3. **Collective Communication**: Collective communication refers to the exchange of messages between a group of processes. This can include operations such as broadcast, where one process sends the same message to all other processes, or reduce, where all processes send data to one process, which then performs a reduction operation on the data.

4. **Deadlock**: Deadlock is a situation where two or more processes are blocked, waiting for each other to release resources. This can occur in message passing systems when processes are waiting for messages from each other.

5. **Buffering**: Buffering refers to the temporary storage of messages in a message passing system. This can be used to improve performance by allowing the sender to continue without waiting for the receiver, or to prevent deadlock by allowing messages to be received out of order.

6. **Routing**: Routing refers to the process of determining the path that a message will take between the sender and the receiver. This can be done statically, where the path is determined before the message is sent, or dynamically, where the path is determined as the message is being sent.

7. **Flow Control**: Flow control refers to the process of regulating the rate at which messages are sent in a message passing system. This can be used to prevent the receiver from being overwhelmed by incoming messages, or to prevent network congestion.

8. **Reliability**: Reliability refers to the ability of a message passing system to deliver messages correctly and in order. This can be achieved through the use of error detection and correction techniques, or through the use of retransmission protocols.

9. **Ordering**: Ordering refers to the order in which messages are delivered in a message passing system. This can be important in some applications, where the order of messages can affect the correctness of the computation.

10. **Group Communication**: Group communication refers to the exchange of messages between a group of processes. This can include operations such as multicast, where one process sends the same message to a group of processes, or gather, where all processes in a group send data to one process, which then collects the data.



### Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems in the Subject of Distributed Systems

- Causal order is a fundamental concept in distributed systems.
- It refers to the ordering of events in a distributed system based on their cause-and-effect relationships.
- In a distributed system, events can occur concurrently and independently on different nodes.
- Causal order ensures that the events are ordered in a way that reflects their logical dependencies.
- This is important for maintaining consistency and correctness in distributed systems.
- Causal order can be achieved through various mechanisms such as vector clocks and logical clocks.
- These mechanisms allow nodes to track the causal relationships between events and order them accordingly.
- Causal order is essential for implementing distributed algorithms and protocols such as distributed mutual exclusion and distributed consensus.
- Understanding causal order is crucial for designing and implementing reliable and robust distributed systems.



### Total Order

Total order is a concept in distributed systems that refers to the ordering of events or messages in a system. In a distributed system, multiple processes or nodes communicate with each other by exchanging messages. These messages may be sent and received in different orders by different processes, leading to inconsistencies in the system.

To ensure consistency, a total order can be imposed on the messages, such that all processes agree on the order in which the messages are received. This can be achieved through various algorithms, such as the Lamport timestamp algorithm or the vector clock algorithm.

Some key points to remember about total order in distributed systems are:

1. Total order ensures that all processes in a distributed system agree on the order of events or messages.
2. Total order can be achieved through various algorithms, such as the Lamport timestamp algorithm or the vector clock algorithm.
3. Total order is important for ensuring consistency in a distributed system.




### Total Causal Order

Total causal order is a concept in distributed systems that refers to the ordering of events in a system. It is a way to ensure that all processes in the system have a consistent view of the order in which events occur.

Here are some key points to remember about total causal order:

1. Total causal order is achieved by using a logical clock to assign timestamps to events. These timestamps are used to order the events in the system.

2. The logical clock is updated whenever an event occurs, and the timestamp of an event is determined by the current value of the logical clock.

3. Total causal order ensures that if event A causally precedes event B, then the timestamp of event A will be less than the timestamp of event B.

4. Total causal order is important in distributed systems because it allows processes to agree on the order of events, even if the events occur at different times on different processes.

5. Total causal order is not the same as total order, which is a stricter ordering that requires all processes to agree on the order of all events, regardless of whether they are causally related.

6. Total causal order is useful in many applications, such as distributed databases, where it is important to maintain a consistent view of the data across all processes.




### Techniques for Message Ordering

In distributed systems, message ordering is an important aspect that ensures the correct execution of processes. There are several techniques for message ordering in distributed systems, including:

1. **FIFO (First-In-First-Out) Ordering**: This technique ensures that messages sent from one process to another are received in the order in which they were sent.

2. **Causal Ordering**: This technique ensures that messages are delivered in a way that respects the cause-and-effect relationship between events in the system.

3. **Total Ordering**: This technique ensures that all processes in the system agree on the order in which messages are delivered.

4. **Partial Ordering**: This technique allows for some flexibility in the order in which messages are delivered, while still ensuring that certain ordering constraints are met.

Each of these techniques has its own advantages and disadvantages, and the choice of technique depends on the specific requirements of the distributed system in question. It is important to carefully consider the message ordering technique used in a distributed system to ensure the correct and efficient execution of processes.



### Causal ordering of messages

Causal ordering of messages is a concept in distributed systems that ensures that messages are delivered in a way that respects the cause-and-effect relationship between events. Here are some key points to consider:

1. In a distributed system, events can occur concurrently, and messages can be sent between processes to communicate information about these events.
2. Causal ordering ensures that if an event e1 causally precedes an event e2, then any message m1 sent as a result of e1 is delivered before any message m2 sent as a result of e2.
3. This is important because it ensures that the system behaves in a predictable and consistent manner, even in the presence of concurrent events and message delays.
4. There are several algorithms that can be used to implement causal ordering, including vector clocks and matrix clocks.
5. Causal ordering is not the same as total ordering, which imposes a total order on all messages in the system. Causal ordering only imposes an order on messages that are causally related.




### Global State

- In a distributed system, the global state is the collection of the local states of all the processes and the state of the communication channels.
- The global state is used to determine the properties of the system, such as whether the system is in a safe state or a deadlock state.
- The global state is not directly observable, as the processes and communication channels are distributed across multiple machines.
- To determine the global state, a snapshot algorithm is used, which records the local states of the processes and the state of the communication channels in a consistent manner.
- The snapshot algorithm must ensure that the recorded global state is consistent, meaning that it could have occurred during the execution of the system.
- The Chandy-Lamport algorithm is a commonly used snapshot algorithm for determining the global state of a distributed system.



### Termination Detection

Termination detection is an important problem in distributed systems. It refers to the process of determining when a distributed computation has completed. This is a non-trivial problem because, in a distributed system, there may be no central control or global knowledge of the state of the system.

There are several approaches to termination detection, including:

1. **Counting messages:** In this approach, each process keeps track of the number of messages it has sent and received. When the number of messages sent equals the number of messages received, the process can determine that the computation has terminated.

2. **Dijkstra-Scholten algorithm:** This is a diffusing computation algorithm that uses a control structure called an "acknowledgment tree" to detect termination. Each process maintains a counter of the number of outstanding messages it has sent. When a process receives a message, it increments its counter. When it sends an acknowledgment, it decrements its counter. When a process's counter reaches zero, it sends an acknowledgment to its parent in the acknowledgment tree. When the root of the tree receives acknowledgments from all its children, the computation is considered terminated.

3. **Snapshots:** In this approach, each process periodically takes a snapshot of its state and sends it to a designated process, called the "monitor." The monitor collects the snapshots and determines if the computation has terminated based on the global state of the system.

These are just a few examples of the many approaches to termination detection in distributed systems. The choice of approach depends on the specific requirements of the system and the nature of the computation being performed.



## Unit 2 - Distributed Mutual Exclusion

Distributed mutual exclusion is a fundamental problem in distributed computing. It refers to the problem of ensuring that, in a distributed system, no two processes access a shared resource simultaneously.

1. **Lamport's Algorithm**: This algorithm uses a logical clock to order requests for the critical section. Each process maintains a queue of requests, sorted by their timestamps. When a process wants to enter the critical section, it sends a request message to all other processes and waits for their replies. Once it has received replies from all other processes, it can enter the critical section.

2. **Ricart-Agrawala Algorithm**: This algorithm is an improvement over Lamport's algorithm. It uses the same basic idea of ordering requests using timestamps, but it reduces the number of messages required. When a process receives a request message, it only sends a reply if it is not currently in the critical section and if it has not already sent a request with a lower timestamp.

3. **Maekawa's Algorithm**: This algorithm reduces the number of messages required even further by dividing the processes into groups, called "voting sets". Each process belongs to multiple voting sets, and each voting set contains a majority of the processes. When a process wants to enter the critical section, it sends a request message to all processes in its voting sets and waits for their replies. Once it has received replies from a majority of the processes in each of its voting sets, it can enter the critical section.

These are some of the algorithms used for distributed mutual exclusion. Each has its own advantages and disadvantages, and the choice of algorithm depends on the specific requirements of the system.



### Classification of Distributed Mutual Exclusion

Distributed mutual exclusion is a fundamental problem in distributed computing systems. It ensures that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner. In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion. Message passing is the sole means for implementing distributed mutual exclusion.

There are three basic approaches for implementing distributed mutual exclusion :

1. **Token-based approach**: A unique token (also known as the PRIVILEGE message) is shared among the sites. A site is allowed to enter its critical section if it possesses the token. Mutual exclusion is ensured because the token is unique .
2. **Non-token-based approach**: This approach does not use a unique token to ensure mutual exclusion.
3. **Quorum-based approach**: This approach uses a quorum (a subset of the sites) to ensure mutual exclusion .

These are the prime classifications of distributed mutual exclusion algorithms.



### Requirement of Mutual Exclusion Theorem

Mutual exclusion is a fundamental concept in the field of distributed systems. It refers to the property that ensures that only one process can access a shared resource at a time. This is essential for maintaining the consistency and integrity of data in a distributed system.

Here are some key points to consider when studying the requirement of mutual exclusion theorem for Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM:

1. Mutual exclusion is necessary to prevent race conditions, where multiple processes attempt to access and modify a shared resource simultaneously, leading to unpredictable and undesirable results.

2. The mutual exclusion theorem provides a formal framework for designing and analyzing algorithms that ensure mutual exclusion in distributed systems.

3. The theorem states that any algorithm that ensures mutual exclusion in a distributed system must satisfy three conditions: safety, liveness, and fairness.

4. Safety means that at any given time, only one process can be in its critical section (i.e., accessing the shared resource).

5. Liveness means that if a process requests to enter its critical section, it will eventually be granted permission to do so.

6. Fairness means that no process should be indefinitely prevented from entering its critical section while other processes are repeatedly granted permission to do so.

7. The mutual exclusion theorem provides a rigorous and systematic approach to designing and analyzing distributed mutual exclusion algorithms, ensuring that they meet the necessary requirements for correctness and efficiency.

In summary, the mutual exclusion theorem is a crucial tool for ensuring the correctness and efficiency of distributed systems, by providing a formal framework for designing and analyzing algorithms that ensure mutual exclusion. It is an important topic to study and understand for anyone working in the field of distributed systems.



### Token based and non token based algorithms

Distributed mutual exclusion is a fundamental problem in distributed systems. It refers to the problem of ensuring that, in a distributed system, only one process can access a shared resource at a time. There are two main approaches to solving this problem: token-based algorithms and non-token-based algorithms.

1. **Token-based algorithms:** In token-based algorithms, a token is passed between processes in the system. The process holding the token has the right to access the shared resource. Once it has finished accessing the resource, it passes the token to the next process in line. Examples of token-based algorithms include the Ricart-Agrawala algorithm and the Suzuki-Kasami algorithm.

2. **Non-token-based algorithms:** In non-token-based algorithms, processes communicate with each other to coordinate access to the shared resource. These algorithms typically use message passing to exchange information about which process should access the resource next. Examples of non-token-based algorithms include the Lamport's algorithm and the Maekawa's algorithm.

Both token-based and non-token-based algorithms have their advantages and disadvantages. Token-based algorithms are generally simpler to implement and understand, but can suffer from problems such as token loss or duplication. Non-token-based algorithms can be more efficient in terms of message complexity, but can be more difficult to implement and understand.

In summary, distributed mutual exclusion is an important problem in distributed systems, and can be solved using either token-based or non-token-based algorithms. Each approach has its own advantages and disadvantages, and the choice of algorithm will depend on the specific requirements of the system.



### Performance Metrics for Distributed Mutual Exclusion Algorithms

Distributed mutual exclusion algorithms are used to ensure that only one process can access a shared resource at a time in a distributed system. There are several performance metrics that can be used to evaluate the effectiveness of these algorithms:

1. **Message complexity:** This refers to the number of messages that must be exchanged between processes in order to grant a request for the shared resource. Lower message complexity is generally desirable, as it reduces the communication overhead and improves the performance of the algorithm.

2. **Synchronization delay:** This is the time it takes for a process to gain access to the shared resource after it has made a request. Lower synchronization delay is desirable, as it means that processes can access the shared resource more quickly.

3. **Response time:** This is the time it takes for a process to receive a response to its request for the shared resource. Lower response time is desirable, as it means that processes can receive confirmation that they have access to the shared resource more quickly.

4. **Fairness:** This refers to the ability of the algorithm to ensure that all processes have an equal opportunity to access the shared resource. An algorithm is considered fair if it prevents starvation, where a process is perpetually denied access to the shared resource.

These are some of the key performance metrics that can be used to evaluate the effectiveness of distributed mutual exclusion algorithms. It is important to consider these metrics when designing and implementing these algorithms in a distributed system.



## Unit 3 - Distributed Deadlock Detection

Distributed deadlock detection is the process of detecting deadlocks in a distributed system. A deadlock occurs when two or more processes are blocked, waiting for resources held by each other. In a distributed system, this can happen when processes are running on different machines and are competing for shared resources.

Some key points to consider when discussing distributed deadlock detection are:

1. **Deadlock detection algorithms**: There are several algorithms that can be used to detect deadlocks in a distributed system. These include the centralized, hierarchical, and distributed algorithms.

2. **Deadlock resolution**: Once a deadlock has been detected, it must be resolved. This can be done by aborting one or more of the processes involved in the deadlock, or by preempting resources and assigning them to other processes.

3. **Deadlock prevention**: Deadlock prevention techniques can be used to prevent deadlocks from occurring in the first place. These techniques include resource ordering, timeouts, and deadlock detection and resolution.

4. **Challenges**: Detecting and resolving deadlocks in a distributed system can be challenging due to the complexity of the system and the need for coordination between different machines.

Overall, distributed deadlock detection is an important topic in the study of distributed systems, as it is essential for ensuring the smooth operation of these systems. It is important to understand the different algorithms and techniques that can be used to detect and resolve deadlocks, as well as the challenges that arise in this process.



### System Model

A system model is a representation of a system that is used to study and understand the behavior of the system. In the context of distributed deadlock detection, the system model typically includes the following components:

1. A set of processes: These are the entities that execute in the system and can request and release resources.

2. A set of resources: These are the entities that can be requested and held by processes.

3. A resource allocation graph: This is a directed graph that represents the current allocation of resources to processes and the requests that processes have made for resources.

4. A deadlock detection algorithm: This is the algorithm that is used to analyze the resource allocation graph to determine if there is a deadlock in the system.

The system model can be used to study the behavior of the system under different conditions and to evaluate the performance of different deadlock detection algorithms. It is an important tool for understanding and designing distributed deadlock detection systems.



### Resource Vs Communication Deadlocks

- **Resource Deadlocks** occur when processes are waiting for resources that are held by other processes. This can happen when multiple processes are competing for a limited number of resources, such as memory, CPU time, or I/O devices.

- **Communication Deadlocks** occur when processes are waiting for messages from other processes that are also waiting for messages. This can happen when processes are communicating with each other in a circular fashion, where each process is waiting for a message from the next process in the circle.

- In a **distributed system**, both resource and communication deadlocks can occur. Distributed deadlock detection algorithms are used to detect and resolve these deadlocks.

- **Distributed Deadlock Detection** algorithms can be classified into two categories: **centralized** and **distributed**. Centralized algorithms rely on a central coordinator to detect deadlocks, while distributed algorithms rely on the cooperation of all processes in the system.

- **Centralized Deadlock Detection** algorithms are simpler to implement, but they can become a bottleneck in large systems. **Distributed Deadlock Detection** algorithms are more scalable, but they can be more complex to implement.

- **Distributed Deadlock Detection** algorithms can also be classified into two categories: **path-pushing** and **edge-chasing**. Path-pushing algorithms propagate information about waiting processes along the edges of the wait-for graph, while edge-chasing algorithms send probes along the edges of the wait-for graph to detect cycles.

- **Path-pushing** algorithms are generally more efficient, but they require more storage space. **Edge-chasing** algorithms are generally less efficient, but they require less storage space.

- In summary, resource and communication deadlocks can occur in distributed systems, and distributed deadlock detection algorithms are used to detect and resolve these deadlocks. These algorithms can be classified into centralized and distributed, as well as path-pushing and edge-chasing. The choice of algorithm depends on the specific requirements of the system.



### Deadlock Prevention

Deadlock prevention is a technique used in distributed systems to avoid the occurrence of deadlocks. Deadlocks occur when two or more processes are blocked and unable to proceed because they are waiting for resources held by other processes. Deadlock prevention techniques aim to ensure that at least one of the conditions necessary for a deadlock to occur is never met. These conditions are:

1. **Mutual Exclusion**: A resource can only be held by one process at a time.
2. **Hold and Wait**: A process can hold resources while waiting for additional resources.
3. **No Preemption**: Resources cannot be forcibly taken away from a process.
4. **Circular Wait**: A circular chain of processes exists, where each process is waiting for a resource held by the next process in the chain.

Deadlock prevention techniques can be implemented by ensuring that at least one of these conditions is never met. For example, one technique is to prevent hold and wait by requiring processes to request all the resources they need at once, rather than holding some resources while waiting for others. Another technique is to prevent circular wait by imposing a total ordering on the resources and requiring processes to request resources in a specific order.

In summary, deadlock prevention is an important technique in distributed systems to avoid the occurrence of deadlocks. It can be achieved by ensuring that at least one of the conditions necessary for a deadlock to occur is never met. Various techniques can be used to achieve this, such as preventing hold and wait or circular wait.



### Avoidance

Avoidance is a technique used in Distributed Deadlock Detection in Distributed Systems. It is a proactive approach that aims to prevent deadlocks from occurring in the first place. Here are some key points to remember about avoidance in the context of Distributed Deadlock Detection:

1. Avoidance algorithms require additional information about the resources and processes in the system, such as the maximum number of resources each process may request.
2. One of the most common avoidance algorithms is the Banker's algorithm, which uses this additional information to determine whether or not a resource request may lead to a deadlock.
3. Avoidance algorithms can be more complex and require more overhead than other deadlock detection techniques, but they can prevent deadlocks from occurring, potentially saving time and resources in the long run.
4. In a distributed system, avoidance algorithms must take into account the distributed nature of the system and the potential for communication delays and failures.
5. Avoidance is not always possible or practical in all distributed systems, and other techniques such as detection and resolution may be used in conjunction with avoidance to manage deadlocks.




### Detection & Resolution for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

1. **Distributed Deadlock Detection**: In a distributed system, deadlock detection is more complex due to the lack of a central resource allocation table and the need for communication between nodes.
2. **Detection Algorithms**: There are several algorithms for detecting deadlocks in distributed systems, including the path-pushing algorithm, the edge-chasing algorithm, and the diffusing computation algorithm.
3. **Resolution**: Once a deadlock is detected, it can be resolved by aborting one or more processes or by preempting resources from one or more processes.
4. **Challenges**: The main challenges in distributed deadlock detection and resolution are the need for efficient communication and coordination between nodes, and the need to handle partial failures and network partitions.




### Centralized Deadlock Detection

Centralized deadlock detection is a method for detecting deadlocks in a distributed system. In this approach, a single designated node, called the coordinator, is responsible for detecting deadlocks. The following are the key points to note about centralized deadlock detection:

1. The coordinator maintains a global wait-for graph (WFG) that represents the dependencies between transactions in the system.
2. Each node in the system periodically sends information about its local wait-for graph to the coordinator.
3. The coordinator merges the local wait-for graphs from all nodes to construct the global wait-for graph.
4. The coordinator then checks the global wait-for graph for cycles. If a cycle is detected, it indicates the presence of a deadlock.
5. The coordinator can then initiate a recovery procedure to resolve the deadlock, such as aborting one or more transactions involved in the deadlock.

Centralized deadlock detection has the advantage of simplicity, as the coordinator is the only node responsible for detecting deadlocks. However, it also has some disadvantages, such as the potential for a single point of failure and the communication overhead of sending local wait-for graphs to the coordinator. Additionally, the coordinator may become a bottleneck in large systems with many nodes and transactions.



### Distributed Deadlock Detection

Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems. It may be identified via a distributed technique like edge chasing or by creating a global wait-for graph (WFG) from local wait-for graphs at a deadlock detector.

Deadlock detection in distributed systems seems to be the best approach to handle deadlocks in distributed systems. Issues in Deadlock Detection Deadlock handling using the approach of deadlock detection entails addressing two basic issues: First, detection of existing deadlocks and second resolution of detected deadlocks.

Distributed deadlock detection algorithms can be divided into four classes: path-pushing, edge-chasing, diffusion computation, and global state detection.

In the deadlock avoidance approach to distributed systems, a resource is granted to a process if the resulting global system is safe. Deadlock detection requires an examination of the status of the process–resources interaction for the presence of a deadlock condition. To resolve the deadlock, we have to abort a deadlocked process.

The techniques of deadlock detection in the distributed system require the following: Progress – The method should be able to detect all the deadlocks in the system. Safety – The method should not detect false or phantom deadlocks. There are three approaches to detect deadlocks in distributed systems. They are as follows.

Distributed deadlocks can be detected either by constructing a global wait-for graph, from local wait-for graphs at a deadlock detector or by a distributed algorithm like edge chasing. Phantom deadlocks are deadlocks that are detected in a distributed system due to system internal delays but no longer actually exist at the time of detection.



### Path Pushing Algorithms

Path pushing algorithms are a class of algorithms used for distributed deadlock detection in distributed systems. These algorithms work by propagating information about blocked processes along wait-for edges in the system's resource graph.

Here are some key points to note about path pushing algorithms:

1. In a path pushing algorithm, each process maintains a set of blocked processes that are dependent on it for resources.
2. When a process becomes blocked, it sends a message to all processes that hold resources it is waiting for, informing them of its blocked status.
3. Upon receiving a message from a blocked process, a process adds the blocked process to its set of dependent processes and propagates the information to all processes that hold resources it is waiting for.
4. If a process receives a message indicating that it is dependent on itself, a deadlock has been detected.
5. Once a deadlock has been detected, a resolution strategy can be employed to resolve the deadlock.

Path pushing algorithms are an effective way to detect deadlocks in distributed systems. They are relatively simple to implement and can detect deadlocks quickly. However, they do require a significant amount of message passing, which can impact the performance of the system.



### Edge Chasing Algorithms

Edge chasing algorithms are used for distributed deadlock detection in distributed systems. Here are some key points to note about edge chasing algorithms:

1. Edge chasing algorithms are based on the concept of sending probe messages to detect cycles in the wait-for graph.
2. A probe message contains information about the initiator of the probe, the current transaction, and the blocked transaction.
3. When a transaction receives a probe message, it checks if it is waiting for any other transaction. If it is, it forwards the probe message to the transaction it is waiting for.
4. If a transaction receives a probe message that it has already seen, it means that a cycle has been detected and a deadlock exists.
5. Once a deadlock is detected, a resolution mechanism is used to break the deadlock, such as aborting one of the transactions involved in the deadlock.
6. Edge chasing algorithms can be classified into two categories: centralized and distributed.
7. In centralized edge chasing algorithms, a single site is responsible for detecting deadlocks, while in distributed edge chasing algorithms, all sites participate in the deadlock detection process.




## Unit 4 - Agreement Protocols

Agreement protocols are a class of protocols used in distributed systems to ensure that all processes in the system agree on a certain value or state. These protocols are important for maintaining consistency and reliability in distributed systems.

Some common types of agreement protocols include:

1. **Consensus protocols:** These protocols are used to ensure that all processes in the system agree on a single value. This is typically achieved through a series of rounds of communication between the processes, where each process proposes a value and then all processes vote on the proposed values.

2. **Byzantine agreement protocols:** These protocols are a type of consensus protocol designed to handle situations where some of the processes in the system may be faulty or malicious. Byzantine agreement protocols use complex algorithms to ensure that all non-faulty processes can agree on a single value, even in the presence of faulty processes.

3. **Atomic commit protocols:** These protocols are used to ensure that a set of transactions are either all committed or all aborted. This is important for maintaining consistency in distributed databases, where multiple processes may be involved in a single transaction.

4. **Leader election protocols:** These protocols are used to elect a leader process among a group of processes. The leader process is responsible for coordinating the actions of the other processes and making decisions on behalf of the group.

Agreement protocols are a crucial component of distributed systems, and their design and implementation can have a significant impact on the performance and reliability of the system. It is important for developers and system architects to carefully consider the requirements of their system and choose the appropriate agreement protocol to meet those requirements.



### Introduction for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- Agreement protocols are a fundamental part of distributed systems.
- They are used to ensure that all nodes in a distributed system agree on a common value or decision.
- Agreement protocols are necessary for the correct functioning of distributed systems, as they help to maintain consistency and reliability.
- There are several types of agreement protocols, including consensus, atomic commit, and voting protocols.
- These protocols use different techniques to achieve agreement, such as message passing, timeouts, and failure detectors.
- The choice of agreement protocol depends on the specific requirements of the distributed system, such as the level of fault tolerance and the desired performance.
- In this unit, we will study the different types of agreement protocols and their properties, as well as their applications in distributed systems.



### System Models for Unit 4 - Agreement Protocols in Distributed Systems

1. **Synchronous System Model**: In this model, there are known bounds on message transmission delays, process execution speeds, and clock drift rates. This model allows for the design of algorithms that can tolerate failures and ensure agreement among processes.

2. **Asynchronous System Model**: In this model, there are no known bounds on message transmission delays, process execution speeds, or clock drift rates. This model is more realistic than the synchronous model, but it makes it more difficult to design algorithms that can ensure agreement among processes.

3. **Partially Synchronous System Model**: This model is a hybrid of the synchronous and asynchronous models. It assumes that the system is synchronous most of the time, but it can occasionally behave asynchronously. This model allows for the design of algorithms that can ensure agreement among processes, even in the presence of occasional asynchronous behavior.

4. **Failure Models**: In distributed systems, it is important to consider the different types of failures that can occur. Common failure models include crash failures, where a process stops executing, and Byzantine failures, where a process can behave arbitrarily.

5. **Communication Models**: In distributed systems, processes communicate with each other by exchanging messages. There are different communication models that can be used, including point-to-point communication, where messages are sent directly from one process to another, and broadcast communication, where messages are sent to all processes in the system.

These are some of the system models that are relevant to the study of agreement protocols in distributed systems. Understanding these models is important for designing and analyzing algorithms that can ensure agreement among processes in a distributed system.



### Classification of Agreement Problem

The agreement problem is a fundamental problem in distributed systems, where multiple processes need to agree on a single value. There are several classifications of the agreement problem, including:

1. **Consensus**: In this problem, all processes must agree on a single value, and the value must be proposed by one of the processes.

2. **Byzantine Agreement**: This is a more general form of the consensus problem, where some of the processes may be faulty and send incorrect information. The goal is for the non-faulty processes to agree on a single value.

3. **Interactive Consistency**: In this problem, each process has an initial value, and the goal is for all processes to agree on a vector of values, where the i-th value is the initial value of the i-th process.

4. **k-Set Agreement**: In this problem, the processes must agree on at most k different values.

These are some of the main classifications of the agreement problem in distributed systems. Understanding these problems and their solutions is crucial for designing reliable and fault-tolerant distributed systems.



### Byzantine Agreement Problem

The Byzantine agreement problem is a fundamental problem in fault-tolerant distributed computing. It was first defined by Lamport, who also provided a solution under the situation of processor failure . The problem requires a set of parties in a distributed environment to agree on a value even if some of the parties are corrupted . This problem is also known as the Byzantine generals problem, interactive consistency, source congruency, error avalanche, Byzantine agreement problem, and Byzantine failure .

The problem of obtaining Byzantine consensus was conceived and formalized by Robert Shostak, who dubbed it the interactive consistency problem. This work was done in 1978 in the context of the NASA-sponsored SIFT project in the Computer Science Lab at SRI International .

To solve the Byzantine Generals problem, loyal generals need a secure way to come to agreement on a plan (known as consensus) and carry out their chosen plan (known as coordination). While actually solving the Byzantine Generals Problem is quite complex, we now understand the fundamental challenge .



### Consensus problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- The consensus problem is a fundamental problem in distributed computing.
- It involves multiple processes or nodes in a distributed system agreeing on a single value or decision.
- The goal is to reach an agreement among all nodes, even in the presence of failures or unreliable communication.
- The consensus problem is important in many applications, such as distributed databases, fault-tolerant systems, and blockchain technology.
- There are several algorithms and protocols that can be used to solve the consensus problem, such as Paxos, Raft, and Byzantine Fault Tolerance.
- The choice of algorithm or protocol depends on the specific requirements and constraints of the system, such as the number of nodes, the type of failures that can occur, and the desired level of fault tolerance.
- Solving the consensus problem is challenging due to the possibility of conflicting information, network partitions, and malicious nodes.
- Research in this area is ongoing, with the goal of developing more efficient and robust solutions to the consensus problem.



### Interactive Consistency Problem

The interactive consistency problem is a fundamental problem in distributed systems, particularly in the context of agreement protocols. It is also known as the Byzantine Generals Problem.

The problem can be stated as follows: In a distributed system with `n` processes, some of which may be faulty, how can the non-faulty processes reach agreement on a common value, despite the presence of the faulty processes?

This problem is challenging because the faulty processes may exhibit arbitrary behavior, including sending conflicting information to different processes. As a result, it is difficult for the non-faulty processes to determine which information is reliable and which is not.

Several solutions have been proposed to solve the interactive consistency problem, including the use of digital signatures, message authentication codes, and other cryptographic techniques. These solutions typically involve the use of additional communication rounds and the exchange of additional messages between the processes.

In summary, the interactive consistency problem is a fundamental challenge in distributed systems, and several techniques have been developed to address it. These techniques typically involve the use of additional communication and cryptographic mechanisms to ensure the reliability of the information exchanged between the processes.



### Solution to Byzantine Agreement problem

The Byzantine Agreement problem, also known as the Byzantine Generals problem, is a fundamental challenge in distributed computing. It was first defined by Lamport, who also provided a solution under the situation of processor failure.

To solve the Byzantine Generals problem, loyal generals need a secure way to come to agreement on a plan (known as consensus) and carry out their chosen plan (known as coordination). The solution to the Byzantine Generals Problem is quite complex and involves some hashing, heavy computing work, and communication between all of the nodes (generals) to verify the message.

There have been several proposed solutions to the Byzantine Agreement problem, including a quantum solution presented by Matthias Fitzi, Nicolas Gisin, and Ueli Maurer.



### Application of Agreement problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

1. The agreement problem is a fundamental problem in distributed systems, where multiple processes need to agree on a single value.
2. This problem arises in various scenarios, such as deciding on a leader, committing a transaction, or reaching a consensus on the state of the system.
3. The agreement problem is challenging because processes may fail, messages may be lost or delayed, and the network may be unreliable.
4. To solve the agreement problem, various agreement protocols have been proposed, such as Paxos, Raft, and Two-Phase Commit.
5. These protocols use techniques such as leader election, message passing, and timeouts to ensure that all processes eventually agree on a single value.
6. The application of agreement protocols is crucial in distributed systems, as it ensures consistency and reliability in the face of failures and uncertainties.
7. Agreement protocols are widely used in distributed databases, distributed file systems, and other distributed applications.




### Atomic Commit in Distributed Database System

- In a distributed database system, an atomic commit is a protocol that ensures that all changes to the database are either committed or aborted.
- The atomic commit protocol is used to ensure that a transaction is either completed in its entirety or not at all, even in the presence of failures.
- The two-phase commit (2PC) protocol is a commonly used atomic commit protocol in distributed database systems.
- In the first phase of the 2PC protocol, the coordinator sends a prepare message to all participants and waits for their responses.
- In the second phase, the coordinator decides whether to commit or abort the transaction based on the responses from the participants.
- If all participants respond with a yes vote, the coordinator sends a commit message to all participants. Otherwise, the coordinator sends an abort message.
- The participants then follow the coordinator's decision and either commit or abort the transaction.
- The atomic commit protocol ensures that all participants agree on the final outcome of the transaction and that the database remains consistent.
- However, the 2PC protocol has some drawbacks, such as the possibility of blocking in the case of coordinator failure.
- Other atomic commit protocols, such as the three-phase commit (3PC) protocol, have been proposed to address these issues.




## Unit 5 - Distributed Resource Management

Distributed Resource Management refers to the process of managing resources in a distributed computing environment. This includes the allocation, scheduling, and coordination of resources such as processing power, memory, storage, and network bandwidth across multiple systems.

Some key points to consider in Distributed Resource Management are:

1. **Resource allocation**: In a distributed environment, resources are spread across multiple systems. Resource allocation involves assigning these resources to tasks in an efficient manner.

2. **Scheduling**: Scheduling refers to the process of determining the order in which tasks are executed. In a distributed environment, scheduling can be more complex due to the need to coordinate tasks across multiple systems.

3. **Coordination**: Coordination involves managing the dependencies between tasks and ensuring that they are executed in the correct order. This is particularly important in a distributed environment where tasks may be spread across multiple systems.

4. **Load balancing**: Load balancing involves distributing workloads across multiple systems to ensure that no single system becomes overloaded. This can help to improve the overall performance of the distributed system.

5. **Fault tolerance**: Fault tolerance refers to the ability of a system to continue functioning in the event of a failure. In a distributed environment, this can involve replicating data and tasks across multiple systems to ensure that a failure in one system does not result in the loss of data or the inability to complete a task.

Overall, Distributed Resource Management is a complex process that involves managing resources across multiple systems in an efficient and effective manner. It is an important aspect of distributed computing and can help to improve the performance and reliability of distributed systems.



### Issues in Distributed File Systems

Distributed file systems are designed to provide transparent access to files stored on a network of computers. While they offer many benefits, there are also several issues that arise in their design and implementation. Some of the key issues in distributed file systems include:

1. **Consistency**: Ensuring that all clients see the same view of the file system and its contents can be challenging in a distributed environment. This is particularly true when multiple clients are accessing and modifying the same file simultaneously.

2. **Availability**: Distributed file systems must be designed to be highly available, even in the face of network or server failures. This requires the use of replication and other fault-tolerance techniques.

3. **Scalability**: As the number of clients and servers in a distributed file system grows, it can become increasingly difficult to maintain performance and manageability. Effective scaling requires careful design and the use of techniques such as caching and load balancing.

4. **Security**: Ensuring the security of data stored in a distributed file system is critical. This includes protecting against unauthorized access, as well as ensuring the integrity and confidentiality of data.

5. **Performance**: Distributed file systems must be designed to provide high performance, even when dealing with large amounts of data and high levels of concurrency. This requires the use of efficient data structures and algorithms, as well as careful tuning of network and disk I/O.

These are some of the key issues that must be addressed when designing and implementing a distributed file system. By carefully considering these issues and using appropriate techniques, it is possible to build a distributed file system that is reliable, scalable, secure, and high-performing.



### Mechanism for building distributed file systems

Distributed file systems are designed to provide shared access to files and directories across a network of computers. Here are some key mechanisms for building distributed file systems:

1. **Data distribution:** One of the main challenges in building a distributed file system is deciding how to distribute data across multiple servers. There are several approaches to this, including data striping, where data is split into blocks and distributed across multiple servers, and data replication, where multiple copies of the data are stored on different servers.

2. **Consistency:** Ensuring consistency of data across multiple servers is another important mechanism in building a distributed file system. This can be achieved through techniques such as versioning, where each update to a file is assigned a unique version number, and conflict resolution, where conflicts between updates from different servers are resolved.

3. **Fault tolerance:** Distributed file systems must be designed to be fault-tolerant, meaning that they can continue to operate even in the presence of failures. This can be achieved through mechanisms such as data replication, where multiple copies of data are stored on different servers, and failure detection and recovery, where the system can detect when a server has failed and take steps to recover from the failure.

4. **Scalability:** As the number of users and the amount of data stored in a distributed file system grows, the system must be able to scale to accommodate this growth. This can be achieved through mechanisms such as dynamic partitioning, where the system can dynamically allocate more servers to store data as the amount of data grows, and load balancing, where the system can distribute requests across multiple servers to balance the load.

5. **Security:** Security is an important consideration in building a distributed file system, as the system must protect against unauthorized access to data. This can be achieved through mechanisms such as access control, where the system can control who has access to which files and directories, and encryption, where data is encrypted before being stored on the servers to protect against unauthorized access.

These are some of the key mechanisms for building distributed file systems. By implementing these mechanisms, a distributed file system can provide shared access to files and directories across a network of computers, while ensuring consistency, fault tolerance, scalability, and security.



### Design issues in Distributed Shared Memory

Distributed Shared Memory (DSM) is a mechanism that manages memory across multiple nodes and makes inter-process communications clear to end-users. To design a distributed shared memory system, certain issues must be addressed. Some of these issues include:

1. **Granularity**: Granularity refers to the block size of a DSM system. It is the unit of sharing and the level of detail at which the system operates.
2. **Structure of shared memory space**: Structure refers to the design of the shared data in the memory. The structure of the shared memory space determines how data is organized and accessed.
3. **Memory coherence**: Memory coherence is the consistency of shared data across multiple nodes. It ensures that all nodes have a consistent view of the shared data.
4. **Design choices**: Design choices include structure and granularity, coherence semantics, scalability, and heterogeneity.
5. **Implementation methods**: Implementation methods refer to the techniques used to implement the DSM system. These methods can affect the performance and functionality of the system.

These are some of the design issues that must be considered when designing a distributed shared memory system. Each of these issues can affect the performance, functionality, and usability of the system.



### Algorithm for Implementation of Distributed Shared Memory

Distributed Shared Memory (DSM) is a system that allows multiple computers to share a single virtual memory space. This allows programs running on different computers to communicate and share data as if they were running on the same computer. Here is an algorithm for implementing DSM:

1. **Initialization**: Each computer in the system is assigned a portion of the shared memory space. This memory is allocated and managed by the local operating system.

2. **Data Access**: When a program running on one computer needs to access data in the shared memory space, it sends a request to the computer that manages that portion of the memory.

3. **Data Transfer**: The computer that manages the requested data sends the data to the requesting computer. This can be done using a variety of communication methods, such as message passing or remote procedure calls.

4. **Data Consistency**: To ensure that all computers have a consistent view of the shared memory, a consistency protocol is used. This protocol ensures that any changes made to the shared memory are propagated to all computers in the system.

5. **Fault Tolerance**: In the event of a failure, such as a computer crashing or a network partition, the system must be able to recover and continue operating. This can be achieved through the use of replication and other fault-tolerance techniques.

This is a high-level overview of the algorithm for implementing Distributed Shared Memory. There are many details and variations that can be applied to this basic algorithm to improve performance, scalability, and reliability. It is important to carefully design and implement a DSM system to meet the specific needs of the application and the underlying hardware and network infrastructure.



## Unit 6 - Failure Recovery in Distributed Systems

1. **Introduction:** In distributed systems, failure recovery is the process of restoring the system to a consistent state after a failure has occurred. This is important to ensure the availability and reliability of the system.

2. **Types of Failures:** There are several types of failures that can occur in a distributed system, including node failures, network failures, and software failures. Each type of failure requires a different recovery strategy.

3. **Recovery Strategies:** There are several strategies that can be used to recover from failures in a distributed system, including checkpointing, replication, and logging. Each strategy has its own advantages and disadvantages, and the choice of strategy depends on the specific requirements of the system.

4. **Checkpointing:** Checkpointing is a recovery strategy that involves periodically saving the state of the system to stable storage. In the event of a failure, the system can be restored to the last saved state.

5. **Replication:** Replication is a recovery strategy that involves maintaining multiple copies of the system state across different nodes. In the event of a failure, the system can continue to operate using the remaining copies.

6. **Logging:** Logging is a recovery strategy that involves recording all changes to the system state in a log. In the event of a failure, the log can be used to restore the system to a consistent state.

7. **Conclusion:** Failure recovery is an important aspect of distributed systems, and there are several strategies that can be used to recover from failures. The choice of strategy depends on the specific requirements of the system, and a combination of strategies may be used to achieve the desired level of availability and reliability.



### Concepts in Backward and Forward recovery for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- **Backward recovery** is a technique used in distributed systems to recover from failures by restoring the system to a previous consistent state.
- This is achieved by maintaining a log of all the changes made to the system and using it to undo the changes made after the last consistent state.
- **Forward recovery** is a technique used in distributed systems to recover from failures by moving the system to a new consistent state.
- This is achieved by detecting the failure and applying corrective actions to bring the system to a new consistent state.
- Both backward and forward recovery techniques are used to ensure the consistency and availability of the distributed system in the event of failures.
- The choice of recovery technique depends on the nature of the failure and the requirements of the system.




### Recovery in Concurrent Systems

Recovery in concurrent systems is an important aspect of failure recovery in distributed systems. Here are some key points to consider:

1. **Concurrency control** is necessary to ensure that multiple processes can access shared data and resources without interfering with each other. This is important for maintaining data consistency and integrity.

2. **Checkpointing** is a technique used to save the state of a system at regular intervals. This allows the system to recover from failures by rolling back to a previous checkpoint and resuming execution from there.

3. **Logging** is another technique used for recovery in concurrent systems. It involves recording all changes made to the system in a log, which can be used to recover the system to a consistent state in the event of a failure.

4. **Recovery algorithms** are used to restore the system to a consistent state after a failure. These algorithms use techniques such as checkpointing and logging to recover the system.

5. **Distributed commit protocols** such as the two-phase commit protocol are used to ensure that transactions are either committed or aborted in a consistent manner across all nodes in a distributed system.

6. **Fault tolerance** is an important aspect of recovery in concurrent systems. This involves designing systems that can continue to operate correctly even in the presence of failures.

In summary, recovery in concurrent systems involves the use of various techniques and algorithms to ensure that the system can recover from failures and continue to operate correctly. These techniques include concurrency control, checkpointing, logging, recovery algorithms, distributed commit protocols, and fault tolerance.



### Obtaining consistent Checkpoints for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

1. **Checkpointing** is a technique used in distributed systems to record the state of the system at a specific point in time. This allows the system to recover from failures by restoring the state from the checkpoint.

2. **Consistent checkpoints** are checkpoints that represent a global state of the system that could have occurred if the system had executed in a sequential manner.

3. To obtain consistent checkpoints, the following steps can be followed:
    - **Coordination**: All processes in the system must agree on when to take the checkpoint.
    - **Recording**: Each process records its local state and sends a message to all other processes indicating that it has taken the checkpoint.
    - **Verification**: Each process verifies that it has received a checkpoint message from all other processes before considering the checkpoint to be complete.

4. There are several algorithms that can be used to obtain consistent checkpoints, including the **Chandy-Lamport algorithm** and the **Skeen's algorithm**.

5. It is important to note that obtaining consistent checkpoints can be a complex and time-consuming process, and may require significant coordination and communication between processes.

6. In summary, obtaining consistent checkpoints is an important technique for ensuring the recoverability of distributed systems in the event of failures. It involves coordination, recording, and verification to ensure that the checkpoints represent a consistent global state of the system. Several algorithms exist to facilitate this process.



### Recovery in Distributed Database Systems

Recovery in distributed database systems is the process of restoring the database to a consistent state after a failure. The goal of recovery is to maintain the atomicity and durability of distributed transactions. A database must guarantee that all statements in a transaction, distributed or non-distributed, either commit or roll back as a unit.

There are two types of failures that can occur in a distributed database system: soft failures and hard failures. In case of soft failures that result in inconsistency of the database, the recovery strategy includes transaction undo or rollback. However, sometimes, transaction redo may also be adopted to recover to a consistent state of the transaction.

In case of hard failures resulting in extensive damage to the database, recovery strategies encompass restoring a past copy of the database from archival backup.

Distributed recovery is more complicated than centralized database recovery because failures can occur at the communication links or a remote site. Ideally, a recovery system should be simple, incur tolerable overhead, maintain system consistency, provide partial operability and avoid global rollback.

Transaction recovery is done to eliminate the adverse effects of faulty transactions rather than to recover from a failure. Faulty transactions include all transactions that have changed the database into an undesired state and the transactions that have used values written by the faulty transactions.



## Unit 7 - Fault Tolerance

Fault tolerance is the ability of a system to continue functioning in the event of a failure of one or more of its components. This is achieved through the use of redundant components, error detection and correction mechanisms, and other techniques.

1. **Redundancy**: Redundancy refers to the use of additional components or systems to provide backup in case of failure. For example, a system may have multiple power supplies, so that if one fails, the others can take over.

2. **Error Detection and Correction**: Error detection and correction mechanisms are used to identify and correct errors that may occur during the operation of a system. For example, a system may use parity bits or checksums to detect errors in data transmission, and error-correcting codes to correct them.

3. **Failover**: Failover is the process of switching to a backup system or component in the event of a failure. For example, if a server fails, a failover mechanism may automatically switch to a backup server to ensure continued operation.

4. **Recovery**: Recovery refers to the process of restoring a system to its normal state after a failure. This may involve repairing or replacing failed components, restoring data from backups, or other actions.

5. **Fault Tolerance Techniques**: There are many techniques that can be used to achieve fault tolerance, including replication, clustering, virtualization, and others. The choice of technique will depend on the specific requirements of the system and the nature of the failures it needs to tolerate.



### Issues in Fault Tolerance

Fault tolerance is the ability of a system to continue functioning in the event of a failure. In the context of distributed systems, fault tolerance is particularly important due to the inherent complexity and potential for failures in such systems. Some of the issues that arise in fault tolerance for distributed systems include:

1. **Failure detection:** In a distributed system, it can be difficult to determine whether a failure has occurred, and if so, what the cause of the failure is. This is because the system is composed of multiple components, and a failure in one component may not be immediately apparent to other components.

2. **Failure recovery:** Once a failure has been detected, the system must be able to recover from it. This can involve replacing failed components, re-routing messages, or other actions to restore the system to a functioning state.

3. **Redundancy:** One way to improve the fault tolerance of a system is to introduce redundancy, such as by replicating data or using multiple components to perform the same task. However, this can increase the complexity and cost of the system.

4. **Consistency:** In a distributed system, it is important to maintain consistency of data and operations across all components. However, this can be challenging in the presence of failures, as some components may have outdated or incorrect information.

5. **Coordination:** Coordinating the actions of multiple components in a distributed system can be difficult, particularly in the presence of failures. This can lead to inconsistencies or other issues that can impact the fault tolerance of the system.

These are some of the key issues that arise in fault tolerance for distributed systems. By addressing these issues, it is possible to improve the resilience of a distributed system and ensure that it can continue to function even in the presence of failures.



### Commit Protocols

Commit protocols are used in distributed systems to ensure that all nodes in the system agree on the final outcome of a transaction. This is important for maintaining consistency and fault tolerance in the system.

There are several types of commit protocols, including:

1. **Two-phase commit (2PC)**: This protocol involves two phases, the prepare phase and the commit phase. In the prepare phase, the coordinator node sends a prepare message to all participant nodes, asking them to prepare to commit the transaction. If all participant nodes respond with a yes vote, the coordinator sends a commit message to all participants, instructing them to commit the transaction. If any participant responds with a no vote, the coordinator sends an abort message to all participants, instructing them to abort the transaction.

2. **Three-phase commit (3PC)**: This protocol is similar to 2PC, but adds an additional phase, the pre-commit phase. In the pre-commit phase, the coordinator sends a pre-commit message to all participants, instructing them to prepare to commit the transaction. If all participants respond with a yes vote, the coordinator sends a commit message to all participants, instructing them to commit the transaction. If any participant responds with a no vote, the coordinator sends an abort message to all participants, instructing them to abort the transaction.

3. **Paxos commit**: This protocol is based on the Paxos consensus algorithm and involves multiple rounds of voting to reach a consensus on the final outcome of the transaction. The protocol is fault-tolerant and can handle the failure of one or more nodes in the system.

These are some of the most commonly used commit protocols in distributed systems. Each protocol has its own advantages and disadvantages, and the choice of protocol depends on the specific requirements of the system. It is important to carefully consider the trade-offs between performance, fault tolerance, and consistency when choosing a commit protocol for a distributed system.



### Voting protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

Voting protocols are used in distributed systems to achieve fault tolerance. They are used to ensure that the system can continue to function correctly even in the presence of failures. Here are some key points to remember about voting protocols:

1. Voting protocols are used to achieve consensus among the nodes in a distributed system.
2. The basic idea behind voting protocols is to have the nodes in the system vote on the value of a data item or the outcome of an operation.
3. The system can tolerate a certain number of failures, as long as the number of correct votes exceeds the number of failed votes.
4. There are different types of voting protocols, including majority voting, weighted voting, and hierarchical voting.
5. In majority voting, the value or outcome that receives the most votes is chosen.
6. In weighted voting, each node is assigned a weight, and the value or outcome that receives the most weight is chosen.
7. In hierarchical voting, the nodes are organized into a hierarchy, and the value or outcome is determined by the votes of the nodes at different levels of the hierarchy.
8. Voting protocols can be used in combination with other fault tolerance techniques, such as replication and checkpointing, to improve the reliability of the system.




### Dynamic Voting Protocols

Dynamic voting protocols are used in distributed systems to achieve fault tolerance. These protocols allow for the dynamic adjustment of the number of votes required to make a decision, based on the current state of the system. This can help to ensure that the system can continue to function even in the presence of failures.

Some key points to consider when studying dynamic voting protocols for fault tolerance in distributed systems include:

1. Dynamic voting protocols can help to ensure that the system can continue to function even in the presence of failures.
2. These protocols allow for the dynamic adjustment of the number of votes required to make a decision, based on the current state of the system.
3. The use of dynamic voting protocols can help to improve the availability and reliability of a distributed system.
4. There are several different approaches to implementing dynamic voting protocols, including the use of quorum-based techniques and weighted voting.
5. The choice of a particular dynamic voting protocol will depend on the specific requirements of the distributed system, including the level of fault tolerance required and the nature of the failures that the system must be able to withstand.
6. It is important to carefully design and test dynamic voting protocols to ensure that they provide the desired level of fault tolerance and do not introduce new vulnerabilities into the system.




## Unit 8 - Transactions and Concurrency Control

1. **Transactions** are a sequence of database operations that are treated as a single logical unit of work. They are used to ensure data consistency and integrity in the database.

2. **Concurrency control** is the process of managing simultaneous access to a database by multiple users. It is used to ensure that transactions are executed in a way that maintains the consistency and integrity of the data.

3. **Locking** is a common concurrency control technique that is used to prevent multiple transactions from accessing the same data at the same time. When a transaction wants to access a piece of data, it must first acquire a lock on that data. If another transaction already holds a lock on the data, the requesting transaction must wait until the lock is released.

4. **Deadlocks** can occur when two or more transactions are waiting for each other to release locks. Deadlock prevention and detection techniques are used to avoid or resolve deadlocks.

5. **Isolation levels** determine the degree to which one transaction is isolated from the effects of other transactions. Higher isolation levels provide stronger guarantees of consistency, but can reduce concurrency and performance.

6. **Two-phase locking (2PL)** is a concurrency control protocol that uses locking to ensure serializability of transactions. In the first phase, a transaction acquires all the locks it needs. In the second phase, it releases all the locks.

7. **Timestamp ordering (TO)** is a concurrency control protocol that assigns a timestamp to each transaction and uses the timestamps to determine the order in which transactions are allowed to execute.

8. **Optimistic concurrency control (OCC)** is a concurrency control protocol that assumes that conflicts between transactions are rare and allows transactions to execute without acquiring locks. Conflicts are detected at commit time, and if a conflict is detected, one of the conflicting transactions is rolled back and must be retried.

9. **Multi-version concurrency control (MVCC)** is a concurrency control protocol that allows multiple versions of the same data to exist at the same time. Transactions can read a consistent snapshot of the database without acquiring locks, which can improve concurrency and performance.



### Transactions
A transaction is a logical unit of work that contains one or more database operations. These operations can include reading, updating, inserting, or deleting data in a database. Transactions are used to ensure that data remains consistent and correct, even in the presence of failures or concurrent access.

Here are some key points to remember about transactions in the context of distributed systems and concurrency control:

1. **Atomicity**: Transactions are atomic, meaning that either all of the operations within a transaction are completed successfully, or none of them are. If a failure occurs during a transaction, any changes that were made are rolled back to their previous state.

2. **Consistency**: Transactions ensure that the database remains in a consistent state. This means that any constraints or rules that apply to the data are enforced, and that the data remains correct and accurate.

3. **Isolation**: Transactions are isolated from one another, meaning that the changes made by one transaction are not visible to other transactions until the first transaction has completed. This ensures that transactions do not interfere with one another and that the data remains consistent.

4. **Durability**: Once a transaction has completed successfully, its changes are permanent and will survive any subsequent failures. This ensures that data is not lost or corrupted.

Concurrency control is the process of managing concurrent access to data in a database. In a distributed system, concurrency control is particularly important, as multiple users or processes may be accessing the data simultaneously. Concurrency control mechanisms, such as locking or timestamp ordering, are used to ensure that transactions are executed in a way that maintains the consistency and correctness of the data.

In summary, transactions are a fundamental concept in distributed systems and are used to ensure that data remains consistent and correct, even in the presence of failures or concurrent access. Concurrency control mechanisms are used to manage concurrent access to data and ensure that transactions are executed in a way that maintains the consistency and correctness of the data.



### Nested Transactions

Nested transactions are a type of transaction that allows for sub-transactions within a larger transaction. This is useful in distributed systems where multiple operations may need to be performed as part of a single transaction.

Some key points to remember about nested transactions are:

1. Nested transactions allow for more fine-grained control over the operations within a transaction.
2. Each sub-transaction can be committed or aborted independently of the others.
3. If a sub-transaction is aborted, it can be retried without affecting the other sub-transactions.
4. If the parent transaction is aborted, all sub-transactions are also aborted.
5. Nested transactions can help improve the performance of distributed systems by reducing the need for global coordination.

In summary, nested transactions provide a useful mechanism for managing complex transactions in distributed systems. They allow for more fine-grained control over the operations within a transaction and can help improve performance by reducing the need for global coordination.



### Locks for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- Locks are a mechanism used to ensure that transactions are executed in a safe and consistent manner in a distributed system.
- Locks can be used to prevent multiple transactions from accessing the same data simultaneously, which can lead to inconsistencies and conflicts.
- There are two main types of locks: shared locks and exclusive locks.
- Shared locks allow multiple transactions to read the same data simultaneously, but prevent any transaction from writing to the data.
- Exclusive locks allow a single transaction to both read and write to the data, but prevent any other transaction from accessing the data.
- Locks can be implemented at different levels of granularity, such as at the row level, page level, or table level.
- Locks can be acquired and released explicitly by the transaction, or they can be managed automatically by the system.
- Deadlocks can occur when two or more transactions are waiting for each other to release locks. Deadlock detection and resolution techniques can be used to prevent or resolve deadlocks.
- Locks are an important part of concurrency control in distributed systems, and help ensure the consistency and integrity of the data.



### Optimistic Concurrency Control

Optimistic Concurrency Control (OCC) is a method used in distributed systems to manage transactions and concurrency control. It is based on the assumption that conflicts between transactions are rare and that it is more efficient to allow transactions to execute concurrently and then check for conflicts at the end, rather than locking resources and preventing conflicts from occurring.

Here are some key points to remember about Optimistic Concurrency Control:

1. OCC allows transactions to execute concurrently without acquiring locks on the data they access.
2. At the end of a transaction, the system checks for conflicts with other transactions that have executed concurrently.
3. If a conflict is detected, the transaction is rolled back and must be restarted.
4. OCC is most effective in systems where conflicts between transactions are rare.
5. OCC can reduce the overhead of locking and increase system performance in such systems.

In summary, Optimistic Concurrency Control is a method used in distributed systems to manage transactions and concurrency control. It allows transactions to execute concurrently without acquiring locks, and checks for conflicts at the end of a transaction. OCC can be an effective way to increase system performance in systems where conflicts between transactions are rare.



### Timestamp Ordering

Timestamp ordering is a concurrency control protocol used in distributed systems to ensure serializability of transactions. It assigns a unique timestamp to each transaction, which represents the transaction's start time. The timestamps are used to determine the order in which conflicting operations are executed.

Here are some key points to remember about timestamp ordering:

1. Each transaction is assigned a unique timestamp when it starts.
2. The timestamp of a transaction is used to determine the order in which conflicting operations are executed.
3. If two transactions conflict, the one with the earlier timestamp is executed first.
4. If a transaction is aborted, it is assigned a new timestamp when it is restarted.
5. Timestamp ordering ensures serializability, but it may not prevent cascading aborts.




### Comparison of methods for concurrency control for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

Concurrency control is the process of managing simultaneous execution of transactions in a shared database, to ensure the consistency and isolation of transactions. There are several methods for concurrency control, including:

1. **Locking**: This method uses locks to control access to data. A transaction must acquire a lock on an object before it can access it. Locks can be shared or exclusive, and can be applied at different levels of granularity.

2. **Timestamp ordering**: This method assigns a unique timestamp to each transaction, and uses these timestamps to determine the order in which transactions are allowed to execute. Transactions with earlier timestamps are given priority over transactions with later timestamps.

3. **Optimistic concurrency control**: This method assumes that conflicts between transactions are rare, and allows transactions to execute without acquiring locks. At the end of the transaction, the system checks for conflicts, and if any are found, the transaction is rolled back and restarted.

4. **Multiversion concurrency control**: This method maintains multiple versions of data, and allows transactions to access the version of the data that was current at the start of the transaction. This can reduce the need for locking, and can improve performance in some cases.

Each of these methods has its own advantages and disadvantages, and the choice of method will depend on the specific requirements of the system. It is important to carefully evaluate the trade-offs between performance, consistency, and isolation when choosing a concurrency control method for a distributed system.



## Unit 9 - Distributed Transactions

1. **Introduction:** A distributed transaction is a transaction that spans multiple systems, typically databases, and ensures that all changes are committed or rolled back across all systems.

2. **Two-Phase Commit Protocol:** The two-phase commit protocol is a distributed algorithm used to coordinate the commit or rollback of a distributed transaction. The first phase, called the prepare phase, involves each participating system voting on whether to commit or abort the transaction. The second phase, called the commit phase, involves the coordinator sending a commit or abort message to all participants based on the outcome of the vote.

3. **Three-Phase Commit Protocol:** The three-phase commit protocol is an extension of the two-phase commit protocol that adds an additional phase, called the pre-commit phase, to reduce the risk of blocking in the event of a coordinator failure.

4. **Global Transaction Identifier:** A global transaction identifier is a unique identifier assigned to a distributed transaction by the coordinator. It is used to track the progress of the transaction across all participating systems.

5. **Distributed Deadlocks:** Distributed deadlocks can occur when multiple transactions are waiting for resources held by other transactions in a distributed system. Deadlock detection and resolution techniques, such as timeouts and deadlock detection algorithms, can be used to prevent or resolve distributed deadlocks.

6. **Distributed Concurrency Control:** Distributed concurrency control mechanisms, such as distributed locking and distributed timestamp ordering, can be used to ensure the consistency and isolation of distributed transactions.

7. **Recovery:** Recovery mechanisms, such as write-ahead logging and checkpointing, can be used to ensure the durability of distributed transactions in the event of a system failure.

8. **Summary:** Distributed transactions provide a mechanism for ensuring the consistency and durability of changes made to multiple systems in a distributed environment. The two-phase and three-phase commit protocols are commonly used to coordinate the commit or rollback of distributed transactions. Distributed concurrency control and recovery mechanisms are also important for ensuring the correctness and durability of distributed transactions.



### Flat and Nested Distributed Transactions

- A flat or nested transaction that accesses objects handled by different servers is referred to as a distributed transaction.
- When a distributed transaction reaches its end, in order to maintain the atomicity property of the transaction, it is mandatory that all of the servers involved in the transaction either commit the transaction or abort it.
- Distributed transactions can be structured in two different ways: Flat transactions and Nested transactions.
- A flat transaction has a single initiating point (Begin) and a single end point (Commit or abort).
- Flat transactions are usually very simple and are generally used for short activities rather than larger ones.
- Flat transactions are the most prevalent model and are supported by most commercial database systems.
- Although nested transactions offer a finer granularity of control over transactions, they are supported by far fewer commercial database systems.
- The distributed transaction takes a bottom-up approach while the nested transaction takes a top-down approach to decompose a complex transaction into subtransactions.
- Distributed transactions provided global integrity constraints over multiple resources. These resources soon started to be heterogeneous as well.



### Atomic Commit protocols for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

- Atomic Commit protocols are used in distributed systems to ensure that a transaction is either committed on all sites or aborted on all sites.
- The goal of these protocols is to achieve atomicity, which means that either all changes made by a transaction are committed or none are.
- There are two main types of atomic commit protocols: Two-Phase Commit (2PC) and Three-Phase Commit (3PC).
- In 2PC, the coordinator sends a prepare message to all participants, asking them to vote on whether to commit or abort the transaction. If all participants vote to commit, the coordinator sends a commit message to all participants. If any participant votes to abort, the coordinator sends an abort message to all participants.
- In 3PC, there is an additional phase called the pre-commit phase. In this phase, the coordinator sends a pre-commit message to all participants, asking them to prepare to commit. If all participants respond with a yes, the coordinator sends a do-commit message to all participants. If any participant responds with a no, the coordinator sends an abort message to all participants.
- Both 2PC and 3PC have their advantages and disadvantages. 2PC is simpler but can result in blocking if the coordinator fails. 3PC is more complex but can avoid blocking in some failure scenarios.
- Atomic Commit protocols are an essential part of distributed transactions and help ensure data consistency in distributed systems.



### Concurrency control in distributed transactions

Concurrency control in distributed transactions refers to the mechanism used to synchronize distributed transactions in such a way that the ACID properties are not violated by their interleaved execution. These transactions are performed in a distributed database system where relevant data is hosted by a group of linked data servers.

Some of the methods used for concurrency control in distributed transactions include:

1. **Locking-based concurrency control protocols**: These protocols use the concept of locking data to ensure that only one transaction can access the data at a time.
2. **Timestamp-based concurrency control algorithms**: These algorithms use a transaction’s timestamp to determine the order in which transactions should be executed.
3. **Optimistic concurrency control**: This method assumes that conflicts between transactions are rare and allows transactions to execute concurrently. Conflicts are detected at the end of the transaction and resolved by aborting and restarting one of the conflicting transactions.
4. **2PC***: This is a novel distributed transaction control protocol that can extract more concurrent processing capabilities under high-intensity competitive workloads than previous approaches for a multi-microservice. 2PC* is an optimized protocol based on the traditional 2PC.

These are some of the methods used for concurrency control in distributed transactions. Each method has its own advantages and disadvantages and the choice of method depends on the specific requirements of the system.



### Distributed Deadlocks

Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems. It may be identified via a distributed technique like edge chasing or by creating a global wait-for graph (WFG) from local wait-for graphs at a deadlock detector.

In distributed systems, there are two main categories of deadlocks: Resource Deadlock and Communication Deadlock. Resource deadlock refers to the deadlock state when the resource required by the first process is locked by the second one and the resource required by the second process is locked by the first process.

Deadlocks can be dealt with using any one of the following three strategies: deadlock prevention, deadlock avoidance, and deadlock detection. In the distributed approach, different nodes work together to detect deadlocks. No single point failure (that is the whole system is dependent on one node if that node fails the whole system crashes) as the workload is equally divided among all nodes.



### Transaction Recovery

Transaction recovery is the procedure of eliminating the adverse effects of faulty transactions in a distributed database system. In distributed databases, recovery is the most difficult procedure. It is extremely difficult to recover a communication network system that has failed.

There are instances in which a transaction may fail for a variety of causes such as system failure, hardware failure, network error, inaccurate or invalid data, application problems, etc. Failures in the midst of a transaction processing, such as the failure of a site where a subtransaction is being processed, may lead to an inconsistent database. As such, a recovery subsystem is an essential component of a distributed database system.

A distributed transaction is a transaction that affects several resources. For a distributed transaction to commit, all participants must guarantee that any change to data will be permanent. Changes must persist despite system crashes or other unforeseen events.



## Unit 10 - Replication

1. Replication is the process by which genetic information is copied from one DNA molecule to another.
2. This process is essential for cell division, as each new cell must receive an exact copy of the genetic information from the parent cell.
3. Replication occurs during the S phase of the cell cycle, when the DNA is unwound and separated into two strands.
4. Each strand serves as a template for the synthesis of a new complementary strand, resulting in the formation of two identical DNA molecules.
5. The process of replication is carried out by a complex of enzymes and proteins, including DNA polymerase, helicase, primase, and ligase.
6. Replication is a highly regulated process, with multiple checkpoints to ensure the accuracy and fidelity of the newly synthesized DNA.
7. Errors in replication can lead to mutations, which can have serious consequences for the cell and the organism.
8. Replication is not limited to DNA, but can also occur with other genetic material such as RNA.




### System Model and Group Communication

In the context of replication in distributed systems, the system model and group communication play a crucial role. Here are some key points to consider:

1. **System Model:** The system model defines the assumptions made about the system, such as the type of failures that can occur, the timing model, and the communication model. Common system models include the synchronous model, the asynchronous model, and the partially synchronous model.

2. **Group Communication:** Group communication refers to the exchange of messages between multiple processes in a distributed system. It is used to coordinate the actions of the processes and to ensure consistency among replicas.

3. **Reliable Group Communication:** Reliable group communication ensures that messages are delivered to all members of the group in a reliable and ordered manner. This is important for maintaining consistency among replicas.

4. **Atomic Broadcast:** Atomic broadcast is a type of reliable group communication that ensures that messages are delivered to all members of the group in the same order. This is important for maintaining consistency among replicas.

5. **Virtual Synchrony:** Virtual synchrony is a group communication model that provides the illusion of synchronous execution in an asynchronous system. It ensures that all members of the group see the same sequence of events, even in the presence of failures.

These are some of the key concepts related to system model and group communication in the context of replication in distributed systems. Understanding these concepts is important for designing and implementing effective replication strategies.



### Fault – tolerant services

Fault-tolerant services are designed to ensure that a system continues to operate even in the presence of failures. This is achieved through the use of replication, where multiple copies of the same data or service are maintained. In the context of distributed systems, fault tolerance is achieved through the use of redundant components and the ability to recover from failures.

Some key points to consider when designing fault-tolerant services in distributed systems include:

1. **Replication:** Replication is the process of maintaining multiple copies of the same data or service. This can be achieved through the use of redundant hardware or software components.

2. **Consistency:** Ensuring consistency among replicas is a key challenge in designing fault-tolerant services. This can be achieved through the use of consensus algorithms or other coordination mechanisms.

3. **Failure detection and recovery:** Fault-tolerant services must be able to detect and recover from failures. This can be achieved through the use of monitoring and recovery mechanisms.

4. **Load balancing:** Load balancing is the process of distributing workloads across multiple components to ensure that no single component becomes a bottleneck. This can help to improve the overall performance and reliability of the system.

Overall, the design of fault-tolerant services in distributed systems requires careful consideration of the trade-offs between performance, reliability, and consistency. By using replication and other techniques, it is possible to build systems that can continue to operate even in the presence of failures.



### Highly Available Services

Highly available services are an essential component of distributed systems, as they ensure that the system remains operational even in the event of failures. Here are some key points to consider when designing highly available services for distributed systems:

1. **Replication**: Replication is the process of creating and maintaining multiple copies of data or services across different nodes in a distributed system. This ensures that even if one node fails, the data or service remains available on other nodes.

2. **Fault tolerance**: Fault tolerance refers to the ability of a system to continue functioning even in the presence of failures. This can be achieved through techniques such as redundancy, where multiple copies of the same data or service are maintained, and failover, where a backup system takes over in the event of a failure.

3. **Load balancing**: Load balancing is the process of distributing workloads across multiple nodes in a distributed system to ensure that no single node becomes a bottleneck. This can help to improve the availability of the system by ensuring that requests are handled by the most available node.

4. **Monitoring**: Monitoring is essential for maintaining the availability of a distributed system. By continuously monitoring the health and performance of the system, it is possible to detect and respond to failures quickly, minimizing downtime.

5. **Recovery**: Recovery refers to the process of restoring a system to its normal state after a failure. This can involve techniques such as data backup and restoration, as well as the use of redundant systems to ensure that the system remains available even during the recovery process.

In summary, highly available services are an essential component of distributed systems, and can be achieved through techniques such as replication, fault tolerance, load balancing, monitoring, and recovery. These techniques help to ensure that the system remains operational even in the event of failures, minimizing downtime and improving the overall availability of the system.



### Transactions with replicated data

In a distributed system, data replication is the process of storing copies of data on multiple nodes to improve data availability, reliability, and performance. Transactions with replicated data involve executing operations on multiple copies of the data.

Here are some key points to consider when dealing with transactions with replicated data:

1. **Consistency**: Ensuring consistency among replicas is a major challenge when dealing with transactions with replicated data. One approach to maintaining consistency is to use a distributed concurrency control protocol, such as two-phase commit, to coordinate updates to the replicas.

2. **Conflict resolution**: Conflicts can arise when multiple transactions attempt to update the same data item concurrently. Conflict resolution techniques, such as timestamp ordering or majority voting, can be used to resolve these conflicts and ensure that the replicas remain consistent.

3. **Fault tolerance**: Replication can improve the fault tolerance of a distributed system by allowing transactions to continue even if some replicas become unavailable due to failures. However, it is important to ensure that the system can recover from failures and restore consistency among the replicas.

4. **Performance**: Replication can improve the performance of a distributed system by allowing transactions to access data from nearby replicas, reducing the need for remote data access. However, the overhead of maintaining consistency among the replicas can impact performance, so it is important to carefully balance the benefits of replication against the costs.

These are some of the key considerations when dealing with transactions with replicated data in a distributed system. It is important to carefully design and implement replication and concurrency control mechanisms to ensure that the system can provide high levels of consistency, fault tolerance, and performance.

