# CIDR

- CIDR stands for **Classless Inter-Domain Routing**  .
- It is a method for allocating IP addresses and for IP routing  .
- It was introduced in 1993 by the Internet Engineering Task Force to replace the previous classful network addressing architecture on the Internet .
- CIDR is based on a bitwise, prefix-based representation of IP addresses and their routing properties.
- It allows blocks of addresses to be grouped into single routing table entries, which reduces the size and complexity of routing tables .
- CIDR also enables more efficient use of the available IP address space, especially for IPv4, which has been exhausted .
- A CIDR IP address looks like a normal IP address followed by a slash and a number, which indicates the length of the network prefix.
- For example, 192.168.1.0/24 is a CIDR IP address that represents the network 192.168.1.0 with a prefix length of 24 bits, which means that the first 24 bits of the address are fixed and the remaining 8 bits can vary.
- The number of addresses in a CIDR block can be calculated by subtracting the prefix length from 32 (for IPv4) or 128 (for IPv6) and raising 2 to the power of the result.
- For example, 192.168.1.0/24 has 32 - 24 = 8 bits that can vary, so it has 2^8 = 256 addresses in the block.
- CIDR notation can also be used to specify a range of IP addresses, by using a hyphen to indicate the lower and upper bounds of the range.
- For example, 192.168.1.0/24 - 192.168.1.255/24 is a CIDR range that covers all the addresses in the 192.168.1.0/24 network.