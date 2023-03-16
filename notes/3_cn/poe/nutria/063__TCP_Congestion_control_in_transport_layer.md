
### TCP Congestion Control in Transport Layer

1. TCP (Transmission Control Protocol) is a connection-oriented protocol used to ensure reliable data transfer over a network. 
2. Congestion control is a mechanism used by TCP to regulate the rate of data transmission so that the network is not overwhelmed.
3. Congestion control is achieved by adjusting the window size, which is the amount of data that can be transmitted before an acknowledgement is required.
4. Slow start is the initial phase of the congestion control algorithm. In this phase, the window size is increased exponentially until a packet loss is detected.
5. Congestive collapse occurs when the window size is too large and the network is overwhelmed by the amount of data being sent.
6. To prevent congestive collapse, the congestion window size is reduced when packet loss is detected. This is known as the congestion avoidance algorithm.
7. The TCP congestion control algorithm also includes the fast retransmit and fast recovery algorithms. 
8. Fast retransmit is used to detect and retransmit lost packets without waiting for a timeout. 
9. Fast recovery is used to reduce the window size and prevent further packet loss.
10. The TCP congestion control algorithm is designed to ensure reliable data transfer over a network while avoiding congestive collapse.