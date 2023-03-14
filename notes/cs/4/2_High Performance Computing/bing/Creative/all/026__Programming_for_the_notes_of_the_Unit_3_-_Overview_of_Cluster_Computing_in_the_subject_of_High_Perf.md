### Programming for the notes of the Unit 3 - Overview of Cluster Computing in the subject of High Performance Computing

- Cluster computing is a collection of tightly or loosely connected computers that work together so that they act as a single entity.
- The connected computers execute operations all together thus creating the idea of a single system.
- The clusters are generally connected through fast local area networks (LANs).
- Cluster computing gives a relatively inexpensive, unconventional to the large server or mainframe computer solutions.
- It resolves the demand for content criticality and process services in a faster way.
- It ensures that computational power is always available.
- It provides a single general strategy for the implementation and application of parallel high-performance systems independent of certain hardware vendors and their product decisions.
- Cluster computing can be classified into three types based on the purpose and design:
  - High performance (HP) clusters: HP clusters use computer clusters and supercomputers to solve advance computational problems. They are used to performing functions that need nodes to communicate as they perform their jobs. They are designed to take benefit of the parallel processing power of several nodes.
  - Load-balancing clusters: Incoming requests are distributed for resources among several nodes running similar programs or having similar content. This prevents any single node from receiving a disproportionate amount of task. This type of distribution is generally used in a web-hosting environment.
  - High Availability (HA) clusters: HA clusters are designed to maintain redundant nodes that can act as backup systems in case any failure occurs. Consistent computing services like business activities, complicated databases, customer services like e-websites and network file distribution are provided. They are designed to give uninterrupted data availability to the customers.
- Cluster computing can also be classified into two types based on the network configuration:
  - Open Cluster: IPs are needed by every node and those are accessed only through the internet or web. This type of cluster causes enhanced security concerns.
  - Close Cluster: The nodes are hidden behind the gateway node, and they provide increased protection. They need fewer IP addresses and are good for computational tasks.
- Cluster computing architecture is designed with an array of interconnected individual computers and the computer systems operating collectively as a single standalone system.
- It is a group of workstations or computers working together as a single, integrated computing resource connected via high speed interconnects.
- A node is either a single or a multiprocessor network having memory, input and output functions and an operating system.
- Two or more nodes are connected on a single line or every node might be connected individually through a LAN connection.
- A simple cluster computing layout is shown below:

```
    +-----------------+     +-----------------+     +-----------------+
    |                 |     |                 |     |                 |
    |     Node 1      |     |     Node 2      |     |     Node 3      |
    |                 |     |                 |     |                 |
    +-----------------+     +-----------------+     +-----------------+
            |                     |                     |
            |                     |                     |
            |                     |                     |
            |                     |                     |
            |                     |                     |
            |                     |                     |
            |                     |                     |
            |                     |                     |
            |                     |                     |
            +---------------------+---------------------+
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
                              |
                              |
                              |
                              |
                              |
                              |