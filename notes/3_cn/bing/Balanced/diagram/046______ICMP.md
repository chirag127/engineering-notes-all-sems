#### ICMP
ICMP stands for Internet Control Message Protocol. It is a network layer protocol that is used for error handling and diagnostic purposes. ICMP messages are transmitted as datagrams, which are independent units of data, and are encapsulated inside IP headers. ICMP messages do not have port numbers, so they are identified by their type and code fields. ICMP messages are typically generated in response to errors in IP operations, such as unreachable destinations, time exceeded, or parameter problems. ICMP messages can also be used for control purposes, such as echo request and reply, timestamp request and reply, or router advertisement and solicitation.

A diagram of an ICMP datagram is shown below, using ASCII characters to represent the bits. The diagram is not drawn to scale, and the bit order may vary depending on the endianness of the system.

```
+-----------------------------------------------------------------+
|0 1 2 3 4 5 6 7|0 1 2 3 4 5 6 7|0 1 2 3 4 5 6 7|0 1 2 3 4 5 6 7|
+-----------------------------------------------------------------+
|Version|  IHL  |Type of Service|          Total Length           |
+-----------------------------------------------------------------+
|         Identification        |Flags|       Fragment Offset     |
+-----------------------------------------------------------------+
|         Time to Live          |  Protocol  |   Header Checksum  |
+-----------------------------------------------------------------+
|                       Source IP Address                        |
+-----------------------------------------------------------------+
|                     Destination IP Address                     |
+-----------------------------------------------------------------+
|     Type      |     Code      |          Checksum               |
+-----------------------------------------------------------------+
|                             Data                                |
|                              ...                               |
+-----------------------------------------------------------------+
```

The IP header contains the following fields:

- Version: 4 bits, indicates the version of IP, usually 4 for IPv4.
- IHL: 4 bits, indicates the length of the IP header in 32-bit words, usually 5 for IPv4.
- Type of Service: 8 bits, indicates the quality of service desired for the datagram, such as precedence, delay, throughput, and reliability.
- Total Length: 16 bits, indicates the length of the entire datagram in bytes, including the IP header and data.
- Identification: 16 bits, used to identify the datagram and help in reassembly of fragmented datagrams.
- Flags: 3 bits, used to control fragmentation of datagrams, such as whether to allow or prohibit fragmentation, or whether the datagram is the last fragment or not.
- Fragment Offset: 13 bits, used to indicate the position of the fragment in the original datagram, measured in units of 8 bytes.
- Time to Live: 8 bits, used to limit the lifetime of the datagram in the network, and prevent infinite looping. The value is decremented by one by each router that forwards the datagram, and the datagram is discarded if the value reaches zero.
- Protocol: 8 bits, used to indicate the protocol of the data carried by the datagram, such as TCP, UDP, or ICMP. The value for ICMP is 1.
- Header Checksum: 16 bits, used to verify the integrity of the IP header. It is calculated by adding the 16-bit words of the header and taking the one's complement of the result. It is recomputed by each router that modifies the header, such as decrementing the TTL.
- Source IP Address: 32 bits, indicates the IP address of the sender of the datagram.
- Destination IP Address: 32 bits, indicates the IP address of the intended receiver of the datagram.

The ICMP header contains the following fields:

- Type: 8 bits, indicates the type of the ICMP message, such as 0 for echo reply, 8 for echo request, 3 for destination unreachable, etc.
- Code: 8 bits, indicates the sub-type of the ICMP message, such as 0 for network unreachable, 1 for host unreachable, etc.
- Checksum: 16 bits, used to verify the integrity of the ICMP header and data. It is calculated in the same way as the IP header checksum, but it is not modified by routers.
- Data: variable length, contains additional information for the ICMP message, such as the original IP header and the first 8 bytes of the original data for error messages, or a sequence number and a timestamp for echo messages. The format and length of the data depend on the type and code of the ICMP message.