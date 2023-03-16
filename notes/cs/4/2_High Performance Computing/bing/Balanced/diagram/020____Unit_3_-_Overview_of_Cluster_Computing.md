## Unit 3 - Overview of Cluster Computing

- Cluster computing is a form of distributed computing that involves a group of computers (called nodes) that work together as a single system.
- Cluster computing aims to provide faster computational speed, higher data integrity, better availability, and scalability for various applications.
- Cluster computing can be classified into different types based on the architecture, topology, and purpose of the nodes. Some common types are:
  - Beowulf cluster: A cluster of commodity hardware that runs Linux or other open-source software and is connected by a local area network (LAN).
  - High-availability cluster: A cluster that provides redundancy and fault tolerance for critical services by using heartbeat signals, failover mechanisms, and shared storage.
  - Load-balancing cluster: A cluster that distributes the workload among the nodes to optimize the performance and resource utilization of the system.
  - High-performance computing (HPC) cluster: A cluster that uses specialized hardware and software to achieve high speed and efficiency for scientific and engineering applications that require intensive calculations or large data sets.
- Cluster computing requires coordination and communication among the nodes, which can be achieved by using various software tools and protocols. Some examples are:
  - Message Passing Interface (MPI): A standard for parallel programming that allows the nodes to exchange messages and data using a common interface.
  - OpenMP: A standard for shared-memory parallel programming that allows the nodes to use multiple threads and synchronize their execution using directives and pragmas.
  - Hadoop: A framework for distributed processing of large data sets using a cluster of commodity hardware and a distributed file system (HDFS).
  - Kubernetes: A platform for managing containerized applications and services using a cluster of nodes and a control plane.