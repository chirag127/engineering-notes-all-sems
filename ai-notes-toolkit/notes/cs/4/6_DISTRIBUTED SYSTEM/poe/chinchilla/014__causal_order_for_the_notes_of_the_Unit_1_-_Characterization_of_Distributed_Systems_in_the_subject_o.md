### Causal Order for the Notes of Unit 1 - Characterization of Distributed Systems

Distributed systems are complex systems that involve multiple nodes communicating with each other. In such systems, it is essential to maintain a causal order of events to ensure consistency and correctness. In this unit, we will discuss the concept of causal order and its significance in distributed systems.

Here are the key points to note regarding causal order:

- Causal order is a relationship between two events in a distributed system, where one event is the cause and the other is the effect.
- Maintaining causal order is crucial in distributed systems, as it helps ensure consistency and correctness.
- In a distributed system, events can occur concurrently, and it is not always possible to determine which event occurred first. Therefore, it is necessary to define a causal relationship between events.
- To ensure causal order, events must be assigned unique identifiers such as timestamps or sequence numbers.
- The Lamport logical clock is commonly used to assign timestamps to events in a distributed system. The Lamport clock assigns a unique timestamp to each event and ensures that events with a lower timestamp occur before events with a higher timestamp.
- The happened-before relationship is used to define causality between events in a distributed system. If event A happened before event B, then A is the cause, and B is the effect.
- The happened-before relationship is transitive, meaning that if event A happened before event B and event B happened before event C, then A must have happened before C.
- In a distributed system, it is not always possible to determine the exact order of events. Therefore, we must rely on the happened-before relationship to ensure causal order.
- In summary, causal order is essential in distributed systems to ensure consistency and correctness. It is achieved by assigning unique identifiers to events and defining the happened-before relationship between events.

By understanding the concept of causal order, we can design and develop distributed systems that are reliable, consistent and correct. It is crucial to master this concept before moving on to more advanced topics in distributed systems.