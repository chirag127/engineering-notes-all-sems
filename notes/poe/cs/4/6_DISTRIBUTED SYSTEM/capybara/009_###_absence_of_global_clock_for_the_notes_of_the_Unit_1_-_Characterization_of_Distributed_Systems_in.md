### Absence of Global Clock for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

In a distributed system, there is no shared clock that all processes can use to synchronize their activities. This absence of a global clock poses several challenges to the design and operation of distributed systems. Here are some key points to keep in mind about the absence of a global clock:

- **Clock Skew**: Each process in a distributed system has its own clock, but due to differences in clock speeds, network delays, and other factors, these clocks can become skewed over time. This means that different processes may have different ideas about what time it is, making it difficult to coordinate their activities.
- **Event Ordering**: In the absence of a global clock, it is difficult to determine the order of events that occur in different processes. For example, if two processes send messages to each other, it may not be clear which message arrived first.
- **Causality**: The absence of a global clock also makes it difficult to determine causal relationships between events. For example, if one process sends a message to another process, it may not be clear whether the message caused some subsequent event to occur.
- **Synchronization**: Without a global clock, processes must use other means to synchronize their activities. This can involve various mechanisms such as timeouts, message exchanges, or the use of logical clocks.

Here are some mnemonics or learning tricks that can help you remember these points:

- **Clock Skew**: Think of a clock that is melting or stretching, representing the fact that different clocks can become skewed over time.
- **Event Ordering**: Think of two race cars that cross the finish line at the same time, but it is not clear which one won. This represents the difficulty of determining the order of events in the absence of a global clock.
- **Causality**: Think of a chain of events where each event is linked to the one before it. Without a global clock, it can be difficult to determine these links in the chain.
- **Synchronization**: Think of a group of people trying to clap their hands together. Without a conductor to keep the beat, they must rely on other means to stay in sync.

Overall, understanding the absence of a global clock is crucial for designing and operating distributed systems. By keeping these key points in mind and using mnemonics or learning tricks to help you remember them, you can master this important topic and excel in your studies of distributed systems.