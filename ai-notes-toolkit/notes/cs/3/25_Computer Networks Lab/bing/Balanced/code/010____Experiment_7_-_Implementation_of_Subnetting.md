## Experiment 7 - Implementation of Subnetting

Subnetting is the process of dividing a network into smaller subnetworks or subnets. Subnetting allows us to:

- Conserve IP addresses by allocating them more efficiently.
- Reduce network traffic by isolating broadcast domains.
- Simplify network design and management by grouping hosts with similar requirements.
- Enhance network security by applying different policies to different subnets.

To perform subnetting, we need to understand the following concepts and terms:

- IP address: A 32-bit binary number that identifies a host or a network interface on the Internet Protocol (IP) network. An IP address consists of two parts: network part and host part. The network part identifies the network to which the host belongs, and the host part identifies the specific host within the network. For example, in the IP address 192.168.1.100, the network part is 192.168.1 and the host part is 100.
- Subnet mask: A 32-bit binary number that determines how many bits of the IP address are used for the network part and how many bits are used for the host part. The subnet mask has 1s in the network part and 0s in the host part. For example, the subnet mask 255.255.255.0 has 24 bits for the network part and 8 bits for the host part. The subnet mask can also be written in slash notation as /24, which means the same thing as 255.255.255.0.
- Network ID: The network part of the IP address, obtained by performing a bitwise AND operation between the IP address and the subnet mask. The network ID identifies the subnet to which the host belongs. For example, the network ID of the IP address 192.168.1.100 with the subnet mask 255.255.255.0 is 192.168.1.0.
- Broadcast ID: The IP address that has all 1s in the host part, obtained by performing a bitwise OR operation between the network ID and the inverse of the subnet mask. The broadcast ID is used to send a message to all hosts in the subnet. For example, the broadcast ID of the network ID 192.168.1.0 with the subnet mask 255.255.255.0 is 192.168.1.255.
- Total hosts: The number of possible IP addresses in the subnet, calculated by raising 2 to the power of the number of bits in the host part. For example, the total hosts in the subnet with the subnet mask 255.255.255.0 is 2^8 = 256.
- Valid hosts: The number of usable IP addresses in the subnet, calculated by subtracting 2 from the total hosts. The two IP addresses that are not usable are the network ID and the broadcast ID. For example, the valid hosts in the subnet with the subnet mask 255.255.255.0 is 256 - 2 = 254.
- Power of 2: The number that is a multiple of 2 and is equal to or greater than the number of required hosts or subnets. For example, the power of 2 for 12 hosts is 16, and the power of 2 for 5 subnets is 8.
- Block size: The difference between two consecutive network IDs or broadcast IDs in the same subnet. The block size is equal to the power of 2 for the number of bits in the host part. For example, the block size for the subnet mask 255.255.255.0 is 2^8 = 256.
- CIDR: Classless Inter-Domain Routing, a notation that combines the IP address and the subnet mask into one expression. The CIDR notation consists of the IP address followed by a slash and the number of bits in the network part. For example, the CIDR notation for the IP address 192.168.1.100 with the subnet mask 255.255.255.0 is 192.168.1.100/24.

The steps to perform subnetting are as follows:

1. Determine the number of required subnets and hosts per subnet.
2. Choose a suitable subnet mask that can accommodate the required subnets and hosts. The subnet mask should have enough bits in the network part to create the subnets and enough bits in the host part to assign the hosts. The subnet mask can be chosen from the following table:

| Subnet mask | Slash notation | Bits for network | Bits for host | Total hosts | Valid hosts