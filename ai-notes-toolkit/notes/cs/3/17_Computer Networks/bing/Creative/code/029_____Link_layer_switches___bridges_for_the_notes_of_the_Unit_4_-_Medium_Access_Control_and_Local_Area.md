### Link layer switches & bridges

- Link layer switches and bridges are network devices that operate at the data link layer (layer 2) of the OSI model and connect multiple LANs together to form a larger LAN  .
- The main function of link layer switches and bridges is to forward frames based on the MAC addresses of the source and destination devices .
- Link layer switches and bridges learn the MAC addresses of the devices connected to their ports by observing the source addresses of the incoming frames and store them in a table called the MAC address table or the forwarding table .
- When a link layer switch or bridge receives a frame, it looks up the destination MAC address in its table and forwards the frame to the corresponding port. If the destination MAC address is not in the table, it floods the frame to all ports except the one it came from .
- Link layer switches and bridges can improve the performance and scalability of LANs by dividing them into smaller segments and reducing the collision domain and the broadcast domain  .
- Link layer switches and bridges can also provide some security features, such as filtering frames based on MAC addresses or VLAN tags, and preventing loops using the spanning tree protocol (STP)  .
- The main difference between link layer switches and bridges is that switches have multiple ports and can forward frames in parallel, while bridges have only two ports and can forward frames in serial. Switches are also faster and more intelligent than bridges .
- Some examples of link layer switches and bridges are Ethernet switches, wireless access points, transparent bridges, and source routing bridges   .