### Congestion control algorithms for the notes of the Unit 5 - Network Layer in the subject of Computer Networks

- Congestion control is a mechanism that controls the entry of data packets into the network, enabling a better use of a shared network infrastructure and avoiding congestive collapse .
- Congestive collapse is a situation where the network performance degrades drastically due to excessive traffic and congestion .
- Congestion control algorithms are implemented at the TCP layer as the mechanism to avoid congestive collapse in a network .
- Congestion control algorithms use packet losses and delays as signals to infer congestion and decide how fast to send data.
- Congestion control algorithms can be broadly classified into two categories: open loop and closed loop.
- Open loop congestion control policies are applied to prevent congestion before it happens. They involve designing the network and the protocols in such a way that congestion is unlikely to occur.
- Closed loop congestion control policies are applied to detect and mitigate congestion after it happens. They involve feedback mechanisms that adjust the network parameters and the sending rates based on the congestion signals.
- Some examples of open loop congestion control techniques are admission control, traffic shaping, and resource reservation.
- Some examples of closed loop congestion control techniques are congestion window, additive increase multiplicative decrease (AIMD), slow start, congestion avoidance, and fast retransmit.
- Some examples of congestion control algorithms that use closed loop techniques are TCP Reno, TCP Tahoe, TCP New Reno, TCP Vegas, TCP BBR, and TCP CUBIC .