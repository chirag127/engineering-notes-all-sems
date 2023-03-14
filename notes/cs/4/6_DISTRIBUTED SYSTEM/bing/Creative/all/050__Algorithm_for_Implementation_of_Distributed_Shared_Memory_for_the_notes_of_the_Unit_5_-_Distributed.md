### Algorithm for Implementation of Distributed Shared Memory for the notes of the Unit 5 - Distributed Resource Management in the subject of DISTRIBUTED SYSTEM

Distributed Shared Memory (DSM) is a resource management component of distributed operating system that implements shared memory model in distributed system which have no physically shared memory. The shared memory model provides a virtual address space which is shared by all nodes in a distributed system.

The central issues in implementing DSM are:

- How to keep track of location of remote data.
- How to overcome communication overheads and delays involved in execution of communication protocols in system for accessing remote data.
- How to make shared data concurrently accessible at several nodes to improve performance.

There are four basic algorithms for implementing DSM  :

- Central Server Algorithm
- Migration Algorithm
- Read Replication Algorithm
- Full Replication Algorithm

#### Central Server Algorithm

- All shared data is maintained by the central server  .
- Other nodes of the distributed system request for reading and writing data to the server which serves the request and updates or provides access to the data along with acknowledgment messages  .
- These acknowledgment messages are used to provide the status of the data request is served by the server .
- When the data is sent to the calling function, it acknowledges a number that shows the access sequence of the data to maintain concurrency .
- Time-out can be used in case of failed acknowledgment while sequence number can be used to avoid duplicate write requests .
- For larger distributed systems, there can be more than one server  .
- In this case, the servers are located using their address or using a mapping function to locate the appropriate server  .

Advantages:

- It is simpler to implement .
- It provides consistency and coherence of shared data.

Disadvantages:

- The central server can become a bottleneck and a single point of failure .
- It has high communication overhead and latency for remote data access .

#### Migration Algorithm

- In contrast to central server algorithm where every data access request is forwarded to location of data, in this algorithm the block containing the data requested by a system is migrated to it for further access and processing  .
- It migrates the data on request.
- This algorithm allows only one node to access a shared data at a time and the whole block containing data item migrates instead of individual item requested  .
- It is susceptible to thrashing where pages frequently migrate between nodes while servicing only a few requests .
- This algorithm provides an opportunity to integrate DSM with virtual memory provided by operating system at individual nodes .

Advantages:

- It reduces the communication overhead and latency for subsequent data access .
- It provides consistency and coherence of shared data.

Disadvantages:

- It has high migration cost and network traffic for initial data access .
- It does not allow concurrent access of shared data by multiple nodes .

#### Read Replication Algorithm

- This algorithm extends the migration algorithm by replicating data blocks and allowing multiple nodes to have read access or one node to have both read and write access  .
- It improves system performance by allowing multiple nodes to access data concurrently .
- The write operation in this algorithm is expensive as all copies of a shared block at various nodes will either have to invalidated or updated with the current value to maintain consistency of shared data block  .
- DSM must keep track of location of all copies of data blocks in this algorithm .

Advantages:

- It reduces the communication overhead and latency for read access .
- It allows concurrent read access of shared data by multiple nodes .

Disadvantages:

-