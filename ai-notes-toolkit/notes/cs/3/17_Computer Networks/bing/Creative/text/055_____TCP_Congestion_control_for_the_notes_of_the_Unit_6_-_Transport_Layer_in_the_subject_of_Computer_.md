### TCP Congestion Control

- TCP congestion control is a mechanism that aims to regulate the amount of data that a sender can inject into the network, based on the network capacity and the feedback from the receiver .
- TCP congestion control consists of three main phases: slow start, congestion avoidance, and congestion detection .
- Slow start phase: The sender starts with a small congestion window (cwnd) and increases it exponentially for every acknowledgment (ACK) received, until it reaches a threshold value (ssthresh) or a packet loss occurs .
- Congestion avoidance phase: The sender increases the cwnd linearly for every ACK received, until a packet loss occurs .
- Congestion detection phase: The sender detects a packet loss by either a timeout or a duplicate ACK. Depending on the algorithm used, the sender may reduce the cwnd by half (multiplicative decrease) or set it to one (slow start restart) and update the ssthresh accordingly .
- TCP congestion control algorithms vary in how they react to packet losses and how they adjust the cwnd and ssthresh values. Some of the common algorithms are: Reno, NewReno, Tahoe, Fast Retransmit, Fast Recovery, SACK, Vegas, Cubic, BBR, etc  .
- Some TCP congestion control algorithms require additional fields or headers in the TCP packet structure, such as Explicit Control Protocol (XCP), MaxNet, etc.