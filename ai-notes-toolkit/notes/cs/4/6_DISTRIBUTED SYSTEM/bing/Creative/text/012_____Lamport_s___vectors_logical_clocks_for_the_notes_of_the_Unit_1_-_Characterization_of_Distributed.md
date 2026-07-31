### Lamport's logical clocks

- Lamport's logical clocks are a way of ordering events in a distributed system without relying on physical clocks.
- Lamport's logical clocks are based on the idea of a **happens-before** relation, denoted by `->`, which captures the causal order of events.
- If `a` and `b` are events on the same process, then `a -> b` if `a` occurs before `b` based on the local clock.
- If `a` is the event of sending a message by one process and `b` is the event of receiving that message by another process, then `a -> b`.
- The happens-before relation is transitive, meaning that if `a -> b` and `b -> c`, then `a -> c`.
- Lamport's logical clocks assign a numerical value, called a **timestamp**, to each event that reflects its position in the happens-before order.
- A timestamp is a software counter that is maintained by each process and incremented before each event.
- When a process sends a message, it attaches its current timestamp to the message.
- When a process receives a message, it updates its timestamp to be the maximum of its own timestamp and the timestamp of the message, and then increments it by one.
- Lamport's logical clocks ensure that if `a -> b`, then the timestamp of `a` is less than the timestamp of `b`.
- However, the converse is not true, meaning that if the timestamp of `a` is less than the timestamp of `b`, it does not imply that `a -> b`.
- Therefore, Lamport's logical clocks can only partially order events, and they cannot distinguish between concurrent events, i.e., events that are not causally related.
- Lamport's logical clocks are simple and easy to implement, but they have some limitations, such as:
  - They do not reflect the real time of events, only their logical order.
  - They do not provide a total order of events, only a partial order.
  - They do not capture the causal dependencies between events on different processes, only between events on the same process or between send and receive events.
  - They may assign different timestamps to events that are logically equivalent, such as two processes sending messages to each other at the same time.