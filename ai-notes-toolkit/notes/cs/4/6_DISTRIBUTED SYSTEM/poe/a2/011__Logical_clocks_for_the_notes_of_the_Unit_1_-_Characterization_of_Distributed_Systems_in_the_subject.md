 Here is the content in markdown format without any emojis or external links:

### Logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

1. Lamport logical clocks:
- Each process maintains a logical clock as a counter.
- Whenever a process sends a message, it includes its logical clock value with the message.
- Whenever a process receives a message, it increases its logical clock value to be greater than the sender's logical clock value in the received message.
- There is no synchronization between the logical clocks of different processes. The only requirement is that the logical clock value should be monotonically increasing.
- These logical clocks are used to detect causality between events and to find a consistent global state.

2. Vector clocks:
- Each process maintains a vector clock which is a vector of logical clock values, one component for each process in the system.
- Whenever a process sends a message to another process, it includes its vector clock value with the message. The receiver process increases only the sender's clock value in its vector clock.
- The vector clocks satisfy the properties of Lamport logical clocks and can capture causality between multiple events involving multiple processes.
- However, the vector clock values may grow indefinitely.

3. Pair-wise synchronization:
- The vector clock size can be reduced by synchronizing the logical clocks of only those processes that communicate with each other. This approach is known as pair-wise synchronization.
- The algorithm runs in rounds. In each round, processes are paired and the logical clock values of the paired processes are synchronized. Different pairs are synchronized in different rounds.
- This reduces the size of the vector clocks but introduces more message overhead as synchronization messages have to be exchanged between the paired processes in every round.

The content is written in a formal tone with points and explanations of the topic as requested. Please let me know if you would like me to modify or add any other details to the content.