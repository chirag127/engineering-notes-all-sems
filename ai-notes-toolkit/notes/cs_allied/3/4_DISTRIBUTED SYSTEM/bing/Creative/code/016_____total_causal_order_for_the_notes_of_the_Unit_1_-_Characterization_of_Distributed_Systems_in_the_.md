### Total Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems in the Subject of Distributed System

- A distributed system is a collection of independent and autonomous processes that communicate and coordinate with each other by exchanging messages.
- Events are the actions or occurrences that happen in a distributed system, such as sending or receiving a message, executing a local operation, or detecting a failure.
- The ordering of events is a way of defining the temporal relationship between events in a distributed system. There are different types of ordering, such as partial order, causal order, and total order.
- A partial order is a binary relation that satisfies three properties: reflexivity, antisymmetry, and transitivity. A partial order relation is denoted by ≤.
- A causal order is a partial order that captures the notion of causality between events. If an event e1 causes or influences another event e2, then e1 is causally before e2, denoted by e1 → e2. The causal order relation satisfies the following rules:
  - If e1 and e2 are events in the same process and e1 occurs before e2, then e1 → e2 (local order).
  - If e1 is the sending of a message m and e2 is the receipt of the same message m, then e1 → e2 (message order).
  - If e1 → e2 and e2 → e3, then e1 → e3 (transitivity).
- A total order is a partial order that satisfies an additional property: totality. This means that for any two events e1 and e2 in the system, either e1 ≤ e2 or e2 ≤ e1. A total order relation is denoted by <.
- A total causal order is a total order that is consistent with the causal order. This means that if e1 → e2, then e1 < e2. A total causal order relation is denoted by <<.
- A total causal order is the strictest ordering in distributed systems; it establishes only one linearization, consistent with the causal ordering, among all the events that occur in the system, even those that occur concurrently. For that reason, the execution of the system is considered as synchronous.
- A total causal order can be implemented by using a logical clock, such as a vector clock, that assigns a timestamp to each event. The timestamp is a vector of integers that reflects the causal history of the event. The total causal order relation can be defined as follows:
  - For any two events e1 and e2 with timestamps t1 and t2, e1 << e2 if and only if t1 < t2, where t1 < t2 means that for all i, t1[i] ≤ t2[i] and there exists j such that t1[j] < t2[j].
- A total causal order can be used to provide fault tolerance and consistency for constructing reliable distributed systems. For example, it can be used to implement a total order broadcast, a communication primitive that ensures that all processes deliver the same set of messages in the same order. It can also be used to implement a distributed snapshot, a technique that captures the global state of the system at a certain point in time.