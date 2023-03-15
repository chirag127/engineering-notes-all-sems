### DHCP

- DHCP stands for Dynamic Host Configuration Protocol  and is a network management protocol that automatically provides an Internet Protocol (IP) host with its IP address and other related configuration information such as the subnet mask and default gateway.
- DHCP uses a client-server architecture, where a DHCP server allocates IP addresses and other parameters to DHCP clients that request them .
- DHCP is based on the Bootstrap Protocol (BOOTP), which was designed for diskless workstations. DHCP extends BOOTP by adding the ability to dynamically assign and reuse IP addresses, and by allowing the clients to obtain additional configuration options .
- DHCP operates in four phases: discovery, offer, request, and acknowledgement   .
  - In the discovery phase, the client broadcasts a DHCPDISCOVER message to locate a DHCP server on the network   .
  - In the offer phase, the server responds with a DHCPOFFER message that contains an IP address and other parameters for the client   .
  - In the request phase, the client chooses one of the offers and broadcasts a DHCPREQUEST message to request the IP address and parameters from the server   .
  - In the acknowledgement phase, the server confirms the allocation with a DHCPACK message, or rejects it with a DHCPNAK message   .
- DHCP can also support static IP address assignment, where the server assigns a fixed IP address to a specific client based on its MAC address or other identifier .
- DHCP can also support dynamic DNS updates, where the server updates the DNS records of the client's hostname and IP address .
- DHCP can also support relay agents, where a device forwards DHCP messages between clients and servers that are on different subnets .
- DHCP can also support options, where the server can provide additional information to the client, such as the domain name, the DNS servers, the time servers, the network boot file, etc .
- DHCP is defined by RFCs 2131 and 2132, and has been updated by several other RFCs .