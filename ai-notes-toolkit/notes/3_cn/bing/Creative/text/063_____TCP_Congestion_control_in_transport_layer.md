### TCP Congestion Control in Transport Layer

- TCP congestion control is a mechanism that aims to regulate the amount of data that a sender can inject into the network, based on the network capacity and the feedback from the receiver .
- TCP congestion control consists of three main phases: slow start, congestion avoidance, and congestion detection .
- Slow start phase: The sender starts with a small congestion window (cwnd) and increases it exponentially for every acknowledgment (ACK) received, until it reaches a threshold value (ssthresh) or a packet loss occurs .
- Congestion avoidance phase: After reaching the ssthresh, the sender increases the cwnd linearly for every round-trip time (RTT), until a packet loss occurs .
- Congestion detection phase: The sender detects a packet loss by either a timeout or a duplicate ACK. Depending on the detection method, the sender either reduces the cwnd by half (fast recovery) or sets it to one segment (slow start) and updates the ssthresh accordingly .
- TCP congestion control algorithms vary in how they adjust the cwnd and the ssthresh in response to network events. Some of the common algorithms are: Reno, NewReno, Tahoe, SACK, Vegas, BIC, CUBIC, etc .
- Some TCP congestion control algorithms require additional fields in the TCP header to carry congestion information, such as XCP and MaxNet.