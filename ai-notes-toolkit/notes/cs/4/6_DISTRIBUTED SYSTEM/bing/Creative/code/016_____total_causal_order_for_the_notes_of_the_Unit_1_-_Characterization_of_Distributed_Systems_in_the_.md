# Total Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent and autonomous processes that communicate and coordinate with each other by exchanging messages.
- A distributed system may exhibit concurrency, asynchrony, partial failure, and non-determinism.
- To reason about the behavior and properties of a distributed system, it is necessary to define a notion of time and order among the events that occur in the system.
- An event is anything that happens at a point in time in a process, such as sending or receiving a message, performing a computation, or changing a state.
- A partial order is a binary relation that is reflexive, antisymmetric, and transitive. A partial order can be represented by a directed acyclic graph (DAG), where the nodes are the events and the edges are the order relation.
- A total order is a partial order that is also total, meaning that any two events are comparable. A total order can be represented by a linear sequence of events, where the order relation is the precedence relation.
- A causal order is a partial order that captures the notion of potential causality among events. An event e1 is said to causally precede an event e2, denoted by e1 -> e2, if one of the following conditions holds:
  - e1 and e2 are events in the same process, and e1 occurred before e2.
  - e1 is the sending of a message m, and e2 is the receipt of the same message m.
  - There exists an event e3 such that e1 -> e3 and e3 -> e2.
- A total causal order is a total order that is consistent with the causal order, meaning that if e1 -> e2, then e1 precedes e2 in the total order. A total causal order establishes a unique linearization of all the events in the system, even those that are concurrent or independent.
- A total causal order is the strictest ordering in distributed systems, as it imposes a global synchronization among all the processes. It can be useful for implementing consistent and reliable services, such as atomic broadcast, consensus, or distributed transactions.
- A total causal order can be achieved by using a logical clock, such as a vector clock, that assigns a timestamp to each event, such that the timestamp reflects the causal order. A total causal order can then be obtained by sorting the events according to their timestamps. Alternatively, a total causal order can be achieved by using a sequencer, which is a special process that assigns a sequence number to each message, such that the sequence number reflects the total order. A total causal order can then be obtained by delivering the messages according to their sequence numbers.