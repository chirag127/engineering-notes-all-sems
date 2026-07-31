### Destination sequenced distance vector routing (DSDV)

- Destination sequenced distance vector routing (DSDV) is a table-driven routing scheme for ad hoc mobile networks based on the Bellman–Ford algorithm.
- It was developed by C. Perkins and P. Bhagwat in 1994.
- The main contribution of the algorithm was to solve the routing loop problem.
- DSDV is adapted from the conventional Routing Information Protocol (RIP) to ad hoc networks routing.
- It adds a new attribute, sequence number, to each route table entry of the conventional RIP.
- Using the newly added sequence number, the mobile nodes can distinguish stale route information from the new and thus prevent the formation of routing loops.
- Each entry in the routing table contains a sequence number.
- DSDV routing protocol is a pro-active, table-driven routing protocol for MANETs.
- It uses the hop count as metric in route selection.
