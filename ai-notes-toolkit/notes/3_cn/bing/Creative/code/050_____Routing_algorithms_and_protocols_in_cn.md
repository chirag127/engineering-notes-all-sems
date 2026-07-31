### Routing algorithms and protocols in computer networks

Routing algorithms and protocols are the methods used by the network layer to determine the best path for sending data packets from a source to a destination in a computer network. Routing algorithms use various metrics, such as distance, bandwidth, or latency, to find the optimal path for data transmission. Routing protocols are the software implementations of routing algorithms that exchange routing information and update routing tables.

There are three major classes of routing protocols in IP networks:

- **Interior gateway protocols (IGPs)**: These are the protocols used within a single autonomous system (AS), which is a group of routers under the same administrative control. IGPs can be further divided into two types:

  - **Link-state routing protocols**: These protocols maintain a complete map of the network topology and calculate the shortest path to each destination using an algorithm such as Dijkstra's or Bellman-Ford. Examples of link-state routing protocols are Open Shortest Path First (OSPF) and Intermediate System to Intermediate System (IS-IS).
  - **Distance-vector routing protocols**: These protocols only keep track of the distance and direction to each destination and exchange routing updates with their neighbors periodically. Examples of distance-vector routing protocols are Routing Information Protocol (RIP), Enhanced Interior Gateway Routing Protocol (EIGRP), and Border Gateway Protocol (BGP).

- **Exterior gateway protocols (EGPs)**: These are the protocols used between different autonomous systems to exchange routing information and establish inter-domain routes. The most common EGP is Border Gateway Protocol (BGP), which is used to connect different networks on the Internet.
- **Hybrid routing protocols**: These are the protocols that combine the features of both link-state and distance-vector routing protocols to achieve better scalability and performance. Examples of hybrid routing protocols are Enhanced Interior Gateway Routing Protocol (EIGRP) and Cisco's Interior Gateway Routing Protocol (IGRP).

The following is a pseudocode example of a distance-vector routing algorithm:

```
# Initialize the routing table with the direct neighbors and their distances
for each neighbor n in the network
  routing_table[n] = distance(n)

# Repeat the following steps until no more updates are received
while true
  # Send the routing table to all neighbors
  for each neighbor n in the network
    send(routing_table, n)

  # Receive the routing tables from all neighbors
  for each neighbor n in the network
    receive(routing_table_n, n)

    # Update the routing table based on the received information
    for each destination d in routing_table_n
      # If the destination is not in the routing table or the new distance is smaller
      if d not in routing_table or routing_table_n[d] + distance(n) < routing_table[d]
        # Update the distance and the next hop
        routing_table[d] = routing_table_n[d] + distance(n)
        next_hop[d] = n
```