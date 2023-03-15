### Learning bridge and spanning tree algorithms for the notes of the Unit 4 - Medium Access Control and Local Area Networks in the subject of Computer Networks

- A bridge is a device that connects two or more LAN segments and forwards frames between them based on the MAC addresses of the destination and source hosts.
- A bridge operates at the data link layer of the OSI model and can filter, forward, or flood frames depending on the destination MAC address and the bridge's forwarding table.
- A bridge can also learn the MAC addresses of the hosts connected to its ports by observing the source MAC address of the incoming frames and updating its forwarding table accordingly.
- A bridge can create a loop-free logical topology for a network of LAN segments by running the spanning tree protocol (STP).
- The spanning tree protocol is a network protocol that builds a loop-free logical topology for Ethernet networks by disabling some of the redundant links between the bridges.
- The basic function of STP is to prevent bridge loops and the broadcast radiation that results from them.
- Spanning tree also allows a network design to include backup links providing fault tolerance if an active link fails.
- The bridges that participate in spanning tree protocol are often called spanning tree bridges.
- To construct a spanning tree, the bridges run a distributed algorithm that uses bridge protocol data units (BPDUs) as the messages.
- BPDUs are data messages that provide the bridges with network information that's used to carry out STP operations.
- The spanning tree algorithm, which was developed by Radia Perlman at the Digital Equipment Corporation, is based on the following steps:

  - Each bridge assigns itself a unique bridge ID, which is a combination of a priority value and a MAC address.
  - Each bridge broadcasts a configuration message (a type of BPDU) out all of its ports to its neighbors, containing its bridge ID and the cost of the path to the root bridge (initially itself).
  - Each bridge compares the received configuration messages with its own and updates its information if it finds a better path to the root bridge (a bridge with a lower bridge ID or a lower path cost).
  - Each bridge also elects a designated bridge for each LAN segment, which is the bridge that has the lowest path cost to the root bridge on that segment.
  - Each bridge also elects a root port, which is the port that connects to the designated bridge on the LAN segment that has the lowest path cost to the root bridge.
  - Each bridge disables all its ports that are not root ports or designated ports, creating a loop-free spanning tree.
  - The root bridge periodically sends out configuration messages to maintain the spanning tree, and the other bridges forward them along the tree.
  - If a link fails or a new bridge is added, the spanning tree algorithm is run again to reconfigure the spanning tree.

- The spanning tree algorithm is dynamic, so if an outage occurs then the spanning tree is recomputed.
- If the outage should partition the network into two pieces, both pieces will build spanning trees.
- The IEEE 802.1 specification for LAN bridges is based on the spanning tree algorithm.