### Logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

A logical clock is a mechanism for capturing chronological and causal relationships in a distributed system. Distributed systems may have no physically synchronous global clock, so a logical clock allows global ordering on events from different processes in such systems.

There are different types of logical clocks, such as Lamport's logical clock, vector clock, matrix clock, etc. Each type of logical clock has its own rules for assigning timestamps to events and comparing the order of events.

The following diagram illustrates the basic idea of a logical clock using Lamport's logical clock as an example. Lamport's logical clock assigns a monotonically increasing integer to each event in a process, and updates the clock value based on the messages sent and received between processes. The diagram shows three processes P1, P2, and P3, and the events that occur in each process. The events are labeled with the logical clock value of the process at the time of the event. The arrows represent the messages sent and received between processes. The diagram also shows the partial order of events based on the logical clock values, using the notation e1 < e2 to mean that event e1 happened before event e2.

```
P1: 1---2---3---4---5---6
    |   |   |   |   |   |
    |   |   |   |   |   |
    |   |   |   |   |   |
P2: 1---2---3---4---5---6
    |   |   |   |   |   |
    |   |   |   |   |   |
    |   |   |   |   |   |
P3: 1---2---3---4---5---6

Events: a1, a2, a3, a4, a5, a6, b1, b2, b3, b4, b5, b6, c1, c2, c3, c4, c5, c6
Messages: a2 -> b2, b3 -> a4, a5 -> c5, c6 -> b6

Partial order: a1 < a2 < b2 < b3 < a4 < a5 < c5 < c6 < b6
               b1 < b2 < b3 < b4 < b5 < b6
               c1 < c2 < c3 < c4 < c5 < c6
```