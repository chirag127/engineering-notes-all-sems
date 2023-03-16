## Unit 3 - Data management issues, data replication for mobile computers, adaptive clustering for mobile

### Data management issues

- Data management technology that can support easy data access from and to mobile devices is among the main concerns in mobile information systems .
- Mobile computing may be considered a variation of distributed computing, where mobile devices are connected to fixed servers or databases via wireless networks .
- Some of the issues that arise in data management of mobile databases are:
  - Mobile database design: The frequent disconnection and reconnection of mobile devices pose challenges for handling queries and resolving global names.
  - Security: The data on mobile devices is more vulnerable to theft, loss, or damage than the data on fixed locations. Therefore, encryption, authentication, and backup mechanisms are needed to protect the data.
  - Data distribution and replication: The uneven and dynamic network bandwidth and availability require efficient strategies for distributing and replicating data among mobile and fixed nodes.
  - Data synchronization and reconciliation: The data updates on mobile devices need to be synchronized and reconciled with the data on fixed servers or databases, taking into account the possible conflicts and inconsistencies.
  - Data caching and prefetching: The limited battery power and storage capacity of mobile devices require effective techniques for caching and prefetching data to reduce the communication cost and improve the data availability.
  - Data broadcasting and dissemination: The broadcast nature of wireless networks can be exploited to disseminate data to multiple mobile devices simultaneously, reducing the network congestion and server load.
  - Data compression and transformation: The data transmitted over wireless networks can be compressed and transformed to reduce the transmission time and energy consumption, as well as to adapt to the device capabilities and user preferences.
  - Data querying and processing: The query processing and optimization techniques for mobile databases need to consider the network and device constraints, as well as the user context and location.

### Data replication for mobile computers

- Data replication is the process of creating and maintaining multiple copies of the same data on different nodes in a distributed system.
- Data replication for mobile computers aims to improve the data availability, reliability, and performance for mobile users, as well as to reduce the network traffic and server load.
- Data replication for mobile computers faces several challenges, such as:
  - Replication granularity: The choice of the unit of replication (e.g., file, record, page, object) affects the replication overhead and consistency.
  - Replication placement: The decision of where to place the replicas (e.g., on mobile devices, on fixed servers, on intermediate nodes) affects the replication accessibility and cost.
  - Replication strategy: The policy of when and how to create, update, and delete replicas (e.g., eager, lazy, hybrid) affects the replication freshness and consistency.
  - Replication consistency: The degree of agreement among the replicas (e.g., strict, causal, eventual) affects the replication correctness and complexity.
  - Replication management: The mechanisms for coordinating and controlling the replication activities (e.g., centralized, distributed, hierarchical) affect the replication scalability and robustness.

### Adaptive clustering for mobile

- Adaptive clustering is a technique for organizing mobile nodes into groups or clusters based on their proximity, connectivity, or similarity.
- Adaptive clustering for mobile aims to facilitate the data management, communication, and coordination among mobile nodes, as well as to reduce the network overhead and complexity.
- Adaptive clustering for mobile faces several challenges, such as:
  - Cluster formation: The criteria and algorithms for forming clusters (e.g., based on location, distance, mobility, or interest) affect the cluster quality and stability.
  - Cluster maintenance: The methods and protocols for maintaining clusters (e.g., by electing cluster heads, updating cluster memberships, or merging and splitting clusters) affect the cluster efficiency and adaptability.
  - Cluster utilization: The applications and services that can benefit from clustering (e.g., data dissemination, routing, location management, or resource allocation) affect the cluster usefulness and performance.