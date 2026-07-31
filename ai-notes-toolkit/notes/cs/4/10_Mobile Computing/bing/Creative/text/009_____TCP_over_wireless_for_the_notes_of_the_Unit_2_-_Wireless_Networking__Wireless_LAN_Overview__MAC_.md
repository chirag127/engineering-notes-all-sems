### TCP over wireless

- Transmission Control Protocol (TCP) is a reliable and connection-oriented protocol that provides end-to-end data delivery over the Internet.
- TCP assumes that most packet losses are due to network congestion and responds by reducing the sending rate to avoid further losses.
- However, in wireless networks, packet losses can also occur due to wireless link errors, such as fading, shadowing, interference, and mobility.
- TCP over wireless networks faces several challenges, such as:
  - TCP cannot distinguish between congestion losses and wireless losses, and may unnecessarily reduce the sending rate when wireless losses occur.
  - TCP may experience frequent timeouts and retransmissions due to the high delay and variability of wireless links.
  - TCP may suffer from spurious retransmissions and duplicate acknowledgements due to packet reordering and out-of-order delivery in wireless networks.
  - TCP may not fully utilize the available bandwidth of wireless links due to the slow start and congestion avoidance mechanisms.
- Several solutions have been proposed to improve the performance of TCP over wireless networks, such as:
  - Link layer solutions: These solutions aim to hide the wireless losses from TCP by using techniques such as error correction, retransmission, and packet scheduling at the link layer. For example, the Wireless Link Protocol (WLP)  provides reliable and in-order delivery of TCP packets over wireless links.
  - Split-connection solutions: These solutions divide the TCP connection into two segments: one over the wired network and one over the wireless network. The wireless segment uses a different protocol that is optimized for wireless conditions, while the wired segment uses standard TCP. For example, the Indirect TCP (I-TCP)  protocol splits the TCP connection at the base station, which acts as a proxy between the mobile host and the destination.
  - End-to-end solutions: These solutions modify the TCP behavior at the end hosts to adapt to wireless conditions, without changing the intermediate nodes or the TCP semantics. For example, the TCP Selective Acknowledgement (SACK)  option allows the sender to recover from multiple losses in a window without retransmitting all the packets.