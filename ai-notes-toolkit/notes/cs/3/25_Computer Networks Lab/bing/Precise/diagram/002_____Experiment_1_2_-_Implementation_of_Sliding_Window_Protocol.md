### Experiment 1.2 - Implementation of Sliding Window Protocol

The Sliding Window Protocol is a method used in computer networks to manage the flow of data between two devices. It is used to ensure that data is transmitted reliably and efficiently.

1. The sender and receiver agree on a window size, which is the maximum number of packets that can be sent before an acknowledgment is received.
2. The sender sends packets within the window and waits for an acknowledgment from the receiver.
3. The receiver sends an acknowledgment for each packet received.
4. The sender moves the window forward by the number of acknowledged packets and sends more packets.
5. This process continues until all data has been transmitted.

The Sliding Window Protocol is an effective way to manage the flow of data and ensure reliable transmission. It is commonly used in computer networks and can be implemented in various ways, depending on the specific needs of the network.