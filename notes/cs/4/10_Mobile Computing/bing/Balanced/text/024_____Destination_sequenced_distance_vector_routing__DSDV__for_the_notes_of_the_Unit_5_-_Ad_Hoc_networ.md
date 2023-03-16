### Destination sequenced distance vector routing (DSDV)

- DSDV is a table-driven routing protocol for ad hoc mobile networks based on the Bellman–Ford algorithm.
- DSDV adds a new attribute, sequence number, to each route table entry of the conventional RIP.
- The sequence number is used to distinguish stale route information from the new and thus prevent the formation of routing loops.
- Each node maintains a routing table that contains the following information for each destination: the next hop, the number of hops, the sequence number, and the installation time.
- The sequence number is originated and incremented by the destination node whenever it updates its route information.
- Each node periodically broadcasts its routing table to its neighbors, and also sends triggered updates when it detects any significant change in the topology.
- The nodes update their routing tables based on the received information, using the following rules:
  - If the received sequence number is greater than the stored one, the node updates the route with the new information.
  - If the received sequence number is equal to the stored one, the node compares the number of hops and chooses the route with the smaller hop count.
  - If the received sequence number is smaller than the stored one, the node discards the received information.
- DSDV provides only one route for a source/destination pair, and thus does not support multipath routing.
- DSDV reduces the control overhead and latency of the classical Bellman-Ford algorithm, but still suffers from frequent updates and wasted bandwidth.