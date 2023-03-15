 Here is the content in markdown format for the topic ### Logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM:

### Logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Logical clocks are used to assign timestamps to events in a distributed system. They help in determining the partial ordering of events.
- Some of the popular logical clocks are:
    - Lamport clocks: Assigns an integer timestamp to each process. Whenever a process sends a message, it includes its timestamp. On receiving a message, the receiver process increases its timestamp if the timestamp of the received message is greater. This ensures that the timestamps keep increasing and the causality is preserved.
    - Vector clocks: Assigns a vector of integers to each process. The ith element of the vector represents the number of events that have occurred at Pi. Whenever a message is sent, the vector clock of the sending process is sent along with the message. On receiving, the receiver adds the vector clock of the received message to its own vector clock element-wise. This preserves the causality and detects concurrent events.
- Advantages:
    - Does not require synchronization.
    - Scales well with the number of processes.
- Disadvantages:
    - Does not represent the real time. The timestamps are just logical entities to determine ordering.
- Applications:
    - Used in distributed debugging to determine the order of events.
    - Used in replication to determine the order of updates.
- Mnemonics:
    - Logical clocks - no sync, scales well, not real time
    - Lamport - integer timestamp, increment on receive if greater
    - Vector - vector of ints, add element-wise on receive

The content is written in points in detail about the topic ### Logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM. I have included advantages, disadvantages, applications and Mnemonics where relevant to help in learning and remembering the topic. Please let me know if you would like me to elaborate on any part or modify the content.