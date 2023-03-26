 Here is the content in markdown format without any emojis or external links and in a formal tone:

### TCP over wireless

- Wireless networks face issues like higher bit error rates, interference, hidden terminals, etc. which affect the performance of TCP.
- TCP assumes a wired network with low error rates and congestion as the primary cause of packet loss. It is not suitable for wireless networks which have higher error rates.
- The high error rates in wireless networks trigger unnecessary retransmissions which reduce throughput. TCP timeouts are also prone to triggering more often.
- The larger delay in wireless networks affects the estimation of Round Trip Time (RTT) which is used by TCP for congestion control. This leads to poor performance.
- Methods to improve TCP performance over wireless networks:
    - Use of forward error correction (FEC) to reduce bit error rates
    - Use of interleaving to handle burst errors
    - Use of larger congestion windows to improve throughput
    - Estimating congestion based on loss intervals rather than individual packet loss
    - Use of split TCP connections with a wired base station acting as a proxy
- Bluetooth and IEEE 802.11 wireless standards have mechanisms to improve TCP performance but it still remains a challenge to efficiently use TCP over wireless networks. More work is required to fully optimize TCP for the wireless medium.

The above content summarizes some of the key challenges with TCP over wireless networks and mentions a few techniques to improve the performance. The content is written in a formal tone with points and without any external links or emojis as instructed. Please let me know if you would like me to modify or expand the content in any way.