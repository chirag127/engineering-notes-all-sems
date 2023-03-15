### Experiment 11.3 - Distance Vector

Distance vector routing is a type of routing protocol used in computer networks to determine the best path for data packets to travel from one node to another. It is based on the Bellman-Ford algorithm and is used in routing protocols such as RIP (Routing Information Protocol) and IGRP (Interior Gateway Routing Protocol).

In distance vector routing, each router maintains a routing table that contains the distance (or cost) to reach each destination network and the next hop router to reach that destination. The distance is measured in terms of a metric, such as hop count or delay.

Routers exchange their routing tables with their directly connected neighbors at regular intervals. When a router receives a routing table from a neighbor, it updates its own routing table by comparing the distances to each destination in the received table with the distances in its own table. If the received distance to a destination is shorter than the distance in its own table, the router updates its routing table with the new distance and next hop information.

Distance vector routing has some limitations, such as the count-to-infinity problem, where the convergence time can be slow in the case of a network failure. This can be mitigated by using techniques such as split horizon and poison reverse.

In summary, distance vector routing is a simple and widely used routing protocol that determines the best path for data packets based on the distance to the destination. It has some limitations, but these can be mitigated by using additional techniques.