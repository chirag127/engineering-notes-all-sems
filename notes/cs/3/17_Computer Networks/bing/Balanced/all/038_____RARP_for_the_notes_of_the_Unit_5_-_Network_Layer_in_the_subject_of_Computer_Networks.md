# RARP

RARP stands for Reverse Address Resolution Protocol. It is a network protocol that allows a host computer to obtain its IP address from a gateway server's ARP table or cache. RARP is used when a host does not know its own IP address, but knows its MAC address, which is a unique identifier assigned to the network interface card (NIC) of the host. RARP is defined in RFC 903 and is part of the TCP/IP protocol suite.

## RARP Operation

The basic steps of RARP operation are as follows:

- The host sends a RARP request packet to the broadcast address of the network, containing its MAC address and a request for its IP address.
- The RARP server, which is a router or a host that maintains a table of MAC-to-IP address mappings, receives the RARP request and looks up the IP address corresponding to the MAC address of the requester.
- The RARP server sends a RARP reply packet to the host, containing its IP address and MAC address.
- The host receives the RARP reply and configures its IP address accordingly.

## RARP Limitations

RARP has some limitations that make it less suitable for modern networks, such as:

- RARP requires a RARP server on each network segment, which increases the administrative overhead and the network traffic.
- RARP does not support subnetting, which is a technique to divide a network into smaller logical units for better performance and security.
- RARP does not provide any authentication or security mechanisms, which makes it vulnerable to spoofing and denial-of-service attacks.
- RARP does not support dynamic allocation of IP addresses, which is a feature that allows hosts to obtain IP addresses on demand from a central server.

## RARP Alternatives

RARP has been largely replaced by other protocols that provide more functionality and flexibility for IP address configuration, such as:

- BOOTP (Bootstrap Protocol), which is a protocol that allows a host to obtain its IP address, subnet mask, default gateway, and other configuration parameters from a BOOTP server.
- DHCP (Dynamic Host Configuration Protocol), which is a protocol that extends BOOTP and allows a host to obtain its IP address and other configuration parameters dynamically from a DHCP server.
- SLAAC (Stateless Address Autoconfiguration), which is a protocol that allows a host to generate its own IP address based on its MAC address and the network prefix, without the need for a server. SLAAC is used for IPv6, the latest version of the Internet Protocol.