#### RARP

Reverse Address Resolution Protocol (RARP) is a networking protocol used to map a physical address (MAC address) to an Internet Protocol (IP) address. It is the inverse of Address Resolution Protocol (ARP), which maps an IP address to a MAC address.

RARP is used in situations where a computer knows its MAC address but not its IP address, such as when a diskless workstation is booted. In such cases, the workstation sends a RARP request to a RARP server, which responds with the corresponding IP address.

Here are some key points to understand about RARP:

- RARP is an older protocol that is not commonly used in modern networks. It has largely been replaced by Dynamic Host Configuration Protocol (DHCP), which performs the same function but with more flexibility and features.
- RARP operates at the data link layer (Layer 2) of the OSI model.
- RARP messages are broadcast over the network and do not use any form of authentication or security.
- RARP uses a simple request-response model, with the requesting device sending its MAC address in a RARP request and the responding device sending the corresponding IP address in a RARP reply.
- RARP servers maintain a database of MAC-to-IP mappings and respond to RARP requests accordingly. If a mapping is not found, the server does not respond.
- RARP can be used in conjunction with BOOTP (Bootstrap Protocol) to provide a complete network bootstrapping solution for diskless workstations.
- RARP has largely been replaced by DHCP as a more flexible and feature-rich protocol for automatically assigning IP addresses to network devices. However, some legacy systems may still use RARP, and it is worth understanding how it works for historical and troubleshooting purposes.