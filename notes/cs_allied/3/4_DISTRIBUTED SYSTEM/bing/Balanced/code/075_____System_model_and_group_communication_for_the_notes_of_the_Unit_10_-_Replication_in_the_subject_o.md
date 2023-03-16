### System model and group communication for replication in distributed systems

- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by passing messages .
- Replication is a technique to improve the availability, performance, and fault tolerance of a distributed system by creating and maintaining multiple copies of the same data or service .
- A system model is a set of assumptions and properties that describe the behavior and characteristics of a distributed system, such as the communication model, the failure model, the timing model, and the security model .
- Group communication is a form of communication between multiple processes in a distributed system that share some common interest or goal, such as replicating data or coordinating actions  .
- Group communication can be classified into two types: broadcast communication and multicast communication .
  - Broadcast communication is when a source process sends a message to all the processes in the system, regardless of their group membership or interest .
  - Multicast communication is when a source process sends a message to a subset of processes in the system that belong to a specific group or have a specific interest  .
- Group communication can also be characterized by the reliability and ordering guarantees it provides, such as reliable, atomic, causal, or total order multicast  .
  - Reliable multicast is when a message sent by a source process is delivered to all the processes in the group, or none of them, in case of a failure .
  - Atomic multicast is when a message sent by a source process is delivered to all the processes in the group atomically, meaning that either all or none of them receive the message, and they all agree on the delivery .
  - Causal multicast is when a message sent by a source process is delivered to all the processes in the group in a way that respects the causal order of events, meaning that if a message m1 causally precedes a message m2, then any process that receives m2 must have received m1 before .
  - Total order multicast is when a message sent by a source process is delivered to all the processes in the group in the same order, meaning that any two processes that receive the same set of messages agree on the order of delivery .
- Group communication is useful for replication in distributed systems because it allows the processes to synchronize their state and actions, to disseminate updates and queries efficiently, and to handle failures and inconsistencies gracefully  .