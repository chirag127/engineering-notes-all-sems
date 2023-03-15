### Logical Clocks for the Notes of Unit 1 - Characterization of Distributed Systems in the Subject of DISTRIBUTED SYSTEM

In a distributed system, it is difficult to determine the ordering of events, especially when events occur simultaneously or across different machines. Logical clocks are used to maintain an ordering of events in a distributed system.

Here are some key points to keep in mind when studying logical clocks:

1. Logical clocks are used to order events in a distributed system.
2. The clock value is incremented whenever an event occurs.
3. Logical clocks can be either scalar clocks or vector clocks.
4. Scalar clocks are based on a single counter, while vector clocks use a vector of counters.
5. Vector clocks are more powerful than scalar clocks because they can capture causality relationships between events.
6. Logical clocks do not necessarily provide accurate time stamps, but they do provide a consistent ordering of events.

Some mnemonics and learning tricks for logical clocks are:

- "Clocks tick when events occur"
- "Scalar clocks have a single counter, vector clocks have a vector"
- "Vector clocks capture causality relationships between events"

It is important to understand the concept of logical clocks because they are used in many distributed systems, such as databases, messaging systems, and network protocols. By maintaining a consistent ordering of events, logical clocks can help ensure the correctness and reliability of a distributed system.