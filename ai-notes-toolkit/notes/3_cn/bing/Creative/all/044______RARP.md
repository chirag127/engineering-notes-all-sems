#### RARP

- RARP stands for Reverse Address Resolution Protocol  .
- It is a protocol based on computer networking that is used by a client computer to request its IP address from a gateway server's Address Resolution Protocol (ARP) table or cache  .
- It is on the Network Access Layer (i.e. the lowest layer of the TCP/IP protocol stack) and is thus a protocol used to send data between two points in a network.
- It works by sending the device's physical address (MAC address) to a specialized RARP server that is on the same LAN and is actively listening for RARP requests.
- The RARP server then looks up the MAC address in its ARP table or cache and returns the corresponding IP address to the client computer.
- RARP is useful for devices that do not have a permanent IP address, such as diskless workstations or printers, and need to obtain one dynamically from a server  .
- RARP is an obsolete protocol that has been replaced by more advanced protocols such as BOOTP and DHCP  .
- RARP has some limitations, such as:
  - It requires a RARP server on each LAN segment, which increases the network administration overhead  .
  - It does not support subnetting or routing, which limits its scalability and flexibility  .
  - It does not provide any security or authentication mechanisms, which exposes the network to potential attacks  .
  - It does not allow the client computer to specify any additional configuration parameters, such as default gateway, DNS server, or subnet mask  .

- A possible mnemonic to remember the RARP protocol is: **R**everse **A**RP **R**equests **P**hysical address.
- A possible learning trick to understand the RARP protocol is to compare it with the ARP protocol, which does the opposite function: it maps an IP address to a MAC address  .
- A possible ASCII diagram to illustrate the RARP protocol is:

```
Client computer (MAC: AA-BB-CC-DD-EE-FF)              RARP server (IP: 192.168.1.1)
|                                                     |
|-----------------RARP request----------------------->|
|                                                     |
|<----------------RARP reply (IP: 192.168.1.100)------|
|                                                     |
```