 Here is the content in markdown format without any emojis or external links and in formal tone:

### Lamport's & vectors logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

1. Lamport's logical clocks:
- Lamport's logical clocks are used to assign timestamps to events in a distributed system and to determine the happened-before relationship between events.
- Each process maintains a logical clock as a counter.
- Whenever a process performs an event, it increments its logical clock and assigns the new value as the timestamp to the event.
- While sending a message, the timestamp of the sender process is attached to the message.
- When a message is received, the receiver process updates its logical clock to the greater of its clock value and the timestamp of the received message.

2. Vector clocks:
- Vector clocks are a generalization of Lamport's logical clocks and used to assign timestamps to events in a distributed system with 'n' processes.
- A vector clock is an array of 'n' logical clocks, one for each process in the system.
- The ith entry represents the local clock value at process i.
- While sending a message, a process attaches its vector clock to the message.
- Upon receiving a message, a process updates the appropriate entry of its vector clock to the greater of the existing value and the value in the received message's vector clock.
- The vector clock values allow determining the happened-before relationship between events in a distributed system.

The content summarizes the key points about Lamport's logical clocks and vector clocks which are used to assign timestamps and determine the happened-before relationship between events in a distributed system. The points are written in a formal tone with no emojis or external links as per the given instructions. Please let me know if you would like me to modify or expand the content.