### Link layer switches & bridges

- Link layer switches and bridges are network devices that operate at the data link layer (layer 2) of the OSI model and forward data frames based on MAC addresses .
- Link layer switches and bridges can connect multiple LANs (local area networks) together to form a larger LAN. This process of aggregating networks is called network bridging .
- Link layer switches and bridges can improve network performance by dividing a large network into smaller segments and reducing collisions and congestion .
- Link layer switches and bridges can also provide filtering, learning, and spanning tree functions  .
  - Filtering: Link layer switches and bridges can discard frames that are not destined for any device on the connected LANs, thus reducing unnecessary traffic .
  - Learning: Link layer switches and bridges can learn the MAC addresses of the devices on the connected LANs by observing the source addresses of the incoming frames and storing them in a table .
  - Spanning tree: Link layer switches and bridges can avoid loops in the network by using a spanning tree protocol that dynamically disables some of the links and creates a tree-like topology .
- Link layer switches and bridges can be classified into different types based on their functionality and features .
  - Transparent bridges: These are the simplest type of bridges that learn MAC addresses and forward frames based on the destination address. They are called transparent because they are invisible to the devices on the network.
  - Source route bridges: These are bridges that use a source routing protocol that requires the sender to specify the path of the frame through the network. They are mainly used in Token Ring networks.
  - Remote bridges: These are bridges that connect LANs over a wide area network (WAN) using a point-to-point link or a tunneling protocol. They can extend the reach of a LAN across different locations.
  - Wireless bridges: These are bridges that connect a wired LAN to a wireless LAN or another wired LAN using a wireless access point. They can provide mobility and flexibility to the network .
  - Layer 3 switches: These are switches that can also forward data at the network layer (layer 3) of the OSI model by incorporating routing functionality. They can use IP addresses or other network layer protocols to forward packets. They are sometimes called IP switches or routing switches .