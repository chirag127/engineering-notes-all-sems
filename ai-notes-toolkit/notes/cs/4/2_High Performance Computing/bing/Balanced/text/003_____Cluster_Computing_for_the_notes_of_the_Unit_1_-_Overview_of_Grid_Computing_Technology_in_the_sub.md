### Cluster Computing

- Cluster computing is a form of parallel computing that involves connecting multiple computers (called nodes) on a network to work together as a single system   .
- Cluster computing provides solutions to solve difficult problems by providing faster computational speed, enhanced data integrity, load balancing and high availability .
- Cluster computing can be classified into two types: loosely coupled and tightly coupled.
  - Loosely coupled clusters have each node running its own operating system and software, and communicate with each other through message passing.
  - Tightly coupled clusters have each node running the same operating system and software, and share memory and disk space.
- Cluster computing can also be categorized based on the purpose and functionality of the clusters, such as:
  - High-performance computing (HPC) clusters: These clusters are designed to perform intensive computations for scientific and engineering applications . An example of an HPC cluster is a Beowulf cluster, which is built with a few personal computers to produce a cost-effective alternative to traditional supercomputers.
  - High-availability (HA) clusters: These clusters are designed to provide continuous service and prevent downtime for critical applications. An example of an HA cluster is a failover cluster, which has a backup node that takes over the workload of a failed node.
  - Load-balancing clusters: These clusters are designed to distribute the workload among multiple nodes to improve performance and scalability. An example of a load-balancing cluster is a web server cluster, which handles requests from web clients and distributes them to different web servers.
- Cluster computing requires special software and hardware components to coordinate and manage the nodes, such as:
  - Cluster management software: This software is responsible for installing, configuring, monitoring and controlling the nodes and the cluster as a whole . Some examples of cluster management software are Rocks, Bright Cluster Manager and OpenHPC .
  - Cluster middleware: This software is responsible for providing communication, synchronization, scheduling and fault tolerance mechanisms for the nodes and the applications running on the cluster . Some examples of cluster middleware are MPI, OpenMP and PVM .
  - Cluster interconnect: This hardware is responsible for providing fast and reliable data transfer between the nodes on the cluster . Some examples of cluster interconnect are Ethernet, InfiniBand and Myrinet .
  - Cluster storage: This hardware is responsible for providing shared and distributed storage for the nodes and the applications on the cluster . Some examples of cluster storage are RAID, SAN and NAS .