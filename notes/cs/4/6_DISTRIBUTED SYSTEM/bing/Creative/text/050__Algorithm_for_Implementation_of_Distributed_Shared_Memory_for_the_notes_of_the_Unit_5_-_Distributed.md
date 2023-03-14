### Algorithm for Implementation of Distributed Shared Memory

Distributed Shared Memory (DSM) is a resource management component of distributed operating system that implements shared memory model in distributed system which have no physically shared memory. The shared memory model provides a virtual address space which is shared by all nodes in a distributed system. The central issues in implementing DSM are:

- How to keep track of location of remote data.
- How to overcome communication overheads and delays involved in execution of communication protocols in system for accessing remote data.
- How to make shared data concurrently accessible at several nodes to improve performance.

There are four basic algorithms for implementing DSM:

- Central Server Algorithm
- Migration Algorithm
- Read Replication Algorithm
- Full Replication Algorithm

#### Central Server Algorithm

- All shared data is maintained by the central server.
- Other nodes of the distributed system request for reading and writing data to the server which serves the request and updates or provides access to the data along with acknowledgment messages.
- These acknowledgment messages are used to provide the status of the data request is served by the server.
- When the data is sent to the calling function, it acknowledges a number that shows the access sequence of the data to maintain concurrency.
- Time-out is returned in case of failure.
- For larger distributed systems, there can be more than one server. In this case, the servers are located using their address or using mapping functions.
- This algorithm is simple to implement but the central server can become a bottleneck and a single point of failure.

#### Migration Algorithm

- Instead of using a central server serving each request, the block containing the data requested by a system is migrated to it for further access and processing.
- It migrates the data on request.
- This algorithm is good if when a system accesses the same block of data multiple times and the ability to integrate virtual memory concept.
- However, this algorithm has some shortcomings that are needed to be addressed.
- Only one node is able to access the shared data element at a time and the whole block is migrated to that node.
- Also, this algorithm is more prone to thrashing due to the migration of data items upon request by the node.

#### Read Replication Algorithm

- In the read replication algorithm, the data block that is to be accessed is replicated and only reading is allowed in all the copies.
- If a write operation is to be done, then all read access is put on halt till all the copies are updated.
- This algorithm improves system performance by allowing multiple nodes to access data concurrently.
- However, the write operation in this algorithm is expensive as all copies of a shared block at various nodes will either have to invalidated or updated with the current value to maintain consistency of shared data block.
- DSM must keep track of location of all copies of data blocks in this algorithm.

#### Full Replication Algorithm

- This is an extension of read replication algorithm which allows multiple nodes to have both read and write access to shared data blocks.
- Since many nodes can write shared data concurrently, the access to shared data must be controlled to maintain its consistency.
- To maintain consistency, it can use a gap free sequences in which all nodes wishing to modify shared data will send the modification to sequencer which will then assign a sequence number and multicast the modification with sequence number to all nodes that have a copy of shared data item.
- This algorithm provides the highest degree of concurrency and fault tolerance but also the highest communication overhead and complexity.