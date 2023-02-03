### Fault - tolerant services for the notes of the Unit 10 - Replication in the subject of DISTRIBUTED SYSTEM
Fault-tolerant services:

1. Definition: Services that continue to operate even when one or more components fail.

2. Key features:
- Redundant components: Multiple copies of critical components are maintained to ensure service availability.
- Load balancing: Requests are distributed across multiple components to ensure that no single component becomes a bottleneck.
- Failure detection: Mechanisms are in place to detect when a component has failed and to trigger recovery procedures.
- Recovery procedures: Procedures are in place to recover from component failure, such as restarting a failed component or redirecting requests to a backup component.

3. Examples: DNS, load balancers, databases with replication.

4. Benefits: Improved reliability, scalability, and availability.

5. Challenges: Complexity, coordination, and overhead of maintaining redundant components and recovery procedures.
