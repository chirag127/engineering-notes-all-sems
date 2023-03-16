Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is some information on destination sequenced distance vector routing (DSDV) for the notes of the Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing.

### Destination sequenced distance vector routing (DSDV)

- DSDV is a table-driven routing scheme for ad hoc mobile networks based on the Bellman–Ford algorithm.
- It was developed by C. Perkins and P. Bhagwat in 1994.
- The main contribution of the algorithm was to solve the routing loop problem.
- It adds a new attribute, sequence number, to each route table entry of the conventional RIP.
- Using the newly added sequence number, the mobile nodes can distinguish stale route information from the new and thus prevent the formation of routing loops.
- DSDV is based on the Routing Information Protocol (RIP), which is a distance vector routing protocol that uses hop count as the metric.
- DSDV is also based on distance vector routing and thus uses bidirectional links.
- A limitation of DSDV is that it provides only one route for a source/destination pair.
- DSDV requires each node to periodically broadcast routing updates, which consumes bandwidth and battery power.
- DSDV can be classified into two types: full dump and incremental.
- Full dump is when a node sends its entire routing table to its neighbors, which is done when there are significant changes in the network topology.
- Incremental is when a node sends only the updated entries in its routing table, which is done when there are minor changes in the network topology.
- DSDV uses two types of packets: route advertisement packets and route request packets.
- Route advertisement packets are used to broadcast routing updates to the neighbors.
- Route request packets are used to request a route to a destination when a node does not have a valid route in its routing table.
- DSDV uses two techniques to reduce the routing overhead: triggered updates and settling time.
- Triggered updates are when a node sends a routing update immediately after detecting a change in the network topology, instead of waiting for the periodic update interval.
- Settling time is the time period during which a node waits before propagating a routing update, in order to avoid sending inconsistent or transient updates.
- DSDV has some advantages and disadvantages over other routing protocols for ad hoc networks.
- Advantages:
  - It guarantees loop-free routes.
  - It supports both unicast and multicast routing.
  - It is simple and easy to implement.
- Disadvantages:
  - It suffers from frequent route updates, which consume bandwidth and battery power.
  - It does not support multipath routing, which can improve load balancing and fault tolerance.
  - It does not adapt well to highly dynamic network topologies, where nodes move frequently and rapidly.