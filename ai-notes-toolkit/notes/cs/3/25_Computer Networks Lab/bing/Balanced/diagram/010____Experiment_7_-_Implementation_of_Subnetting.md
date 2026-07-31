## Experiment 7 - Implementation of Subnetting

### Objective
- To understand the concept of subnetting and its benefits.
- To learn how to divide a network into smaller subnets using subnet masks.
- To practice subnetting calculations and address assignments.

### Theory
- Subnetting is a technique of dividing a large network into smaller subnets, each with its own range of IP addresses and network parameters.
- Subnetting reduces network congestion, improves security, and simplifies network management.
- Subnetting involves applying a subnet mask to an IP address, which determines how many bits are used for the network ID and how many bits are used for the host ID.
- The subnet mask is a 32-bit binary number that has 1s in the network ID portion and 0s in the host ID portion. For example, 255.255.255.0 is a subnet mask that divides an IP address into 24 bits for the network ID and 8 bits for the host ID.
- The subnet mask can also be written in dotted decimal notation or in slash notation. For example, 255.255.255.0 is equivalent to /24.
- To calculate the number of subnets and hosts per subnet, the following formulas can be used:

  - Number of subnets = 2^n, where n is the number of bits borrowed from the host ID portion of the subnet mask.
  - Number of hosts per subnet = 2^m - 2, where m is the number of bits remaining in the host ID portion of the subnet mask. The -2 is to account for the network address and the broadcast address, which cannot be assigned to hosts.

- To assign IP addresses to subnets, the following steps can be followed:

  - Identify the network address and the broadcast address of the original network. The network address is the lowest IP address in the range, and the broadcast address is the highest IP address in the range. For example, if the original network is 192.168.1.0/24, then the network address is 192.168.1.0 and the broadcast address is 192.168.1.255.
  - Determine the subnet mask and the number of subnets and hosts per subnet. For example, if the subnet mask is 255.255.255.192, then the number of subnets is 2^2 = 4 and the number of hosts per subnet is 2^6 - 2 = 62.
  - Divide the original network into subnets by incrementing the network address by the number of hosts per subnet. For example, the first subnet will have the network address 192.168.1.0 and the broadcast address 192.168.1.63, the second subnet will have the network address 192.168.1.64 and the broadcast address 192.168.1.127, and so on.
  - Assign IP addresses to hosts within each subnet. For example, the first host in the first subnet can have the IP address 192.168.1.1, the second host can have the IP address 192.168.1.2, and so on. The last host in the first subnet can have the IP address 192.168.1.62. The same logic applies to the other subnets.

### Procedure
- To implement subnetting in a network, the following steps can be followed:

  - Design a network topology that consists of routers, switches, and hosts. For example, a network topology can have two routers, four switches, and eight hosts.
  - Configure the routers with the appropriate IP addresses and subnet masks for their interfaces. For example, the first router can have the IP address 192.168.1.1/26 for its first interface and 192.168.1.65/26 for its second interface. The second router can have the IP address 192.168.1.129/26 for its first interface and 192.168.1.193/26 for its second interface.
  - Configure the switches with the appropriate IP addresses and subnet masks for their management interfaces. For example, the first switch can have the IP address 192.168.1.2/26, the second switch can have the IP address 192.168.1.66/26, and so on.
  - Configure the hosts with the appropriate IP addresses and subnet masks for their network interfaces. For example, the first host can have the IP address 192.168.1.3/26, the second host can have the IP address 192.168.1.4/26, and so on.
  - Verify the connectivity between the hosts and the routers using ping commands