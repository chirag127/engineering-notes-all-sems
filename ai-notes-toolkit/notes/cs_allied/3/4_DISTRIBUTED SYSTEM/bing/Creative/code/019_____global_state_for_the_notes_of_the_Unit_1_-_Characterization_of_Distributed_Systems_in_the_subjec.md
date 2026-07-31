### Global State for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent processes that communicate through message passing.
- The global state of a distributed system is the union of the local states of the processes and the channels .
- A local state of a process is the values of its variables, registers, program counter, etc. at a given point in time.
- A channel state is the set of messages that have been sent but not yet received by the processes.
- A global state is consistent if it reflects a possible execution of the system, i.e., no causal violations occur .
- A causal violation is when a message is received before it is sent, or a process observes the effect of a message before it observes the message itself.
- A consistent global state can be used for debugging, checkpointing, termination detection, garbage collection, etc. in distributed systems  .
- A consistent global state can be recorded by using distributed snapshot algorithms, which are protocols that allow processes to coordinate and capture their local states and channel states without blocking or synchronizing .
- A distributed snapshot algorithm must satisfy two properties: completeness and accuracy.
  - Completeness means that every process records its local state and every message in transit is recorded by either the sender or the receiver.
  - Accuracy means that the recorded global state is consistent, i.e., no causal violations occur.
- There are different types of distributed snapshot algorithms, such as Chandy-Lamport, Lai-Yang, Mattern, etc. that differ in their assumptions, communication patterns, and complexity .