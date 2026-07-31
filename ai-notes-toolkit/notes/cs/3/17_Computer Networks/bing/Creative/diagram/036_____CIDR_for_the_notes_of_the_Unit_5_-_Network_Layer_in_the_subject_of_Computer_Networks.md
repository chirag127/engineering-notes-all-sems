### CIDR

- CIDR stands for **Classless Inter-Domain Routing** , which is a method for allocating IP addresses and for IP routing.
- CIDR does not use the standard IP address classes like Class A, B or C, but instead uses a **variable-length subnet mask (VLSM)** to divide an IP address space into a hierarchy of subnets of different sizes.
- CIDR allows for a more efficient allocation of IP addresses than the older method, which was by assigning organizations a class of IPs. This reduces the waste of IP addresses and the size of routing tables.
- CIDR addresses are made up of two sets of numbers: **Prefix** and **Prefix Length** . The prefix is the network portion of the IP address, and the prefix length is the number of bits that specify the network part. For example, 192.168.1.0/24 is a CIDR address, where 192.168.1.0 is the prefix and 24 is the prefix length.
- CIDR notation uses a **slash (/)** to separate the prefix and the prefix length. The prefix length can range from 0 to 32 for IPv4 addresses, and from 0 to 128 for IPv6 addresses.
- CIDR can be used to create subnets with different host counts without wasting large numbers of addresses. For example, a /24 network can be divided into four /26 subnets, each with 62 hosts, or into two /25 subnets, each with 126 hosts.
- CIDR can also be used to aggregate multiple contiguous networks into a single routing entry, which is called **supernetting** or **route summarization** . For example, four /24 networks can be aggregated into a single /22 network, which reduces the number of routing entries by four.