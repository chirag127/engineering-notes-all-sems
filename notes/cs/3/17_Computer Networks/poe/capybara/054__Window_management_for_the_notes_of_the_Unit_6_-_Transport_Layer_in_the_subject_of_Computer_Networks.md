### Window Management for the Notes of Unit 6 - Transport Layer in the Subject of Computer Networks

Window Management is a crucial aspect of the Transport Layer of the OSI model, which is responsible for reliable data transfer between systems. Here are some essential points to help you understand the concept better:

- Window Management involves the use of a sliding window, which is a range of sequence numbers used by the sender and receiver to keep track of the data packets exchanged during a session.
- The sender assigns a sequence number to each data packet, and the receiver acknowledges the receipt of each packet by sending an acknowledgment (ACK) packet with the next expected sequence number back to the sender.
- The sender maintains a window size, which is the number of unacknowledged packets it can send at any given time. Once the receiver sends an ACK, the sender updates the window size and sends the next set of packets.
- The receiver also maintains a window size, which is the number of out-of-order packets it can buffer before it starts discarding them. Once the receiver sends an ACK, it updates the window size and sends the next expected sequence number to the sender.
- If the sender sends packets that exceed the receiver's window size, the receiver may send a negative acknowledgment (NAK) to request the missing packets. The sender can then retransmit those packets.
- Window Management helps prevent issues like packet loss, packet corruption, and congestion by ensuring that data packets are sent and received in an orderly and reliable fashion.

In conclusion, understanding Window Management is essential for anyone studying Computer Networks, as it is a critical aspect of the Transport Layer that ensures reliable data transfer between systems.