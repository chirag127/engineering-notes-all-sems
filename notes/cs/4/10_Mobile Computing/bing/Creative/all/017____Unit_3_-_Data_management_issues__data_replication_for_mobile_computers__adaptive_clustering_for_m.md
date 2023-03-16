# Unit 3 - Data management issues, data replication for mobile computers, adaptive clustering for mobile

- Data management issues
  - Data management is the process of collecting, storing, processing, and distributing data in a mobile computing environment.
  - Data management issues arise due to the characteristics of mobile computing, such as mobility, heterogeneity, disconnection, limited resources, and security.
  - Some of the data management issues are:
    - Data availability: How to ensure that data is accessible to mobile users even when they are disconnected from the network or move across different networks.
    - Data consistency: How to maintain the integrity and correctness of data when it is replicated or cached on multiple devices or servers.
    - Data synchronization: How to coordinate the updates and changes of data among different replicas or caches.
    - Data dissemination: How to efficiently and effectively distribute data to mobile users according to their interests, preferences, and contexts.
    - Data security: How to protect data from unauthorized access, modification, or disclosure when it is transmitted or stored on mobile devices or servers.

- Data replication for mobile computers
  - Data replication is a technique to improve data availability and performance by creating and maintaining multiple copies of data on different devices or servers.
  - Data replication for mobile computers is a special case of data replication that considers the challenges and requirements of mobile computing, such as frequent disconnection, limited bandwidth, and variable network quality.
  - Data replication for mobile computers can be classified into two types: client-initiated and server-initiated.
    - Client-initiated replication: The mobile client decides when and what data to replicate from the server, based on its needs and resources. The client is responsible for managing and synchronizing the replicas with the server.
    - Server-initiated replication: The server decides when and what data to replicate to the mobile client, based on its policies and knowledge. The server is responsible for managing and synchronizing the replicas with the client.
  - Data replication for mobile computers can also be classified into two modes: eager and lazy.
    - Eager replication: The replicas are updated as soon as possible after a change occurs on the original data. Eager replication ensures strong consistency, but requires high communication cost and availability.
    - Lazy replication: The replicas are updated periodically or on demand after a change occurs on the original data. Lazy replication reduces communication cost and tolerates disconnection, but may cause weak consistency and conflicts.

- Adaptive clustering for mobile
  - Adaptive clustering is a technique to organize mobile nodes into groups or clusters based on their proximity, similarity, or functionality.
  - Adaptive clustering for mobile aims to achieve efficient and scalable data management, communication, and coordination among mobile nodes, especially in ad hoc or peer-to-peer networks.
  - Adaptive clustering for mobile can be classified into two types: centralized and distributed.
    - Centralized clustering: A single node or a set of nodes act as the cluster head or leader, and control the formation and maintenance of the cluster. The cluster head is responsible for managing the cluster members, routing the messages, and providing services to the cluster.
    - Distributed clustering: All nodes participate in the formation and maintenance of the cluster, and share the responsibilities of the cluster head. The cluster is self-organized and self-healing, and adapts to the changes in the network topology and conditions.
  - Adaptive clustering for mobile can also be classified into two modes: static and dynamic.
    - Static clustering: The clusters are formed once and remain unchanged until the network is reconfigured or terminated. Static clustering simplifies the cluster management, but may not reflect the current network state or user needs.
    - Dynamic clustering: The clusters are formed and reformed dynamically according to the network state or user needs. Dynamic clustering adapts to the network changes, but may incur high overhead and instability.