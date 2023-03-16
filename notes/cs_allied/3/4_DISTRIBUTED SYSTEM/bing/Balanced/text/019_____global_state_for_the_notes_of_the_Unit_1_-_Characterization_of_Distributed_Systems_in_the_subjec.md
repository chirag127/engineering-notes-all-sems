### Global State for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent processes that communicate through message passing.
- The global state of a distributed system is the union of the local states of the processes and the channels .
- A local state of a process is the values of its variables and registers at a given point in time.
- A channel state is the set of messages that have been sent but not yet received by the processes.
- A global state is consistent if it reflects a possible execution of the system, i.e., no causal violations occur .
- A causal violation is when a message is received before it is sent, or a process observes the effect of a message before it observes the message itself.
- A consistent global state can be used for various purposes, such as debugging, checkpointing, termination detection, garbage collection, etc .
- A consistent global state can be recorded by using distributed snapshot algorithms, which capture the local states of the processes and the channel states in a coordinated manner.
- A distributed snapshot algorithm must satisfy two properties:
  - Safety: The recorded global state is consistent.
  - Liveness: The algorithm eventually terminates and does not interfere with the normal execution of the system.