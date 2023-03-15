#### CIDR

- CIDR stands for Classless Inter-Domain Routing, a method for allocating IP addresses and for IP routing .
- CIDR replaces the previous classful network addressing architecture on the Internet, which was based on fixed classes A, B, and C .
- CIDR allows blocks of IP addresses to be grouped into single routing table entries, which reduces the size and complexity of routing tables and improves the efficiency of address distribution .
- CIDR notation is a compact representation of an IP address and its associated routing prefix. It consists of an IP address, a slash (/), and a number that indicates the number of bits in the prefix  .
- For example, 192.168.1.0/24 is a CIDR notation that represents the IP address 192.168.1.0 and its prefix of 24 bits, which corresponds to the subnet mask 255.255.255.0. This means that the network has 256 possible IP addresses, from 192.168.1.0 to 192.168.1.255 .
- CIDR notation can also be used to represent a range of IP addresses, such as 192.168.0.0/16, which covers all the addresses from 192.168.0.0 to 192.168.255.255, or 10.0.0.0/8, which covers all the addresses from 10.0.0.0 to 10.255.255.255 .
- CIDR notation can be converted to IPv4 address range using a utility tool or by applying some simple arithmetic operations. For example, to convert 192.168.1.0/24 to IPv4 address range, we can do the following steps:
  - Find the number of host bits by subtracting the prefix length from 32. In this case, 32 - 24 = 8 host bits.
  - Find the number of possible hosts by raising 2 to the power of the host bits. In this case, 2^8 = 256 possible hosts.
  - Find the network address by performing a bitwise AND operation between the IP address and the subnet mask. In this case, 192.168.1.0 AND 255.255.255.0 = 192.168.1.0.
  - Find the broadcast address by performing a bitwise OR operation between the network address and the inverted subnet mask. In this case, 192.168.1.0 OR 0.0.0.255 = 192.168.1.255.
  - Find the first and last usable IP addresses by adding 1 to the network address and subtracting 1 from the broadcast address. In this case, 192.168.1.0 + 1 = 192.168.1.1 and 192.168.1.255 - 1 = 192.168.1.254.
  - The IPv4 address range is then the first and last usable IP addresses, separated by a dash. In this case, 192.168.1.1-192.168.1.254.
- A possible mnemonic to remember the CIDR notation is to think of the slash as a division sign, and the number after the slash as the number of equal parts that the IP address is divided into. For example, 192.168.1.0/24 means that the IP address is divided into 24 equal parts, each with 8 bits. The first part is the network prefix, and the remaining parts are the host addresses. The subnet mask is then the number of ones in the prefix, followed by zeros in the host bits. In this case, 11111111.11111111.11111111.00000000, or 255.255.255.0.