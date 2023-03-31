
### Destination Sequenced Distance Vector Routing (DSDV)

* DSDV is a routing protocol for mobile ad hoc networks (MANETs) that uses the Bellman-Ford algorithm to create a routing table. 
* It is based on a distance-vector algorithm, which means that each node in the network maintains a vector of the distances to each other node in the network, and updates its neighbors with changes in the vector. 
* DSDV is an improvement over the original distance-vector algorithm, as it includes a sequence number in each route entry, which helps to avoid routing loops. 
* The sequence numbers are used to distinguish between stale and new routes, and the routing table is updated periodically to ensure that the most recent information is available. 
* DSDV provides loop-free routing, but the update process can be slow and the overhead can be high, especially in large networks. 
* DSDV is suitable for networks where the topology changes frequently, such as in mobile ad hoc networks.