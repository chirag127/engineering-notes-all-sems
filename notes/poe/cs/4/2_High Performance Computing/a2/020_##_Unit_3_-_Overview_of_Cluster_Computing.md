 Here is the content in markdown format for the topic ## Unit 3 - Overview of Cluster Computing:

## Unit 3 - Overview of Cluster Computing

- A cluster is a group of computers that work together closely so that in many respects they can be viewed as a single system.
- Clusters are mainly used for parallel processing, high availability, and load balancing.
- The components of a cluster are:
    - Nodes: The individual computers that make up the cluster. They can be servers or personal computers.
    - Network: The high-speed network that interconnects the nodes in the cluster.
    - Software: The software needed to operate the cluster, such as an operating system and applications designed for clusters.
    - Administrative system: The software and tools needed to install, configure, monitor, and manage the cluster.
- The three main types of clusters are:
    1. High-availability clusters: The goal is to maximize the availability of applications and services. The nodes monitor each other, and if one fails, the remaining nodes take over its work.
    2. Load-balancing clusters: The goal is to distribute workloads across multiple nodes to improve performance. As nodes become free, new work is sent to them.
    3. High-performance computing (HPC) clusters: The goal is to solve large computational problems by harnessing the combined power of multiple nodes working in parallel. Special programming techniques are needed to divide up the work efficiently across the nodes.
- Advantages of clusters:
    - Increased performance: Clustering allows combining the computing power of multiple systems, enabling more work to be done in parallel.
    - High availability: Critical services and applications can be kept running even if some nodes fail.
    - Scalability: Clusters can grow by just adding more nodes, which is simpler than replacing individual systems with more powerful ones.
    - Cost effectiveness: Commodity hardware and open source software can be used to build clusters at lower cost.
- Disadvantages of clusters:
    - Complexity: Setting up and managing a cluster requires technical expertise.
    - Software challenges: Special programming techniques are required to parallelize work across nodes.
    - Reliability: Although clusters are designed to be highly available, as the number of components increases, so does the chance of part of the system failing.