### Learning Bridge and Spanning Tree Algorithms for the Notes of Unit 4 - Medium Access Control and Local Area Networks in the Subject of Computer Networks

When it comes to Local Area Networks (LANs), one of the most important aspects is the efficient use of network resources. This is where the concept of Medium Access Control (MAC) comes into play, which deals with the way multiple devices contend for access to the same communication medium. In this unit, we will focus on Learning Bridges and Spanning Tree Algorithms, two key techniques used in MAC that ensure efficient network operation and prevent network loops.

#### Learning Bridges

- Learning Bridges are devices that operate in the Data Link Layer (Layer 2) of the OSI model and are used to connect two or more LAN segments.
- They learn the MAC addresses of devices connected to each segment by monitoring the source addresses of incoming frames and building a forwarding table that maps MAC addresses to the port on which they were received.
- Learning Bridges use this forwarding table to forward frames only to the segments where the destination MAC address is located, thereby reducing unnecessary traffic on the network.
- If a frame with a destination MAC address not in the forwarding table is received, the bridge forwards the frame to all connected segments, a process known as flooding.

#### Spanning Tree Algorithms

- Spanning Tree Algorithms are used to prevent network loops that can occur when multiple paths exist between two switches or bridges in a network.
- These algorithms create a logical tree structure that spans the network, allowing for the selection of the shortest path between any two devices.
- The algorithm works by selecting a root bridge, the bridge with the lowest Bridge ID, and disabling all other paths to that bridge except for the shortest path.
- If a link in the network fails, the algorithm recalculates the shortest path and adjusts the forwarding table of each bridge accordingly.
- This process ensures that there is only one active path between any two switches or bridges, preventing loops and ensuring efficient network operation.

Overall, Learning Bridges and Spanning Tree Algorithms are critical techniques for efficient network operation and preventing network loops in LANs. By understanding these concepts, network administrators can ensure that their networks are operating efficiently and reliably.