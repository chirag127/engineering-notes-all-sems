### System Model for the Notes of Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

In this unit, we will be discussing the system model for distributed deadlock detection. Below are the key points to keep in mind:

- A distributed system consists of multiple nodes, where each node can access shared resources.
- Deadlocks can occur in a distributed system when multiple nodes request and hold resources that are needed by other nodes. This can result in a circular wait, where each node is waiting for a resource held by another node.
- The system model for distributed deadlock detection includes the following components:
  - Resource allocation graph (RAG): This graph represents the resources and processes in the system, where each node is a process and each edge represents a resource request.
  - Wait-for graph (WFG): This graph represents the waiting relationships between processes, where each node is a process and each edge represents a process waiting for another process to release a resource.
  - Coordinator: This is a centralized component that is responsible for detecting deadlocks in the system. The coordinator periodically collects the RAG and WFG from each node and analyzes them to detect deadlocks.
  - Message passing: Nodes communicate with each other using message passing. The coordinator sends messages to nodes to request their RAGs and WFGs, and nodes send messages to the coordinator to report changes in their RAGs and WFGs.
- To detect deadlocks in a distributed system, the coordinator must perform the following steps:
  - Collect the RAG and WFG from each node.
  - Construct a global RAG and WFG by merging the local RAGs and WFGs.
  - Analyze the global RAG and WFG to detect cycles, which indicate the presence of deadlocks.
  - If a deadlock is detected, the coordinator can take corrective action, such as releasing resources or killing processes, to resolve the deadlock.
- There are several algorithms for distributed deadlock detection, including the Chandy-Misra-Haas (CMH) algorithm and the Distributed Deadlock Detection Algorithm (DDDA). These algorithms differ in their approach to constructing and analyzing the global RAG and WFG.
- Distributed deadlock detection can be expensive in terms of message passing and computation overhead. To reduce this overhead, we can use techniques such as partial deadlock detection, where only a subset of the system is analyzed for deadlocks, and distributed deadlock avoidance, where the system is designed to avoid deadlocks altogether.

Keep these points in mind as you study the system model for distributed deadlock detection. Understanding this model is essential for designing and managing distributed systems that are resilient to deadlocks.