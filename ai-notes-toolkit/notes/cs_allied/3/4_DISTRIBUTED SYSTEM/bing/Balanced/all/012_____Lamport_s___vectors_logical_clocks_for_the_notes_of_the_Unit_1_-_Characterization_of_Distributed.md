# Lamport's Logical Clocks

- Lamport's logical clocks are a way of ordering events in a distributed system without relying on physical clocks or synchronization.
- Lamport's logical clocks are based on the idea of a **happens-before** relation, denoted by `->`, which captures the causal order of events.
- If `a` and `b` are events on the same process, then `a -> b` if `a` occurs before `b` based on the local clock.
- If `a` is the event of sending a message by one process and `b` is the event of receiving that message by another process, then `a -> b`.
- If `a -> b` and `b -> c`, then `a -> c`.
- Two events `a` and `b` are **concurrent**, denoted by `a || b`, if neither `a -> b` nor `b -> a`.
- Lamport's logical clocks assign a numerical value, called a **timestamp**, to each event that is consistent with the happens-before relation.
- A timestamp is a positive integer that represents the logical time of an event.
- Each process maintains a local logical clock, which is a counter that is incremented before each event on that process.
- When a process sends a message, it attaches its current logical clock value to the message.
- When a process receives a message, it updates its logical clock to be the maximum of its own clock and the timestamp in the message, and then increments it by one.
- Lamport's logical clocks ensure that if `a -> b`, then the timestamp of `a` is less than the timestamp of `b`.
- However, the converse is not true: if the timestamp of `a` is less than the timestamp of `b`, it does not imply that `a -> b`.
- Therefore, Lamport's logical clocks can only partially order events, and cannot distinguish between concurrent events.