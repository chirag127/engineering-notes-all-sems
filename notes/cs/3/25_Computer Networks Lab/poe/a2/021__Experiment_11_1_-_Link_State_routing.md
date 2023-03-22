 Here is the content in markdown format with all the given instructions:

### Experiment 11.1 - Link State routing

1. Link state routing is a routing algorithm used in packet-switched networks. Each router builds a map of the network and determines the best path for data packets to travel from the source to the destination based on the available bandwidth, delay, load, and other factors.
2. In link state routing, each router shares the information about the state of its directly connected links with other routers in the network. Each router then builds a map of the entire network topology based on the received information. Using this topology map, each router calculates the shortest path to every other router in the network using a shortest path algorithm.
3. The steps involved in the link state routing algorithm are:

a) Each router discovers its neighbors and determines the cost of its links to each neighbor.
b) Each router then floods the network with link state advertisements containing information about its directly connected links and their costs.
c) Each router receives the link state advertisements from all other routers and builds a map of the topology of the entire network.
d) Using the topology map, each router runs a shortest path algorithm to determine the lowest cost path to each other router in the network.
e) The routing tables are then updated with the shortest path to each destination.

4. The advantages of link state routing are:

a) Fast convergence - The topology database is updated quickly as any change in the network is propagated to all routers simultaneously. This results in fast recalculation and convergence of routes.
b) Uses of the entire topology information - Each router has a global view of the network topology allowing the optimal path to be calculated.
c) Scalable - Link state routing is scalable and can be used in large and complex networks. The Shortest Path First (SPF) algorithm used to calculate routes is efficient and can handle a large amount of topology information.