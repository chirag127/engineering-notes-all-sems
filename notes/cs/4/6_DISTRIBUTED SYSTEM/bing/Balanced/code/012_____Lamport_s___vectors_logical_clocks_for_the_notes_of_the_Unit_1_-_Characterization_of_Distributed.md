### Lamport's logical clocks

- Lamport's logical clocks are a way of ordering events in a distributed system without relying on physical clocks.
- They are based on the idea of a "happens-before" relation, denoted by `->`, which means that one event causally affects another.
- For example, if a process sends a message to another process, then the send event happens before the receive event.
- Lamport's logical clocks assign a numerical value, called a timestamp, to each event in a process.
- The timestamp reflects the order of events within a process and across processes that communicate with each other.
- The rules for assigning timestamps are:

  - Each process maintains a counter, initialized to zero, that is incremented before each event in the process.
  - The timestamp of an event is the value of the counter when the event occurs.
  - When a process sends a message, it attaches its current timestamp to the message.
  - When a process receives a message, it updates its counter to be the maximum of its own counter and the timestamp in the message, plus one.

- The timestamps can be used to compare the order of events in a distributed system.
- If `a` and `b` are events in the same process, then `a -> b` if and only if the timestamp of `a` is less than the timestamp of `b`.
- If `a` is the send event of a message and `b` is the receive event of the same message, then `a -> b`.
- If `a -> b` and `b -> c`, then `a -> c`.
- If `a` and `b` are events in different processes that do not communicate with each other, then they are concurrent, denoted by `a || b`, and their timestamps cannot be compared.