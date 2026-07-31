### Lamport's logical clocks

- Lamport's logical clocks are a way of ordering events in a distributed system without relying on physical clocks.
- Lamport's logical clocks are based on the concept of a **happens-before** relation, denoted by `->`, which captures the causal order of events.
- If `a` and `b` are events on the same process, then `a -> b` if `a` occurs before `b` based on the local clock.
- If `a` is the event of sending a message by one process and `b` is the event of receiving that message by another process, then `a -> b`.
- The happens-before relation is transitive, meaning that if `a -> b` and `b -> c`, then `a -> c`.
- Lamport's logical clocks are implemented by assigning a numerical value, called a **timestamp**, to each event that occurs in the system.
- Each process maintains a local counter that is incremented after each event that occurs on that process.
- The timestamp of an event is the value of the counter when the event occurs.
- When a process sends a message, it attaches its current counter value to the message.
- When a process receives a message, it updates its counter to be the maximum of its own counter and the timestamp of the message, and then increments it by one.
- Lamport's logical clocks ensure that if `a -> b`, then the timestamp of `a` is less than the timestamp of `b`.
- However, the converse is not true, meaning that if the timestamp of `a` is less than the timestamp of `b`, it does not imply that `a -> b`.
- Therefore, Lamport's logical clocks can only partially order the events in the system, and there may be some events that are **concurrent**, meaning that they are not causally related.
- Lamport's logical clocks are simple and easy to implement, but they do not capture the full causal order of events in the system.