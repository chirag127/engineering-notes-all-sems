
### Flow Control for the Notes of the Unit 3 - Link Layer in the Subject of Computer Networks

1. Flow control is a mechanism used by a sender to regulate the amount of data sent over a network. It is used to prevent the sender from overwhelming the receiver with too much data, resulting in packet loss and network congestion.

2. Flow control can be implemented at the link layer, which is the layer of the OSI model responsible for establishing and maintaining connections between two nodes on a network.

3. One of the most common flow control mechanisms used at the link layer is sliding window flow control. This mechanism uses a sender window and a receiver window to regulate the amount of data that can be sent at any given time.

4. The sender window is a sequence of packets that the sender is allowed to send at any given time. The size of the window is determined by the receiver, and is usually adjusted based on the amount of available bandwidth.

5. The receiver window is a sequence of packets that the receiver is allowed to receive at any given time. The size of the window is determined by the sender, and is usually adjusted based on the amount of available bandwidth.

6. When the sender window is full, the sender must wait for the receiver to acknowledge the packets before sending any more. This ensures that the receiver is not overwhelmed with too much data.

7. Flow control at the link layer also helps to ensure that packets are delivered in the correct order. This is done by using a sequence number for each packet, which is used to determine the order in which the packets should be delivered.

8. Flow control is an important part of network communication, as it helps to ensure that data is delivered efficiently and reliably. It is used to prevent network congestion, packet loss, and out-of-order delivery of packets.