 Here is the content in markdown format for the topic ### Destination sequenced distance vector routing (DSDV) for the notes of the Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing:

### Destination sequenced distance vector routing (DSDV)

DSDV is a proactive routing protocol for ad hoc networks. It is based on the distance vector routing algorithm. Each node maintains a routing table that contains the distance and sequence number of the destinations. The sequence number is used to determine the freshness of the routes and avoid the count to infinity problem.

The steps involved in DSDV are:

1. Each node initializes its routing table with distances to all destinations as infinite except for itself which is 0. Sequence number is also initialized to 0.
2. Each node broadcasts its routing table to neighboring nodes periodically.
3. On receiving routing updates from neighbors, each node compares the sequence number to check the freshness of the route. The route with the higher sequence number is updated in the routing table. In case of a tie, the route with the smaller hop count is selected.
4. The node then increments its own sequence number, updates the distances from its neighbors and broadcasts the updated routing table.

Advantages:

- Simple to implement.
- Avoid count to infinity problem using sequence numbers.

Disadvantages:

- High overhead due to periodic broadcasting of routing tables.
- Slow convergence.
- Does not scale well for large and dense networks.

Applications:

- Small wireless ad hoc networks where bandwidth is not a major constraint.

Hope this helps! Let me know if you would like me to explain anything in more detail.