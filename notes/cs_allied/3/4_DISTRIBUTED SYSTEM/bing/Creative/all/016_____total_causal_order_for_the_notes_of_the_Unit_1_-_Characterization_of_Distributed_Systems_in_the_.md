# Total Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by exchanging messages.
- Events are the basic units of activity in a distributed system. An event can be a message send, a message receive, a local computation, or a failure.
- The order of events is important for understanding the behavior and correctness of a distributed system. However, due to the lack of a global clock and the uncertainty of message delays, it is not always possible to determine the exact order of events in a distributed system.
- A partial order is a relation that satisfies three properties: reflexivity, antisymmetry, and transitivity. A partial order can be used to compare events that are causally related, i.e., events that have a direct or indirect influence on each other.
- A total order is a relation that satisfies the properties of a partial order and also the property of totality, i.e., any two events can be compared. A total order can be used to compare events that are concurrent, i.e., events that have no causal relation.
- A causal order is a partial order that captures the causal dependencies among events in a distributed system. A causal order can be defined using the happened-before relation (→), which is derived from the following rules:
  - If a and b are events in the same process, and a occurs before b, then a → b.
  - If a is the sending of a message by one process and b is the receipt of the same message by another process, then a → b.
  - If a → b and b → c, then a → c.
- A total causal order is a total order that is consistent with the causal order, i.e., if a → b, then a precedes b in the total order. A total causal order can be achieved by using a logical clock, such as a Lamport clock or a vector clock, to assign timestamps to events and compare them according to the timestamps.
- A total causal order is useful for ensuring consistency and agreement among processes in a distributed system. For example, a total causal order can be used to implement a reliable broadcast service, where every process delivers the same set of messages in the same order. A total causal order can also be used to take consistent snapshots of the global state of a distributed system.