# Total Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent processes that communicate by exchanging messages over a network.
- Events are actions or occurrences that happen in a process, such as sending or receiving a message, executing a statement, or changing a state variable.
- The order of events in a distributed system is important for ensuring the consistency and correctness of the system's behavior and state.
- However, the order of events in a distributed system is not always obvious or unique, due to the lack of a global clock, the presence of concurrency, and the possibility of failures and delays.
- Therefore, different orderings of events can be defined based on different criteria and assumptions, such as the logical or physical time of events, the causal or potential dependencies among events, or the agreement or preference of processes.
- One of the possible orderings of events in a distributed system is the **total causal order**, which is the strictest ordering among all the orderings that respect the causal dependencies among events.
- The causal dependencies among events are defined by the **happened-before** relation, denoted by `->`, which is a partial order that satisfies the following properties:
  - If `a` and `b` are events in the same process, and `a` occurs before `b`, then `a -> b`.
  - If `a` is the event of sending a message by a process, and `b` is the event of receiving that message by another process, then `a -> b`.
  - If `a -> b` and `b -> c`, then `a -> c` (transitivity).
- The total causal order is a total order that extends the happened-before relation, meaning that it satisfies the following properties:
  - If `a -> b`, then `a` precedes `b` in the total causal order.
  - If `a` and `b` are concurrent events, meaning that neither `a -> b` nor `b -> a`, then `a` and `b` can be ordered arbitrarily in the total causal order, as long as the order is consistent for all processes.
- The total causal order establishes only one linearization, consistent with the causal ordering, among all the events that occur in the system, even those that occur concurrently. For that reason, the execution of the system is considered as synchronous.
- The total causal order can be implemented by using a **total order broadcast** protocol, which is a communication primitive that guarantees that all processes deliver the same set of messages in the same order, and that the order respects the causal dependencies among messages.
- A total order broadcast protocol can be based on different mechanisms, such as using a sequencer process, a logical clock, a vector clock, or a consensus algorithm, to assign a unique and monotonically increasing identifier to each message, and to order the messages according to their identifiers.