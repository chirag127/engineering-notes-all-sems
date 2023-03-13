#### Flow control in link layer in Computer Networks

- Flow control is a technique that allows two stations working at different speeds to communicate with each other.
- It regulates the amount of data that a sender can send so that a fast sender does not overwhelm a slow receiver .
- It makes the sender wait until an acknowledgment is received from the receiver's end.
- Methods of flow control are Stop-and-wait, and Sliding window.
- Stop-and-wait is a simple method where the sender sends one frame and waits for an acknowledgment before sending the next frame.
- Sliding window is a more efficient method where the sender can send multiple frames without waiting for acknowledgments, but the number of frames is limited by a window size.
- Flow control on Ethernet can be implemented at the data link layer using pause frames, which are defined by the IEEE standard 802.3x.