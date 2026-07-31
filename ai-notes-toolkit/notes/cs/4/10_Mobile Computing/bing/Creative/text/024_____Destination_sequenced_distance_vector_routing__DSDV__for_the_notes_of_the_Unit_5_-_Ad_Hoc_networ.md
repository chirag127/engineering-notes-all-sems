### Destination sequenced distance vector routing (DSDV)

- DSDV is a table-driven routing protocol for ad hoc mobile networks based on the Bellman–Ford algorithm.
- DSDV adds a new attribute, sequence number, to each route table entry of the conventional RIP.
- The sequence number is used to distinguish stale route information from the new and thus prevent the formation of routing loops.
- Each node maintains a routing table that contains the following information for each destination: the next hop, the number of hops, the sequence number, and the installation time.
- Each node periodically broadcasts its routing table to its neighbors, and updates its own table based on the received information.
- If a node detects a link break, it increments the sequence number of the destination and advertises the metric as infinity.
- DSDV provides only one route for a source/destination pair, and does not support multipath routing.
- DSDV reduces the control overhead and latency compared to the classical Bellman-Ford algorithm, but still suffers from frequent updates and wasted bandwidth.