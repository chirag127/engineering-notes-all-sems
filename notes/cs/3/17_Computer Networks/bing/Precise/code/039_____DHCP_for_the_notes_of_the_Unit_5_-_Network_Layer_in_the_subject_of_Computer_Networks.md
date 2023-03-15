### DHCP (Dynamic Host Configuration Protocol)

- DHCP is a network protocol used to assign IP addresses and other network configuration information to devices on a network.
- DHCP operates on a client-server model, where a DHCP server assigns network configuration information to DHCP clients.
- The DHCP server maintains a pool of available IP addresses and assigns one to a client when it requests network access.
- DHCP can also provide other network configuration information, such as the default gateway, DNS server, and subnet mask.
- When a device connects to a network, it sends a broadcast message requesting network configuration information. This message is known as a DHCPDISCOVER message.
- The DHCP server responds with a DHCPOFFER message, offering an IP address and other network configuration information to the client.
- The client responds with a DHCPREQUEST message, requesting the offered IP address and network configuration information.
- The DHCP server responds with a DHCPACK message, acknowledging the client's request and providing the requested network configuration information.
- The client then configures its network interface with the provided information and can communicate on the network.
- DHCP can also be used to assign static IP addresses to specific devices, based on their MAC address.
- DHCP is commonly used in home networks, enterprise networks, and by internet service providers to assign IP addresses to customers.
