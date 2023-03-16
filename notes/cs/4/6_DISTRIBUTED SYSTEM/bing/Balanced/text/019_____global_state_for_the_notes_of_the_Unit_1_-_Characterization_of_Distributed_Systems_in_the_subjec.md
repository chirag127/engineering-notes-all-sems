### Global State for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent processes that communicate through message passing.
- The local state of a process is the values of its variables and the contents of its memory at a given point in time.
- The global state of a distributed system is the union of the local states of all the processes and the states of the communication channels.
- A global state is consistent if it reflects a possible execution of the system, i.e., no causal dependencies are violated.
- A global state is useful for detecting global properties of the system, such as deadlock, termination, or invariant violation.
- A global state can be recorded by taking a distributed snapshot, which is a collection of local snapshots taken by each process at some point during the execution.
- A distributed snapshot algorithm must ensure that the recorded global state is consistent and that the normal execution of the system is not disrupted.
- There are different distributed snapshot algorithms for different types of communication channels, such as FIFO, causal, or reliable.