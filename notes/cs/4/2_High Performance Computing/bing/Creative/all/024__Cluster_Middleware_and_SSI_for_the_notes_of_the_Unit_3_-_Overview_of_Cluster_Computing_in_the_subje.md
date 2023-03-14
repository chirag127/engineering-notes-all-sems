### Cluster Middleware and SSI for the notes of the Unit 3 - Overview of Cluster Computing in the subject of High Performance Computing

- Cluster middleware is a software layer that provides services and abstractions for cluster computing, such as resource management, communication, fault tolerance, load balancing, etc. 
- Single System Image (SSI) is a cluster middleware feature that creates an illusion of a single powerful resource from a collection of interconnected nodes.  
- SSI makes the cluster appear like a single machine to the user, to applications, and to the network. 
- SSI is supported by a middleware layer that resides between the OS and the user-level environment. The middleware consists of two sub-layers of software infrastructure: 
  - SSI infrastructure: provides services such as process migration, single process space, single root, single I/O space, single IPC space, cluster IP address, etc.  
  - System Availability Infrastructure (SAI): provides services such as checkpointing, automatic failover, recovery from failure, and fault tolerance.  
- SSI can improve the performance, scalability, availability, and usability of cluster systems.  
- SSI can also pose some challenges, such as maintaining consistency, security, and heterogeneity of cluster nodes.  
- Some examples of SSI cluster systems are OpenSSI, MOSIX, Kerrighed, HP TruCluster, and HP VMScluster.