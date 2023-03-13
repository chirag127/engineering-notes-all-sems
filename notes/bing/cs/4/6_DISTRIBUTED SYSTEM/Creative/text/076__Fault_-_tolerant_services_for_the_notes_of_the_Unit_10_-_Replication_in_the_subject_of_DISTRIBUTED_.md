### Fault-tolerant services

- Fault-tolerant services are services that can continue to function correctly even in the presence of failures, such as server crashes, network partitions, or malicious attacks.
- Fault-tolerance is an important property for distributed systems, as failures are inevitable in large-scale and complex systems.
- One of the main techniques for achieving fault-tolerance is replication, which involves creating and maintaining multiple copies of the same service or data across different nodes in the system.
- Replication can improve the availability, performance, and reliability of the service, as well as provide consistency guarantees to the clients.
- However, replication also introduces challenges, such as how to coordinate the replicas, how to handle concurrent and conflicting updates, how to recover from failures, and how to balance the trade-offs between consistency and availability.

#### Replication techniques

- There are two main classes of replication techniques: primary-backup replication and active replication.
- Primary-backup replication is a passive replication technique, where one replica is designated as the primary and the others are backups. The primary receives and executes all the requests from the clients, and sends updates to the backups. The backups only execute the requests in case the primary fails or is suspected to fail.
- Active replication is an active replication technique, where all the replicas receive and execute the same requests from the clients, and produce the same outputs. The outputs are compared and agreed upon by a consensus protocol, such as Paxos or Raft, to ensure consistency and fault-tolerance.
- Primary-backup replication has the advantage of lower overhead and latency, as only one replica executes the requests and the backups can be updated asynchronously. However, it also has the disadvantage of lower fault-tolerance, as the primary is a single point of failure and the backups may lag behind the primary in terms of state.
- Active replication has the advantage of higher fault-tolerance, as any replica can serve the requests and the replicas are always in sync. However, it also has the disadvantage of higher overhead and latency, as all the replicas execute the same requests and the consensus protocol requires multiple rounds of communication.

#### Consistency models

- Consistency models are formal specifications of the behavior and guarantees of a replicated service, in terms of the order and visibility of the updates across the replicas and the clients.
- There are different levels of consistency models, ranging from strong to weak, depending on the trade-offs between consistency and availability.
- Strong consistency models, such as linearizability and serializability, require that all the replicas and the clients see the same order and state of the updates, as if they were executed atomically and sequentially by a single service. These models provide the highest level of consistency and correctness, but also the lowest level of availability and performance, as they require synchronous and coordinated communication among the replicas and the clients.
- Weak consistency models, such as eventual consistency and causal consistency, allow some degree of divergence and inconsistency among the replicas and the clients, as long as they eventually converge to the same state. These models provide the lowest level of consistency and correctness, but also the highest level of availability and performance, as they allow asynchronous and independent communication among the replicas and the clients.

#### References

: Lamport, L. (1978). Time, clocks, and the ordering of events in a distributed system. Communications of the ACM, 21(7), 558-565.

: Lamport, L. (1998). The part-time parliament. ACM Transactions on Computer Systems (TOCS), 16(2), 133-169.

: Schneider, F. B. (1990). Implementing fault-tolerant services using the state machine approach: A tutorial. ACM Computing Surveys (CSUR), 22(4), 299-319.

: Pedone, F., & Schiper, A. (1996, June). Fault-tolerance by replication in distributed systems. In International Conference on Reliable Software Technologies (pp. 38-57). Springer, Berlin, Heidelberg.

: Ongaro, D., & Ousterhout, J. (2014). In search of an understandable consensus algorithm. In 2014 {USENIX} Annual Technical Conference ({USENIX}{ATC} 14), 305-320.

: Lamport, L. (2001). Paxos made simple. ACM Sigact News, 32(4), 18-25.

[^7^