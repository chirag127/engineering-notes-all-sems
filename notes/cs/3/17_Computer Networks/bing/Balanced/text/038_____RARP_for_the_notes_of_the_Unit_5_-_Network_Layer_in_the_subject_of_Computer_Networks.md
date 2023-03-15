### RARP

- RARP stands for Reverse Address Resolution Protocol, which is a network protocol used to obtain the IP address of a device from its MAC address  .
- RARP is based on the Network Access Layer of the TCP/IP protocol stack, which is the lowest layer that deals with the physical transmission of data between two points in a network .
- RARP works by sending a broadcast message to a RARP server on the same local area network (LAN), containing the MAC address of the device that needs an IP address  .
- The RARP server then looks up its table or cache of MAC-to-IP mappings and replies with a unicast message containing the IP address of the device, if it is found  .
- RARP is useful for devices that do not have a permanent storage to store their IP address, such as diskless workstations or bootstrapping devices  .
- RARP has some limitations, such as:
  - It requires a dedicated RARP server on each LAN, which may not be available or reliable  .
  - It only works on networks that support broadcast messages, such as Ethernet or Token Ring, but not on point-to-point links or non-broadcast networks  .
  - It only supports IPv4 addresses, but not IPv6 addresses  .
- RARP has been largely replaced by other protocols, such as BOOTP and DHCP, which offer more features and flexibility for dynamic IP address allocation   .