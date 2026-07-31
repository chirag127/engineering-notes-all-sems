### Lamport's & vectors logical clocks

- Lamport's logical clock is a procedure to determine the order of events occurring in a distributed system, where there is no global clock.
- Lamport's logical clock is based on the idea of a logical timestamp, which is a numerical value maintained by each process in the system.
- The logical timestamp reflects the causal order of events, such that if event A happens before event B, then the timestamp of A is less than the timestamp of B.
- The logical timestamp is updated according to the following rules:
  - When a process performs an internal event, it increments its logical clock by one.
  - When a process sends a message, it increments its logical clock by one and attaches the timestamp to the message.
  - When a process receives a message, it updates its logical clock to the maximum of its own clock and the timestamp in the message, and then increments it by one.
- Lamport's logical clock provides a total ordering of events consistent with causality, but it does not capture the concurrency of events. Two events that are concurrent (i.e., neither causally precedes nor follows the other) may have different timestamps depending on the order of message delivery.
- Vector clocks extend the capabilities of Lamport's logical clock to allow us to understand the ordering across multiple processes that cross communicate.
- Vector clocks are vectors of logical clocks, one clock per process in the system. Each process maintains a local copy of the global vector clock, and updates it according to the following rules:
  - When a process performs an internal event, it increments its own clock in the vector by one.
  - When a process sends a message, it increments its own clock in the vector by one and attaches the vector to the message.
  - When a process receives a message, it updates each entry in its vector to the maximum of its own entry and the corresponding entry in the message, and then increments its own clock by one.
- Vector clocks allow us to determine if any two arbitrarily selected events are causally dependent or concurrent. Two events are causally dependent if one of them causally precedes the other, and concurrent if neither causally precedes nor follows the other.
- The causal order of two events can be determined by comparing their vector clocks. If the vector clock of event A is less than the vector clock of event B in all entries, then A causally precedes B. If the vector clock of event A is greater than the vector clock of event B in all entries, then B causally precedes A. If neither of these conditions hold, then A and B are concurrent.
- Vector clocks provide a partial ordering of events consistent with causality and concurrency, but they are more complex and require more space than Lamport's logical clock. Each vector clock has N entries, where N is the number of processes in the system, and each entry is a logical clock that can grow arbitrarily large.