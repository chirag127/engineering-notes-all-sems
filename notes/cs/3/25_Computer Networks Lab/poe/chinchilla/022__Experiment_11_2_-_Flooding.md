### Experiment 11.2 - Flooding

In the field of computer networking, flooding is a technique used for broadcasting messages to all devices within a network. This experiment aims to understand the concept of flooding and its implementation in computer networks.

#### Objectives:
- To understand the concept of flooding in computer networks.
- To implement flooding in a simple computer network.
- To observe the behavior of network devices during flooding.

#### Materials Required:
- 3 computers connected through a LAN cable
- Network simulator software (such as GNS3 or Cisco Packet Tracer)

#### Procedure:
1. Connect the 3 computers through a LAN cable to form a simple network.
2. Launch the network simulator software and open the network topology.
3. Configure the network devices with IP addresses and subnet masks.
4. Open the command prompt on all devices and execute the 'ping' command to check network connectivity.
5. Select one device as the 'source' and another device as the 'destination'.
6. On the source device, open the command prompt and execute the 'ping' command with the IP address of the destination device. 
7. Observe the behavior of the network devices during the 'ping' command execution.
8. Implement flooding by sending a message from the source device to all devices within the network.
9. Observe the behavior of the network devices during flooding.

#### Results:
- During the 'ping' command execution, the source device sends an ICMP packet to the destination device, which then responds with an ICMP reply packet.
- If the destination device is unreachable, the source device displays a timeout message.
- During flooding, the source device sends the message to all devices within the network, which then forward the message to their connected devices until all devices receive the message.
- Flooding can cause network congestion and is generally used for small networks.

#### Conclusion:
Flooding is a simple technique used for broadcasting messages to all devices within a network. It can be useful for small networks, but can cause congestion in larger networks. By implementing flooding in a simple network, we were able to observe the behavior of network devices during flooding and understand the concept of flooding in computer networks.