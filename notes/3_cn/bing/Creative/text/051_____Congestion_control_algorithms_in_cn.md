### Congestion control algorithms in computer networks

- Congestion control algorithms are mechanisms that control the entry of data packets into the network, enabling a better use of a shared network infrastructure and avoiding congestive collapse.
- Congestive collapse is a situation where the network performance degrades drastically due to excessive traffic and congestion.
- Congestion control algorithms can be broadly classified into two categories: open loop and closed loop.
- Open loop congestion control policies are applied to prevent congestion before it happens. They involve designing the network and the protocols in such a way that congestion is unlikely to occur.
- Closed loop congestion control policies are applied to detect and mitigate congestion after it happens. They involve monitoring the network state and adjusting the transmission rate or window size of the senders based on feedback signals such as packet losses and delays.
- Some examples of open loop congestion control techniques are admission control, traffic shaping, and resource reservation.
- Some examples of closed loop congestion control techniques are congestion avoidance, congestion recovery, and congestion pricing.
- Congestion avoidance algorithms are implemented at the TCP layer as the mechanism to avoid congestive collapse in a network. They use a combination of additive increase/multiplicative decrease (AIMD), slow start, and congestion window (CWND) schemes to adjust the transmission rate of the senders based on the network conditions.
- Congestion recovery algorithms are implemented at the TCP layer as the mechanism to recover from packet losses due to congestion. They use a combination of fast retransmit, fast recovery, and selective acknowledgment (SACK) schemes to retransmit the lost packets and resume the transmission rate of the senders based on the network conditions.
- Congestion pricing algorithms are implemented at the network layer as the mechanism to allocate the network resources based on the demand and supply of the users. They use a combination of pricing, auction, and incentive schemes to charge the users for the network usage and encourage them to reduce their demand during congestion.
- Some examples of congestion avoidance algorithms are TCP Tahoe, TCP Reno, TCP New Reno, TCP Vegas, TCP BIC, and TCP CUBIC.
- Some examples of congestion recovery algorithms are TCP SACK, TCP FACK, and TCP D-SACK.
- Some examples of congestion pricing algorithms are Smart Market, Progressive Second Price, and Proportional Fairness.