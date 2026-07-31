# Causal ordering of messages

- Causal ordering of messages is a partial ordering of messages in a distributed computing environment .
- It places a restriction on communication between processes by requiring that if the transmission of message mi to process pk necessarily preceded the transmission of message mj to the same process, then the delivery of these messages to that process must be ordered such that mi is delivered before mj .
- Causal ordering of messages is one of the four semantics of multicast communication, namely unordered, totally ordered, causal, and sync-ordered communication.
- Multicast communication methods vary according to the message’s reliability guarantee and ordering guarantee.
- Causal ordering of messages is based on the notion of potential causality, which is defined by Lamport's happened-before relation .
- The happened-before relation, denoted by ->, is a transitive, irreflexive, and antisymmetric relation that captures the causal dependencies between events in a distributed system .
- The happened-before relation is defined as follows :
  - If a and b are events in the same process, and a occurs before b, then a -> b.
  - If a is the event of sending a message by one process and b is the event of receiving the same message by another process, then a -> b.
  - If a -> b and b -> c, then a -> c.
- Causal ordering of messages ensures that if a message m1 causes another message m2, then m1 is delivered before m2 at every process that receives both messages .
- Causal ordering of messages can be implemented by various algorithms, such as vector clocks, causal broadcast, and causal multicast  .
- Vector clocks are logical clocks that assign a vector of timestamps to each event, such that the vector reflects the causal history of the event .
- Causal broadcast is a communication primitive that delivers messages to all processes in the same causal order .
- Causal multicast is a communication primitive that delivers messages to a subset of processes in the same causal order .
- Causal ordering of messages is useful for applications that require consistency and coordination among distributed processes, such as collaborative editing, distributed databases, and replicated state machines .