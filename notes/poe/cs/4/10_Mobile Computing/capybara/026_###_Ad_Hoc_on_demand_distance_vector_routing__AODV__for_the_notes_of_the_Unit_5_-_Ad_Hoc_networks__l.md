### Ad Hoc on Demand Distance Vector Routing (AODV)

Ad Hoc on Demand Distance Vector Routing (AODV) is a reactive routing protocol that is used in mobile ad-hoc networks (MANETs). AODV is designed to operate efficiently in dynamic and self-organizing networks. It is a distance-vector routing protocol that uses hop count as the metric for path selection.

#### How AODV Works

AODV is a reactive routing protocol, which means that routes are only discovered when they are needed. When a node wants to send a packet to a destination for which there is no existing route, it broadcasts a Route Request (RREQ) packet. The RREQ packet is flooded throughout the network until it reaches the destination or a node that has a fresh enough route to the destination. When the RREQ packet reaches either the destination or a node with a fresh enough route, a Route Reply (RREP) packet is sent back to the source node. The source node then caches the route and uses it to send the packet.

AODV also includes a mechanism for handling broken links or routes. When a node detects a broken link or route, it sends a Route Error (RERR) packet to the nodes that are affected. The affected nodes then update their routing tables accordingly.

#### Advantages of AODV

- Efficient use of network resources: AODV only discovers routes when they are needed, which reduces the overhead on the network.

- Rapid adaptation to changes in network topology: AODV is designed to work in dynamic and self-organizing networks, which makes it well-suited for mobile ad-hoc networks.

- Scalability: AODV is scalable to large networks, as it uses hop count as the metric for path selection.

#### Disadvantages of AODV

- Delay in discovering routes: AODV has a delay in discovering routes, as the RREQ packet must be flooded throughout the network.

- Overhead on the network: Although AODV is efficient in its use of network resources, the flooding of RREQ packets can still create overhead on the network.

#### Learning Tricks and Mnemonics

There are no widely accepted mnemonic devices or learning tricks for AODV. However, some students have found it helpful to remember that AODV is a reactive routing protocol, which means that routes are only discovered when they are needed. Additionally, it may be helpful to remember that AODV uses hop count as the metric for path selection.