TCP congestion control is a mechanism that prevents the network from being overloaded by the excessive amount of data sent by the TCP sender. It is implemented in the transport layer of the TCP/IP protocol stack. TCP congestion control consists of three main phases: slow start, congestion avoidance, and congestion recovery. The following diagram illustrates the basic idea of TCP congestion control:

### TCP Congestion Control in Transport Layer

```
    +-----------------+        +-----------------+
    |                 |        |                 |
    |   TCP Sender    |        |   TCP Receiver  |
    |                 |        |                 |
    +-----------------+        +-----------------+
            |                          ^
            |                          |
            |                          |
            |                          |
            |                          |
            |                          |
            |                          |
            |                          |
            |                          |
            |                          |
            |                          |
            |                          |
            |                          |
            |                          |
            |                          |
            |                          |
            |                          |
            |                          |
            |                          |
            |                          |
            |                          |
            |                          |
            |                          |
            v                          |
    +-----------------+        +-----------------+
    |                 |        |                 |
    |   Network       |        |   Network       |
    |   Layer         |        |   Layer         |
    |                 |        |                 |
    +-----------------+        +-----------------+
            |                          ^
            |                          |
            |                          |
            |                          |
            |                          |
            |                          |
            |                          |
            |                          |
            |                          |
            |                          |
            |                          |
            |                          |
            v                          |
    +-----------------+        +-----------------+
    |                 |        |                 |
    |   Link Layer    |        |   Link Layer    |
    |                 |        |                 |
    +-----------------+        +-----------------+
            |                          ^
            |                          |
            |                          |
            |                          |
            |                          |
            |                          |
            |                          |
            |                          |
            |                          |
            |                          |
            v                          |
    +-----------------+        +-----------------+
    |                 |        |                 |
    |   Physical      |        |   Physical      |
    |   Layer         |        |   Layer         |
    |                 |        |                 |
    +-----------------+        +-----------------+
```

The TCP sender maintains a variable called congestion window (cwnd) that determines how many packets can be sent at a time. The TCP receiver maintains a variable called receive window (rwnd) that determines how many packets can be received at a time. The TCP sender can send up to min(cwnd, rwnd) packets at a time.

In the slow start phase, the TCP sender starts with a small cwnd (usually one or two packets) and doubles it every round trip time (RTT), which is the time it takes for a packet to travel from the sender to the receiver and back. This exponential growth allows the TCP sender to probe the network capacity and find the optimal sending rate.

In the congestion avoidance phase, the TCP sender increases the cwnd by one packet every RTT, which is a linear growth. This phase is entered when the cwnd reaches a threshold value (ssthresh) that is set by the TCP sender based on the network conditions. The congestion avoidance phase aims to maintain a high and stable throughput without causing congestion.

In the congestion recovery phase, the TCP sender detects a packet loss, which is a sign of congestion, and reduces the cwnd by half. This phase is entered when the TCP sender receives three duplicate acknowledgments (ACKs) for the same packet, which is called fast retransmit, or when the TCP sender times out, which is called timeout retransmit. The congestion recovery phase aims to recover from the packet loss and resume the normal transmission.