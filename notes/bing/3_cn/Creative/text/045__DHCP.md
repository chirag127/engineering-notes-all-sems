#### DHCP

- DHCP stands for Dynamic Host Configuration Protocol .
- It is a network management protocol that automatically assigns IP addresses and other communication parameters to devices connected to a network using a client-server architecture  .
- It simplifies the configuration and administration of IP networks, as it eliminates the need for manual intervention or pre-allocation of IP resources   .
- It operates on four basic steps: discover, offer, request, and acknowledge  .
  - Discover: The client broadcasts a DHCPDISCOVER message to find a DHCP server on the network  .
  - Offer: The DHCP server responds with a DHCPOFFER message that contains an IP address and other configuration information for the client  .
  - Request: The client sends a DHCPREQUEST message to accept the offer and request the IP address and configuration information from the server  .
  - Acknowledge: The server sends a DHCPACK message to confirm the IP address and configuration information to the client  .
- It supports different types of IP address allocation methods, such as static, dynamic, and automatic .
  - Static: The DHCP server assigns a fixed IP address to a specific client based on its MAC address .
  - Dynamic: The DHCP server assigns an IP address from a pool of available addresses for a limited period of time (called a lease) .
  - Automatic: The DHCP server assigns an IP address from a pool of available addresses for an indefinite period of time (until the client releases it) .
- It is based on the Bootstrap Protocol (BOOTP), which is an older protocol for IP address allocation .
- It is defined by RFCs 2131 and 2132, and has been extended by several other RFCs to support additional features and options .