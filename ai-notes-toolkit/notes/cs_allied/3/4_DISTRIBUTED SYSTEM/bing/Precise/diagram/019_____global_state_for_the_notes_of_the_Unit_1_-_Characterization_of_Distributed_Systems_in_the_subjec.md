### Global State

- In a distributed system, the global state is the collection of the local states of all the processes and the state of the communication channels.
- The global state is used to determine the properties of the system, such as whether a computation has terminated or whether a message has been delivered.
- The global state is not directly observable, as the local states of the processes and the state of the communication channels are distributed across the system.
- To determine the global state, a snapshot algorithm can be used. This algorithm takes a consistent cut of the system, which is a snapshot of the local states of the processes and the state of the communication channels that is consistent with the causal order of events in the system.
- The global state can be used to detect global predicates, which are properties of the system that depend on the state of multiple processes. For example, a global predicate could be used to detect whether a distributed computation has reached a certain state or whether a message has been delivered to all processes.
- The global state can also be used to detect stable properties, which are properties of the system that, once they become true, remain true for the rest of the computation. For example, a stable property could be used to detect whether a distributed computation has terminated.