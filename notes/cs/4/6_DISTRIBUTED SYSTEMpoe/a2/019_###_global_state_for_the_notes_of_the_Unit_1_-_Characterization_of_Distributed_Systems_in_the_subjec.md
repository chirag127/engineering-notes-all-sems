 Here is the content in markdown format:

### Global State for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

The global state of a distributed system refers to the state of the entire system at a particular instant of time. It incorporates the state of each individual process and the state of the communication channels between the processes.

It is difficult to capture the global state of a distributed system due to the following reasons:

- Lack of centralized control: There is no global clock and no single entity to take a snapshot of the entire system state. Each process progresses at its own pace.
- Asynchrony: The speed of processes and message delays are not bounded. This makes it impossible to determine a unique global state and the order of events.
- Concurrency: Many events can occur concurrently in the system due to parallelism making the global state complex.

Some ways to capture a partial global state are:

- Log records: Each process maintains logs of messages sent and received. By collecting and merging these logs, we can deduce a partial ordering of events.
- Distributed snapshots: A snapshot algorithm can be used to capture local states of processes at approximately the same instant of time. However, it is difficult to get a truly concurrent snapshot of a distributed system.
- Blackboards: A shared storage (blackboard) is used where processes post their local states. By reading the blackboard, we can get a view of the current global state. However, there are challenges with consistency and concurrency control.

In general, capturing a precise global state is difficult and often not feasible in distributed systems. We have to often make do with approximations and partial views of the global state.