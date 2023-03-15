# TCP Congestion Control

TCP Congestion Control is a mechanism used by the Transmission Control Protocol (TCP) to handle congestion in a network. It consists of three phases: Slow Start, Congestion Avoidance, and Congestion Detection .

- **Slow Start:** In this phase, the sender starts sending packets slowly and gradually increases the number of packets until it reaches a threshold .
- **Congestion Avoidance:** After reaching the threshold, the sender increases the number of packets by 1 .
- **Congestion Detection:** If congestion is detected, the sender goes back to the Slow Start phase or the Congestion Avoidance phase .

TCP uses a network congestion-avoidance algorithm that includes various aspects of an additive increase/multiplicative decrease (AIMD) scheme, along with other schemes including slow start and congestion window (CWND), to achieve congestion avoidance .

Some algorithms require custom fields to be added to the TCP packet structure, such as the Explicit Control Protocol (XCP) and MaxNet .

- **Explicit Control Protocol (XCP):** XCP packets carry a congestion header with a feedback field, indicating the increase or decrease in the congestion window .
- **MaxNet:** Uses a single header field, which carries the maximum congestion level of any router along the path .

TCP Congestion Control techniques prevent congestion or help mitigate the congestion after it occurs. Unlike the sliding window (rwnd) used in the flow control mechanism and maintained by the receiver, TCP uses the congestion window (cwnd) maintained by the sender .