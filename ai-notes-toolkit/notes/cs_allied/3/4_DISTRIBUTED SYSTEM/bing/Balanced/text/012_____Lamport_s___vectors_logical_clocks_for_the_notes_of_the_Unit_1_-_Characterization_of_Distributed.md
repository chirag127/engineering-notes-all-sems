### Lamport's logical clocks

- Lamport's logical clocks are a way of ordering events in a distributed system based on their causal relationships, rather than their physical timestamps.
- Lamport's logical clocks are also known as logical timestamps or scalar clocks.
- Lamport's logical clocks are based on the idea of a **happens-before** relation, denoted by `->`, which captures the notion of causality between events.
- If `a` and `b` are events on the same process, then `a -> b` if `a` occurs before `b` based on the local clock.
- If `a` is the event of sending a message by one process and `b` is the event of receiving that message by another process, then `a -> b`.
- If `a -> b` and `b -> c`, then `a -> c`. This is the transitivity property of the happens-before relation.
- Two events `a` and `b` are said to be **concurrent** if neither `a -> b` nor `b -> a`. This means that they are causally unrelated and can happen in any order.
- Lamport's logical clocks assign a numerical value, called a **logical clock**, to each event in a distributed system. This value is maintained by each process and incremented whenever an event occurs.
- The logical clock of an event is denoted by `C(a)`, where `C` is a function that maps events to integers.
- The logical clocks satisfy the following rules:
  - If `a` and `b` are events on the same process, and `a` occurs before `b`, then `C(a) < C(b)`.
  - If `a` is the event of sending a message by one process and `b` is the event of receiving that message by another process, then `C(a) < C(b)`.
  - A process increments its logical clock before sending a message, and includes the logical clock value in the message.
  - A process updates its logical clock when receiving a message, by taking the maximum of its own logical clock and the logical clock value in the message, and then increments it by one.
- Lamport's logical clocks ensure that if `a -> b`, then `C(a) < C(b)`. However, the converse is not true, i.e., if `C(a) < C(b)`, it does not imply that `a -> b`. This means that Lamport's logical clocks can only partially order events, and cannot distinguish between concurrent events.
- Lamport's logical clocks are simple and easy to implement, but they have some limitations. For example, they cannot capture the causal dependencies between events that happen on different processes, and they cannot measure the actual duration of events or the physical time difference between them.