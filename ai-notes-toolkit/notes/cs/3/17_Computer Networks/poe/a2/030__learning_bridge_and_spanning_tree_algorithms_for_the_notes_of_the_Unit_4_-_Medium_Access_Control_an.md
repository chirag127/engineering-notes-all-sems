 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Learning Bridge and Spanning Tree Algorithms

For the notes of Unit 4 - Medium Access Control and Local Area Networks in Computer Networks

- Bridges connect two network segments and forwards traffic between them. They operate at the data link layer.
- Bridges learn which MAC addresses are present on which side of the bridge and forward traffic accordingly. This is known as transparent bridging.
- In networks with multiple bridges, loops can occur leading to broadcast storms. Spanning tree algorithm is used to detect and remove loops.
- Spanning tree algorithm:
-- Bridges detect loops in the network.
-- One bridge is elected as the root bridge.
-- Each bridge assigns a cost to the port based on port speed with the root bridge as reference.
-- Each bridge selects the path with the lowest total cost to reach the root bridge and blocks the other ports to avoid loops.
-- The elected paths form a tree topology with the root bridge at the root.
-- The algorithm reconfigures the network in case of changes to handle faults.
- This creates an active topology that allows for most efficient forwarding of traffic. The blocked ports can be used in case of faults.
- Rapid Spanning Tree Protocol (RSTP) and Multiple Spanning Tree Protocol (MSTP) are enhancements of the spanning tree algorithm to be more efficient.

The above content summarizes the key points around bridges, transparent bridging and spanning tree algorithm to remove loops in a formal tone as requested. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.