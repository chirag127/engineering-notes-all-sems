 Here is the content in markdown format for the topic ## Experiment 7 - Implementation of Subnetting:

## Experiment 7 - Implementation of Subnetting

- Subnetting is a technique of dividing a large network into smaller subnetworks to minimize congestion and improve performance.
- It helps in optimizing the use of available IP addresses and provides security and flexibility in network design.
- The subnet mask is used to divide the network address into subnet address and host address.
- To implement subnetting, follow the below steps:

1. Determine the number of subnets and hosts required. This will decide the subnet mask to be used.
2. Calculate the subnet mask using the formula: 2^n - 2 where n is the number of bits required for subnet.
3. Calculate the subnet address by performing AND operation on the IP address and subnet mask.
4. Calculate the broadcast address for each subnet by changing all host bits to 1 in the subnet mask and performing OR operation with subnet address.
5. Calculate the range of host addresses for each subnet by subtracting subnet address and broadcast address and incrementing by 1.

- Examples:

Subnet Mask	Number of Subnets	Number of Hosts
255.255.255.0	1	254
255.255.254.0	2	126
255.255.252.0	4	62

Advantages:
- Optimizes the use of IP addresses
- Provides security through segmentation
- Flexibility in network design

Disadvantages:
- Extra administration required for subnet management
- Complex subnet calculations

Applications:
- In large networks to minimize congestion
- In network with varying requirements of subnets and hosts
- For providing Internet access to an organization through a single external IP

[Detailed diagrams and examples can be added if required]