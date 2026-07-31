 Here is the content in markdown format without any emojis or external links and in formal tone:

### TCP Congestion control

- TCP Congestion control is a mechanism to control congestion in the network which may occur due to various reasons like buffer overflow, excessive load etc. It is used to reduce the congestion by controlling the transmission rate.
- There are 2 phases of TCP Congestion control:

1. Slow start: The sender maintains a congestion window (cwnd) which is initially very small. The sender can transmit only up to the size of congestion window. cwnd is incremented for every ACK received. Through this, the transmission rate is slowly increased.
2. Congestion avoidance: Once the congestion window reaches a threshold (ssthresh), the protocol enters into congestion avoidance phase. In this phase, the congestion window is incremented for every round trip time (RTT). This leads to slower growth of window size as compared to slow start. This mechanism probes for spare bandwidth in the network and accordingly adjusts the transmission rate.

- If there is packet loss detected due to congestion, congestion avoidance algorithms reduce the transmission rate by reducing congestion window size. This is done to ease out the congestion in the network. The algorithms then again follow the same cycle to probe for higher bandwidth while maintaining smaller congestion window to avoid congestion.
- The key goals of TCP Congestion control are:
 - Maximize throughput
 - Minimize delay
 - Treat TCP connections fairly
 - Avoid congestion collapse

This summarizes the key points about TCP Congestion control. Let me know if you would like me to elaborate on any of the points or add more details to the content.