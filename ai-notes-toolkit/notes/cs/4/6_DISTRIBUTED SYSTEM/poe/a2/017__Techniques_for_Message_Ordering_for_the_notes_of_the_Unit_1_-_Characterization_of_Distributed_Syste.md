 Here is the content in Markdown format without any emojis or external links:

### Techniques for Message Ordering

1. Lamport Timestamps - Each message is stamped with a timestamp by the sender. The receiver delivers messages in the increasing order of timestamps. This ensures that if a message M1 is sent before M2, then M1 is delivered before M2.
2. Vector Clocks - Each process maintains a vector of logical clocks, one for each other process. Whenever a message is sent, the sender includes the value of its logical clock for the receiver. The receiver delivers messages in the increasing order of the senders' logical clocks and updates its logical clock values when a message is received. This ensures proper ordering as well as detection of causality violations.
3. Happened-before Relation - If two events e1 and e2 are related by the happened-before relation, then e1 must be ordered before e2. This relation is the transitive closure of the following relations:
- If e1 is the sending of a message m and e2 is the receipt of m, then e1 happens before e2.
- If e1 is the writing of a variable v by one process and e2 is the subsequent reading of v by another process, then e1 happens before e2.
- If e1 is in the past of process p and e2 is in the future of p, then e1 happens before e2.

By ensuring that events related by the happened-before relation are delivered in the same order, we can ensure proper message ordering.

The above points cover the major techniques for message ordering in distributed systems. The aim is to ensure that the order of messages received and delivered corresponds to the order in which they were sent so as to maintain consistency and avoid causality violations.