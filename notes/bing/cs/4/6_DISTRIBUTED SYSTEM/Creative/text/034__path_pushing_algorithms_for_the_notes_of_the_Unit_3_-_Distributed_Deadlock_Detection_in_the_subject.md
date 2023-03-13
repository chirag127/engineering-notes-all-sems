### Path Pushing Algorithms

- Path pushing algorithms are a class of distributed deadlock detection algorithms that use the concept of **wait-for graphs** to detect cycles of waiting processes.
- A wait-for graph is a directed graph that represents the dependencies among processes in a distributed system. Each node is a process and each edge is a wait-for relation, meaning that the source process is waiting for the destination process to release some resource.
- A cycle in a wait-for graph indicates a deadlock situation, where a set of processes are mutually waiting for each other and none of them can proceed.
- Path pushing algorithms work by propagating the information about the wait-for relations along the edges of the graph, until a cycle is detected or the graph becomes stable.
- There are two main types of path pushing algorithms: **edge chasing** and **diffusing computation**.

#### Edge Chasing

- Edge chasing is a path pushing algorithm that uses **probe messages** to track the wait-for relations among processes.
- Each process maintains a **dependency list**, which is a set of processes that it is waiting for or that are waiting for it.
- When a process P requests a resource from another process Q, it sends a probe message to Q, containing its own identifier and the dependency list of P.
- When Q receives the probe message, it does the following steps:
  - If Q is not waiting for any other process, it grants the resource to P and sends an **acknowledgment message** to P, indicating that the request is satisfied.
  - If Q is waiting for some other process R, it adds P to its dependency list and forwards the probe message to R, after appending its own identifier and the dependency list of Q to the message.
  - If Q detects a cycle in the probe message, meaning that Q or some process in its dependency list is already in the message, it sends a **nack message** to P, indicating that a deadlock has occurred.
- When P receives an acknowledgment message from Q, it removes Q from its dependency list and proceeds with the resource.
- When P receives a nack message from Q, it initiates a **resolution phase**, where it sends a **release message** to all the processes in its dependency list, asking them to release the resources they are holding and abort their requests.
- Edge chasing has the advantage of being simple and efficient, but it has the disadvantage of generating a large number of probe messages, especially in systems with high resource contention or long wait-for chains.

#### Diffusing Computation

- Diffusing computation is a path pushing algorithm that uses **initiator processes** and **cohort processes** to detect deadlocks.
- An initiator process is a process that initiates a diffusing computation, which is a distributed algorithm that involves a subset of processes in the system, called the cohort.
- A cohort process is a process that participates in a diffusing computation, either by being an initiator or by being contacted by an initiator or another cohort process.
- When a process P requests a resource from another process Q, it does the following steps:
  - If Q is not waiting for any other process, it grants the resource to P and the request is satisfied.
  - If Q is waiting for some other process R, it rejects the request from P and P becomes an initiator of a new diffusing computation, with Q as the first cohort process.
  - P sends a **query message** to Q, asking Q to report its wait-for status and to forward the query message to all the processes that Q is waiting for, if any.
  - Q sends a **reply message** to P, indicating whether it is involved in a cycle or not, and forwards the query message to all the processes that Q is waiting for, if any, making them cohort processes as well.
  - Each cohort process repeats the same steps, sending reply messages to their initiators and forwarding query messages to their wait-for processes, until all the processes in the cohort have been contacted or a cycle has been detected.
  - If P receives a reply message indicating a cycle, it initiates a resolution phase, where it sends a **rollback message** to all the cohort processes, asking them to release the resources they are holding and abort their requests.
  - If P receives reply messages from all the cohort processes indicating no cycle, it terminates the diffusing computation and retries the request to Q.
- Diffusing computation has the advantage of generating fewer messages than edge chasing, but it has the disadvantage of being more complex and requiring more state information at each process.