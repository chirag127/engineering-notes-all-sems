### TCP over Wireless for the Notes of Unit 2 - Wireless Networking, Wireless LAN Overview: MAC issues, IEEE 802.11, Blue Tooth, Wireless in the Subject of Mobile Computing

TCP (Transmission Control Protocol) is a reliable transport protocol widely used in wired networks. However, the reliability of TCP over wireless networks is a major concern due to the inherent characteristics of wireless communication. In this section, we will discuss TCP over wireless and its challenges.

#### Challenges of TCP over Wireless
- **Packet Loss:** Wireless networks are prone to packet loss due to interference, fading, and noise. Packet loss can cause retransmission, delay, and reduced throughput.
- **Delay and Jitter:** Wireless networks suffer from delay and jitter due to varying transmission times and queuing delays. Delay and jitter can affect the performance of TCP congestion control mechanisms.
- **Handover:** In mobile networks, handover can cause interruptions and delay in TCP connections. Handover occurs when a mobile device moves from one access point to another, and the new access point may have a different network configuration.
- **Congestion Control:** TCP congestion control mechanisms assume that packet loss is due to network congestion. However, in wireless networks, packet loss can occur due to other reasons such as interference and fading. TCP congestion control can cause unnecessary retransmissions and reduced throughput.

#### Solutions for TCP over Wireless
- **Packet Loss Recovery:** To recover from packet loss, TCP uses retransmission and congestion control mechanisms. However, in wireless networks, retransmission can cause additional delay and congestion. To reduce the impact of retransmission, TCP variants such as TCP Vegas and TCP Westwood use techniques such as fast recovery and selective acknowledgment (SACK).
- **Delay and Jitter Control:** To control delay and jitter in wireless networks, TCP variants such as TCP New Reno and TCP BIC use techniques such as Explicit Congestion Notification (ECN) and Hybrid Slow Start (HSS). ECN allows routers to notify the sender about congestion before packet loss occurs, while HSS allows the sender to adjust its congestion window based on the network conditions.
- **Handover Management:** To manage handover in mobile networks, TCP variants such as Mobile TCP (M-TCP) and Fast-handover TCP (F-TCP) use techniques such as context transfer and pre-handover buffering. Context transfer allows the mobile device to transfer its TCP context to the new access point, while pre-handover buffering allows the new access point to buffer packets before the handover occurs.
- **Congestion Control Adaptation:** To adapt TCP congestion control to wireless networks, TCP variants such as TCP Westwood+ and TCP Hybla use techniques such as window adjustment and loss differentiation. Window adjustment allows the sender to adjust its congestion window based on the wireless conditions, while loss differentiation allows the sender to distinguish between congestion loss and other types of loss.

#### Mnemonic:
To remember the challenges and solutions of TCP over wireless, use the mnemonic "PDHC" (Packet Loss, Delay, Handover, Congestion) and "PDDC" (Packet Loss Recovery, Delay and Jitter Control, Handover Management, Congestion Control Adaptation).

In conclusion, TCP over wireless is a challenging topic due to the unique characteristics of wireless communication. However, various TCP variants have been proposed to address the challenges and improve the performance of TCP over wireless networks.