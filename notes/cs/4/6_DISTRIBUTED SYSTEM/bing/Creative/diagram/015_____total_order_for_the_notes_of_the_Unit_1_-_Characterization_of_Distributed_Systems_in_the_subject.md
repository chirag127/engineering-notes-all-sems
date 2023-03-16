### Total Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent entities that communicate by message passing and coordinate their actions to achieve a common goal.
- Events are occurrences that happen at a specific point in time and space in a distributed system.
- A partial order is a binary relation that is reflexive, antisymmetric, and transitive. For example, the relation "happens before" is a partial order among events in a distributed system.
- A total order is a partial order that is also complete, meaning that any two elements are comparable. For example, the relation "less than or equal to" is a total order among natural numbers.
- A distributed system is said to have partial order if we can have a partial order relationship among the events in the system. For example, if event A causes event B, then A happens before B, and this relation is transitive.
- A distributed system is said to have total order if we can establish a causal relationship among all events in the system. For example, if we assign a unique timestamp to each event, and use some arbitrary mechanism to break ties, then we can compare any two events by their timestamps.
- Total order is very useful for distributed system implementation, as it can help ensure consistency, reliability, and fault-tolerance . For example, if we want to implement a shared resource that can be used by only one process at a time, we can use total order to decide which process gets the resource first.
- Total order can be achieved by various algorithms and protocols, such as Lamport timestamps, vector clocks, logical clocks, atomic broadcast, etc  . These methods have different trade-offs in terms of complexity, performance, and scalability  .
- A diagram that illustrates the total order of events in a distributed system is shown below:

```
Process 1: a -> b -> c -> d
Process 2: e -> f -> g -> h
Process 3: i -> j -> k -> l

Messages: a -> f, b -> j, c -> k, g -> d, h -> l

Total order: a -> f -> b -> j -> c -> k -> g -> d -> h -> l -> e -> i
```

- In this diagram, the events are labeled by letters, and the messages are shown by arrows. The total order is determined by using Lamport timestamps and process IDs to break ties. The total order is consistent with the partial order induced by the "happens before" relation.