### Global State

- The global state of a distributed system is the **union** of the states of the individual processes and the channels .
- A process that wishes to construct a global state must infer the remote components of that state through message exchanges.
- A global state is **consistent** if it reflects a possible execution of the system, i.e., no causal violations occur .
- A global state is **correct** if it is computed along a consistent cut, i.e., a set of local states that are mutually consistent.
- A global state is **useful** for applications such as debugging, checkpointing, termination detection, garbage collection, etc .
- A global state can be recorded by using **distributed snapshot algorithms**, which are protocols that allow processes to cooperate in capturing a consistent global state without blocking or synchronizing.