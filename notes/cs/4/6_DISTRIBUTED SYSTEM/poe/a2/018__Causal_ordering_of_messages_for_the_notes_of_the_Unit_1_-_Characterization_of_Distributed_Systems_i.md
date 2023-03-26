 Here is the content in markdown format without any emojis or external links, written in points in a formal tone:

### Causal ordering of messages for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

1. In distributed systems, messages may be delivered out of order. Causal ordering ensures that messages are delivered in the same order as they were sent.
2. To achieve causal ordering, each message must contain information about which previous messages caused it to be sent. This is often done by associating a sequence number with each message.
3. If message B is sent after message A and is dependent on A, then B's sequence number must be greater than A's. When messages arrive at their destination, they can be reordered correctly based on the sequence numbers.
4. Causal ordering ensures that the state of the system will change in an order consistent with the order of the events that caused the state changes. This is important for maintaining a consistent system state and expected program behavior in distributed systems.
5. A system that implements causal ordering may have lower performance than one without ordering guarantees, due to the additional information that must be tracked and processed for each message. The performance impact must be weighed against the need for correctly ordered messages.

Does this sound okay? Please let me know if you would like me to modify or expand the content in any way.