# Total Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems in the Subject of Distributed System

- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by passing messages.
- A distributed system may exhibit different types of ordering among the messages exchanged by the processes, depending on the application requirements and the system model.
- One of the ordering types is **total causal order**, which is the strictest ordering in distributed systems.
- Total causal order has the following properties  :
  - It establishes only one linearization, consistent with the causal ordering, among all the events that occur in the system, even those that occur concurrently.
  - It ensures that if any process delivers a message m1 before m2, then all processes will deliver m1 before m2.
  - It implies FIFO ordering, since any two multicasts by the same process are related by the happened-before relation.
  - It does not imply causal ordering, just says that all processes must agree on the same order of messages.
- Total causal order can be achieved by using different algorithms, such as vector clocks, logical clocks, or sequencer-based algorithms .
- Total causal order can be useful for providing fault tolerance, consistency, and synchronization for constructing reliable distributed systems.