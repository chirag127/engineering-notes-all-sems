### TCP Congestion control in transport layer

Transmission Control Protocol (TCP) is a reliable transport protocol that provides end-to-end delivery of data between applications running on different hosts. Congestion control is an important aspect of TCP, which manages the data transmission rate to prevent network congestion.

TCP congestion control consists of several mechanisms that work together to ensure that the network is not overloaded with traffic. These mechanisms are:

1. Slow start: When a TCP connection is established, the sender starts with a small window size and gradually increases it until it detects congestion. This mechanism prevents the sender from overwhelming the network with traffic at the start of the connection.

2. Congestion Avoidance: Once the sender detects congestion, it reduces the transmission rate to prevent further congestion. This mechanism uses a congestion window to control the amount of data that can be transmitted at a time.

3. Fast Retransmit/Fast Recovery: If the sender receives three duplicate acknowledgments for the same packet, it assumes that the packet has been lost and retransmits it immediately. This mechanism is faster than waiting for a timeout and retransmitting the packet.

4. Timeout: If the sender does not receive an acknowledgment for a packet within a certain time, it assumes that the packet has been lost and retransmits it. This mechanism is slower than fast retransmit but is necessary when the network experiences severe congestion.

TCP congestion control has the following advantages:

- It prevents network congestion by managing the data transmission rate.
- It ensures reliable delivery of data by retransmitting lost packets.
- It provides fairness among TCP connections sharing the same network.

However, TCP congestion control also has the following disadvantages:

- It may result in lower throughput when the network is not congested.
- It may not work well with real-time applications that require a constant data rate.

TCP congestion control is used in a wide range of applications, including web browsing, file transfer, email, and video streaming. It is an essential mechanism for maintaining network stability and ensuring reliable data delivery.