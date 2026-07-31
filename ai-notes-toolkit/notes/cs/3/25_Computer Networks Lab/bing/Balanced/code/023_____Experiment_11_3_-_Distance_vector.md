### Experiment 11.3 - Distance vector

- Distance vector is a routing algorithm that calculates the best route for a packet based on the distance or hop count to the destination.
- Distance vector routers exchange their routing tables periodically with their neighbors to update their knowledge of the network topology.
- Distance vector routers use the Bellman-Ford algorithm to compute the shortest path to each destination based on the information received from their neighbors.
- Distance vector routers suffer from two major problems: slow convergence and count-to-infinity.
- Slow convergence means that it takes a long time for the routers to reach a consistent view of the network after a change in the topology, such as a link failure or a new link addition.
- Count-to-infinity means that the routers may increment the distance to a destination indefinitely in the presence of a loop in the network, making the destination unreachable.
- Distance vector routers can use some techniques to overcome these problems, such as split horizon, poison reverse, triggered updates, and hold-down timers.