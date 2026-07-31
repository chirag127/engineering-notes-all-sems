
### Experiment 1.2 - Implementation of Sliding Window Protocol

1. The Sliding Window Protocol is a data link layer protocol that is used to ensure reliable communication between two devices. 
2. It is a type of stop-and-wait protocol, which means that the sender will wait for an acknowledgement from the receiver before sending the next packet. 
3. The protocol works by having the sender and receiver maintain a window of packets, where the sender can only send packets within the window and the receiver can only receive packets within the window. 
4. The sender will start by sending a packet and the receiver will send an acknowledgement for that packet. 
5. The sender will then send the next packet and the receiver will send an acknowledgement for that packet. 
6. This process continues until the window is full. 
7. The sender will then wait for the receiver to send an acknowledgement for the last packet, before sending the next packet. 
8. The receiver will send an acknowledgement for each packet received, and the sender will adjust the window size accordingly. 
9. The protocol ensures reliable communication by using acknowledgements and adjusting the window size.