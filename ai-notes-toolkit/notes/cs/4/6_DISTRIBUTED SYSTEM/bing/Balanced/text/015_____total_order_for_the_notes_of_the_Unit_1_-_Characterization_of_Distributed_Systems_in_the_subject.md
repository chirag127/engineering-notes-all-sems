### Total Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent entities that communicate by message passing and coordinate their actions to achieve a common goal.
- Events are occurrences that happen at a specific point in time and space in a distributed system, such as sending or receiving a message, executing a statement, or accessing a shared resource.
- A partial order is a binary relation that satisfies three properties: reflexivity, antisymmetry, and transitivity. A partial order can be used to compare some but not all events in a distributed system, based on their causal relationship.
- A total order is a binary relation that satisfies four properties: reflexivity, antisymmetry, transitivity, and totality. A total order can be used to compare all events in a distributed system, regardless of their causal relationship.
- A total order can be established by using some arbitrary mechanism to break ties among events that are not causally related, such as the ID of the process, the timestamp of the event, or the lexicographic order of the message content.
- A total order can be useful for implementing distributed algorithms that require consistency, agreement, or coordination among the entities, such as mutual exclusion, atomic broadcast, consensus, or distributed transactions.