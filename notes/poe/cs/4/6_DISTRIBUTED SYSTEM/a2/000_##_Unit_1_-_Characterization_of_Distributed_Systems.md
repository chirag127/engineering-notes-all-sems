 Here is the content in markdown format for the topic ## Unit 1 - Characterization of Distributed Systems:

## Unit 1 - Characterization of Distributed Systems

- A distributed system consists of multiple autonomous computers that communicate and coordinate their actions by passing messages.
- The computers that are a part of the distributed system are called nodes. The nodes are interconnected by a communication network.
- The nodes can be heterogeneous or homogeneous. Heterogeneous nodes have different hardware and software configurations. Homogeneous nodes have similar hardware and software configurations.
- The distribution of the system is transparent to the user. The user interacts with the system as a single entity though the processing is carried out by multiple nodes.
- The key characteristic features of a distributed system are:
    - Concurrency: The different nodes of the system operate concurrently. The operations are not performed sequentially one after the other. This increases the efficiency but also introduces issues like race conditions.
    - Lack of shared memory: The nodes do not share memory. Each node has its own local memory. The nodes have to exchange messages to share data and synchronize their actions.
    - Independent failure: The nodes are independent and can fail independently. This can affect the availability of the system and resources. The system must be fault-tolerant and resilient to handle such failures.
    - Dynamic behaviour: The behaviour of the system is dynamic. The nodes can join or leave the system. The system must handle such dynamic membership changes.
    - Resource sharing: The nodes share system resources like files, storage, peripherals, etc. This requires mechanisms to coordinate the access to the shared resources.
- Some examples of distributed systems are the Internet, distributed databases, and cloud computing systems. The main advantages of distributed systems are resource sharing, reliability, scalability, and performance. However, they are complex to design and manage due to issues like concurrency, lack of shared memory, partial failures, and dynamic behaviour.