### ICMP

- ICMP stands for Internet Control Message Protocol. It is a network layer protocol that is used by network devices to communicate problems with data transmission  .
- ICMP messages are typically used for diagnostic or control purposes or generated in response to errors in IP operations. For example, ICMP can report if a destination host is unreachable, if a packet is too large to be delivered, or if the time to live (TTL) of a packet has expired .
- ICMP messages have a common header format that consists of 8 bits of type, 8 bits of code, and 16 bits of checksum. The type and code fields indicate the purpose and the details of the message. The checksum field is used to verify the integrity of the message.
- Some of the common ICMP message types are:

  - Echo request and echo reply: These messages are used to test the connectivity and reachability of a destination host. The echo request message is sent by the source host and the echo reply message is sent back by the destination host. This is the basis of the ping utility  .
  - Destination unreachable: This message is sent by a router or a host when it cannot deliver a packet to the intended destination. The code field specifies the reason for the failure, such as network unreachable, host unreachable, protocol unreachable, port unreachable, or fragmentation needed  .
  - Time exceeded: This message is sent by a router or a host when the TTL of a packet has expired. The TTL is a field in the IP header that indicates how many hops a packet can traverse before being discarded. The code field specifies whether the TTL expired in transit or in reassembly  .
  - Parameter problem: This message is sent by a router or a host when it encounters an error in the IP header of a packet. The code field specifies the type of error, such as pointer indicates the error, missing a required option, or bad length. The pointer field indicates the location of the error in the IP header.
  - Source quench: This message is sent by a router or a host when it is experiencing congestion and cannot process incoming packets. The source quench message requests the sender to reduce the rate of transmission.
  - Redirect: This message is sent by a router to inform a host of a better route to a destination. The code field specifies the type of redirect, such as redirect for network, redirect for host, redirect for type of service and network, or redirect for type of service and host. The gateway address field indicates the IP address of the preferred router.

- ICMP is an important aspect of the error reporting and network diagnostics processes. However, ICMP can also be used for malicious purposes, such as scanning, spoofing, or denial-of-service attacks. Therefore, network administrators should monitor and filter ICMP traffic carefully .

: https://www.fortinet.com/resources/cyberglossary/internet-control-message-protocol-icmp
: https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol
: https://www.cloudflare.com/learning/ddos/glossary/internet-control-message-protocol-icmp/