# TCP over wireless

- TCP (Transmission Control Protocol) is a reliable and connection-oriented protocol that provides end-to-end data delivery over the Internet.
- TCP assumes that most packet losses are due to network congestion and responds by reducing the sending rate to avoid further losses.
- However, in wireless networks, packet losses can also occur due to wireless link errors, such as fading, shadowing, interference, and mobility.
- TCP cannot distinguish between congestion losses and wireless losses and may unnecessarily reduce the sending rate, resulting in poor performance and underutilization of the wireless bandwidth.
- Therefore, TCP needs to be adapted or enhanced to cope with the challenges of wireless networks, such as high delays, high error rates, variable bandwidth, and frequent handoffs.
- Several mechanisms have been proposed to improve the performance of TCP over wireless networks, which can be classified into four categories   :

  - **End-to-end solutions**: These solutions modify the TCP sender or receiver to make them aware of the wireless link conditions and adjust their behavior accordingly. For example, TCP Westwood estimates the available bandwidth based on the rate of acknowledgments and adapts the congestion window accordingly. TCP Snoop caches packets at the base station and retransmits them locally in case of wireless losses, without notifying the TCP sender.
  - **Link layer solutions**: These solutions use link layer protocols to provide reliable data transmission over the wireless link and hide the wireless losses from the TCP layer. For example, Automatic Repeat reQuest (ARQ) protocols use acknowledgments and timeouts to detect and recover from errors. Forward Error Correction (FEC) protocols add redundant bits to the packets to correct errors without retransmission.
  - **Split-connection solutions**: These solutions split the TCP connection into two sub-connections: one between the TCP sender and the base station, and another between the base station and the TCP receiver. The base station acts as a proxy that handles the wireless losses and congestion control for the sub-connection with the TCP receiver. For example, I-TCP uses a TCP connection over the wired network and a non-TCP connection over the wireless network.
  - **Cross-layer solutions**: These solutions exploit the interactions and information exchange between different layers of the network stack to optimize the performance of TCP over wireless networks. For example, TCP-Friendly Rate Control (TFRC) uses feedback from the MAC layer to estimate the wireless link quality and adjust the sending rate accordingly.

: https://en.wikipedia.org/wiki/TCP_Westwood
: https://en.wikipedia.org/wiki/TCP_Snoop
: https://en.wikipedia.org/wiki/Indirect_TCP
: https://en.wikipedia.org/wiki/TCP-friendly_rate_control