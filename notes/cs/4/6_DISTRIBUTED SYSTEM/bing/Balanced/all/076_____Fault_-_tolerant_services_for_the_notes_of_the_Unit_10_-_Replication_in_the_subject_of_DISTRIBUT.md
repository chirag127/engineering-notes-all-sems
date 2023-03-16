# Fault-Tolerant Services for the Notes of the Unit 10 - Replication in the Subject of Distributed System

Fault-tolerant services are services that can continue to function correctly even in the presence of failures, such as server crashes, network partitions, or malicious attacks. Replication is a common technique for achieving fault tolerance in distributed systems, by maintaining multiple copies of the same service or data across different nodes.

There are two main classes of replication techniques: primary-backup replication and active replication.

- Primary-backup replication: In this technique, one of the replicas is designated as the primary, and the others are backups. The primary is responsible for processing client requests and updating the backups. The backups are passive and only respond to the primary. If the primary fails, a new primary is elected from the backups. This technique requires less communication and computation than active replication, but it introduces a single point of failure and a bottleneck in the primary.

- Active replication: In this technique, all the replicas are active and process client requests in the same order. The replicas use a consensus protocol to agree on the order of requests and ensure consistency. This technique tolerates more failures than primary-backup replication, and does not have a single point of failure or a bottleneck. However, it requires more communication and computation than primary-backup replication, and it may introduce more latency and overhead.

There are also different models of faults that can affect replicated services, such as crash faults, omission faults, timing faults, and Byzantine faults.

- Crash faults: A crash fault occurs when a node stops functioning and does not send or receive any messages. This is the simplest and most common type of fault in distributed systems. Replication can tolerate crash faults by having enough replicas to continue the service in case some of them crash.

- Omission faults: An omission fault occurs when a node fails to send or receive some messages, but does not crash completely. This type of fault can be caused by network congestion, packet loss, or buffer overflow. Replication can tolerate omission faults by using reliable communication protocols, such as TCP, or by using timeouts and retransmissions.

- Timing faults: A timing fault occurs when a node deviates from the expected timing behavior, such as violating a deadline, sending a message too early or too late, or having a skewed clock. This type of fault can be caused by hardware or software errors, or by network delays or synchronization issues. Replication can tolerate timing faults by using synchronization protocols, such as NTP, or by using logical clocks, such as Lamport timestamps or vector clocks.

- Byzantine faults: A Byzantine fault occurs when a node behaves arbitrarily, such as sending incorrect or conflicting messages, or colluding with other faulty nodes. This type of fault can be caused by malicious attacks, software bugs, or hardware faults. Replication can tolerate Byzantine faults by using cryptographic techniques, such as digital signatures or encryption, or by using Byzantine agreement protocols, such as PBFT or Zyzzyva.