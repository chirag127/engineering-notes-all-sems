CIDR stands for Classless Inter-Domain Routing. It is a method for allocating IP addresses and for IP routing. It allows blocks of addresses to be grouped into single routing table entries, which improves the efficiency of address distribution and routing.

CIDR notation is a compact representation of an IP address and its associated routing prefix. The notation is constructed from an IP address, a slash ('/') character, and a decimal number. The number is the count of leading 1 bits in the routing mask, traditionally called the network mask. The IP address is expressed according to the standards of IPv4 or IPv6.

For example, the IPv4 address 192.168.100.14/24 represents the IPv4 address 192.168.100.14 and its associated routing prefix 192.168.100.0, or equivalently, its subnet mask 255.255.255.0, which has 24 leading 1-bits.

The following ASCII diagram shows how CIDR notation works for IPv4 addresses:

```
  192.168.100.14/24
  |<--network-->|<--host-->|
  |<-prefix len->|
  |              |
  |              V
  11000000.10101000.01100100.00001110
  |<-------- 24 bits ------->|<- 8 ->|
  |<----- routing mask ----->|<--->|
  |                          |
  |                          V
  255.255.255.0
  |<--network-->|<--host-->|
```

The diagram shows that the IP address 192.168.100.14 belongs to the network 192.168.100.0, which has a prefix length of 24 bits. The routing mask is a binary string of 24 1-bits followed by 8 0-bits, which corresponds to the decimal value 255.255.255.0. The host part of the IP address is the remaining 8 bits, which can vary from 0 to 255.