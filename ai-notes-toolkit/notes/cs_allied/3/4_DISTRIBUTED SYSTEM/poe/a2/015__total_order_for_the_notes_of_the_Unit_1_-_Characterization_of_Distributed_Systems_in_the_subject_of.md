 Here are the notes for Unit 1 - Characterization of Distributed Systems in a formal tone without emojis or external links:

### Total Order

1. In distributed systems, events occur at different processes simultaneously. There is a need to establish a global ordering of these events to maintain consistency.
2. A total order is a strict ordering of events such that if event x precedes event y in the total order, then all correct processes agree on this ordering.
3. There are a few ways to achieve total ordering:
- Using a central sequencer: A central server receives timestamped events and assigns IDs to establish ordering. However, this creates a single point of failure.
- Using a distributed sequencer: Multiple servers assign partial orders, which are then merged to obtain a total order. This avoids a single point of failure but is more complex to implement.
- Using communication-induced ordering: If event x is the cause of event y, then y is ordered after x. This restricts the types of events that can be totally ordered.
- Using happened-before relationship: If event x happens before event y in the same process, or if x is the sending of a message and y is the receipt of that message, then x is ordered before y. This preserves causality but may not establish a total order.

In summary, total ordering of events is necessary to maintain consistency in distributed systems. There are a few approaches to achieve total ordering, each with their own trade-offs. The choice of approach depends on the system requirements and the types of events that need to be ordered.