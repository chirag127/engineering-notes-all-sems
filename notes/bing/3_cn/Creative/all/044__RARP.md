#### RARP

- RARP stands for **Reverse Address Resolution Protocol**   .
- It is a protocol based on computer networking that is used by a client computer to request its **IP address** from a gateway server's **ARP table** or cache   .
- It works on the **Network Access Layer** (the lowest layer) of the TCP/IP protocol stack .
- It is useful for devices that do not have a permanent IP address, such as diskless workstations or printers  .
- It operates by sending a **broadcast packet** containing the device's **MAC address** to the network, and waiting for a **RARP server** to reply with the corresponding IP address   .
- A RARP server is a specialized device that has a table or database of MAC addresses and IP addresses, and can respond to RARP requests .
- The format of a RARP packet is similar to an ARP packet, except that the **operation code** is set to 3 for request and 4 for reply.
- A RARP packet has the following fields:

| Field | Size (bytes) | Description |
| --- | --- | --- |
| Hardware type | 2 | Specifies the type of network hardware, such as Ethernet |
| Protocol type | 2 | Specifies the type of network protocol, such as IP |
| Hardware address length | 1 | Specifies the length of the hardware address, such as 6 for MAC address |
| Protocol address length | 1 | Specifies the length of the protocol address, such as 4 for IP address |
| Operation code | 2 | Specifies the type of RARP message, such as 3 for request and 4 for reply |
| Sender hardware address | Variable | Specifies the MAC address of the sender |
| Sender protocol address | Variable | Specifies the IP address of the sender (0.0.0.0 for request) |
| Target hardware address | Variable | Specifies the MAC address of the target (same as sender for request) |
| Target protocol address | Variable | Specifies the IP address of the target (0.0.0.0 for request, assigned IP address for reply) |

- An example of a RARP request and reply is shown below:

```
RARP request:

| Hardware type | Protocol type | Hardware address length | Protocol address length | Operation code | Sender hardware address | Sender protocol address | Target hardware address | Target protocol address |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 (Ethernet) | 0x0800 (IP) | 6 | 4 | 3 (request) | 00:0C:29:0A:0B:0C | 0.0.0.0 | 00:0C:29:0A:0B:0C | 0.0.0.0 |

RARP reply:

| Hardware type | Protocol type | Hardware address length | Protocol address length | Operation code | Sender hardware address | Sender protocol address | Target hardware address | Target protocol address |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 (Ethernet) | 0x0800 (IP) | 6 | 4 | 4 (reply) | 00:0C:29:0A:0B:0D | 192.168.1.1 | 00:0C:29:0A:0B:0C | 192.168.1.2 |
```

- RARP has some limitations and disadvantages, such as   :
  - It requires a RARP server on the same LAN as the client, which may not be available or reliable.
  - It only works with IP addresses, and cannot support other network protocols.
  - It only provides the IP address, and not other configuration information, such as subnet mask, default gateway, or DNS server.
  - It uses broadcast packets, which may cause network congestion or security issues.
- RARP has been superseded by other protocols, such as **BOOTP