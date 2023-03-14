 Here is the content in markdown format with points on ### Congestion control algorithms in cn:

### Congestion control algorithms in cn

1. Slow start: Used by TCP. Initially slow increase in cwnd (congestion window) to slowly probe the network for available bandwidth and find congestion point. Exponential increase in cwnd till congestion is detected. Helps in efficiently utilizing bandwidth while avoiding congestion.

2. Congestion avoidance: Used by TCP after slow start. cwnd is incremented linearly to gently probe for more bandwidth while avoiding congestion. Upon congestion detection, cwnd is halved. This process continues leading to oscillation of cwnd around the available bandwidth.

3. Fast retransmit: If multiple duplicate ACKs are received, it is assumed that a segment has been dropped due to congestion. The dropped segment is retransmitted without waiting for the retransmission timer to expire, helping in faster recovery from congestion.

4. Fast recovery: After fast retransmit, cwnd is halved and then for each additional duplicate ACK received, cwnd is incremented by 1. This leads to efficient recovery from congestion without waiting for the slower retransmission timer.

Advantages: Effective utilization of bandwidth, avoiding congestion collapse.
Disadvantages: Can be unfair to other TCP connections, global synchronization can occur leading to inefficiency.

Examples: TCP Reno, TCP Vegas, TCP New Reno.

Applications: Web traffic, file transfer, etc.

The mnemonics and learning tricks for these algorithms are:

- Slow start: Slowly start, then exponential rise
- Congestion avoidance: Linear increase and halving on congestion
- Fast retransmit: Multiple dup ACKs imply packet drop
- Fast recovery: Halve cwnd and increment by 1 per dup ACK

However, these mnemonics may not be very easy to remember and depend on individual learning style. So only included them on your suggestion. Let me know if you would like me to modify or add any other points in the content.