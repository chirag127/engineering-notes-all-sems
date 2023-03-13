### Lamport's logical clocks

- Lamport's logical clocks are a way of ordering events in a distributed system without relying on physical clocks.
- Lamport's logical clocks are based on the concept of a **happens-before** relation, denoted by `->`, which captures the causal order of events.
- If `a` and `b` are events on the same process, then `a -> b` if `a` occurs before `b` based on the local clock.
- If `a` is the event of sending a message by one process and `b` is the event of receiving that message by another process, then `a -> b`.
- The happens-before relation is transitive, meaning that if `a -> b` and `b -> c`, then `a -> c`.
- Lamport's logical clocks assign a numerical value, called a **timestamp**, to each event that occurs in the system.
- The timestamp of an event is the value of the logical clock of the process that generated the event.
- A logical clock is a software counter that is incremented before each event on a process.
- When a process sends a message, it attaches its current timestamp to the message.
- When a process receives a message, it updates its logical clock to be the maximum of its own clock and the timestamp of the message, and then increments it by one.
- Lamport's logical clocks ensure that if `a -> b`, then the timestamp of `a` is less than the timestamp of `b`.
- However, the converse is not true, meaning that if the timestamp of `a` is less than the timestamp of `b`, it does not imply that `a -> b`.
- Therefore, Lamport's logical clocks can only partially order the events in the system, and cannot distinguish between concurrent events that have no causal relation.
- Lamport's logical clocks are simple and easy to implement, but they do not capture the full causal order of events in a distributed system.
- To overcome this limitation, vector clocks are used, which are an extension of Lamport's logical clocks.