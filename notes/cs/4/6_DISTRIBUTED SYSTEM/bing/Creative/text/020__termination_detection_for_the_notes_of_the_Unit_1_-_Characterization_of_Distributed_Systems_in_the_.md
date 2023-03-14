### Termination Detection

- Termination detection is the problem of determining when a distributed computation has finished.
- A distributed computation consists of a set of processes that communicate by exchanging messages, and that may start and stop at different times.
- A computation is said to be terminated when all processes have completed their work and no messages are in transit.
- Termination detection is useful for coordinating distributed activities, such as garbage collection, checkpointing, load balancing, etc.
- Termination detection can be classified into two categories: centralized and distributed.
- Centralized termination detection relies on a designated process, called the coordinator, that collects information from other processes and decides whether the computation has terminated.
- Distributed termination detection does not use a coordinator, but rather relies on local information and message passing among processes to reach a global agreement on termination.
- Centralized termination detection algorithms are simpler and more efficient, but they introduce a single point of failure and a bottleneck for communication.
- Distributed termination detection algorithms are more robust and scalable, but they are more complex and require more messages.
- Some examples of centralized termination detection algorithms are:
  - The basic algorithm: The coordinator initiates the computation and sends a token to each process. Each process sends back the token when it finishes its work. The coordinator declares termination when it receives all tokens back.
  - The credit distribution algorithm: The coordinator assigns a credit to each process and each message. Each process sends back a credit when it finishes its work or receives a message. The coordinator declares termination when it receives all credits back.
  - The echo algorithm: The coordinator initiates the computation and sends a probe message to each process. Each process forwards the probe to its neighbors and sends back an echo when it receives echoes from all its neighbors. The coordinator declares termination when it receives echoes from all processes.
- Some examples of distributed termination detection algorithms are:
  - The diffusing computation algorithm: Each process maintains a counter of the number of messages it has sent and received. Each process initiates a diffusing computation when it starts its work and terminates it when it finishes its work and its counter is zero. A diffusing computation propagates a termination message along a spanning tree of processes. A process declares termination when it receives a termination message from all its children in the tree.
  - The Dijkstra-Scholten algorithm: Each process maintains a set of processes that it depends on, called its parents. A process becomes a parent of another process when it sends a message to it. A process sends an acknowledgment to its parent when it receives a message from it. A process removes a parent from its set when it receives an acknowledgment from it. A process declares termination when it has no parents and no work to do.
  - The Huang's algorithm: Each process maintains a vector of counters, one for each process in the system. Each counter records the number of messages sent and received by the corresponding process. Each process periodically sends its vector to a designated process, called the monitor. The monitor declares termination when the sum of each column in the vectors is zero.