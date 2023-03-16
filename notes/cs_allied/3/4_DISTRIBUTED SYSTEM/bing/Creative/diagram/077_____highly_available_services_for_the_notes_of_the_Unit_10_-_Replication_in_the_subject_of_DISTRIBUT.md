### Highly Available Services

- A highly available service is a service that can provide continuous and reliable operation despite failures or faults in the system.
- Replication is a technique for achieving high availability by creating and maintaining multiple copies of the same data or service on different nodes in a distributed system .
- Replication can improve availability by allowing the system to tolerate node failures, network partitions, or data corruption, as long as there are enough replicas that can serve the requests.
- Replication can also improve performance by reducing the load on a single node, increasing the throughput of the system, and reducing the latency for the clients.
- Replication can be classified into two types: eager replication and lazy replication .
  - Eager replication ensures that all replicas are updated as soon as a change occurs, using synchronous or atomic multicast protocols. This provides strong consistency and fault tolerance, but at the cost of higher communication overhead and lower availability in the presence of network failures.
  - Lazy replication allows some replicas to be updated later than others, using asynchronous or epidemic protocols. This provides higher availability and lower communication overhead, but at the cost of weaker consistency and possible conflicts or divergence.
- Replication can also be classified into two modes: primary-backup and active replication.
  - Primary-backup replication assigns a single replica as the primary, which is responsible for processing all the requests and updating the backups. This simplifies the implementation and avoids conflicts, but introduces a single point of failure and a performance bottleneck.
  - Active replication executes the same request on all replicas in the same order, using a consensus or a total order protocol. This eliminates the single point of failure and the performance bottleneck, but increases the complexity and the communication overhead.