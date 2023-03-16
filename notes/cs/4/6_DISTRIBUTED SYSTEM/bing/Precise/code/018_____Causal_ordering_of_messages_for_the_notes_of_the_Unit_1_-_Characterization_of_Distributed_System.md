### Causal ordering of messages

Causal ordering of messages is a concept in distributed systems that ensures that messages are delivered in an order that respects the cause-and-effect relationship between events.

1. In a distributed system, events can occur concurrently and independently at different nodes.
2. The order in which these events occur can affect the outcome of the system.
3. Causal ordering ensures that if an event `e1` causally precedes another event `e2`, then `e1` must be delivered before `e2` at all nodes.
4. This is achieved by attaching a vector timestamp to each message, which records the number of events that have occurred at each node.
5. When a node receives a message, it compares the vector timestamp of the message with its own vector timestamp to determine if the message can be delivered or if it must be delayed until all causally preceding messages have been delivered.
6. Causal ordering is important in distributed systems because it ensures that the system behaves in a predictable and consistent manner, even in the presence of concurrency and asynchrony.
