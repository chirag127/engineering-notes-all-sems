### Logical Clocks

Logical clocks are an essential concept in distributed systems, used to order events in the absence of a global clock. They were first introduced by Leslie Lamport in his 1978 paper "Time, Clocks, and the Ordering of Events in a Distributed System."

Here are some key points to remember about logical clocks:

1. A logical clock is a monotonically increasing software counter, maintained by each process in the system.
2. Each process increments its logical clock before executing an event.
3. When a process sends a message, it includes the current value of its logical clock in the message.
4. When a process receives a message, it sets its logical clock to the maximum of its current value and the timestamp in the received message, and then increments it by one.
5. The happened-before relation, denoted by ->, is a partial order on the set of events in a distributed system. It is defined as follows: if a and b are two events, then a -> b if and only if one of the following conditions holds:
    - a and b are events in the same process, and a occurred before b.
    - a is the sending of a message by one process, and b is the receipt of the same message by another process.
    - There exists an event c such that a -> c and c -> b.
6. Logical clocks provide a way to implement the happened-before relation by assigning a timestamp to each event, such that if a -> b, then the timestamp of a is less than the timestamp of b.
7. Logical clocks do not provide a total order on events, as two events may be concurrent, i.e., neither happened before the other. In this case, their timestamps may be equal or incomparable.
8. Vector clocks are an extension of logical clocks that provide a total order on events. They are an array of n logical clocks, one for each process in the system, and are updated in a similar way to logical clocks.
