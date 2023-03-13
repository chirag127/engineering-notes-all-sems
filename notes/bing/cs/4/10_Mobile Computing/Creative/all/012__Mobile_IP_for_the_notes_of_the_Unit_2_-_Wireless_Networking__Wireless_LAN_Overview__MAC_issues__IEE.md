### Mobile IP for the notes of the Unit 2 - Wireless Networking, Wireless LAN Overview: MAC issues, IEEE 802.11, Blue Tooth, Wireless in the subject of Mobile Computing

- Mobile IP (MIP) is a standard protocol that allows mobile devices to move from one network to another while maintaining the same permanent IP address.
- Mobile IP is based on the Internet Protocol (IP) and can support any media that can support IP, such as wired and wireless networks.
- Mobile IP is designed to support seamless and continuous Internet connectivity for mobile users who roam across different networks.
- Mobile IP works by using two types of IP addresses: a home address and a care-of address. The home address is the permanent IP address of the mobile device, assigned by its home network. The care-of address is the temporary IP address of the mobile device, assigned by the foreign network that it visits.
- Mobile IP uses three entities to facilitate mobility: a home agent, a foreign agent, and a mobile node. The home agent is a router in the home network that maintains a binding between the home address and the care-of address of the mobile device. The foreign agent is a router in the foreign network that provides routing services to the mobile device. The mobile node is the mobile device that changes its point of attachment to the Internet.
- Mobile IP operates in two phases: registration and tunneling. In the registration phase, the mobile node informs the home agent of its care-of address and requests a binding update. The home agent then sends a registration reply to the mobile node, either accepting or rejecting the binding. In the tunneling phase, the home agent encapsulates the packets destined for the mobile node and forwards them to the care-of address. The foreign agent then decapsulates the packets and delivers them to the mobile node. The reverse process happens for the packets sent by the mobile node.
- Mobile IP has several advantages, such as:
  - It preserves the existing IP applications and security mechanisms, as the mobile node does not change its home address.
  - It supports transparent mobility, as the mobile node does not need to reconfigure its IP settings or restart its connections when moving between networks.
  - It enables global roaming, as the mobile node can access the Internet from any network that supports IP.
- Mobile IP also has some disadvantages, such as:
  - It introduces additional overhead and latency, as the packets have to be encapsulated and decapsulated by the home agent and the foreign agent.
  - It may cause suboptimal routing, as the packets have to travel through the home network before reaching the mobile node, even if there is a shorter path available.
  - It may suffer from security issues, such as spoofing, replay, and denial-of-service attacks, as the registration and tunneling processes are vulnerable to malicious interference.
- Mobile IP can be used in various scenarios, such as:
  - Roaming between overlapping wireless systems, such as WLAN, WiMAX, and BWA.
  - Accessing the Internet from mobile devices, such as smartphones, tablets, and laptops.
  - Providing network connectivity for vehicles, such as cars, buses, and trains.

- A possible mnemonic to remember the three entities of Mobile IP is: **H**ome **A**gent, **F**oreign **A**gent, and **M**obile **N**ode, or **HAFMN**.
- A possible learning trick to understand the tunneling process of Mobile IP is to imagine a tunnel as a pipe that connects the home agent and the foreign agent. The packets are wrapped in a layer of IP header that contains the care-of address, and then sent through the pipe. The foreign agent then unwraps the packets and delivers them to the mobile node. The reverse process happens for the packets sent by the mobile node.