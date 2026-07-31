 Here is the content in markdown format without any emojis or external links, in formal tone with points:

### Causal ordering of messages for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

1. In a distributed system, the messages may arrive out of order. Causal ordering ensures that messages are delivered in the same order as they were sent.
2. If event A causes event B, then all messages containing B must be delivered after all messages containing A. This is known as causal ordering.
3. Lamport's logical clocks can be used to establish a partial ordering of events. A vector of logical clocks is associated with each process. Each component is incremented whenever a message is sent. When a message is received, the vector is updated by taking the max of each component. If two vectors are compared and one is less than the other in all components, then the events are causally ordered.
4. Sequence numbers can also be used - each message is stamped with a sequence number by the sender. The receiver delivers messages in the incrementing order of sequence numbers. This ensures causal delivery of messages.
5. Causal ordering requires some additional information to be sent with each message, such as vector clocks or sequence numbers. This incurs some performance overhead but ensures correctness.

The above points cover the key aspects of causal ordering of messages which is important to correctly characterize the ordering of events and messages in a distributed system.