### Cluster Computing

- Cluster computing is a form of parallel computing that involves connecting multiple computers (called nodes) on a network and using them as a single system for high-performance tasks   .
- Cluster computing provides benefits such as faster computational speed, enhanced data integrity, increased availability, load balancing and scalability .
- Cluster computing can be classified into different types based on the degree of coupling, the architecture, the communication pattern and the application domain  .
- Some common types of clusters are:
  - Beowulf cluster: A cluster of commodity hardware running Linux or other free software, designed for high-performance scientific computing .
  - Load-balancing cluster: A cluster that distributes the workload among the nodes to optimize the use of resources and improve the response time .
  - High-availability cluster: A cluster that provides redundancy and fault tolerance to ensure the continuity of service in case of node failures .
  - Grid cluster: A cluster that connects geographically distributed nodes over the internet or other networks, and allows sharing of data and resources among different organizations or domains .
- A typical cluster consists of two types of nodes: a head node and one or more compute nodes. The head node is responsible for managing the cluster, scheduling the tasks, and communicating with the users. The compute nodes are the ones that perform the actual computations and return the results to the head node.
- A cluster also requires a network infrastructure to connect the nodes and enable data transfer and communication. The network can be either a local area network (LAN) or a wide area network (WAN), depending on the distance and bandwidth between the nodes  .
- A cluster also needs a software environment that supports parallel programming, distributed processing, and cluster management. Some examples of cluster software are MPI, OpenMP, Hadoop, Spark, Kubernetes, and Slurm   .