### System model and group communication for replication in distributed systems

- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by exchanging messages.
- Replication is a technique to create and maintain multiple copies of the same data or service on different processes, for the purposes of fault tolerance, availability, performance, or scalability.
- A system model is a set of assumptions and properties that describe the behavior and characteristics of a distributed system, such as the communication model, the failure model, the timing model, and the consistency model.
- Group communication is a form of communication between multiple processes in a distributed system, where a group is a logical collection of processes that share some common interest or goal .
- Group communication can be classified into two types: broadcast communication and multicast communication.
  - Broadcast communication is when a source process sends a message to all the processes in the system, regardless of their group membership.
  - Multicast communication is when a source process sends a message to a subset of processes that belong to a specific group .
- Group communication can also be characterized by the reliability and ordering guarantees that it provides, such as best-effort, reliable, causal, total, or atomic.
  - Best-effort delivery means that the system tries to deliver the message to the destination processes, but there is no guarantee that it will succeed.
  - Reliable delivery means that the system guarantees that every message sent by a correct process will be eventually delivered to every correct process in the group.
  - Causal delivery means that the system guarantees that every message that causally depends on another message will be delivered after that message.
  - Total delivery means that the system guarantees that every message will be delivered to all the processes in the same order.
  - Atomic delivery means that the system guarantees that every message will be delivered to all the processes or none of them.
- Group communication is useful for implementing replication in distributed systems, as it allows the processes to coordinate their actions and maintain consistency among their replicas .
  - For example, a database cluster can use multicast to replicate the data among the nodes, and use a consensus protocol to agree on the order of the transactions.
  - Another example is a distributed file system that can use broadcast to propagate the updates to the files among the servers, and use a version vector to detect and resolve conflicts.