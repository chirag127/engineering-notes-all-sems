### Global State

- A global state of a distributed system is a collection of the local states of the processes and the channels involved in the system   .
- A local state of a process is the values of its variables and its program counter at a given point in time.
- A local state of a channel is the sequence of messages that have been sent but not yet received along that channel.
- A global state can be represented by a cut, which is a set of events, one per process, such that no event in the cut is causally dependent on an event outside the cut.
- A cut is consistent if it contains no message that is received but not sent. A consistent cut represents a possible global state that could have occurred during the execution of the system.
- A global state is correct if it is computed along a consistent cut.
- Determining the global state of a distributed system is useful for debugging, monitoring, checkpointing, rollback-recovery, and termination detection.
- There are different algorithms for recording the global state of a distributed system, such as the Chandy-Lamport algorithm, the Lai-Yang algorithm, and the Mattern algorithm. These algorithms are based on sending and receiving special messages called markers to capture the local states and the channel states.
- The challenges of determining the global state of a distributed system are the lack of a global clock, the asynchrony of the communication, and the possibility of failures .