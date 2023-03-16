# Unit 3 - Distributed Deadlock Detection

- A **deadlock** is a condition where a set of processes request resources that are held by other processes in the set, and none of the processes can proceed until some of the resources are released.
- A **distributed deadlock** is a deadlock that involves processes and resources located on different machines in a distributed system.
- **Deadlock detection** is a strategy to deal with deadlocks by examining the status of the process-resource interactions for the presence of cyclic wait.
- **Deadlock resolution** is a strategy to deal with deadlocks by aborting or preempting some of the deadlocked processes or resources to break the cycle.
- **Deadlock detection** in distributed systems is challenging because of the following reasons:
  - The global state of the system is not known or easily accessible.
  - The system is dynamic and asynchronous, and the processes and resources may change their states frequently.
  - The communication and computation costs of detecting and resolving deadlocks may be high.
- There are three main approaches to **deadlock detection** in distributed systems:
  - **Centralized approach**: A designated node, called the **deadlock detector**, collects the local wait-for graphs (WFGs) from all the nodes and constructs a global WFG to detect cycles. This approach has the advantages of simplicity and low communication cost, but it has the disadvantages of single point of failure, bottleneck, and scalability issues.
  - **Distributed approach**: Each node maintains its own local WFG and periodically sends it to its neighbors. A cycle detection algorithm, such as **edge chasing** or **probe-based**, is used to trace the dependencies among the nodes and detect cycles. This approach has the advantages of fault tolerance, load balancing, and scalability, but it has the disadvantages of high communication cost, false deadlock detection, and synchronization issues.
  - **Hierarchical approach**: The nodes are organized into a hierarchy of clusters, and each cluster has a **coordinator** that collects the local WFGs from its members and constructs a cluster WFG. The coordinators communicate with each other to construct a global WFG and detect cycles. This approach has the advantages of reducing the communication cost and the size of the WFGs, but it has the disadvantages of increased complexity and dependency on the cluster structure.