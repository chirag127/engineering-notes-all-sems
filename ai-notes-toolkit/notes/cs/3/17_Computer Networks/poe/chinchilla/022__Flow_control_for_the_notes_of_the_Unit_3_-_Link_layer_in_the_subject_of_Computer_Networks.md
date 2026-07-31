### Flow Control for the notes of the Unit 3 - Link layer in the subject of Computer Networks

Flow control is an essential aspect that ensures the smooth transmission of data across a network. In this unit, we will learn about the different techniques used for flow control in the link layer of a computer network. Here are some important points to keep in mind:

1. Flow control is necessary to prevent the receiver from being overwhelmed by too much data sent by the sender.

2. The link layer provides two types of flow control: stop-and-wait and sliding window.

3. In stop-and-wait flow control, the sender sends a packet to the receiver and waits for an acknowledgment before sending the next packet. This technique is simple but inefficient because the sender has to wait for the acknowledgment before sending the next packet.

4. Sliding window flow control allows the sender to send multiple packets without waiting for an acknowledgment for each packet. The receiver sends an acknowledgment for the packets received, and the sender can continue sending packets up to a certain window size.

5. The receiver can also control the flow of data by sending a flow control message to the sender. The message indicates the amount of data the receiver can accept, and the sender adjusts its transmission accordingly.

6. Flow control can also be implemented using a credit-based system. In this system, the sender is assigned a certain number of credits, which represent the amount of data it can send. The sender sends data until it exhausts its credits, and then it waits for more credits from the receiver.

7. Flow control is important in networks with high traffic because it prevents congestion and ensures that data is transmitted efficiently.

8. Flow control is implemented in both wired and wireless networks.

In conclusion, flow control is a critical aspect of network communication, and it ensures that data is transmitted efficiently and without congestion. The link layer provides different techniques for flow control, including stop-and-wait and sliding window, and the receiver can also control the flow of data using flow control messages or a credit-based system. Understanding flow control is essential for anyone studying computer networks.