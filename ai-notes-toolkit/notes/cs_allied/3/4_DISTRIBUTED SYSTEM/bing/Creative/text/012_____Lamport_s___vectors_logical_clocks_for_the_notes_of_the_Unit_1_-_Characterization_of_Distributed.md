### Lamport's logical clocks

- Lamport's logical clocks are a way of ordering events in a distributed system based on their causal relationships, rather than their physical timestamps.
- Lamport's logical clocks are also known as **logical timestamps** or **logical counters**.
- Lamport's logical clocks are based on the idea of a **happens-before** relation, denoted by `->`, which captures the notion of causality between events.
- If `a` and `b` are events on the same process, then `a -> b` if `a` occurs before `b` based on the local clock.
- If `a` is the event of sending a message by one process and `b` is the event of receiving that message by another process, then `a -> b`.
- The happens-before relation is **transitive**, meaning that if `a -> b` and `b -> c`, then `a -> c`.
- The happens-before relation is **irreflexive**, meaning that no event happens before itself.
- The happens-before relation is **antisymmetric**, meaning that if `a -> b`, then `b` does not happen before `a`.
- Lamport's logical clocks assign a **logical clock value** to each event, denoted by `C(e)`, which is a non-negative integer that increases monotonically with each event.
- Lamport's logical clocks follow two rules:
  - Rule 1: Each process increments its logical clock value by one before each event it executes.
  - Rule 2: When a process sends a message, it includes its current logical clock value in the message. When a process receives a message, it sets its logical clock value to the maximum of its own value and the value received in the message, and then increments it by one.
- Lamport's logical clocks ensure that if `a -> b`, then `C(a) < C(b)`. However, the converse is not true, meaning that if `C(a) < C(b)`, it does not imply that `a -> b`.
- Lamport's logical clocks are useful for determining a **partial order** of events in a distributed system, but they cannot distinguish between **concurrent** events, which are events that are not causally related.