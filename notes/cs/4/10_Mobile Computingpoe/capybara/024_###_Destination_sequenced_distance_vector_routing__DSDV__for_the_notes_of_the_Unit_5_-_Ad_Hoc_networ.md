### Destination Sequenced Distance Vector Routing (DSDV)

DSDV is a proactive routing protocol for wireless ad hoc networks. It is based on the classical Bellman-Ford algorithm with some enhancements to provide loop-free paths and quick convergence. 

#### How does it work?

- Each node maintains a routing table that contains the destination addresses, the next hop, the number of hops to reach the destination, and the sequence number of the last update received for that destination.
- The sequence number is used to differentiate between old and new updates. If a new update is received with a higher sequence number, the routing table is updated with the new information. If the sequence numbers are the same, the update is ignored.
- Each node periodically broadcasts its routing table to its neighbors. The broadcast is done using a special packet called a "beacon".
- When a node receives a beacon from a neighbor, it updates its routing table with the information from the beacon if it is newer than the information it already has.
- If a node does not receive a beacon from a neighbor for a certain period of time, it assumes that the neighbor is no longer reachable and marks the corresponding entries in its routing table as invalid.

#### Advantages of DSDV

- Provides loop-free paths and quick convergence.
- Suitable for networks with low mobility and a small number of nodes.
- Works well in networks with a high degree of connectivity.

#### Disadvantages of DSDV

- Requires a lot of overhead due to the periodic broadcasts of the routing table.
- Not suitable for networks with high mobility and a large number of nodes.

#### Example

Consider a network with three nodes A, B, and C. The initial routing table for each node is as follows:

| Destination | Next Hop | Hops | Sequence |
| --- | --- | --- | --- |
| A | - | Infinity | 0 |
| B | - | Infinity | 0 |
| C | - | Infinity | 0 |

Assume that node A wants to send a packet to node B. The following steps occur:

1. Node A checks its routing table and finds that it does not have a valid route to node B.
2. Node A broadcasts a beacon containing its routing table to its neighbors B and C.
3. Nodes B and C receive the beacon and update their routing tables with the information from the beacon.
4. Node B finds a route to node A through node C with a distance of 2 hops and updates its routing table accordingly.
5. Node B sends a reply packet to node A through node C.
6. Node A updates its routing table with the new information received from node B.
7. Node A sends the original packet to node B through node C using the updated routing table.

#### Applications

DSDV is used in wireless ad hoc networks where the nodes are stationary or have low mobility. It is suitable for environments where the network topology is relatively stable and the number of nodes is small. DSDV is commonly used in military, emergency, and disaster recovery applications.