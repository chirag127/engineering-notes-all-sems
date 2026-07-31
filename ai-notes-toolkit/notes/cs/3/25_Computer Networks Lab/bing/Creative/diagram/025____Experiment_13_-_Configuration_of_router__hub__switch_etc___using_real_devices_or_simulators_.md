## Experiment 13 - Configuration of router, hub, switch etc. (using real devices or simulators)

In this experiment, you will learn how to configure a router, a hub, and a switch for a simple network topology. You will also learn the differences between these devices and their roles in a network.

### Objectives

- To understand the functions and features of a router, a hub, and a switch.
- To configure a router with basic settings such as IP address, subnet mask, default gateway, and routing table.
- To connect a hub and a switch to a router and verify the connectivity between different devices.
- To observe the traffic flow and packet forwarding behavior of a router, a hub, and a switch.

### Requirements

- A router with at least two Ethernet interfaces and a console port.
- A hub with at least four ports.
- A switch with at least four ports.
- A PC or a laptop with a terminal emulator software such as PuTTY or HyperTerminal.
- An Ethernet cable for each device.
- A console cable for the router.

### Procedure

1. Connect the router to the PC or laptop using the console cable. Launch the terminal emulator software and configure the serial port settings as follows: baud rate 9600, data bits 8, parity none, stop bits 1, and flow control none.
2. Power on the router and press Enter to access the user mode. Enter the command `enable` to enter the privileged mode. Enter the command `configure terminal` to enter the global configuration mode.
3. Assign an IP address and a subnet mask to each interface of the router using the command `ip address <ip-address> <subnet-mask>`. For example, to assign the IP address 192.168.1.1 and the subnet mask 255.255.255.0 to the interface FastEthernet 0/0, enter the command `ip address 192.168.1.1 255.255.255.0`.
4. Assign a default gateway to the router using the command `ip default-gateway <ip-address>`. For example, to assign the IP address 192.168.1.254 as the default gateway, enter the command `ip default-gateway 192.168.1.254`.
5. Configure the routing table of the router using the command `ip route <destination-network> <subnet-mask> <next-hop-address>`. For example, to add a route for the network 192.168.2.0/24 with the next hop address 192.168.1.2, enter the command `ip route 192.168.2.0 255.255.255.0 192.168.1.2`.
6. Exit the global configuration mode and save the configuration using the command `copy running-config startup-config`.
7. Connect the hub to the router using an Ethernet cable. Connect one port of the hub to the interface FastEthernet 0/0 of the router.
8. Connect the switch to the router using an Ethernet cable. Connect one port of the switch to the interface FastEthernet 0/1 of the router.
9. Connect other devices such as PCs or laptops to the hub and the switch using Ethernet cables. Assign IP addresses and subnet masks to each device according to the network topology. For example, to assign the IP address 192.168.1.10 and the subnet mask 255.255.255.0 to a PC connected to the hub, enter the command `ipconfig /set address "Local Area Connection" static 192.168.1.10 255.255.255.0` in the command prompt.
10. Verify the connectivity between different devices using the command `ping <ip-address>`. For example, to ping the router from a PC connected to the hub, enter the command `ping 192.168.1.1` in the command prompt. You should see a reply from the router if the connection is successful.
11. Observe the traffic flow and packet forwarding behavior of the router, the hub, and the switch using a network analyzer software such as Wireshark or Packet Tracer. You can capture the packets on the devices or on the links between them. You can also filter the packets by protocol, source, destination, or port.

### Results and Analysis

- A router is a device that connects different networks and forwards packets based on their destination IP addresses. A router has a routing table that contains the information about the routes to different networks. A router can perform network address translation (NAT), firewall, and other functions.
-