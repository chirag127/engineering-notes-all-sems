### TCP Congestion Control in Transport Layer

- TCP congestion control is a mechanism that prevents the network from being overloaded by the TCP traffic.
- TCP congestion control adapts the sending rate of the TCP sender to the network conditions, such as the available bandwidth and the level of congestion.
- TCP congestion control consists of three main phases: slow start, congestion avoidance, and congestion detection.
- Slow start phase: The TCP sender starts with a small congestion window (cwnd) of one segment and increases it exponentially for every round-trip time (RTT) until it reaches a threshold (ssthresh) value.
- Congestion avoidance phase: The TCP sender increases the cwnd linearly for every RTT, by adding one segment per RTT, until it detects congestion.
- Congestion detection phase: The TCP sender detects congestion by either a timeout or three duplicate acknowledgements (ACKs). Depending on the case, the TCP sender reacts differently:
  - Timeout: The TCP sender assumes that the network is highly congested and reduces the ssthresh to half of the current cwnd, sets the cwnd to one segment, and restarts the slow start phase.
  - Three duplicate ACKs: The TCP sender assumes that the network is mildly congested and reduces the ssthresh to half of the current cwnd, sets the cwnd to the new ssthresh, and continues the congestion avoidance phase.
- TCP congestion control aims to achieve both efficiency and fairness in the network. Efficiency means that the TCP traffic utilizes the network capacity well, without causing excessive delay or loss. Fairness means that the TCP flows share the network resources equally or proportionally.
- TCP congestion control is a distributed and adaptive algorithm that relies on the feedback from the network and the receiver. TCP congestion control does not require any explicit signaling from the network or the receiver about the network conditions.
- TCP congestion control is one of the most important Internet protocols, as it carries a much higher volume of traffic on the Internet than any other transport-layer protocol. TCP congestion control is the main technique that prevents the Internet from collapsing due to over-utilization.