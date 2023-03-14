### Mobile IP for the notes of the Unit 2 - Wireless Networking, Wireless LAN Overview: MAC issues, IEEE 802.11, Blue Tooth, Wireless in the subject of Mobile Computing

- Mobile IP (or MIP) is an Internet Engineering Task Force (IETF) standard communications protocol that is designed to allow mobile device users to move from one network to another while maintaining a permanent IP address.
- Mobile IP is based on IP and can support any media that can support IP, such as wired and wireless networks.
- Mobile IP is useful for applications that require continuous connectivity and seamless roaming, such as remote login, remote printing, file transfer, etc.
- Mobile IP works by using two types of IP addresses: a home address and a care-of address.
  - A home address is the permanent IP address of the mobile device, assigned by its home network.
  - A care-of address is the temporary IP address of the mobile device, assigned by the foreign network that it visits.
- Mobile IP also uses three types of entities: a mobile node, a home agent, and a foreign agent.
  - A mobile node is the device that roams across networks, such as a laptop or a smartphone.
  - A home agent is a router on the home network that keeps track of the mobile node's location and forwards packets to its care-of address.
  - A foreign agent is a router on the foreign network that provides services to the mobile node, such as assigning a care-of address and relaying packets to and from the home agent.
- Mobile IP works by using three main processes: agent discovery, registration, and tunneling.
  - Agent discovery is the process by which the mobile node discovers the presence and availability of home and foreign agents on the networks it visits.
  - Registration is the process by which the mobile node informs its home agent of its current care-of address and obtains authorization to use it.
  - Tunneling is the process by which the home agent encapsulates the packets destined for the mobile node and sends them to its care-of address, and vice versa.
- Mobile IP faces some challenges and limitations, such as security, scalability, efficiency, and compatibility.
  - Security issues include the risk of spoofing, replaying, or intercepting the registration messages and the tunneled packets.
  - Scalability issues include the overhead of maintaining and updating the binding entries for a large number of mobile nodes and the potential bottleneck at the home agent.
  - Efficiency issues include the suboptimal routing of the packets through the home agent and the foreign agent, which may increase the delay and the bandwidth consumption.
  - Compatibility issues include the need to support both IPv4 and IPv6 addresses and the possible conflicts with other protocols or network policies.

- A possible mnemonic to remember the main components and processes of Mobile IP is: **MART**.
  - **M**obile node: the device that roams across networks.
  - **A**gent: the router that provides services to the mobile node, either home or foreign.
  - **R**egistration: the process by which the mobile node informs its home agent of its current care-of address.
  - **T**unneling: the process by which the packets are encapsulated and forwarded to the mobile node's care-of address.