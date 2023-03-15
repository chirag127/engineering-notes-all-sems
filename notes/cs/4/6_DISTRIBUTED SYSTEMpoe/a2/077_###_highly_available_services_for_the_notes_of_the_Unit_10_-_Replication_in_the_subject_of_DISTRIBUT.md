 Here is the content in markdown format:

### Highly Available Services for the notes of the Unit 10 - Replication in the subject of DISTRIBUTED SYSTEM

Highly Available services aim to reduce downtime and ensure continued availability of services in the face of faults or other disruptions. Some key techniques to achieve high availability are:

1. Replication: Maintaining multiple identical copies of services/data on different machines. If one copy fails, others can continue providing service.
- Pros: High tolerance to failures. Services remain available even if some replicas fail.
- Cons: Higher resource usage (multiple copies). Increased complexity in replication management and consistency maintenance.

Mnemonics: Replicate for resilience. More copies mean more chances of survival.

2. Failover: Switching over to a redundant component (server/network path/etc.) upon failure of the primary component. The redundant component then takes over the functionality.
- Pros: Failure transparency and continued service.
- Cons: Additional resources required for the redundant component. Failover process must be efficient and automatic.

Mnemonics: Have a backup to take over when primary is down. No downtime if switch is quick.

3. Load balancing: Distributing workload/requests across multiple components to avoid overloading any one single component. This improves performance and can also aid in high availability by avoiding single points of failure.
- Pros: Better resource utilization and performance. Fault tolerance.
- Cons: Additional complexity in monitoring workloads and managing redistribution.

Mnemonics: Don't put all eggs in one basket. Spread the load for efficiency and robustness.

[Include diagrams/examples/codes/applications/advantages/disadvantages as needed.]

The key is to eliminate single points of failure and ensure service continuity through redundancy and alternatives. Highly available services are critical for many applications/systems to function reliably and meet strict availability requirements.