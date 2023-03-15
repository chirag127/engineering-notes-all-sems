# Experiment 11.3 - Distance vector

- Distance vector is a routing protocol that calculates the best route for a packet based on the distance and direction to the destination.
- Distance vector routers exchange information about their routing tables with their neighbors periodically or when there is a change in the network topology.
- Distance vector routers use the Bellman-Ford algorithm to update their routing tables and find the shortest path to the destination.
- Distance vector routers have the following characteristics:
  - They only know the distance and direction to the destination, not the entire path.
  - They use hop count as the metric to measure the distance to the destination.
  - They are prone to routing loops, count-to-infinity problems, and slow convergence.
  - They use split horizon, poison reverse, and triggered updates to prevent or mitigate these problems.
  - They are simple, easy to implement, and suitable for small networks with low traffic and stable topology.
- Distance vector routers perform the following steps to update their routing tables:
  1. Initialize the routing table with the directly connected networks and assign a hop count of zero to them.
  2. Send the routing table to all the neighboring routers and receive their routing tables.
  3. For each destination in the received routing table, compare the hop count with the existing hop count in the local routing table.
  4. If the received hop count is smaller than the existing hop count, update the local routing table with the new hop count and the next hop router.
  5. If the received hop count is equal to the existing hop count, check if the next hop router is different. If yes, add the alternative route to the local routing table.
  6. If the received hop count is larger than the existing hop count, ignore the update.
  7. Repeat steps 2 to 6 until no more updates are received or the routing table stabilizes.