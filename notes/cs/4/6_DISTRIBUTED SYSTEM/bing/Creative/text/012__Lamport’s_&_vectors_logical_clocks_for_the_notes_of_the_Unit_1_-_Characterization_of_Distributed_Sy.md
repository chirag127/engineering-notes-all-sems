### Lamport’s & vectors logical clocks

- Lamport’s logical clock is a simple algorithm to determine the order of events in a distributed system, where different processes may not have synchronized clocks.
- Lamport’s logical clock is based on the concept of **happened-before** relation, which is a partial ordering of events that captures the causal dependencies between them.
- Lamport’s logical clock assigns a numerical value, called a **timestamp**, to each event that occurs in a process. The timestamp reflects the logical order of events, not the physical time.
- Lamport’s logical clock follows two rules:
  - If event a happens before event b in the same process, then the timestamp of a is less than the timestamp of b. (C(a) < C(b))
  - If event a is the sending of a message by one process and event b is the receipt of that message by another process, then the timestamp of a is less than the timestamp of b. (C(a) < C(b))
- Lamport’s logical clock ensures that if event a happens before event b, then the timestamp of a is less than the timestamp of b. However, the converse is not necessarily true: if the timestamp of a is less than the timestamp of b, it does not imply that a happens before b. This is because events that are concurrent (i.e., not causally related) may have arbitrary timestamps.
- Lamport’s logical clock is useful for ordering events and detecting causality violations, but it does not provide a total ordering of events or a way to measure the elapsed time between events.
- Vector clock is an extension of Lamport’s logical clock that provides a total ordering of events and a way to measure the elapsed time between events.
- Vector clock assigns a vector of timestamps to each event, where each element of the vector corresponds to the logical clock of a process in the system.
- Vector clock follows two rules:
  - Initially, all elements of the vector are zero.
  - Each time a process experiences an internal event, it increments its own logical clock in the vector by one.
  - Each time a process sends a message, it piggybacks its current vector on the message.
  - Each time a process receives a message, it increments its own logical clock in the vector by one and updates each element in its vector by taking the maximum of its own value and the value received in the message.
- Vector clock allows to compare any two events and determine their causal relationship. If the vector of event a is less than the vector of event b in all elements, then a happens before b. If the vector of event a is greater than the vector of event b in all elements, then b happens before a. If neither is true, then a and b are concurrent.
- Vector clock also allows to measure the elapsed time between any two events by taking the difference of their vectors. The difference of two vectors is a vector that has the absolute value of the difference of each element. The elapsed time between two events is the maximum element in the difference vector.