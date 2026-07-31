# RARP

RARP stands for Reverse Address Resolution Protocol. It is a network protocol that allows a host to obtain its IP address from a gateway server's ARP table or cache. RARP is used when a host does not have a permanent or preconfigured IP address, such as a diskless workstation or a device that boots from a network. RARP is defined in RFC 903.

Some points to note about RARP are:

- RARP operates on the network access layer, which is the lowest layer of the TCP/IP protocol stack. RARP uses the same packet format as ARP, but with different operation codes.
- RARP requires a specialized RARP server on the same LAN as the host. The RARP server maintains a table that maps the MAC addresses of the hosts to their IP addresses. The RARP server listens for RARP requests and responds with the corresponding IP address if it has an entry for the host in its table.
- RARP works as follows: The host broadcasts a RARP request packet with its MAC address as the source and destination address. The RARP server receives the packet and looks up the MAC address in its table. If it finds a match, it sends a RARP reply packet with the IP address of the host as the source and destination address. The host receives the packet and extracts its IP address from it.
- RARP has some limitations, such as: It only works on broadcast networks, such as Ethernet. It does not support subnetting or routing. It relies on the availability and accuracy of the RARP server. It does not provide any security or authentication mechanisms.
- RARP has been largely replaced by other protocols, such as BOOTP and DHCP, which offer more features and flexibility for dynamic IP address allocation. However, RARP is still supported by some devices and operating systems for backward compatibility.