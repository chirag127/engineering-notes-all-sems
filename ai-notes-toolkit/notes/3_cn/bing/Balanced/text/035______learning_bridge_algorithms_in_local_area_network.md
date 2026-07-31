#### Learning bridge algorithms in local area network

- A bridge is a device that connects two or more local area networks (LANs) and forwards data frames between them based on their MAC addresses.
- A bridge algorithm is a set of rules that determines how a bridge learns the MAC addresses of the devices connected to the LANs and how it decides which frames to forward or filter.
- There are different types of bridge algorithms, such as transparent bridging, source routing bridging, and spanning tree protocol.
- Transparent bridging is the most common type of bridge algorithm. It uses two main functions: learning and filtering/forwarding.
  - Learning: The bridge maintains a table that maps each MAC address to the port where it was last seen. Whenever the bridge receives a frame, it updates the table with the source MAC address and the port number.
  - Filtering/forwarding: The bridge checks the destination MAC address of each frame against the table. If the destination MAC address is found in the table and the port number matches the incoming port, the bridge filters (discards) the frame. If the destination MAC address is not found in the table or the port number does not match the incoming port, the bridge forwards the frame to all other ports (flooding).
- Source routing bridging is another type of bridge algorithm that is used in token ring networks. It relies on the source device to specify the path of the frame through the network using a routing information field (RIF) in the frame header.
  - The RIF contains a list of bridge numbers and ring numbers that the frame must traverse to reach the destination.
  - The bridge checks the RIF and forwards the frame to the appropriate port based on the next bridge number and ring number in the list.
  - The bridge also updates the RIF with its own bridge number and ring number as the frame passes through it.
- Spanning tree protocol (STP) is a bridge algorithm that prevents loops in a network with multiple bridges. It creates a logical tree structure of the network by selecting a root bridge and designating ports as either root ports, designated ports, or blocked ports.
  - Root bridge: The bridge with the lowest bridge ID (a combination of priority and MAC address) in the network. It is the root of the spanning tree.
  - Root port: The port on each non-root bridge that has the lowest cost path to the root bridge. It is used to forward frames to and from the root bridge.
  - Designated port: The port on each LAN segment that has the lowest cost path to the root bridge. It is used to forward frames to and from the LAN segment.
  - Blocked port: The port on each bridge that is neither a root port nor a designated port. It is not used to forward frames and is in a listening state.
  - The bridge algorithm uses a protocol called bridge protocol data units (BPDUs) to exchange information about the bridge IDs, port costs, and port states among the bridges and to elect the root bridge and the designated ports.