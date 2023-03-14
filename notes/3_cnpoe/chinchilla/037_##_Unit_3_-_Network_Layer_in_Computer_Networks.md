## Unit 3 - Network Layer in Computer Networks

The network layer is an essential component of computer networks that provides logical addressing, routing, and forwarding of data packets between different networks. It plays a crucial role in ensuring the smooth and efficient functioning of the internet and other large-scale networks. In this unit, we will cover the following topics related to the network layer:

### 1. Network Layer Functions
- Logical addressing: The network layer provides unique logical addresses to every device on the network, which helps in identifying the source and destination of data packets.
- Routing: The network layer determines the best path for data packets to travel from the source to the destination based on network topology, congestion, and other factors.
- Fragmentation and reassembly: The network layer breaks the data packets into smaller units for transmission and reassembles them at the destination.
- Congestion control: The network layer monitors the network traffic and takes measures to prevent congestion, such as slowing down the rate of transmission.

### 2. Internet Protocol (IP)
- IP is the most widely used protocol in the network layer of the internet and other networks.
- It provides logical addressing through IP addresses, which are 32-bit numbers assigned to each device on the network.
- IP packets contain the source and destination IP addresses, as well as other information such as packet length, time-to-live (TTL), and protocol type.

### 3. Routing Algorithms
- There are various routing algorithms used in the network layer, such as shortest path routing, flooding, and distance vector routing.
- Shortest path routing algorithms determine the best path for data packets based on the shortest distance between the source and destination.
- Flooding sends data packets to all devices on the network, which can be inefficient but useful in some scenarios.
- Distance vector routing algorithms use a distributed algorithm to determine the best path for data packets based on hop count.

### 4. Network Address Translation (NAT)
- NAT is a technique used in the network layer to allow devices on a local network to share a single IP address when communicating with devices on the internet.
- NAT modifies the source IP address of data packets as they leave the local network and replaces it with the public IP address of the NAT device.
- NAT helps conserve IP address space and provides an additional layer of security for local networks.

### 5. Quality of Service (QoS)
- QoS is a set of techniques used in the network layer to prioritize certain types of traffic, such as voice or video, over others.
- QoS can be used to ensure that critical applications receive sufficient bandwidth and minimize delays and packet loss.
- QoS mechanisms include traffic shaping, packet scheduling, and admission control.

### Mnemonic and Learning Trick
- To remember the functions of the network layer, use the mnemonic "LRFC" - Logical addressing, Routing, Fragmentation and reassembly, Congestion control.
- To remember the types of routing algorithms, use the mnemonic "SFD" - Shortest path routing, Flooding, Distance vector routing.