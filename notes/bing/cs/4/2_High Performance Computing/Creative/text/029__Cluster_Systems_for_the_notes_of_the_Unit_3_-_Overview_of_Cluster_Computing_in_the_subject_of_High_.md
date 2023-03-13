### Cluster Systems

- Cluster systems are a type of high performance computing (HPC) architecture that consist of two or more individual computer systems, called nodes, that work together as a parallel unit to perform computational tasks .
- Cluster systems result in high performance as they can distribute the workload among the nodes and leverage the hardware made for consumer and general business usage .
- Cluster systems also provide fault tolerance, as the failure of one node does not affect the functionality of the entire cluster.
- Cluster systems consist of the following components  :
  - A cluster provisioner that ensures node homogeneity and manages the installation and configuration of the cluster software and hardware.
  - Servers or nodes that perform the computation. Nodes can be classified into different types, such as head nodes, compute nodes, login nodes, storage nodes, etc., depending on their role and function in the cluster.
  - A scheduler that queues up workloads against the cluster resources and allocates them to the nodes according to some policies and criteria.
  - A network for communication between nodes. The network can be based on different technologies, such as Ethernet, InfiniBand, or Omni-Path, and can have different topologies, such as star, ring, or mesh, depending on the performance and scalability requirements of the cluster.
  - A general-purpose storage solution used to store applications and user data. The storage solution can be based on different technologies, such as NFS, SAN, or NAS, and can have different levels of redundancy and availability.
  - A high-speed, low-latency clustered file system generally used for computational storage. The clustered file system allows multiple nodes to access the same data concurrently and provides high throughput and performance for data-intensive applications. Examples of clustered file systems are Lustre, GPFS, and BeeGFS.