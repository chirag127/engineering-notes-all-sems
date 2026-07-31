 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Lamport's & Vectors Logical Clocks

**Lamport's Logical Clocks:**

- Each process maintains a counter which is incremented whenever a message is sent.
- When a message is sent, the counter value is attached to the message.
- When a message is received, the receiver accepts the message only if the timestamp is greater than the receiver's own counter. If so, the receiver's counter is set to the received timestamp + 1.
- The single integer timestamp acts as a logical clock and can be used to determine the partial ordering of events in a distributed system.

**Vector Clocks:**

- A vector of n logical clocks is maintained, where n is the number of processes in the system.
- The i^th component of the vector is the logical clock maintained by the i^th process.
- When a message is sent, the sender's vector clock is piggybacked onto the message.
- When a message is received, the receiver's vector clock is updated component-wise taking the maximum value from the sender's vector clock for each component.
- The vector clock values can determine the causal ordering between events and detect concurrent events in a distributed system.

The above content summarizes the key points about Lamport's logical clocks and vector clocks which are mechanisms to assign timestamps and determine partial/causal ordering of events in a distributed system. The points are written in a formal tone with no emojis or external links as per the given instructions.