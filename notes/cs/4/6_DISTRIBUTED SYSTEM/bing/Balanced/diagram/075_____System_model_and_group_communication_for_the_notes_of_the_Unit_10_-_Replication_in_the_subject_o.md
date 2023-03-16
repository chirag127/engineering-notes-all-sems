### System model and group communication for replication in distributed systems

- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by passing messages.
- Replication is a technique to improve the availability, reliability, and performance of a distributed system by creating and maintaining multiple copies of data or services across different processes or nodes.
- A system model is a set of assumptions and properties that describe the behavior and characteristics of a distributed system, such as the communication model, the failure model, the timing model, and the security model.
- Group communication is a form of communication between multiple processes in a distributed system that share some common interest or goal, such as replicating data or coordinating actions.
- Group communication can be classified into two types: broadcast communication and multicast communication.
  - Broadcast communication is when a source process sends a message to all other processes in the system, regardless of their interest or membership in a group. Broadcast communication can be used to disseminate information widely and efficiently, such as code or a file.
  - Multicast communication is when a source process sends a message to a subset of processes in the system that belong to a specific group. Multicast communication can be used to implement replication and consistency protocols, such as data updates or consensus.
- Group communication can also be characterized by the reliability and ordering guarantees it provides, such as reliable, atomic, causal, or total order delivery of messages.
  - Reliable delivery means that every message sent by a process is eventually received by all intended recipients, unless the sender or the receiver fails.
  - Atomic delivery means that every message sent by a process is either received by all or none of the intended recipients, and that the sender is notified of the outcome.
  - Causal delivery means that every message sent by a process is received by all intended recipients in the same causal order as they were sent, where causal order is defined by the happens-before relation between events in the system.
  - Total order delivery means that every message sent by a process is received by all intended recipients in the same order, regardless of the causal order or the sender identity.
- Group communication can be implemented using various protocols and algorithms, such as flooding, gossiping, spanning trees, logical clocks, vector clocks, or consensus algorithms. The choice of the protocol depends on the system model, the group size, the network topology, the communication cost, and the desired reliability and ordering guarantees.