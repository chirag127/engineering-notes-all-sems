#### DHCP

- DHCP stands for Dynamic Host Configuration Protocol.
- It is a network protocol that assigns IP addresses and other network parameters to devices dynamically.
- It operates on the application layer of the TCP/IP model and uses UDP as the transport protocol.
- It works in four steps: Discover, Offer, Request, and Acknowledge (DORA).
  - Discover: The client broadcasts a DHCPDISCOVER message to find a DHCP server on the network.
  - Offer: The DHCP server responds with a DHCPOFFER message, offering an IP address and other network parameters to the client.
  - Request: The client accepts the offer and broadcasts a DHCPREQUEST message, requesting the IP address and other network parameters from the server.
  - Acknowledge: The DHCP server confirms the allocation and sends a DHCPACK message to the client, acknowledging the request.
- DHCP has several advantages, such as:
  - It simplifies network administration by automating IP address assignment and configuration.
  - It reduces network conflicts and errors by avoiding duplicate IP addresses and ensuring consistency of network parameters.
  - It supports network scalability and mobility by allowing devices to join and leave the network easily and dynamically.
- DHCP has some disadvantages, such as:
  - It introduces security risks by exposing network information and allowing unauthorized devices to obtain IP addresses and access the network.
  - It depends on the availability and reliability of the DHCP server, which may fail or be overloaded by requests.
  - It consumes network bandwidth and resources by generating broadcast messages and requiring periodic renewals of IP addresses.

- A mnemonic to remember the four steps of DHCP is: **D**o **O**r **R**egret **A**ction (DORA).
- An example of a DHCPDISCOVER message is:

```
+---------------------+
| OP: 1 (request)     |
+---------------------+
| HTYPE: 1 (Ethernet) |
+---------------------+
| HLEN: 6             |
+---------------------+
| HOPS: 0             |
+---------------------+
| XID: 0x12345678     |
+---------------------+
| SECS: 0             |
+---------------------+
| FLAGS: 0x0000       |
+---------------------+
| CIADDR: 0.0.0.0     |
+---------------------+
| YIADDR: 0.0.0.0     |
+---------------------+
| SIADDR: 0.0.0.0     |
+---------------------+
| GIADDR: 0.0.0.0     |
+---------------------+
| CHADDR: 00:11:22:33:44:55 |
+---------------------+
| SNAME: (empty)      |
+---------------------+
| FILE: (empty)       |
+---------------------+
| OPTIONS:            |
|  - 53: DHCP Message Type (1: Discover) |
|  - 55: Parameter Request List (1: Subnet Mask, 3: Router, 6: DNS Server, 15: Domain Name) |
|  - 255: End         |
+---------------------+
```

- An example of a DHCPOFFER message is:

```
+---------------------+
| OP: 2 (reply)       |
+---------------------+
| HTYPE: 1 (Ethernet) |
+---------------------+
| HLEN: 6             |
+---------------------+
| HOPS: 0             |
+---------------------+
| XID: 0x12345678     |
+---------------------+
| SECS: 0             |
+---------------------+
| FLAGS: 0x0000       |
+---------------------+
| CIADDR: 0.0.0.0     |
+---------------------+
| YIADDR: 192.168.1.100 |
+---------------------+
| SIADDR: 192.168.1.1 |
+---------------------+
| GIADDR: 0.0.0.0     |
+---------------------+
| CHADDR: 00:11:22:33:44:55 |
+---------------------+
| SNAME: (empty)      |
+---------------------+
| FILE: (empty)       |
+---------------------+
| OPTIONS:            |
|  - 53: DHCP Message Type (2: Offer) |
|  - 1: Subnet Mask (255.255.255.0) |
|  - 3: Router (192.168.1.1) |
|  - 6: DNS Server (8.8.8.8) |
|  - 15: Domain Name (example.com) |
|  - 51: IP Address Lease Time (86400