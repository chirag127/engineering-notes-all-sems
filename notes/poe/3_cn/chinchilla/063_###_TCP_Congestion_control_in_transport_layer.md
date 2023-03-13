### TCP Congestion control in transport layer

TCP (Transmission Control Protocol) is a reliable and connection-oriented protocol in the transport layer of the TCP/IP protocol suite. It ensures that the data transmitted between two hosts is received without any errors and in the correct order. TCP implements a congestion control mechanism to prevent network congestion and ensure fair sharing of network resources among different flows. In this section, we will learn about TCP congestion control and its various algorithms.

#### TCP Congestion Control

TCP congestion control is a mechanism by which TCP sources limit their sending rate to avoid congesting the network. It is an end-to-end mechanism that relies on feedback from the network to adjust the sending rate of the TCP sources. TCP congestion control uses a feedback mechanism called TCP congestion window (CWND) to regulate the sending rate of the TCP sources.

#### TCP Congestion Window (CWND)

The TCP congestion window (CWND) is a variable maintained by the TCP sender that limits the amount of data that can be transmitted before receiving an acknowledgment (ACK) from the receiver. The size of the CWND is dynamically adjusted based on the feedback received from the network. The CWND is increased when the network is underutilized and decreased when congestion is detected.

#### TCP Congestion Control Algorithms

TCP congestion control algorithms are used to adjust the size of the CWND based on the feedback received from the network. The following are some of the popular TCP congestion control algorithms:

- Slow Start: In the slow start algorithm, the TCP sender starts with a small CWND and increases it exponentially until it detects congestion. The CWND is doubled for each round-trip time (RTT) until it reaches the slow-start threshold (SSTHRESH).

- Congestion Avoidance: In the congestion avoidance algorithm, the TCP sender increases the CWND by one MSS (Maximum Segment Size) for every RTT until it detects congestion. Once congestion is detected, the CWND is reduced and the slow start algorithm is used to increase the CWND again.

- Fast Recovery: In the fast recovery algorithm, the TCP sender reduces the CWND to half of the current value and enters the fast recovery state when it receives three duplicate ACKs from the receiver. In the fast recovery state, the sender retransmits the lost segment and continues to transmit new segments.

- Fast Retransmit: In the fast retransmit algorithm, the TCP sender retransmits a lost segment when it receives three duplicate ACKs from the receiver. This avoids the need for the sender to wait for a retransmission timeout (RTO) before retransmitting the lost segment.

#### Advantages of TCP Congestion Control

- TCP congestion control ensures fair sharing of network resources among different flows.
- It prevents network congestion and helps in maintaining network stability.
- It ensures reliable delivery of data by preventing packet loss due to congestion.

#### Disadvantages of TCP Congestion Control

- TCP congestion control may result in lower throughput when the network is underutilized.
- It may increase the delay in delivering data due to the need to regulate the sending rate.

#### Mnemonics and Learning Tricks

- "Slow and steady wins the race" can be used to remember the slow start algorithm.
- "Avoid congestion by taking small steps" can be used to remember the congestion avoidance algorithm.
- "Recover fast from duplicates" can be used to remember the fast recovery algorithm.
- "Retransmit fast to avoid timeouts" can be used to remember the fast retransmit algorithm.

#### Examples and Applications

TCP congestion control is used in various applications such as web browsing, email, file transfer, and video streaming. It ensures reliable and efficient transmission of data over the internet and helps in maintaining network stability.