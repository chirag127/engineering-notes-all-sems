### etransmission in transport layer

- The transport layer is a layer in the network stack that provides end-to-end communication services for applications.
- The transport layer is responsible for ensuring that the data transmitted by the application layer is delivered reliably, efficiently, and in the correct order to the destination application layer.
- One of the functions of the transport layer is error control, which involves detecting and correcting errors that may occur during data transmission.
- Error control is achieved through retransmission of the packet, which means sending the packet again if it is lost, delayed, corrupted, or duplicated .
- The transport layer uses two mechanisms to trigger retransmission of packets: duplicate acknowledgements (ACK) and retransmission timers.
- Duplicate ACKs are sent by the receiver when it detects a gap in the sequence of received packets, indicating that some packets are missing or out of order.
- Retransmission timers are set by the sender for each packet, and if the timer expires before receiving an ACK, the sender assumes that the packet is lost and retransmits it.
- The transport layer also provides congestion control, which involves preventing or removing congestion in the network, which can cause packet loss, delay, and reduced throughput.
- Congestion control can be open loop or closed loop, depending on whether it acts before or after congestion occurs.
- Open loop congestion control involves avoiding congestion by regulating the rate of data transmission or the number of packets in the network.
- Closed loop congestion control involves detecting congestion by measuring the network parameters, such as packet loss, delay, or queue length, and adjusting the data transmission accordingly.
- The transport layer can use different protocols to perform its functions, such as Transmission Control Protocol (TCP) or User Datagram Protocol (UDP).
- TCP is a reliable, connection-oriented, and stream-oriented protocol that provides error control, congestion control, flow control, and in-order delivery of data.
- UDP is an unreliable, connectionless, and datagram-oriented protocol that provides minimal error control, no congestion control, no flow control, and no guarantee of in-order delivery of data.
- The choice of protocol depends on the requirements of the application layer, such as reliability, efficiency, or real-time communication.