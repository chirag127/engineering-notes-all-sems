### Global State for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent processes that communicate through message passing.
- The global state of a distributed system is the union of the local states of the individual processes and the channels.
- A local state of a process is the values of its variables, registers, program counter, etc. at a given point in time.
- A channel state is the set of messages that have been sent but not yet received by the processes.
- The global state of a distributed system may change due to the occurrence of events, such as local computation, message sending, or message receiving.
- A global state is consistent if it reflects a possible execution of the system, i.e., it does not contain any causal anomaly.
- A causal anomaly is a violation of the causal order of events, such as a message being received before it is sent, or a process observing the effect of an event before the cause.
- A consistent global state can be computed along a consistent cut, which is a partition of the set of events into past and future such that no message is received in the past from the future.
- A consistent cut can be determined by using distributed snapshot algorithms, which are protocols that allow the processes to record their local states and the channel states in a coordinated way.
- Distributed snapshot algorithms can be classified into two categories: uncoordinated and coordinated.
- Uncoordinated algorithms do not require any synchronization among the processes, but they may record inconsistent global states. An example of an uncoordinated algorithm is the Chandy-Lamport algorithm.
- Coordinated algorithms ensure that the recorded global state is consistent, but they may incur more overhead and delay. An example of a coordinated algorithm is the Lai-Yang algorithm.
- The global state of a distributed system can be used for various purposes, such as debugging, checkpointing, recovery, termination detection, deadlock detection, etc.