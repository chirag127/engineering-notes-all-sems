### Logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

In distributed systems, it is essential to keep track of events and time. Logical clocks are used to capture the order of events in a distributed system.

Here are some important points about logical clocks:

- Logical clocks are used to capture the causal relationship between events in a distributed system.
- Logical clocks do not provide a global notion of time, but they do provide a partial order of events.
- There are two types of logical clocks: Lamport clocks and vector clocks.
- Lamport clocks assign a unique timestamp to each event in a distributed system. The timestamp is a pair (t, i), where t is a logical time and i is the identifier of the process that generated the event.
- Vector clocks are similar to Lamport clocks, but they use a vector of timestamps instead of a single timestamp. Each process maintains a vector clock that contains a timestamp for each process in the system.
- Vector clocks are more accurate than Lamport clocks because they can capture the causal relationship between events involving multiple processes.
- Logical clocks are useful for detecting concurrent events and for implementing distributed algorithms such as distributed snapshots and consensus protocols.

In summary, logical clocks are a fundamental concept in distributed systems that are used to capture the causal relationship between events. Lamport clocks and vector clocks are two types of logical clocks that are commonly used in distributed systems.