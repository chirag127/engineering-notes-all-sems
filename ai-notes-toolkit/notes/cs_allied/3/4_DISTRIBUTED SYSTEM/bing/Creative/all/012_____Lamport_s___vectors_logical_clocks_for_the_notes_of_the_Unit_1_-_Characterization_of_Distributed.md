# Lamport's Logical Clocks

- Lamport's logical clocks are a way of ordering events in a distributed system without relying on physical clocks.
- Lamport's logical clocks are based on the concept of **happens-before** relation, denoted by `->`, which defines a partial order among events.
- If `a` and `b` are events on the same process, then `a -> b` if `a` occurs before `b` based on the local clock.
- If `a` is the event of sending a message by one process and `b` is the event of receiving that message by another process, then `a -> b`.
- If `a -> b` and `b -> c`, then `a -> c`.
- Two events `a` and `b` are **concurrent**, denoted by `a || b`, if neither `a -> b` nor `b -> a`.
- Lamport's logical clocks assign a numerical value, called a **timestamp**, to each event that occurs in the system, such that if `a -> b`, then the timestamp of `a` is less than the timestamp of `b`.
- A Lamport logical clock is a numerical software counter value maintained in each process. Conceptually, this logical clock can be thought of as a clock that only has meaning in relation to messages moving between processes.
- When a process receives a message, it re-synchronizes its logical clock with that sender by taking the maximum of its own clock value and the timestamp in the message, and then incrementing it by one.
- When a process sends a message, it increments its logical clock by one and attaches the updated timestamp to the message.
- Lamport's logical clocks ensure that the timestamps reflect the happens-before relation, but they do not guarantee that concurrent events have distinct timestamps.
- Lamport's logical clocks are widely used in distributed systems to provide a logical ordering of events, but they do not capture the causal dependencies among events.
- Lamport's logical clocks provide a basis for the more advanced vector clock algorithm, which can distinguish between concurrent events and preserve the causal order of events.