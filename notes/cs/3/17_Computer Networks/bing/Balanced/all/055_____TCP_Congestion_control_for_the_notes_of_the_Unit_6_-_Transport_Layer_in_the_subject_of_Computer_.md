# TCP Congestion Control

- TCP congestion control is a mechanism that aims to regulate the amount of data that a sender can inject into the network, based on the network capacity and the level of congestion.
- TCP congestion control consists of three main phases: slow start, congestion avoidance, and congestion detection.
- Slow start phase: The sender starts with a small congestion window (cwnd) and increases it exponentially for every acknowledgment (ACK) received, until it reaches a threshold value (ssthresh) or a packet loss occurs .
- Congestion avoidance phase: After reaching the threshold, the sender increases the cwnd linearly for every ACK received, until a packet loss occurs .
- Congestion detection phase: The sender detects a packet loss by either a timeout or a duplicate ACK. Depending on the algorithm used, the sender may reduce the cwnd by half (multiplicative decrease) or set it to one (slow start restart) and update the ssthresh accordingly .
- TCP congestion control algorithms: There are different variants of TCP congestion control algorithms, such as TCP Reno, TCP NewReno, TCP Vegas, TCP Cubic, TCP BBR, etc. They differ in how they react to packet losses, how they estimate the available bandwidth, and how they adjust the cwnd and ssthresh values .
- Some TCP congestion control algorithms require custom fields to be added to the TCP packet structure, such as Explicit Control Protocol (XCP), MaxNet, etc. These algorithms use explicit feedback from the routers to adjust the sending rate of the sender.