# Experiment 7 - Implementation of Subnetting

## Objective
- To understand the concept of subnetting and its benefits.
- To learn how to divide a network into smaller subnets using subnet masks.
- To practice subnetting calculations and address assignments.

## Theory
- Subnetting is a technique of dividing a large network into smaller subnets, each with its own range of IP addresses and network parameters.
- Subnetting allows efficient use of IP address space, reduces network congestion, improves security and performance, and simplifies network administration and troubleshooting.
- Subnetting involves applying a subnet mask to an IP address, which determines how many bits are used for the network ID and how many bits are used for the host ID.
- The subnet mask is a 32-bit binary number that has 1s in the network ID portion and 0s in the host ID portion. For example, 255.255.255.0 is a subnet mask that indicates that the first 24 bits are used for the network ID and the last 8 bits are used for the host ID.
- The subnet mask can also be written in slash notation, which indicates the number of 1s in the subnet mask. For example, /24 is equivalent to 255.255.255.0.
- To subnet a network, the network administrator borrows some bits from the host ID portion and assigns them to the subnet ID portion. This creates more subnets, but reduces the number of hosts per subnet.
- The number of subnets and hosts per subnet can be calculated using the following formulas:

  - Number of subnets = 2^n, where n is the number of borrowed bits.
  - Number of hosts per subnet = 2^m - 2, where m is the number of remaining bits in the host ID portion. The -2 accounts for the network address and the broadcast address, which cannot be assigned to hosts.

- To assign IP addresses to subnets, the network administrator follows these steps:

  - Choose a subnet mask that meets the requirements of the network.
  - Identify the network address of the original network by performing a bitwise AND operation between the IP address and the subnet mask.
  - Identify the subnet addresses by incrementing the subnet ID portion of the network address by one for each subnet.
  - Identify the host addresses by assigning any value between 1 and 254 to the host ID portion of the subnet address. The value 0 is reserved for the network address and the value 255 is reserved for the broadcast address.
  - Identify the broadcast address of each subnet by replacing the host ID portion of the subnet address with all 1s.

## Example
- Suppose a network has an IP address of 192.168.1.0/24 and needs to be divided into four subnets, each with at least 50 hosts. How can this be done?

  - Step 1: Choose a subnet mask that meets the requirements of the network. Since we need four subnets, we need to borrow two bits from the host ID portion. This gives us a subnet mask of 255.255.255.192 or /26.
  - Step 2: Identify the network address of the original network by performing a bitwise AND operation between the IP address and the subnet mask. This gives us 192.168.1.0 as the network address.
  - Step 3: Identify the subnet addresses by incrementing the subnet ID portion of the network address by one for each subnet. This gives us the following subnet addresses:

    - Subnet 1: 192.168.1.0
    - Subnet 2: 192.168.1.64
    - Subnet 3: 192.168.1.128
    - Subnet 4: 192.168.1.192

  - Step 4: Identify the host addresses by assigning any value between 1 and 254 to the host ID portion of the subnet address. The value 0 is reserved for the network address and the value 255 is reserved for the broadcast address. This gives us the following host address ranges for each subnet:

    - Subnet 1: 192.168.1.1 to 192.168.1.62
    - Subnet 2: 192.168.1.65 to 192.168.1.126
    - Subnet 3: 192.168.1.129 to 192.168.1.190
    - Subnet 4: 192.168.1.193 to 192.168.1.254

  - Step 5: Identify the broadcast address of each subnet by replacing the host ID portion of