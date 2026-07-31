### Causal ordering of messages

- Causal ordering of messages is a partial ordering of messages in a distributed computing environment .
- It places a restriction on communication between processes by requiring that if the transmission of message mi to process pk necessarily preceded the transmission of message mj to the same process, then the delivery of these messages to that process must be ordered such that mi is delivered before mj .
- Causal ordering of messages is one of the four semantics of multicast communication, namely unordered, totally ordered, causal, and sync-ordered communication.
- Multicast communication methods vary according to the message’s reliability guarantee and ordering guarantee.
- Causal ordering of messages is based on the concept of potential causality, which is defined by the following rules :
  - If a process pi sends a message m1 and then sends another message m2, then m1 -> m2 (-> denotes potential causality).
  - If a process pi sends a message m1 to another process pj, and pj receives m1 and then sends a message m2 to another process pk, then m1 -> m2.
  - If m1 -> m2 and m2 -> m3, then m1 -> m3 (transitivity).
  - If not (m1 -> m2), then m1 and m2 are concurrent (denoted by m1 || m2), meaning that m1 cannot possibly have caused m2 .
- Causal ordering of messages can be implemented by various algorithms, such as vector clocks, logical clocks, or piggybacking  .
- Causal ordering of messages can help to ensure consistency, correctness, and fault tolerance in distributed systems  .