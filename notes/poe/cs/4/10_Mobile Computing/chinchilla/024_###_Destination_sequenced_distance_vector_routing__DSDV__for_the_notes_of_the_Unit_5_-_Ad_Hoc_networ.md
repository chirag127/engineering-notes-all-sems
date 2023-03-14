### Destination Sequenced Distance Vector Routing (DSDV)

Destination Sequenced Distance Vector (DSDV) is a table-driven routing protocol that is used in mobile ad-hoc networks (MANETs). DSDV is a proactive routing protocol that maintains a routing table at each node in the network. The routing table is updated periodically or when there is a change in the network topology.

#### Working Principle

DSDV uses the Bellman-Ford algorithm to calculate the shortest path to a destination node. Each node in the network maintains a routing table that contains the next hop to reach a destination node and the distance to that node. The routing table also contains a sequence number that is used to identify the latest update of the routing information.

When a node wants to send a packet to a destination node, it looks up the destination node in its routing table and sends the packet to the next hop node. If there is no entry for the destination node in the routing table, the node broadcasts a request for the destination node's routing information.

#### Advantages

- DSDV is a loop-free routing protocol, which ensures that packets do not get stuck in a routing loop.
- DSDV provides quick convergence, as each node updates its routing table periodically or when there is a change in the network topology.
- DSDV is suitable for networks with low mobility, as it maintains a stable routing table.

#### Disadvantages

- DSDV requires a large amount of overhead traffic for updating routing information, which can lead to network congestion.
- DSDV may not be suitable for networks with high mobility, as frequent updates to the routing table may cause instability.

#### Mnemonics and Learning Tricks

- Remember that DSDV is a proactive routing protocol that maintains a routing table at each node in the network.
- Think of the sequence number in the routing table as a version number, which helps to identify the latest update of the routing information.
- Remember that DSDV uses the Bellman-Ford algorithm to calculate the shortest path to a destination node.

#### Example

Consider a network of four nodes, A, B, C, and D, as shown below.

```
   A----B
   |    | 
   C----D
```

Each node maintains a routing table that lists the next hop to reach a destination node and the distance to that node. For example, node A's routing table may look like this:

```
Destination | Next Hop | Distance | Sequence Number
------------|---------|----------|----------------
A           | -       | 0        | 1
B           | B       | 1        | 1
C           | C       | 1        | 1
D           | B       | 2        | 1
```

Node A's routing table shows that it can reach itself with a distance of 0, node B with a distance of 1 via node B, node C with a distance of 1 via node C, and node D with a distance of 2 via node B.

Suppose node A wants to send a packet to node D. Node A looks up node D in its routing table and finds that the next hop to reach node D is node B. Node A then sends the packet to node B.

If there is a change in the network topology, such as node B moving out of range of node A, node A's routing table will be updated accordingly. The updated routing table may look like this:

```
Destination | Next Hop | Distance | Sequence Number
------------|---------|----------|----------------
A           | -       | 0        | 2
B           | -       | infinity | 1
C           | C       | 1        | 2
D           | -       | infinity | 1
```

Node A's routing table now shows that it cannot reach nodes B and D, as their distances are infinity. Node A will broadcast a request for the routing information for nodes B and D. Once it receives the updated routing information, node A's routing table will be updated accordingly.