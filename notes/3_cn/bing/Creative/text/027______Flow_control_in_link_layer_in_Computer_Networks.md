#### Flow control in link layer in Computer Networks

- Flow control is a technique that allows two stations working at different speeds to communicate with each other.
- It regulates the amount of data that a sender can send before receiving an acknowledgment from the receiver .
- It prevents the sender from overwhelming the receiver with too much data or frames.
- It can be implemented at the data link layer using two methods: stop-and-wait and sliding window.
- Stop-and-wait is a simple method where the sender sends one frame at a time and waits for an acknowledgment before sending the next frame.
- Sliding window is a more efficient method where the sender can send multiple frames within a window size without waiting for acknowledgments.
- The window size is the number of frames that can be sent or received at a time.
- The window size can be fixed or variable depending on the protocol.
- Ethernet flow control is an example of flow control at the data link layer using pause frames.
- Pause frames are special frames that can be sent by the receiver to the sender to request a temporary halt of data transmission.