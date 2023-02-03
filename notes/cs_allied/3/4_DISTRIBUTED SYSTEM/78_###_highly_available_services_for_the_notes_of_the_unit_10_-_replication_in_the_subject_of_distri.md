### highly available services for the notes of the Unit 10 - Replication in the subject of DISTRIBUTED SYSTEM

Highly available services are services that are designed to provide continuous availability, even in the presence of failures. In the context of distributed systems, highly available services are services that are replicated across multiple nodes to ensure that they are always available, even if one or more nodes fail.

Highly available services can be achieved through various approaches, including:
1. Active-passive replication: a service is replicated on multiple nodes, with one node designated as the active node, and the others as passive nodes. The active node handles all requests, and the passive nodes are used as backups in case the active node fails.

2. Active-active replication: a service is replicated on multiple nodes, and all nodes are active and handle requests. The load is balanced across the nodes, and if one node fails, the others continue to handle requests.

3. Leader-follower replication: a service is replicated on multiple nodes, with one node designated as the leader, and the others as followers. The leader handles all requests, and the followers continuously synchronize with the leader to ensure that they are up-to-date.

Each approach has its own advantages and disadvantages, and the choice of approach depends on the specific requirements of the system.

In summary, Highly available services are services that are designed to provide continuous availability, even in the presence of failures. They can be achieved through approaches such as active-passive replication, active-active replication, and leader-follower replication, and the choice of approach depends on the specific requirements of the system.
