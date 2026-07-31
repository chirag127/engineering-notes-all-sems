### RARP

RARP stands for Reverse Address Resolution Protocol. It is a network protocol that allows a host to obtain its IP address from a gateway server's ARP table or cache. RARP is used when a host does not have a permanent IP address assigned to it, such as a diskless workstation or a device that boots from a network. RARP operates on the network access layer of the TCP/IP protocol stack and uses the same packet format as ARP.

Some points to note about RARP are:

- RARP requires a RARP server on the same LAN as the host that needs an IP address. The RARP server maintains a table that maps MAC addresses to IP addresses.
- RARP uses broadcast messages to request and reply IP addresses. A host that needs an IP address sends a RARP request with its MAC address as the source and the broadcast address as the destination. The RARP server that receives the request looks up the MAC address in its table and sends back a RARP reply with the corresponding IP address.
- RARP is an obsolete protocol that has been replaced by other methods of obtaining IP addresses, such as BOOTP and DHCP. RARP is not supported by most modern operating systems and devices. RARP is defined in RFC 903.