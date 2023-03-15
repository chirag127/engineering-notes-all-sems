 Here is the content in markdown format for the topic ### Design issues in Distributed Shared Memory for the notes of the Unit 5 - Distributed Resource Management in the subject of DISTRIBUTED SYSTEM:

### Design issues in Distributed Shared Memory

- Consistency: Ensuring that all copies of shared data are updated atomically is challenging. Solutions like two-phase commit can reduce performance.
- Granularity: Choosing the right size for shared data objects impacts performance. Fine-grained sharing improves parallelism but increases overhead. Coarse-grained sharing reduces overhead but limits parallelism.
- Replication: Determining how many copies of shared data to maintain and where to locate them affects availability, latency, and consistency.
- Cache coherence: Keeping shared data coherent in local caches is difficult to implement efficiently. Invalidation-based and update-based protocols help but add overhead.
- Location transparency: Making the location of shared data transparent to processes simplifies programming but can reduce performance due to extra indirection and delayed binding of data to locations.

Some mnemonics to remember the design issues:

- CONSISTENCY: Atomic, durable, isolated, consistent
- GRANULARITY: Fine vs coarse, parallelism vs overhead trade-off
- REPLICATION: Availability vs latency vs consistency trade-off
- CACHE COHERENCE: Invalidation vs update, overhead
- LOCATION TRANSPARENCY: Simplicity vs performance trade-off

[Detailed diagrams and examples can be added here if required to understand the concepts better.]

The key advantages of distributed shared memory are simplified programming and location transparency. The major disadvantages are reduced performance and complex consistency management. Distributed shared memory is useful for applications where shared data access is irregular or fine-grained and consistency is important.