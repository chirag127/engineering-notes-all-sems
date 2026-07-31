### Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- Causal order is a way of defining the logical precedence of events in a distributed system, based on the potential causal influence between them.
- Causal order is important for ensuring the consistency and correctness of distributed applications, such as collaborative editing, chat systems, distributed databases, etc.
- Causal order is weaker than total order, which imposes a single linear sequence of all events in the system, even those that are concurrent. Causal order allows more concurrency and scalability, but also more complexity and ambiguity.
- Causal order can be defined formally using Lamport's happened-before relation: an event a happens before an event b (denoted as a -> b) if one of the following conditions holds :
  - a and b are events in the same process, and a occurs before b in the local clock order.
  - a is the sending of a message by one process, and b is the receipt of the same message by another process.
  - there exists some event c such that a -> c and c -> b (transitivity).
- Causal order can be implemented using various algorithms, such as vector clocks, causal broadcast, causal memory, etc . These algorithms typically require some form of metadata or communication overhead to track the causal dependencies among events.