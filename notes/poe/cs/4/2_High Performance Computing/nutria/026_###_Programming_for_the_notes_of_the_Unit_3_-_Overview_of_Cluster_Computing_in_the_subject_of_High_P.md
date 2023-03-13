
### Programming for the Notes of the Unit 3 - Overview of Cluster Computing in the Subject of High Performance Computing

Cluster computing is an approach to distributed computing that involves connecting multiple computers to work together as a single system. Cluster computing is often used to increase performance and reliability of a system by providing redundancy and failover capabilities.

There are several programming models used in cluster computing, including message passing, shared memory, and distributed memory. Each model has its own advantages and disadvantages, so it is important to understand the requirements of the application and choose the appropriate model.

Message Passing: In this model, the nodes of a cluster communicate with each other using messages. Each node sends and receives messages and processes them asynchronously. This model is suitable for applications that require communication between nodes, and it is easy to implement.

Shared Memory: In this model, the nodes of a cluster share a single memory space. This allows for faster communication between nodes, since they do not need to send messages back and forth. However, it is difficult to implement, and it is not suitable for applications that require node-to-node communication.

Distributed Memory: In this model, each node has its own memory, and the nodes communicate by sending messages. This model is suitable for applications that require communication between nodes, and it is relatively easy to implement.

Mnemonics and Learning Tricks:

- **M**essage **P**assing **M**odel: **M**P**M**
- **S**hared **M**emory **M**odel: **S**M**M**
- **D**istributed **M**emory **M**odel: **D**M**M**