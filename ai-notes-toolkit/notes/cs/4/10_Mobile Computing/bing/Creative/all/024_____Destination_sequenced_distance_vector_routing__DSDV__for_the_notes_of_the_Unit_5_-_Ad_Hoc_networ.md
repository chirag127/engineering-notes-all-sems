# Destination sequenced distance vector routing (DSDV)

- Destination sequenced distance vector routing (DSDV) is a table-driven routing scheme for ad hoc mobile networks based on the Bellman–Ford algorithm.
- It was developed by C. Perkins and P. Bhagwat in 1994.
- The main contribution of the algorithm was to solve the routing loop problem.
- It adds a new attribute, sequence number, to each route table entry of the conventional Routing Information Protocol (RIP).
- Using the newly added sequence number, the mobile nodes can distinguish stale route information from the new and thus prevent the formation of routing loops.
- A limitation of DSDV is that it provides only one route for a source/destination pair.
- DSDV is also based on distance vector routing and thus uses bidirectional links.
- A node holds a routing table containing all the possible destinations within the network and the number of hops to each destination.
- A node periodically broadcasts its routing table to its neighbors.
- A node updates its routing table if it receives a new sequence number or a lower metric for an existing route.
- DSDV uses two types of packets for routing updates: full dump and incremental.
- A full dump packet contains all the routing table entries and is sent infrequently.
- An incremental packet contains only the updated entries and is sent more frequently.
- DSDV reduces the control overhead by using triggered updates and settling time.
- A triggered update is sent when a node detects a significant change in the network topology.
- A settling time is the time period during which a node waits for possible updates before broadcasting a new route.
- DSDV is suitable for small and moderately sized networks with low mobility.
- DSDV is not scalable for large networks with high mobility due to frequent updates and large routing tables.