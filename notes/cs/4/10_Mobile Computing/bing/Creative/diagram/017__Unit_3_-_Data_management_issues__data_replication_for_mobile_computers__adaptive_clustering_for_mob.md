## Unit 3 - Data management issues, data replication for mobile computers, adaptive clustering for mobile

The following diagram illustrates the basic architecture of a data replication system for mobile computers:

```
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|  Mobile Host   |       |  Mobile Host   |       |  Mobile Host   |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|  Base Station  |       |  Base Station  |       |  Base Station  |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       +-----------------------+-----------------------+
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|  Data Server   |       |  Data Server   |       |  Data Server   |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
```

The diagram shows the following components:

- Mobile hosts: These are the devices that access data from the data servers via wireless networks. They may have limited storage, processing, and battery capacity. They may also move across different locations and networks, causing disconnections and handoffs.
- Base stations: These are the access points that provide wireless connectivity to the mobile hosts. They may also cache or replicate some data from the data servers to reduce the communication cost and latency for the mobile hosts.
- Data servers: These are the stationary computers that store the online databases. They may be distributed across different locations and networks, and may have different update frequencies and policies.

The data replication system aims to optimize the communication cost between the mobile hosts and the data servers, while maintaining the consistency and availability of the data. There are various static and dynamic data allocation methods that can be used to achieve this goal, depending on the cost model, the access pattern, and the update frequency of the data.

Some of the data management issues that arise in this system are:

- How to decide which data items to replicate or cache at the base stations or the mobile hosts, and how to update them efficiently and consistently    ?
- How to handle disconnections, handoffs, and failures of the mobile hosts, the base stations, or the data servers   ?
- How to adapt to the changing network conditions, user preferences, and data access patterns of the mobile hosts   ?
- How to balance the trade-off between communication cost, data consistency, and data availability   ?

One of the techniques that can be used to address some of these issues is adaptive clustering for mobile. This technique involves grouping the mobile hosts into clusters based on their physical proximity, network connectivity, or data access patterns. Each cluster has a leader that acts as a representative for the cluster and communicates with the data servers or other clusters. The leader may also cache or replicate some data for the cluster members. The