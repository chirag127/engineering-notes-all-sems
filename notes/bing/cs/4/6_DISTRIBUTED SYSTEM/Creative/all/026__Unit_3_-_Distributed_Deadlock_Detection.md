## Unit 3 - Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set .
- Deadlock detection is a strategy to deal with deadlocks by examining the status of the process-resource interactions for the presence of a deadlock condition .
- Deadlock detection in distributed systems is challenging because there is no global knowledge of the system state and no central coordinator .
- There are three main approaches to deadlock detection in distributed systems:
  - Centralized approach: A designated node collects information about the resource allocation and requests from all other nodes and runs a deadlock detection algorithm periodically or on demand .
    - Advantages: Simple and efficient .
    - Disadvantages: Single point of failure, communication overhead, scalability issues .
  - Distributed approach: Each node maintains its own local information about the resource allocation and requests and exchanges messages with other nodes to detect cycles in the wait-for graph .
    - Advantages: No single point of failure, distributed workload, faster detection .
    - Disadvantages: Complex and costly message exchange, possibility of false or phantom deadlocks .
  - Hierarchical approach: The nodes are organized into a tree structure and each node collects information from its children and passes it to its parent until the root node runs a deadlock detection algorithm .
    - Advantages: Reduced communication overhead, balanced workload, improved scalability .
    - Disadvantages: Dependency on the root node, delay in detection, possibility of false or phantom deadlocks .
- To resolve a deadlock, one or more processes involved in the cycle have to be aborted or rolled back .
- The criteria for selecting a victim process include the priority, the execution time, the number of resources held, the future resource requests, and the rollback cost .
- A possible mnemonic to remember the three approaches to deadlock detection in distributed systems is **CDH** (Centralized, Distributed, Hierarchical).