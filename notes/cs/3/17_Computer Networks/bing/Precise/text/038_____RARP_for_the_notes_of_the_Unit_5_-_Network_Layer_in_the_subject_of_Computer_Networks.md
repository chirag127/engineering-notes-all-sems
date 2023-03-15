### RARP

- RARP stands for Reverse Address Resolution Protocol.
- It is a network layer protocol used to resolve an IP address from a given hardware address, such as an Ethernet address.
- RARP is the opposite of the Address Resolution Protocol (ARP), which is used to resolve a hardware address from a given IP address.
- RARP is used in diskless workstations, which do not have a permanent storage to store their IP addresses.
- When a diskless workstation is powered on, it broadcasts a RARP request containing its hardware address to the network.
- A RARP server on the network receives the request and responds with the IP address that is associated with the hardware address.
- The diskless workstation can then use the IP address to communicate with other devices on the network.
- RARP is defined in RFC 903 and uses the same packet format as ARP.
- RARP has been largely replaced by other protocols, such as BOOTP and DHCP, which provide more functionality and flexibility in assigning IP addresses to devices on a network.