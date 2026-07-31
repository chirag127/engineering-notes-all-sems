### Congestion control algorithms in computer networks

- Congestion control algorithms are mechanisms that control the entry of data packets into the network, enabling a better use of a shared network infrastructure and avoiding congestive collapse.
- Congestive collapse is a situation where the network performance degrades drastically due to excessive traffic and congestion.
- Congestion control algorithms can be broadly classified into two categories: open loop and closed loop.
- Open loop congestion control policies are applied to prevent congestion before it happens. They involve designing the network and choosing the appropriate protocols and parameters to avoid congestion.
- Closed loop congestion control policies are applied to detect and mitigate congestion after it happens. They involve monitoring the network state and adjusting the transmission rate or window size of the senders based on feedback signals such as packet loss, delay, or explicit notifications.
- Some examples of open loop congestion control techniques are admission control, traffic shaping, and resource reservation.
- Some examples of closed loop congestion control techniques are congestion avoidance, congestion recovery, and congestion notification.
- Congestion avoidance algorithms are implemented at the TCP layer as the mechanism to avoid congestive collapse in a network. They aim to keep the network operating at the optimal point where the throughput is high and the delay is low.
- Some examples of congestion avoidance algorithms are slow start, additive increase/multiplicative decrease (AIMD), congestion window (CWND), and fast retransmit.
- Slow start is an algorithm that starts with a small transmission rate and increases it exponentially until a threshold is reached or a packet is lost. It is used to probe the network capacity and avoid sending too many packets at once.
- AIMD is an algorithm that increases the transmission rate linearly until a packet is lost, and then decreases it multiplicatively by a factor. It is used to achieve fairness and stability among multiple competing flows.
- CWND is a variable that limits the number of packets that a sender can have in the network at any time. It is adjusted by the congestion avoidance algorithms based on the network conditions.
- Fast retransmit is an algorithm that detects packet loss by receiving duplicate acknowledgments from the receiver, and retransmits the lost packet without waiting for a timeout. It is used to recover from packet loss quickly and avoid unnecessary retransmissions.
- Some mnemonics and learning tricks for congestion control algorithms are:
  - Slow start: Start slow and grow fast.
  - AIMD: Add and multiply, divide and subtract.
  - CWND: Window size is the key to congestion control.
  - Fast retransmit: Don't wait, just retransmit.