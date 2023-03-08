 Here is the content written in markdown format on the topic ### etransmission  in transport layer:

### Etransmission in Transport Layer

- Etransmission refers to the process of retransmitting data packets that get corrupted or lost during transmission in the transport layer.
- The transport layer protocols like TCP provide reliable data transmission using etransmission.
- The steps involved in etransmission are:
1. The sender sends data packets to the receiver.
2. The receiver sends back acknowledgement (ACK) packets for the data packets received.
3. If the sender does not receive ACK for a sent data packet within a specified time period, it retransmits the data packet.
4. This process of sending data packets, waiting for ACK and retransmitting is repeated until all packets are received correctly at the receiver.
5. Etransmission helps in achieving reliable data transmission over unreliable networks.

Advantages:
- Achieves reliable data transmission over unreliable networks.
- Ensures all data packets are received correctly at the receiver.

Disadvantages:
- Increases network traffic due to extra ACK and retransmitted packets.
- Increases latency as packets have to be buffered and retransmitted.

Examples: TCP provides reliable data transmission using e-transmission.

Applications: Used in file transfer, email, etc. where reliable data transmission is required.

[Diagrams and codes can be added here to illustrate the concept]

Hope this helps!