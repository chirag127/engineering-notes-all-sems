# TCP Congestion Control

- TCP congestion control is a mechanism that aims to regulate the amount of data that a sender can inject into the network, based on the network capacity and the level of congestion .
- TCP congestion control consists of three main phases: slow start, congestion avoidance, and congestion detection .
- Slow start phase: The sender starts with a small congestion window (cwnd) and increases it exponentially for every acknowledgment (ACK) received, until it reaches a threshold value (ssthresh) or a packet loss occurs .
- Congestion avoidance phase: After reaching the ssthresh, the sender increases the cwnd linearly for every ACK received, until a packet loss occurs .
- Congestion detection phase: The sender detects a packet loss by either a timeout or a duplicate ACK. Depending on the algorithm used, the sender may reduce the cwnd by half (multiplicative decrease) or set it to one (slow start restart) and update the ssthresh accordingly .
- TCP uses various algorithms to implement congestion control, such as Reno, NewReno, Tahoe, Vegas, Cubic, BBR, etc. Some of these algorithms require additional fields in the TCP header, such as Explicit Congestion Notification (ECN), Explicit Control Protocol (XCP), or MaxNet .
- TCP congestion control is essential for ensuring the efficient and fair use of network resources, avoiding congestion collapse, and providing end-to-end reliability .