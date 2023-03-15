 Here is the content in markdown format:

### Techniques for Message Ordering for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

The following are the techniques for message ordering in distributed systems:

1. **Lamport Timestamps**: Each process maintains a counter which is incremented whenever a process sends a message. This counter value is attached to the message as a timestamp. When a process receives a message, it orders the messages based on the timestamp values. This ensures that if message M1 is sent before M2, then M1 is processed before M2. However, this technique does not work if the counters are not synchronized.

2. **Vector Clocks**: Each process maintains a vector of counters where each element corresponds to a process in the system. When a process sends a message, it increments its counter in the vector and attaches the vector to the message. On receiving a message, the vector is updated by taking the maximum value of each element from the sent and received vector. The messages are ordered based on the vector clocks. This handles counter synchronization problem but leads to high overhead.

3. **Logical Clocks**: The counters are replaced by logical timestamps which are partial orders on events. The timestamps are attached to messages and causal ordering is achieved. The overhead is lower than vector clocks but may result in unrelated messages getting the same timestamp.

4. **Sequential Numbers**: Each process maintains a sequence number which is incremented and attached to messages. When a process receives a message, it orders the messages based on the sequence numbers. This requires synchronized sequence numbers across processes.

The technique to be chosen depends on the system requirements and overhead constraints. Lamport timestamps and vector clocks provide stronger ordering guarantees but have higher overhead than logical clocks and sequential numbers.

Does this help? Let me know if you would like me to elaborate on any of the points or add more details.