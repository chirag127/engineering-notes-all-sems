### TCP over wireless for the notes of the Unit 2 - Wireless Networking, Wireless LAN Overview: MAC issues, IEEE 802.11, Blue Tooth, Wireless in the subject of Mobile Computing

Transmission Control Protocol (TCP) is a connection-oriented protocol that ensures reliable and orderly data delivery between two devices over a network. However, TCP over wireless networks, such as Wireless LAN (WLAN), can be challenging due to various factors that affect the quality of the wireless link. Here are some important points to consider when dealing with TCP over wireless:

1. **Packet Loss:** Wireless networks are prone to packet loss due to interference, signal attenuation, and other factors. TCP relies on the receipt of acknowledgement packets (ACKs) to ensure reliable data delivery. If an ACK is not received, TCP assumes that the packet was lost and retransmits it. However, in wireless networks, packet loss can be more frequent, leading to unnecessary retransmissions and congestion.

2. **Latency:** Latency is the delay between sending a packet and receiving its corresponding ACK. In wireless networks, latency can be higher due to the time it takes for the signal to travel through the air and the processing time at the receiver. TCP's congestion control algorithm assumes that a high latency is an indication of network congestion and reduces the sending rate. However, in wireless networks, high latency may not always be an indication of congestion.

3. **Bandwidth:** Wireless networks have limited bandwidth compared to wired networks. TCP's congestion control algorithm adjusts the sending rate based on the available bandwidth. However, in wireless networks, the available bandwidth can fluctuate due to interference and other factors, leading to underutilization of the network.

To overcome these challenges, various techniques have been developed for TCP over wireless networks, such as:

1. **TCP Vegas:** TCP Vegas is a modification of TCP that uses latency as an indicator of network congestion rather than packet loss. This approach reduces unnecessary retransmissions and improves throughput in wireless networks.

2. **TCP Westwood:** TCP Westwood is a modification of TCP that uses a bandwidth estimation algorithm to adjust the sending rate based on the available bandwidth. This approach improves the utilization of the network in wireless environments.

3. **TCP Hybla:** TCP Hybla is a modification of TCP that adjusts the sending rate based on the round-trip time (RTT) of the packets. This approach improves the performance of TCP over wireless networks with high latency.

In conclusion, TCP over wireless networks can be challenging due to packet loss, latency, and limited bandwidth. However, various techniques have been developed to improve the performance of TCP in wireless environments. Understanding these techniques can help in designing and optimizing wireless networks for reliable and efficient data delivery.