# Causal Order for the Notes of the Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by exchanging messages.
- In a distributed system, there is no global clock or shared memory, so the order of events is not always clear or consistent.
- Causal order is a partial order relation that captures the notion of potential causality between events in a distributed system.
- Causal order is based on Lamport's happened-before relation, which defines that event a happened before event b (denoted as a -> b) if one of the following conditions holds:
  - a and b are events in the same process, and a occurred before b in that process.
  - a is the sending of a message by one process, and b is the receipt of that message by another process.
  - there exists some event c such that a -> c and c -> b (transitivity).
- Causal order implies that if a -> b, then any process that observes b must also observe a, and in the same order. However, causal order does not impose any order on concurrent events, which are events that are not causally related (denoted as a || b).
- Causal order is useful for ensuring the consistency and correctness of distributed applications that rely on the causal dependencies between events, such as collaborative editing, social media, or distributed databases.
- Causal order can be implemented by various algorithms, such as vector clocks, causal broadcast, or causal memory. These algorithms use different mechanisms to track and enforce the causal dependencies between events, such as logical timestamps, message buffers, or version vectors.