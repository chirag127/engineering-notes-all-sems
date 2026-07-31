## Unit 3 - Data management issues, data replication for mobile computers, adaptive clustering for mobile

### Data management issues

- Data management technology that can support easy data access from and to mobile devices is among the main concerns in mobile information systems .
- Mobile computing may be considered a variation of distributed computing, where mobile devices are connected to a fixed network via wireless links .
- Some of the issues that arise in data management of mobile databases are:
  - Mobile database design: The frequent disconnection and reconnection of mobile devices pose challenges for handling queries and resolving global names.
  - Security: The data on mobile devices is more vulnerable to theft, loss, or damage than the data on fixed locations. Therefore, encryption, authentication, and backup mechanisms are needed.
  - Data distribution and replication: The uneven and dynamic network topology, the limited bandwidth and battery power, and the high mobility of mobile devices require efficient and adaptive strategies for data replication and synchronization.
  - Query processing and optimization: The query processing and optimization techniques for mobile databases need to consider the network heterogeneity, the location and context awareness, the data availability and consistency, and the user preferences and profiles.
  - Transaction management: The transaction management protocols for mobile databases need to cope with the issues of concurrency control, recovery, and commit in the presence of disconnections, failures, and mobility.
  - Data broadcasting and caching: Data broadcasting and caching are techniques to improve the data availability and reduce the communication cost for mobile devices. Data broadcasting involves disseminating data to a large number of mobile devices via a wireless channel, while data caching involves storing frequently accessed data on the mobile devices or intermediate servers.

### Data replication for mobile computers

- Data replication is the process of creating and maintaining multiple copies of the same data on different locations.
- Data replication for mobile computers aims to improve the data availability, reduce the communication cost, and enhance the system performance and scalability .
- Data replication for mobile computers faces several challenges, such as :
  - How to select the data items to be replicated and where to place them?
  - How to maintain the consistency and freshness of the replicated data in the presence of updates, disconnections, and mobility?
  - How to handle the conflicts and reconcile the divergent replicas when they reconnect?
  - How to adapt the replication strategy to the changing network conditions and user requirements?
- Data replication for mobile computers can be classified into two categories: server-initiated and client-initiated .
  - Server-initiated replication: The server decides which data items to replicate and where to place them, based on the global information about the system state and the user profiles. The server also initiates the data synchronization and conflict resolution processes. This approach is suitable for scenarios where the server has a high degree of control and the network is relatively stable .
  - Client-initiated replication: The client decides which data items to replicate and where to place them, based on the local information about the data access patterns and the network conditions. The client also initiates the data synchronization and conflict resolution processes. This approach is suitable for scenarios where the client has a high degree of autonomy and the network is highly dynamic .

### Adaptive clustering for mobile

- Adaptive clustering is a technique to organize the mobile devices into groups or clusters, based on some criteria such as location, connectivity, or similarity .
- Adaptive clustering for mobile aims to improve the data management and communication efficiency, reduce the network overhead and energy consumption, and enhance the system scalability and fault tolerance .
- Adaptive clustering for mobile faces several challenges, such as :
  - How to form and maintain the clusters in the presence of mobility, disconnections, and failures?
  - How to select the cluster heads or coordinators and balance the load among them?
  - How to handle the inter-cluster and intra-cluster communication and data exchange?
  - How to adapt the clustering strategy to the changing network conditions and user requirements?
- Adaptive clustering for mobile can be classified into two categories: centralized and distributed .
  - Centralized clustering: A central server or a designated cluster head is responsible for forming and maintaining the clusters, based on the global information about