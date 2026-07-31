# Unit 10 - Replication: Highly Available Services

- Highly available services are designed to ensure that the system remains operational even in the event of failures.
- Replication is a key technique used to achieve high availability.
- By replicating data and services across multiple nodes, the system can continue to function even if one or more nodes fail.
- Replication can be implemented at different levels, including at the data storage level, the application level, or the service level.
- There are different replication strategies, including active-active replication, where all replicas are available for read and write operations, and active-passive replication, where only one replica is available for write operations while the others are available for read operations.
- Replication can also be synchronous, where all replicas are updated simultaneously, or asynchronous, where updates are propagated to replicas with some delay.
- The choice of replication strategy depends on the requirements of the system, including the desired level of availability, performance, and consistency.
- Replication can also help improve performance by distributing the load across multiple nodes.
- However, replication also introduces challenges, such as the need to ensure consistency across replicas and to handle conflicts when multiple replicas are updated simultaneously.
- To address these challenges, various consistency models and conflict resolution strategies have been proposed.
