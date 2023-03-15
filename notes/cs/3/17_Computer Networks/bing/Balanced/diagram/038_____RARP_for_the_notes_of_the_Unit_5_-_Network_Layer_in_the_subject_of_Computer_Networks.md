### RARP

- RARP stands for **Reverse Address Resolution Protocol**   .
- It is a network-specific standard protocol that is described in **RFC 903**.
- It is used by a client computer to request its **IP address** from a gateway server's **ARP table** or cache  .
- It is on the **Network Access Layer** (i.e. the lowest layer of the TCP/IP protocol stack) and is used to send data between two points in a network .
- Each network participant has two unique addresses: **IP address** (a logical address) and **MAC address** (the physical address). The IP address is assigned by software and the MAC address is built into the hardware.
- RARP is useful for **diskless workstations** that do not have a permanent IP address and need to obtain one at boot time  .
- RARP works as follows  :
  - The client computer broadcasts a RARP request packet that contains its MAC address to the network.
  - The RARP server, which has a table that maps MAC addresses to IP addresses, receives the request and sends back a RARP reply packet that contains the IP address of the client.
  - The client computer receives the reply and configures its IP address accordingly.
- RARP has some limitations  :
  - It requires a RARP server on the same LAN as the client, which may not be always available or reliable.
  - It does not provide any authentication or security mechanism to verify the identity of the client or the server.
  - It does not support any configuration parameters other than the IP address, such as subnet mask, default gateway, DNS server, etc.
  - It is not widely supported by modern operating systems and devices, and has been replaced by other protocols such as **Bootstrap Protocol (BOOTP)** and **Dynamic Host Configuration Protocol (DHCP)**.