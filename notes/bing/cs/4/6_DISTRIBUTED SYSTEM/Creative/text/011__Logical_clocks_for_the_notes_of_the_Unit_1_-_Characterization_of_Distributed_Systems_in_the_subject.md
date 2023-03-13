### Logical clocks

- A logical clock is a mechanism for capturing chronological and causal relationships in a distributed system.
- A distributed system may have no physically synchronous global clock, so a logical clock allows global ordering on events from different processes in such systems.
- A logical clock assigns a unique timestamp to each event in the system, determined by a logical time function that takes into account the events that have occurred in the past.
- A logical clock satisfies the following property: if event A causally precedes event B, then the timestamp of A is less than the timestamp of B.
- A logical clock does not need to synchronize with the real time, it only needs to agree on the order in which events occur.
- One example of a logical clock is the Lamport timestamp, which is based on the following rules:
  - Each process maintains a counter that is incremented before each event in that process.
  - When a process sends a message, it attaches its current counter value to the message.
  - When a process receives a message, it updates its counter to be the maximum of its own counter and the received counter value, and then increments it by one.
- Another example of a logical clock is the vector clock, which is based on the following rules:
  - Each process maintains a vector of counters, one for each process in the system.
  - The counter at position i in the vector represents the logical time of process i as seen by the current process.
  - When a process executes an event, it increments its own counter in the vector.
  - When a process sends a message, it attaches its current vector to the message.
  - When a process receives a message, it updates each element in its vector to be the maximum of its own element and the received element, and then increments its own counter by one.
- Logical clocks enable distributed systems to achieve partial ordering, causal ordering, and consistent snapshots of the global state.