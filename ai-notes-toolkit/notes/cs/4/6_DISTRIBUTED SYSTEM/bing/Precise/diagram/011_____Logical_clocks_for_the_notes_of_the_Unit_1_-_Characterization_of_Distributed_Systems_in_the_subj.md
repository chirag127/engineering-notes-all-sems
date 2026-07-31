### Logical Clocks

Logical clocks are an essential concept in the characterization of distributed systems. They are used to provide a partial ordering of events in a distributed system and to detect causality violations.

Here are some key points to remember about logical clocks:

1. A logical clock is a monotonically increasing software counter that is maintained by each process in a distributed system.
2. Each process increments its logical clock counter before executing an event.
3. When a process sends a message, it includes the current value of its logical clock in the message.
4. When a process receives a message, it updates its logical clock to be the maximum of its current value and the value received in the message, and then increments the clock by one.
5. Logical clocks allow us to determine whether one event happened before another event in a distributed system, but they do not provide a total ordering of events.
6. Logical clocks can be used to detect causality violations, which occur when the order of events in a distributed system does not match the cause-and-effect relationships between those events.

These are some of the key points to remember about logical clocks in the context of distributed systems. They provide a useful tool for reasoning about the behavior of distributed systems and for detecting potential problems.