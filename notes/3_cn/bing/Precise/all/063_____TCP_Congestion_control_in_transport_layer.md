### TCP Congestion control in transport layer

TCP congestion control is a mechanism used by the transport layer protocol, TCP, to control the flow of data in a network and prevent congestion. It is an essential part of the TCP protocol and is used to ensure that the network is used efficiently and fairly.

1. **Slow Start**: When a TCP connection is first established, the sender starts by sending a small amount of data, typically one or two segments. The sender then waits for an acknowledgement from the receiver before sending more data. This process is repeated, with the sender doubling the amount of data sent each time until the receiver's advertised window is reached or packet loss occurs.

2. **Congestion Avoidance**: Once the slow start phase is complete, the sender enters the congestion avoidance phase. In this phase, the sender increases the amount of data sent by one segment for each round trip time (RTT). This allows the sender to gradually increase the amount of data sent until the network becomes congested.

3. **Fast Retransmit**: If the sender detects that a segment has been lost, it will immediately retransmit the lost segment without waiting for the retransmission timer to expire. This is known as fast retransmit.

4. **Fast Recovery**: After fast retransmit, the sender enters the fast recovery phase. In this phase, the sender reduces the congestion window by half and continues to transmit data at a reduced rate. This allows the sender to quickly recover from the lost segment and resume transmitting data at a high rate.

A mnemonic to remember the four phases of TCP congestion control is **"Start Avoiding Fast Recovery"**.

TCP congestion control is an important mechanism that helps to ensure that the network is used efficiently and fairly. By controlling the flow of data, TCP congestion control can prevent congestion and improve the overall performance of the network. It is an essential part of the TCP protocol and is used by all TCP-based applications.