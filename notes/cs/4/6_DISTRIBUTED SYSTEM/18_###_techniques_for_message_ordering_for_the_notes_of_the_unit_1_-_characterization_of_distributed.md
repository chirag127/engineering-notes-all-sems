### Techniques for Message Ordering for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM
Message ordering techniques in distributed systems:
1. Total Order Broadcast: A global ordering of messages is established and delivered to all nodes.
2. Causal Order Broadcast: A partial ordering of messages is established based on the causal relationship between them.
3. Vector Clocks: Each node maintains a vector of logical timestamps to determine the order of events.
4. Lamport Timestamps: A unique timestamp is assigned to each message based on the logical clock at the sender node.
5. Physical Clocks: Real-time clocks are used to determine the order of events.

These techniques ensure that messages are delivered in the correct order, which is important for maintaining consistency and avoiding conflicts in distributed systems.
