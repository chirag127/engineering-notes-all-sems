### Causal order for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Causal order is a concept that describes the logical relationship between events in a distributed system, where events can be internal, send, or receive events.
- Causal order is based on the "happened before" relation, which is a partial order that captures the potential causal influence of one event on another.
- Causal order is important for maintaining consistency and correctness in distributed systems, especially for applications that rely on multicast communication, state machine replication, or distributed mutual exclusion.
- Causal order is not automatically guaranteed in distributed systems, due to factors such as network delays, congestion, or failures.
- Causal order can be enforced by using logical clocks, which are functions that assign numerical timestamps to events, such that the timestamps respect the "happened before" relation.
- Logical clocks can be implemented using different algorithms, such as Lamport clocks, vector clocks, or matrix clocks, depending on the level of precision and overhead required.
- Causal order can also be achieved by using protocols that deliver messages to processes only if the messages that causally precede them have been delivered, or by using process groups that provide ordered multicast primitives, such as the ISIS system.

Some possible mnemonics and learning tricks for causal order are:

- Remember the three conditions for the "happened before" relation: same process, send-receive, and transitivity. You can use the acronym SST or the phrase "Same, Send, Transit".
- Remember the difference between logical clocks and physical clocks: logical clocks are based on events, not on real time. You can use the phrase "Logical clocks are eventful, physical clocks are temporal".
- Remember the trade-off between different logical clock algorithms: Lamport clocks are simple and efficient, but imprecise; vector clocks are precise, but complex and costly; matrix clocks are the most precise, but also the most complex and costly. You can use the phrase "Lamport is simple, vector is precise, matrix is costly".