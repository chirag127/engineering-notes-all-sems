#### RARP

RARP stands for Reverse Address Resolution Protocol. It is a protocol used to map a MAC address to an IP address. It is used in situations where a device knows its own MAC address but does not know its IP address.

- RARP operates at the Data Link Layer of the OSI model.
- RARP is used by diskless workstations to obtain an IP address from a RARP server.
- RARP uses the same message format as ARP, but with different operation codes.
- RARP is not widely used anymore and has been replaced by other protocols such as BOOTP and DHCP.

A mnemonic to remember the difference between ARP and RARP is that ARP is used to find the MAC address when the IP address is known, while RARP is used to find the IP address when the MAC address is known. You can remember this by thinking of the "R" in RARP as standing for "Reverse".