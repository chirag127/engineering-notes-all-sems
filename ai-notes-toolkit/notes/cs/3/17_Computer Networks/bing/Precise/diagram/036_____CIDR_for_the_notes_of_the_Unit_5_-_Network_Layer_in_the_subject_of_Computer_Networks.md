### CIDR (Classless Inter-Domain Routing)

CIDR is a method for allocating IP addresses and routing Internet Protocol packets. It was introduced in 1993 to replace the previous classful network addressing architecture and to slow the growth of routing tables on routers across the Internet.

Here are some key points to remember about CIDR:

- CIDR notation is used to represent an IP address and its associated routing prefix. It is written as the IP address, followed by a forward slash, and then the number of bits in the routing prefix. For example, `192.168.1.0/24` represents the IPv4 address `192.168.1.0` with a 24-bit routing prefix.

- CIDR allows for more efficient use of IP address space by allowing for variable-length subnet masks. This means that a network can be divided into subnets of different sizes, rather than being limited to the fixed sizes determined by the classful addressing system.

- CIDR also helps to reduce the size of routing tables by allowing for route aggregation. This means that multiple routes to networks with the same routing prefix can be combined into a single route, reducing the number of entries in the routing table.

- CIDR is an important concept to understand when working with IP networks, as it is widely used in both IPv4 and IPv6 addressing and routing.