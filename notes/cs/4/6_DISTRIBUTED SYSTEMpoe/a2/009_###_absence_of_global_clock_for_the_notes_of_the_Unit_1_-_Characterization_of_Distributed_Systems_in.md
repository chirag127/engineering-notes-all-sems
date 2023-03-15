 Here is the content in markdown format for the topic ### absence of global clock for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM:

### Absence of global clock

- In distributed systems, there is no single global clock. Each machine has its own local clock which can be slightly different from others.
- This makes it difficult to synchronize events and determine the ordering of events.
- Timestamps are attached to events but they are local to each machine. There is no way to compare timestamps across machines directly.
- Solutions like Network Time Protocol (NTP) are used to synchronize clocks but absolute synchronization is not achievable. Clock values can only be approximately in sync.
- This property makes distributed systems more challenging to program and debug as ordering of events can be non-deterministic. Care must be taken to explicitly specify ordering requirements and handle clock inconsistencies.

[Diagram showing multiple local clocks with different times to illustrate absence of global clock]

Advantages:
- There is no single point of failure (the global clock). The system continues to function as long as majority of local clocks are operational.
- It is more scalable as there is no additional overhead on a global clock due to addition of more machines.

Disadvantages:
- It is harder to program and debug distributed systems due to non-determinism induced by unsynchronized local clocks. Extra effort is required to reason about ordering of events.
- Approximate synchronization using solutions like NTP is not precise and can still lead to subtle bugs.

Examples:
- When a file is modified, the timestamp is recorded locally. It is difficult to determine the exact global order of modifications done by different users.
- In leader election, if local clocks are not properly synchronized, it can lead to multiple leaders being elected.