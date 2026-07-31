### RARP

RARP stands for Reverse Address Resolution Protocol. It is used to obtain the IP address of a host when its physical address is already known. Here are some important points to keep in mind regarding RARP:

- RARP is used in situations where a host does not have an IP address configured and needs to obtain one dynamically from a RARP server.
- RARP works in the opposite direction of ARP, which is used to obtain the physical address of a host when its IP address is already known.
- RARP operates at the data link layer of the OSI model.
- The RARP request message contains the physical address of the host that is requesting an IP address.
- The RARP server responds to the request with an IP address that is mapped to the physical address in its database.
- RARP uses a simple client-server model. The client sends a broadcast request to all hosts on the network, and the server responds with the appropriate IP address.
- RARP servers are typically configured with a static mapping between physical addresses and IP addresses.
- RARP has largely been replaced by more modern protocols such as DHCP (Dynamic Host Configuration Protocol), which can provide additional functionality such as assigning subnet masks and default gateways.

Overall, while RARP may not be widely used today, it is still important to understand its basic principles and how it fits into the network layer of the OSI model.