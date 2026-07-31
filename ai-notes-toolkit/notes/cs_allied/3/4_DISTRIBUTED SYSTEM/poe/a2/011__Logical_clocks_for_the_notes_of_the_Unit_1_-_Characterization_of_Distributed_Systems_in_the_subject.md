 Here is the content in markdown format without any emojis or external links:

### Logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Logical clocks are used to assign timestamps to events in a distributed system.
- They help in partial ordering of events and detection of causal relationships between events.
- Lamport timestamps: Each process maintains a counter which is incremented locally. When a message is sent, the current counter value is attached to it. On receiving a message, the maximum of its timestamp and the local counter is used.
- Vector clocks: An array of counters is maintained, one per process. On sending a message, the local counter is incremented and attached to the message. On receiving a message, the corresponding entry is updated to the maximum of the two values.
- Happened-before relation: A partial ordering of events based on sending/receiving of messages which helps in reconstructing a consistent global timeline of events.

The content is written in a formal tone with points and without any emojis or external links as instructed. Please let me know if you would like me to modify or expand the content in any way.