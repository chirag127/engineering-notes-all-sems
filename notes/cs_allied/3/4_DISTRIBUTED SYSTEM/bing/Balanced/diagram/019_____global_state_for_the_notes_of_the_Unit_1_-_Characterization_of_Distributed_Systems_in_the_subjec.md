### Global State

- The global state of a distributed system is the **union** of the states of the individual processes and the channels .
- A process that wishes to construct a global state must infer the remote components of that state through message exchanges.
- A global state is **consistent** if it reflects a possible state of the system that could have occurred during the execution .
- A global state is **correct** if it is computed along a **consistent cut**, which is a set of local states that are causally related.
- A global state can be used for various purposes, such as debugging, checkpointing, recovery, termination detection, etc .
- A global state can be recorded by using **snapshot algorithms**, which are protocols that allow each process to record its local state and the state of its incoming channels without blocking the system execution.