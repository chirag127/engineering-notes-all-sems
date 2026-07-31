# Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- Causal order is a partial order of messages in a distributed system that reflects the causal dependencies between events.
- Causal order is based on the happened-before relation, which is defined as follows:
  - If event a and event b occur in the same process, and a occurs before b, then a happened-before b (denoted as a -> b).
  - If event a is the sending of a message by one process and event b is the receipt of that message by another process, then a -> b.
  - If a -> b and b -> c, then a -> c (transitivity).
- Causal order ensures that if a message m1 causally precedes another message m2, then m1 is delivered before m2 to every process that receives both messages.
- Causal order is useful for maintaining consistency and coherence in distributed systems, such as replicated data, distributed transactions, and collaborative applications.
- Causal order can be implemented by various algorithms, such as vector clocks, logical clocks, or causal broadcast   .
- Causal order is weaker than total order, which requires that all messages are delivered in the same order to all processes, but stronger than unordered delivery, which does not impose any ordering constraints.