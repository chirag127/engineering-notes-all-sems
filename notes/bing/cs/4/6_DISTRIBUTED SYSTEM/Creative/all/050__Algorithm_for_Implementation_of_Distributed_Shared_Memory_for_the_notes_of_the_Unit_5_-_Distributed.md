### Algorithm for Implementation of Distributed Shared Memory for the notes of the Unit 5 - Distributed Resource Management in the subject of DISTRIBUTED SYSTEM

Distributed Shared Memory (DSM) is a technique that allows multiple processes on different nodes of a distributed system to share a common virtual address space and access the same data. DSM provides the illusion of a shared memory system, even though the physical memory is distributed among the nodes.

There are different algorithms for implementing DSM, each with its own advantages and disadvantages. Here, we will briefly describe four basic algorithms: Central Server Algorithm, Migration Algorithm, Read Replication Algorithm, and Full Replication Algorithm.

#### Central Server Algorithm
- All shared data is maintained by the central server.
- Other nodes of the distributed system send read and write requests to the server.
- For read requests, the server returns the data to the requesting node.
- For write requests, the server updates the data and sends an acknowledgment to the requesting node.
- This algorithm is simple and easy to implement, but it has some drawbacks:
  - The server can become a bottleneck and a single point of failure.
  - The network traffic and latency can be high, especially for frequent write operations.
  - The algorithm does not exploit the locality of reference, i.e., the tendency of processes to access the same or nearby data repeatedly.

#### Migration Algorithm
- The shared data is initially stored at the central server, but it can migrate to other nodes as needed.
- When a node requests to read or write a data item, the server transfers the ownership of that item to the requesting node.
- The requesting node can then access the data locally, without contacting the server, until another node requests the same data item.
- When the ownership of a data item changes, the previous owner must invalidate its copy and the server must update its record.
- This algorithm reduces the network traffic and latency, and exploits the locality of reference, but it also has some drawbacks:
  - The algorithm can cause frequent data migration, especially for data items that are accessed by multiple nodes concurrently or alternately.
  - The algorithm can cause inconsistency and coherence problems, if the data items are not properly synchronized among the nodes.
  - The server still remains a bottleneck and a single point of failure.

#### Read Replication Algorithm
- The shared data is initially stored at the central server, but it can be replicated to other nodes for read-only access.
- When a node requests to read a data item, the server sends a copy of that item to the requesting node, and marks it as read-only.
- The requesting node can then read the data locally, without contacting the server, until the data item is modified by another node.
- When a node requests to write a data item, the server invalidates all the read-only copies of that item, and sends the updated data to the requesting node.
- This algorithm reduces the network traffic and latency for read operations, and exploits the locality of reference, but it also has some drawbacks:
  - The algorithm can cause high network traffic and latency for write operations, especially for data items that have many read-only copies.
  - The algorithm can cause inconsistency and coherence problems, if the data items are not properly synchronized among the nodes.
  - The server still remains a bottleneck and a single point of failure.

#### Full Replication Algorithm
- The shared data is fully replicated to all the nodes of the distributed system, and each node maintains a local copy of the data.
- When a node requests to read a data item, it can access its local copy, without contacting any other node.
- When a node requests to write a data item, it must broadcast the update to all the other nodes, and wait for their acknowledgments.
- This algorithm reduces the network traffic and latency for read operations, and eliminates the need for a central server, but it also has some drawbacks:
  - The algorithm can cause high network traffic and latency for write operations, especially for data items that are frequently modified.
  - The algorithm can cause inconsistency and coherence problems, if the data items are not properly synchronized among the nodes.
  - The algorithm can cause storage overhead, as each node must store the entire shared data.

#### Mnemonics and Learning Tricks
- To remember the four basic algorithms for implementing DSM, you can use the acronym **CRMF** (Central, Migration, Read, Full).
- To remember the advantages and disadvantages of each algorithm, you can use the following table:

| Algorithm | Advantages | Disadvantages |
|-----------|------------|---------------|
| Central   | Simple and easy | Server bottleneck, high traffic and latency, no locality |
| Migration |