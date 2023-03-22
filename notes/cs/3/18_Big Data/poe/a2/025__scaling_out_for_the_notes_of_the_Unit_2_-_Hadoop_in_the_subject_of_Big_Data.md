 Here are the notes for Scaling out for Unit 2 - Hadoop in the subject of Big Data:

### Scaling out

- Horizontal scaling: Increasing the number of nodes in a cluster to handle the increased load. Also known as scaling out.
- Advantages:
  - Cost effective as commodity hardware can be used.
  - Higher aggregate resource utilization as the workload is distributed.
  - Fault tolerance is increased as there are multiple nodes. If some nodes fail, others can take over the work.
- Challenges:
  - Complexity in distributing and coordinating work across nodes.
  - Communication overhead between nodes can become a bottleneck.
  - Programming models become more complex to handle distribution of data and work.

Hadoop enables scaling out by:

- Breaking up large data into blocks and storing multiple replicas across nodes in a cluster.
- Distributing MapReduce tasks across nodes to process data in parallel.
- Handling failures at the application layer through replication and task reassignment.
- Using a simple programming model (MapReduce) to write distributed applications.

The benefits of scaling out outweigh the challenges for big data workloads due to:

- The volume of data and computational requirements exceeding the capabilities of a single large server.
- The low cost and increased aggregate resources/fault tolerance provided by a cluster of commodity nodes.
- The availability of frameworks like Hadoop that can handle the complexity of distribution and coordination.