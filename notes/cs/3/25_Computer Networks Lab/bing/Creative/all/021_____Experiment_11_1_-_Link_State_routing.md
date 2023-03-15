# Experiment 11.1 - Link State routing

- Link state routing is a type of routing algorithm that computes the shortest path between a source and a destination in a network.
- Link state routing requires each router to maintain a complete and consistent view of the network topology, called the link state database (LSDB).
- Link state routing uses a distributed algorithm called the link state update protocol to exchange link state information among routers and to keep the LSDBs synchronized.
- Link state routing uses a local algorithm called the shortest path first (SPF) algorithm to calculate the shortest path tree for each router based on the LSDB.
- Link state routing has several advantages over distance vector routing, such as faster convergence, loop-free routing, and support for hierarchical routing.
- Link state routing also has some disadvantages, such as higher memory and CPU requirements, more bandwidth consumption, and vulnerability to link state flooding attacks.