# Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent and autonomous processes that communicate by exchanging messages over a network.
- A distributed system may exhibit concurrency, asynchrony, partial failure, and non-determinism.
- In a distributed system, it is important to reason about the order of events and messages, as it affects the consistency and correctness of the system.
- Causal order is a partial order relation that captures the potential causal dependencies between events and messages in a distributed system.
- Causal order is defined as follows: 
  - If event A happens before event B in the same process, then A causally precedes B, denoted as A -> B.
  - If event A is the sending of a message m and event B is the receiving of the same message m, then A causally precedes B, denoted as A -> B.
  - If A -> B and B -> C, then A -> C (transitivity).
  - If A and B are concurrent events, meaning that neither A -> B nor B -> A, then they are causally unrelated, denoted as A || B.
- Causal order is a natural and intuitive way of ordering events and messages in a distributed system, as it reflects the possible causal influences between them.
- Causal order is also useful for ensuring causal consistency, which is a weaker form of consistency than sequential consistency, but allows more concurrency and scalability.
- Causal consistency requires that if a process observes an update, then it must also observe all the updates that causally precede it.
- Causal order can be implemented by using logical clocks, such as vector clocks or matrix clocks, that encode the causal dependencies between events and messages in a distributed system.
- Causal order can also be enforced by using causal delivery protocols, such as causal broadcast or causal multicast, that ensure that messages are delivered according to their causal order.