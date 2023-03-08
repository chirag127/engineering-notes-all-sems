### Experiment 7 - Implementation of Subnetting

Subnetting is a technique used to divide a single network into multiple smaller networks, known as subnets. This technique helps in optimizing the network, improving the performance, and simplifying network management. In this experiment, we will learn how to implement subnetting in a network.

#### Objective
The objective of this experiment is to understand the concept of subnetting and implement it in a network.

#### Requirements
- A computer with a network interface card (NIC) installed.
- Cisco Packet Tracer software.

#### Procedure
1. Open the Cisco Packet Tracer software.
2. Create a network topology with at least two routers and multiple hosts.
3. Assign IP addresses to each host.
4. Determine the subnet mask for the network.
5. Divide the network into multiple subnets using the subnet mask.
6. Assign IP addresses to each subnet.
7. Configure the routers to route traffic between subnets.
8. Test the network by pinging between hosts in different subnets.

#### Example
Suppose we have a network with the IP address range 192.168.1.0/24. This means that there are 256 IP addresses available in the network. We can divide this network into four subnets with each subnet having 64 IP addresses. The subnet masks for each subnet would be:

- Subnet 1: 192.168.1.0/26
- Subnet 2: 192.168.1.64/26
- Subnet 3: 192.168.1.128/26
- Subnet 4: 192.168.1.192/26

We can assign IP addresses to each host in each subnet using these subnet masks.

#### Advantages of Subnetting
- Improves network performance by reducing network congestion.
- Simplifies network management by dividing the network into smaller, manageable subnets.
- Enhances network security by isolating subnets and controlling access to them.

#### Disadvantages of Subnetting
- Can be complex to implement and manage.
- Requires careful planning and design to ensure optimal performance.

#### Applications
- Used in large networks to optimize performance and simplify network management.
- Used in organizations to control access to sensitive data by isolating subnets.

#### Conclusion
Subnetting is an essential technique for optimizing network performance and simplifying network management. By dividing a network into smaller subnets, we can improve performance, enhance security, and simplify network management.