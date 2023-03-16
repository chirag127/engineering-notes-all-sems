# Global State

- The global state of a distributed system is a collection of the local states of the processes and the channels  .
- A local state of a process is the values of its variables and its program counter at a given point in time .
- A local state of a channel is the sequence of messages that have been sent but not yet received on that channel .
- A global state can be represented by a global state vector, which is a vector of local state vectors, one for each process and channel .
- A global state vector can be written as G = (P1, P2, ..., Pn, C1, C2, ..., Cm), where Pi is the local state vector of process i and Cj is the local state vector of channel j .
- A global state is consistent if it could have occurred during an execution of the distributed system .
- A consistent global state can be computed along a consistent cut, which is a partition of the set of events in the distributed system such that no message is received before it is sent .
- A consistent cut can be determined by using a distributed snapshot algorithm, which is a protocol that allows each process to record its local state and the state of its incoming channels without blocking the computation .
- A distributed snapshot algorithm can be based on markers, which are special messages that are sent and received by the processes to indicate the start and end of the snapshot .
- A distributed snapshot algorithm can be used for various purposes, such as detecting global predicates, checkpointing, debugging, rollback-recovery, and termination detection .