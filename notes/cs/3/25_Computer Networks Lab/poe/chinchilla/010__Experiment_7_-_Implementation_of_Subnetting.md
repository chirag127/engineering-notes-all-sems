## Experiment 7 - Implementation of Subnetting

In this experiment, we will learn about subnetting, which is the process of dividing a network into smaller subnetworks. Subnetting is commonly used in large networks to improve performance and manageability. By dividing a network into smaller subnetworks, we can reduce broadcast traffic, increase network security, and improve network efficiency.

To implement subnetting, we need to follow these steps:

1. Determine the network requirements: Before subnetting a network, we need to determine the network requirements, such as the number of hosts required, the network topology, and the network address range.

2. Choose a subnet mask: The subnet mask is used to divide the network into smaller subnetworks. We need to choose a subnet mask that will provide enough IP addresses for the network while still allowing room for growth.

3. Divide the network into subnets: Once we have chosen a subnet mask, we can divide the network into smaller subnets. Each subnet will have its own network address and broadcast address.

4. Assign IP addresses: After dividing the network into subnets, we need to assign IP addresses to each device on the network. Each device will be assigned an IP address within its subnet.

5. Test the network: After implementing subnetting, we need to test the network to ensure that it is working correctly. We can use tools such as ping and traceroute to test network connectivity.

Some important concepts related to subnetting are:

- Subnet mask: The subnet mask is a 32-bit number that is used to divide the network into subnets. It is represented in dotted decimal notation, such as 255.255.255.0.

- Network address: The network address is the first IP address in a subnet. It is used to identify the subnet and is the address that is used for routing.

- Broadcast address: The broadcast address is the last IP address in a subnet. It is used to send broadcast messages to all devices on the subnet.

- Host address: The host address is the IP address assigned to a device on the network. It is unique within its subnet.

- CIDR notation: CIDR notation is a compact representation of a subnet mask. It is represented as a slash followed by the number of bits in the subnet mask, such as /24.

In conclusion, subnetting is a powerful tool for managing large networks. By dividing a network into smaller subnets, we can improve network performance and manageability. To implement subnetting, we need to follow a set of steps that include determining network requirements, choosing a subnet mask, dividing the network into subnets, assigning IP addresses, and testing the network. Understanding the key concepts related to subnetting, such as subnet masks, network addresses, and host addresses, is also important.