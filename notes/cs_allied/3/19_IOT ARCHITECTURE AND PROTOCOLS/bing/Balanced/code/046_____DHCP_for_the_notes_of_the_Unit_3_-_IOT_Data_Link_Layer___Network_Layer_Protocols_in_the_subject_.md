# DHCP

- DHCP stands for Dynamic Host Configuration Protocol  .
- It is a network management protocol that automatically provides an Internet Protocol (IP) host with its IP address and other related configuration information such as the subnet mask and default gateway .
- It uses a client-server architecture, where a DHCP server allocates IP addresses and other parameters to DHCP clients that request them .
- It is based on the Bootstrap Protocol (BOOTP), which was designed for diskless workstations .
- It is defined by RFCs 2131 and 2132, and is an Internet Engineering Task Force (IETF) standard.
- It operates on four basic steps: discover, offer, request, and acknowledge (DORA)  .
  - Discover: The DHCP client broadcasts a DHCPDISCOVER message to find a DHCP server on the network  .
  - Offer: The DHCP server responds with a DHCPOFFER message, which contains an IP address and other configuration information for the client  .
  - Request: The DHCP client sends a DHCPREQUEST message to accept the offer from the server  .
  - Acknowledge: The DHCP server sends a DHCPACK message to confirm the allocation of the IP address and other parameters to the client  .
- It supports different types of IP address allocation, such as static, dynamic, and automatic .
  - Static: The DHCP server assigns a fixed IP address to a specific client based on its MAC address .
  - Dynamic: The DHCP server assigns an IP address from a pool of available addresses for a limited period of time (lease) .
  - Automatic: The DHCP server assigns an IP address from a pool of available addresses permanently .
- It has many benefits, such as reducing manual configuration, avoiding IP address conflicts, saving network resources, and simplifying network administration  .