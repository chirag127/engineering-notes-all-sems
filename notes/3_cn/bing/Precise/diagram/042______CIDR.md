#### CIDR
Classless Inter-Domain Routing (CIDR) is a method for allocating IP addresses and routing Internet Protocol packets. Here is an ASCII diagram that illustrates the concept of CIDR notation:

```
  192.168.100.14/24
  |__________| |__|
       |        |
       |        |
 IP Address   Prefix Length
```

In this example, the IP address is `192.168.100.14` and the prefix length is `24`. The prefix length specifies how many of the leftmost contiguous bits of the address comprise the network portion of the address. In this case, the first 24 bits of the IP address are the network portion, and the remaining 8 bits are the host portion. This means that all IP addresses in the range `192.168.100.0` to `192.168.100.255` are in the same network.
