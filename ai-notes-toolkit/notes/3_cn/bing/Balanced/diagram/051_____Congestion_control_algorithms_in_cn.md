### Congestion control algorithms in computer networks

- Congestion control algorithms are mechanisms that control the entry of data packets into the network, enabling a better use of a shared network infrastructure and avoiding congestive collapse .
- Congestive collapse is a situation where the network performance degrades drastically due to excessive traffic and congestion.
- Congestion control algorithms can be broadly classified into two categories: open loop and closed loop.
- Open loop congestion control policies are applied to prevent congestion before it happens. They involve designing the network and choosing the appropriate protocols and parameters to avoid congestion.
- Closed loop congestion control policies are applied to detect and mitigate congestion after it happens. They involve monitoring the network state and adjusting the transmission rate and window size of the senders and receivers based on feedback signals.
- Some examples of open loop congestion control techniques are admission control, traffic shaping, and resource reservation.
- Some examples of closed loop congestion control techniques are congestion avoidance, congestion recovery, and congestion control algorithms in TCP.
- Congestion avoidance algorithms are implemented at the TCP layer as the mechanism to avoid congestive collapse in a network. They use packet losses and delays as signals to infer congestion and decide how fast to send data .
- Some examples of congestion avoidance algorithms are slow start, additive increase/multiplicative decrease (AIMD), congestion window (CWND), fast retransmit, fast recovery, and TCP variants such as Tahoe, Reno, New Reno, Vegas, and BBR.
- Congestion recovery algorithms are implemented at the data link layer or the network layer as the mechanism to recover from congestion and restore the network performance. They use explicit or implicit notifications from the routers or the receivers to inform the senders about the congestion and request them to reduce their transmission rate.
- Some examples of congestion recovery algorithms are backpressure, choke packets, explicit congestion notification (ECN), and random early detection (RED).