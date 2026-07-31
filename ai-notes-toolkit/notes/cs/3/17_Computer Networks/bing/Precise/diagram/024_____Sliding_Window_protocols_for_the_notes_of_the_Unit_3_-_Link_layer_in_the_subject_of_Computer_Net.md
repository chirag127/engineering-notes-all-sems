### Sliding Window Protocols

Sliding Window protocols are a method of flow control for data transmission in computer networks. They are used in the Link Layer of the OSI model. Here are some key points to remember about Sliding Window protocols:

1. Sliding Window protocols allow the sender to transmit multiple packets before receiving an acknowledgment from the receiver.
2. The sender maintains a window of packets that have been sent but not yet acknowledged. The size of the window determines how many packets can be sent before waiting for an acknowledgment.
3. The receiver also maintains a window of packets that it is ready to receive. The size of the receiver's window determines how many packets can be received before the receiver must send an acknowledgment.
4. When the sender receives an acknowledgment, it slides its window forward to include the next set of packets to be sent.
5. If a packet is lost or corrupted during transmission, the receiver will send a negative acknowledgment (NAK) to the sender. The sender will then retransmit the lost or corrupted packet.
6. Sliding Window protocols can be implemented using either Selective Repeat or Go-Back-N mechanisms.
7. Selective Repeat allows the sender to retransmit only the lost or corrupted packets, while Go-Back-N requires the sender to retransmit all packets from the lost or corrupted packet onwards.
8. Sliding Window protocols are commonly used in TCP, the main transport layer protocol used on the Internet.
