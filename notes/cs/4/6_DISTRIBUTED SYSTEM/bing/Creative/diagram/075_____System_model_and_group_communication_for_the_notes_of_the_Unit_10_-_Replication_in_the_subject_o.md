### System model and group communication for replication in distributed systems

- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by exchanging messages.
- Replication is a technique to improve the availability, reliability, performance, and fault-tolerance of a distributed system by creating and maintaining multiple copies of data or services across different processes or nodes.
- A system model is a set of assumptions and properties that describe the behavior and characteristics of a distributed system, such as the communication model, the failure model, the timing model, and the security model.
- A group is a subset of processes in a distributed system that share some common interest or functionality, such as a replicated service, a multicast group, or a cluster.
- Group communication is a mechanism to send and receive messages among the members of a group in a distributed system, such as broadcast, multicast, or anycast.
- Group communication can be classified into two types: reliable and unreliable.
  - Reliable group communication guarantees that a message sent by a group member is delivered to all other group members in the same order, and that no message is lost, duplicated, or corrupted.
  - Unreliable group communication does not provide any guarantee on the delivery, order, or integrity of messages, and may result in message loss, duplication, or reordering.
- Group communication can also be classified into two modes: atomic and non-atomic.
  - Atomic group communication ensures that a message sent by a group member is delivered to all other group members atomically, meaning that either all or none of them receive the message, and that they all agree on the delivery status of the message.
  - Non-atomic group communication does not ensure atomicity, and may result in some group members receiving a message while others do not, or in different group members having different views on the delivery status of a message.
- Group communication is essential for replication in distributed systems, as it enables the coordination and synchronization of replicated data or services among different group members, and the dissemination of updates or requests to all or some of the replicas.
- Group communication can also be used to implement various replication strategies, such as primary-backup, active replication, passive replication, or quorum-based replication, depending on the consistency and availability requirements of the replicated data or service.
- Group communication can also be used to handle failures and recovery of replicated data or services, such as by detecting and excluding faulty replicas, electing new leaders or coordinators, or restoring the state of failed replicas from other group members.