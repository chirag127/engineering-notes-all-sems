### CIDR for the notes of the Unit 5 - Network Layer in the subject of Computer Networks

- CIDR stands for Classless Inter-Domain Routing .
- CIDR is a method for assigning IP addresses and for IP routing.
- CIDR does not use the standard IP address classes like Class A, B or C.
- CIDR allows for a more efficient allocation of IP addresses than the older method of classful addressing .
- CIDR is based on variable-length subnet masking (VLSM), which enables network engineers to divide an IP address space into a hierarchy of subnets of different sizes.
- CIDR addresses are made up of two sets of numbers: prefix and suffix.
- The prefix is the network portion of the IP address and indicates how many bits are used for the network ID .
- The suffix is the host portion of the IP address and indicates how many bits are used for the host ID .
- CIDR notation uses a slash (/) to separate the prefix and the suffix, and indicates the number of bits in the prefix .
- For example, 192.168.1.0/24 means that the prefix is 192.168.1.0 and the suffix is 24 bits long, which means that the network ID is the first 24 bits of the IP address and the host ID is the remaining 8 bits .
- CIDR notation can also be used to specify a range of IP addresses that belong to the same network or subnet .
- For example, 192.168.1.0/25 means that the network ID is the first 25 bits of the IP address and the host ID is the remaining 7 bits, which means that the IP addresses from 192.168.1.0 to 192.168.1.127 belong to the same subnet .
- CIDR notation can also be used to aggregate multiple contiguous subnets into a single routing entry, which reduces the size of routing tables and improves the efficiency of routing .
- For example, 192.168.0.0/16 means that the network ID is the first 16 bits of the IP address and the host ID is the remaining 16 bits, which means that the IP addresses from 192.168.0.0 to 192.168.255.255 belong to the same network and can be represented by a single routing entry .