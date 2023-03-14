Congestion control algorithms are methods to regulate the flow of data packets in a network and prevent congestion collapse. There are different types of congestion control algorithms, such as leaky bucket, token bucket, additive increase/multiplicative decrease (AIMD), slow start, and congestion window (CWND). Each algorithm has its own advantages and disadvantages, depending on the network scenario and the desired performance.

### Congestion control algorithms in computer networks

The following diagram illustrates the basic architecture of a congestion control algorithm in a computer network. It shows how a sender and a receiver communicate over a network link, and how the sender adjusts its sending rate based on the feedback from the receiver and the network.

```
    +--------+        +--------+        +--------+
    | Sender |------->| Router |------->| Receiver|
    +--------+        +--------+        +--------+
        |                 |                 |
        |<----------------|-----------------|
        |    Feedback     |    Acknowledgment
        |                 |                 |
        |                 |<----------------|
        |                 |    Data packet
        |---------------->|
        |    Sending rate |
        |                 |
```

The sender sends data packets to the receiver through the router, which may buffer, drop, or delay the packets depending on the network conditions. The receiver sends acknowledgments (ACKs) to the sender for each packet received, and may also send feedback information such as the round-trip time (RTT), the available bandwidth, or the packet loss rate. The sender uses this feedback to adjust its sending rate, which is the number of packets sent per unit time. The sender tries to maximize its sending rate without causing congestion in the network, which can lead to packet losses, long delays, and low throughput.

Different congestion control algorithms use different strategies to adjust the sending rate. For example, the leaky bucket algorithm sends packets at a constant rate, regardless of the network conditions. The token bucket algorithm allows bursts of packets up to a certain limit, and then sends packets at a constant rate. The AIMD algorithm increases the sending rate by a fixed amount until a packet loss occurs, and then decreases the sending rate by a multiplicative factor. The slow start algorithm starts with a low sending rate and doubles it every RTT until a threshold is reached, and then switches to the AIMD algorithm. The CWND algorithm maintains a congestion window, which is the number of packets that can be sent without waiting for an ACK, and adjusts it based on the network feedback.