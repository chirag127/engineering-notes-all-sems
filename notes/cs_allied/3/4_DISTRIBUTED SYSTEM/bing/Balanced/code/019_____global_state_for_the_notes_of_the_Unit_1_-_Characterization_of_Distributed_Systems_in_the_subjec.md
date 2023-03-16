### Global State for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent processes that communicate through message passing.
- The global state of a distributed system is the union of the local states of the processes and the channels .
- A local state of a process is the values of its variables and registers at a given point in time.
- A channel state is the set of messages that have been sent but not yet received by the processes.
- A global state is consistent if it reflects a possible execution of the system, i.e., no causal violations occur .
- A causal violation is when a message is received before it is sent, or a process observes the effect of a message before it observes the message itself.
- A consistent global state can be used for debugging, checkpointing, termination detection, and other applications in distributed systems  .
- A consistent global state can be recorded by using distributed snapshot algorithms, which are protocols that allow processes to coordinate and capture their local states and channel states without blocking or synchronizing.
- A distributed snapshot algorithm must satisfy two properties: correctness and termination.
- Correctness means that the recorded global state is consistent and reflects a possible execution of the system.
- Termination means that the algorithm eventually completes and all processes resume their normal execution.