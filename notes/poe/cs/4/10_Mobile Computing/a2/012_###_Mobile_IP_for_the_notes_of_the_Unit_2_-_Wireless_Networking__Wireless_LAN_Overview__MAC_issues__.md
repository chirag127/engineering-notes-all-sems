 Here is the content in markdown format:

### Mobile IP for the notes of the Unit 2 - Wireless Networking, Wireless LAN Overview: MAC issues, IEEE 802.11, Blue Tooth, Wireless in the subject of Mobile Computing

Mobile IP is a protocol that allows mobile devices to move from one network to another while maintaining a permanent IP address. It solves the problem of changing IP addresses as the device moves to a new subnet.

**How it works:**

- Home Agent: A router on the home network that tracks the mobile node's current location.
- Foreign Agent: A router on the visited network that helps route packets to the mobile node.
- Mobile Node: The mobile device that is moving between networks.

The mobile node is always addressable by its home IP address. When it moves to a foreign network, it registers its temporary care-of address with the home agent. The home agent forwards any packets destined for the mobile node to its care-of address. This makes it appear as if the mobile node is still on the home network, allowing sessions to be maintained as the node moves.

**Advantages:**

- Device can move freely without losing network connectivity.
- No changes required to higher-level protocols.
- Devices can be accessed using a consistent IP address.

**Disadvantages:**

- Additional overhead for registration and encapsulation of packets.
- Reliance on foreign agents in visited networks.
- Security vulnerabilities with malicious redirection of packets.

**Applications:** Mobile computing, wireless networking.

**Mnemonics:**

- Home sweet home: The home agent is on the home network.
- Visit and register: The mobile node visits a foreign network and registers with the home agent.
- One address to find them: The mobile node is addressed using its permanent home IP address.

Does this help? Let me know if you would like me to elaborate on any part of the content.