### TCP Congestion control in transport layer

- TCP congestion control is a mechanism that aims to regulate the amount of data sent by a sender to avoid overwhelming the network or the receiver.
- TCP congestion control is based on the concept of congestion window (cwnd), which is the maximum number of bytes that a sender can have in flight (unacknowledged) at any time.
- TCP congestion control consists of four phases: slow start, congestion avoidance, fast retransmit, and fast recovery.
- Slow start: The sender starts with a small cwnd (usually one segment) and increases it by one segment for every ACK received, until it reaches a threshold (ssthresh) or a loss occurs.
- Congestion avoidance: The sender increases the cwnd by a fraction of a segment for every ACK received, to probe the network capacity gradually.
- Fast retransmit: The sender detects a loss by receiving three duplicate ACKs for the same segment, and retransmits the lost segment without waiting for a timeout.
- Fast recovery: The sender reduces the cwnd by half and enters the congestion avoidance phase, to recover from the loss quickly.