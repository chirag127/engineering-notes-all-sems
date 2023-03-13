#### RARP

- RARP stands for Reverse Address Resolution Protocol, which is a network protocol used to obtain an IP address from a MAC address.
- RARP operates on the Network Access Layer of the TCP/IP protocol stack, which is the lowest layer that deals with data transmission between two points in a network.
- RARP works by sending a broadcast message to a RARP server on the same local area network (LAN), containing the MAC address of the requesting device. The RARP server then looks up its table or cache of MAC-to-IP mappings and replies with the corresponding IP address, if found.
- RARP was published in 1984 and was used for address assignment for network hosts that did not have a permanent IP address, such as diskless workstations. However, RARP had some limitations, such as:
  - It required a RARP server on each LAN segment, which increased the network administration overhead.
  - It could not provide any additional information, such as subnet mask, default gateway, or domain name server, that a host might need to configure its network interface.
  - It could not handle dynamic address allocation or address reuse, which are essential for large-scale networks.
- RARP was eventually replaced by BOOTP and DHCP, which are more advanced and flexible protocols for address assignment and configuration. RARP is now considered obsolete and is rarely used in modern networks.