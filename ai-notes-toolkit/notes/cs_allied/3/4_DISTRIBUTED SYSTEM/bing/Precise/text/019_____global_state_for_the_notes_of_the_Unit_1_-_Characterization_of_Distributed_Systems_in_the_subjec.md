### Global State

- In a distributed system, the global state is the collection of the local states of all the processes and the state of the communication channels.
- The global state is used to determine the properties of the system, such as whether the system is in a safe state or a deadlock state.
- The global state is not directly observable, as the processes and communication channels are distributed across multiple machines.
- To determine the global state, a snapshot algorithm is used, which records the local states of the processes and the state of the communication channels in a consistent manner.
- The snapshot algorithm must ensure that the recorded global state is consistent, meaning that it could have occurred during the execution of the system.
- The Chandy-Lamport algorithm is a commonly used snapshot algorithm for determining the global state of a distributed system.