# Detection and Resolution of Distributed Deadlocks

- A distributed deadlock is a situation where a set of processes in a distributed system are waiting for each other to release resources or messages, and none of them can proceed.
- Distributed deadlock detection is the problem of finding and resolving such deadlocks in a distributed system.
- Distributed deadlock resolution is the process of breaking the deadlock by aborting or rolling back some of the deadlocked processes, and releasing their resources or messages to other processes.
- There are two main approaches to distributed deadlock detection and resolution: centralized and distributed.

## Centralized Approach

- In the centralized approach, there is a designated coordinator process that is responsible for maintaining and analyzing the global wait-for graph (WFG) of the system.
- The WFG is a directed graph that represents the dependencies among processes and resources in the system. A node in the WFG is either a process or a resource, and an edge from node A to node B means that A is waiting for B.
- A cycle in the WFG indicates a deadlock. The coordinator periodically collects the local WFG information from each process, and merges them into a global WFG. Then, it searches the global WFG for cycles, and initiates the resolution of any detected deadlocks.
- The advantages of the centralized approach are simplicity and efficiency. The disadvantages are the single point of failure and the communication overhead of the coordinator.

## Distributed Approach

- In the distributed approach, there is no coordinator process, and each process participates in the deadlock detection and resolution.
- There are three main techniques for distributed deadlock detection: edge chasing, path pushing, and diffusing computation.
- Edge chasing is a technique where each process sends a probe message along the edges of the WFG, and waits for an acknowledgment. If a process receives a probe message that it has sent before, it means that there is a cycle in the WFG, and a deadlock has occurred.
- Path pushing is a technique where each process maintains a list of processes that are dependent on it, and sends this list along with any request or reply message. If a process receives a message that contains its own identifier in the list, it means that there is a cycle in the WFG, and a deadlock has occurred.
- Diffusing computation is a technique where each process initiates a distributed computation when it requests a resource, and terminates it when it releases the resource. The computation involves sending and receiving messages among the processes that are involved in the resource allocation. If a process detects that its computation has terminated without receiving the resource, it means that there is a deadlock in the system.
- The advantages of the distributed approach are fault tolerance and scalability. The disadvantages are the complexity and the message overhead of the techniques.