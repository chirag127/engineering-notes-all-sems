 Here is the content in markdown format:

### Design issues in Distributed Shared Memory for the notes of the Unit 5 - Distributed Resource Management in the subject of DISTRIBUTED SYSTEM

The following are the main design issues in Distributed Shared Memory:

1. Coherence: The value of a memory location can be cached in multiple nodes. This can lead to coherence problems where different nodes have different values for the same memory location. The system must ensure coherence between these values by using protocols.
2. Consistency: The system must ensure that operations on memory are performed in a consistent order. For example, if one process updates a memory location and then reads another location, other processes must see the update before the read. Weaker consistency models can improve performance but complicate programming.
3. Latency: Accessing remote memory can take longer than accessing local memory. This additional latency can affect performance, so data may need to be managed carefully to minimize remote accesses.
4. Bandwidth: The system may become bottlenecked on the bandwidth of the network connecting the nodes. Care must be taken to minimize excess data transfers and to exploit locality of reference.

Some possible mnemonics for remembering the design issues:

- Coherence: Keep your memories straight
- Consistency: Order matters
- Latency: Slow memory is painful
- Bandwidth: Don't overcrowd the network

Detailed diagrams and examples can be included if required. The advantages and disadvantages of distributed shared memory can also be discussed in detail. Applications such as shared databases can be mentioned where distributed shared memory is useful.

Overall, the key points to remember are coherence, consistency, latency, and bandwidth - the four main design issues that must be handled in distributed shared memory systems. With proper mechanisms to address these issues, distributed shared memory can be a convenient programming model for distributed systems.