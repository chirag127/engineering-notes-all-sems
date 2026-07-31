### Congestion control algorithms in computer networks

- Congestion control algorithms are mechanisms that control the entry of data packets into the network, enabling a better use of a shared network infrastructure and avoiding congestive collapse.
- Congestive collapse is a situation where the network performance degrades drastically due to excessive traffic and congestion.
- Congestion control algorithms can be broadly classified into two categories: open loop and closed loop.
- Open loop congestion control policies are applied to prevent congestion before it happens. They involve designing the network and choosing the appropriate protocols and parameters to avoid congestion.
- Closed loop congestion control policies are applied to detect and mitigate congestion after it happens. They involve monitoring the network state and adjusting the transmission rate or window size of the senders based on feedback signals such as packet losses and delays.
- Some examples of open loop congestion control techniques are admission control, traffic shaping, and resource reservation.
- Some examples of closed loop congestion control techniques are congestion avoidance, congestion recovery, and congestion pricing.
- Congestion avoidance algorithms are implemented at the TCP layer as the mechanism to avoid congestive collapse in a network. They use additive increase/multiplicative decrease (AIMD) scheme, along with other schemes such as slow start and congestion window (CWND), to achieve congestion avoidance.
- Congestion recovery algorithms are implemented at the TCP layer as the mechanism to recover from packet losses due to congestion. They use fast retransmit, fast recovery, and selective acknowledgment (SACK) schemes to reduce the recovery time and improve the throughput.
- Congestion pricing algorithms are implemented at the network layer as the mechanism to allocate network resources based on the demand and supply. They use economic principles such as marginal cost pricing, smart market, and progressive second price auction to charge users for using the network and incentivize them to reduce their demand during congestion.