### Experiment 1.2 - Implementation of Sliding Window Protocol

The Sliding Window Protocol is a method used in computer networks to manage the flow of data between two devices. It is used to ensure that data is transmitted reliably and efficiently, without overwhelming the receiver or causing congestion in the network.

Here are the key points to remember when implementing the Sliding Window Protocol:

1. The sender maintains a window of data packets that it is allowed to send at any given time. The size of the window is determined by the receiver, based on its current capacity to process incoming data.

2. The receiver acknowledges the receipt of each packet by sending an acknowledgement (ACK) message back to the sender. The sender uses these ACK messages to update its window and determine which packets have been successfully received.

3. If a packet is lost or corrupted during transmission, the receiver will not send an ACK for that packet. The sender will eventually retransmit the lost packet, based on a timeout mechanism or the receipt of duplicate ACKs for other packets.

4. The sender may also use a technique called selective repeat, where it retransmits only the lost or corrupted packets, rather than retransmitting the entire window of data.

5. The Sliding Window Protocol can be implemented using either a go-back-N or a selective repeat mechanism. In a go-back-N implementation, the sender retransmits all packets in the window after a lost or corrupted packet is detected. In a selective repeat implementation, the sender retransmits only the lost or corrupted packets.

6. The Sliding Window Protocol is widely used in computer networks, including in the Transmission Control Protocol (TCP), which is the primary protocol used for transmitting data over the Internet. It is an effective way to manage the flow of data and ensure reliable transmission, even in the presence of network congestion or packet loss.