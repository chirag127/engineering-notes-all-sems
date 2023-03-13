### Global state for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A **global state** of a distributed system is a collection of the **local states** of the processes and the channels  .
- A **local state** of a process is the values of its variables and its program counter at a given point in time .
- A **local state** of a channel is the sequence of messages that have been sent but not yet received on that channel .
- A global state is **consistent** if it reflects a possible execution of the system, i.e., it does not violate the causal order of events  .
- A **cut** is a subset of events in the system's execution such that for any process, either all or none of its events are in the cut .
- A cut is **consistent** if it contains no message and its corresponding receive event .
- A **snapshot** is a technique to record a consistent global state of a distributed system  .
- A snapshot algorithm must satisfy the following properties  :
  - **Termination**: Every process eventually records its local state.
  - **Consistency**: The recorded global state is consistent.
  - **Accuracy**: The recorded global state reflects the system state at some point during the execution of the algorithm.
- A snapshot algorithm can be used for various purposes, such as  :
  - **Checkpointing**: Saving the system state periodically to recover from failures.
  - **Monitoring**: Observing the system behavior and detecting anomalies or deadlocks.
  - **Garbage collection**: Reclaiming the unused resources or messages in the system.
  - **Global predicate evaluation**: Checking whether a certain condition holds in the system.

- A possible mnemonic to remember the properties of a snapshot algorithm is **TCA** (Termination, Consistency, Accuracy).
- A possible mnemonic to remember the purposes of a snapshot algorithm is **MMGG** (Monitoring, Checkpointing, Garbage collection, Global predicate evaluation).