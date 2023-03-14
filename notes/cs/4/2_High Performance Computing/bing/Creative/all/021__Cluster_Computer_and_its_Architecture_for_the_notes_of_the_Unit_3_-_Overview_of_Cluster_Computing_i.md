### Cluster Computer and its Architecture for the notes of the Unit 3 - Overview of Cluster Computing in the subject of High Performance Computing

- A cluster computer is a set of computers (nodes) that work together as a single system.     
- The nodes are usually connected by a fast local area network and run the same task, controlled and scheduled by software.  
- The nodes can range from simple desktop-class computers to massive high-end servers, depending on the application and performance requirements.  
- The main advantages of cluster computing are:
  - Improved performance and scalability: by distributing the workload among multiple nodes, the cluster can achieve faster results and handle larger problems.   
  - Increased availability and reliability: by having redundant nodes, the cluster can tolerate node failures and continue to provide service.   
  - Cost-effectiveness: by using low-cost commercial off-the-shelf computers, the cluster can be much cheaper than a single computer of comparable speed or availability.    
- The main challenges of cluster computing are:
  - Complexity and management: the cluster requires software and hardware coordination, load balancing, fault tolerance, synchronization, and security.   
  - Communication and network: the cluster depends on the network quality and bandwidth to exchange data and messages among the nodes.   
  - Compatibility and standardization: the cluster may need to ensure that the nodes have the same hardware and software specifications, or use common protocols and interfaces.   
- The basic components of a cluster computer architecture are:   
  - Computing nodes: the servers that process the user load and run the same task.
  - Managing nodes: the servers that monitor the cluster hardware and software, and take measures to reconfigure it according to any event. They can also run on computing nodes to save resources.
  - Private network(s): the network that connects the nodes and allows them to communicate and coordinate. It is responsible for the heartbeat messages that check the node status, and the command messages that reconfigure and synchronize the cluster.
  - Shared redundant storage: the storage that is accessible to all computing nodes and contains the common data. It is essential for a computing node to take over a failed one.
  - Public-access layer: the layer that virtualizes the access to the cluster and makes it look like a single system. It can create virtual IPs that host the service entry points, and distribute the incoming requests to the active nodes.
- The types of cluster computing are:   
  - High-performance computing (HPC) clusters: they aim to achieve the maximum performance and scalability for computationally intensive tasks, such as scientific simulations, data analysis, and machine learning. They use parallel processing and distributed memory models, and often employ specialized hardware such as GPUs and FPGAs.
  - High-availability (HA) clusters: they aim to provide continuous service and minimize downtime for critical applications, such as web servers, databases, and email servers. They use failover and load balancing mechanisms, and often employ redundant hardware such as RAID and UPS.
  - Load balancing clusters: they aim to distribute the workload among multiple nodes and optimize the resource utilization and response time for dynamic applications, such as web applications, e-commerce, and online gaming. They use load balancing algorithms and policies, and often employ caching and proxy servers.
  - Grid computing clusters: they aim to share and coordinate the resources of multiple clusters or organizations for large-scale and heterogeneous tasks, such as scientific collaborations, distributed databases, and volunteer computing. They use grid middleware and protocols, and often employ virtualization and cloud computing technologies.

: Computer cluster - Wikipedia
: Computer Clusters, Types, Uses and Applications | Baeldung on Computer Science
: An Overview of Cluster Computing - GeeksforGeeks
: Cluster Computing : Architecture & Its Types - WatElectronics.com
: Computer Cluster [What It Is & How