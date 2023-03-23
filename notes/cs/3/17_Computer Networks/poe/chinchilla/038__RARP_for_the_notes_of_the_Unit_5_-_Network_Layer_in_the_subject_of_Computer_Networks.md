### RARP

RARP stands for Reverse Address Resolution Protocol. It is a protocol used to map a physical or MAC address to an IP address. In contrast to ARP (Address Resolution Protocol) which maps an IP address to a physical address, RARP does the opposite. Here are some important points to understand about RARP:

- RARP is a legacy protocol that is rarely used in modern networks.
- It was developed by Sun Microsystems for use in their diskless workstations.
- RARP uses a server-client model, where a RARP server maintains a database of MAC addresses and their corresponding IP addresses, and responds to RARP requests from clients.
- When a client needs to determine its IP address, it sends a RARP broadcast message containing its MAC address. The RARP server then responds with the corresponding IP address.
- RARP is typically used in environments where diskless workstations are used, such as in a thin client or virtual desktop infrastructure (VDI) environment.
- RARP has several limitations, including security concerns and the fact that it does not scale well in large networks.
- RARP has largely been replaced by newer protocols such as DHCP (Dynamic Host Configuration Protocol), which can provide more functionality and security.

In summary, RARP is a legacy protocol used to map MAC addresses to IP addresses. While it has some uses in specific environments, it has largely been supplanted by newer protocols such as DHCP.