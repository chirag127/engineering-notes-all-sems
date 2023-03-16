### Fault-tolerant services for the notes of the Unit 10 - Replication in the subject of DISTRIBUTED SYSTEM

- Fault-tolerant services are services that can continue to function correctly even in the presence of failures, such as server crashes, network partitions, or malicious attacks.
- Replication is a technique for implementing fault-tolerant services by creating and maintaining multiple copies of the same service (or object) on different servers in a distributed system.
- Replication can improve availability, performance, and reliability of the service, but also introduces challenges such as consistency, concurrency, and communication overhead.
- The main classes of replication techniques are:
  - Primary-backup replication: One server acts as the primary (or leader) and handles all the requests from the clients, while the other servers act as backups (or followers) and receive updates from the primary. The primary is responsible for ensuring that the backups are consistent with it. If the primary fails, a new primary is elected from the backups.
  - Active replication: All servers act as replicas and execute the same requests from the clients in the same order. The replicas use a consensus protocol to agree on the order of requests and ensure consistency. If a replica fails, the remaining replicas can continue to serve the clients.
- The correctness criterion for replicated services is linearizability, which means that the service behaves as if there is only one copy of it and every request is executed atomically and in the order specified by the clients.
- The trade-offs between primary-backup replication and active replication are:
  - Primary-backup replication has lower communication overhead and latency than active replication, but requires more complex recovery mechanisms and may have lower availability and fault-tolerance.
  - Active replication has higher communication overhead and latency than primary-backup replication, but requires simpler recovery mechanisms and may have higher availability and fault-tolerance.