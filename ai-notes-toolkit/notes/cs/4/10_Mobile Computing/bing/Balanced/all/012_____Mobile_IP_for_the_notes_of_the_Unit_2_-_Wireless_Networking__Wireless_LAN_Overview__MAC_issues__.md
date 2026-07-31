# Mobile IP

Mobile IP is a communication protocol that allows the users to move from one network to another with the same IP address. It ensures that the communication will continue without the user's sessions or connections being dropped. It was designed to support seamless and continuous Internet connectivity. It is used in many wired and wireless environments where users have to carry their mobile devices across multiple LAN subnets. Mobile IP is scalable for the Internet because it is based on IP—any media that can support IP can support Mobile IP.

Some of the applications of Mobile IP are:

- Roaming between overlapping wireless systems, e.g., IP over DVB, WLAN, WiMAX and BWA.
- Mobile data communication in cellular systems such as 3G and in wireless LAN such as 802.11, and extending into satellite communication.
- Supporting mobile devices that need to access the Internet or other IP-based networks while moving across different networks or link layers.

Some of the key concepts and components of Mobile IP are:

- Home network: The network where the mobile device has a permanent IP address and is registered.
- Foreign network: The network where the mobile device is currently located and has a temporary IP address.
- Home agent: A router on the home network that maintains a binding table of the mobile device's permanent and temporary IP addresses and forwards packets to the foreign network.
- Foreign agent: A router on the foreign network that provides a temporary IP address to the mobile device and forwards packets to the mobile device from the home agent.
- Care-of address: The temporary IP address assigned to the mobile device on the foreign network.
- Tunneling: The process of encapsulating and decapsulating packets between the home agent and the foreign agent to deliver them to the mobile device.
- Registration: The process of notifying the home agent of the mobile device's current care-of address and updating the binding table.