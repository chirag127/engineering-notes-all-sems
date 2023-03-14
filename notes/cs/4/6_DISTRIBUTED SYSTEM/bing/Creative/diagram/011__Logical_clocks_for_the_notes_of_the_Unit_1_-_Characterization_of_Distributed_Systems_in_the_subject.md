A logical clock is a mechanism for capturing chronological and causal relationships in a distributed system. Distributed systems may have no physically synchronous global clock, so a logical clock allows global ordering on events from different processes in such systems .

One way to implement a logical clock is to use Lamport timestamps, which are based on the happen-before relation. The happen-before relation is a partial order on the events in a distributed system, such that if event A happens before event B in the same process, or if event A is the sending of a message and event B is the receiving of that message, then A happens before B. The happen-before relation is transitive, meaning that if A happens before B and B happens before C, then A happens before C .

To assign Lamport timestamps to events, each process maintains a counter that is incremented after each event. When a process sends a message, it attaches its current counter value to the message. When a process receives a message, it updates its counter to be the maximum of its own counter and the received counter value, and then increments it by one. This way, the counter value reflects the causal order of events, and timestamps can be compared to determine the logical order of events .

The following diagram illustrates the basic architecture of a logical clock using Lamport timestamps:

```
    P1                  P2                  P3
    |                   |                   |
    |---a (1)---------> |                   |
    |                   |---b (2)---------> |
    |                   |                   |---c (3)--->
    |                   |<--d (4)---------- |
    |<--e (5)---------- |                   |
    |---f (6)---------> |                   |
    |                   |                   |
```

In this diagram, P1, P2, and P3 are three processes in a distributed system. The events are labeled with lowercase letters and the corresponding Lamport timestamps are shown in parentheses. The arrows indicate the sending and receiving of messages. For example, event a is the sending of a message from P1 to P2 with timestamp 1, and event b is the receiving of that message by P2 with timestamp 2. The logical order of events can be determined by comparing the timestamps. For instance, event c happens before event d, because 3 < 4. Event e is concurrent with event c, because they are not causally related and their timestamps are incomparable. Event f happens after event e, because 6 > 5 .