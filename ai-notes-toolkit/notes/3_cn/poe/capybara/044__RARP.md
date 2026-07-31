#### RARP

RARP (Reverse Address Resolution Protocol) is a protocol used to map a physical address to an IP address. It is used by diskless workstations to obtain their IP addresses from a network server. Here are some important points to know about RARP:

- RARP is the reverse of ARP (Address Resolution Protocol).
- ARP maps an IP address to a physical address, while RARP maps a physical address to an IP address.
- RARP is used by diskless workstations that do not have a hard disk to store their IP address configuration.
- The diskless workstation sends a broadcast message containing its physical address to the network, requesting its IP address.
- The RARP server responds with the corresponding IP address for the requested physical address.
- RARP is a legacy protocol and has been replaced by DHCP (Dynamic Host Configuration Protocol) in modern networks.
- RARP is not widely used anymore and is considered obsolete.
- RARP packets are encapsulated within Ethernet frames and have a protocol type value of 0x8035.
- RARP uses a table called the RARP table to map physical addresses to IP addresses.
- RARP is vulnerable to security attacks, such as spoofing and man-in-the-middle attacks.

In conclusion, RARP is a protocol that is used to map a physical address to an IP address. It is used by diskless workstations to obtain their IP addresses from a network server. However, it has been replaced by DHCP in modern networks and is considered obsolete.