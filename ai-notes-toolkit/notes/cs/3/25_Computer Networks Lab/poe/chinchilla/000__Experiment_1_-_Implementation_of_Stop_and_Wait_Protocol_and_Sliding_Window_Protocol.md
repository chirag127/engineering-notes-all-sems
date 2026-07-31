## Experiment 1 - Implementation of Stop and Wait Protocol and Sliding Window Protocol

In this experiment, we will learn about two important flow control techniques used in computer networks, Stop and Wait Protocol and Sliding Window Protocol. We will implement these protocols and evaluate their performance in terms of efficiency and reliability.

### Stop and Wait Protocol

Stop and Wait Protocol is a simple flow control technique used in communication systems, where the sender sends a packet of data to the receiver and waits for an acknowledgment (ACK) message from the receiver. If the sender receives an ACK message, it sends the next packet; otherwise, it re-transmits the same packet until it receives an ACK message.

The implementation of Stop and Wait Protocol involves the following steps:

1. The sender sends a packet of data to the receiver.
2. The sender starts a timer and waits for an ACK message from the receiver.
3. If the sender receives an ACK message within the timeout period, it sends the next packet of data. Otherwise, it re-transmits the same packet of data.
4. The receiver receives the packet of data and sends an ACK message back to the sender.
5. The sender receives the ACK message and stops the timer.

### Sliding Window Protocol

Sliding Window Protocol is a more advanced flow control technique used in communication systems, where the sender can send multiple packets of data to the receiver without waiting for an ACK message for each packet. The sender maintains a sliding window of packets that can be sent without waiting for an ACK message. The receiver sends an ACK message for all the packets it receives.

The implementation of Sliding Window Protocol involves the following steps:

1. The sender sends multiple packets of data to the receiver.
2. The sender maintains a sliding window that can hold a certain number of packets.
3. The sender waits for an ACK message for the first packet in the sliding window.
4. If the sender receives an ACK message for the first packet, it slides the window to the next packet and sends the new packet.
5. If the sender does not receive an ACK message for the first packet within the timeout period, it re-transmits the packet and resets the timer.
6. The receiver receives the packets and sends an ACK message for each packet.
7. The sender receives the ACK message and slides the window to the next packet.

In conclusion, the Stop and Wait Protocol and Sliding Window Protocol are two important flow control techniques used in communication systems to ensure efficient and reliable data transfer. By implementing these protocols, we can evaluate their performance and choose the most suitable technique for our requirements.