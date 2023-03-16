# Global State for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent processes that communicate through message passing.
- The state of a process is the values of its variables and registers at a given point in time.
- The state of a channel is the sequence of messages that have been sent but not yet received on that channel.
- The global state of a distributed system is the union of the states of the individual processes and channels.
- A global state is consistent if it reflects a possible execution of the system, i.e., no causal violations occur.
- A causal violation is when a message is received before it is sent, according to the global state.
- A cut is a partition of the set of events in the system into two subsets: past and future.
- A cut is consistent if it respects the causal order of events, i.e., no message crosses the cut from future to past.
- A snapshot is a mechanism to record a consistent global state of a distributed system.
- A snapshot algorithm is a distributed protocol that allows each process to record its local state and the state of its incoming channels, such that the resulting global state is consistent.
- A snapshot algorithm is correct if it satisfies the following properties:
  - Termination: every process eventually records its state and terminates the algorithm.
  - Consistency: the recorded global state is consistent.
  - Local: no process needs to record the state of another process or an outgoing channel.
- A snapshot algorithm can be used for various purposes, such as:
  - Checkpointing: saving the global state of the system for recovery purposes.
  - Monitoring: observing the global state of the system for debugging or performance analysis.
  - Global predicate evaluation: checking whether a global property holds in the system.