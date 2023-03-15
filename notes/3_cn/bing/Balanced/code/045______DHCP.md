#### DHCP
Dynamic Host Configuration Protocol (DHCP) is a protocol that allows a server to assign an IP address and other network configuration parameters to a client automatically. The client sends a DHCPDISCOVER message to the server, and the server responds with a DHCPOFFER message containing the IP address and other information. The client then sends a DHCPREQUEST message to accept the offer, and the server sends a DHCPACK message to acknowledge the request.

A DHCP message consists of several fields, such as:

- OP Code: indicates whether the message is from the client (1) or the server (2).
- Hardware Type: indicates the type of network interface used by the client, such as Ethernet or Wi-Fi.
- Hardware Address Length: indicates the length of the hardware address, such as 6 for Ethernet MAC address.
- Transaction ID: a random number chosen by the client to identify the message exchange.
- Flags: indicates whether the client can receive unicast or broadcast messages from the server.
- Client IP Address: the IP address of the client, if already assigned.
- Your (client) IP Address: the IP address offered by the server to the client.
- Server IP Address: the IP address of the server that sent the offer.
- Gateway IP Address: the IP address of the router that connects the client to the server.
- Client Hardware Address: the MAC address of the client's network interface.
- Server Host Name: the name of the server that sent the offer.
- Boot File Name: the name of the file that contains the boot image for the client, if applicable.
- Options: a variable-length field that contains additional parameters for the client, such as subnet mask, default gateway, DNS server, etc.

An example of a DHCP message in hexadecimal format is:

```hex
01 01 06 00 9b 0f 6f 1a 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
63 82 53 63 35 01 01 3d 07 01 00 0c 29 9b 0f 6f
1a 32 04 c0 a8 01 64 37 0a 01 03 06 0c 2a ff 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
```

This message can be interpreted as follows:

- OP Code: 01 (client)
- Hardware Type: 01 (Ethernet)
- Hardware Address Length: 06 (6 bytes)
- Transaction ID: 9b0f6f1a
- Flags: 0000 (unicast)
- Client IP Address: 00000000 (not assigned)
- Your (client) IP Address: 00000000 (not assigned)
- Server IP Address: 00000000 (not assigned)
- Gateway IP Address: 00000000 (not assigned)
- Client Hardware Address: 000c299b0f6f (MAC address)
- Server Host Name: 000000000000000000000000000000000000000000000000 (not specified)
- Boot File Name: 000000000000000000000000000000000000000000000000 (not specified)
- Options: 63825363 (magic cookie)
  - 35 01 01 (option 53, length 1, value 1: DHCPDISCOVER)
  - 3d 07 01 00 0c 29 9b 0f 6f 1a (option 61, length 7, value 01000c299b0f6f1a: client identifier)
  - 32 04 c0 a8 01 64 (option 50, length 4, value c0a80164: requested IP address 192