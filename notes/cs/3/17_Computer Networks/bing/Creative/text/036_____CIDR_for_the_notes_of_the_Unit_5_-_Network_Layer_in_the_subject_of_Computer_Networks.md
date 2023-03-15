### CIDR

- CIDR stands for **Classless Inter-Domain Routing** , which is a method for allocating IP addresses and for IP routing.
- CIDR does not use the standard IP address classes like Class A, B or C, but instead allows for a more flexible and efficient allocation of IP addresses .
- CIDR is based on **variable-length subnet masking (VLSM)**, which enables network engineers to divide an IP address space into a hierarchy of subnets of different sizes.
- CIDR addresses are made up of two sets of numbers: **Prefix** and **Prefix Length** .
- The prefix is the network portion of the IP address, which identifies the network to which the host belongs.
- The prefix length is the number of bits that make up the prefix, which indicates the size of the network.
- The prefix length is written after the prefix, separated by a slash (/), and is also called the **network mask**.
- For example, the CIDR address 192.168.1.0/24 means that the prefix is 192.168.1.0 and the prefix length is 24 bits, which means that the network has 256 possible host addresses (2^(32-24))^5^.
- CIDR notation is also used to specify the **route aggregation** or **supernetting** , which is the process of combining multiple contiguous networks into a single larger network for routing purposes.
- For example, the CIDR address 192.168.0.0/16 means that the network consists of 16 contiguous subnets, each with 256 host addresses, for a total of 4096 possible host addresses.
- CIDR was introduced in 1993 by the Internet Engineering Task Force (IETF) to replace the previous classful network addressing architecture on the Internet, which was inefficient and wasteful of IP address space.
- CIDR also allows for more efficient routing and address allocation, as well as improved security and scalability of the Internet.