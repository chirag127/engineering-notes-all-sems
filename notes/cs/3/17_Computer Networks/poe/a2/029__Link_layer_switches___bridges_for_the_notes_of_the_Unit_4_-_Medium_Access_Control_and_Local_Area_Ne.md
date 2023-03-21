 Here are the notes on Link layer switches & bridges for the Unit 4 - Medium Access Control and Local Area Networks in Computer Networks:

### Link layer switches & bridges

- Link layer switches operate at the data link layer (layer 2) of the OSI model. They forward traffic based on MAC addresses and are faster than routers as they do not need to examine network layer packet headers.
- A bridge is a simplest form of a link layer switch. It connects two network segments and forwards traffic between them based on MAC addresses. It learns the MAC addresses of devices on each segment and maintains a MAC address table. When a frame is received, it looks up the destination MAC address in the table and forwards the frame to the appropriate segment.
- Advanced link layer switches use application-specific integrated circuits (ASICs) to build and maintain the MAC address table and forward frames. They offer additional features like support for VLANs and Spanning Tree Protocol.
- The key benefits of link layer switches are their speed and low cost. However, they can only forward traffic within a single LAN and cannot connect multiple LANs like routers. So, they are typically used within a small network.

The above points cover the key aspects of link layer switches and bridges. The notes are written in a formal tone with points and no emojis or external links as per the given guidelines. Please let me know if you would like me to elaborate on any of the points or modify the content.