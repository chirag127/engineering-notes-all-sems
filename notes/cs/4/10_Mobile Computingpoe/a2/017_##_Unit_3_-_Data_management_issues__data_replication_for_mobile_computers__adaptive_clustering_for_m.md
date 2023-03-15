 Here is the content in markdown format for the given topic:

## Unit 3 - Data management issues, data replication for mobile computers, adaptive clustering for mobile

### Data management issues for mobile computing

- Limited storage capacity: Mobile devices have limited storage capacity so efficient data management techniques are required to store and retrieve data.
- Limited battery power: Frequent access to storage devices consumes additional power, so power-efficient data management techniques are needed.
- Frequent disconnections: Mobile devices frequently move in and out of wireless coverage, so the data management system must tolerate frequent disconnections and offline operation.
- Data heterogeneity: Mobile devices may store/access data of multiple types (text, images, audio, video, etc.) and formats, requiring a versatile data management system.

### Data replication for mobile computing

- Data replication is used to improve data availability and access latency for mobile users.
- Data is copied from centralized servers to mobile clients, allowing them to operate while disconnected.
- Different replication strategies are used:
    - Full replication: Entire data is copied to every mobile client. Not scalable.
    - Selective replication: Only subset of data is copied based on access patterns. More efficient.
    - Caching: Recently/frequently accessed data is temporarily stored in client cache. Further reduces latency.
- Challenges: Managing consistency between replicated copies, handling partial updates & conflicts, adapting to dynamic access patterns, minimizing replication overhead.

### Adaptive data clustering for mobile computing

- Groups similar data items together into clusters to reduce number of replicas and improve scalability.
- Clusters are dynamically adapted based on access patterns to balance between cluster size (smaller clusters reduce replication overhead but increase number of clusters) and inter-cluster distance (larger inter-cluster distance reduces access latency but may exceed disconnection tolerance).
- Example: Cluster web pages based on their categories to group pages on similar topics into same cluster.
- Challenges: Handling clustering with skewed/dynamic access patterns, providing load balancing, adapting to changes in data characteristics.