### DHCP

- DHCP stands for Dynamic Host Configuration Protocol   .
- It is a network management protocol that automatically provides an Internet Protocol (IP) host with its IP address and other related configuration information such as the subnet mask and default gateway .
- It uses a client-server architecture, where a DHCP server allocates IP addresses and other parameters to DHCP clients that request them   .
- It is based on the Bootstrap Protocol (BOOTP), which was designed for diskless workstations .
- It is defined by RFCs 2131 and 2132, and supports both IPv4 and IPv6 .
- It operates on four basic steps: discover, offer, request, and acknowledge   .
  - Discover: The DHCP client broadcasts a DHCPDISCOVER message to find a DHCP server on the network   .
  - Offer: The DHCP server responds with a DHCPOFFER message, containing an IP address and other configuration options for the client   .
  - Request: The DHCP client selects one of the offers and sends a DHCPREQUEST message to the chosen server, requesting the IP address and other parameters   .
  - Acknowledge: The DHCP server confirms the allocation with a DHCPACK message, or rejects it with a DHCPNAK message   .
- It allows for dynamic and efficient management of IP addresses and network configuration, reducing manual intervention and errors   .
- It also supports features such as lease time, renewal, release, and rebinding of IP addresses, as well as static and dynamic allocation of IP addresses   .
- It is widely used in various types of networks, such as LANs, WANs, WLANs, and IoT networks   .