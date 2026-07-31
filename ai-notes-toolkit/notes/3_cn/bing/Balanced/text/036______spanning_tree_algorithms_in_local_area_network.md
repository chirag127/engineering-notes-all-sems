#### Spanning Tree Algorithms in Local Area Network

- Spanning tree algorithms are used to prevent loops in a network topology that uses bridges or switches to connect multiple segments of a local area network (LAN).
- Loops can cause problems such as broadcast storms, multiple frame transmission, and MAC address table instability.
- Spanning tree algorithms work by creating a logical tree structure of the network, where only one path exists between any two nodes. This is done by blocking some of the links that create loops, while keeping others as backup links in case of link failure.
- The most common spanning tree algorithm is the Spanning Tree Protocol (STP), which is standardized by IEEE 802.1D. STP operates as follows :
  - STP elects one switch as the root bridge, which is the central point of the spanning tree. The root bridge is chosen based on the lowest bridge ID, which is a combination of a priority value and a MAC address.
  - STP assigns a cost to each link based on the bandwidth of the link. The lower the bandwidth, the higher the cost.
  - STP calculates the shortest path from each switch to the root bridge, based on the sum of the link costs. This path is called the root port for each switch.
  - STP determines the best link to forward traffic between switches on the same segment, based on the lowest port ID, which is a combination of a priority value and a port number. This link is called the designated port for each segment.
  - STP blocks all other links that are not root ports or designated ports. These links are called non-designated ports or alternate ports.
  - STP periodically sends special frames called Bridge Protocol Data Units (BPDUs) to exchange information about the network topology and detect changes. BPDUs are sent from the root bridge to all other switches, and from each designated port to its segment.
  - STP adapts to changes in the network topology by recalculating the spanning tree and unblocking or blocking ports as needed. This process is called convergence and may take several seconds to complete.