### Fault-tolerant services

- A fault-tolerant service is a service that can continue to provide correct functionality despite the occurrence of faults in the system, such as server crashes, network partitions, or malicious attacks.
- Fault-tolerance is achieved by replicating the service state across multiple servers and coordinating the client interactions with the server replicas.
- Replication ensures that the service remains available and consistent even if some replicas fail or become isolated from the rest of the system.
- Replication also improves the performance of the service by allowing clients to access the closest or least loaded replica.

### Replication techniques

- There are two main classes of replication techniques: primary-backup replication and active replication.
- In primary-backup replication, one replica is designated as the primary and the others are backups. The primary receives all the client requests and executes them. The primary then sends the updates to the backups, which apply them to their local state. The backups only become active if the primary fails or is suspected to have failed.
- In active replication, all replicas receive and execute the same client requests in the same order. The replicas use a consensus protocol to agree on the order of requests and ensure consistency. The replicas send their responses to the clients, which accept the first valid response they receive.
- Primary-backup replication has lower overhead and latency than active replication, but it requires a reliable and timely failure detection mechanism to switch to a new primary when needed. Active replication does not rely on failure detection, but it requires more messages and computation than primary-backup replication.

### Group communication

- Group communication is a communication infrastructure that provides the adequate multicast primitives to implement replication techniques. A group is a set of processes that communicate with each other using group communication primitives.
- Group communication primitives include reliable multicast, which ensures that a message sent to a group is delivered to all group members or none, and total order multicast, which ensures that all group members deliver the same messages in the same order.
- Another important group communication primitive is view synchronous multicast, which ensures that all group members have a consistent view of the group membership and the messages delivered in each view. A view is a snapshot of the group composition at a given time. Views change when processes join or leave the group, or when they are suspected to have failed.
- Group communication can be used to implement primary-backup replication by electing a primary in each view and using reliable multicast to propagate the updates to the backups. Group communication can also be used to implement active replication by using total order multicast to agree on the order of requests and execute them at all replicas.