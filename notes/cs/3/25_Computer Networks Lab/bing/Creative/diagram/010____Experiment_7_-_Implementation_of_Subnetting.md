## Experiment 7 - Implementation of Subnetting

- Subnetting is a technique of dividing a network into smaller subnetworks, each with its own range of IP addresses and subnet mask.
- Subnetting can improve network performance, security, and scalability by reducing the size of the broadcast domain and the routing table.
- Subnetting can be done by borrowing bits from the host portion of an IP address and using them to create subnets.
- The number of subnets and hosts per subnet depends on the subnet mask, which is a 32-bit binary number that indicates which bits of the IP address belong to the network and which belong to the host.
- The subnet mask can be written in dotted decimal notation, such as 255.255.255.0, or in slash notation, such as /24, which indicates the number of bits in the network portion of the IP address.
- To calculate the number of subnets and hosts per subnet, the following formulas can be used:

  - Number of subnets = 2^n, where n is the number of borrowed bits
  - Number of hosts per subnet = 2^m - 2, where m is the number of remaining bits in the host portion
  - For example, if the IP address is 192.168.1.0/24 and the subnet mask is 255.255.255.192 (/26), then:

    - Number of borrowed bits = 26 - 24 = 2
    - Number of subnets = 2^2 = 4
    - Number of remaining bits = 32 - 26 = 6
    - Number of hosts per subnet = 2^6 - 2 = 62

- To assign IP addresses to subnets, the following steps can be followed:

  - Identify the network address and the broadcast address of the original network. The network address is the lowest IP address in the range, and the broadcast address is the highest IP address in the range. For example, if the IP address is 192.168.1.0/24, then the network address is 192.168.1.0 and the broadcast address is 192.168.1.255.
  - Identify the subnet size, which is the number of IP addresses in each subnet. The subnet size can be calculated by adding 1 to the number of hosts per subnet. For example, if the number of hosts per subnet is 62, then the subnet size is 62 + 1 = 63.
  - Identify the subnet increment, which is the value that is added to the network address to get the next subnet. The subnet increment can be calculated by subtracting the subnet size from 256. For example, if the subnet size is 63, then the subnet increment is 256 - 63 = 193.
  - Assign IP addresses to subnets by adding the subnet increment to the network address. The first subnet will have the same network address as the original network, and the last subnet will have the same broadcast address as the original network. For example, if the network address is 192.168.1.0 and the subnet increment is 193, then the subnets will be:

    - Subnet 1: 192.168.1.0 - 192.168.1.62
    - Subnet 2: 192.168.1.64 - 192.168.1.126
    - Subnet 3: 192.168.1.128 - 192.168.1.190
    - Subnet 4: 192.168.1.192 - 192.168.1.254

- To verify the subnetting, the following steps can be followed:

  - Use the ping command to test the connectivity between hosts in the same subnet and in different subnets. For example, ping 192.168.1.1 from 192.168.1.2 (same subnet) and from 192.168.1.65 (different subnet).
  - Use the ipconfig command to check the IP address and the subnet mask of each host. For example, ipconfig /all on 192.168.1.1 should show 192.168.1.1 as the IP address and 255.255.255.192 as the subnet mask.
  - Use the tracert command to check the route taken by packets from one host to another. For example, tracert 192.168.1.65 from 192.168.1.1 should show the hops between the hosts and the IP addresses of the routers.