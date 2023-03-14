Message ordering is a fundamental problem in distributed systems, where processes communicate via message-passing and need to agree on a consistent order of events. There are different techniques for message ordering, depending on the desired properties and guarantees. Some of the common techniques are:

- Non-FIFO ordering: This is the simplest technique, where messages are delivered in any order, regardless of the order they were sent. This technique does not require any coordination or synchronization among processes, but it may lead to inconsistent views of the system state.
- FIFO ordering: This technique ensures that messages sent by the same process are delivered in the order they were sent. This technique requires each process to maintain a sequence number for each message it sends, and each receiver to buffer messages until they arrive in order. This technique preserves the causal order of events within a process, but not across processes.
- Causal ordering: This technique ensures that messages that are causally related are delivered in the order they were sent. Causal relation means that one message depends on another message, either directly or transitively. For example, if process A sends a message m1 to process B, and then process B sends a message m2 to process C, then m1 and m2 are causally related. This technique requires each process to maintain a vector clock for each message it sends or receives, and each receiver to buffer messages until they satisfy the causal order condition. This technique preserves the causal order of events across processes, but not the total order of events in the system.
- Total ordering: This technique ensures that all messages are delivered in the same order to all processes. This technique requires a global agreement among processes on the order of messages, which can be achieved by using a leader process, a consensus protocol, or a multicast algorithm. This technique preserves the total order of events in the system, but it may incur a high overhead in terms of communication and coordination.

The following diagram illustrates the basic architecture of a distributed system with message ordering techniques:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|   Process A    |     |   Process B    |     |   Process C    |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|   FIFO Queue   |     |   FIFO Queue   |     |   FIFO Queue   |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Vector Clock  |     |  Vector Clock  |     |  Vector Clock  |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Total Order   |     |  Total Order   |     |  Total Order   |
|   Protocol     |     |   Protocol     |     |   Protocol     |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Message       |     |  Message       |     |  Message       |
|   Passing      |     |   Passing      |     |   Passing      |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
```

Each process has a FIFO queue, a vector clock, and a total order protocol to implement different message ordering techniques. The message passing layer handles the communication among processes. Depending on the application requirements, a process can use one or more of these techniques to order the messages it sends or receives. For example, a process can use FIFO ordering for some messages, causal ordering for others, and total ordering for the rest.