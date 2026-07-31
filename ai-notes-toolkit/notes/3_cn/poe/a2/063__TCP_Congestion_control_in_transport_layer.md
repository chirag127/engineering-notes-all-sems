 Here is the formal content on the topic "TCP Congestion control in transport layer" in markdown format without any emojis or external links:

### TCP Congestion control in transport layer

1. TCP employs a congestion avoidance algorithm that aims to reduce congestion in the network and prevent packet loss.
2. TCP monitors the rate of returning acknowledgements (ACKs) from the receiver. If ACKs return at a slower rate than expected, it is a sign of congestion in the network. TCP will then slow down its transmission rate.
3. TCP uses an "Additive Increase Multiplicative Decrease" (AIMD) algorithm. The transmission rate is increased additively on each round trip time (RTT) if there is no congestion. However, upon detection of congestion via loss of ACKs, TCP reduces its transmission rate multiplicatively. This leads to a sawtooth pattern of slow increase followed by a sharp decrease in transmission rate. This probes for available bandwidth in the network while avoiding persistent high congestion.
4. Modern TCP implementations use mechanisms like slow start and congestion avoidance to more efficiently probe for bandwidth and recover from losses. TCP optimizes throughput while avoiding congestion collapse.
5. TCP's congestion control makes it a "responsive" and "fair" transport protocol that adapts to the available bandwidth and shares it fairly with other TCP flows in the network. This makes the Internet's packet-switched network more efficient and robust.