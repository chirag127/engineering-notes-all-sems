## Unit 3 - Data management issues, data replication for mobile computers, adaptive clustering for mobile

### Data management issues

- Data management technology that can support easy data access from and to mobile devices is among the main concerns in mobile information systems .
- Mobile computing may be considered a variation of distributed computing, where mobile devices are connected to fixed servers or databases through wireless networks .
- Some of the issues that arise in data management of mobile databases are:
  - Mobile database design: The frequent disconnection and reconnection of mobile devices pose challenges for handling queries and transactions, and for resolving global name conflicts.
  - Security: The data stored or transmitted by mobile devices is more vulnerable to unauthorized access, modification, or theft than the data at fixed locations. Therefore, encryption, authentication, and access control mechanisms are needed to protect the mobile data.
  - Data distribution and replication: The uneven and dynamic network connectivity of mobile devices requires efficient strategies for distributing and replicating data among fixed and mobile nodes, to improve data availability and performance.
  - Data caching and hoarding: The limited bandwidth and power of mobile devices motivate the use of data caching and hoarding techniques, which allow mobile devices to store frequently or recently accessed data locally, and to prefetch data that may be needed in the future.
  - Data synchronization and reconciliation: The data cached or hoarded by mobile devices may become stale or inconsistent with the data at the fixed servers or databases, due to updates or disconnections. Therefore, mechanisms are needed to synchronize and reconcile the data when the mobile devices reconnect to the network.
  - Data broadcasting and dissemination: The data broadcasting and dissemination techniques aim to deliver data to multiple mobile devices simultaneously, by using a single broadcast channel or a multicast group. This can reduce the network congestion and the power consumption of mobile devices.
  - Query processing and optimization: The query processing and optimization techniques for mobile databases need to consider the characteristics and constraints of mobile devices and wireless networks, such as limited resources, mobility, disconnection, and location-awareness.
  - Transaction management and recovery: The transaction management and recovery techniques for mobile databases need to ensure the ACID (atomicity, consistency, isolation, and durability) properties of transactions, despite the possibility of failures, disconnections, or conflicts.

### Data replication for mobile computers

- Data replication is the process of creating and maintaining multiple copies of the same data at different locations, to improve data availability, reliability, and performance.
- Data replication for mobile computers involves replicating data among fixed servers or databases and mobile devices, to cope with the challenges of mobile computing, such as limited bandwidth, frequent disconnection, and dynamic network topology.
- Data replication for mobile computers can be classified into two categories:
  - Server-initiated replication: The fixed servers or databases initiate the replication process, by pushing data updates to the mobile devices, or by pulling data updates from the mobile devices. This approach can reduce the communication cost and the data inconsistency, but it requires the servers to know the location and the interest of the mobile devices.
  - Client-initiated replication: The mobile devices initiate the replication process, by requesting data updates from the fixed servers or databases, or by sending data updates to the fixed servers or databases. This approach can increase the data autonomy and the flexibility of the mobile devices, but it may incur more communication cost and data inconsistency.
- Data replication for mobile computers can also be classified into two types:
  - Eager replication: The data updates are propagated to all the replicas as soon as they occur, to ensure that all the replicas are always consistent. This type of replication can provide fast and accurate query responses, but it requires a reliable and stable network connection, and it may cause update conflicts or deadlock.
  - Lazy replication: The data updates are propagated to the replicas only when the network connection is available, to tolerate network disconnection and failure. This type of replication can provide high data availability and low communication cost, but it may cause data inconsistency or staleness, and it requires reconciliation mechanisms.

### Adaptive clustering for mobile

- Adaptive clustering is a technique that dynamically organizes mobile devices into clusters, based on their location, mobility, and communication patterns, to facilitate data management and communication among mobile devices.
- Adaptive clustering for mobile can provide the following benefits:
  - Scalability: