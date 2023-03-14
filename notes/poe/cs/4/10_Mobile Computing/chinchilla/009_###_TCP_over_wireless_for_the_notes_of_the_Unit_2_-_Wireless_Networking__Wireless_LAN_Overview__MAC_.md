### TCP over Wireless

TCP (Transmission Control Protocol) is a widely used protocol for reliable data transmission over wired networks. However, when it comes to wireless networks, TCP faces some unique challenges due to the unpredictable nature of wireless communication. In this section, we will discuss some of the issues related to TCP over wireless networks and how they can be addressed.

#### Challenges with TCP over Wireless

1. **Packet Loss:** Wireless networks are prone to packet loss due to interference, signal attenuation, and other factors. When a packet is lost, TCP assumes that it is due to congestion and reduces its congestion window, causing a decrease in throughput.

2. **Delay:** Wireless networks have higher delay compared to wired networks due to factors such as propagation delay, processing delay, and queuing delay. This can cause TCP to timeout and retransmit packets unnecessarily.

3. **Jitter:** Jitter refers to the variation in delay between packets. In wireless networks, jitter can be high due to the variable nature of wireless communication, which can cause TCP to interpret jitter as congestion and reduce its congestion window.

4. **Limited Bandwidth:** Wireless networks typically have lower bandwidth compared to wired networks, which can cause congestion and reduce TCP throughput.

#### Solutions for TCP over Wireless

1. **TCP Variants:** There are several TCP variants that are designed specifically for wireless networks, such as TCP Vegas, TCP Westwood, and TCP NewReno. These variants use different congestion control mechanisms to address the challenges of wireless networks.

2. **Packet Loss Recovery:** To address packet loss, TCP uses mechanisms such as selective acknowledgments (SACK) and fast retransmit to recover lost packets without waiting for a timeout.

3. **Delayed ACKs:** Delayed acknowledgments can reduce the number of packets sent over the wireless network by combining multiple acknowledgments into a single packet.

4. **Window Scaling:** TCP window scaling allows for larger congestion windows, which can improve throughput in wireless networks with high bandwidth delays.

5. **Buffer Management:** Proper buffer management can help reduce packet loss and improve TCP performance in wireless networks.

6. **Link Layer Retransmissions:** Some wireless technologies, such as IEEE 802.11, provide link layer retransmissions, which can help reduce packet loss and improve TCP performance.

#### Mnemonic

To remember the challenges and solutions for TCP over wireless, you can use the mnemonic "LPD BWV" which stands for:

1. **L**oss
2. **P**acket Delay
3. **D**elayed ACKs
4. **B**andwidth
5. **W**indow Scaling
6. **V**ariants

#### Conclusion

TCP is a widely used protocol for reliable data transmission over wired networks. However, when it comes to wireless networks, TCP faces some unique challenges. By using TCP variants, packet loss recovery mechanisms, delayed ACKs, window scaling, buffer management, and link layer retransmissions, these challenges can be addressed to improve TCP performance in wireless networks.