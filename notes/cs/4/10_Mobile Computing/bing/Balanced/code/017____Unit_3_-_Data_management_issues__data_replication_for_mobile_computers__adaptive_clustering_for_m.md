## Unit 3 - Data management issues, data replication for mobile computers, adaptive clustering for mobile

### Data management issues

- Data management technology that can support easy data access from and to mobile devices is among the main concerns in mobile information systems .
- Mobile computing may be considered a variation of distributed computing, where mobile devices are connected to a fixed network via wireless links .
- Some of the issues that arise in data management of mobile databases are:
  - Mobile database design: The frequent disconnection and reconnection of mobile devices pose challenges for handling queries and resolving global names.
  - Security: The data on mobile devices is more vulnerable to theft, loss, or damage than the data on fixed locations. Therefore, encryption, authentication, and backup mechanisms are needed.
  - Data distribution and replication: The uneven and dynamic network topology, the limited bandwidth and battery power, and the high mobility of mobile devices require efficient and adaptive strategies for data distribution and replication.
  - Data caching and hoarding: The data caching and hoarding techniques aim to improve the data availability and reduce the communication cost by storing frequently accessed or anticipated data on mobile devices.
  - Data dissemination and broadcasting: The data dissemination and broadcasting techniques aim to push relevant data to mobile devices based on their profiles, preferences, or subscriptions.
  - Transaction management: The transaction management techniques aim to ensure the consistency and reliability of data updates in the presence of mobility, disconnection, and concurrency.
  - Query processing and optimization: The query processing and optimization techniques aim to execute queries efficiently and effectively on mobile devices and fixed servers, taking into account the network and device constraints.

### Data replication for mobile computers

- Data replication is the process of creating and maintaining multiple copies of the same data on different locations.
- Data replication can improve the data availability, performance, and fault tolerance for mobile computers, but it also introduces challenges such as :
  - Replica placement: The replica placement problem is to decide where and how many replicas of each data item should be stored, considering the network topology, the access patterns, and the resource limitations .
  - Replica consistency: The replica consistency problem is to ensure that all replicas of the same data item have the same value, or at least an acceptable degree of divergence, despite the updates and disconnections .
  - Replica synchronization: The replica synchronization problem is to propagate the updates among the replicas and resolve any conflicts that may arise due to concurrent or delayed updates .
- Data replication can be classified into two types: eager replication and lazy replication .
  - Eager replication: Eager replication is a replication technique that propagates the updates to all replicas as soon as they occur, ensuring strong consistency among the replicas .
  - Lazy replication: Lazy replication is a replication technique that propagates the updates to the replicas only when they reconnect to the network, allowing temporary inconsistency among the replicas .

### Adaptive clustering for mobile

- Adaptive clustering is a technique that organizes mobile devices into groups called clusters, where each cluster has a leader called a clusterhead that coordinates the communication and data management within and among the clusters .
- Adaptive clustering can improve the scalability, efficiency, and robustness of mobile computing systems, but it also faces challenges such as :
  - Cluster formation: The cluster formation problem is to decide how to partition the mobile devices into clusters, considering the network topology, the device characteristics, and the application requirements .
  - Cluster maintenance: The cluster maintenance problem is to adapt the cluster structure to the changes in the network topology, such as the mobility, disconnection, or failure of mobile devices .
  - Clusterhead selection: The clusterhead selection problem is to decide which mobile device should act as the clusterhead for each cluster, considering the device capabilities, the network conditions, and the load balancing .
- Adaptive clustering can be classified into two types: centralized clustering and distributed clustering .
  - Centralized clustering: Centralized clustering is a clustering technique that relies on a central authority, such as a fixed