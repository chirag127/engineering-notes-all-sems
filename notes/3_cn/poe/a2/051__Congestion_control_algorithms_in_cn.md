 Here is the formal content on the topic "Congestion control algorithms in cn" in markdown format without any emojis or external links:

### Congestion control algorithms in cn

1. Slow start: When a connection is established, congestion window is initialized to 1 or 2 segments. In each RTT, congestion window is increased by 1. This leads to exponential increase in congestion window. This phase is called slow start. The goal of slow start is to quickly open up the window and grab as much bandwidth as possible.
2. Congestion avoidance: Once slow start threshold is reached, congestion avoidance phase starts. In this phase, congestion window is increased linearly (one segment per RTT). This is done to probe the network for available bandwidth without overloading the network.
3. Fast retransmit: If duplicate ACKs are received, it indicates that segments have been dropped. So the dropped segments are retransmitted without waiting for the timeout. This is called fast retransmit.
4. Fast recovery: After fast retransmit, congestion window is set to half its previous value. This is called fast recovery. New segments are sent only after 3 duplicate ACKs are received. This helps in preventing bursty traffic into the network.
5. Timeouts: If an ACK is not received for a segment within a certain amount of time called timeout, the segment is retransmitted. This is required when duplicate ACKs are not received. Timeout values can be quite high leading to noticeable delays.

The above points summarise the key congestion control algorithms used in TCP to control congestion and achieve maximum throughput without overloading the network. The algorithms work in tandem with each other to adapt to the changing network conditions.