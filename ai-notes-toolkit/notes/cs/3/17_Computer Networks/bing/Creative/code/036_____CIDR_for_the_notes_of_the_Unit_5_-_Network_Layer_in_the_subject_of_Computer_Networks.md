# CIDR for the notes of the Unit 5 - Network Layer in the subject of Computer Networks

- CIDR stands for Classless Inter-Domain Routing .
- It is a method for assigning IP addresses and for IP routing.
- It does not use the standard IP address classes like Class A, Class B or Class C.
- It is based on variable-length subnet masking (VLSM), which enables network engineers to divide an IP address space into a hierarchy of subnets of different sizes.
- It allows for a more efficient allocation of IP addresses and reduces the size of routing tables .
- It uses a notation called CIDR notation to represent an IP address and its associated network prefix.
- CIDR notation consists of two sets of numbers separated by a slash: the IP address and the prefix length.
- The prefix length indicates the number of significant bits that make up the routing or networking portion of the IP address.
- For example, 192.168.1.0/24 means that the first 24 bits of the IP address are used for the network prefix and the remaining 8 bits are used for the host identifier.
- The network prefix can be used to identify the network or subnet that the IP address belongs to.
- The host identifier can be used to identify the specific device or interface within the network or subnet.
- CIDR notation can also be used to aggregate multiple contiguous subnets into a single routing entry, which is called supernetting or route summarization .
- For example, 192.168.0.0/16 can be used to represent the network that contains all the subnets from 192.168.0.0/24 to 192.168.255.0/24.
- CIDR was introduced in 1993 to replace the previous classful network addressing architecture on the Internet, which was inefficient and wasteful of IP addresses .
- CIDR is widely used in modern IP networks and is supported by most network devices and protocols.