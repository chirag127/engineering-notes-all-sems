# Total Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent entities that communicate by message passing and coordinate their actions to achieve a common goal.
- Events are occurrences that happen at a specific point in time and space in a distributed system.
- The order of events is important for understanding the behavior and correctness of a distributed system.
- A partial order is a binary relation that satisfies three properties: reflexivity, antisymmetry, and transitivity.
- A total order is a partial order that also satisfies the property of totality, which means that any two events are comparable.
- A distributed system is said to have partial order if we can have a partial order relationship among the events in the system .
- A distributed system is said to have total order if we can establish a causal relationship among all events in the system .
- A causal relationship between two events means that one event influences or causes the other event.
- A total order of events is useful for distributed system implementation, as it can help ensure consistency, agreement, and coordination among the entities .
- A total order of events can be achieved by using logical clocks, such as Lamport timestamps or vector clocks, that assign a unique and monotonically increasing value to each event .
- A total order of events can also be achieved by using atomic broadcast, which is a communication primitive that guarantees that all entities receive the same messages in the same order .
- A total order of events can be used to implement various distributed algorithms, such as mutual exclusion, consensus, leader election, replication, and fault tolerance  .