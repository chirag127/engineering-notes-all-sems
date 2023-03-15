### TCP Congestion Control

- TCP congestion control is a mechanism that aims to avoid network congestion and ensure fair and efficient use of network resources by TCP senders.
- TCP congestion control consists of three main components:
  - Congestion window (cwnd): a variable maintained by the sender that limits the amount of data that can be in transit at any time.
  - Congestion avoidance algorithm: a set of rules that determines how the sender adjusts the cwnd in response to network events, such as acknowledgments, timeouts, or duplicate acknowledgments.
  - Slow start algorithm: a special case of congestion avoidance that is used when the sender starts a new connection or restarts after a long idle period or a packet loss.
- TCP congestion control operates in three phases:
  - Slow start phase: the sender starts with a small cwnd (usually one or two segments) and increases it exponentially for every acknowledgment received, until it reaches a threshold value (ssthresh) or a packet loss occurs.
  - Congestion avoidance phase: the sender increases the cwnd linearly for every round-trip time (RTT), as long as there is no packet loss. The cwnd is incremented by one segment per RTT, which is equivalent to adding one segment for every cwnd segments acknowledged.
  - Congestion detection phase: the sender detects a packet loss by either a timeout or receiving three duplicate acknowledgments. Depending on the detection method, the sender reacts differently:
    - Timeout: the sender assumes that the network is severely congested and sets the ssthresh to half of the current cwnd, and the cwnd to one segment. The sender then enters the slow start phase again.
    - Three duplicate acknowledgments: the sender assumes that the network is mildly congested and sets the ssthresh to half of the current cwnd, and the cwnd to the ssthresh value. The sender then enters the congestion avoidance phase.
- TCP congestion control is based on the additive increase/multiplicative decrease (AIMD) principle, which ensures that the cwnd grows slowly when it is large and shrinks quickly when it is small.
- TCP congestion control is also adaptive and self-clocking, meaning that it adjusts the sending rate according to the feedback from the network and the receiver, and that it synchronizes the sender with the receiver by using acknowledgments as implicit signals.
- TCP congestion control has been improved over the years by introducing various enhancements and variations, such as fast retransmit, fast recovery, selective acknowledgment, NewReno, Vegas, Cubic, BBR, and others  . Some of these algorithms require custom fields to be added to the TCP packet structure, such as XCP, MaxNet, and ECN.