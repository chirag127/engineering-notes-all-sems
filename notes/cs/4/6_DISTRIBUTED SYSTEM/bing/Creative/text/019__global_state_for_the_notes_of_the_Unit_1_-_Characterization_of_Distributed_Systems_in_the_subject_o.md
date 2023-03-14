### Global State for the Notes of the Unit 1 - Characterization of Distributed Systems in the Subject of DISTRIBUTED SYSTEM

- A **global state** of a distributed system is the union of the states of the individual processes and the communication channels.
- A process that wishes to construct a global state must infer the remote components of that state through message exchanges.
- A global state is useful for solving many problems in distributed systems, such as checkpointing, garbage collection, deadlock detection, termination detection, and stable property detection.
- A **stable property** is one that persists: once a stable property becomes true, it remains true thereafter.
- A **consistent global state** is one that could have occurred during the execution of the system.
- A **cut** is a partition of the set of events in a distributed system into two subsets: past and future.
- A **consistent cut** is a cut that does not contain any causal anomaly, such as a message being received before it was sent.
- A **global snapshot** is a global state computed along a consistent cut.
- A global snapshot can be used to detect stable properties of a distributed system.
- A **global checkpoint** is a transaction that must view a globally consistent system state for correct operation.
- A global checkpoint can be used to restart a distributed system after a failure.
- There are various algorithms for determining global states and snapshots of distributed systems, such as the Chandy-Lamport algorithm, the Lai-Yang algorithm, and the Mattern algorithm.