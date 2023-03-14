### Lamport’s & Vectors Logical Clocks

Distributed systems consist of multiple processes running on different machines that communicate with each other to accomplish a task. As these processes operate independently, it becomes difficult to determine the order of events occurring across these processes. This is where logical clocks come into play.

Lamport’s logical clock and vector clock are two widely used logical clock algorithms that help to order events in a distributed system.

#### Lamport’s Logical Clock

Lamport's logical clock is a simple algorithm that assigns a timestamp to each event in a distributed system. The timestamp represents the order of occurrence of events in the system. The following are the key features of Lamport's logical clock:

- Each process maintains a logical clock counter, which is incremented whenever an event occurs.
- Each event carries a timestamp, which is the value of the logical clock counter at the time of the event.
- When a process sends a message, it attaches its own timestamp to the message.
- When a process receives a message, it updates its own logical clock counter to the maximum of its current value and the timestamp in the received message. It then assigns a new timestamp to the event that just occurred.

The Lamport's logical clock algorithm ensures that events are ordered correctly as long as the clock values are monotonically increasing. However, it does not guarantee the accuracy of the clock value as it can be skewed due to clock drift.

#### Vector Clock

Vector clock is an extension of Lamport's logical clock, which addresses the issue of clock drift. It is a more sophisticated algorithm that uses a vector of logical clocks instead of a single logical clock. The following are the key features of vector clock:

- Each process maintains a vector of logical clocks, one clock for each process in the system.
- Each time an event occurs, the process increments its own logical clock in the vector.
- When a process sends a message, it attaches its own vector clock to the message.
- When a process receives a message, it updates its own vector clock to the maximum of its current clock value and the vector clock in the received message.

Vector clock algorithm guarantees the correct ordering of events and eliminates the issue of clock drift. However, it requires more memory as compared to Lamport's logical clock algorithm.

### Lamport's & Vectors Logical Clocks - Learning Tricks

To remember the key features of Lamport's logical clock algorithm, you can use the mnemonic "Lamport's Lousy Clock":

- L - logical clock counter incremented for each event
- L - each event carries a timestamp
- C - when a process sends a message, it attaches its own timestamp
- L - when a process receives a message, it updates its own logical clock counter
- C - assigns a new timestamp to the event that just occurred

To remember the key features of vector clock algorithm, you can use the mnemonic "Vectors are Sophisticated":

- V - each process maintains a vector of logical clocks
- A - each time an event occurs, the process increments its own logical clock in the vector
- R - when a process sends a message, it attaches its own vector clock
- E - when a process receives a message, it updates its own vector clock
- S - vector clock algorithm guarantees the correct ordering of events and eliminates the issue of clock drift