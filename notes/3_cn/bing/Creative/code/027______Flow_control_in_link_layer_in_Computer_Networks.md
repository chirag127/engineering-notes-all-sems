#### Flow control in link layer in Computer Networks

Flow control is a technique that allows two stations working at different speeds to communicate with each other. It is a set of measures taken to regulate the amount of data that a sender can send so that a fast sender does not overwhelm a slow receiver.

Flow control is an essential function of the data link layer. It determines the amount of data that a sender can send. It makes the sender wait until an acknowledgment is received from the receiver’s end.

There are two main methods of flow control in data link layer:

- Stop-and-wait: In this method, the sender sends one frame at a time and waits for an acknowledgment from the receiver before sending the next frame. This method is simple but inefficient, as it wastes the bandwidth and time during the waiting period.
- Sliding window: In this method, the sender can send multiple frames without waiting for acknowledgments, but it has to keep track of a window size that indicates how many frames can be sent at a time. The window size is determined by the receiver's buffer capacity and the network conditions. The receiver sends acknowledgments for the received frames and also updates the window size for the sender. This method is more efficient and utilizes the bandwidth and time better than stop-and-wait .

Flow control on Ethernet can be implemented at the data link layer using the pause frame, which is defined by the IEEE standard 802.3x. The pause frame is a special frame that can be sent by the receiver to the sender to request a temporary halt of data transmission. The pause frame contains a parameter that specifies the duration of the pause. The sender has to respect the pause request and stop sending data until the pause time expires or a resume frame is received.