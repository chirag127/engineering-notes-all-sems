Spanning tree algorithms are used to prevent loops in a local area network (LAN) that has redundant links between switches. They work by selecting one switch as the root bridge and then blocking or disabling some of the links that are not part of the shortest path to the root bridge. This way, a loop-free logical topology is created for the LAN.

The following diagram illustrates the basic architecture of a spanning tree algorithm in a LAN:

```
    +--------+         +--------+         +--------+
    | Switch |---------| Switch |---------| Switch |
    |   A    |         |   B    |         |   C    |
    +--------+         +--------+         +--------+
       |  |              |  |              |  |
       |  |              |  |              |  |
       |  +--------------+  +--------------+  |
       |                    |                 |
       |                    |                 |
       |                    |                 |
    +--------+         +--------+         +--------+
    | Switch |---------| Switch |---------| Switch |
    |   D    |         |   E    |         |   F    |
    +--------+         +--------+         +--------+
```

In this diagram, there are six switches (A, B, C, D, E, F) connected by nine links. If all the links are active, there will be loops in the network, which can cause problems such as broadcast storms, multiple frame copies, and inconsistent MAC address tables. To avoid these problems, a spanning tree algorithm is run on the switches to select a root bridge and block some of the links.

One example of a spanning tree algorithm is the Spanning Tree Protocol (STP), which is based on the following steps:

1. Each switch sends out Bridge Protocol Data Units (BPDUs) to announce its identity and priority to the other switches.
2. The switch with the lowest priority (or the lowest MAC address if there is a tie) becomes the root bridge. In this example, let's assume that switch A is the root bridge.
3. Each switch determines the shortest path to the root bridge based on the cost of the links. The cost is usually proportional to the bandwidth of the link, with lower cost for higher bandwidth.
4. Each switch selects one of its ports as the root port, which is the port that connects to the shortest path to the root bridge. For example, switch B selects the port that connects to switch A as its root port.
5. Each switch also selects one of its ports as the designated port for each LAN segment, which is the port that offers the lowest cost path to the root bridge for that segment. For example, switch B selects the port that connects to switch C as the designated port for the segment between B and C.
6. All the ports that are neither root ports nor designated ports are blocked or disabled, which means they do not forward any traffic. For example, switch B blocks the port that connects to switch E.

The result of the STP algorithm is a spanning tree that covers all the switches in the LAN, as shown in the diagram below. The blocked ports are marked with X.

```
    +--------+         +--------+         +--------+
    | Switch |---------| Switch |---------| Switch |
    |   A    |         |   B    |         |   C    |
    +--------+         +--------+         +--------+
       |  |              |  |              |  |
       |  |              |  |              |  |
       |  +--------------+  +--------------+  |
       |  X                  X              X |
       |                    |                 |
       |                    |                 |
       |                    |                 |
    +--------+         +--------+         +--------+
    | Switch |---------| Switch |---------| Switch |
    |   D    |         |   E    |         |   F    |
    +--------+         +--------+         +--------+
```

The spanning tree provides a loop-free and redundant topology for the LAN. If any of the active links fails, the STP algorithm can detect the failure and unblock one of the blocked ports to restore connectivity. For example, if the link between switch A and switch B fails, switch B can unblock the port that connects to switch E and use it as the new root port. This way, the network can recover from link failures without manual intervention.