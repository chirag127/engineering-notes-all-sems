### Flow control for the notes of the Unit 3 - Link layer in the subject of Computer Networks

- Flow control is a technique that allows two stations working at different speeds to communicate with each other.
- Flow control regulates the amount of data that a sender can send before it waits for an acknowledgment from the receiver.
- Flow control prevents the sender from overwhelming the receiver with more data than it can handle.
- Flow control can be implemented at the data link layer using different methods, such as:
  - Stop-and-wait: The sender sends one frame at a time and waits for an acknowledgment before sending the next frame.
  - Sliding window: The sender can send multiple frames within a window size and wait for acknowledgments for all of them. The window size can be adjusted dynamically based on the feedback from the receiver.
  - Pause frame: The receiver can send a special frame to the sender to pause the transmission for a specified duration. This is used in full duplex Ethernet link segments.