## Experiment 7 - Implementation of Subnetting

- Subnetting is a technique of dividing a network into smaller logical subnetworks, each with its own range of IP addresses and network prefix.
- Subnetting can improve network performance, security, and scalability by reducing the size of the broadcast domain and the routing table.
- Subnetting requires a network mask, which is a binary number that indicates which bits of the IP address belong to the network prefix and which bits belong to the host identifier.
- The network mask can be expressed in dotted decimal notation (e.g., 255.255.255.0) or in slash notation (e.g., /24).
- To perform subnetting, the network administrator can borrow some bits from the host identifier and use them to create subnetwork identifiers. The number of subnets and hosts per subnet depends on how many bits are borrowed.
- The formula for calculating the number of subnets is 2^n, where n is the number of borrowed bits. The formula for calculating the number of hosts per subnet is 2^(32-n-m)-2, where n is the number of borrowed bits and m is the number of network prefix bits.
- To find the subnet address, the network mask is bitwise ANDed with the IP address. To find the broadcast address, the network mask is bitwise inverted and then bitwise ORed with the IP address.
- To find the valid host range, the subnet address is incremented by one and the broadcast address is decremented by one. The first and last addresses in the range are the valid host addresses.
- An example of subnetting is given below:

  - Given a network address of 192.168.1.0/24 and a requirement of 4 subnets, the network mask can be changed to 255.255.255.192 or /26 by borrowing 2 bits from the host identifier.
  - The number of subnets is 2^2 = 4 and the number of hosts per subnet is 2^(32-26-8)-2 = 62.
  - The subnet addresses are 192.168.1.0, 192.168.1.64, 192.168.1.128, and 192.168.1.192.
  - The broadcast addresses are 192.168.1.63, 192.168.1.127, 192.168.1.191, and 192.168.1.255.
  - The valid host ranges are 192.168.1.1-192.168.1.62, 192.168.1.65-192.168.1.126, 192.168.1.129-192.168.1.190, and 192.168.1.193-192.168.1.254.