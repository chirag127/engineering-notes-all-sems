# Logical Addressing

Logical addressing is a scheme of addressing that allows computers to communicate over a network using a global addressing scheme. Logical addresses are also known as internet protocol (IP) addresses, and they are assigned by the network layer of the TCP/IP protocol stack.

## Features of Logical Addressing

- Logical addresses are software-based, meaning they can be changed or modified by the network administrator or the operating system.
- Logical addresses are independent of the physical addresses, meaning they do not depend on the hardware or the link layer of the network.
- Logical addresses are hierarchical, meaning they have two parts: a network part and a host part. The network part identifies the network or the subnet to which the host belongs, and the host part identifies the specific host within the network or the subnet.
- Logical addresses are unique, meaning no two hosts on the same network or the internet can have the same logical address.

## Methods of Logical Addressing

There are two versions of logical addressing: IPv4 and IPv6. IPv4 is the most widely used version, and it uses 32-bit addresses. IPv6 is the newer version, and it uses 128-bit addresses. Both versions have different formats and features, and they are not compatible with each other.

### IPv4 Addressing

- An IPv4 address is a 32-bit binary number that is usually written in dotted-decimal notation, such as 192.168.1.1. Each decimal number represents 8 bits, and there are four decimal numbers separated by dots.
- An IPv4 address has two parts: a network part and a host part. The network part is determined by the network mask or the prefix length, which indicates how many bits are used for the network part. For example, a network mask of 255.255.255.0 or a prefix length of /24 means that the first 24 bits are used for the network part, and the remaining 8 bits are used for the host part.
- An IPv4 address can be classified into five classes: A, B, C, D, and E. Each class has a different range of network addresses and host addresses, and a different default network mask. For example, class A addresses have a network mask of 255.0.0.0 or /8, and they can have up to 126 networks and 16,777,214 hosts per network.
- An IPv4 address can also be divided into subnets, which are smaller networks within a larger network. Subnetting allows more efficient use of the address space and better control of the network traffic. Subnetting involves borrowing bits from the host part and adding them to the network part, creating a new network mask or prefix length. For example, a class C address with a network mask of 255.255.255.0 or /24 can be subnetted into four subnets with a network mask of 255.255.255.192 or /26, each having 62 hosts.

### IPv6 Addressing

- An IPv6 address is a 128-bit binary number that is usually written in hexadecimal notation, such as 2001:db8:0:1234:0:567:8:1. Each hexadecimal number represents 4 bits, and there are eight hexadecimal numbers separated by colons.
- An IPv6 address has two parts: a network part and an interface part. The network part is determined by the network prefix, which indicates how many bits are used for the network part. For example, a network prefix of 2001:db8::/32 means that the first 32 bits are used for the network part, and the remaining 96 bits are used for the interface part.
- An IPv6 address can be abbreviated by omitting leading zeros and replacing consecutive zeros with a double colon. For example, the address 2001:0db8:0000:1234:0000:0567:0008:0001 can be abbreviated as 2001:db8:0:1234::567:8:1.
- An IPv6 address can also be assigned to multiple interfaces, creating a link-local address or a site-local address. A link-local address is used for communication within the same link or subnet, and it has a prefix of fe80::/10. A site-local address is used for communication within the same site or organization, and it has a prefix of fec0