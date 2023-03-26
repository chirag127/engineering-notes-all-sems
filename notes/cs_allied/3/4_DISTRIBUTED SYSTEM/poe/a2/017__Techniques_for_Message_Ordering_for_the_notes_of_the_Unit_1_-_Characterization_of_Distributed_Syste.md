 Here is the content in markdown format without any emojis or external links, being formal and not showing any feeling:

### Techniques for Message Ordering

1. Lamport Timestamps - Each message is stamped with a timestamp by the sender. The receiver delivers messages in increasing timestamp order. This ensures that causally dependent messages are delivered in order.
2. Vector Clocks - Each process maintains a vector of logical clocks, one component for each other process. When a message is sent, the sending process's vector clock is stamped on the message. When a message is received, the receiver updates its vector clock by taking a component-wise maximum with the received timestamp. The receiver delivers messages in increasing vector clock order. Vector clocks allow detection of causal relationships that may not be detectable using Lamport timestamps.
3. Happened-before Relation - The happened-before relation is a partial ordering over events in a distributed system. If event A happened before event B, then B's state incorporates the effect of A, so A must be ordered before B. The happened-before relation can be captured using vector clocks or other techniques to ensure correct total ordering of events.
4. Processor Ordering - On a single processor system, events can be totally ordered simply by ordering them in the sequence they are processed by the CPU. This is not possible on a distributed system with multiple processors operating concurrently, so other techniques are needed toorder events and send messages.

The above points cover the major techniques for ordering messages and events in a distributed system to ensure correctness. Proper ordering of causally dependent events and messages is critical to the proper operation of distributed systems.