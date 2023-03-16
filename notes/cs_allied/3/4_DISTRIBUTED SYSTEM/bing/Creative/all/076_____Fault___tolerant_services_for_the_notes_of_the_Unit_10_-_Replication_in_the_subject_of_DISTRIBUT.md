# Fault-Tolerant Services for the Notes of the Unit 10 - Replication in the Subject of Distributed System

- Fault-tolerant services are services that can continue to function correctly even in the presence of failures, such as server crashes, network partitions, or malicious attacks.
- Replication is a technique for implementing fault-tolerant services by creating and maintaining multiple copies of the same service or data on different servers or locations.
- Replication can improve the availability, performance, and reliability of distributed systems, but also introduces challenges such as consistency, coordination, and recovery.
- There are two main classes of replication techniques: primary-backup replication and active replication.
  - Primary-backup replication: One server acts as the primary and handles all the requests from the clients, while the others act as backups and receive updates from the primary. The primary is responsible for ensuring the consistency and order of the updates. If the primary fails, one of the backups takes over as the new primary.
  - Active replication: All servers are active and execute the same requests from the clients in the same order. The servers use a consensus protocol to agree on the order of the requests. The clients receive responses from all servers and ignore the faulty ones.
- There are also different models of faults that can affect the replicated services: crash faults, omission faults, and Byzantine faults.
  - Crash faults: A server stops functioning and does not send or receive any messages.
  - Omission faults: A server fails to send or receive some messages, but otherwise functions correctly.
  - Byzantine faults: A server behaves arbitrarily and may send incorrect or conflicting messages to other servers or clients.
- The number and type of faults that a replicated service can tolerate depends on the replication technique and the assumptions about the system. For example, to tolerate f crash faults, a primary-backup replication scheme needs at least f+1 replicas, while an active replication scheme needs at least 2f+1 replicas. To tolerate f Byzantine faults, an active replication scheme needs at least 3f+1 replicas.
- Replication can also be combined with other techniques, such as coding theory, to achieve fault-tolerance with less overhead or more efficiency. For example, fused state machines use a combination of coding theory and replication to ensure low overhead during normal operations and savings in storage and messages, but may incur higher overhead during recovery from faults .