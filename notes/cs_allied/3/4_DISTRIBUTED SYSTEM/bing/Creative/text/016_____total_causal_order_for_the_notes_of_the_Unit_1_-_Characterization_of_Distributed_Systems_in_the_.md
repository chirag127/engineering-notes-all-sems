### Total Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems in the Subject of Distributed System

- A distributed system is a collection of independent and autonomous processes that communicate and coordinate with each other by exchanging messages.
- Events are the actions or occurrences that happen in a distributed system, such as sending or receiving a message, executing a local operation, or detecting a failure.
- The order of events is important for understanding the behavior and correctness of a distributed system, especially in the presence of concurrency and failures.
- A partial order is a binary relation that satisfies three properties: reflexivity, antisymmetry, and transitivity. A partial order can be represented by a directed acyclic graph (DAG), where the nodes are the events and the edges are the order relation.
- A causal order is a partial order that captures the notion of potential causality between events. An event e1 is causally related to another event e2, denoted by e1 -> e2, if one of the following conditions holds:
  - e1 and e2 are events in the same process, and e1 happened before e2.
  - e1 is the sending of a message m, and e2 is the receipt of the same message m.
  - There exists an event e3 such that e1 -> e3 and e3 -> e2.
- A total order is a partial order that satisfies an additional property: comparability. This means that for any two events e1 and e2, either e1 -> e2, or e2 -> e1, or both (if e1 and e2 are the same event). A total order can be represented by a linear sequence of events, where the order relation is the same as the sequence order.
- A total causal order is a total order that is consistent with the causal order. This means that if e1 -> e2 in the causal order, then e1 -> e2 in the total order as well. A total causal order can be obtained by extending the causal order with a tie-breaking rule that determines the order of concurrent events (events that are not causally related).
- A total causal order is the strictest ordering in distributed systems; it establishes only one linearization, consistent with the causal order, among all the events that occur in the system, even those that occur concurrently. For that reason, the execution of the system is considered as synchronous.
- A total causal order is useful for implementing reliable and consistent services in distributed systems, such as atomic broadcast, distributed snapshots, consensus, and replication  .
- A total causal order can be implemented by using logical clocks, such as vector clocks, that capture the causal dependencies between events, and by using a deterministic algorithm, such as a sequencer or a leader, that assigns a unique and increasing identifier to each message .