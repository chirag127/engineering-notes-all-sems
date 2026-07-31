# Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set.
- A distributed deadlock is a deadlock that involves processes and resources located on different machines in a distributed system.
- Distributed deadlock detection is the process of identifying and resolving deadlocks in a distributed system.
- Distributed deadlock detection involves two basic issues:
  - Detection of existing deadlocks
  - Resolution of detected deadlocks
- There are three main approaches to distributed deadlock detection:
  - Global wait-for graph (WFG) approach
  - Local wait-for graph (LWFG) approach
  - Path-pushing (edge-chasing) approach

## Global wait-for graph (WFG) approach

- A wait-for graph is a directed graph that represents the waiting relationships among processes and resources.
- A node in the graph can be either a process or a resource, and an edge from node A to node B means that A is waiting for B.
- A cycle in the graph indicates a deadlock.
- In the global WFG approach, a centralized or distributed algorithm is used to construct a global WFG from the local WFGs of each site.
- The global WFG is then examined for cycles to detect deadlocks.
- The advantages of this approach are:
  - It is simple and easy to implement
  - It can detect all deadlocks in the system
- The disadvantages of this approach are:
  - It requires a lot of communication and computation overhead
  - It may introduce false deadlocks due to stale information
  - It may not be scalable or fault-tolerant

## Local wait-for graph (LWFG) approach

- In the local WFG approach, each site maintains its own local WFG and periodically sends it to a designated deadlock detector.
- The deadlock detector merges the received local WFGs into a global WFG and checks for cycles to detect deadlocks.
- The advantages of this approach are:
  - It reduces the communication and computation overhead compared to the global WFG approach
  - It can detect all deadlocks in the system
- The disadvantages of this approach are:
  - It still requires some communication and computation overhead
  - It may introduce false deadlocks due to stale information
  - It may not be scalable or fault-tolerant

## Path-pushing (edge-chasing) approach

- In the path-pushing approach, each site maintains a local WFG and sends a probe message along the edges of the graph to detect cycles.
- A probe message contains the identifier of the initiator site and the path of the message so far.
- When a site receives a probe message, it checks if the message has reached the initiator site or if it has visited the site before.
- If either condition is true, a cycle is detected and a deadlock is reported.
- Otherwise, the site appends its identifier to the path and forwards the message along the outgoing edges of the graph.
- The advantages of this approach are:
  - It does not require a global WFG or a deadlock detector
  - It does not introduce false deadlocks due to stale information
  - It is scalable and fault-tolerant
- The disadvantages of this approach are:
  - It may generate a lot of probe messages and cause network congestion
  - It may not detect all deadlocks in the system
  - It may have a long detection delay