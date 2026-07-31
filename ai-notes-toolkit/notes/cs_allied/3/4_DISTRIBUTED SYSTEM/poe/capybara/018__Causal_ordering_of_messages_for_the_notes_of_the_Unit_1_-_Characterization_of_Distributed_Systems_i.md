### Causal ordering of messages for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

In a distributed system, messages are exchanged between different nodes. However, the order of messages can become ambiguous when multiple nodes send messages at the same time. This is where causal ordering of messages comes into play.

Causal ordering of messages ensures that the order of messages is preserved in a distributed system. Here are some important points to keep in mind regarding causal ordering of messages:

1. Causal ordering is based on the concept of happened-before relation. This relation is used to determine the causal order of events.

2. In a distributed system, the happened-before relation is determined by a combination of local and remote events. Local events are the events that happen on a specific node, while remote events are the events that happen on other nodes.

3. The happened-before relation is transitive, meaning that if A happened before B and B happened before C, then A happened before C.

4. Causal ordering of messages is achieved by assigning a unique timestamp to each message. This timestamp is used to order the messages based on their happened-before relation.

5. In order to ensure that the timestamps are unique, a logical clock is used. A logical clock is a clock that is not synchronized with the physical clock, but it ensures that the timestamps are unique.

6. Causal ordering of messages is important in a distributed system because it ensures that the order of events is preserved. This is important for maintaining consistency and correctness in the system.

Overall, causal ordering of messages is an important concept in distributed systems. It ensures that the order of events is preserved, which is crucial for maintaining consistency and correctness.