 Here is the content in markdown format for the given topic:

### Cluster Systems for the notes of the Unit 3 - Overview of Cluster Computing in the subject of High Performance Computing

- A cluster is a group of loosely connected computers that work together closely, so that in many respects they can be viewed as a single system.
- Clusters are commonly used for parallel processing, load balancing, and fault tolerance.
- The components of a cluster are usually connected to each other through fast local area networks. Each node in a cluster has its own memory, CPU, and storage, but coordinates with the other nodes to execute parallel applications and to handle failover.
- Advantages of cluster systems:
    - Cost-effectiveness: Cluster systems are more cost-effective than supercomputers as they use existing hardware components arranged in a network.
    - Scalability: Additional computers/nodes can be easily added to the cluster to increase the computational power. This scalability makes clusters ideal for tasks that require a large amount of computing power.
    - Fault tolerance: If one node fails, the task assigned to that node can be reassigned to another node. This ensures high availability and fault tolerance.
- Disadvantages of cluster systems:
    - Complex software: Specialized software is required to effectively manage and coordinate the cluster resources. This software can be complex to install and maintain.
    - Bandwidth requirements: The nodes in the cluster need to be connected via a high-speed network to avoid bottlenecks. This can increase the cost for network connectivity and bandwidth.
    - Programming challenges: It can be challenging to partition and coordinate parallel programs across the cluster. Extra effort is required to parallelize algorithms and applications for distribution across multiple nodes.
- Applications of cluster systems: Cluster systems are widely used for applications such as web serving, scientific computing, database handling, enterprise resource planning, etc. that require a large amount of computing power, high availability, and fault tolerance.