
### Logical Clocks for the Notes of the Unit 1 - Characterization of Distributed Systems in the Subject of DISTRIBUTED SYSTEM

1. Logical clocks are a way of assigning timestamps to events in a distributed system in order to maintain the causality of events.

2. Lamport clocks are one type of logical clock, which uses a single counter that is incremented each time an event occurs. The counter is then used to assign a timestamp to the event.

3. Vector clocks are another type of logical clock, which use a vector of counters to assign timestamps to events. Each node in the distributed system has its own counter, and each time an event occurs, all of the counters are incremented.

4. Logical clocks are used to maintain the causality of events in a distributed system, as well as to detect concurrent events. They can also be used to detect causality violations, which occur when events in a distributed system are not ordered correctly.

5. Logical clocks are also used in distributed databases, to ensure that transactions are correctly ordered, and to detect conflicts between transactions.