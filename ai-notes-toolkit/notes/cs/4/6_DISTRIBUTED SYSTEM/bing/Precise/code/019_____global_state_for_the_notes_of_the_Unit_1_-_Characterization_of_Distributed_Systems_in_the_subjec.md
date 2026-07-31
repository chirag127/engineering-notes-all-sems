### Global State

- In a distributed system, the global state is the collection of the local states of all the processes and the state of the communication channels.
- The global state is used to determine the properties of the system, such as whether the system is in a safe or unsafe state.
- The global state is not directly observable, as the local states of the processes and the state of the communication channels are distributed across the system.
- To determine the global state, a snapshot algorithm is used, which records the local states of the processes and the state of the communication channels in a consistent manner.
- The global state can be used to detect global properties, such as deadlocks or termination, and to reason about the behavior of the system.
- The global state is an important concept in the design and analysis of distributed algorithms.
