# Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent and autonomous processes that communicate by exchanging messages over a network.
- The processes in a distributed system may have different views of the system state and the order of events, due to network delays, failures, or concurrency.
- Causal order is a partial order relation that captures the potential causal dependencies between events in a distributed system.
- Causal order is defined as follows: an event e1 is causally before an event e2 (denoted as e1 -> e2) if and only if one of the following conditions holds:
  - e1 and e2 are events in the same process, and e1 occurred before e2 in that process.
  - e1 is the sending of a message m, and e2 is the receipt of that message m.
  - There exists some event e3 such that e1 -> e3 and e3 -> e2 (transitivity).
- Causal order is important for ensuring the consistency and correctness of distributed applications, such as replicated data stores, collaborative editing, or distributed algorithms.
- Causal order can be implemented by various mechanisms, such as vector clocks, logical clocks, or message ordering protocols.
- Causal order can be classified into different levels of strictness, depending on how much concurrency is allowed between causally independent events:
  - Total-causal order is the strictest ordering in distributed systems; it establishes only one linearization, consistent with the causal ordering, among all the events that occur in the system, even those that occur concurrently. For that reason, the execution of the system is considered as synchronous .
  - Causal order is a weaker ordering than total-causal order; it allows different linearizations of concurrent events, as long as they respect the causal dependencies. For that reason, the execution of the system is considered as asynchronous .
  - Fuzzy causal order is a weaker ordering than causal order; it allows some violations of causal dependencies, as long as they are within a certain tolerance. For that reason, the execution of the system is considered as partially synchronous .
- Causal order is a trade-off between performance and consistency; the stricter the ordering, the more overhead and coordination is required, but the more predictable and reliable the system behavior is. The weaker the ordering, the more concurrency and scalability is possible, but the more anomalies and conflicts may arise.