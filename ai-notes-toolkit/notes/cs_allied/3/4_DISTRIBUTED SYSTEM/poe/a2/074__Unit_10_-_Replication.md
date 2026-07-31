 Here is the formal content in markdown format without any emojis or external links:

## Unit 10 - Replication

1. Replication is the process of copying and distributing data and components to ensure high availability, fault tolerance, and improved performance.
2. Master-slave replication: In this method, one database server ("master") receives write operations/transactions and replicates/transmits them to one or more "slave" servers. The slaves can serve read-only queries, offloading read traffic from the master. If the master fails, one of the slaves can be promoted to become the new master.
3. Master-master replication: Both servers can receive write operations, and data is replicated bidirectionally between them. This provides increased redundancy and availability, as there is no single point of failure. Complex conflict resolution logic may be required if updates are made to the same data on both masters at the same time.
4. Cascading replication: In this model, a replica acts as the master for another replica, and so on. This can be used to scale replication to a larger number of nodes. However, it also introduces additional latency and complexity.
5. Peer-to-peer replication: There is no master server, and all nodes communicate with each other bidirectionally. This is a highly performant and scalable approach, but conflict resolution becomes more complex as there are multiple paths for data to converge. It is a popular choice for distributed systems and blockchains.

This covers the key points on replication in a formal tone with points instead of paragraphs and without any emojis or external links as instructed. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.