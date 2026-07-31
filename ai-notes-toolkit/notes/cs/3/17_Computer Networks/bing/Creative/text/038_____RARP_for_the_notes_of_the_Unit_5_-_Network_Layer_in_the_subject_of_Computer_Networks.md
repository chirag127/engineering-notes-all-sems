### RARP

- RARP stands for Reverse Address Resolution Protocol   .
- It is a network-specific standard protocol that is described in RFC 903.
- It is used by a client computer to request its IP address from a gateway server's Address Resolution Protocol (ARP) table or cache .
- It is based on the Network Access Layer (the lowest layer of the TCP/IP protocol stack) and is used to send data between two points in a network .
- Each network participant has two unique addresses: IP address (a logical address) and MAC address (the physical address) .
- The IP address is assigned by software and the MAC address is built into the hardware .
- RARP is useful for diskless workstations that do not have a permanent IP address and need to obtain one at boot time  .
- RARP works as follows  :
  - The client broadcasts a RARP request packet that contains its MAC address to the network.
  - The RARP server, which has a table that maps MAC addresses to IP addresses, receives the request and sends back a RARP reply packet that contains the IP address of the client.
  - The client receives the reply and configures its IP address accordingly.
- RARP has some limitations  :
  - It requires a RARP server on the same LAN as the client, which may not be always available or reliable.
  - It does not provide any authentication or security mechanism to verify the identity of the client or the server.
  - It does not support subnetting or routing, as it only works within a single broadcast domain.
  - It is obsolete and has been replaced by other protocols such as BOOTP and DHCP that offer more functionality and flexibility.