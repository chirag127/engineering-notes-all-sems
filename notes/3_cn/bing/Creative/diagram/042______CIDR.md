#### CIDR

CIDR stands for Classless Inter-Domain Routing. It is a method for allocating IP addresses and for IP routing. It was introduced in 1993 to replace the previous classful network addressing architecture on the Internet.

Some of the main features of CIDR are:

- It uses a bitwise, prefix-based notation to represent IP addresses and their routing properties. For example, 192.168.1.0/24 means that the first 24 bits of the address are fixed, and the remaining 8 bits can vary. This notation is also called CIDR format .
- It allows blocks of addresses to be grouped into single routing table entries, reducing the size and complexity of routing tables. For example, 192.168.0.0/16 can represent 65,536 addresses in one entry, instead of 256 entries for each /24 subnet .
- It enables more efficient use of the IP address space, by allowing variable-length subnetting and supernetting. Subnetting is the process of dividing a network into smaller subnetworks, while supernetting is the process of combining multiple networks into a larger network .
- It supports both IPv4 and IPv6 protocols, although the notation and the address space are different for each. For example, IPv4 uses 32-bit addresses, while IPv6 uses 128-bit addresses.