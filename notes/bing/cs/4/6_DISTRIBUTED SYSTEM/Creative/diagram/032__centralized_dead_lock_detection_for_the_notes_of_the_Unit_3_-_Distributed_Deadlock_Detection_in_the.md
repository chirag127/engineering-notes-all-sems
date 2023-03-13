The following text and diagram illustrate the basic architecture of a centralized deadlock detection approach in a distributed system, based on the information from the web search results    .

A centralized deadlock detection approach uses a single chosen site, called the deadlock-detection coordinator, to maintain a global wait-for graph of processes and the resources they are using or requesting in the distributed system. The coordinator collects information from all the other sites about their local wait-for graphs and merges them into a global one. Then, the coordinator applies a deadlock detection algorithm, such as cycle detection, to the global wait-for graph and identifies any deadlocks. If a deadlock is detected, the coordinator informs the involved sites and initiates a recovery action, such as aborting or preempting some processes.

The centralized deadlock detection approach has some advantages and disadvantages. The advantages are:

- It is simple and easy to implement.
- It avoids the overhead of distributed communication and synchronization for deadlock detection.
- It can detect global deadlocks that span multiple sites.

The disadvantages are:

- It introduces a single point of failure and a performance bottleneck at the coordinator site.
- It requires frequent and costly message exchanges between the coordinator and the other sites to update the global wait-for graph.
- It may detect false deadlocks due to stale or incomplete information.

The diagram below shows an example of a centralized deadlock detection approach in a distributed system with four sites (S1, S2, S3, S4) and six processes (P1, P2, P3, P4, P5, P6). The coordinator site is S1. The arrows represent the wait-for relationships between the processes and the resources. The dashed circle indicates a deadlock involving P2, P3, P4, and P5.

```
+-----------------+       +-----------------+
|                 |       |                 |
|      S1        |       |      S2        |
|                 |       |                 |
| +-----+         |       | +-----+         |
| | P1  |         |       | | P2  |         |
| +-----+         |       | +-----+         |
|                 |       |                 |
|                 |       |                 |
|                 |       |                 |
|                 |       |                 |
|                 |       |                 |
|                 |       |                 |
+-----------------+       +-----------------+
    |  ^                    |  ^  |
    |  |                    |  |  |
    v  |                    v  |  |
+-----------------+       +-----------------+
|                 |       |                 |
|      S3        |       |      S4        |
|                 |       |                 |
| +-----+         |       | +-----+         |
| | P3  |         |       | | P4  |         |
| +-----+         |       | +-----+         |
|                 |       |                 |
|                 |       |                 |
|                 |       |                 |
| +-----+         |       | +-----+         |
| | P5  |         |       | | P6  |         |
| +-----+         |       | +-----+         |
|                 |       |                 |
+-----------------+       +-----------------+
    ^  |                    ^  |
    |  |                    |  |
    |  v                    |  v
+-----------------+       +-----------------+
|                 |       |                 |
|      S1        |       |      S2        |
|                 |       |                 |
|                 |       |                 |
|                 |       |                 |
|                 |       |                 |
|                 |       |                 |
|                 |       |                 |
|                 |       |                 |
|                 |       |                 |
|                 |       |                 |
+-----------------+       +-----------------+
    |  ^                    |  ^  |
    |  |                    |  |  |
    v  |                    v  |  |
+-----------------+       +-----------------+
|                 |       |                 |
|      S3        |       |      S4        |
|                 |       |                 |
|                 |       |                 |
|                 |       |                 |
|                 |       |                 |
|                 |       |                 |
|                 |       |                 |
|                 |       |                 |
|                 |       |                 |
|                 |       |                 |
+-----------------