## Unit 3 - Overview of Cluster Computing

Cluster computing is a collection of tightly or loosely connected computers that work together so that they act as a single entity. The connected computers execute operations all together thus creating the idea of a single system. The clusters are generally connected through fast local area networks (LANs) .

The following diagram illustrates the basic architecture of a cluster computing system:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Application   |     |   Application   |     |   Application   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Middleware    |     |   Middleware    |     |   Middleware    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Operating     |     |   Operating     |     |   Operating     |
|    System       |     |    System       |     |    System       |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Hardware     |     |    Hardware     |     |    Hardware     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       Node 1              Node 2              Node 3
         |                   |                   |
         |                   |                   |
         +-------------------+-------------------+
                         LAN
```

Each node in the cluster consists of four layers: hardware, operating system, middleware, and application. The hardware layer provides the physical components of the node, such as CPU, memory, disk, and network interface. The operating system layer provides the basic services for the node, such as file system, process management, and network communication. The middleware layer provides the software tools and libraries that enable the nodes to communicate and coordinate with each other, such as message passing, load balancing, and fault tolerance. The application layer provides the specific tasks that the cluster is designed to perform, such as scientific computing, web serving, or data analysis.

The cluster computing system can be classified into different types based on the degree of coupling, the hardware and software homogeneity, and the communication pattern. Some common types of clusters are:

- High-performance computing (HPC) clusters: These clusters are designed to provide high-speed computation for intensive tasks, such as numerical simulations, weather forecasting, and cryptography. They usually have tightly coupled nodes with homogeneous hardware and software, and use low-latency, high-bandwidth networks. They often use parallel programming models, such as MPI or OpenMP, to distribute the workload among the nodes.
- High-availability (HA) clusters: These clusters are designed to provide continuous service for critical applications, such as databases, web servers, and email servers. They usually have loosely coupled nodes with heterogeneous hardware and software, and use standard LANs or WANs. They often use replication and failover techniques, such as RAID or heartbeat, to ensure the reliability and availability of the system.
- Load-balancing clusters: These clusters are designed to distribute the incoming requests among multiple nodes, such as web servers, application servers, or proxy servers. They usually have loosely coupled nodes with heterogeneous hardware and software, and use standard LANs or WANs. They often use load-balancing algorithms, such as round-robin or least-connection, to optimize the performance and scalability of the system.
- Grid computing clusters: These clusters are designed to share the resources and services among multiple organizations or domains, such as scientific research, education, or business. They usually have loosely coupled nodes with heterogeneous hardware and software, and use the Internet or other WANs. They often use grid middleware, such as Globus or Condor, to enable the discovery, access, and coordination of the distributed resources.