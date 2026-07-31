#### Spanning Tree Algorithms in Local Area Network

- Spanning Tree Protocol (STP) is a network protocol that builds a loop-free logical topology for Ethernet networks.
- The basic function of STP is to prevent bridge loops and the broadcast radiation that results from them.
- Spanning tree also allows a network design to include backup links providing fault tolerance if an active link fails.
- The spanning-tree algorithm blocks forwarding on redundant links by setting up one preferred link between switches in the LAN.
- This preferred link is used for all Ethernet frames unless it fails, in which case a non-preferred redundant link is enabled.
- When implemented in a network, STP designates one layer-2 switch as root bridge.
- The spanning tree algorithm allows to remove logical rings from the network physical topology, by disabling links to transform a mesh topology (graph) into a tree called spanning tree, whose root is one of the bridges called root bridge.