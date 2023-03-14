According to the web search results, cluster computing is a collection of tightly or loosely connected computers that work together as a single entity. The clusters are generally connected through fast local area networks (LANs) . Cluster computing can be classified into different types based on the purpose and the architecture of the clusters. Some of the common types are:

- High performance (HP) clusters: These clusters use computer clusters and supercomputers to solve advanced computational problems. They are designed to take advantage of the parallel processing power of several nodes .
- Load-balancing clusters: These clusters distribute incoming requests for resources among several nodes running similar programs or having similar content. This prevents any single node from receiving a disproportionate amount of work. This type of distribution is generally used in a web-hosting environment .
- High availability (HA) clusters: These clusters are designed to maintain redundant nodes that can act as backup systems in case of any failure. They provide consistent computing services like business activities, complex databases, customer services like e-websites and network file distribution. They are designed to provide uninterrupted data availability to the customers .

Cluster computing can also be classified into open clusters and closed clusters based on the visibility and accessibility of the nodes .

- Open clusters: These clusters require IPs for every node and those are accessed only through the internet or web. This type of cluster causes enhanced security concerns .
- Closed clusters: These clusters hide the nodes behind the gateway node, and they provide increased protection. They require fewer IP addresses and are good for computational tasks .

The following diagram illustrates the basic architecture of a cluster computing system using ASCII characters. The diagram shows a gateway node that connects the cluster to the internet or web, and several nodes that are connected to each other through a LAN. The nodes can be either single or multiprocessor systems with memory, input and output functions and an operating system  .

```
    +-----------------+       +-----------------+
    |                 |       |                 |
    |  Gateway Node   |       |  Internet/Web   |
    |                 |       |                 |
    +-----------------+       +-----------------+
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
            |                         |
+-----------------+ +-----------------+ +-----------------+ +-----------------+
|                 | |                 | |                 | |                 |
|     Node 1      | |     Node 2      | |     Node 3      | |     Node 4      |
|                 | |                 | |                 | |                 |
+-----------------+ +-----------------+ +-----------------+ +-----------------+
```