### Destination sequenced distance vector routing (DSDV)

- Destination sequenced distance vector routing (DSDV) is a table-driven routing scheme for ad hoc mobile networks based on the Bellman–Ford algorithm.
- It was developed by C. Perkins and P. Bhagwat in 1994.
- The main contribution of the algorithm was to solve the routing loop problem.
- It adds a new attribute, sequence number, to each route table entry of the conventional Routing Information Protocol (RIP).
- Using the newly added sequence number, the mobile nodes can distinguish stale route information from the new and thus prevent the formation of routing loops.
- A limitation of DSDV is that it provides only one route for a source/destination pair.
- DSDV is also based on distance vector routing and thus uses bidirectional links.
- DSDV requires each node to periodically broadcast routing updates.
- This is a table driven algorithm based on modifications made to the Bellman-Ford routing mechanism.