# TCP over wireless

- TCP (Transmission Control Protocol) is a reliable and connection-oriented protocol that provides end-to-end data delivery over the Internet.
- TCP assumes that most packet losses are due to network congestion and responds by reducing the sending rate to avoid further losses.
- However, in wireless networks, packet losses can also occur due to wireless link errors, such as fading, shadowing, interference, and mobility.
- TCP cannot distinguish between congestion losses and wireless losses and may unnecessarily reduce the sending rate, resulting in poor performance and low throughput.
- Therefore, TCP needs to be adapted or enhanced to cope with the challenges of wireless networks, such as high delays, high error rates, variable bandwidth, and frequent handoffs.

## TCP over wireless challenges

- Wireless networks have different characteristics and challenges than wired networks, which affect the performance of TCP. Some of these challenges are:

  - **High delays**: Wireless networks may have higher propagation delays due to the long distances between the sender and the receiver, especially in satellite networks. TCP relies on timers and acknowledgments to estimate the round-trip time (RTT) and detect losses, which may be inaccurate or delayed in wireless networks. This may lead to spurious timeouts, unnecessary retransmissions, and slow recovery.

  - **High error rates**: Wireless links are prone to errors due to various factors, such as noise, interference, fading, and shadowing. TCP treats all losses as congestion losses and invokes congestion control mechanisms, such as slow start and congestion avoidance, to reduce the congestion window and the sending rate. This may result in underutilization of the available bandwidth and low throughput.

  - **Variable bandwidth**: Wireless networks may have variable bandwidth due to factors such as channel conditions, interference, and mobility. TCP uses the congestion window to control the sending rate, which is based on the assumption of a fixed bandwidth. TCP may not be able to adapt quickly to the changing bandwidth and may cause either congestion or underutilization.

  - **Frequent handoffs**: Wireless networks may involve frequent handoffs due to mobility of the nodes. Handoffs may cause temporary disconnections, packet losses, or route changes, which may affect the TCP performance. TCP may interpret these events as congestion and reduce the sending rate, or may experience long timeouts and slow recovery.

## TCP over wireless solutions

- Several solutions have been proposed to improve the performance of TCP over wireless networks. These solutions can be classified into four categories:

  - **End-to-end solutions**: These solutions modify the TCP sender or receiver to cope with wireless losses without involving the intermediate nodes. For example, TCP selective acknowledgment (SACK) allows the receiver to report multiple non-contiguous segments that have been received, which can help the sender to avoid unnecessary retransmissions. TCP Vegas is another example that uses the RTT variation to detect congestion instead of packet losses.

  - **Link-layer solutions**: These solutions enhance the link layer protocols to provide local reliability and error recovery over the wireless links, without modifying the TCP layer. For example, automatic repeat request (ARQ) is a technique that uses acknowledgments and retransmissions at the link layer to ensure reliable delivery of packets. Forward error correction (FEC) is another technique that adds redundant bits to the packets to correct errors at the receiver without retransmissions.

  - **Split-connection solutions**: These solutions split the TCP connection into two sub-connections: one over the wired network and one over the wireless network. The intermediate node, such as the base station, acts as a proxy that terminates the TCP connection from the sender and initiates a new TCP connection to the receiver. The proxy can use different TCP variants or parameters for each sub-connection and can perform local error recovery over the wireless link.

  - **Cross-layer solutions**: These solutions exploit the interactions and information exchange between different layers of the network stack to optimize the TCP performance over wireless networks. For example, TCP feedback (TCP-F) is a technique that uses the feedback from the network layer to inform the TCP sender about the wireless link conditions and the cause of packet losses. TCP adaptive pacing (TCP-AP) is another technique that uses the feedback from the physical layer to adjust the TCP sending rate according to the wireless channel quality.