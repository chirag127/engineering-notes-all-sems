#### Flow control in link layer in Computer Networks

- Flow control is a technique that allows two stations working at different speeds to communicate with each other.
- It regulates the amount of data that a sender can send before receiving an acknowledgment from the receiver .
- It prevents the sender from overwhelming the receiver with too many frames or data packets.
- There are two main methods of flow control in the link layer: stop-and-wait and sliding window.
- Stop-and-wait is a simple method where the sender sends one frame at a time and waits for an acknowledgment from the receiver before sending the next frame.
- Sliding window is a more efficient method where the sender can send multiple frames without waiting for acknowledgments, as long as the number of frames does not exceed the window size agreed by both stations.
- The window size is the number of frames that can be sent or received at a time.
- The sender maintains a send window that indicates the range of frames that can be sent, and the receiver maintains a receive window that indicates the range of frames that can be accepted.
- The sender and the receiver update their windows based on the acknowledgments and feedback they receive from each other.
- Flow control can also be implemented at the Ethernet level using pause frames, which are special frames that can be sent by the receiver to the sender to temporarily stop the transmission of data.