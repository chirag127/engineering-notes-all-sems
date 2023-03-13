### Total order for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A distributed system is a collection of independent entities that communicate by message passing and coordinate their actions to achieve a common goal.
- Events are the occurrences of actions or state changes in a distributed system, such as sending or receiving a message, accessing a shared resource, or executing a computation.
- The order of events is important for understanding the behavior and correctness of a distributed system, especially when there are concurrent or conflicting events.
- A partial order is a binary relation that satisfies three properties: reflexivity, antisymmetry, and transitivity. A partial order can be represented by a directed acyclic graph (DAG), where the nodes are the events and the edges are the order relation.
- A total order is a special case of a partial order, where every pair of events is comparable, i.e., there is a causal relationship between them. A total order can be represented by a linear sequence of events, where the order relation is consistent with the partial order.
- A distributed system is said to have partial order if we can have a partial order relationship among the events in the system. If 'totality', i.e., causal relationship among all events in the system, can be established, then the system is said to have total order.
- Total order is very useful for distributed system implementation, as it can help ensure consistency, agreement, and coordination among the entities in the system. For example, total order can be used to implement mutual exclusion, atomic broadcast, consensus, and replication protocols.
- However, total order is not easy to achieve in a distributed system, as there is no global clock or shared memory to synchronize the events. Therefore, various algorithms and techniques have been proposed to establish total order in a distributed system, such as logical clocks, vector clocks, Lamport timestamps, and Paxos.
- A logical clock is a mechanism to assign logical timestamps to the events in a distributed system, such that the order of the timestamps reflects the causal order of the events. A logical clock can be implemented by using counters that are incremented by each entity when an event occurs, and piggybacked on the messages that are exchanged among the entities.
- A vector clock is an extension of a logical clock, where each entity maintains a vector of counters, one for each entity in the system. A vector clock can capture the partial order of concurrent events more precisely than a logical clock, as it can distinguish between events that are causally related and events that are causally independent.
- A Lamport timestamp is a special case of a logical clock, where the timestamps are scalar values that are totally ordered. Lamport timestamps can be used to create a total ordering of events in a distributed system by using some arbitrary mechanism to break ties (e.g. the ID of the process).
- Paxos is a family of algorithms that can achieve consensus among a set of entities in a distributed system, even in the presence of failures. Paxos can be used to implement a total order broadcast service, where every entity agrees on the same sequence of messages that are delivered in the system.

#### Mnemonics and learning tricks

- A possible mnemonic to remember the properties of a partial order is RAT: Reflexivity, Antisymmetry, and Transitivity.
- A possible mnemonic to remember the difference between a logical clock and a vector clock is LCV: Logical Clock is a scalar Value, Vector Clock is a Vector of values.
- A possible mnemonic to remember the name of Lamport timestamps is LAMP: Logical clock with Arbitrary tie-breaking Mechanism for Partial order.
- A possible mnemonic to remember the name of Paxos is PAX: Protocol for Agreement and eXchange.