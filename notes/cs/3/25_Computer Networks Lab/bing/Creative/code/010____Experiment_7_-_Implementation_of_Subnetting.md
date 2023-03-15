## Experiment 7 - Implementation of Subnetting

- Subnetting is a technique of dividing a network into smaller subnetworks, each with its own range of IP addresses and subnet mask.
- Subnetting can improve network performance, security, and scalability by reducing the size of the broadcast domain and the routing table.
- Subnetting can be done by borrowing bits from the host portion of an IP address and using them to create subnets.
- The number of subnets and hosts per subnet depends on the subnet mask, which is a 32-bit binary number that indicates which bits of the IP address belong to the network and which belong to the host.
- The subnet mask can be written in dotted decimal notation, such as 255.255.255.0, or in slash notation, such as /24, which indicates the number of network bits.
- To calculate the number of subnets and hosts per subnet, the following formulas can be used:

  - Number of subnets = 2^n, where n is the number of borrowed bits
  - Number of hosts per subnet = 2^m - 2, where m is the number of remaining host bits
  - For example, if the subnet mask is 255.255.255.192 or /26, then n = 2 and m = 6, so the number of subnets is 2^2 = 4 and the number of hosts per subnet is 2^6 - 2 = 62.

- To find the subnet address, host address, and broadcast address of a given IP address and subnet mask, the following steps can be followed:

  - Convert the IP address and subnet mask to binary.
  - Perform a bitwise AND operation between the IP address and subnet mask to get the subnet address.
  - To get the host address, replace the network bits with zeros and the host bits with the corresponding bits of the IP address.
  - To get the broadcast address, replace the network bits with ones and the host bits with the corresponding bits of the IP address.
  - Convert the binary addresses back to dotted decimal notation.
  - For example, if the IP address is 192.168.1.100 and the subnet mask is 255.255.255.192 or /26, then the subnet address, host address, and broadcast address are:

    - Subnet address: 192.168.1.64
    - Host address: 192.168.1.100
    - Broadcast address: 192.168.1.127