### System model for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- A system model is a representation of the essential features and properties of a system that can be used to analyze and design the system.
- A system model for distributed deadlock detection is a system model that captures the characteristics and assumptions of the distributed system that are relevant for detecting deadlocks.
- A deadlock is a situation where a set of processes are blocked waiting for resources that are held by other processes in the set.
- A distributed system is a system that consists of multiple nodes (processes or machines) that communicate and cooperate with each other to achieve a common goal.
- A distributed deadlock detection algorithm is an algorithm that can identify and resolve deadlocks in a distributed system without requiring a central coordinator or a global state.

#### Basic system model for distributed deadlock detection

- The basic system model for distributed deadlock detection is based on the following assumptions  :

  - The system has only **reusable resources**, which can be used by one process at a time and can be released and reused by other processes.
  - Processes are allowed only **exclusive access** to resources, which means that a process can request a resource only if it does not hold any other resource.
  - There is only **one copy** of each resource in the system, which means that a resource cannot be replicated or shared among multiple nodes.
  - Processes communicate with each other using **message passing**, which means that they can send and receive messages to exchange information or request resources.
  - Processes and resources are **static**, which means that they do not join or leave the system during the execution.
  - Processes and resources are **fail-stop**, which means that they can fail by crashing but not by behaving incorrectly or maliciously.
  - Processes and resources have **unique identifiers**, which can be used to distinguish them from each other and to order them in a consistent way.

#### Distributed deadlock models

- Based on the basic system model, there are two main models for representing and detecting distributed deadlocks  :

  - The **wait-for graph (WFG)** model, which is a directed graph that shows the dependency relationships among processes and resources in the system. A node in the WFG represents a process or a resource, and an edge from node A to node B represents that A is waiting for B. A cycle in the WFG indicates a deadlock.
  - The **global resource graph (GRG)** model, which is a directed graph that shows the allocation and request relationships among processes and resources in the system. A node in the GRG represents a process, and an edge from node A to node B represents that A holds or requests a resource that is held or requested by B. A cycle in the GRG indicates a deadlock.

#### Example of WFG and GRG

- Consider the following scenario of a distributed system with four processes (P1, P2, P3, P4) and four resources (R1, R2, R3, R4):

  - P1 holds R1 and requests R2
  - P2 holds R2 and requests R3
  - P3 holds R3 and requests R4
  - P4 holds R4 and requests R1

- The WFG and GRG for this scenario are shown below:

```
WFG:                GRG:

  P1  R1  P2  R2     P1  R1  P2  R2
   \  /    \  /       \ /    \ /
    \/      \/         X      X
    /\      /\         X      X
   /  \    /  \       / \    / \
  P4  R4  P3  R3     P4  R4  P3  R3
```

- Both graphs have a cycle, which indicates a deadlock in the system.