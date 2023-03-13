Destination sequenced distance vector routing (DSDV) is a table-driven routing protocol for ad hoc networks that is based on the Bellman-Ford algorithm. It uses sequence numbers to avoid routing loops and to ensure the freshness of routes. Each node maintains a routing table that contains the following information for each destination: the next hop, the number of hops, the sequence number, and a flag to indicate if the route is valid or not. Each node periodically broadcasts its routing table to its neighbors, and updates its own table based on the received information. If a node detects a link break, it increments the sequence number of the affected destination and advertises the route with an infinite metric.

The following diagram illustrates the basic architecture of a DSDV network:

```
+-----+     +-----+     +-----+     +-----+
|  A  |-----|  B  |-----|  C  |-----|  D  |
+-----+     +-----+     +-----+     +-----+
  |           |           |           |
  |           |           |           |
  |           |           |           |
  |           |           |           |
  |           |           |           |
  |           |           |           |
+-----+     +-----+     +-----+     +-----+
|  E  |-----|  F  |-----|  G  |-----|  H  |
+-----+     +-----+     +-----+     +-----+
```

Each node has a routing table that contains the following entries:

| Destination | Next Hop | Hops | Sequence Number | Flag |
|-------------|----------|------|-----------------|------|
| A           | A        | 0    | 2               | V    |
| B           | B        | 1    | 4               | V    |
| C           | B        | 2    | 6               | V    |
| D           | B        | 3    | 8               | V    |
| E           | E        | 1    | 10              | V    |
| F           | E        | 2    | 12              | V    |
| G           | E        | 3    | 14              | V    |
| H           | E        | 4    | 16              | V    |

The sequence numbers are even for valid routes and odd for invalid routes. The flag is V for valid and I for invalid. The hops are the number of intermediate nodes between the source and the destination. The next hop is the node that is directly connected to the source and is on the shortest path to the destination.