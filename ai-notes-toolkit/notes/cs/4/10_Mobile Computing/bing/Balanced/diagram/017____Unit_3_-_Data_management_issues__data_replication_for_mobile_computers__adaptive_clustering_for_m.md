## Unit 3 - Data management issues, data replication for mobile computers, adaptive clustering for mobile

- Data management issues in mobile computing refer to the challenges and problems that arise when managing data in a mobile environment, where users can access data from and to mobile devices, such as smartphones, tablets, laptops, etc.
- Some of the data management issues in mobile computing are:

  - Mobile database design: This involves designing a database that can support the needs and requirements of mobile users, such as frequent disconnections, limited bandwidth, variable network quality, location awareness, etc. Mobile database design also has to deal with the global name resolution problem, which is the difficulty of identifying and locating data items in a distributed system.
  - Security: This involves protecting the data that is stored and transmitted in a mobile environment, which is more vulnerable to attacks, theft, loss, or damage than data in a fixed location. Security measures include encryption, authentication, authorization, access control, backup, etc.
  - Data distribution and replication: This involves deciding how to distribute and replicate data among mobile devices and fixed servers, to improve data availability, reliability, and performance. Data distribution and replication also have to consider the trade-offs between data consistency and data currency, which are the degree to which the data reflects the latest updates and the degree to which the data is synchronized across different copies, respectively.
  - Data caching: This involves storing frequently accessed or recently updated data in the local memory of mobile devices, to reduce the network traffic and the response time. Data caching also has to deal with the cache coherence problem, which is the difficulty of maintaining the consistency and validity of cached data when the original data is modified or invalidated.
  - Data synchronization: This involves updating and reconciling the data that is stored and modified in different locations, such as mobile devices and fixed servers, to ensure data consistency and currency. Data synchronization also has to deal with the conflict resolution problem, which is the difficulty of resolving the discrepancies and contradictions that may arise when different users or devices update the same data item concurrently or independently.
  - Data broadcasting: This involves transmitting data from a fixed server to multiple mobile devices simultaneously, to disseminate information efficiently and effectively. Data broadcasting also has to deal with the data indexing problem, which is the difficulty of organizing and accessing the data that is broadcasted in a sequential and periodic manner.

- Data replication for mobile computers is a technique that involves creating and maintaining multiple copies of data in different locations, such as mobile devices and fixed servers, to improve data availability, reliability, and performance in a mobile environment.
- Some of the benefits of data replication for mobile computers are:

  - It reduces the network traffic and the response time, by allowing mobile users to access local copies of data instead of remote copies of data.
  - It increases the data availability and reliability, by allowing mobile users to access data even when they are disconnected from the network or when the network is unreliable.
  - It enhances the data performance, by allowing mobile users to access data that is closer to their current location or context.

- Some of the challenges of data replication for mobile computers are:

  - It increases the storage space and the memory consumption, by requiring multiple copies of data to be stored and maintained in different locations.
  - It introduces the data consistency and currency issues, by requiring multiple copies of data to be synchronized and updated when the data is modified or invalidated.
  - It complicates the data management and the query processing, by requiring the data replication policies and the data access methods to be designed and implemented.

- Adaptive clustering for mobile is a technique that involves grouping mobile devices into clusters based on their proximity, connectivity, or similarity, to facilitate data management and communication in a mobile environment.
- Some of the benefits of adaptive clustering for mobile are:

  - It reduces the network traffic and the energy consumption, by allowing mobile devices to communicate with each other within clusters instead of with distant servers or devices.
  - It increases the data availability and reliability, by allowing mobile devices to share and backup data within clusters instead of relying on fixed servers or devices.
  - It enhances the data performance and quality, by allowing mobile devices to access data that is relevant to their current location or context.

- Some of the challenges of adaptive clustering for mobile are:

  - It increases the computation and communication overhead, by requiring mobile devices to form and maintain clusters dynamically and periodically.
  - It introduces the cluster formation and maintenance issues, by requiring the cluster criteria and the cluster protocols to be defined and executed.
  - It complicates the data management and the query processing, by requiring the data distribution and replication strategies and the data access methods to