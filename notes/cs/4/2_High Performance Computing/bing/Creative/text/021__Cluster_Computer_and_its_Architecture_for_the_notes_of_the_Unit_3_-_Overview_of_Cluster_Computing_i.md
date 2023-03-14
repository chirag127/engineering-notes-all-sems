### Cluster Computer and its Architecture

- A cluster computer is a set of computers (nodes) that work together as a single system.     
- The nodes are usually connected by a fast local area network and run the same task, controlled and scheduled by software.  
- The nodes can range from simple desktop-class computers to massive high-end servers, depending on the application and performance requirements.  
- The cluster computer has several advantages over a single computer, such as:
  - Higher processing power and scalability: the cluster can handle more workload and can be expanded by adding more nodes.   
  - Higher availability and reliability: the cluster can tolerate node failures and continue to operate without interruption.   
  - Lower cost and energy consumption: the cluster can use low-cost and energy-efficient hardware components, compared to a single high-end computer.   
- The cluster computer has several components and layers, such as:
  - Computing nodes: the servers that process the user load and run the same task.  
  - Managing nodes: the servers that monitor the cluster hardware and software, and coordinate the load sharing and node replacement.  
  - Private network(s): the communication channel between the nodes, responsible for the heartbeat and command messages.  
  - Shared redundant storage: the data repository that is accessible to all computing nodes, allowing data consistency and node takeover.  
  - Public-access layer: the interface that virtualizes the access to the cluster and distributes the incoming requests to the active nodes.  
- The cluster computer can be classified into different types, depending on the purpose and configuration, such as:
  - High-performance computing (HPC) cluster: a cluster that aims to achieve high speed and efficiency in processing complex and intensive tasks, such as scientific simulations, data analysis, and machine learning.   
  - High-availability (HA) cluster: a cluster that aims to provide continuous and uninterrupted service, even in the event of node failures, by using redundancy and failover mechanisms.   
  - Load-balancing cluster: a cluster that aims to distribute the workload evenly among the nodes, to optimize the resource utilization and performance.   
  - Grid computing cluster: a cluster that consists of geographically distributed and heterogeneous nodes, that cooperate to solve a common problem, using a middleware layer.   
  - Cloud computing cluster: a cluster that provides on-demand and scalable computing resources and services over the internet, using a virtualization layer.   

: Computer cluster - Wikipedia
: Computer Clusters, Types, Uses and Applications | Baeldung on Computer Science
: An Overview of Cluster Computing - GeeksforGeeks
: Cluster Computing : Architecture & Its Types - WatElectronics.com
: Computer Cluster [What It Is & How It Works] | Liquid Web