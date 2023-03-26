 Here is the content in markdown format without any emojis or external links, written in points and in a formal tone:

### Survey routing protocols for the notes of the Unit 4 - Network & Communication aspects in IoT

1. Protocol Independent Multicast (PIM): PIM is used for efficiently distributing data to large numbers of receivers. PIM routers build distribution trees that are multicast delivery paths between the sender and receivers. PIM has different modes:
- PIM-SM (Sparse-Mode): Used for multicast applications with widely dispersed receivers.
- PIM-DM (Dense-Mode): Used for dense receiver environments.

2. Distance Vector Multicast Routing Protocol (DVMRP): DVMRP uses a reverse path forwarding (RPF) check mechanism to build a distribution tree emanating from the source. It uses distance vectors to propagate reachability information between routers. The protocol specifies a mechanism to prune the distribution tree.

3. Multicast Open Shortest Path First (MOSPF): MOSPF is an extension to OSPF that supports multicast routing. OSPF link state advertisements are extended to include group membership information. The protocol computes multicast delivery trees that include only routers and links necessary to deliver packets to group members.

4. Core Based Trees (CBT): CBT creates a multicast distribution tree with a single core router at the root of the tree. Multicast data is forwarded along the tree from the source to the core and then from the core to the receivers. The core router is typically the router nearest the midpoint of the senders and receivers. The key advantage of CBT is that the core router aggregates state for the tree, limiting the amount of routing state in PIM routers.

[Further points and explanations...]