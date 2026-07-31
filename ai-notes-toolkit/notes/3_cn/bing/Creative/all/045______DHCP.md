#### DHCP

- DHCP stands for Dynamic Host Configuration Protocol   .
- It is a network management protocol that automatically assigns IP addresses and other communication parameters to devices connected to a network using a client-server architecture   .
- It is based on the Bootstrap Protocol (BOOTP), which is an older protocol for network booting .
- It uses the User Datagram Protocol (UDP) as the transport protocol and operates on port 67 for the server and port 68 for the client .
- It consists of four basic steps: discover, offer, request, and acknowledge (DORA)  .
  - Discover: The client broadcasts a DHCPDISCOVER message to find a DHCP server on the network  .
  - Offer: The DHCP server responds with a DHCPOFFER message that contains an IP address and other configuration information for the client  .
  - Request: The client sends a DHCPREQUEST message to accept the offer from the server and request the IP address lease  .
  - Acknowledge: The server sends a DHCPACK message to confirm the lease and provide additional information to the client  .
- It can also provide other information such as the subnet mask, default gateway, domain name, DNS servers, and time servers   .
- It can be configured to assign static or dynamic IP addresses to clients   .
  - Static IP addresses are fixed and do not change over time   .
  - Dynamic IP addresses are temporary and can change when the lease expires or when the client renews the lease   .
- It has several advantages, such as   :
  - Reducing manual configuration and human errors   .
  - Simplifying network administration and management   .
  - Improving network performance and security   .
  - Supporting network scalability and mobility   .
- It has some disadvantages, such as   :
  - Requiring a DHCP server to be available and reliable   .
  - Increasing network traffic and latency due to broadcast messages   .
  - Exposing the network to potential security risks and attacks   .
- It is widely used in various network environments, such as home networks, enterprise networks, wireless networks, and Internet service providers   .

: https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol
: https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-top
: https://www.spiceworks.com/tech/networking/articles/what-is-dhcp/
: https://www.lifewire.com/what-is-dhcp-2625848