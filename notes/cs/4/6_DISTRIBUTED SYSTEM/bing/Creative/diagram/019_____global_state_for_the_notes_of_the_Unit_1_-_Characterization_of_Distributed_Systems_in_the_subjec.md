### Global State for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent processes that communicate through message passing.
- The global state of a distributed system is the union of the local states of the individual processes and the channels .
- A local state of a process is the values of its variables, registers, program counter, etc. at a given point in time.
- A channel state is the set of messages that have been sent but not yet received by the processes.
- The global state of a distributed system may change due to the occurrence of events, such as local computation, message sending, message receiving, etc.
- A global state is consistent if it reflects a possible execution of the system, i.e., it does not contain any causal anomaly .
- A causal anomaly is a situation where a message is received before it is sent, or a process observes the effect of a message before it observes the message itself.
- A consistent global state can be computed along a consistent cut, which is a partition of the system's execution history into past and future events .
- A consistent cut satisfies the property that if an event is in the future of the cut, then all events that causally precede it are also in the future of the cut .
- A global snapshot is a technique for recording a consistent global state of a distributed system without stopping or synchronizing the processes.
- A global snapshot algorithm ensures that each process records its local state and the state of its incoming channels in such a way that the resulting global state is consistent.
- A global snapshot can be used for various purposes, such as checkpointing, debugging, monitoring, termination detection, etc.  .