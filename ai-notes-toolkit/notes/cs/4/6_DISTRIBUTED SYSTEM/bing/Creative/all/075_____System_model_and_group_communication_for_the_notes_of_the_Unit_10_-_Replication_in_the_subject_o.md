# System model and group communication for replication in distributed systems

- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by passing messages .
- Replication is a technique to improve the availability, performance, and fault tolerance of a distributed system by creating and maintaining multiple copies of data or services .
- A system model is a set of assumptions and properties that describe the behavior and characteristics of a distributed system, such as the communication model, the failure model, the timing model, and the security model .
- Group communication is a form of communication between multiple processes in a distributed system that share some common interest or goal, such as replicating data or coordinating actions .
- Group communication can be classified into two types: broadcast communication and multicast communication .
  - Broadcast communication is when a source process sends a message to all other processes in the system, regardless of their group membership or interest .
  - Multicast communication is when a source process sends a message to a subset of processes in the system that belong to a specific group .
- Group communication can also be characterized by the reliability and ordering guarantees it provides, such as reliable, atomic, causal, or total order multicast .
  - Reliable multicast is when a message sent by a source process is delivered to all processes in the group, or none at all, in the presence of failures .
  - Atomic multicast is when a message sent by a source process is delivered to all processes in the group, or none at all, and all processes agree on the same set of messages delivered .
  - Causal multicast is when a message sent by a source process is delivered to all processes in the group, or none at all, and the delivery order respects the causal dependencies between messages .
  - Total order multicast is when a message sent by a source process is delivered to all processes in the group, or none at all, and the delivery order is the same for all processes .
- Group communication is useful for replication in distributed systems because it allows processes to disseminate and synchronize their data or state efficiently and consistently .
- Group communication can also be used to implement consensus protocols, which are algorithms that allow processes to agree on a common value or decision in the presence of failures .
- Consensus protocols are essential for replication in distributed systems because they enable processes to maintain a consistent view of the system state and resolve conflicts or inconsistencies that may arise due to concurrent updates or failures .
- Some examples of consensus protocols are Paxos, Raft, and Zab, which are used by distributed systems such as Google Chubby, Apache ZooKeeper, and Kafka .
- Replication in distributed systems can also be influenced by the consistency model, which defines the rules and expectations for reading and writing data across multiple replicas .
- Consistency models can be classified into two categories: strong consistency and weak consistency .
  - Strong consistency models guarantee that all replicas have the same value for a given data item at any point in time, and that any read operation returns the most recent write operation .
  - Weak consistency models allow replicas to have different values for a given data item at some point in time, and that some read operations may return stale or outdated values .
- Strong consistency models provide a simpler and more intuitive abstraction for replication in distributed systems, but they incur higher communication and coordination overhead and may reduce availability and performance .
- Weak consistency models provide a more flexible and efficient abstraction for replication in distributed systems, but they require more complex application logic and may introduce anomalies or inconsistencies .
- Some examples of strong consistency models are linearizability, sequential consistency, and serializability .
- Some examples of weak consistency models are eventual consistency, causal consistency, and session consistency .

: https://www.geeksforgeeks.org/group-communication-in-distributed-systems/
: https://medium.com/@queirozgustavo/group-communication-in-distributed-systems-385b8a44b8c9
: https://distributedsystemsblog.com/docs/group-communication/
: https://cs.gmu.edu/~setia/cs707/slides/replication2.pdf
: https://www-users.cselabs.umn.edu/classes