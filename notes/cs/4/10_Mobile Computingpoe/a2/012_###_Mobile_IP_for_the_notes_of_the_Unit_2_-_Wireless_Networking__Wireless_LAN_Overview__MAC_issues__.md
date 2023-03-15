 Here is the content in Markdown format for the topic ### Mobile IP for the notes of the Unit 2 - Wireless Networking, Wireless LAN Overview: MAC issues, IEEE 802.11, Blue Tooth, Wireless in the subject of Mobile Computing:

# Mobile IP

Mobile IP is a protocol that allows mobile devices to move from one network to another while maintaining a consistent IP address. This means that the mobile device can stay connected to the network and access services even when it is not in its home network.

Some key points about Mobile IP:

- It allows mobile devices to change their point of attachment to the Internet without changing their IP address.
- It consists of two main components: Home Agent and Foreign Agent.
- Home Agent is a router on the mobile device's home network which tunnels datagrams for delivery to the mobile device and maintains current location information for the mobile device.
- Foreign Agent is a router on a foreign network which provides routing services to the mobile device while it is attached to that network. It can also provide Mobile IP registration and tunneling services.
- The mobile device is always addressable by its home address, no matter which network it is attached to.
- Packets addressed to the mobile device's home address are intercepted by its Home Agent and tunneled to the mobile device's current location.
- Mobile IP allows applications running on the mobile device to maintain TCP/IP connections as the device moves or changes its point of network attachment.

Some advantages of Mobile IP are:

- Transparency - Mobile devices can move between networks without changing their IP address. This is transparent to applications and peers.
- Simplicity - No changes are required to the network infrastructure. Only Mobile IP capable devices and agents are needed.
- Flexibility - Mobile devices are not limited to a specific foreign network and can attach to any network along their path.

Some disadvantages of Mobile IP are:

- Inefficiency - Tunneling overhead can reduce performance.
- Complexity - Mobile IP requires support on the mobile device and in the network. Implementing and configuring Mobile IP can be complex.
- Security - Mobile IP may pose some security risks due to roaming and tunneling. Extra security measures may be needed.

Applications of Mobile IP include:

- Allowing laptops and PDAs to roam between wireless LANs and wireline networks while maintaining connections.
- Enabling continuous Internet access for devices in vehicles moving between networks.
- Supporting cellular handoffs to provide ubiquitous Internet access.