### TCP over Wireless

TCP (Transmission Control Protocol) is a widely used transport layer protocol that provides reliable, connection-oriented communication between two devices. TCP is designed to work over wired networks, where packet loss is mainly due to congestion. However, when TCP is used over wireless networks, the performance of the protocol can be significantly degraded due to the characteristics of wireless networks, such as high bit error rates, frequent disconnections, and handoffs.

Here are some points to consider when using TCP over wireless networks:

1. **Packet Loss**: In wireless networks, packet loss can occur due to various reasons such as interference, fading, and handoffs. TCP interprets packet loss as a sign of congestion and reduces its sending rate, which can result in unnecessary throughput degradation.

2. **Disconnections**: Wireless networks are prone to frequent disconnections due to mobility, interference, and limited coverage. When a disconnection occurs, TCP times out and enters the retransmission phase, which can result in long delays and reduced throughput.

3. **Handoffs**: When a mobile device moves from one base station to another, a handoff occurs. During a handoff, the connection may be temporarily lost, which can result in packet loss and delay. TCP may interpret this as congestion and reduce its sending rate, resulting in reduced throughput.

To address these issues, several enhancements to TCP have been proposed for use over wireless networks. These enhancements include:

1. **Snoop Protocol**: The snoop protocol is a link-layer protocol that caches packets at the base station and retransmits lost packets locally, without involving the sender. This can reduce the delay and improve the throughput of TCP over wireless networks.

2. **Indirect TCP**: Indirect TCP (I-TCP) splits the TCP connection into two separate connections: one between the mobile device and the base station, and another between the base station and the destination. The base station acts as a proxy and handles the wireless part of the connection, while the destination handles the wired part. This can improve the performance of TCP over wireless networks by isolating the wireless part of the connection.

3. **Mobile TCP**: Mobile TCP (M-TCP) is an enhancement to TCP that detects disconnections and handoffs and freezes the TCP state until the connection is re-established. This can prevent unnecessary retransmissions and improve the performance of TCP over wireless networks.

These are some of the key points to consider when using TCP over wireless networks. By understanding the challenges and using appropriate enhancements, the performance of TCP over wireless networks can be significantly improved.