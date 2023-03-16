### Unit 10 - Replication: Highly Available Services

- Highly available services are designed to ensure that the system remains operational and accessible to users, even in the event of failures or disruptions.
- Replication is a key technique used to achieve high availability, by creating multiple copies of data or services and distributing them across different nodes or locations.
- This allows the system to continue functioning even if one or more nodes fail, as other nodes can take over and provide the necessary services.
- Replication can be implemented at different levels, such as data replication, where multiple copies of the data are stored, or service replication, where multiple instances of a service are run.
- There are different approaches to replication, such as active-active, where all replicas are actively used and updated, or active-passive, where one replica is active and others are passive backups.
- Replication can also be synchronous, where updates are propagated to all replicas before the operation is considered complete, or asynchronous, where updates are propagated in the background.
- The choice of replication approach depends on factors such as the required level of availability, performance, and consistency.
- Replication can also be combined with other techniques such as load balancing and failover to further improve the availability and reliability of the system.