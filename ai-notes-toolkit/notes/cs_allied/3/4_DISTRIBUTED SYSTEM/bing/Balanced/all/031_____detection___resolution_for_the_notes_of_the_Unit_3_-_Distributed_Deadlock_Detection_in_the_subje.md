# Detection and Resolution of Distributed Deadlocks

- A distributed deadlock is a situation where a set of processes in a distributed system are waiting for each other to release resources or messages, and none of them can proceed.
- Detection and resolution of distributed deadlocks involve two steps: first, identifying the existence of deadlocks in the system, and second, breaking the cycles of dependency among the deadlocked processes.
- Detection of distributed deadlocks requires the following properties:
  - Progress: the method should be able to detect all the deadlocks in the system.
  - Safety: the method should not detect false or phantom deadlocks, which are cycles that do not involve any real dependency.
- There are three main approaches to detect distributed deadlocks, based on the representation and maintenance of the wait-for graph (WFG), which is a directed graph that shows the dependency relationships among the processes and resources in the system:
  - Centralized approach: a single designated node collects the information about the WFG from all the other nodes, and periodically searches the WFG for cycles. This approach is simple and efficient, but it has a single point of failure and a high communication overhead.
  - Distributed approach: each node maintains a local WFG that reflects its own dependency relationships, and exchanges messages with other nodes to detect global cycles. This approach is fault-tolerant and scalable, but it has a high complexity and a high message overhead.
  - Hierarchical approach: the nodes are organized into a hierarchy of clusters, and each cluster has a coordinator that maintains a partial WFG for its cluster. The coordinators communicate with each other to detect global cycles. This approach is a compromise between the centralized and distributed approaches, but it has a high coordination overhead and a variable detection time.
- Resolution of distributed deadlocks involves breaking the existing wait-for dependencies in the WFG, by aborting or preempting some of the deadlocked processes and releasing their resources or messages to the blocked processes. The resolution of distributed deadlocks requires the following properties:
  - Effectiveness: the method should be able to resolve all the deadlocks in the system.
  - Efficiency: the method should minimize the number of processes aborted or preempted, and the amount of resources or messages wasted.
  - Fairness: the method should not favor or penalize any process or node unfairly.
- There are two main strategies to resolve distributed deadlocks, based on the timing and the scope of the resolution:
  - Eager strategy: the resolution is performed as soon as a deadlock is detected, and it involves all the processes in the cycle. This strategy is proactive and simple, but it may abort or preempt more processes than necessary, and it may cause cascading aborts or preemptions.
  - Lazy strategy: the resolution is delayed until a deadlock affects the system performance, and it involves only a subset of processes in the cycle. This strategy is reactive and selective, but it may increase the deadlock detection time and complexity, and it may cause starvation or livelock.