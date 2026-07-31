#### Spanning Tree Algorithms in Local Area Network

- Spanning tree algorithms are used to prevent loops in a bridged Ethernet local area network (LAN) by disabling some of the redundant links between switches .
- The basic idea of spanning tree algorithms is to construct a logical tree topology from the physical mesh topology of the LAN, such that there is only one path between any two nodes in the network .
- The spanning tree algorithms use a distributed protocol that runs on each switch in the LAN. The protocol involves exchanging messages called Bridge Protocol Data Units (BPDUs) to elect a root bridge, assign port roles, and detect topology changes  .
- The root bridge is the switch that has the lowest bridge ID, which is a combination of a priority value and a MAC address. The root bridge is the reference point for the spanning tree topology and sends periodic BPDUs to the rest of the switches  .
- The port roles are determined by the distance from the root bridge, measured in terms of path cost. The port roles are:

  - Root port: The port on a non-root bridge that has the lowest path cost to the root bridge. There is only one root port per bridge, and it is always in forwarding state  .
  - Designated port: The port on a segment that has the lowest path cost to the root bridge. There is only one designated port per segment, and it is always in forwarding state  .
  - Alternate port: The port on a non-root bridge that has an alternative path to the root bridge, with a higher path cost than the root port. It is in blocking state to prevent loops .
  - Backup port: The port on a bridge that has a redundant link to the same segment as the designated port. It is in blocking state to prevent loops .
  - Disabled port: The port that is administratively shut down or not part of the spanning tree instance. It is in disabled state and does not participate in the protocol .

- The topology changes are detected by the switches when they receive BPDUs with different information than their own, or when they stop receiving BPDUs on a port. The switches then update their port roles and states accordingly, and propagate the topology change notification to the rest of the network  .
- There are different versions and variants of spanning tree algorithms, such as:

  - Spanning Tree Protocol (STP): The original IEEE 802.1D standard, which has a slow convergence time and a single instance of spanning tree per LAN .
  - Rapid Spanning Tree Protocol (RSTP): The IEEE 802.1w standard, which improves the convergence time and introduces new port states and roles, such as discarding, learning, forwarding, edge, and point-to-point .
  - Multiple Spanning Tree Protocol (MSTP): The IEEE 802.1s standard, which allows multiple instances of spanning tree per LAN, each with a different VLAN configuration and root bridge .
  - Per-VLAN Spanning Tree Protocol (PVSTP): A Cisco proprietary protocol, which runs a separate instance of STP for each VLAN in the LAN .
  - Per-VLAN Rapid Spanning Tree Protocol (PVRSTP): A Cisco proprietary protocol, which runs a separate instance of RSTP for each VLAN in the LAN .

- The advantages of spanning tree algorithms are:

  - They provide loop-free and redundant operation for Ethernet LANs, which improves network reliability and performance  .
  - They are simple and easy to implement, as they do not require any configuration or routing protocols on the switches  .
  - They are flexible and adaptable, as they can adjust to any topology changes automatically and quickly  .

- The disadvantages of spanning tree algorithms are:

  - They waste bandwidth and resources, as they block some of the links